# LOT-2E — Déplacements verticaux et chutes dans OXCE 8.7.1

| | |
|---|---|
| Mandat | `docs/mandates/BASTION-MANDAT-LOT-2E-v1.0.md`, branche `orchestration/mandats`, commit `1d88ffcb1c581a6b2ba11d9fe4b971114802fac3`. Lu sur GitHub avec l'outil GitHub de la session, ni recopié ni archivé. |
| Autorisation | Propriétaire, 8 novembre 2026. |
| Branche | `research/lot-2e-verticalite-oxce`, créée depuis `origin/main` = `4c884fb5da7d2bb9def4ba24c188f6ef8b40a7ad` (base attendue, revérifiée après `git fetch origin main`). |
| Référence | `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` (OXCE 8.7.1), règles `xcom1`, options par défaut, aucun mod. |
| Nature | Étude du code source, **sans exécution d'OXCE**. Aucune décision de `MEC-0001` modifiée, aucun gameplay, aucune reprise de code, de données ni d'assets (D4). |

## 1. Résumé

**Établi par lecture du code (VC), pour une unité de taille 1 :**
- **Escaliers** : il n'existe pas d'objet « escalier » ; chaque case a une hauteur de terrain.
  - Un pas horizontal fait **monter** d'un niveau quand l'unité part du haut d'une marche et que la case au-dessus de la case visée a un sol.
  - Il fait **descendre** d'un niveau quand la case visée n'a pas de sol et que la case en dessous est assez haute.
  - Coût : celui du sol d'arrivée, sans l'objet qui s'y trouve, plus 1 TU à la montée.
- **Échelles** : c'est un ajout d'OXCE. Un mur ou un objet qui porte l'indicateur « grav-lift » des données de terrain sert d'échelle ; on y monte et on en descend d'un niveau par pas. Aucune orientation n'est contrôlée.
- **Ascenseurs gravitationnels (grav-lifts)** : ce n'est pas un ascenseur mécanique. C'est un **sol marqué** : une unité passe d'un niveau à l'autre si la case de départ et celle d'arrivée ont toutes deux ce sol. Coût par défaut : 8 TU, 0 énergie.
- **Chutes** : une unité qui ne vole pas, au-dessus du niveau 0 et sans sol sous elle, tombe niveau par niveau jusqu'à un sol, **sans coût en TU ni en énergie**. Les causes : sol détruit, pas dans le vide, saut d'échelle interrompu, entre autres.
- **Unité dessous** : une chute planifiée ne vise jamais une case occupée par une unité connue. Une unité inconnue, ou présente sous une chute non planifiée, est écartée vers une case voisine ; à défaut, elle est **mise hors de combat** : assommée, ou tuée si elle n'est pas capturable.
- **Dégâts de chute** : **aucun calcul identifié dans le périmètre examiné** (§2). Dans ce périmètre, l'unité qui tombe ne subit aucun dégât, et rien ne fait intervenir la hauteur, la Force, l'armure ou le poids.

**Non établi :**
- la présence réelle d'escaliers, d'échelles, de grav-lifts et de cases sans sol dans les terrains `xcom1`. Elle dépend des fichiers de terrain `.MCD`, non lus, et de correctifs des règles (NV) ;
- les comportements observés en jeu : aucune exécution (aucun OE) ;
- l'absence universelle de dégâts de chute, dans tout le code ou avec des mods.

## 2. Méthode et périmètre

- **Code** : clone Git du commit exact (`git rev-parse HEAD` = `441cae1b071d249d40a223858cb6bd07fd5d791b`, aucune modification locale), lu en lecture seule. Les références `fichier:lignes` sont relatives à ce commit.
- **Statuts** :
  - **VC** : vérifié par lecture du code ;
  - **OE** : observé à l'exécution — **aucun dans ce lot** ;
  - **INF** : inférence tirée du code ;
  - **NV** : non vérifié.
