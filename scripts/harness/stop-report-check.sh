#!/usr/bin/env bash
# Hook Stop du harnais Bastion.
# Si des fichiers ont changé (non commités, ou commités sur la branche depuis origin/main,
# ou main à défaut),
# l'un d'eux doit être un rapport dans docs/reviews/. Sinon l'arrêt est bloqué (code 2)
# et Claude reçoit le rappel. Un seul rappel : si Claude continue déjà à cause d'un
# hook Stop (stop_hook_active), on le laisse s'arrêter pour éviter une boucle.

entree=$(cat)
if printf '%s' "$entree" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

# Base : origin/main de préférence, sinon main. Le hook ne lance pas « git fetch » :
# origin/main peut donc être périmée si « git fetch origin main » n'a pas été fait en début de lot.
base=$(git merge-base HEAD origin/main 2>/dev/null || git merge-base HEAD main 2>/dev/null)
changements=$(
  git -c core.quotePath=false status --porcelain --untracked-files=all | cut -c4-
  if [ -n "$base" ]; then
    git -c core.quotePath=false diff --name-only "$base" HEAD
  else
    # Sans main (dépôt neuf) : fichiers des commits propres à la branche courante,
    # c'est-à-dire absents des autres branches locales.
    branche=$(git symbolic-ref --short -q HEAD)
    git -c core.quotePath=false log --name-only --format= HEAD --not ${branche:+--exclude="$branche"} --branches 2>/dev/null
  fi
)

[ -z "$changements" ] && exit 0
# Accepte aussi un renommage (« ancien -> nouveau ») et un chemin entre guillemets.
printf '%s\n' "$changements" | grep -Eq '(^|-> )"?docs/reviews/' && exit 0

echo "Harnais Bastion : Aucun rapport du lot n'a été ajouté ou modifié dans docs/reviews/ alors que des fichiers ont changé sur cette branche (commités ou non). Si le mandat est terminé, rédigez son rapport avec les contrôles exécutés et non exécutés ; sinon indiquez explicitement que le mandat est incomplet ou en attente d'arbitrage." >&2
exit 2
