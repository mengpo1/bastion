# Registre des mécaniques de gameplay

Registre protégé (spécification v0.2, §3.1). Une fiche n'autorise un changement de comportement qu'avec une **décision du propriétaire « acceptée »**, explicite, datée et prouvée. Claude Code n'y écrit qu'avec cet accord.

**Une seule fiche est enregistrée : `MEC-0001`, proposée et incomplète, sans décision globale « acceptée ».** Aucune mécanique n'est acceptée dans son ensemble : aucune mécanique de jeu ne peut donc être implémentée.

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

### MEC-0001 — Déplacement élémentaire à pied

**Fiche de conception incomplète. La mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**

| Champ | Valeur |
|---|---|
| Système | Combat tactique : déplacement d'une unité à pied. |
| Description | Une unité se déplace de case en case vers une destination choisie, en payant des unités de temps (TU). Règles partielles ci-dessous. |
| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. |
| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12 et de la proposition Z1 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception S1 à S12 acceptées le 8 novembre 2026 ; proposition Z1 du propriétaire, à confirmer. Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par le mandat `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (branche `orchestration/mandats`, commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`), confirmées par l'autorisation d'exécution du LOT-2C donnée par le propriétaire le 8 novembre 2026. |
| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12 ne couvrent pas. |
| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
| Tests de modification | Critères futurs seulement, un par écart retenu. Aucun test écrit ni exécuté. |
| État d'implémentation | non commencé |

#### Sous-décisions de conception acceptées le 8 novembre 2026

Elles n'autorisent, seules, aucun gameplay. Chaque sous-décision S*n* transcrit la déclaration A.*n* du mandat LOT-2C ; ces numéros sont distincts des scénarios S1 à S7 du LOT-2A.

- **S1** — Huit directions, diagonales incluses.
- **S2** — Coût d'un pas en diagonale : coût de la case d'arrivée × 1,5, arrondi à l'entier inférieur (comme OXCE, selon la lecture du code : LOT-2A §2 ligne 4).
- **S3** — Diagonale interdite uniquement lorsque les deux cases orthogonales voisines sont bloquées.
- **S4** — Une unité voisine ne compte pas comme obstacle pour la règle des diagonales.
- **S5** — TU insuffisantes : déplacement partiel, comme dans OXCE (selon la lecture du code : LOT-2A §2 ligne 9). Décision initiale, nuancée ensuite par la proposition Z1.
- **S6** — Destinations autorisées : cases actuellement visibles ou déjà explorées.
- **S7** — Le trajet reste entièrement dans des cases actuellement visibles ou déjà explorées.
- **S8** — Le trajet est calculé selon le dernier état connu du terrain ; le déplacement est interrompu lorsqu'un obstacle inconnu est rencontré.
- **S9** — Un obstacle inconnu rencontré pendant un déplacement devient connu du joueur et met à jour sa connaissance du terrain.
- **S10** — Une case occupée par une autre unité est infranchissable, pour la traversée comme pour la destination.
- **S11** — Une unité cachée rencontrée pendant un déplacement est révélée au joueur.
- **S12** — Une unité révélée redevient cachée lorsqu'elle n'est plus observable, sans indication persistante de sa position.

#### Proposition du propriétaire à confirmer (non acceptée)

- **Z1** — Afficher la zone atteignable et interdire de sélectionner une destination hors de cette zone. Si elle est confirmée, elle remplacerait le déplacement partiel de S5 pour une sélection normale de destination ; l'interruption devant un obstacle inconnu (S8) demeurerait.

#### Encore ouvert

- Carte à un seul niveau ; taille des unités ; modèle du coût d'entrée par case ; modèle des murs et obstacles. S2 et S3 supposent un coût par case et des obstacles en cases bloquées : la réponse à ce point peut obliger à les revoir.
- Valeurs des coûts de terrain ; capital initial et renouvellement des TU.
- Calcul de chemin garantissant le coût minimal ; départage déterministe des chemins de même coût.
- Orientation et rotation ; énergie ; interruptions non encore spécifiées.
- Conditions détaillées de visibilité ; règles de brouillard de guerre hors du déplacement.
- Interface de la zone atteignable : présentation et sélection.
- Trajet devenu non payable ou non réalisable à cause d'un coût réel ou d'une occupation jusque-là inconnus.
- Confirmation de Z1 et rôle restant du déplacement partiel (S5).
- Autres propositions du LOT-2B non arbitrées, notamment : ordre impossible sans TU dépensée (P14), paiement de chaque pas avant de le faire, marche seule ; classe définitive de la fiche.

Cette liste n'est pas exhaustive : tout ce que S1 à S12 ne couvrent pas reste non décidé.

L'hypothèse provisoire du LOT-2B « toutes les unités sont connues » n'est pas retenue : S6 à S9 introduisent les cases explorées et le terrain mémorisé, S11 et S12 les unités cachées.