- **Aucune exécution** : OXCE exige les ressources du jeu original, absentes (LOT-2A §1).
- **Données** :
  - les fichiers `.MCD` n'ont pas été lus (D4, provenance non vérifiée) ;
  - dans les règles `xcom1`, seuls des noms de clés et des couples clé–valeur ont été comptés, sans relever de valeur de terrain : `mcdPatches.rul`, `armors.rul` (`movementType`), `units.rul` (`capturable`) ;
  - `MCDPatch.cpp` ne reconnaît aucune clé pour l'indicateur grav-lift.
- **Fichiers lus en entier ou en grande partie** :
  - `src/Battlescape/UnitFallBState.cpp` (en entier) ;
  - `src/Battlescape/Pathfinding.cpp` (calcul des coûts, de la chute, des escaliers, de `validateUpDown`) ;
  - `src/Battlescape/UnitWalkBState.cpp` ;
  - `src/Battlescape/TileEngine.cpp` (`applyGravity`) ;
  - `src/Savegame/Tile.cpp` et `Tile.h` (cache d'une case) ;
  - `src/Savegame/BattleUnit.cpp` (`knockOut`, `instaKill`, marche) ;
  - `src/Battlescape/UnitDieBState.cpp` (mort d'une unité non capturable) ;
  - `src/Mod/Armor.h` (pourcentages de coût) ;
  - `src/Mod/MCDPatch.cpp` (clés reconnues) ;
  - `src/Mod/ModScript.h` (liste des points d'accroche des scripts).
- **Recherches obligatoires** (`grep -rl` sur `src/`, sensible à la casse, sauf mention), en nombre de fichiers :

| Terme | Fichiers | Résultat |
|---|---|---|
| `fallDamage`, `FallDamage` | 0 | Aucun |
| `falling` | 14 | Chute (`UnitWalkBState`, `UnitFallBState`, `Pathfinding`, `SavedBattleGame`, `TileEngine`, `BattlescapeGame`, `BattleUnit`), objets lancés (`ProjectileFlyBState`), animation de mort (`UnitDieBState`) ; aucun dégât |
| `gravity` | 5 | `applyGravity` : objets et unités qui tombent quand le sol disparaît ; aucun dégât |
| `noFloor`, `NoFloor` | 2 et 19 | Absence de sol (cache des cases, recherche de chemin, chute, correctifs de terrain) |
| `hasLadder`, `Ladder` | 4 et 5 | Échelles, sur un mur ou un objet portant l'indicateur grav-lift |
| `gravLift`, `GravLift` | 2 et 9 | Sol grav-lift ; pourcentage de coût `gravLiftPercent` |
| `climb`, `Climb` | 5 et 6 | Coûts de l'échelle, pourcentages d'armure |
| `applyDamage` | 2 | Défense de base sur la Géoscape, sans rapport |
| `height` (`-i`), `hit` (`-w`) | 179 et 40 | Termes trop généraux. Recherche ciblée (`-i`) de `height`, `damage` ou `hit` à moins de 40 caractères de `fall` : aucun résultat |
| Appels de `damage(` | — | `TileEngine.cpp:3148` (impact), `NextTurnState.cpp:459` (conditions d'environnement définies par mod), commandes de débogage ; aucun ne concerne une chute |
| « fall » dans `src/Mod` (`-i`) | — | Seulement des images de sprites et des « fallback » ; aucune clé de règle sur la chute |
| Scripts (`ModScript.h:334-417`) | — | Aucun point d'accroche dédié à la chute ou à l'atterrissage |

## 3. Comportement de référence par mécanisme

Pour une unité de taille 1, sauf mention contraire.

**Commun à la marche, aux escaliers, aux échelles et aux grav-lifts** (VC) :
- **Paiement** : TU et énergie sont payées au début de chaque pas (`src/Battlescape/UnitWalkBState.cpp:295-327`, `:376-383`).
- **Case d'arrivée** : une unité connue de celle qui bouge (de son camp, ou visible du joueur) la bloque (`src/Battlescape/Pathfinding.cpp:394`, `:868-885`).
- **Arrêts** : sur repérage d'un ennemi et sur tir de réaction, comme pour la marche (`UnitWalkBState.cpp:224-245`, LOT-2A §2 ligne 16).

### Escaliers

| # | Question | Comportement OXCE | Preuve | Statut |
|---|---|---|---|---|
| E1 | Représentation | Pas d'objet escalier : chaque case a une **hauteur de terrain**, la plus haute du sol et de l'objet. En voxels, plus la valeur est négative, plus c'est haut : −8 = marche basse, −16 = marche haute, −24 = hauteur pleine. | `src/Savegame/Tile.cpp:229-254` ; `src/Savegame/Tile.h:217-224` | VC |
| E2 | Montée | Depuis une case de hauteur ≤ −16, un pas horizontal mène à la case **au-dessus** de la case visée, si celle-ci a un sol. La condition « case au-dessus du départ sans sol » ne compte que pour les unités de 2 × 2. | `Pathfinding.cpp:322-326`, `:341-344`, `:368`, `:384-387`, `:479-491`, `:619-623` | VC |
| E3 | Descente | Un pas horizontal vers une case **sans sol**, dont la case en dessous a une hauteur ≤ −12, mène à cette case inférieure. | `Pathfinding.cpp:327-330`, `:369`, `:388-391`, `:624-627` | VC |
| E4 | Hauteur franchissable | Un pas ne peut pas monter de plus de 8 unités de hauteur de terrain. Une descente n'est pas bloquée par ce test. | `Pathfinding.cpp:318-319`, `:439-440`, `:488-489`, commentaire `:943-946` | VC |
| E5 | Coût | Sur un pas d'escalier :<br>- coût en TU du **sol** d'arrivée, sans l'objet qui s'y trouve ;<br>- en descente, sans les murs du côté de l'arrivée ;<br>- **+ 1 TU** quand l'arrivée est un niveau plus haut, ajouté **avant** le × 1,5 de la diagonale.<br>Énergie : 50 % du coût, comme la marche. Aucun surcoût lié à une pente sur un même niveau. | `Pathfinding.cpp:498-533`, `:554-577` ; LOT-2A §2 lignes 5 et 6 | VC (coûts des terrains `xcom1` : NV) |
| E6 | Destination | Le moteur corrige d'un niveau vers le haut la destination d'un clic :<br>- quand on vise la case juste au-delà du haut d'un escalier droit, depuis l'escalier ou devant lui, jusqu'à 3 cases ;<br>- quand on vise une case de hauteur −24.<br>Les formes −18 / −12 propres à TFTD existent aussi. | `Pathfinding.cpp:109-120`, `:1061-1121` (dont `:1073`, `:1086`) | VC |
| E7 | Diagonale | Le code n'interdit pas de monter un escalier en diagonale. | `Pathfinding.cpp:322-326` (pas de condition de direction) | INF |
| E8 | Présence dans `xcom1` | Les hauteurs viennent des fichiers `.MCD`, non lus. Les règles `xcom1` peuvent aussi les corriger : `mcdPatches.rul` contient 1 clé `terrainHeight` et 19 clés `noFloor`, appliquées par `MCDPatch.cpp`. | `src/Mod/MapDataSet.cpp:183` ; `src/Mod/MCDPatch.cpp:76-79`, `:116-119` | NV |

### Échelles

| # | Question | Comportement OXCE | Preuve | Statut |
|---|---|---|---|---|
| L1 | Représentation | Un **objet ou un mur** dont la donnée de terrain porte l'indicateur grav-lift est une échelle (sur un sol, le même indicateur désigne un grav-lift). | `src/Savegame/Tile.cpp:256-267` ; `src/Savegame/Tile.h:199-206` ; `MapDataSet.cpp:182` | VC |
| L2 | Accès et déclencheur | Unité de taille 1, sans vol, sur une case à échelle :<br>- vers le haut si la case du dessus n'a pas de sol ;<br>- vers le bas si la case de départ (avec échelle) n'a pas de sol.<br>On les commande par les boutons « monter » et « descendre », ou par un chemin. | `Pathfinding.cpp:311`, `:353-357`, `:1161-1169` ; `src/Battlescape/BattlescapeState.cpp:1141-1161` | VC (boutons) ; INF (chemin par clic, non observé) |
| L3 | Pas de chute | Une unité sur une case à échelle sans sol ne tombe pas. Cas particulier : un « saut » de l'échelle vers un rebord. | `Pathfinding.cpp:345-352` ; `src/Savegame/BattleUnit.cpp:3470` ; `UnitWalkBState.cpp:163-168` | VC |
| L4 | Coût | Le plus faible coût en TU des parties « échelle » de la case de départ, ou 8 s'il est nul. Puis pourcentages d'armure par défaut : 100 % en TU et 50 % en énergie, à la montée comme à la descente. | `Pathfinding.cpp:447-468`, `:665-668`, `:680-690` ; `src/Mod/Armor.h:142`, `:154-155` | VC |
| L5 | Orientation | Aucune orientation de l'unité n'est contrôlée. Une échelle posée sur un mur dispense du coût de ce mur. | `Pathfinding.cpp:498`, `:507`, `:516`, `:525` | VC |
| L6 | Interruption | Comme la marche, sauf pendant le saut d'échelle, où le tir de réaction n'est pas testé. | `UnitWalkBState.cpp:238` | VC |
| L7 | Présence dans `xcom1` | Elle dépend de l'indicateur dans les `.MCD` ; les règles `xcom1` ne peuvent pas le modifier. | `src/Mod/MCDPatch.cpp` (clés reconnues) | NV |

### Grav-lifts

| # | Question | Comportement OXCE | Preuve | Statut |
|---|---|---|---|---|
| G1 | Mécanisme | **Sol marqué**, pas un ascenseur mécanique : ni objet mobile, ni attente, ni capacité. Un pas vers le haut ou vers le bas est permis si la case de départ et celle d'arrivée ont toutes deux un sol grav-lift. Un niveau par pas. | `Pathfinding.cpp:1143-1158` | VC |
| G2 | Commande | Boutons « monter » et « descendre » : contrôle `validateUpDown`, puis chemin vers le niveau voisin. L'unité se relève d'abord si elle est agenouillée. La recherche de chemin explore aussi le haut et le bas : un clic sur un autre niveau peut passer par un grav-lift. | `BattlescapeState.cpp:1141-1161` ; `src/Battlescape/BattlescapeGame.cpp:2105-2124` ; `Pathfinding.cpp:221` | VC (boutons) ; INF (chemin par clic, non observé) |
| G3 | Coût | Base de 8 TU (`DEFAULT_MOVE_FLY_COST`), puis pourcentages grav-lift par défaut : 100 % en TU, **0 % en énergie**. | `src/Battlescape/Pathfinding.h:84` ; `Pathfinding.cpp:471`, `:703-706` ; `Armor.h:156` | VC |
| G4 | Effet annexe | Aux hauteurs de voxel 0 et 1, le moteur ne traite pas comme plancher un sol grav-lift posé sur un autre. L'effet sur les tirs et la vue dépend des formes de voxels des données. | `src/Battlescape/TileEngine.cpp:4560-4566` | VC (règle) ; INF (effet) |
| G5 | Présence dans `xcom1` | Elle dépend des `.MCD`. | — | NV |

### Vol et glissement (pour comparaison)

| # | Comportement OXCE | Preuve | Statut |
|---|---|---|---|
| V1 | Une unité volante (`MT_FLY`) ne tombe pas. Elle monte si la case du dessus n'a pas de sol (pas de toit) et descend si sa case n'en a pas. Coût : 8 TU de base, 100 % en TU, 0 % en énergie. | `Pathfinding.cpp:1161-1167`, `:691-701` ; `Armor.h:152-153` | VC |
| V2 | Dans `armors.rul` de `xcom1`, 9 armures déclarent `movementType: 1` (vol) et 4 `movementType: 2` (glissement, `MT_SLIDE`). Une unité qui glisse est traitée comme non volante, donc peut tomber. Elle paie les coûts de glissement (`TUSlide`) des données. | `src/Mod/MapData.h:44` ; `src/Mod/MapData.cpp:271-284` | VC (comptes de couples clé–valeur) |

### Chutes

| # | Question | Comportement OXCE | Preuve | Statut |
|---|---|---|---|---|
| C1 | Condition | Une unité qui ne vole pas, au-dessus du niveau 0, sans sol sous elle et entre deux pas, tombe. Une case dont la case inférieure a une hauteur −24 compte comme ayant un sol. | `src/Battlescape/UnitFallBState.cpp:95-98` ; `UnitWalkBState.cpp:160-169` ; `Pathfinding.cpp:1023-1029` ; `Tile.cpp:318-331` | VC |
| C2 | Déclencheurs involontaires | (a) Sol détruit par un impact ou une explosion. (b) Script qui change le type de déplacement. (c) Saut d'une échelle vers un rebord interrompu : l'unité tombe au lieu de s'arrêter (voir L3). (d) Capacité spéciale « brûle le sol » qui perce le sol. | (a) `TileEngine.cpp:3293-3296`, `:3515-3525`, `:5103-5157`. (b) `BattlescapeGame.cpp:975-980`. (c) `UnitWalkBState.cpp:127-138`, `:164-168`. (d) `UnitWalkBState.cpp:201-213`, `UnitFallBState.cpp:137-147` | VC |
| C3 | Chute « volontaire » | Aucune commande dédiée : le bouton « descendre » refuse un marcheur sans échelle ni grav-lift. En revanche :<br>- un pas vers une case sans sol est accepté (coût de base 4) ;<br>- un pas vers le bas depuis le vide coûte 0 ;<br>- une destination sans sol est abaissée jusqu'au sol inférieur.<br>Un clic peut donc produire un chemin qui passe le bord puis descend, à condition que la case d'arrivée ne soit pas occupée par une unité connue. | `Pathfinding.cpp:128-136`, `:138`, `:547-551`, `:655-658`, `:1130-1173` ; `BattlescapeState.cpp:1154-1161` | VC (chaque élément) ; INF (enchaînement, non observé) |
| C4 | Déroulement | Niveau par niveau, jusqu'à un sol ou au niveau 0. Le nombre de niveaux n'est pas limité. | `UnitFallBState.cpp:126-133` ; `UnitWalkBState.cpp:281-285`, `:370-374` | VC |
| C5 | Coût | **0 TU et 0 énergie**. La réserve de TU n'est pas contrôlée pendant la chute, et la chute due à la gravité ne paie rien. | `Pathfinding.cpp:655-658` ; `UnitWalkBState.cpp:324` ; `UnitFallBState.cpp:126-133` | VC |
| C6 | Interruption | **Pendant la chute** : pas d'arrêt sur repérage d'un ennemi, pas de tir de réaction. Les grenades de proximité sont testées à chaque niveau, et peuvent arrêter l'action.<br>**À l'atterrissage** : repérage possible (marche), grenades de proximité, éclairage, champ de vision, tir de réaction (annule le chemin si l'unité est visée). | `UnitWalkBState.cpp:221`, `:226-236`, `:238` ; `UnitFallBState.cpp:149-161` | VC |
| C7 | Unité dessous | **Chute planifiée** : la recherche de chemin refuse une case d'arrivée occupée par une unité connue (comme pour la marche).<br>**Unité inconnue, ou chute non planifiée** (par exemple un sol détruit) : l'unité de la case d'arrivée est écartée vers une case voisine libre, avec sol (ou si elle vole), sans dépense de TU. À défaut, elle est **mise hors de combat** :<br>- son étourdissement est porté au niveau de sa santé, ce qui l'assomme ;<br>- une unité non capturable est alors tuée ;<br>- une unité qui se transforme est d'abord convertie.<br>Dans `units.rul` de `xcom1`, 2 définitions portent `capturable: false`, toutes deux de grandes unités. Le calcul de chemin évite aussi une chute qui ferait intervenir une grande unité. | `Pathfinding.cpp:107`, `:138`, `:394`, `:868-885`, `:886-914` ; `UnitWalkBState.cpp:170-187` ; `UnitFallBState.cpp:100-123`, `:170-262` ; `BattleUnit.cpp:2078-2101`, `:4773-4778` ; `src/Battlescape/UnitDieBState.cpp:243-246` | VC |
| C8 | Dégâts à l'unité qui tombe | **Aucun calcul identifié dans le périmètre examiné** : pas d'appel de dégâts dans les fichiers de chute, ni clé de règle, ni point d'accroche de script (§2). Les seuls `hit` de ces fichiers relèvent de la capacité « brûle le sol ». | `UnitFallBState.cpp` (en entier) ; `UnitWalkBState.cpp:201-213` ; §2 | VC pour les fichiers examinés ; absence universelle : NV |
| C9 | Hauteur, Force, santé, armure, poids, objets | Aucun effet sur une chute identifié dans le périmètre examiné, faute de calcul de dégâts. Le poids ne réduit que les TU récupérées à chaque tour (LOT-2D). | Comme C8 ; `BattleUnit.cpp:2709-2726` | Comme C8 |
| C10 | Présence dans `xcom1` | Les cases sans sol dépendent des `.MCD` et des 19 correctifs `noFloor` de `mcdPatches.rul`. Des trous peuvent aussi apparaître par destruction (C2 a). | `MapDataSet.cpp:182` ; `MCDPatch.cpp:116-119` | NV (cartes précises) ; VC (mécanisme) |

## 4. Parcours types

Exemples **hypothétiques**. Coûts de terrain fictifs (`c` = coût d'un sol), à l'exception des constantes du code citées.

1. **Monter un escalier.** L'unité est sur la marche haute (hauteur −16) au niveau 0, et la case au-dessus de la case visée a un sol. Un pas l'amène au niveau 1, pour `c` + 1 TU, l'objet de la case d'arrivée n'étant pas compté (E2, E5).
2. **Prendre un grav-lift.** L'unité est sur un sol grav-lift au niveau 0, et la case au-dessus a aussi un sol grav-lift. « Monter » : un pas, 8 TU, 0 énergie, avec les pourcentages par défaut (G1, G3).
3. **Passer un bord.**
   ```
   niveau 1 :  U  [vide]
   niveau 0 :      D
   ```
   Un clic sur `D` donne un pas vers la case vide (base 4 TU, plus un éventuel objet), puis une descente à 0 TU (C3, C5). Enchaînement non observé.
   - Si une unité **connue** occupe `D`, le chemin est refusé.
   - Si elle est **inconnue**, elle est écartée ou mise hors de combat (C7).
4. **Sol détruit.** Une explosion détruit le sol sous une unité au niveau 2, avec du vide jusqu'au niveau 0. L'unité tombe de deux niveaux, sans coût ni dégât dans le périmètre examiné. À l'atterrissage, elle peut subir un tir de réaction (C2, C4 à C6, C8).

## 5. Cas limites, ambiguïtés et dépendances aux données

- **Niveau 0** : aucune chute possible (C1).
- **Case inférieure de hauteur −24** : elle sert de sol à la case du dessus (C1).
- **Saut d'échelle interrompu** : l'unité tombe au lieu de s'arrêter (C2 c, L3).
- **Unité non capturable sous une chute** : mise hors de combat puis tuée (C7).
- **Grandes unités** : hors périmètre. Un commentaire du code annonce leur exclusion des chutes, mais le code ne bloque que certains cas (`Pathfinding.cpp:886-914`). NV.
- **Échelles et grav-lifts** : même indicateur de données, sens différent selon la partie de la case (L1, G1). Leur présence dans `xcom1` dépend des `.MCD`, non lus (NV).
- **Escaliers et cases sans sol** : définis par les hauteurs et indicateurs des `.MCD`, éventuellement corrigés par `mcdPatches.rul` (E8, C10). Les formes propres à TFTD (−18 / −12) existent dans le moteur, sans usage attendu en `xcom1` (INF).
- **Ascenseur mécanique** : aucun mécanisme de ce type identifié ; le grav-lift est un sol marqué (G1).
- **Dégâts de chute** : aucun calcul dans le périmètre examiné. Un mod pourrait passer par des mécanismes généraux, mais aucun point d'accroche n'est dédié à la chute (§2 ; INF).

## 6. Comparaison avec `MEC-0001`

Les décisions du propriétaire restent acceptées : cette étude n'a **aucun pouvoir de les changer**. Catégories : similaire au comportement de référence établi ; écart volontaire ou potentiel ; non comparable ; à vérifier.

| Décision | Rapport à OXCE | Catégorie |
|---|---|---|
| N3 — Plusieurs niveaux (x, y, z) | Grille à trois dimensions (LOT-2A ; E2, E3) | Similaire |
| N4 — Escaliers | Principe présent, par hauteur de terrain (E1 à E6) ; présence dans `xcom1` NV | Similaire dans le principe ; présence à vérifier |
| N4 — Échelles | Présentes dans le moteur (L1 à L6) ; présence dans `xcom1` NV | Similaire dans le principe ; présence à vérifier |
| N4 — Ascenseurs | OXCE n'a que des grav-lifts, des sols marqués (G1) ; ce que Bastion entend par « ascenseur » n'est pas défini | Non comparable en l'état |
| N5 — Chutes involontaires | Présentes (C2) | Similaire |
| N5 — Chutes volontaires | Pas de commande dédiée, seulement un chemin qui passe un bord (C3, INF) | À vérifier ; écart potentiel selon le contrôle voulu |
| N6 — Dégâts croissants avec la hauteur | Aucun calcul identifié dans le périmètre examiné (C8) | Écart volontaire, dans le périmètre examiné |
| N7 — Pas de dégâts pour les petites chutes | Aucune chute ne blesse dans le périmètre examiné (C8) ; pas de seuil | Similaire, dans le périmètre examiné ; le seuil n'a pas d'équivalent |
| N8, N9, N10 — Caractéristiques, équipements, armure, poids lors d'une chute | Aucun effet identifié dans le périmètre examiné (C9) | Écart volontaire, dans le périmètre examiné |

**Point partiellement couvert par `MEC-0001`.** S10 rend infranchissable une case occupée. OXCE fait de même pour une chute **planifiée** vers une case occupée par une unité connue (C7). Rien dans `MEC-0001` ne règle le cas d'une chute sur une unité **inconnue**, ni celui d'une chute **non planifiée** (sol détruit) au-dessus d'une unité. OXCE écarte alors l'unité dessous ou la met hors de combat (C7).

## 7. Arbitrages futurs, par priorité

Classement selon leur importance pour jouer et tester. Aucun n'est tranché ici. « Règle » = forme du comportement ; « paramètres » = valeurs.

| Priorité | Sujet | Nature | Repère OXCE |
|---|---|---|---|
| 1 | Chute sur une unité inconnue, ou chute non planifiée au-dessus d'une unité | Règle à décider | Écartement, ou mise hors de combat (C7) |
| 2 | Déclenchement d'une chute volontaire (commande, confirmation, lien avec la zone atteignable Z1) | Règle à décider (interface liée) | Pas de commande ; chemin qui passe un bord (C3) |
| 3 | Sens de « ascenseur » dans Bastion | Règle à décider | Grav-lift = sol marqué (G1) |
| 4 | Dégâts de chute : forme de la règle (déclencheur, prise en compte de la hauteur), puis formule et seuil | Règle encore ouverte (principe décidé : N6, N7), puis paramètres | Aucun calcul identifié (C8) |
| 5 | Effets des caractéristiques, de l'armure et du poids sur une chute | Règle encore ouverte (principe décidé : N8 à N10), puis paramètres | Aucun effet identifié (C9) |
| 6 | Coûts des changements de niveau et des chutes : modèle, puis valeurs en TU et en énergie | Règle (modèle) encore ouverte, puis paramètres | Escalier : sol d'arrivée + 1 TU ; échelle : coût de la pièce ou 8 ; grav-lift : 8 TU sans énergie ; chute : 0 (E5, L4, G3, C5) |
| 7 | Interruptions pendant une chute | Règle à décider | Aucune pendant la chute, sauf grenades de proximité ; tir de réaction à l'arrivée (C6) |

## 8. Vérifications, limites et revue indépendante

**Vérifications exécutées.**

| Commande ou contrôle | Résultat | Code de sortie |
|---|---|---|
| `git fetch origin main` | `origin/main` = `4c884fb`, base attendue | 0 |
| `git rev-parse HEAD` et `git status --short` dans le clone OXCE | `441cae1b071d249d40a223858cb6bd07fd5d791b` ; aucune modification locale | 0 |
| Recherches obligatoires (`grep -rl` sur `src/`) | Tableau du §2 | 0 ou 1 selon le terme (1 = aucune correspondance) |
| Clés de `mcdPatches.rul`, `armors.rul` et `units.rul` (`xcom1`) | Comptées seulement, sans relever de valeurs de terrain | 0 |
| `git status --short` (Bastion) | Un seul fichier, non suivi : ce rapport | 0 |
| `git diff --check` (fichiers suivis) | Aucune sortie | 0 |
| `git diff --no-index --check /dev/null` sur ce rapport | Aucune erreur d'espacement | 1 (attendu : le fichier diffère de `/dev/null`) |
| Recherche d'espaces en fin de ligne (`grep -nP "[ \t]+$"`) | Aucune ligne | 1 (aucune correspondance) |

Tests .NET non lancés : non requis pour cette étude documentaire, et aucun code n'est modifié. L'état de la CI GitHub est relevé après publication, dans la PR.

**Limites.**
- Aucune exécution d'OXCE : aucun comportement observé.
- Les fichiers `.MCD` n'ont pas été lus : la présence d'escaliers, d'échelles, de grav-lifts et de cases sans sol dans `xcom1` n'est pas vérifiée.
- L'absence de dégâts de chute vaut pour le périmètre examiné, pas pour tout le code ni pour les mods.
- Les grandes unités, l'IA et TFTD sont hors périmètre.
- Aucun code, aucune donnée et aucun asset d'OXCE ne sont repris : seulement des références et des reformulations (D4).

**Revue indépendante.**
- **Relecteur** : agent distinct du développeur, en lecture seule (aucune écriture, aucun `fetch`). Il a lu le mandat sur GitHub, le rapport non commité, le registre de Bastion et le code OXCE au commit figé.
- **Contrôles** : plus de 50 références `fichier:lignes`, ainsi qu'une recherche indépendante des dégâts de chute. Celle-ci confirme : aucun calcul identifié dans le périmètre examiné, sans absence universelle.
- **Résultat** : 14 constats, dont 0 bloquant, 8 importants et 6 mineurs.
- **Tous intégrés**, après vérification dans le code par le développeur :
  - **constats importants :**
    - condition de montée d'escalier corrigée : le « trou au-dessus » ne concerne que les grandes unités (E2) ;
    - coût d'un pas d'escalier corrigé : objet non compté, murs d'arrivée non comptés en descente, + 1 avant le × 1,5 (E5) ;
    - unité non capturable tuée après mise hors de combat (C7) ;
    - chute planifiée refusée vers une unité connue ; l'écartement ne concerne que les unités inconnues ou les chutes non planifiées (C7, parcours 3, §6) ;
    - annulation au-dessus du vide limitée au saut d'échelle (C2 c) ;
    - moment de paiement, obstacles, interruptions, déclencheur et orientation des échelles ajoutés (encadré commun, L2, L5, L6) ;
    - dépendance aux correctifs `terrainHeight` et `noFloor` des règles `xcom1` (E8, C10) ;
    - preuves de fin complétées (§8) ;
  - **constats mineurs :**
    - grenades de proximité et repérage dans C6 ;
    - G4 reclassé en inférence pour l'effet ;
    - options de recherche précisées et ligne `falling` corrigée (§2) ;
    - catégories du §6 réduites aux quatre du mandat ;
    - « dans le périmètre examiné » ajouté ;
    - règles et paramètres distingués au §7 ;
    - références d'E1 et d'E6 précisées, glissement (V2), descente par échelle (L2), C5 complété.
- **Limites de la revue** : lecture de code seulement ; les `.MCD` n'ont pas été lus ; le relecteur est du même type que le développeur, et sa revue ne vaut pas validation.
