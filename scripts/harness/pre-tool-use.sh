#!/usr/bin/env bash
# Hook PreToolUse du harnais Bastion.
# Entrée : l'appel d'outil en JSON sur stdin. Réponse :
#   - code 2 + message      : appel BLOQUÉ (commande destructive, commit sur main) ;
#   - JSON "ask" sur stdout : Claude Code demande l'accord du propriétaire
#                             (écriture d'un fichier protégé, git push / merge / rebase) ;
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

# Fichiers de gouvernance et du harnais.
PROTEGES='GAMEPLAY-DECISIONS\.md|TECHNICAL-DECISIONS\.md|OXCE-BASELINE\.md|CLAUDE\.md|docs/mandates/|\.claude/|scripts/harness/|\.github/workflows/'
# Commandes destructives (liste courte). \\n : retour à la ligne échappé dans le JSON.
DESTRUCTIF='(^|[^[:alnum:]_.-]|\\n)rm[[:space:]]+-[[:alnum:]]*[rR]|git[[:space:]]+reset[[:space:]]+--hard|git[[:space:]]+clean[[:space:]]+-[[:alnum:]]*f|git[[:space:]]+branch[[:space:]]+-D|git[[:space:]]+push[[:space:]].*(--force|[[:space:]]-f([[:space:]]|\\|$))'
# Indices d'écriture dans une commande shell (2>&1 et 2>/dev/null ne comptent pas).
ECRITURE='(^|[^0-9])>|tee[[:space:]]|sed[[:space:]]+-i|(^|[[:space:]])(mv|cp|rm|truncate)[[:space:]]'

case "$(champ tool_name)" in
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
       [ "$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" = main ]; then
      bloquer "commit direct sur main"
    fi
    if printf '%s' "$cmd" | grep -Eq 'git[[:space:]]+(push|merge|rebase)'; then
      demander "git push, merge ou rebase"
    fi
    if printf '%s' "$cmd" | grep -Eq "$PROTEGES" && printf '%s' "$cmd" | grep -Eq "$ECRITURE"; then
      demander "commande shell pouvant modifier un fichier protégé"
    fi
    ;;
esac
exit 0
