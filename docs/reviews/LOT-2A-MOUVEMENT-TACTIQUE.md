# LOT-2A — Étude du déplacement tactique à pied dans OXCE 8.7.1

| | |
|---|---|
| Mandat | `docs/mandates/BASTION-MANDAT-LOT-2A-v1.0.md`, branche `orchestration/mandats`, commit `3a7b1251ec816921ad65ec0522dd87fed38d9313`. Lu sur GitHub avec l'outil GitHub de la session, ni recopié ni archivé. |
| Autorisation | Propriétaire, 8 novembre 2026. |
| Branche | `research/lot-2a-mouvement-tactique`, créée depuis `main` = `8b1bc3f09b8d1e2b3d15df0ad3ebb6fecc0798bd` (base attendue par le mandat, revérifiée). |
| Référence | `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` (OXCE 8.7.1), règles `xcom1`, options par défaut, aucun mod (`docs/references/OXCE-BASELINE.md`). |
| Nature | Étude documentaire. **Aucun gameplay implémenté. Aucune fiche `MEC` créée. Aucune décision prise.** |

## 0. Résumé

- OXCE place les unités sur une grille de cases en trois dimensions. Une unité à pied se déplace selon 8 directions horizontales, en payant à chaque pas un coût en unités de temps (TU) qui dépend surtout de la case d'arrivée.
- La diagonale est permise ; elle coûte 1,5 fois le pas, tronqué à l'entier.
- Le chemin est calculé sans tenir compte des TU restantes. L'unité avance pas à pas et s'arrête dès que le pas suivant coûte plus que ce qui lui reste.
- Tout ce qui suit est **lu dans le code** au commit figé. **Rien n'a été exécuté** : OXCE exige les fichiers du jeu original, non disponibles. **Les coûts réels des terrains `xcom1` n'ont pas été relevés** : ils viennent de fichiers de terrain de provenance non vérifiée, exclus de toute reprise par D4.
- Le §4 propose un périmètre minimal pour `MEC-0001`. Le §5 liste 14 choix laissés au propriétaire : reproduire la référence ou s'en écarter volontairement.

## 1. Méthode et niveau de preuve

- **Source.** Code obtenu par Git au commit exact (`git fetch --depth 1 origin 441cae1b071d249d40a223858cb6bd07fd5d791b`). `git rev-parse HEAD` donne bien ce SHA (commit « OXCE 8.7.1 », Meridian, 2026-09-19).
- **Références.** Notées `fichier:lignes`, au commit figé, chemins relatifs à `src/` sauf mention contraire. Exemple de lien complet : `https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/src/Battlescape/Pathfinding.cpp#L573-L577`.
- **Statut de chaque affirmation :**
  - **VC** : vérifié dans le code, par lecture ;
  - **OE** : observé à l'exécution — **aucun cas dans ce lot** ;
  - **INF** : inférence tirée du code, non observée ;
  - **NV** : non vérifié.
- **Aucune exécution.** Le `README.md` d'OXCE (ligne 17) indique qu'OpenXcom exige une copie des ressources X-COM d'origine. Elles ne sont pas fournies, et D4 exclut leur reprise. Aucun binaire n'a été construit. Aucun comportement n'est donc « validé par une exécution ».
- **Coûts de terrain non relevés.** Le coût en TU de chaque sol, mur et objet est lu dans des fichiers de terrain `.MCD` (`Mod/MapDataSet.cpp:137`, `:181`) :
  - ceux du jeu original ;
  - 15 fichiers `.MCD` livrés par OXCE dans `bin/standard/xcom1/TERRAIN`. S'ajoutent-ils aux fichiers d'origine ou les remplacent-ils ? NV.

  Ces données sont ensuite corrigées par `bin/standard/xcom1/mcdPatches.rul`, appliqué juste après leur lecture (`Mod/MapDataSet.cpp:219-223` ; `Mod/MCDPatch.cpp:147-152`). Ce fichier contient 5 lignes `TUWalk` et 54 lignes `bigWall` ; seules ces lignes ont été comptées. Aucune valeur de ces fichiers n'a été relevée : leur provenance n'est pas vérifiée, et D4 exclut la reprise de données. Ce rapport ne donne donc aucune valeur réelle. Seules apparaissent les constantes du code, et des valeurs explicitement **hypothétiques** dans les scénarios.
