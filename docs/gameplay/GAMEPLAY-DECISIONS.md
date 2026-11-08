# Registre des mécaniques de gameplay

Registre protégé (spécification v0.2, §3.1). Une fiche n'autorise un changement de comportement qu'avec une **décision du propriétaire « acceptée »**, explicite, datée et prouvée. Claude Code n'y écrit qu'avec cet accord.

**Aucune mécanique n'est enregistrée à ce jour.** Aucune mécanique de jeu ne peut donc être implémentée.

## Règles

- **Classe** (nature de la mécanique) et **état d'implémentation** (avancement) sont deux champs distincts : ne pas les confondre.
- `MODIFICATION-PROPOSEE` ou `A-VERIFIER` : n'autorise **aucun** changement de comportement.
- `MODIFICATION-VALIDEE` : n'autorise **que** le périmètre décrit et approuvé.
- Une idée évoquée dans une conversation n'est pas une décision validée.

| Classe | Signification |
|---|---|
| `OXCE-REFERENCE` | Comportement de référence d'OXCE à reproduire |
| `MODIFICATION-PROPOSEE` | Modification soumise au propriétaire, non validée |
| `MODIFICATION-VALIDEE` | Modification approuvée par le propriétaire, dans le périmètre décrit |
| `A-VERIFIER` | Comportement de référence non encore établi |

| État d'implémentation |
|---|
| non commencé · en cours · testé · intégré |

## Gabarit d'une fiche

```markdown
### MEC-NNNN — <titre court>

| Champ | Valeur |
|---|---|
| Système | |
| Description | |
| Classe | OXCE-REFERENCE / MODIFICATION-PROPOSEE / MODIFICATION-VALIDEE / A-VERIFIER |
| Fonctionnement de référence et preuves | commit OXCE, fichiers, documentation, reproduction expérimentale |
| Changement demandé | contenu, raisons, impacts prévus |
| Décision du propriétaire | acceptée / refusée / reportée — preuve de validation explicite — date |
| Périmètre autorisé | |
| Éléments exclus | |
| Tests de référence | |
| Tests de modification | |
| État d'implémentation | non commencé / en cours / testé / intégré |
```

L'identifiant `MEC-NNNN` est permanent : il n'est jamais réattribué.

## Mécaniques

_Aucune._
