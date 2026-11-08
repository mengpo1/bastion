#!/usr/bin/env bash
# Tests des hooks du harnais : effets attendus ET limites connues.
# Usage : bash scripts/harness/test-hooks.sh   (code de sortie 1 si un test échoue)
# Résultats possibles d'un hook : autorise | demande (ask) | bloque (code 2).

ici=$(cd "$(dirname "$0")" && pwd)
PRE="$ici/pre-tool-use.sh"
STOP="$ici/stop-report-check.sh"
total=0
echecs=0

# verifier <attendu> <description> <hook> <json> [dossier où lancer le hook]
verifier() {
  dossier=${5:-$PWD}
  sortie=$(cd "$dossier" && printf '%s' "$4" | CLAUDE_PROJECT_DIR="$dossier" bash "$3" 2>/dev/null)
  code=$?
  case "$code" in
    2) obtenu=bloque ;;
    0) case "$sortie" in
         '') obtenu=autorise ;;
         *'"permissionDecision":"ask"'*) obtenu=demande ;;
         *) obtenu="sortie inattendue" ;;
       esac ;;
    *) obtenu="code $code" ;;
  esac
  total=$((total + 1))
  if [ "$obtenu" = "$1" ]; then
    echo "OK     [$1] $2"
  else
    echo "ÉCHEC  [attendu $1, obtenu $obtenu] $2"
    echecs=$((echecs + 1))
  fi
}

# Construit l'entrée JSON d'un appel d'outil (les arguments sont déjà échappés pour JSON).
bash_json()  { printf '{"session_id":"test","hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"%s","description":"test"}}' "$1"; }
ecrit_json() { printf '{"session_id":"test","hook_event_name":"PreToolUse","tool_name":"%s","tool_input":{"%s":"%s","content":"x"}}' "$1" "${3:-file_path}" "$2"; }
outil_json() { printf '{"session_id":"test","hook_event_name":"PreToolUse","tool_name":"%s","tool_input":{"owner":"o","repo":"r"}}' "$1"; }
stop_json()  { printf '{"session_id":"test","hook_event_name":"Stop","stop_hook_active":%s}' "$1"; }

# Dépôts Git temporaires
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
g() { git -C "$1" -c user.name=test -c user.email=test@example.invalid -c commit.gpgsign=false "${@:2}"; }
nouveau_depot() { git init -q -b main "$1" && g "$1" commit -q --allow-empty -m init; }
nouveau_depot "$tmp/main"
nouveau_depot "$tmp/branche"
g "$tmp/branche" checkout -q -b chore/test
echo "code" > "$tmp/branche/fichier.cs"
echo "notes" > "$tmp/branche/notes.md"
g "$tmp/branche" add fichier.cs notes.md
g "$tmp/branche" commit -q -m "ajout"
git init -q -b main "$tmp/neuf"                 # main pas encore créé (aucun commit)
# Dépôts sans branche main, comme Bastion avant son initialisation.
git init -q -b chore/lot-a "$tmp/sansmain"
mkdir -p "$tmp/sansmain/docs/reviews"
echo "rapport A" > "$tmp/sansmain/docs/reviews/LOT-A.md"
echo "a" > "$tmp/sansmain/a.cs"
g "$tmp/sansmain" add docs a.cs
g "$tmp/sansmain" commit -q -m "lot A avec rapport"
git init -q -b chore/seul "$tmp/seul"
echo "s" > "$tmp/seul/s.cs"
g "$tmp/seul" add s.cs
g "$tmp/seul" commit -q -m "lot sans rapport"