- **Règles `xcom1`, armures.** Aucune surcharge des pourcentages de coût ni du coût de rotation n'a été trouvée. Recherche de `moveCost`, `turnBeforeFirstStep`, `turnCost`, `extendedMovementCostRounding` et `extendedRunningCost` dans `bin/standard/xcom1` et `bin/common` : aucun résultat (code de sortie 1). Les valeurs par défaut du code s'appliquent donc (INF : la recherche est textuelle). La recherche de `TUWalk` et `MCDPatches` trouve `mcdPatches.rul` (code de sortie 0) : voir le point précédent.
- **Périmètre lu.** Déplacement **à pied** (`MT_WALK`) d'une unité du **joueur**, **de taille 1**, en **marche normale**. L'IA, la sauvegarde et le multijoueur n'ont pas été étudiés.
- **Propriété intellectuelle (D4).** Aucun code, aucune donnée et aucune règle YAML d'OXCE ne sont copiés. Le rapport ne contient que des observations reformulées et des références courtes (noms de fichiers, de fonctions et de constantes).

## 2. Comportement de référence

| # | Question | Comportement OXCE | Preuve | Statut, limites | Décision à prendre |
|---|---|---|---|---|---|
| 1 | Position | Trois entiers `x`, `y`, `z` ; `z` est le niveau. Une case par position. | `Battlescape/Position.h:37` ; `Savegame/SavedBattleGame.h:256-259` | VC | P1 |
| 2 | Voisinage | 8 directions horizontales, numérotées de 0 (nord, `y` − 1) dans le sens horaire ; 8 = haut, 9 = bas. | `Battlescape/Pathfinding.h:42-45`, `:92-93`, `:229-244` | VC | P2 |
| 3 | Diagonale permise ? | Oui. Refusée si un mur mince concerné bloque, ou si une case orthogonale voisine porte un objet « grand mur » plein, ou diagonal en travers du pas. Un objet infranchissable ordinaire dans une case voisine ne l'empêche pas, une unité voisine non plus. | `Battlescape/Pathfinding.cpp:221`, `:825-840`, `:940-1003` ; types de grands murs : `Pathfinding.h:94-194` | VC pour les contrôles ; INF pour leurs conséquences. `mcdPatches.rul` modifie des indicateurs `bigWall` (§1) | P7 |
| 4 | Coût de la diagonale | Coût du pas multiplié par 1,5 et tronqué, avant l'ajout du coût des murs. | `Pathfinding.cpp:573-579` | VC | P3 |
| 5 | Coût d'un pas | TU du sol de la case d'arrivée + TU de l'objet qui s'y trouve. Total nul : 4. Case sans sol : base de 4, à laquelle s'ajoutent les coûts du sol et de l'objet. Montée d'un niveau : + 1. Murs franchissables traversés : moyenne de leurs coûts, ajoutée. 255 = infranchissable. Plafond : 100 par pas. | `Pathfinding.cpp:493-570`, `:613-614` ; `Pathfinding.h:82-88` | VC ; **valeurs `xcom1` non relevées** (§1) | P4, P5 |
| 6 | Modificateurs | Pourcentages portés par l'armure : la marche coûte 100 % du coût en TU et 50 % en énergie. Division entière (troncature). Coût final en TU borné entre 1 et 254. | `Mod/Armor.h:140-156` ; `Mod/Mod.cpp:315` ; `Pathfinding.cpp:660-759` | VC ; absence de surcharge : voir §1 | P11 |
| 7 | Modes de marche | Marche, course, pas de côté, marche furtive. L'option `strafe` est désactivée par défaut : Ctrl et Alt sont sans effet, le joueur ne dispose que de la marche. Maj fait ignorer les ennemis repérés, même par défaut. | `Engine/Options.cpp:274` ; `Battlescape/BattlescapeGame.cpp:1956-1996` | VC | Proposé : marche seule (§4, à décider) |
| 8 | Rotation | Tourner pendant la marche ne coûte rien. Avant le premier pas, la rotation coûte seulement si l'armure l'exige (`turnBeforeFirstStep`, faux par défaut) ou si une unité est repérée pendant la rotation. | `Battlescape/UnitWalkBState.cpp:329-335`, `:403-437` ; `Mod/Armor.cpp:41` | VC | P10 |
| 9 | TU insuffisantes | Le chemin est calculé sans regarder les TU restantes (plafond de 1000 TU pour l'A* ; aucun pour la ligne droite, voir ligne 14). Avant chaque pas, si son coût dépasse les TU (ou l'énergie) de l'unité, celle-ci s'arrête sur sa case, avec le message « pas assez de TU » (ou d'énergie). Les pas déjà faits restent payés. | `Pathfinding.h:205` ; `BattlescapeGame.cpp:1967`, `:1239-1242` ; `UnitWalkBState.cpp:295-322` | VC | P9 |
| 10 | Paiement | TU et énergie débités au début de chaque pas, avant l'animation. | `UnitWalkBState.cpp:376-383` ; `Savegame/BattleUnit.cpp:2320-2350` | VC | — |
| 11 | Obstacles | Une case a 4 parties : sol, mur ouest, mur nord, objet. Une partie bloque si son coût vaut 255. Un pas vers le nord teste le mur nord de la case de départ ; vers l'est, le mur ouest de la case d'arrivée, etc. Un pas qui monte de plus de 8 unités de hauteur de terrain est refusé ; ce test ne bloque pas une descente. | `Mod/MapData.h:46` ; `Savegame/Tile.cpp:299-310` ; `Pathfinding.cpp:318-319`, `:825-929`, `:940-1003` | VC | P6 |
| 12 | Occupation | Pour le calcul, une unité bloque sa case si elle est de la même faction, ou visible du joueur ; une unité hors de combat ne bloque pas. Une unité ennemie non vue ne bloque pas le calcul : la marche s'arrête avant sa case (contrôle avant chaque pas). | `Pathfinding.cpp:868-885` ; `UnitWalkBState.cpp:142-157`, `:355-367` | VC ; détail de la rotation et du repérage à cet instant : NV | P12 |
| 13 | Destination invalide | Clic sur une case portant une unité visible (les unités du joueur le sont toujours) : aucun calcul de chemin. Si elle est du camp qui joue, elle devient l'unité sélectionnée. Hors carte, sol ou objet infranchissable : aucun chemin, aucune marche, aucun TU dépensé, et aucun message trouvé sur ce chemin d'exécution. | `BattlescapeGame.cpp:1936-1953`, `:2004-2011` ; `Savegame/BattleUnit.cpp:3426-3431` ; `Pathfinding.cpp:92`, `:107`, `:138` | VC ; absence de message : INF | P14 |
| 14 | Calcul du chemin | D'abord une ligne droite (algorithme de Bresenham), retenue dès que tous ses pas ont un coût homogène, sans comparaison avec un détour et sans plafond de TU. Sinon A* sur 10 directions : priorité = 4 × coût cumulé en TU + 4 × distance euclidienne restante, soit environ 1 TU estimé par case restante. Un nœud déjà fermé n'est pas rouvert. | `Pathfinding.cpp:160-175`, `:188-243` (dont `:230`), `:1323-1455` (dont `:1419-1427`) ; `Battlescape/PathfindingNode.cpp:101` ; `Battlescape/PathfindingOpenSet.cpp:75` | VC. Chemin le moins coûteux non garanti : une ligne droite de cases uniformément chères peut l'emporter sur un détour moins cher (INF). Départage des égalités : NV | P8 |
| 15 | Ordre de déplacement | Options par défaut sur ordinateur (`battleNewPreviewPath` = aucun) : un clic sur une case lance la marche, sans aperçu. Si l'aperçu est activé : 1er clic = aperçu coloré, 2e clic = confirmation. Le commentaire de `Options.cpp:156` (« double-clic pour confirmer ») contredit le code, qui prévaut. Chaque pas recalcule son coût sur l'état courant de la carte. | `Engine/Options.cpp:153-157` ; `BattlescapeGame.cpp:1731`, `:1954-2011` ; `Pathfinding.cpp:1180-1311` ; `UnitWalkBState.cpp:295` | VC | Proposé : hors `MEC-0001` (à décider) |
| 16 | Arrêt et interruption | Arrêt quand le chemin est fini, si une nouvelle unité ennemie est repérée (sauf avec Maj), si l'unité essuie un tir de réaction, si le pas suivant devient impossible, ou sur annulation du joueur. L'annulation est sans effet pendant la rotation initiale, et n'agit que pendant le tour du joueur, une fois la panique traitée. | `UnitWalkBState.cpp:224-245`, `:301-304`, `:444-454`, `:459-515` ; `BattlescapeGame.cpp:1623-1685` | VC ; après annulation, le pas en cours s'achève : INF | P13 |

## 3. Scénarios de comportement attendu

**Aucun scénario n'a été exécuté.** Ils sont déduits de la lecture du code (§2).

Conditions communes :
- carte plane d'un seul niveau, sol uniforme sans objet ;
- unité du joueur de taille 1, en marche normale, options par défaut ;
- énergie suffisante pour tout le trajet ;
- aucune autre unité, sauf mention contraire ; aucune réserve de TU.

`c` désigne le coût en TU du sol, inconnu pour `xcom1`. La valeur `c = 4` n'est utilisée qu'à titre d'**exemple hypothétique**.

| # | Situation | Attendu selon le code | Lignes du §2 |
|---|---|---|---|
| S1 | Cas normal : de (5, 5) à (5, 2), soit 3 cases au nord, avec au moins 3c TU | 3 pas vers le nord ; coût total 3c TU ; énergie 3 × (c/2 tronqué) ; rotation initiale gratuite. Exemple : 12 TU et 6 d'énergie. | 2, 5, 6, 8, 10 |
| S2 | Diagonale : de (5, 5) à (7, 3) | Ligne droite homogène : 2 pas nord-est, coût 2 × (1,5c tronqué). Exemple : 12 TU, contre 16 pour 4 pas orthogonaux. | 3, 4, 14 |
| S3 | Destination bloquée : objet infranchissable (coût 255) sur la case cible | Aucun chemin. L'unité ne bouge pas et ne dépense rien ; aucun message trouvé. | 11, 13 |
| S3 bis | Clic sur une case portant une autre unité du joueur | Aucun calcul de chemin : l'unité cliquée devient l'unité sélectionnée. | 13 |
| S4 | TU insuffisantes : 5 cases au nord, avec 2c + 1 TU (c ≥ 2) | 2 pas, arrêt sur la 2e case, 1 TU restant, message « pas assez de TU ». | 9, 10 |
| S5 | Chemin bloqué : rangée infranchissable entre départ et destination, percée d'une ouverture | Ligne droite rejetée ; A* contourne par l'ouverture. Sans ouverture : aucun chemin, aucun mouvement. | 11, 14 |
| S6 | Diagonale entre deux cases voisines portant chacune un objet infranchissable | Objets ordinaires : diagonale permise. Objets « grand mur » pleins : diagonale refusée. | 3 |
| S7 | Unité ennemie non vue sur le trajet (hors du périmètre proposé) | Le chemin passe par sa case ; la marche s'arrête avant elle ; les pas déjà faits restent payés. | 12 |

## 4. Proposition de périmètre minimal pour `MEC-0001`

> **Projet soumis au propriétaire.** Ce n'est ni une fiche du registre ni une décision acceptée. Rien n'est implémenté. Les choix du §5 peuvent modifier ce projet.

Titre proposé : « `MEC-0001` — Déplacement élémentaire à pied ». Présentation selon le gabarit de `docs/gameplay/GAMEPLAY-DECISIONS.md` :

| Champ | Proposition |
|---|---|
| Système | Combat tactique : déplacement d'une unité à pied. |
| Description | Une unité se déplace de case en case vers une destination choisie, sur une carte à un seul niveau, en payant un coût en TU à chaque pas. |
| Classe | À choisir. `OXCE-REFERENCE` si les choix du §5 suivent tous la référence. En cas d'écart : `MODIFICATION-PROPOSEE` tant qu'il n'est pas accepté (n'autorise aucun changement de comportement), puis `MODIFICATION-VALIDEE` s'il est accepté (n'autorise que le périmètre décrit). |
| Fonctionnement de référence et preuves | Ce rapport (§2 et §3) : lecture du code au commit `441cae1`, sans exécution. |
| Périmètre proposé | Entre crochets : choix du §5 et option retenue **à titre de projet**.<br>1. Carte rectangulaire à un niveau ; cases repérées par deux entiers (x, y) ; hors carte = invalide. [P1 : un seul niveau]<br>2. Huit directions. [P2 : convention à fixer]<br>3. Chaque case est franchissable ou non, et porte un coût d'entrée en TU (entier ≥ 1). [P4 : coût unique par case ; P6 : cases bloquantes seulement]<br>4. Coût d'un pas = coût d'entrée de la case d'arrivée. [P3 : diagonale à choisir ; P7 : à choisir]<br>5. Une case occupée par une autre unité ne peut être ni traversée ni choisie comme destination ; toutes les unités sont connues. [P12 : unités toutes connues]<br>6. Chemin de coût total minimal, avec un départage déterministe. [P8 : coût minimal garanti]<br>7. L'unité dispose d'un capital de TU ; elle paie chaque pas avant de le faire. [P9 : règle d'arrêt à choisir]<br>8. Destination invalide ou inaccessible : aucun déplacement, aucun TU dépensé. [P14 : message à choisir]<br>9. Coûts de terrain propres à Bastion, sans revendication de fidélité aux valeurs. [P5 : valeurs propres] |
| Éléments exclus | Sujets du §6. Orientation (P10), énergie (P11) et interruptions (P13) : inclusion ou exclusion à décider. |
| Tests de référence | Scénarios S1 à S6, transposés avec des coûts propres à Bastion, déclarés comme tels. S6 dépend de P6 et P7. |
| Tests de modification | Un test par écart retenu au §5. |
| État d'implémentation | non commencé |

Les coûts de terrain d'OXCE n'étant pas connus, Bastion ne pourrait revendiquer qu'une fidélité aux **règles** (structure du calcul), pas aux **valeurs**.

## 5. Choix à faire : reproduire la référence ou s'en écarter

Le choix revient au propriétaire. Pour proposer un périmètre minimal, le §4 retient **à titre de projet** une option pour P1, P4, P5, P6, P8 et P12 ; le propriétaire peut en retenir d'autres. Ailleurs, le rapport ne recommande aucune option.

| # | Sujet | Référence OXCE | Options |
|---|---|---|---|
| P1 | Niveaux | Grille en 3 dimensions, avec escaliers et chutes. | Un seul niveau dans `MEC-0001`, `z` plus tard ; ou `z` dès le départ. |
| P2 | Convention des directions | 0 = nord (`y` − 1), sens horaire. | La reproduire ; ou une autre convention interne, sans effet visible en jeu. |
| P3 | Coût de la diagonale | × 1,5, tronqué. | Le reproduire ; ou une autre règle (même coût que l'orthogonal, autre arrondi…). |
| P4 | Modèle de coût | Sol + objet de la case d'arrivée, murs franchis (moyenne), + 1 en montée, plafond 100. | Un coût unique par case ; ou le modèle d'OXCE complet. |
| P5 | Valeurs de coût | Données des fichiers de terrain, corrigées par `mcdPatches.rul` ; non relevées. | Valeurs propres à Bastion, sans revendication de fidélité. Un relevé des valeurs d'origine est **incompatible avec D4 en l'état** : il supposerait un réexamen préalable de D4 par le propriétaire, avec examen des licences (`CLAUDE.md` §4). |
| P6 | Obstacles | Murs minces entre les cases et objets dans les cases. | Cases bloquantes seulement ; ou murs minces aussi. |
| P7 | Diagonale le long d'un obstacle | Refusée par certains murs et par les objets « grand mur », pas par un objet ordinaire ni par une unité. | La reproduire ; l'interdire dès qu'un obstacle borde la diagonale ; ou toujours l'autoriser. |
| P8 | Calcul du chemin | Ligne droite retenue dès que ses pas ont un coût homogène, puis A* ; coût minimal non garanti ; départage non étudié. | Garantir le coût minimal et un départage déterministe documenté ; ou reproduire l'algorithme d'OXCE (étude plus fine nécessaire). |
| P9 | TU insuffisantes | Déplacement partiel jusqu'au dernier pas payable, puis message. | Le reproduire ; refuser l'ordre entier ; ou limiter le choix aux cases atteignables. |
| P10 | Orientation et rotation | Rotation gratuite pendant la marche et, par défaut, avant le premier pas. | Ignorer l'orientation dans `MEC-0001` ; la gérer sans coût ; ou avec un coût. |
| P11 | Énergie | La marche coûte la moitié du coût en TU (tronquée) ; arrêt si l'énergie manque. | L'exclure de `MEC-0001` ; ou l'inclure. |
| P12 | Unités non vues | Les unités connues bloquent ; les autres sont découvertes en marchant. | `MEC-0001` avec toutes les unités connues, règle des unités cachées traitée avec la visibilité ; ou découverte des unités cachées dès `MEC-0001`, ce qui suppose d'y inclure la visibilité. |
| P13 | Interruptions | Repérage d'un ennemi, tir de réaction, annulation. | Toutes hors `MEC-0001` ; ou annulation seule. |
| P14 | Ordre impossible | Aucun message trouvé. Clic sur une autre unité du joueur : changement de sélection. | Message explicite ; ou comportement silencieux. Rôle du clic sur une unité : à fixer avec l'interface. |

## 6. Sujets connexes à reporter

Ils sont signalés, sans être spécifiés dans ce lot :

- **Niveaux, escaliers, chute, dénivelés** : `Pathfinding.cpp:109-136`, `:1023-1121`.
- **Vol, ascenseurs gravitationnels, échelles** : `Pathfinding.cpp:442-478`, `:1130-1173`. **Sauts** : aucun mécanisme de saut identifié ; seul un « saut » depuis une échelle est mentionné en commentaire (`UnitWalkBState.cpp:165`). NV.
- **Grandes unités** (2 × 2) : `Pathfinding.cpp:400-409`, `:629-647`.
- **Portes** et portes d'OVNI : `UnitWalkBState.cpp:337-354` ; `Battlescape/TileEngine.cpp:4056-4068`.
- **Course, pas de côté, marche furtive**, désactivés par défaut : ligne 7 du §2.
- **Réserve de TU** pour un tir ou l'agenouillement : `BattlescapeGame.cpp:1382-1470`. Aucune réserve par défaut : `Savegame/SavedBattleGame.cpp:73`.
- **Agenouillement** : se relever avant de marcher, `UnitWalkBState.cpp:101-117`.
- **Récupération à chaque tour** :
  - TU, avec encombrement et blessures aux jambes : `BattleUnit.cpp:2705-2725` ;
  - énergie : `BattleUnit.cpp:2729-2742`.
- **Feu et fumée** : pénalité de chemin pour les unités non joueuses, `Pathfinding.cpp:411-423` ; surcoût sous l'eau, propre à TFTD, `:581-585`.
- **Visibilité, repérage, tir de réaction, grenades de proximité** : `UnitWalkBState.cpp:221-245`.
- **IA** : marche furtive `sneakyAI`, désactivée par défaut (`Engine/Options.cpp:256`).
- **Animation, sons, caméra** : 8 phases par pas, 16 en diagonale, `BattleUnit.cpp:1198-1240`.
- **Interface** : aperçu du chemin, couleurs, confirmation, `Pathfinding.cpp:1180-1311`.

## 7. Harmonisations documentaires (mandat, §4)

1. **`docs/references/OXCE-BASELINE.md`, règle de référence.** L'ancienne règle exigeait une décision « au statut « Validée » ». Elle exige désormais une fiche `MEC` portant une décision du propriétaire « acceptée », explicite et datée. Elle précise que `MODIFICATION-VALIDEE` est une **classe** de fiche, distincte de ce statut de décision.
2. **`docs/references/OXCE-BASELINE.md` et `CLAUDE.md` §4, propriété intellectuelle.** La formulation « sans audit de licence et décision enregistrée » laissait une copie possible. Elle est remplacée par l'interdiction de D4 : aucune reprise de code, de données ni d'assets d'OXCE ou des jeux X-COM. L'examen des licences n'est maintenu que si la politique devait être réexaminée.

Aucune autre règle n'est modifiée. Dans `CLAUDE.md` §4, la puce « Aucun asset X-COM original. » est conservée telle quelle.

**Formulation non modifiée.** La ligne « Licence » du tableau d'`OXCE-BASELINE.md` indique « À auditer avant toute réutilisation (reprise exclue par D4) ». Elle n'est pas la règle visée par le mandat et rappelle déjà D4 : elle est laissée telle quelle et signalée au §11.

## 8. Fichiers et vérifications

**Fichiers modifiés (3, ceux qu'autorise le mandat) :**
- `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md` : nouveau, ce rapport ;
- `docs/references/OXCE-BASELINE.md` : deux règles harmonisées (§7) ;
- `CLAUDE.md` : une puce du §4 harmonisée (§7).

Aucun autre fichier : ni `docs/gameplay/GAMEPLAY-DECISIONS.md`, ni code C#, ni CI, ni harnais.

| Vérification | Résultat | Code de sortie |
|---|---|---|
| `git fetch origin main` au démarrage | `origin/main` = `8b1bc3f09b8d1e2b3d15df0ad3ebb6fecc0798bd`, base attendue par le mandat | 0 |
| `git rev-parse HEAD` dans le clone OXCE | `441cae1b071d249d40a223858cb6bd07fd5d791b` | 0 |
| `git diff --name-only` et `git ls-files --others --exclude-standard` | Les 3 fichiers ci-dessus, et eux seuls | 0 |
| `git diff --check` (fichiers suivis) | Aucune sortie | 0 |
| Recherche d'espaces en fin de ligne dans le nouveau rapport (`grep -nP "[ \t]+$"`) | Aucune ligne | 1 (aucune correspondance) |
| `dotnet build` (SDK local 10.0.114) | 0 avertissement, 0 erreur | 0 |
| `dotnet test` | 2 réussis, 0 échec | 0 |
| `dotnet format --verify-no-changes` | Aucune modification requise | 0 |
| `bash scripts/harness/test-hooks.sh` | 75 tests, 0 échec | 0 |
| Recherches dans les règles `xcom1` (§1) | Armures : aucun résultat. Terrain : `mcdPatches.rul` | 1 et 0 |

Les commandes `dotnet` et les tests des hooks ont été lancés avant les corrections issues de la revue ; celles-ci ne touchent que ce rapport. L'état de la CI GitHub est relevé après publication et communiqué au propriétaire.

## 9. Revue indépendante

- **Relecteur** : agent distinct du développeur, en lecture seule (aucune écriture, aucun commit). Il a relu le diff non commité, le mandat, les registres et le code OXCE au commit figé.
- **Résultat** : 17 constats, dont 0 bloquant, 5 importants et 12 mineurs. Le relecteur a contrôlé dans le code les 16 lignes du tableau du §2 et les scénarios.
- **Intégrés**, après vérification dans le code par le développeur :
  - constat 1 : origine des coûts de terrain, avec les fichiers `.MCD` livrés par OXCE et `mcdPatches.rul` (§0, §1, ligne 3, P5) ;
  - constat 2 : priorité de l'A* et vraie raison pour laquelle le coût minimal n'est pas garanti (lignes 9 et 14, P8) ;
  - constat 3 : clic sur une case portant une unité visible (ligne 13, S3 bis, P14) ;
  - constat 4 : options retenues à titre de projet, désormais signalées (§4, §5) ;
  - constat 5 : relevé des valeurs d'origine déclaré incompatible avec D4 en l'état (P5) ;
  - constats mineurs 6 à 13 et 15 à 17 (grands murs, dénivelé, case sans sol, annulation, commentaire d'option contradictoire, références de récupération, formulations de décision, classe, origine de la lecture du mandat, énergie dans les scénarios, sections à compléter).
- **Non intégré** : constat 14, ajouter « prouvée » à la nouvelle règle d'`OXCE-BASELINE.md`. La règle reprend la formulation du mandat et de `CLAUDE.md` §3 ; cet alignement facultatif est laissé au propriétaire (§11).
- **Limites de la revue** : rien n'a été exécuté ; les fichiers de terrain n'ont pas été lus ; les conséquences tirées du code restent des inférences. Le relecteur est un agent du même type que le développeur, mandaté séparément.

## 10. Limites

- **Aucune exécution d'OXCE** (§1) : chaque comportement est au mieux « vérifié dans le code ».
- **Coûts de terrain `xcom1` non relevés** : fichiers non lus, aucune valeur réelle avancée.
- **Lecture ciblée** : seul le déplacement à pied du joueur a été suivi. Les autres appels du calcul de chemin (IA, missiles guidés) n'ont pas été étudiés.
- **Numéros de ligne** valables au seul commit `441cae1`.
- **Pages web GitHub d'OXCE** non consultées depuis l'environnement d'étude ; le code a été lu dans un clone Git du commit figé.

## 11. Points à décider par le propriétaire

1. Le périmètre de `MEC-0001` (§4) et les choix P1 à P14 (§5). Aucune fiche ne sera créée sans décision « acceptée », explicite et datée.
2. La ligne « Licence » d'`OXCE-BASELINE.md` (§7) : la laisser telle quelle ou l'harmoniser aussi.
3. L'ajout de « prouvée » à la règle d'`OXCE-BASELINE.md`, comme dans `GAMEPLAY-DECISIONS.md` (§9).
