# Registre des mécaniques de gameplay

Registre protégé (spécification v0.2, §3.1). Une fiche n'autorise un changement de comportement qu'avec une **décision du propriétaire « acceptée »**, explicite, datée et prouvée. Claude Code n'y écrit qu'avec cet accord.

**Deux fiches sont enregistrées : `MEC-0001` et `MEC-0002`, proposées et incomplètes, sans décision globale « acceptée ».** Aucune mécanique n'est acceptée dans son ensemble : aucune mécanique de jeu ne peut donc être implémentée.

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

**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14, puis ARB-A à ARB-E et G1 à G4 le 17 novembre 2026), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé. Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`.**

| Champ | Valeur |
|---|---|
| Système | Combat tactique : déplacement d'une unité à pied. |
| Description | Une unité se déplace de case en case vers une destination choisie, en payant des unités de temps (TU). Règles partielles ci-dessous. |
| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. Actualisation : `docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`. Inscription des sous-décisions du 17 novembre 2026 : `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md`. Surcharge, même commit, lecture du code : `src/Savegame/BattleUnit.cpp:2709-2726` et `:4852-4861`, `src/Battlescape/UnitWalkBState.cpp:295-323`. |
| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception acceptées le 8 novembre 2026 : S1 à S12 (LOT-2C), puis Z1 et N1 à N14 (LOT-2D ; N12 et N13 fusionnées dans N14). Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par les mandats `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`) et `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md` (commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`), branche `orchestration/mandats`, confirmées par les autorisations d'exécution de ces lots données par le propriétaire le 8 novembre 2026. Sous-décisions de conception acceptées explicitement par le propriétaire, en conversation, le 17 novembre 2026 : ARB-A à ARB-E et G1 à G4 ; preuve et provenance : bloc « Sous-décisions de conception acceptées le 17 novembre 2026 » ci-dessous. |
| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 ne couvrent pas ; les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002`. |
| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
| Tests de modification | Critères futurs seulement, un par écart retenu. Aucun test écrit ni exécuté. |
| État d'implémentation | non commencé |

#### Sous-décisions de conception acceptées le 8 novembre 2026 (LOT-2C)

Elles n'autorisent, seules, aucun gameplay. Chaque sous-décision S*n* transcrit la déclaration A.*n* du mandat LOT-2C ; ces numéros sont distincts des scénarios S1 à S7 du LOT-2A.

- **S1** — Huit directions, diagonales incluses.
- **S2** — Coût d'un pas en diagonale : coût de la case d'arrivée × 1,5, arrondi à l'entier inférieur (comme OXCE, selon la lecture du code : LOT-2A §2 ligne 4).
- **S3** — Diagonale interdite uniquement lorsque les deux cases orthogonales voisines sont bloquées.
- **S4** — Une unité voisine ne compte pas comme obstacle pour la règle des diagonales. *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé ; restreinte postérieurement par ARB-A et G1. Une unité voisine ne compte toujours pas comme un mur pour le contrôle topologique, mais une unité consciente peut rendre physiquement impraticable le passage emprunté par la diagonale ; voir le bloc du 17 novembre 2026.)*
- **S5** — TU insuffisantes : déplacement partiel, comme dans OXCE (selon la lecture du code : LOT-2A §2 ligne 9). Décision initiale, conservée comme historique : **supplantée par Z1 pour la sélection normale d'une destination**. Une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. *(Annotation ajoutée au LOT-2D.)*
- **S6** — Destinations autorisées : cases actuellement visibles ou déjà explorées.
- **S7** — Le trajet reste entièrement dans des cases actuellement visibles ou déjà explorées.
- **S8** — Le trajet est calculé selon le dernier état connu du terrain ; le déplacement est interrompu lorsqu'un obstacle inconnu est rencontré.
- **S9** — Un obstacle inconnu rencontré pendant un déplacement devient connu du joueur et met à jour sa connaissance du terrain.
- **S10** — Une case occupée par une autre unité est infranchissable, pour la traversée comme pour la destination. *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé ; deux exceptions postérieures. Pour la marche ordinaire, un corps mort ou inconscient ne bloque ni la traversée ni la destination (ARB-B). Lors d'un réveil sans case voisine disponible, deux unités conscientes occupent transitoirement la même case (G2). Voir le bloc du 17 novembre 2026.)*
- **S11** — Une unité cachée rencontrée pendant un déplacement est révélée au joueur.
- **S12** — Une unité révélée redevient cachée lorsqu'elle n'est plus observable, sans indication persistante de sa position.

#### Décisions acceptées le 8 novembre 2026, après le LOT-2C (LOT-2D)

Elles n'autorisent, seules, aucun gameplay. Les références Z1 et N*n* reprennent celles du mandat LOT-2D.

Entre crochets, le rapport à OXCE, établi par lecture du code (sans exécution) ; le détail figure dans le rapport LOT-2D. « Vérifié » : comportement d'OXCE lu dans le code, concordant dans son principe avec la décision ; aucune fidélité n'est démontrée. « Écart établi » : la décision s'écarte de ce comportement lu. « À vérifier » : point seulement signalé au LOT-2A (§6), sans étude.

- **Z1** — Afficher la zone atteignable selon les TU et les informations connues ; interdire la sélection d'une destination hors de cette zone. Proposée au LOT-2C, acceptée ensuite. Z1 supplante S5 pour la sélection normale ; une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. [Écart établi : OXCE calcule le chemin sans regarder les TU, puis déplace partiellement l'unité (LOT-2A §2 ligne 9).] *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé ; G3 ajoute postérieurement l'énergie. La zone atteignable est calculée avec les TU, l'énergie et les informations connues ; une destination qui ne peut être atteinte avec les deux ressources n'est pas sélectionnable. Voir le bloc du 17 novembre 2026.)*
- **N1** — Terrain en « modèle B » : des cases et des murs séparant les cases ; huit directions maintenues (S1). [Vérifié : dans OXCE, une case a un sol, un mur ouest, un mur nord et un objet (LOT-2A §2 ligne 11).]
- **N2** — Règle permissive dans le modèle B : diagonale permise si au moins un des deux passages orthogonaux autour du coin est ouvert ; interdite si les deux sont bloqués. N2 étend aux murs du modèle B le principe permissif de S3 ; S4 inchangée. [Écart établi : OXCE refuse la diagonale dès qu'un des murs concernés bloque, sur l'un ou l'autre passage (LOT-2A §2 ligne 3 ; `src/Battlescape/Pathfinding.cpp:959-966` pour le nord-est).] *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé. N2 reste le premier contrôle, topologique ; ARB-A et G1 y ajoutent postérieurement un contrôle physique : une diagonale permise par N2 est refusée si aucun passage orthogonal n'est physiquement praticable. La mention « S4 inchangée » se lit avec l'annotation de S4.)*
- **N3** — Plusieurs niveaux dès `MEC-0001`, avec des positions de principe (x, y, z). [Vérifié : positions en x, y, z dans OXCE (LOT-2A §2 ligne 1).]
- **N4** — Changements de niveau prévus dès la conception : escaliers, échelles et ascenseurs. [À vérifier.]
- **N5** — Chutes volontaires et involontaires autorisées. [À vérifier.]
- **N6** — Dégâts de chute croissants avec la hauteur. [À vérifier.]
- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] Précisée par `MEC-0002`, qui fait autorité pour les sauts et les chutes : pas de dégâts de chute ordinaires jusqu'à 3 m inclus de hauteur équivalente (CH-09) ; voir aussi CH-01 (saut volontaire) et CH-03 (chute involontaire). *(Annotation ajoutée lors de l'inscription de `MEC-0002`.)*
- **N8** — Les caractéristiques individuelles et les équipements peuvent modifier les conséquences d'une chute. [À vérifier.]
- **N9** — L'armure peut protéger, mais son poids peut aussi aggraver les conséquences d'une chute. [À vérifier.]
- **N10** — Le poids de l'inventaire (armes, munitions, matériel) contribue aussi à l'effet de la charge lors d'une chute. [Effet sur les chutes : à vérifier. Vérifié : dans OXCE, le poids porté est le poids de l'armure plus celui des objets de l'inventaire (`src/Savegame/BattleUnit.cpp:4852-4861`).]
  *(Annotation ajoutée lors de l'inscription de `MEC-0002` : pour les sauts, les chutes et leurs conséquences, N5 à N10 sont précisées par `MEC-0002`, qui fait autorité ; leur texte est conservé ici comme historique.)*
- **N11** — Le poids total porté affecte aussi le déplacement normal. [Vérifié : dans OXCE, l'effet est indirect, par la réduction des TU, qui touche toutes les actions ; voir N12 à N14.]
- **N12 à N14** — Surcharge, décision finale N14 (la plus récente) :
  - principe d'OXCE, sans seuil d'immobilisation supplémentaire ;
  - l'unité est empêchée d'avancer seulement lorsque ses TU restantes ne permettent pas de payer le pas suivant : aucune immobilisation liée à la charge ; *(annotation ajoutée le 17 novembre 2026 : texte historique conservé ; G3 ajoute postérieurement un second motif de non-exécution du pas, l'énergie insuffisante : le pas n'est payable que si les TU et l'énergie suffisent. Aucune immobilisation liée à la charge n'est ajoutée. Pour l'ordre de la récupération et de la réduction due à la surcharge, voir ARB-D, bloc du 17 novembre 2026.)*
  - « encombré » peut rester un simple indicateur informatif, sans nouveau modificateur ni statut technique décidé ;
  - la Force détermine l'effet de la surcharge (N13).

  Étapes : N12 souhaitait une pénalité progressive et un état encombré immobilisant ; N13 a fait dépendre l'effet de la Force. N14 a remplacé la pénalité et l'immobilisation de N12 par le principe d'OXCE, où la Force détermine l'effet. Aucun surcoût des pas lié au poids n'est décidé.

  [Vérifié : dans OXCE, à la récupération des TU, si le rapport Force / poids porté est inférieur à 1, les TU sont multipliées par ce rapport et tronquées, avant d'autres pénalités ; ce n'est pas un surcoût des pas (`src/Savegame/BattleUnit.cpp:2709-2726`). L'unité s'arrête quand le pas suivant dépasse ses TU restantes (`src/Battlescape/UnitWalkBState.cpp:295-323`).]

#### Sous-décisions de conception acceptées le 17 novembre 2026 (ARB-A à ARB-E, G1 à G4)

Elles n'autorisent, seules, aucun gameplay : `MEC-0001` reste reportée dans son ensemble. Validées explicitement par le propriétaire, en conversation, le 17 novembre 2026, elles sont inscrites par le mandat d'inscription documentaire `MEC-0001` v1.0, validé par le propriétaire le même jour, et transcrites depuis la consolidation documentaire `MEC-0001` v1.4.1 du 17 novembre 2026. Ces deux documents, transmis par le propriétaire, ne sont pas archivés dans le dépôt : consolidation, SHA-256 `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc` ; mandat, SHA-256 `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0`. Détail de l'inscription : `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md`.

Preuve de validation : transcription des échanges du 17 novembre 2026, reprise au §1.2 de la consolidation v1.4.1 ; les messages d'origine ne sont pas dans le dépôt. « parfait. je valide les deux » valide ARB-B et ARB-E ; « Je valide tout le reste », après le récapitulatif des cinq arbitrages, valide ARB-A, ARB-C et ARB-D. Pour G1 à G4, le propriétaire a répondu « B » (G1 : trajet par un passage ouvert), « B » puis « A » (G2 : repositionnement automatique, puis réveil sur place faute de case voisine libre), « B » (G3 : TU et énergie) et « A » (G4 : priorité aux TU), puis « Je valide » après le récapitulatif de G1 à G4. Le même §1.2 reprend les formulations qui précisent G2 et G4 : soumises avant ces choix, ou présentées après eux et dans le récapitulatif approuvé par « Je valide ».

Les valeurs numériques des scénarios de test de la consolidation sont fictives : aucune n'est inscrite ici. Entre crochets, le rapport à OXCE que la consolidation signale, selon les conventions du bloc précédent ; les lectures du code qui le fondent sont détaillées dans le rapport d'inscription.

- **ARB-A** — Une diagonale admise par le contrôle topologique (S4, N2) peut néanmoins être inexécutable si le volume de l'unité ne peut pas passer sans collision. Restriction postérieure explicite de S4 et N2 (voir leurs annotations), précisée par G1. Ouvert : géométrie détaillée. [Écart établi : dans OXCE, une unité voisine n'empêche pas la diagonale (LOT-2A §2 ligne 3).]
- **ARB-B** — Pendant la marche ordinaire, les corps morts ou inconscients ne bloquent ni la traversée ni la destination. Exception postérieure à la formulation historique de S10 (voir son annotation). Le simple chevauchement lié à la marche n'est pas un impact de `MEC-0002` ; le corps garde sa masse et son volume pour `MEC-0002` (RP-04, EN-08). Précisée par G2 pour le réveil.
- **ARB-C** — Une porte demande une ouverture explicite : la marche ne l'ouvre pas automatiquement. Les escaliers et les échelles s'empruntent par des connexions définies ; les ascenseurs ont des états et des connexions définis. La marche ordinaire ne change pas de niveau de façon implicite ; les sauts et les chutes relèvent de `MEC-0002`. Ouvert : coûts, états et détails d'interaction. [Écart établi : dans OXCE, la marche ouvre les portes au passage (`src/Battlescape/UnitWalkBState.cpp:337-354`, emplacement signalé au LOT-2A §6 ; lecture du code, sans exécution, rapportée dans le rapport d'inscription).]
- **ARB-D** — Après récupération, les TU disponibles valent min(solde restant + TU récupérées, TU maximales) ; la réduction due à la surcharge s'applique ensuite à ce total plafonné, et non au seul incrément récupéré. L'énergie est récupérée séparément. La surcharge ne majore pas le prix des pas. Ouvert : formule exacte du facteur, conversion de la Force en capacité en kg, arrondis, valeurs.
- **ARB-E** — Un tir de réaction effectivement tiré contre une unité qui marche interrompt son ordre de marche, même s'il manque, ne blesse pas ou ne met pas hors de combat. Le pas déjà effectué reste débité une seule fois, sans remboursement. Un surveillant qui pivote sans tirer n'interrompt pas la marche au titre d'ARB-E. Ouvert : conditions, ordre et coûts du système de surveillance (Overwatch), hors de cette fiche. Aucune conversion des UT de kowlting en TU de Bastion.
- **G1** — Le pas diagonal ne suit pas obligatoirement la droite entre les centres des cases : il passe par l'un des passages orthogonaux praticables autour du coin.
  - N2 reste le premier contrôle : au moins un des deux passages orthogonaux doit être ouvert.
  - Le volume de l'unité doit pouvoir emprunter un passage sans traverser celui d'une autre unité consciente ou d'un obstacle ; pendant la marche ordinaire, un corps mort ou inconscient reste traversable (ARB-B).
  - Une unité voisine n'interdit pas automatiquement la diagonale au titre de S4, mais peut rendre le passage physiquement impraticable.
  - Le trajet physique respecte S7 : il n'exploite pas de terrain jamais exploré.
  - Le déplacement reste un seul pas diagonal : le coût en TU de S2 est facturé une fois, et il ne devient pas deux pas orthogonaux.
  - Sans passage physiquement praticable, la diagonale est refusée.

  Ouvert : dimensions des volumes, largeur des cases, épaisseur des murs, tolérance géométrique, trajectoire et sous-segments (dont l'application de S7 et les contacts avec les murs), événements détectés pendant la traversée, coût éventuel des murs, coût en énergie du pas diagonal (G3).
- **G2** — Réveil d'une unité inconsciente dont la case est occupée par une autre unité :
  - si une case voisine libre et accessible existe, l'unité réveillée y est automatiquement repositionnée ; ce repositionnement n'est ni un déplacement volontaire ni un pas de marche ordinaire, et ne coûte pas de TU de marche ; aucun autre coût n'est fixé ;
  - si aucune case voisine n'est disponible, l'unité reprend conscience sur place et reste au sol ; elle ne peut pas se relever tant que sa case reste occupée. Ce chevauchement de deux unités conscientes est une exception transitoire à S10 ; la reprise de conscience n'est pas différée faute de place ;
  - ARB-B demeure : pendant la marche ordinaire, un corps inconscient reste traversable jusqu'au réveil, un corps mort reste traversable.

  Ouvert : choix entre plusieurs cases voisines libres ; sens précis d'« accessible » (terrain, niveau, visibilité, support, volumes) ; statut d'une case portant déjà un corps (compte-t-elle comme « libre » ?) ; correspondance technique de l'état « au sol » avec les postures de GE-03, sans relèvement implicite ; contacts et interactions pendant la coexistence ; événements consécutifs ; coûts des autres actions de posture. Hors de G2 : admissibilité des cases portant un corps pour les esquives (ES-08, ES-11, ES-12), les repoussements (RP-03, RP-05) et les sauts, qui relève de `MEC-0002`.
- **G3** — Chaque pas de marche ordinaire coûte des TU et de l'énergie ; il n'est réalisable que si les deux ressources suffisent pour ce pas. La zone atteignable (Z1) se calcule avec les TU disponibles, l'énergie disponible et les informations connues ; une destination qui ne peut pas être atteinte avec les deux ressources n'est pas sélectionnable. Les coûts sont propres à Bastion : ni conversion des UT de kowlting, ni reprise automatique des valeurs d'OXCE. G3 n'ajoute aucun coût d'énergie aux esquives de `MEC-0002` : ES-09 et ES-10 ne prévoient que le débit de TU ; une telle extension exigerait une décision distincte. G3 modifie la portée de Z1 et de N14 (voir leurs annotations), sans ajouter d'immobilisation liée à la surcharge. Ouvert : barèmes de terrain, coûts en énergie des diagonales et des passages, arrondis, coûts des murs, récupération et plafond d'énergie, hausse imprévue d'un coût pendant un ordre.
- **G4** — Parmi les chemins admissibles avec les ressources disponibles et les informations connues du camp (S6 à S9, et non la vérité cachée) :
  - choisir celui qui dépense le moins de TU ;
  - à égalité de TU, celui qui dépense le moins d'énergie ;
  - s'il reste une égalité, appliquer un départage déterministe, identique pour un même état et une même destination.

  Un chemin moins cher en TU mais irréalisable en énergie n'est pas admissible ; la priorité est lexicographique, sans mélange pondéré des deux ressources. Ouvert : clé exacte du départage final, algorithme de recherche. [Écart établi : OXCE retient une ligne droite à coût homogène sans la comparer à un détour ; le chemin le moins coûteux n'est donc pas garanti (inférence, LOT-2A §2 ligne 14).]

#### Encore ouvert

- Géométrie précise des murs et des angles, dont ce qu'est un passage orthogonal « bloqué » pour N2 ; trajectoire physique du pas diagonal (G1) ; portes : l'ouverture explicite est décidée (ARB-C), leurs coûts et leurs détails restent ouverts ; taille des unités.
- Modèle et valeurs des coûts, en TU et en énergie (G3) : terrain, murs éventuels, changements de niveau. S2 suppose un coût d'entrée par case d'arrivée : le modèle B (N1) peut obliger à la revoir, notamment pour un coût éventuel des murs (dans OXCE, ce coût s'ajoute après le facteur 1,5 : LOT-2A §2 lignes 4 et 5).
- Règles précises des escaliers, échelles et ascenseurs ; le principe des connexions définies et des états d'ascenseur est décidé (ARB-C).
- Chutes :
  - règles des chutes volontaires et involontaires ;
  - formule et valeurs des dégâts ;
  - hauteur de chute sans dégâts ;
  - effet précis des caractéristiques, équipements, armure et charge ;
  - ces points sont précisés ou tranchés en partie par `MEC-0002`, qui fait autorité (seuil sans dégâts : 3 m inclus, CH-09) ; les points qui restent ouverts y sont listés.
- Surcharge : l'ordre de la récupération est décidé (ARB-D : solde plus récupération, plafond aux TU maximales, puis réduction sur le total plafonné) ; restent ouverts la formule exacte du facteur, la conversion de la Force en capacité en kg, l'arrondi, l'ordre avec les autres pénalités et la présentation de l'indicateur « encombré ».
- Capital initial et quantités de TU récupérées, TU maximales ; le principe du renouvellement est décidé (ARB-D).
- Calcul de chemin : le critère est décidé (G4 : TU minimales, puis énergie minimale, puis départage déterministe) ; restent ouverts la clé exacte du départage final et l'algorithme de recherche.
- Orientation et rotation ; énergie, notamment : barèmes, énergie maximale, récupération et plafond (le double coût en TU et en énergie est décidé, G3) ; interruptions autres que le tir de réaction (ARB-E), dont la simple découverte d'un ennemi sans tir ; conditions et coûts du système de surveillance (Overwatch).
- Conditions détaillées de visibilité ; règles de brouillard de guerre hors du déplacement.
- Interface de la zone atteignable : présentation et sélection.
- Trajet devenu non payable ou non réalisable en cours de route, à cause d'un coût réel, d'une occupation ou d'un obstacle jusque-là inconnus. Au-delà de l'interruption (S8, S11), ce cas n'est pas entièrement défini, notamment en cas d'augmentation imprévue du coût.
- Autres propositions du LOT-2B non arbitrées, notamment : ordre impossible sans TU dépensée (P14), paiement de chaque pas avant de le faire, marche seule ; classe définitive de la fiche.

Cette liste n'est pas exhaustive : tout ce que S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté. Les points laissés ouverts par ARB-A à ARB-E et G1 à G4 sont aussi indiqués dans chacune de ces sous-décisions.

L'hypothèse provisoire du LOT-2B « toutes les unités sont connues » n'est pas retenue : S6 à S9 introduisent les cases explorées et le terrain mémorisé, S11 et S12 les unités cachées.

### MEC-0002 — Sauts, chutes et collisions

**Fiche de conception incomplète. Des principes de conception sont acceptés (PE-01 à EN-10, du 14 novembre 2026, sauf GE-09 et RP-09, du 13 novembre 2026, dont le maintien a été confirmé le 14 novembre 2026), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**

| Champ | Valeur |
|---|---|
| Système | Combat tactique : sauts simples et attaques sautées, chutes volontaires et involontaires, trajectoire balistique, collisions, réception, esquives réactives, repoussements, destruction sous impact et chaîne d'événements associée. |
| Description | Une unité peut sauter vers une case admissible, tomber, heurter des unités ou le décor, esquiver une unité qui tombe ou être repoussée. Règles partielles ci-dessous. |
| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** ; aucun calcul de dégâts de chute n'y a été identifié (`docs/reviews/LOT-2E-VERTICALITE-OXCE.md`, C8). Les règles ci-dessous sont des adaptations de Bastion, sans reprise de code, de données ni d'assets (D4). Spécification : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Arbitrage : `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. Principes DS1 à DS5 : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`. Consolidation : `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` et `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`. |
| Changement demandé | Fixer les sauts, chutes et collisions de Bastion à partir des principes PE-01 à EN-10 ci-dessous. Les points encore ouverts sont listés plus bas. |
| Décision du propriétaire | reportée — inscription partielle des principes de conception. Principes acceptés le 14 novembre 2026 : 29 propositions et arbitrages complémentaires 1A à 6A, consolidés dans `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` (branche `orchestration/mandats`, commit `d028c52f500ed8daeca917adbcb9a9e1eb3ff8bd`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`). Preuve : déclaration du propriétaire du 14 novembre 2026 (preuve déclarative), qui précise que les esquives sont des tentatives automatiques dont la réussite dépend d'un tirage et des Réactions. Le même jour, arbitrages complémentaires du propriétaire sur la hauteur d'étage (3 m), le seuil de chute sans dégâts (3 m inclus), la surcharge, la gravité et la vitesse héritée, et confirmation des huit points laissés à confirmer par le LOT-2I ; ils sont transcrits par l'orchestrateur dans `docs/mandates/BASTION-MANDAT-LOT-2I-v1.2-CORRECTIF-MEC-0002.md` (branche `orchestration/mandats`, commit `f8cf26e38783499a23244f823da4e221d4a95992`, SHA-256 `e4c5345a324ed4e5eb9cab294c7af900b34c389cb0ea8e25e943da400ace5ba0`), preuve déclarative, et prévalent sur la consolidation là où ils la modifient. GE-09 et RP-09 reprennent DS5.5 et DS5.3 (13 novembre 2026), que la consolidation ne modifie pas ; leur maintien a été confirmé le 14 novembre 2026. Ces principes reprennent ou modifient les décisions du 9 novembre 2026 et le correctif du propriétaire (identifiants du LOT-2F), ainsi que les principes DS1 à DS5 du 13 novembre 2026. |
| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
| Éléments exclus | Tous les points listés sous « Encore ouvert » ; escaliers, échelles et ascenseurs ; règles générales du brouillard ; renouvellement des TU ; stabilité structurelle des bâtiments ; toute autre mécanique (tir, explosion, destruction de cadavre, vol, apesanteur). |
| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` §3). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
| Tests de modification | Critères futurs seulement. Aucun test écrit ni exécuté. |
| État d'implémentation | non commencé |

#### Principes de conception acceptés le 14 novembre 2026

Ils n'autorisent, seuls, aucun gameplay. Les identifiants PE, GE, SA, CH, CO, ES, RP et EN ont été proposés par le LOT-2I. Entre crochets, la décision antérieure reprise, précisée ou modifiée. S, Z et N renvoient à `MEC-0001` (R : registre). Les autres identifiants (J, K, D, I, P, E) renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` (M : décision du 9 novembre 2026 ; P : correctif du propriétaire). DS*n*.*m* renvoie à la consolidation DS1 à DS5 du 13 novembre 2026. A3A, A4.1D, A4.2A, A4.3A, A8A, D1C, D2A, D3A, D4A et « exception de surcharge » désignent les arbitrages complémentaires du 14 novembre 2026, et A12, A18, A24, A25, A27 les points du LOT-2I confirmés le même jour (mandat LOT-2I v1.2, §2). Un renvoi A*n* seul (A5, A6, A7, A15, A17, A19, A26, A29, A30, etc.) désigne l'ambiguïté du même numéro, au §12 de `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` : A12, A18, A24, A25 et A27 y sont réglées, les autres restent ouvertes ; D1C à D4A n'ont aucun lien avec les décisions D01 à D13. « Ouvert » nomme le paramètre qui reste à fixer.