echo "== PreToolUse : effets =="
verifier autorise "écriture d'un fichier source" "$PRE" "$(ecrit_json Write /depot/src/Bastion.Simulation/Exemple.cs)"
verifier autorise "commande ordinaire (dotnet test)" "$PRE" "$(bash_json 'dotnet test')"
verifier autorise "lecture d'un fichier protégé (cat CLAUDE.md)" "$PRE" "$(bash_json 'cat CLAUDE.md 2>/dev/null')"
verifier autorise "git merge-base (lecture seule)" "$PRE" "$(bash_json 'git diff $(git merge-base main HEAD)')"
verifier autorise "commit sur une branche de travail" "$PRE" "$(bash_json 'git commit -m test')" "$tmp/branche"
verifier autorise "plan de Claude dans ~/.claude/plans/" "$PRE" "$(ecrit_json Write /home/u/.claude/plans/plan.md)"
verifier autorise "lecture GitHub par MCP (get_file_contents)" "$PRE" "$(outil_json mcp__github__get_file_contents)"
verifier autorise "lecture GitHub par MCP (pull_request_read)" "$PRE" "$(outil_json mcp__github__pull_request_read)"
verifier demande "Edit du registre de gameplay" "$PRE" "$(ecrit_json Edit /depot/docs/gameplay/GAMEPLAY-DECISIONS.md)"
verifier demande "nouveau fichier dans docs/gameplay/" "$PRE" "$(ecrit_json Write /depot/docs/gameplay/G-001.md)"
verifier demande "Write de .claude/settings.json" "$PRE" "$(ecrit_json Write /depot/.claude/settings.json)"
verifier demande "Write de ~/.claude/settings.json" "$PRE" "$(ecrit_json Write /home/u/.claude/settings.json)"
verifier demande "Write d'un registre, chemin Windows" "$PRE" "$(ecrit_json Write 'C:\\depot\\docs\\decisions\\TECHNICAL-DECISIONS.md')"
verifier demande "NotebookEdit dans docs/mandates/" "$PRE" "$(ecrit_json NotebookEdit /depot/docs/mandates/n.ipynb notebook_path)"
verifier demande "redirection shell vers un registre" "$PRE" "$(bash_json 'echo x >> docs/references/OXCE-BASELINE.md')"
verifier demande "git push" "$PRE" "$(bash_json 'git push -u origin chore/test')"
verifier demande "git pull" "$PRE" "$(bash_json 'git pull origin main')"
verifier demande "git merge" "$PRE" "$(bash_json 'git merge main')"
verifier demande "gh pr merge" "$PRE" "$(bash_json 'gh pr merge 3 --squash')"
verifier demande "fusion GitHub par MCP (merge_pull_request)" "$PRE" "$(outil_json mcp__github__merge_pull_request)"
verifier demande "écriture GitHub par MCP (push_files)" "$PRE" "$(outil_json mcp__github__push_files)"
verifier bloque "rm -rf" "$PRE" "$(bash_json 'rm -rf build')"
verifier bloque "rm -fr sur une 2e ligne" "$PRE" "$(bash_json 'git status\nrm -fr src')"
verifier bloque "git reset --hard" "$PRE" "$(bash_json 'git reset --hard HEAD~1')"
verifier bloque "git clean -fd" "$PRE" "$(bash_json 'git clean -fd')"
verifier bloque "git push --force" "$PRE" "$(bash_json 'git push --force origin chore/test')"
verifier bloque "git push -f" "$PRE" "$(bash_json 'git push -f origin chore/test')"
verifier bloque "git branch -D" "$PRE" "$(bash_json 'git branch -D chore/test')"
verifier bloque "commit sur main" "$PRE" "$(bash_json 'git commit -m test')" "$tmp/main"
verifier bloque "premier commit sur main (dépôt neuf)" "$PRE" "$(bash_json 'git commit -m test')" "$tmp/neuf"

echo "== PreToolUse : limites connues =="
verifier autorise "LIMITE rm --recursive non détecté" "$PRE" "$(bash_json 'rm --recursive build')"
verifier autorise "LIMITE écriture via python non détectée" "$PRE" "$(bash_json "python3 -c \\\"open('CLAUDE.md','w')\\\"")"
verifier autorise "LIMITE code de gameplay dans src/ non détecté" "$PRE" "$(ecrit_json Write /depot/src/Bastion.Simulation/Degats.cs)"
verifier autorise "LIMITE checkout main puis commit dans la même commande" "$PRE" "$(bash_json 'git checkout main && git commit -m x')" "$tmp/branche"
verifier demande "LIMITE faux positif : message de commit citant git push" "$PRE" "$(bash_json 'git commit -m \"interdire git push\"')" "$tmp/branche"
verifier bloque "LIMITE faux positif bloquant : recherche du texte rm -rf" "$PRE" "$(bash_json 'grep -rn \"rm -rf\" scripts/')"

