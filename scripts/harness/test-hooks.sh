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
git init -q -b chore/x "$tmp/sansmain"          # dépôt sans branche main
mkdir -p "$tmp/sansmain/docs/reviews"
echo "ancien" > "$tmp/sansmain/docs/reviews/ANCIEN.md"
g "$tmp/sansmain" add docs
g "$tmp/sansmain" commit -q -m "ancien rapport"

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
verifier autorise "LIMITE sans main : commits non contrôlés" "$STOP" "$(stop_json false)" "$tmp/sansmain"
echo "x" > "$tmp/sansmain/nouveau.cs"
verifier bloque "sans main : ancien rapport commité, nouvelle modification" "$STOP" "$(stop_json false)" "$tmp/sansmain"

echo "== $total tests, $echecs échec(s) =="
[ "$echecs" -eq 0 ]