- **Périmètre**
  - **PE-01** — `MEC-0001` garde la marche ordinaire : cheminement, coûts de terrain, diagonales, visibilité du trajet, TU du déplacement ordinaire. Elle conserve S1 à S12, Z1 et N1 à N14, avec une annotation historique de N7, sous réserve d'autorisation d'inscription. Pour les sauts, les chutes et les collisions, `MEC-0002` fait autorité ; N5 à N10 restent dans `MEC-0001` comme historique. [Rattachement de la fiche (LOT-2H, §5 ligne 12) ; primauté confirmée : A24.]
  - **PE-02** — `MEC-0002` couvre le saut simple, l'attaque sautée, les chutes volontaires et involontaires, la trajectoire, les contacts et collisions, la réception, l'esquive réactive, le repoussement, l'impact des corps, la destruction sous impact et la chaîne d'événements associée.
  - **PE-03** — Hors de `MEC-0002` : escaliers, échelles, ascenseurs, règles générales du brouillard, renouvellement global des TU, stabilité structurelle des bâtiments.
  - **PE-04** — Décrire une règle physique utilisable ailleurs n'autorise pas d'autres mécaniques (tir, explosion, destruction de cadavre, vol, apesanteur, etc.).

- **Géométrie, masse et posture**
  - **GE-01** — Positions `(x, y, z)`, plusieurs niveaux. [N3 (R).]
  - **GE-02** — Largeur de case et volumes des unités en proportions, sans mètres fixés. Hauteur d'étage : **3 m** fixes entre deux sols d'étages consécutifs, à distinguer de la montée d'un saut. [DS1.1 ; **précisée** par A3A, qui fixe en mètres la seule hauteur d'étage.] Ouvert : largeur de case, volumes, rapport case/étage.
  - **GE-03** — Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. [DS1.2 ; postures : nouveau.] Ouvert : dimensions par type et posture.
  - **GE-04** — Pendant le vol, posture et orientation du volume sont conservées : pas de rotation des pavés, pas de changement de posture. [nouveau.]
  - **GE-05** — Un contact de surfaces suffit à détecter la rencontre. Sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés, sans créer d'énergie ni dédoubler un impact. [D11 ; contacts : nouveau.] Ouvert : tolérance numérique.
  - **GE-06** — La masse physique totale `M` comprend le corps, l'armure, l'équipement et l'inventaire, en kg. [E23 (P).] Ouvert : masses par type et par objet.
  - **GE-07** — La charge portée, pour la surcharge, comprend l'armure, l'équipement et l'inventaire, en kg ; elle est distincte de `M`. La Force se traduit en capacité de portage en kg, selon un modèle à définir. [N10, N14 (R) ; E20 (LOT-2F).] Ouvert : modèle Force → capacité.
  - **GE-08** — Les unités de plusieurs cases peuvent subir des chutes involontaires et des collisions. Leurs sauts volontaires sont provisoirement indisponibles (« proposition 8/29 »). [étend DS5.5, qui excluait l'attaque sautée faite par ces unités et contre elles.]
  - **GE-09** — Une unité de plusieurs cases n'est pas choisie comme cible d'une attaque sautée. **Maintenue de DS5.5** : la consolidation du 14 novembre ne la redit pas, mais ne la modifie pas ; maintien confirmé par le propriétaire. [DS5.5 ; maintien confirmé : A12.]

- **Sauts**
  - **SA-01** — Saut simple vers une destination admissible au même niveau ou plus bas ; il permet de franchir une ouverture ou un obstacle. Un saut vers une zone sans support immédiat est permis : l'unité continue de tomber jusqu'à un support ou un contact. [nouveau ; N5 (R).]
  - **SA-02** — L'attaque sautée n'est possible que si la cible est au moins un étage plus bas. [J01 (M).]
  - **SA-03** — Un allié ou un neutre déjà identifié ne peut pas être ciblé intentionnellement. [J06 (M).]
  - **SA-04** — Un ennemi actuellement visible peut être ciblé malgré S10. [J13, E14 (P) ; DS1.4.]
  - **SA-05** — Destination visible ou déjà explorée ; jamais explorée : interdite. [J03, J04 (M) ; S6 (R).]
  - **SA-06** — Les cases survolées peuvent n'avoir jamais été explorées. [tranche E15 (LOT-2F).]
  - **SA-07** — Obstacles et unités cachés ne sont révélés qu'à leur rencontre. [P08, I01 (M) ; DS5.2.]
  - **SA-08** — Un ennemi caché, ou un allié ou neutre caché, sur la case attaquée peut être percuté, avec le bonus d'attaque sautée même s'il était allié ou neutre. [J05, J07, J08 (M).]
  - **SA-09** — Un saut simple qui percute par accident une unité cachée : collision et dégâts possibles, **sans** bonus × 1,25. [nouveau ; D08 (M).]
  - **SA-10** — Arc balistique continu, sans contournement des obstacles. Seule une destination à portée de Manhattan est permise ; la trajectoire réelle est ensuite vérifiée avec les volumes. [P07 (M) ; DS1.2.]
  - **SA-11** — Le sol de la case de départ est ignoré au décollage, sans étendre cette exception aux autres surfaces. [DS1.3.]
  - **SA-12** — Obstacle connu sur la trajectoire : engagement interdit, sauf pour les cibles offensives permises. Obstacle inconnu : saut engagé, puis collision, arrêt et révélation à l'impact. [P08 (M).]
  - **SA-13** — En vol : aucune modification volontaire de destination ni d'impulsion ; vitesse horizontale constante tant qu'aucun contact ne la modifie ; fin de l'action à une réception stable, sans glissement automatique. [nouveau.]
  - **SA-14** — Le saut s'arrête au premier choc ; la collision et les chutes qui suivent sont des événements distincts, résolus dans l'ordre chronologique. [DS5.2 ; D13 (M).]
  - **SA-15** — Chaque type d'unité a une impulsion verticale et une capacité d'impulsion horizontale distinctes et configurables. [P02, P03 (M).] Ouvert : valeurs par type.
  - **SA-16** — Loi : impulsion constante à effort égal. Pour une unité donnée et des conditions comparables, la vitesse initiale varie en raison inverse de sa masse totale, `v = v_ref × (M_ref/M)`. À gravité constante, la hauteur varie comme le carré du rapport des masses ; la portée diminue aussi quand la masse augmente. [DS2.1 ; tranche E11 (quantité de mouvement) ; écarte la recommandation E11 du LOT-2G.] Ouvert : `M_ref`, `v_ref` par type.
  - **SA-17** — La gravité influe sur la durée de vol, la hauteur et la portée. Chaque type d'unité a sa plage de gravité où il peut sauter. [P01 (M) ; DS2.4 (plage par type au lieu d'une plage unique).] Ouvert : bornes.
  - **SA-18** — Aucun saut balistique à 0 g ; l'apesanteur est hors périmètre. Une chute involontaire reste possible en gravité positive, même quand les sauts sont interdits. Une gravité négative est invalide. [DS2.4 ; E3 (LOT-2F).]
  - **SA-19** — Référence à 1 g, pour l'unité de référence : sommet à un quart d'étage, soit **0,75 m** avec 3 m par étage ; portée de 2 cases de Manhattan **au même niveau**, pour franchir un trou d'une case ; portée pour un étage de descente **supérieure à 2 cases**, valeur à calculer. Ce sommet de saut n'est pas un seuil de blessure (CH-09). [P04 (M) inchangée ; **remplace** P05 (M) et la portée de DS2.3 ; 0,75 m selon A3A.] Ouvert : valeur de la portée en descente.
  - **SA-20** — À capacités égales, un saut au même niveau a une durée de vol et une portée inférieures à un saut avec un étage de descente. [conséquence de SA-16 à SA-19.]
  - **SA-21** — Portée horizontale `|Δx| + |Δy|`, plafond entier arrondi vers le bas. Aucune portée minimale garantie quand le calcul donne moins d'une case. [P05 (M) ; DS2.2 ; tranche la conversion de E2.]
  - **SA-22** — Distance pour les TU : `d_3D = |Δx| + |Δy| + |Δz|`, distincte de la portée horizontale. [précise DS5.6 (« distance de Manhattan »).]
  - **SA-23** — `TU_simple = d_3D × C_saut`. [nouveau.] Ouvert : `C_saut` ; coût non entier.
  - **SA-24** — `TU_attaque = d_3D × C_saut + max(1, ⌊0,20 × TU_max⌋)`. [J09 (M) ; DS5.6.] Ouvert : `C_saut` ; coût non entier.
  - **SA-25** — `C_saut` est propre aux sauts, indépendant de la marche ; sa valeur est explicitement reportée à l'équilibrage. [E13 (LOT-2F).] Ouvert : valeur.
  - **SA-26** — Coût payé en entier à l'engagement, même si le saut est interrompu ou si la cible esquive ; aucun remboursement. Une chute passive qui suit la destination choisie ne coûte pas de TU en plus. [J09 (M) ; DS5.6.]
  - **SA-27** — Une action sans TU suffisantes est interdite. Destination, coût et trajectoire sont prévisualisés dans les limites des informations connues. [J10, I02 (M).]