echo "== Stop : effets et limites =="
verifier autorise "dépôt propre sur main" "$STOP" "$(stop_json false)" "$tmp/main"
verifier bloque "branche modifiée sans rapport" "$STOP" "$(stop_json false)" "$tmp/branche"
verifier autorise "LIMITE un seul rappel (stop_hook_active)" "$STOP" "$(stop_json true)" "$tmp/branche"
mkdir -p "$tmp/branche/docs/reviews"
g "$tmp/branche" mv notes.md "docs/reviews/LOT 0C rapport.md"
verifier autorise "rapport ajouté par renommage, nom avec espace" "$STOP" "$(stop_json false)" "$tmp/branche"
g "$tmp/branche" mv "docs/reviews/LOT 0C rapport.md" notes.md
echo "rapport" > "$tmp/branche/docs/reviews/LOT-TEST.md"
verifier autorise "branche modifiée avec rapport dans docs/reviews/" "$STOP" "$(stop_json false)" "$tmp/branche"
echo "x" > "$tmp/main/note.txt"
verifier bloque "modification non commitée sur main sans rapport" "$STOP" "$(stop_json false)" "$tmp/main"

echo "== Stop : dépôt sans branche main =="
verifier autorise "sans main : branche avec rapport commité, arbre propre" "$STOP" "$(stop_json false)" "$tmp/sansmain"
verifier bloque "sans main : branche commitée sans rapport, arbre propre" "$STOP" "$(stop_json false)" "$tmp/seul"
g "$tmp/sansmain" checkout -q -b chore/lot-b
echo "b" > "$tmp/sansmain/b.cs"
g "$tmp/sansmain" add b.cs
g "$tmp/sansmain" commit -q -m "lot B sans rapport"
verifier bloque "sans main : nouvelle branche sans rapport (celui du lot A ne compte pas)" "$STOP" "$(stop_json false)" "$tmp/sansmain"
echo "c" > "$tmp/sansmain/c.cs"
verifier bloque "sans main : modification non commitée sans rapport" "$STOP" "$(stop_json false)" "$tmp/sansmain"
echo "rapport B" > "$tmp/sansmain/docs/reviews/LOT-B.md"
verifier autorise "sans main : rapport non commité présent" "$STOP" "$(stop_json false)" "$tmp/sansmain"
# Limite : si la branche d'origine est supprimée, son rapport redevient « propre » à la branche.
mkdir -p "$tmp/seul/docs/reviews"
echo "rapport" > "$tmp/seul/docs/reviews/SEUL.md"
g "$tmp/seul" add docs
g "$tmp/seul" commit -q -m "rapport"
g "$tmp/seul" checkout -q -b chore/suite
echo "t" > "$tmp/seul/t.cs"
g "$tmp/seul" add t.cs
g "$tmp/seul" commit -q -m "suite sans rapport"
g "$tmp/seul" branch -q -D chore/seul
verifier autorise "LIMITE sans main : branche d'origine supprimée, son rapport compte" "$STOP" "$(stop_json false)" "$tmp/seul"

echo "== Stop : référence origin/main =="
# main locale périmée (C0) ; origin/main à jour (C1, qui contient le rapport d'un lot déjà fusionné).
git init -q -b main "$tmp/perime"
g "$tmp/perime" commit -q --allow-empty -m "C0"
c0=$(git -C "$tmp/perime" rev-parse HEAD)
mkdir -p "$tmp/perime/docs/reviews"
echo "rapport A" > "$tmp/perime/docs/reviews/LOT-A.md"
g "$tmp/perime" add docs
g "$tmp/perime" commit -q -m "C1 : lot A fusionné avec son rapport"
git -C "$tmp/perime" update-ref refs/remotes/origin/main HEAD
g "$tmp/perime" checkout -q -b chore/lot-b
git -C "$tmp/perime" branch -q -f main "$c0"
verifier autorise "branche identique à origin/main : pas de faux blocage" "$STOP" "$(stop_json false)" "$tmp/perime"
echo "b" > "$tmp/perime/b.cs"
g "$tmp/perime" add b.cs
g "$tmp/perime" commit -q -m "lot B sans rapport"
verifier bloque "main locale périmée, origin/main à jour : branche sans rapport" "$STOP" "$(stop_json false)" "$tmp/perime"
total=$((total + 1))
message=$(cd "$tmp/perime" && printf '%s' "$(stop_json false)" | CLAUDE_PROJECT_DIR="$tmp/perime" bash "$STOP" 2>&1 >/dev/null)
case "$message" in
  *"Aucun rapport du lot"*"incomplet ou en attente d'arbitrage"*)
    echo "OK     [message] le rappel vise le rapport du lot et demande de déclarer un mandat incomplet" ;;
  *) echo "ÉCHEC  [message] rappel inattendu : $message"; echecs=$((echecs + 1)) ;;
esac
echo "rapport B" > "$tmp/perime/docs/reviews/LOT-B.md"
verifier autorise "main locale périmée, origin/main à jour : rapport présent" "$STOP" "$(stop_json false)" "$tmp/perime"

