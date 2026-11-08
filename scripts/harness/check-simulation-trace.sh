#!/usr/bin/env bash
# Contrôle de traçabilité des changements de simulation (CI, pull requests).
# Usage : check-simulation-trace.sh <base> <fichier contenant la description de la PR>
#
# Si la PR ajoute, modifie, renomme ou supprime un fichier de src/Bastion.Simulation/,
# sa description doit contenir au moins une ligne :
#   Traçabilité simulation : TECHNIQUE — <justification>
#   Traçabilité simulation : MEC-NNNN — <justification>   (fiche existante, décision « acceptée »)
# Contrôle syntaxique seulement : il ne prouve pas l'absence de changement de gameplay.
# La description est une donnée non fiable : elle est lue, jamais exécutée ni interpolée.

base=$1
description=$2
registre=docs/gameplay/GAMEPLAY-DECISIONS.md
motif='^[[:space:]]*Traçabilité simulation[[:space:]]*:[[:space:]]*(TECHNIQUE|MEC-[0-9]{4})[[:space:]]+(—|–|-)[[:space:]]+(.*[^[:space:]])[[:space:]]*$'

erreur() {
  echo "${GITHUB_ACTIONS:+::error::}Traçabilité simulation : $1" >&2
  exit 1
}

fichiers=$(git diff --name-only --no-renames "$base" HEAD -- src/Bastion.Simulation/) ||
  erreur "comparaison impossible avec la base « $base »."
if [ -z "$fichiers" ]; then
  echo "Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise."
  exit 0
fi
echo "Fichiers de simulation modifiés :"
printf '%s\n' "$fichiers" | sed 's/^/  /'

lignes=$(tr -d '\r' < "$description" | grep -aE '^[[:space:]]*Traçabilité simulation[[:space:]]*:')
[ -n "$lignes" ] || erreur "déclaration absente de la description de la PR. Ajoutez une ligne « Traçabilité simulation : TECHNIQUE — <justification> » ou « Traçabilité simulation : MEC-NNNN — <justification> »."

while IFS= read -r ligne; do
  type=$(printf '%s\n' "$ligne" | sed -nE "s/$motif/\1/p")
  justification=$(printf '%s\n' "$ligne" | sed -nE "s/$motif/\3/p")
  [ -n "$type" ] || erreur "déclaration mal formée ou sans justification : « $ligne »."
  case "$justification" in
    \<*\>) erreur "justification à compléter : « $justification »." ;;
  esac
  if [ "$type" = TECHNIQUE ]; then
    echo "Déclaration TECHNIQUE reconnue (contrôle syntaxique). Elle ne prouve pas l'absence de changement de gameplay : la revue doit le vérifier."
    continue
  fi
  # Fiche MEC : bloc qui commence par « ### MEC-NNNN » jusqu'au titre suivant.
  fiche=$(awk -v id="$type" '$0 ~ "^### " id "([^0-9]|$)" {f = 1; next} f && /^### / {f = 0} f' "$registre" 2>/dev/null)
  [ -n "$fiche" ] || erreur "$type : fiche absente de $registre."
  decision=$(printf '%s\n' "$fiche" | grep -aE '^\|[[:space:]]*Décision du propriétaire[[:space:]]*\|' | head -n 1 | cut -d'|' -f3)
  case "$decision" in
    *refusée* | *reportée*) erreur "$type : la décision du propriétaire n'est pas « acceptée »." ;;
  esac
  printf '%s' "$decision" | grep -qE '^[[:space:]]*acceptée' ||
    erreur "$type : la décision du propriétaire n'est pas « acceptée »."
  echo "Déclaration $type reconnue (fiche présente, décision « acceptée »). La revue doit vérifier la décision, ses preuves et son périmètre."
done <<< "$lignes"
exit 0
