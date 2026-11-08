#!/usr/bin/env bash
# Hook PreToolUse du harnais Bastion.
# Entrée : l'appel d'outil en JSON sur stdin. Réponse :
#   - code 2 + message      : appel BLOQUÉ (commande destructive, commit sur main) ;
#   - JSON "ask" sur stdout : Claude Code demande l'accord du propriétaire
#                             (fichier protégé, git push / pull / merge / rebase,
#                             écriture sur GitHub) ;
#   - code 0 sans sortie    : appel autorisé.
# Détection par motifs de texte, non exhaustive : voir scripts/harness/README.md.

entree=$(cat)

# Valeur d'un champ texte du JSON (laissée échappée). Sans jq, pour rester portable.
champ() {
  printf '%s' "$entree" |
    sed -nE 's/.*"'"$1"'"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p' | head -n 1
}

bloquer() {
  echo "Harnais Bastion — BLOQUÉ : $1. Voir CLAUDE.md." >&2
  exit 2
}

demander() {
  raison=$(printf '%s' "$1" | tr -d '"\\')
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Harnais Bastion : %s. Accord explicite du propriétaire requis."}}\n' "$raison"
  exit 0
}

# Registres, mandats, règles et harnais.
PROTEGES='docs/(gameplay|decisions|references|mandates)/|CLAUDE\.md|\.claude/settings[^/]*\.json|scripts/harness/|\.github/workflows/'
# Commandes destructives (liste courte). \\n : retour à la ligne échappé dans le JSON.
DESTRUCTIF='(^|[^[:alnum:]_.-]|\\n)rm[[:space:]]+-[[:alnum:]]*[rR]|git[[:space:]]+reset[[:space:]]+--hard|git[[:space:]]+clean[[:space:]]+-[[:alnum:]]*f|git[[:space:]]+branch[[:space:]]+-D|git[[:space:]]+push.*[[:space:]](--force|-f([[:space:]]|\\|$))'
# Publication et fusion.
PUBLICATION='git[[:space:]]+(push|pull|merge|rebase)([[:space:]]|\\|$)|gh[[:space:]]+pr[[:space:]]+merge'
# Indices d'écriture dans une commande shell (2>&1 et 2>/dev/null ne comptent pas).
ECRITURE='(^|[^0-9])>|tee[[:space:]]|sed[[:space:]]+-i|(^|[[:space:]])(mv|cp|rm|truncate)[[:space:]]'

outil=$(champ tool_name)
case "$outil" in
  Write|Edit|MultiEdit|NotebookEdit)
    chemin=$(champ file_path)
    [ -n "$chemin" ] || chemin=$(champ notebook_path)
    chemin=$(printf '%s' "$chemin" | sed 's#\\\\#/#g')  # chemins Windows
    if printf '%s' "$chemin" | grep -Eq "$PROTEGES"; then
      demander "écriture dans un fichier protégé ($chemin)"
    fi
    ;;
  Bash)
    cmd=$(champ command)
    if printf '%s' "$cmd" | grep -Eq "$DESTRUCTIF"; then
      bloquer "commande destructive"
    fi
    if printf '%s' "$cmd" | grep -Eq 'git[[:space:]]+commit' &&
       [ "$(git symbolic-ref --short -q HEAD 2>/dev/null)" = main ]; then
      bloquer "commit direct sur main"
    fi
    if printf '%s' "$cmd" | grep -Eq "$PUBLICATION"; then
      demander "git push, pull, merge, rebase ou gh pr merge"
    fi
    if printf '%s' "$cmd" | grep -Eq "$PROTEGES" && printf '%s' "$cmd" | grep -Eq "$ECRITURE"; then
      demander "commande shell pouvant modifier un fichier protégé"
    fi
    ;;
  mcp__github__*)
    # Lecture (get_, list_, search_, *_read, *_get, *_list) : libre. Le reste écrit sur GitHub.
    if ! printf '%s' "$outil" | grep -Eq '^mcp__github__(get_|list_|search_)|_(read|get|list)$'; then
      demander "écriture sur GitHub ($outil)"
    fi
    ;;
esac
exit 0