echo "== Traçabilité simulation (contrôle CI des PR) =="
TRACE="$ici/check-simulation-trace.sh"
D="$tmp/trace"
# verifier_trace <attendu ok|echec> <description du test> <texte de la description de PR>
# Lancé dans le dépôt d'essai $D, sur sa branche courante, avec main comme base.
verifier_trace() {
  printf '%s' "$3" > "$tmp/description-pr.txt"
  (cd "$D" && bash "$TRACE" main "$tmp/description-pr.txt" > /dev/null 2>&1)
  code=$?
  case "$code" in 0) obtenu=ok ;; 1) obtenu=echec ;; *) obtenu="code $code" ;; esac
  total=$((total + 1))
  if [ "$obtenu" = "$1" ]; then
    echo "OK     [$1] $2"
  else
    echo "ÉCHEC  [attendu $1, obtenu $obtenu] $2"
    echecs=$((echecs + 1))
  fi
}
git init -q -b main "$D"
mkdir -p "$D/src/Bastion.Simulation" "$D/scripts/harness" "$D/docs/gameplay"
echo "class A {}" > "$D/src/Bastion.Simulation/A.cs"
echo "x" > "$D/scripts/harness/x.sh"
echo "doc" > "$D/README.md"
# Registre d'essai : données de test du dépôt temporaire, pas le registre du projet.
cat > "$D/docs/gameplay/GAMEPLAY-DECISIONS.md" <<'FIN'
# Registre d'essai

### MEC-0001 — Fiche d'essai acceptée

| Champ | Valeur |
|---|---|
| Décision du propriétaire | acceptée — essai — 2026-11-08 |

### MEC-0002 — Fiche d'essai refusée

| Champ | Valeur |
|---|---|
| Décision du propriétaire | refusée — essai — 2026-11-08 |

### MEC-0003 — Fiche recopiée du gabarit sans être remplie

| Champ | Valeur |
|---|---|
| Décision du propriétaire | acceptée / refusée / reportée — preuve de validation explicite — date |
FIN
g "$D" add .
g "$D" commit -q -m "base"
g "$D" checkout -q -b doc
echo "doc 2" >> "$D/README.md"
g "$D" commit -qam "doc"
verifier_trace ok "PR sans changement de simulation, sans déclaration" ""
g "$D" checkout -q main
g "$D" checkout -q -b harnais
echo "y" >> "$D/scripts/harness/x.sh"
g "$D" commit -qam "harnais"
verifier_trace ok "PR ne touchant que le harnais, sans déclaration" ""
g "$D" checkout -q main
g "$D" checkout -q -b sim
echo "// changement" >> "$D/src/Bastion.Simulation/A.cs"
g "$D" commit -qam "sim"
verifier_trace echec "simulation modifiée, description vide" ""
verifier_trace echec "simulation modifiée, texte sans déclaration" "Corrige un détail."
verifier_trace echec "déclaration sans justification" "Traçabilité simulation : TECHNIQUE — "
verifier_trace echec "déclaration mal formée (type inconnu)" "Traçabilité simulation : TECH — détail"
verifier_trace echec "justification laissée au gabarit" "Traçabilité simulation : TECHNIQUE — <justification précise>"
verifier_trace echec "MEC inexistant" "Traçabilité simulation : MEC-0009 — essai"
verifier_trace echec "MEC refusé" "Traçabilité simulation : MEC-0002 — essai"
verifier_trace echec "MEC recopié du gabarit, non décidé" "Traçabilité simulation : MEC-0003 — essai"
verifier_trace echec "une déclaration valide et une invalide" $'Traçabilité simulation : TECHNIQUE — renommage interne\nTraçabilité simulation : MEC-0009 — essai'
verifier_trace ok "MEC accepté (données d'essai)" "Traçabilité simulation : MEC-0001 — essai"
verifier_trace ok "LIMITE TECHNIQUE justifié : contrôle syntaxique seulement" "Traçabilité simulation : TECHNIQUE — renommage interne sans effet de jeu"
verifier_trace ok "fins de ligne Windows dans la description" $'Résumé\r\n\r\nTraçabilité simulation : TECHNIQUE — renommage interne\r\n'
g "$D" checkout -q main
g "$D" checkout -q -b suppression
g "$D" rm -q src/Bastion.Simulation/A.cs
g "$D" commit -qm "suppression"
verifier_trace echec "fichier de simulation supprimé, sans déclaration" ""

echo "== $total tests, $echecs échec(s) =="
[ "$echecs" -eq 0 ]