- **Chutes et réception**
  - **CH-01** — Un saut volontaire (simple ou offensif), sans surcharge, n'inflige pas de dégâts de réception au sol : au **même niveau**, même si la trajectoire monte puis redescend ; d'**un étage** vers le bas. Pour un saut d'un étage vers le bas, avec ou sans surcharge, la hauteur comptée est l'écart entre le sol de départ et le sol d'arrivée (3 m), sans ajouter la montée au sommet ; en surcharge, cette hauteur est majorée, et des dégâts sont possibles (CH-02, CH-18). Un choc contre une unité est une collision, calculée à part (CH-04). [précise DS3.1 (« volontaire ») ; N7 (R) ; A3A, A4.2A, A4.3A, exception de surcharge : « un étage » défini, saut au même niveau ajouté ; collision calculée à part : A25.]
  - **CH-02** — En surcharge, un saut volontaire d'un étage peut produire des dégâts. [DS3.1, DS3.2 ; confirmé par l'exception de surcharge : dégâts possibles même à 3 m.]
  - **CH-03** — Une chute **involontaire**, prévue ou subie par surprise, suit le seuil de CH-09 : sans surcharge, sans vitesse descendante héritée et sans collision, une chute de 3 m au plus, soit un étage, n'inflige pas de dégâts de chute ; au-delà, des dégâts sont possibles. [**remplace** D01 (M), repris par la consolidation du 14 novembre 2026 (blessure possible dès un étage, même sans surcharge) : A4.1D, D3A ; rejoint DS3.1 pour une chute ordinaire d'un étage.]
  - **CH-04** — Une réception sur une unité est une collision, distincte d'une réception au sol : ses dégâts sont calculés à part, et les deux unités peuvent être blessées, même si la réception de l'unité qui tombe est exemptée (CH-01). Le bonus offensif ne vaut que pour l'attaque sautée. [DS3.4 ; K01, K02, D08 (M) ; **restreint** DS3.1 : l'exemption ne protège pas des dégâts de collision ; confirmé : A25.]
  - **CH-05** — Si la cible esquive, l'attaquant finit son saut au sol : ce saut reste **volontaire**, sa réception est comptée entre le sol de départ et le sol d'arrivée, et l'exemption d'un étage sans surcharge s'applique (CH-01). L'esquive ne transforme pas cette réception en chute involontaire. [E18 (P) ; DS3.1 ; mesure entre les sols : A4.3A.]
  - **CH-06** — Si un obstacle interrompt la trajectoire puis provoque une nouvelle chute, cette chute est **involontaire** ; collision et chute sont comptées séparément. [D13 (M).]
  - **CH-07** — Au-delà du seuil de 3 m, la puissance d'une chute au sol dépend de la hauteur équivalente et de la gravité (CH-10), selon une courbe **à recalibrer lors des tests** ; aucune valeur n'est fixée. [**remplace**, comme barème, la courbe `B(n)` de D03 et D04 (M), reprise par la consolidation du 14 novembre 2026 : D1C ; cette courbe reste historique, sans décalage d'un étage.] Ouvert : courbe et valeurs (A29).
  - **CH-08** — Hauteurs en mètres, fractions comprises, avec 3 m entre deux sols d'étages consécutifs. Trois grandeurs sont distinctes : l'écart entre le sol de départ et le sol d'arrivée ; la trajectoire, avec la montée et le sommet d'un saut ; la hauteur équivalente utilisée pour les dégâts (CH-09 à CH-11, CH-16). Pour une chute, la hauteur parcourue est la hauteur réelle ; pour un saut volontaire, la hauteur comptée suit CH-01 et CH-11. [nouveau ; tranche le comptage de E12 pour les dégâts ; A3A, A4.3A ; l'interpolation linéaire entre les points `B(n)` de la consolidation du 14 novembre 2026 devient historique avec eux.] Ouvert : sauts non couverts par CH-01 (A30).
  - **CH-09** — Seuil des dégâts de chute ordinaires : **3 m inclus** de hauteur équivalente, quelle que soit la gravité positive. Une chute ordinaire de 3 m au plus, sans surcharge ni vitesse descendante héritée, n'inflige aucun dégât de chute ; une collision distincte reste possible (CH-04). Au-delà de 3 m, des dégâts sont possibles, sans être garantis (CH-07). [**remplace** le seuil de 0,25 étage de la consolidation du 14 novembre 2026 et son interpolation : A4.1D, D1C, D3A ; précise N7 (R) ; tranche « moins d'un étage » (DS3).]
  - **CH-10** — En gravité positive, la gravité module les dégâts **au-delà** du seuil de 3 m, sans modifier ce seuil. Le facteur `g/g0`, avec `g0 = 1 g`, reste la référence ; son point d'application et l'absence de double comptage avec la hauteur équivalente (CH-11) sont à vérifier. La précision décimale est gardée jusqu'aux arrondis prévus. [**modifie** D03, qui ne dépendait pas de la gravité ; la gravité ne déplace pas le seuil : D3A.] Ouvert : point d'application, double comptage (A5).
  - **CH-11** — Une vitesse verticale descendante **héritée**, par exemple après la traversée d'un support, accroît la hauteur équivalente, donc les dégâts possibles : `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 3 m porte sur `H_eq`. Pour un saut volontaire d'un étage vers le bas, avec ou sans surcharge, et pour un saut au même niveau sans surcharge, la montée et le sommet ne sont pas ajoutés (CH-01). Pour une autre vitesse initiale montante, la montée, le sommet et la descente sont résolus physiquement, avec la vitesse réelle à l'impact ; l'application de cette règle aux sauts volontaires que CH-01 ne couvre pas (plus d'un étage, même niveau en surcharge), et à un saut exempté qui se poursuit en chute, reste ouverte (A30). [nouveau ; vitesse héritée confirmée : D4A ; le seuil de 0,25 de la consolidation du 14 novembre 2026 est remplacé par celui de 3 m ; montée non comptée : A4.2A, A4.3A.] Ouvert : combinaison avec la surcharge et la gravité (A5) ; tolérance de la comparaison au seuil (A29) ; sauts non couverts par CH-01, saut exempté suivi d'une chute, réception de l'attaquant après un choc (A30).
  - **CH-12** — Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse verticale ; la vitesse horizontale compte contre les surfaces qui lui sont normales. [D11 (M).]
  - **CH-13** — Plafond de puissance de base 70 pour une chute au sol, limite précédemment validée. La surcharge n'agit plus sur la puissance après ce plafond : elle majore la hauteur équivalente (CH-16, CH-17). Les plafonds 60 (unité qui tombe), 80 (cible percutée) et 70 (obstacle) restent pour leurs domaines. Leur interaction avec la courbe à recalibrer, la hauteur majorée et les arrondis reste à vérifier. [D05 (M) ; déroge à D09 (M), qui plaçait les facteurs de poids après le tirage ; la surcharge passe sur la hauteur équivalente : D2A.] Ouvert : interaction avec la courbe, la hauteur majorée et les arrondis ; portée de D1C sur les plafonds (A6, A29).
  - **CH-14** — Capacité de portage en kg selon la Force ; seuil de surcharge commun à N14. [DS3.2 ; N14 (R).] Ouvert : modèle Force → kg.
  - **CH-15** — Dépassement relatif `S = max(0, charge / capacité − 1)`, avec une capacité strictement positive. [nouveau.]
  - **CH-16** — Coefficient `F_surcharge = min(2, 1 + 0,5 × S)`, inchangé. Il majore la hauteur équivalente de chute. [nouveau ; tranche E24 pour le poids au sol ; appliqué à la hauteur équivalente, et non plus à la puissance : D2A.] Ouvert : combinaison avec la vitesse héritée et la gravité (A5) ; portée de D1C sur le plafond 2 (A29).
  - **CH-17** — Pour une chute, ce coefficient n'est appliqué qu'une fois, à la hauteur équivalente : il n'est pas réappliqué à la puissance. La puissance obtenue sert aux blessures et à l'étourdissement ; l'armure applique ensuite ses protections. [N9, N10 (R) ; **remplace**, pour une chute, l'aggravation de la puissance par la surcharge (la consolidation du 14 novembre 2026) : D2A ; collisions : CO-09, A6.]
  - **CH-18** — La surcharge ne supprime pas le seuil de 3 m : elle majore la hauteur équivalente qui lui est comparée. En surcharge, une chute ou un saut d'un étage peut donc blesser, même à 3 m. [nouveau ; le seuil de 0,25 de la consolidation du 14 novembre 2026 est remplacé par celui de 3 m ; exception de surcharge.]
  - **CH-19** — La nature du sol ne modifie pas directement les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol. [D02 (M).]
  - **CH-20** — L'impact peut endommager ou détruire le support ; s'il cède, la chute continue. Chaque impact successif est résolu à part, et les dommages corporels peuvent s'additionner. [D12, D13 (M).]
  - **CH-21** — Traverser une surface destructible absorbe de l'énergie et ralentit le corps ; la gravité peut ensuite le réaccélérer. [nouveau.] Ouvert : formule de perte d'énergie.

- **Collisions et dégâts**
  - **CO-01** — Détection des contacts sur les volumes réels au moment du contact, y compris après un déplacement d'esquive ou une perte de support. [DS1.2.]
  - **CO-02** — Puissance de base `P = K × v_n²`, où `v_n` est la composante normale de la vitesse relative au contact (entre deux unités, ou contre une surface fixe). Deux coefficients distincts et configurables : `K_unités` et `K_obstacles`. [étend DS4.2 aux collisions entre unités ; D10 (M).] Ouvert : `K_unités`, `K_obstacles`.
  - **CO-03** — Entre unités, facteur appliqué aux dégâts reçus par chacune : `F_i = clamp(√(M_autre/M_i), 0,75 ; 1,5)`, masses strictement positives. [DS4.1 ; K08 (M) ; formule E6 du LOT-2G non reprise ; interaction avec le tirage commun réglée : A8A.]
  - **CO-04** — Contre le décor : référence du LOT-2F `min(M/80, 3)` pour le facteur de masse, et plafond de 70. Le point d'insertion de ce facteur dans la nouvelle chaîne reste à revoir. [D10, D05 (M).] Ouvert : point d'insertion (A7).
  - **CO-05** — Type de dégâts « impact » propre à Bastion : zones corporelles exposées et protections d'armure liées à la direction du choc, sans recopier de code ni de données d'OXCE. [DS4.4 ; D07 (LOT-2F, ouverte : E7).] Ouvert : protections par zone.
  - **CO-06** — Blessures et étourdissement sont des effets séparés ; une armure peut protéger plus la santé que l'étourdissement ; on peut être étourdi sans perdre de santé. [K02 (M).] Ouvert : coefficients santé / étourdissement.
  - **CO-07** — Chaque type d'unité a une sensibilité à l'étourdissement ; 0 vaut immunité aux étourdissements d'impact. Une unité consciente mais étourdie peut encore tenter une esquive, avec des Réactions réduites. [nouveau.] Ouvert : pénalité sur les Réactions.
  - **CO-08** — Tirage d'intensité de 50 à 150 %, **une fois par événement de collision**, partagé par les deux unités d'une collision entre unités, ou par l'unité et l'obstacle. Résistances et effets s'appliquent ensuite à chacun. Des collisions réellement distinctes, même rapprochées, ont des tirages distincts. Conséquence assumée : entre deux unités, ce tirage commun ne peut pas, à lui seul, inverser le rapport de leurs puissances avant protections ; leurs protections individuelles s'appliquent ensuite. [D06 (M) ; **étend** DS4.5 aux collisions entre unités ; confirmé, avec son écart à DS4.1 : A8A.] Ouvert : nature et normalisation du tirage (A26).
  - **CO-09** — Ordre : puissance initiale (pour une chute, calculée sur la hauteur équivalente déjà majorée par la surcharge, CH-16) ; facteur de gravité s'il s'applique, au-delà du seuil (CH-10) ; plafond de base ; bonus d'attaque applicable ; arrondi au plus proche, moitié vers le haut ; tirage ; facteur de masse s'il s'applique ; second arrondi ; puis effets et protections séparés pour la santé et l'étourdissement. Pour une chute, la surcharge n'est plus un bonus appliqué à la puissance (CH-17) ; son application éventuelle aux collisions reste ouverte (A6). Surcharge, gravité et masse ne sont comptées qu'une fois chacune ; les termes D09 et D10, et la combinaison de la vitesse héritée, de la surcharge et de la gravité, restent à réconcilier. [DS3.5 ; D10 (M) ; déroge à D09 (M) : la surcharge, facteur lié au poids, précède le tirage ; surcharge sur la hauteur équivalente et gravité au-delà du seuil : D2A, D3A.] Ouvert : réconciliation (A5 à A7) ; détail des deux arrondis et du tirage (A26).
  - **CO-10** — Bonus × 1,25 uniquement sur les dégâts infligés à la cible d'une attaque sautée, après le plafond et avant le tirage ; jamais pour l'attaquant. Une cible alliée ou neutre cachée le reçoit aussi. [J08, J11, J12, D08 (M).]
  - **CO-11** — Contacts simultanés d'un même choc : les surfaces peuvent être endommagées, sans dupliquer la puissance corporelle. Contre plusieurs unités distinctes : un calcul par cible, regroupé au besoin dans un même événement. [nouveau.] Ouvert : détails d'implémentation.

- **Esquives réactives**
  - **ES-01** — Le moteur déclenche la tentative tout seul, sans le joueur ; la réussite n'est pas automatique : elle dépend d'un tirage et des Réactions. [K03, K05 (M) ; DS5.7 ; précision du propriétaire du 14 novembre 2026.]
  - **ES-02** — Conditions : menace vue **juste avant l'impact**, TU suffisantes, case admissible. Une unité qui découvre la menace pendant la chute peut tenter l'esquive. [K03 (M) ; DS5.7.] Ouvert : instant exact (A15).
  - **ES-03** — Bonus de + 10 points si l'unité menacée voyait la menace **dès le départ** du saut ou dès le début d'une chute involontaire ; sinon 0. Même logique pour les corps qui tombent, selon ce que perçoit la cible. [nouveau.]
  - **ES-04** — Bonus de + 5 points par étage, `n = |z_départ − z_arrivée|`, pour une menace qui descend. [K05 (M).] Ouvert : `n` pour un impact à hauteur intermédiaire.
  - **ES-05** — `P = clamp(R_effectif + B_visibilité + 5n, 0, 100)` %, où `R_effectif` est la valeur des Réactions après une éventuelle pénalité d'étourdissement. [K05 (M) ; DS5.7.] Ouvert : pénalité d'étourdissement.
  - **ES-06** — Tirage entier uniforme `t` dans {1, …, 100} ; réussite si `t ≤ P`. [nouveau ; LOT-2G (E12 e) non repris.] Ouvert : `P` non entier.
  - **ES-07** — Une unité inconsciente ou morte n'esquive pas ; les corps qui tombent peuvent, eux, être esquivés. [nouveau.]
  - **ES-08** — Déplacement vers l'une des 8 cases voisines du même niveau, diagonales comprises, avec un support valide ; pas de saut dans le vide en esquivant. [DS5.7.]
  - **ES-09** — Coût habituel de la marche vers la case choisie (terrain, facteur diagonal), payé avec les TU restantes, même pendant le tour adverse. [DS5.7 ; S2 (R).] Ouvert : coûts de terrain (`MEC-0001`).
  - **ES-10** — Esquive réussie et effectivement faite : TU débitées. Échec du tirage ou déplacement impossible : aucun débit. [K06, K07 (M).]
  - **ES-11** — Choix aléatoire uniforme parmi les destinations admissibles. Une information cachée ne permet pas de choisir une case. La découverte d'un obstacle bloque et révèle la tentative, sans débit de TU. [K04 (M) ; tranche E22 (loi uniforme).]
  - **ES-12** — Pas d'échange simultané de cases ni de volumes qui se traversent ; destination libre au début de la résolution. Esquives en conflit : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager au hasard les combinaisons équivalentes. [nouveau.] Ouvert : algorithme (A17).
  - **ES-13** — Plusieurs menaces visibles et simultanées sur une même unité dans un même événement : une seule tentative ; la case doit éviter toutes les menaces **connues** ; `n` vient de la menace visible qui tombe du plus d'étages. Les menaces cachées ne comptent pas dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée. [nouveau.]
  - **ES-14** — Dangers successifs : nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte suit le moteur séquentiel. [nouveau.]

- **Repoussement et retombées**
  - **RP-01** — Esquive réussie : déplacement volontaire, pas de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un repoussement **après** l'impact. [**tranche** le point « à vérifier » K07 (M) / DS5.3 ; confirmé : A27.]
  - **RP-02** — Cible touchée : repoussement en priorité dans la direction de l'impact, sinon vers les directions voisines les plus proches, égalités tirées au hasard. Une case au-dessus du vide est admissible pour un repoussement forcé et entraîne une chute involontaire. [précise DS5.3.]
  - **RP-03** — Une case occupée par une autre unité n'est pas admissible : pas de repoussement en chaîne. [S10 (R).]
  - **RP-04** — Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort garde sa masse et son volume. [tranche « cible hors de combat » (DS5).]
  - **RP-05** — Si la cible ne peut pas être repoussée, l'attaquant cherche une case adjacente (8 voisines) pour retomber, en priorité du côté d'où il vient, puis par proximité de direction ; pas de recherche au-delà. [précise DS5.4 (rayon : cases adjacentes).]
  - **RP-06** — Impossibilité entièrement connue avant l'engagement : l'attaque sautée est refusée, sans révéler de données cachées. Impossibilité révélée en vol : l'attaquant s'arrête au contact, puis retombe verticalement depuis sa dernière position libre, sans pénétrer la cible. [nouveau.] Ouvert : issue de la retombée (A19).
  - **RP-07** — Une collision accidentelle, un cadavre ou un corps inconscient peut repousser ; aucune intention n'est requise, et aucun bonus offensif n'est créé. [nouveau.]
  - **RP-08** — Plusieurs impacts vraiment simultanés : la direction du repoussement combine intensités et directions ; cela n'introduit pas d'attaques volontaires simultanées. [nouveau.]
  - **RP-09** — Après le repoussement de la cible, l'attaquant prend la case initiale de la cible. **Maintenue de DS5.3** : la consolidation du 14 novembre ne la redit pas, mais la suppose (RP-05) ; maintien confirmé par le propriétaire. [DS5.3 ; maintien confirmé : A18.]

- **Environnement destructible et événements**
  - **EN-01** — Murs, portes, planchers et autres décors destructibles ont des points de résistance **cumulatifs** : les dégâts successifs les réduisent. Les éléments indestructibles restent intacts. [**modifie** D12 (M), qui suivait le seuil sans cumul d'OXCE.] Ouvert : résistances, unité des dégâts du terrain.
  - **EN-02** — Tant que leur résistance reste strictement positive, les éléments gardent leur blocage et leurs collisions ; l'apparence peut changer, sans fissure fonctionnelle automatique. [nouveau.]
  - **EN-03** — À zéro : destruction immédiate ; perte de support et chutes immédiates. Pas d'effondrement automatique des éléments voisins. [D12 (M) ; PE-03.]
  - **EN-04** — Un même événement qui produit plusieurs impacts simultanés sur un même plancher additionne leurs dégâts avant de décider de la destruction ; à distinguer de chutes successives. [nouveau.]
  - **EN-05** — Tour par tour : une action offensive volontaire est résolue jusqu'au bout avant l'action de combat suivante. [DS5.1.]
  - **EN-06** — Si plusieurs unités perdent leur support à cause d'un même événement, leurs chutes sont traitées **l'une après l'autre**, dans un ordre stable (par exemple les identifiants internes), en file FIFO ; les nouvelles chutes passent après celles qui attendent. [précise DS5.1 et DS5.2 ; I03 (M).] Ouvert : clé d'ordre ; articulation avec la chronologie.
  - **EN-07** — À chaque traitement : réévaluer positions, vitesses, santé et supports ; annuler un événement devenu caduc ; un seul événement de chute en attente par unité. [nouveau.]
  - **EN-08** — Les corps morts ou inconscients peuvent tomber, heurter d'autres unités et provoquer dégâts, étourdissement ou repoussement. Un cadavre ne subit plus de pertes de santé ni d'étourdissement ; la destruction des corps est hors périmètre. [nouveau.]
  - **EN-09** — Les collisions d'un même événement peuvent toucher plusieurs surfaces ou cibles, sans réintroduire plusieurs actions offensives simultanées. [nouveau.]
  - **EN-10** — Hasard contrôlable par une graine ; ordre de traitement déterministe en dehors du hasard choisi ; tests reproductibles. [nouveau.]

#### Décisions antérieures remplacées ou modifiées

Ces décisions restent dans leurs sources d'origine, comme historique ; elles ne sont pas effacées.

- P05 et la portée de DS2.3 (deux cases pour une descente d'un étage) : remplacées par SA-19 (deux cases au même niveau).
- D01 (chute blessante possible dès un étage) : remplacée ; une chute ordinaire de 3 m au plus ne blesse pas (CH-03, CH-09).
- D03 et D04 (courbe `B(n)` selon le nombre d'étages, sans gravité) : la courbe n'est plus un barème ; elle reste historique, sans décalage d'un étage ; au-delà de 3 m, la puissance est à recalibrer lors des tests (CH-07) et modulée par la gravité (CH-10).
- D09 (facteurs de poids après le tirage) : pour une chute, la surcharge, facteur lié au poids, majore la hauteur équivalente, donc avant le tirage (CH-13, CH-16, CO-09) ; son effet dans les collisions reste ouvert.
- D12 (résistance du terrain d'OXCE, sans cumul) : modifiée par EN-01 (résistance cumulative).
- DS1.1 (proportions, sans échelle en mètres) : la hauteur d'étage est fixée à 3 m (GE-02).
- DS3.1 (exemption d'un étage sans surcharge) : précisée ; une chute ordinaire de 3 m au plus ne blesse pas (CH-03, CH-09) ; un saut volontaire sans surcharge ne blesse pas à la réception, au même niveau ou d'un étage vers le bas (CH-01) ; l'exemption ne protège pas des dégâts d'une collision avec une unité, calculés à part (CH-04).
- DS4.5 (tirage commun entre l'unité et l'obstacle) : étendu aux collisions entre unités (CO-08) ; l'écart avec DS4.1 est assumé.
- Seuil de 0,25 étage, interpolation jusqu'à la base 8 et multiplicateur de surcharge appliqué à la puissance d'une chute, proposés par la consolidation du 14 novembre 2026 : remplacés le même jour par le seuil de 3 m (CH-09) et par la majoration de la hauteur équivalente (CH-16, CH-17).
- DS5.5 (grandes unités exclues de l'attaque sautée, comme sauteurs et comme cibles) : étendu à tout saut volontaire (GE-08) ; l'exclusion comme cible est maintenue (GE-09).
- DS5.3 (l'attaquant prend la case de la cible repoussée) : maintenue (RP-09).
- DS5.6 (coût proportionnel à la distance de Manhattan) : distance 3D pour les TU, et saut simple sans supplément (SA-22 à SA-24).
- Recommandation E11 du LOT-2G (même vitesse pour toutes les masses) : écartée par SA-16.

#### Encore ouvert

- Géométrie : largeur de case et rapport case/étage (la hauteur d'étage est fixée à 3 m) ; dimensions des unités par type et par posture ; épaisseur des surfaces ; tolérance des contacts.
- Sauts : masses et capacités de référence par type ; calibrage horizontal et portée en descente ; plage de gravité par type et très faible gravité ; valeur de `C_saut` ; coût en TU non entier.
- Force et charge : capacité de portage en kg selon la Force ; cohérence avec N14 ; masses des corps et des objets.
- Chutes : courbe de puissance au-delà de 3 m, à recalibrer lors des tests, et portée de ce recalibrage sur les plafonds de puissance et sur le plafond 2 de `F_surcharge` ; tolérance numérique de la comparaison au seuil quand la hauteur équivalente est calculée ; combinaison de la vitesse héritée, de la surcharge et de la gravité (ordre, point d'application de `g/g0`, absence de double comptage) ; hauteur comptée pour un saut volontaire de plus d'un étage et pour un saut au même niveau en surcharge ; suite d'un saut exempté qui se poursuit en chute, si le support de réception cède ou si la destination est sans support ; réception de l'attaquant après un choc contre sa cible : réception exemptée, ou chute consécutive distincte avec vitesse résiduelle.
- Dégâts : `K_unités`, `K_obstacles` ; absorption d'énergie des planchers ; conversion de la résistance en énergie ; protections par zone et direction ; coefficients de santé et d'étourdissement ; pénalité d'étourdissement sur les Réactions.
- Chaîne de calcul : place de `min(M/80, 3)` contre le décor ; surcharge dans les collisions ; interaction des plafonds 60, 70 et 80 avec les bonus, la gravité et la hauteur majorée par la surcharge ; nature et normalisation du tirage de 50 à 150 % ; détail des deux arrondis ; limites numériques éventuelles ; double comptage de la gravité, de la vitesse et de la masse.
- Vitesse après un choc qui interrompt le saut, et vitesse résiduelle après la traversée d'une surface.
- Esquive : instant où la menace est « vue » ; `n` pour un impact à hauteur intermédiaire ; probabilité non entière ; algorithme des esquives en conflit.
- Repoussement : retombée verticale de l'attaquant au-dessus de la cible (RP-06).
- Événements : ordre FIFO des chutes et chronologie physique ; clé d'ordre stable ; emplacement des cadavres ; collisions imbriquées et multi-cibles ; nombre maximal d'événements en chaîne.
- Décor : propriétés destructible ou indestructible, résistances initiales, unité des dégâts du terrain.
- Marche et TU : coûts des cases, capital et renouvellement des TU, visibilité, sous la responsabilité de `MEC-0001`.
- Décisions du 9 novembre 2026 et correctif du propriétaire (LOT-2F) : reprises ici par leurs identifiants, sans inscription propre.

Cette liste n'est pas exhaustive : tout ce que PE-01 à EN-10 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.
