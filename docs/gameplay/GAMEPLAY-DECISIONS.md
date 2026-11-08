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

**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**

| Champ | Valeur |
|---|---|
| Système | Combat tactique : déplacement d'une unité à pied. |
| Description | Une unité se déplace de case en case vers une destination choisie, en payant des unités de temps (TU). Règles partielles ci-dessous. |
| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. Actualisation : `docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`. Surcharge, même commit, lecture du code : `src/Savegame/BattleUnit.cpp:2709-2726` et `:4852-4861`, `src/Battlescape/UnitWalkBState.cpp:295-323`. |
| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12, Z1 et N1 à N14 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception acceptées le 8 novembre 2026 : S1 à S12 (LOT-2C), puis Z1 et N1 à N14 (LOT-2D ; N12 et N13 fusionnées dans N14). Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par les mandats `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`) et `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md` (commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`), branche `orchestration/mandats`, confirmées par les autorisations d'exécution de ces lots données par le propriétaire le 8 novembre 2026. |
| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas. |
| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
| Tests de modification | Critères futurs seulement, un par écart retenu. Aucun test écrit ni exécuté. |
| État d'implémentation | non commencé |

#### Sous-décisions de conception acceptées le 8 novembre 2026 (LOT-2C)

Elles n'autorisent, seules, aucun gameplay. Chaque sous-décision S*n* transcrit la déclaration A.*n* du mandat LOT-2C ; ces numéros sont distincts des scénarios S1 à S7 du LOT-2A.

- **S1** — Huit directions, diagonales incluses.
- **S2** — Coût d'un pas en diagonale : coût de la case d'arrivée × 1,5, arrondi à l'entier inférieur (comme OXCE, selon la lecture du code : LOT-2A §2 ligne 4).
- **S3** — Diagonale interdite uniquement lorsque les deux cases orthogonales voisines sont bloquées.
- **S4** — Une unité voisine ne compte pas comme obstacle pour la règle des diagonales.
- **S5** — TU insuffisantes : déplacement partiel, comme dans OXCE (selon la lecture du code : LOT-2A §2 ligne 9). Décision initiale, conservée comme historique : **supplantée par Z1 pour la sélection normale d'une destination**. Une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. *(Annotation ajoutée au LOT-2D.)*
- **S6** — Destinations autorisées : cases actuellement visibles ou déjà explorées.
- **S7** — Le trajet reste entièrement dans des cases actuellement visibles ou déjà explorées.
- **S8** — Le trajet est calculé selon le dernier état connu du terrain ; le déplacement est interrompu lorsqu'un obstacle inconnu est rencontré.
- **S9** — Un obstacle inconnu rencontré pendant un déplacement devient connu du joueur et met à jour sa connaissance du terrain.
- **S10** — Une case occupée par une autre unité est infranchissable, pour la traversée comme pour la destination.
- **S11** — Une unité cachée rencontrée pendant un déplacement est révélée au joueur.
- **S12** — Une unité révélée redevient cachée lorsqu'elle n'est plus observable, sans indication persistante de sa position.

#### Décisions acceptées le 8 novembre 2026, après le LOT-2C (LOT-2D)

Elles n'autorisent, seules, aucun gameplay. Les références Z1 et N*n* reprennent celles du mandat LOT-2D.

Entre crochets, le rapport à OXCE, établi par lecture du code (sans exécution) ; le détail figure dans le rapport LOT-2D. « Vérifié » : comportement d'OXCE lu dans le code, concordant dans son principe avec la décision ; aucune fidélité n'est démontrée. « Écart établi » : la décision s'écarte de ce comportement lu. « À vérifier » : point seulement signalé au LOT-2A (§6), sans étude.

- **Z1** — Afficher la zone atteignable selon les TU et les informations connues ; interdire la sélection d'une destination hors de cette zone. Proposée au LOT-2C, acceptée ensuite. Z1 supplante S5 pour la sélection normale ; une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. [Écart établi : OXCE calcule le chemin sans regarder les TU, puis déplace partiellement l'unité (LOT-2A §2 ligne 9).]
- **N1** — Terrain en « modèle B » : des cases et des murs séparant les cases ; huit directions maintenues (S1). [Vérifié : dans OXCE, une case a un sol, un mur ouest, un mur nord et un objet (LOT-2A §2 ligne 11).]
- **N2** — Règle permissive dans le modèle B : diagonale permise si au moins un des deux passages orthogonaux autour du coin est ouvert ; interdite si les deux sont bloqués. N2 étend aux murs du modèle B le principe permissif de S3 ; S4 inchangée. [Écart établi : OXCE refuse la diagonale dès qu'un des murs concernés bloque, sur l'un ou l'autre passage (LOT-2A §2 ligne 3 ; `src/Battlescape/Pathfinding.cpp:959-966` pour le nord-est).]
- **N3** — Plusieurs niveaux dès `MEC-0001`, avec des positions de principe (x, y, z). [Vérifié : positions en x, y, z dans OXCE (LOT-2A §2 ligne 1).]
- **N4** — Changements de niveau prévus dès la conception : escaliers, échelles et ascenseurs. [À vérifier.]
- **N5** — Chutes volontaires et involontaires autorisées. [À vérifier.]
- **N6** — Dégâts de chute croissants avec la hauteur. [À vérifier.]
- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.]
- **N8** — Les caractéristiques individuelles et les équipements peuvent modifier les conséquences d'une chute. [À vérifier.]
- **N9** — L'armure peut protéger, mais son poids peut aussi aggraver les conséquences d'une chute. [À vérifier.]
- **N10** — Le poids de l'inventaire (armes, munitions, matériel) contribue aussi à l'effet de la charge lors d'une chute. [Effet sur les chutes : à vérifier. Vérifié : dans OXCE, le poids porté est le poids de l'armure plus celui des objets de l'inventaire (`src/Savegame/BattleUnit.cpp:4852-4861`).]
- **N11** — Le poids total porté affecte aussi le déplacement normal. [Vérifié : dans OXCE, l'effet est indirect, par la réduction des TU, qui touche toutes les actions ; voir N12 à N14.]
- **N12 à N14** — Surcharge, décision finale N14 (la plus récente) :
  - principe d'OXCE, sans seuil d'immobilisation supplémentaire ;
  - l'unité est empêchée d'avancer seulement lorsque ses TU restantes ne permettent pas de payer le pas suivant : aucune immobilisation liée à la charge ;
  - « encombré » peut rester un simple indicateur informatif, sans nouveau modificateur ni statut technique décidé ;
  - la Force détermine l'effet de la surcharge (N13).

  Étapes : N12 souhaitait une pénalité progressive et un état encombré immobilisant ; N13 a fait dépendre l'effet de la Force. N14 a remplacé la pénalité et l'immobilisation de N12 par le principe d'OXCE, où la Force détermine l'effet. Aucun surcoût des pas lié au poids n'est décidé.

  [Vérifié : dans OXCE, à la récupération des TU, si le rapport Force / poids porté est inférieur à 1, les TU sont multipliées par ce rapport et tronquées, avant d'autres pénalités ; ce n'est pas un surcoût des pas (`src/Savegame/BattleUnit.cpp:2709-2726`). L'unité s'arrête quand le pas suivant dépasse ses TU restantes (`src/Battlescape/UnitWalkBState.cpp:295-323`).]

#### Encore ouvert

- Géométrie précise des murs et des angles, dont ce qu'est un passage orthogonal « bloqué » pour N2 ; portes ; taille des unités.
- Modèle et valeurs des coûts : terrain, murs éventuels, changements de niveau. S2 suppose un coût d'entrée par case d'arrivée : le modèle B (N1) peut obliger à la revoir, notamment pour un coût éventuel des murs (dans OXCE, ce coût s'ajoute après le facteur 1,5 : LOT-2A §2 lignes 4 et 5).
- Règles précises des escaliers, échelles et ascenseurs.
- Chutes :
  - règles des chutes volontaires et involontaires ;
  - formule et valeurs des dégâts ;
  - hauteur de chute sans dégâts ;
  - effet précis des caractéristiques, équipements, armure et charge.
- Surcharge : transposition exacte du principe d'OXCE (formule, arrondi, ordre avec les autres pénalités) ; présentation de l'indicateur « encombré ».
- Capital initial et renouvellement des TU.
- Calcul de chemin garantissant le coût minimal ; départage déterministe des chemins de même coût.
- Orientation et rotation ; énergie ; interruptions non encore spécifiées.
- Conditions détaillées de visibilité ; règles de brouillard de guerre hors du déplacement.
- Interface de la zone atteignable : présentation et sélection.
- Trajet devenu non payable ou non réalisable en cours de route, à cause d'un coût réel, d'une occupation ou d'un obstacle jusque-là inconnus. Au-delà de l'interruption (S8, S11), ce cas n'est pas entièrement défini, notamment en cas d'augmentation imprévue du coût.
- Autres propositions du LOT-2B non arbitrées, notamment : ordre impossible sans TU dépensée (P14), paiement de chaque pas avant de le faire, marche seule ; classe définitive de la fiche.

Cette liste n'est pas exhaustive : tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.

L'hypothèse provisoire du LOT-2B « toutes les unités sont connues » n'est pas retenue : S6 à S9 introduisent les cases explorées et le terrain mémorisé, S11 et S12 les unités cachées.
