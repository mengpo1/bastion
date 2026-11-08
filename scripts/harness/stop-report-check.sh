#!/usr/bin/env bash
# Hook Stop du harnais Bastion.
# Si des fichiers ont changé (non commités, ou commités sur la branche depuis main),
# l'un d'eux doit être un rapport dans docs/reviews/. Sinon l'arrêt est bloqué (code 2)
# et Claude reçoit le rappel. Un seul rappel : si Claude continue déjà à cause d'un
# hook Stop (stop_hook_active), on le laisse s'arrêter pour éviter une boucle.

entree=$(cat)
if printf '%s' "$entree" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

base=$(git merge-base HEAD main 2>/dev/null || git merge-base HEAD origin/main 2>/dev/null)
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

echo "Harnais Bastion : des fichiers ont changé sans rapport dans docs/reviews/. Si le mandat est terminé, rédigez son rapport avant de terminer, en y indiquant les contrôles non exécutés. Si vous attendez une réponse du propriétaire, dites-le et arrêtez-vous." >&2
exit 2
