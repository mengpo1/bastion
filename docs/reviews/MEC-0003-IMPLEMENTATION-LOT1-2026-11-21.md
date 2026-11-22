# Bastion — MEC-0003, lot 1 : implémentation et tests de la marche sur terrain plat

**Dates :** 21 et 22 novembre 2026
**Mandat :** « BASTION — Mandat d'implémentation MEC-0003 v1.0 », reçu le 2026-11-21T21:06:41.831Z (horodatage du journal de session).

**Autorisations du propriétaire** (pièces du lot au §10 ; texte exact des messages de la conversation en annexe B) :
- 2026-11-21T21:09:26.953Z : exécution du mandat, avec installation de .NET dans le conteneur ; publication autorisée « après contrôles » ;
- 2026-11-21T21:41:14.860Z : consignes sur l'écart de T13. Elles demandent notamment de ne pas publier sans autorisation distincte ;
- 2026-11-21T22:18:31.802Z : **avenant n° 1**, limité à la dernière phrase de T13 et à l'assertion C# correspondante ;
- 2026-11-22T04:51:30.049Z : **avenant n° 2**, limité aux tests de RL-01, RL-02 et RL-03, au complément de T13 et à l'archivage. Il interdit toute modification du moteur, des règles et des autres tests, ainsi que toute publication ;
- 2026-11-22T09:43:00.852Z : **autorisation de publication**. Elle porte sur l'indexation de l'avenant n° 2, un commit unique, le push de la seule branche du lot et une PR en brouillon vers `main`. Toute fusion exige votre accord explicite.

**Base :** `main` au commit `25e7a28d18d29fea3753f3313a10f27126c3f274`, contrôlée par `git fetch origin main` le 21 puis le 22 novembre (inchangée).
**Branche :** `claude/implementation-mec-0003-lot1`, créée à partir de `origin/main`.
**État :** lot vérifié, puis publié sur autorisation du 2026-11-22T09:43:00.852Z : commit unique sur la branche ci-dessous et PR en brouillon vers `main`. **Aucune fusion** : elle exige votre accord explicite.
**MEC-0001 et MEC-0002 restent reportées.** Seul le périmètre de MEC-0003 est implémenté.

## 1. Résumé

La marche de MEC-0003 est implémentée dans `src/Bastion.Simulation/Movement/`, en C# et sans dépendance à Godot :
- carte, terrains, murs, cases infranchissables et bords ;
- coûts en TU et en énergie, avec leurs arrondis ;
- géométrie exacte du volume rectangulaire réel : rotations, translations, diagonales en L, passages, contact et chevauchement ;
- zone atteignable et choix du chemin ;
- exécution pas à pas, selon A9.

Les 30 scénarios du registre (T01 à T29 et T03b) sont testés dans `tests/Bastion.Simulation.Tests/Movement/`. S'y ajoutent deux tests complémentaires du mandat initial et quatre cas de l'avenant n° 2. Résultat : **46 tests, 46 réussis**, dont les 2 tests fumée existants.

**Avenant n° 1.** Un écart du registre a été constaté dans T13 : la zone atteignable y était mal décrite. Il a été corrigé après votre autorisation (§6).

**Relecture indépendante :** verdict « conforme sous réserves », sans constat bloquant (§7.1). Le moteur concorde avec un modèle indépendant sur 280 cartes aléatoires, sans aucun désaccord. Trois exigences du mandat n'étaient démontrées par aucun test, bien que le code les respecte (RL-01 à RL-03).

**Avenant n° 2.**
- **Trois tests ajoutés :** chacun échoue sur le défaut qu'il vise, introduit dans une copie jetable, et réussit sur le moteur réel (§5.2).
- **T13 complété :** passages, arrivée, solde des ressources, état de référence de la zone ; méthode renommée.
- **Archivage :** les deux avenants sont archivés dans `docs/mandates/`.
- **Relecture ciblée** de ces changements : « conforme sous réserves ». Le relecteur juge levées les réserves RL-01, RL-02, RL-03, RL-08 et RL-09, ainsi que RL-15 pour l'avenant n° 1, preuves de mutation à l'appui. Sa seule réserve, RC-08, portait sur le rapport d'exécution, qui n'était pas encore actualisé (§7.2).

**Réserves restantes** (§8, §9) :
- **RL-11 :** l'invariant de `UnitState` est contournable ; le moteur n'est pas modifié dans ce lot ;
- **RL-13 :** le passage d'un pas diagonal est recalculé à l'exécution, comportement observé, non validé comme règle ;
- les observations RL-04 à RL-07, RL-10, RL-12, RL-14 et RL-16 à RL-19.

## 2. Fichiers

| Fichier | Rôle |
|---|---|
| `src/Bastion.Simulation/Movement/Direction.cs` | huit directions, dans l'ordre de Q4.16 ; décalages ; passages d'une diagonale, dans l'ordre de priorité de A3 |
| `src/Bastion.Simulation/Movement/GridPosition.cs` | case (colonne, ligne) |
| `src/Bastion.Simulation/Movement/Millimetres.cs` | validation des dimensions configurées : millimètres entiers et strictement positifs (R-5) |
| `src/Bastion.Simulation/Movement/TerrainType.cs` | facteur de terrain unique, commun aux TU et à l'énergie (A6) ; catégories initiales (Q3.8) |
| `src/Bastion.Simulation/Movement/WallType.cs` | épaisseur des murs, configurable et non nulle (Q1.3, Q1.7) |
| `src/Bastion.Simulation/Movement/MovementRules.cs` | barème (Q3.7, Q3.2) et coût d'un pas (S2, Q3.13) |
| `src/Bastion.Simulation/Movement/UnitBody.cs` | emprise largeur × profondeur × hauteur (Q1.2, Q1.6, A8) |
| `src/Bastion.Simulation/Movement/UnitState.cs` | état immuable : position, orientation, TU, énergie |
| `src/Bastion.Simulation/Movement/TacticalMap.cs` | carte immuable et constructeur validant (Q1.1) |
| `src/Bastion.Simulation/Movement/StepResults.cs` | motifs de refus, sens de rotation, choix du demi-tour (A7), résultats d'un pas, d'un chemin et d'un ordre |
| `src/Bastion.Simulation/Movement/MovementModel.cs` | contrôles d'un pas, exécution d'un chemin et d'un ordre (A9) |
| `src/Bastion.Simulation/Movement/PathSearch.cs` | zone atteignable et meilleur chemin (Z1, G3, G4, Q4.16) |
| `src/Bastion.Simulation/Movement/Geometry/Rational.cs`, `Surd.cs`, `Vec.cs`, `Box.cs` | arithmétique exacte en a + b√2 et pavés d'obstacle |
| `src/Bastion.Simulation/Movement/Geometry/Collision.cs` | chevauchement exact polygone–pavé (axes séparateurs) et secteur–pavé |
| `src/Bastion.Simulation/Movement/Geometry/StepGeometry.cs` | emprise orientée, rotations, translations ; obstacles de la carte |
| `tests/Bastion.Simulation.Tests/Movement/*.cs` | 5 fichiers de tests (§4) ; `GeometryTests.cs` et `SearchAndExecutionTests.cs` complétés par l'avenant n° 2 |
| `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-transcription.md` | mandat initial, transcrit du journal de session |
| `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-1-transcription.md` | avenant n° 1, transcrit du journal de session ; archivé au titre de l'avenant n° 2 |
| `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-2-transcription.md` | avenant n° 2, transcrit du journal de session ; archivé au titre de l'avenant n° 2 |
| `docs/mandates/README.md` | trois lignes ajoutées : le mandat initial et l'avenant n° 1, au titre de l'avenant n° 2 ; l'avenant n° 2, au titre de l'autorisation de publication |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | avenant n° 1 : une seule phrase de T13 remplacée (§6) |
| `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md` | ce rapport |
| `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-2026-11-21.md` | rapport du relecteur indépendant, copié sans modification |
| `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-CIBLEE-AVENANT-2-2026-11-22.md` | rapport de relecture ciblée de l'avenant n° 2, copié sans modification |

Les empreintes SHA-256 figurent en annexe A.

Aucun autre fichier n'est modifié : ni le moteur depuis l'avenant n° 1, ni les autres règles ou registres, ni le harnais, ni `CLAUDE.md`, ni les autres mandats.

## 3. Conception

**Modèle.** `MovementModel` réunit une carte, un barème et une emprise :
- `CreateState` crée un état valide ;
- `EvaluateStep` évalue un pas ;
- `ComputeReachability` calcule la zone et les chemins ;
- `ExecutePath` et `ExecuteOrder` exécutent un chemin ou un ordre.

Les états et la carte sont immuables. Un pas ne produit un nouvel état que si tous ses contrôles réussissent : rotation, passage, coût réel et ressources. Sinon, l'état rendu est l'état de départ, le même objet (A9). Les calculs de zone et de chemin ne modifient rien.

**Coûts** (`MovementRules.CostOf`) :
- la base de chaque ressource est multipliée par le facteur du terrain d'arrivée, puis arrondie à l'entier supérieur (Q3.13, A6) ;
- pour une diagonale : TU × 1,5, arrondi inférieur (S2) ; énergie × multiplicateur propre, arrondi supérieur (Q3.2, Q3.9) ;
- les facteurs sont des `decimal`, sans arrondi intermédiaire.

**Géométrie.** Elle se calcule en plan (A2), dans un repère où x va vers l'est et y vers le sud. Le centre de la case (c, l) est en (c × L, l × L), L étant la largeur de case.
- **Calcul exact.** Les coordonnées sont des nombres a + b√2, à coefficients rationnels (`BigInteger`). Ils suffisent pour les huit orientations, et leur signe se calcule exactement. Le contact se distingue ainsi du chevauchement sans tolérance numérique. Le registre laisse ouvertes la méthode et la précision (R-5), ainsi que la tolérance des contacts (GE-05) : aucune tolérance n'est introduite (§8).
- **Emprise (A1, A8).** C'est un rectangle centré sur la case : largeur selon le vecteur latéral, profondeur selon le vecteur de face. Pour un cap θ (N = 0°, sens horaire) : face = (sin θ, −cos θ), droite = (cos θ, sin θ).
- **Translation (A2).** Le volume balayé est l'enveloppe convexe des deux emprises extrêmes. Le test des axes séparateurs porte sur les axes de l'emprise et sur ceux du pavé. La translation étant parallèle à un axe, ces axes comprennent toutes les normales de l'enveloppe.
- **Pas diagonal (A2, A3).** Le trajet suit un L par le centre de la case intermédiaire, l'unité restant orientée vers le pas. Les passages sont essayés dans l'ordre N, E, S, W. Un passage est d'abord contrôlé au sens de S3 et de N2 : case intermédiaire franchissable, aucun mur sur les deux arêtes traversées. Il est ensuite contrôlé au sens physique, sur chacun des deux segments.
- **Rotation (A5, A7).** Elle a lieu au centre de la case de départ et se décompose en huitièmes de tour. La surface balayée par un huitième de tour est l'union exacte des deux emprises extrêmes et des quatre secteurs circulaires parcourus par les coins (rayon : la demi-diagonale ; angle : 45°).
  - Le test secteur–pavé découpe le pavé par le coin angulaire du secteur. Il y a chevauchement si le polygone obtenu a une aire non nulle et s'approche du sommet à moins d'un rayon.
  - Sens de rotation : le côté le plus court pour 45°, 90° et 135°. Pour un demi-tour : le sens horaire, puis le sens antihoraire, avec un refus seulement si les deux sont bloqués (`RotationRules.ChooseHalfTurn`).
- **Obstacles.**
  - Les murs sont des pavés de leur épaisseur, centrés sur l'arête, d'un coin à l'autre.
  - Les cases infranchissables sont des pavés de la case entière.
  - Les bords de la carte sont quatre pavés extérieurs.
  - Un préfiltre écarte les obstacles plus éloignés du trajet du centre que la demi-diagonale de l'emprise, par une comparaison exacte.

**Recherche** (`PathSearch`). Elle explore des états (case, orientation), car l'orientation conditionne les rotations.
- Les étiquettes sont traitées dans l'ordre (TU, énergie, suite de directions comparée lexicographiquement) (G4, Q4.16).
- Une étiquette dominée en TU et en énergie dans le même état est écartée.
- La première étiquette traitée pour une case donne son meilleur chemin.
- La recherche termine, car chaque pas coûte au moins 1 TU (A4 d).
- La case de départ n'appartient pas à la zone.

**Exécution.** Pour chaque pas, le coût réel est recalculé sur la carte d'exécution (M-05). Le premier refus arrête l'ordre, sans nouveau calcul (Q3.4, Q4.21).

**Choix d'implémentation qui ne sont pas des règles :**
- **Ordre de signalement des refus** : case hors carte ou infranchissable, puis rotation, puis passage, puis TU et énergie. A9 impose seulement que tous les contrôles précèdent toute modification.
- **Dimensions en `decimal`** : les dimensions configurées sont reçues en `decimal`, pour pouvoir refuser une valeur non entière (T19).
- **Cache** des contrôles d'un pas, par carte.
- **Convention interne des coordonnées**, sans effet observable.

**Comportement observé, non validé comme règle : recalcul du passage diagonal à l'exécution (RL-13).**
- **Constat.** Un chemin calculé ne mémorise que ses directions. À l'exécution, chaque pas est réévalué sur la carte d'exécution, et le passage d'un pas diagonal est donc choisi de nouveau selon A3.
- **Effet.** Si la carte change entre le calcul et l'exécution, un pas diagonal dont le passage prévu est devenu impraticable peut emprunter l'autre passage, au lieu d'être refusé.
- **Portée.** Ce cas n'existe que dans le contexte des tests : A4 (g) n'admet une modification de carte entre le calcul et l'exécution que dans les tests, pour vérifier Q3.4, M-05 et Q4.21. Aucun test ne le couvre.
- **Statut.** Ce comportement découle de la structure du code. **Ce n'est pas une règle de gameplay validée** : MEC-0001 laisse ouvert le « repli d'un pas diagonal sur l'autre passage orthogonal » (registre, l. 232 et 258), et aucun arbitrage n'est fait dans ce lot. Il est conservé tel quel, conformément à l'avenant n° 2.

## 4. Correspondance des tests

| Scénario | Méthode |
|---|---|
| T01 à T04, T03b | `CostTests.T01_…`, `T02_…`, `T03_…`, `T03b_…`, `T04_…` |
| T05 à T09 | `SearchAndExecutionTests.T05_…` à `T09_…` |
| T10, T11 | `GeometryTests.T10_…`, `T11_…` |
| T12 | `GeometryTests.T12_ContactWithBothCorridorWallsIsAllowed` ; contre-épreuve : `T12_CounterCheck_TwoMoreMillimetresIsAnOverlap` (une largeur de 1 402 mm chevauche) |
| T13 | `GeometryTests.T13_VolumeMayExceedItsCellButMayNotOverlapAnImpassableCell` : 2e pas N refusé, état conservé, seul le 1er pas débité ; inchangé. `GeometryTests.T13_TargetCellRemainsInTheReachableZoneAndIsReachedFacingNorthWest` : zone, chemin, passages, arrivée et solde (avenants n° 1 et n° 2, §6) |
| T14 | `GeometryTests.T14_…` (pas N admis ; NE et S refusés pour rotation) |
| T15 à T18 | `SearchAndExecutionTests.T15_…` à `T18_…` |
| T19 | `ConfigurationTests.T19_…` : 4 tests (case impaire, dimension non entière, pas à 0 TU, position initiale en chevauchement) |
| T20 à T22 | `GeometryTests.T20_T21_T22_PassagePriorityNorthEastSouthWest` : 4 cas (NE, SE, SW, NW) |
| T23 à T28 | `GeometryTests.T23_…` à `T28_…` |
| T29 | `GeometryTests.T29_HalfTurnSenseChoice` : 4 combinaisons |
| Mandat, §4 | `SearchAndExecutionTests.ZoneAndPathComputationsDoNotModifyTheUnitStateOrTheMap` |
| RL-01 (avenant n° 2, hors registre) | `GeometryTests.RL01_VolumeIsCheckedDuringTheWholeTranslation` |
| RL-02 (avenant n° 2, hors registre) | `GeometryTests.RL02_VolumeIsCheckedOnBothLegsOfTheDiagonalPath` : 2 cas, un par segment du L |
| RL-03 (avenant n° 2, hors registre) | `SearchAndExecutionTests.RL03_OrderStopsAtTheFirstRefusedStep` |

Les résultats attendus sont ceux du registre, sauf la phrase de T13 corrigée par l'avenant n° 1. Le relecteur a confronté chaque test du registre à son scénario et les juge tous fidèles (rapport de relecture, §5.1).

**Scénarios de l'avenant n° 2.** Les valeurs sont détaillées dans les commentaires des tests.
- **RL-01.**
  - Situation : unité de 1 700 × 600 mm orientée E en (1,1) ; mur sur l'arête est de (1,0) ; pas E.
  - Ni le départ ni l'arrivée ne touchent le mur : chacune de ces deux positions s'arrête à 400 mm d'une de ses faces. L'arrivée est d'ailleurs créée sans erreur dans le test.
  - Seul le volume balayé chevauche le mur, de 100 mm.
  - Attendu : refus `VolumeCollision`, état inchangé (le même objet).
- **RL-02.**
  - Situation : carte de 4 × 4 ; unité de 1 200 × 1 200 mm orientée N en (1,2) ; pas NE. Sans mur, le pas emprunte le passage N, prioritaire.
  - Un mur est placé, selon le cas, au bord du 1er ou du 2e segment du passage N. Aucun des deux murs n'est sur une arête traversée.
  - Orientée NE, l'unité ne touche le mur ni au départ, ni dans la case intermédiaire, ni à l'arrivée : ces trois positions sont créées sans erreur dans le test.
  - Le volume balayé par le segment, lui, chevauche le mur de 98,53 mm.
  - Attendu : pas admis par le passage E.
- **RL-03.**
  - Situation : chemin [N, N, NE] calculé de (0,3) vers (1,0) sur une carte de 3 × 4 ; puis la case (0,1) devient infranchissable (A4 g).
  - Attendu :
    - deux résultats de pas seulement ;
    - le 2e pas refusé (`ArrivalBlocked`) ;
    - l'unité en (0,2), orientée N, avec 56 TU et 98 d'énergie ; l'état final est celui du 1er pas.
  - Le test montre aussi que le 3e pas resterait exécutable et que (1,0) resterait atteignable : l'unité ne fait pourtant ni l'un ni l'autre.

## 5. Vérifications exécutées

**Environnement.** Le SDK .NET 10.0.115 a été installé par `apt` dans le conteneur, qui n'en avait pas. C'est la version que proposait le dépôt `apt` ; la question d'autorisation mentionnait la 10.0.114. Toutes les commandes ont été exécutées dans `/home/user/bastion`, sauf mention contraire.

### 5.1 Mandat initial et avenant n° 1

| Étape | Commande | Résultat |
|---|---|---|
| Base | `git fetch origin main` ; `git rev-parse origin/main` | code 0 ; `25e7a28d…` |
| Base, avant toute modification (21:10 UTC) | `dotnet restore`, `build`, `test`, `format --verify-no-changes` | codes 0 ; 2 tests, 2 réussis |
| Avant l'avenant n° 1 | `dotnet test --configuration Release` | code 1 ; 42 tests, 41 réussis. Seul échec : l'assertion de T13 sur la zone (§6) |
| Après l'avenant n° 1 | `dotnet restore`, `build`, `test`, `format --verify-no-changes`, `test-hooks.sh` | codes 0 ; 0 avertissement ; 42 tests, 42 réussis ; « 75 tests, 0 échec(s) » |
| Avenant n° 1 | comparaison automatique du registre avant et après | registre identique à celui d'avant, à la seule phrase de T13 près |
| Contre-vérification de la relecture (dans la copie du relecteur) | `dotnet test --configuration Release --filter FullyQualifiedName~RevueTests` | code 0 ; les 22 tests proposés par le relecteur réussissent sur le moteur non modifié |
| | idem, sortie détaillée de `Rv07` | passages du chemin de T13 : « NE Clockwise N ; NW CounterClockwise W » ; « Depuis (2,3) : E,NW 10/5 » |
| Contre-vérification de la relecture (dans ma propre copie, sans les tests du relecteur) | mutants M1, M6 et M22 du relecteur, un à un, puis `dotnet test --configuration Release` | code 0 pour chacun : 42 tests, 42 réussis. Les trois défauts passaient inaperçus |

### 5.2 Avenant n° 2

| Étape | Commande | Résultat |
|---|---|---|
| Base | `git fetch origin main` ; `git rev-parse origin/main HEAD` | code 0 ; `25e7a28d…` pour les deux : base inchangée |
| Moteur inchangé | `sha256sum -c` sur les 18 sources, avec les empreintes relevées avant l'avenant n° 2 | 18 × OK, au début et à la fin |
| Registre inchangé depuis l'avenant n° 1 | `sha256sum docs/gameplay/GAMEPLAY-DECISIONS.md` | `7b4931f3…`, l'empreinte d'après l'avenant n° 1 |
| Autres tests inchangés | `sha256sum` de `CostTests.cs`, `ConfigurationTests.cs`, `TestWorld.cs` | empreintes identiques à celles d'avant |
| Diff des tests | `diff -u` avec les copies d'avant l'avenant n° 2 | `GeometryTests.cs` : 2 lignes retirées (l'ancien nom de la méthode de T13 ; l'assertion d'orientation, reprise dans la nouvelle forme), 67 ajoutées, dont 59 non vides. `SearchAndExecutionTests.cs` : 0 retirée, 32 ajoutées, dont 28 non vides |
| Archives | comparaison octet pour octet avec les messages extraits du journal de session, suivis d'un saut de ligne final comme la transcription du mandat initial | identiques pour les deux avenants |
| Restauration | `dotnet restore` | code 0 |
| Compilation | `dotnet build --configuration Release` | code 0 ; 0 avertissement, 0 erreur |
| Tests | `dotnet test --configuration Release` | code 0 ; **46 tests, 46 réussis** |
| Format | `dotnet format --verify-no-changes` | code 0 ; aucune sortie |
| Harnais | `bash scripts/harness/test-hooks.sh` | code 0 ; « 75 tests, 0 échec(s) » |
| Mutants | `python3 -I mutants.py <dépôt> <dossier>` (script hors dépôt) : chaque mutant est appliqué dans une copie jetable, puis `dotnet test --configuration Release` | voir le tableau suivant |
| Clôture de la relecture ciblée (RC-17) | `diff` du rapport depuis la version contrôlée par le relecteur (`44da10db…`) ; `cmp` de la copie de relecture ciblée avec le rapport définitif du relecteur ; `sha256sum -c` des empreintes de l'annexe A | diff limité aux deux marqueurs remplis, aux corrections de RC-14 à RC-16 et à cette ligne ; copie identique (`2737a3b0…`) ; 30 × OK |

**Mutants.** Chaque mutant modifie un seul passage du moteur, dans une copie jetable supprimée après usage. Le dépôt n'en a jamais contenu : les 18 sources du moteur gardent leurs empreintes.

| Mutant | Défaut introduit | Code | Tests (sur 46) | Tests en échec |
|---|---|---|---|---|
| témoin | aucun | 0 | 46 réussis | — |
| M1 | translation contrôlée aux deux extrémités seulement | 1 | 43 réussis, 3 en échec | `RL01_…` ; `RL02_…` (2 cas) |
| ML | trajet en L : seuls le point intermédiaire et la destination sont contrôlés | 1 | 44 réussis, 2 en échec | `RL02_…` (2 cas) |
| M6 | trajet en L : aucun contrôle physique | 1 | 43 réussis, 3 en échec | `RL02_…` (2 cas) ; `T13_TargetCellRemains…` |
| M7 | trajet en L : 1er segment seulement | 1 | 45 réussis, 1 en échec | `RL02_…`, cas du mur sur l'arête est de (1,0) |
| M7b | trajet en L : 2e segment seulement | 1 | 45 réussis, 1 en échec | `RL02_…`, cas du mur sur l'arête nord de (0,2) |
| M8 | trajet en L : orientation de départ conservée, au lieu de celle du pas (A2) | 1 | 44 réussis, 2 en échec | `RL02_…` (2 cas) |
| M22 | exécution poursuivie après un refus | 1 | 45 réussis, 1 en échec | `RL03_…` |

**Ce que montrent les mutants :**
- **RL-01** est détecté par `RL01_…`.
- **RL-02** : `RL02_…` détecte le défaut décrit par l'avenant, ML. Chacun de ses deux cas détecte l'oubli d'un segment, M7 ou M7b. Le test détecte aussi M6 et M8.
- **RL-03** est détecté par `RL03_…`.
- **T13 complété** détecte M6 : sans contrôle physique, le 2e pas emprunterait le passage N au lieu du passage W.

Les mutants M1, M6, M7, M8 et M22 reprennent ceux du relecteur ; ML et M7b sont nouveaux.

**CI GitHub :** elle n'avait pas tourné à la rédaction de ce rapport. Son état réel est donné avec la PR (§5.3).

### 5.3 Avant publication (22 novembre 2026)

| Étape | Commande | Résultat |
|---|---|---|
| Base | `git fetch origin main` ; `git rev-parse origin/main HEAD` ; `git ls-remote --heads origin claude/implementation-mec-0003-lot1` | code 0 ; `25e7a28d…` pour les deux : base inchangée, aucune intervention sur l'historique ; branche distante absente |
| Index des mandats | `git diff docs/mandates/README.md` | 3 lignes ajoutées, aucune retirée ; la troisième, sur l'avenant n° 2, suit le modèle des deux autres |
| Conformité | `sha256sum -c` sur les 18 sources du moteur ; `sha256sum` du registre et des 5 fichiers de tests ; `git diff --quiet HEAD -- .claude scripts .github CLAUDE.md docs/decisions docs/references` | moteur 18 × OK ; registre `7b4931f3…` ; tests aux empreintes de l'annexe A ; harnais, décisions et références inchangés (code 0, aucun fichier non suivi) |
| Restauration | `dotnet restore` | code 0 |
| Compilation | `dotnet build --configuration Release` | code 0 ; 0 avertissement, 0 erreur |
| Tests | `dotnet test --configuration Release` | code 0 ; 46 tests, 46 réussis |
| Format | `dotnet format --verify-no-changes` | code 0 |
| Harnais | `bash scripts/harness/test-hooks.sh` | code 0 ; « 75 tests, 0 échec(s) » |

La CI, le SHA du commit et le lien de la PR ne peuvent figurer dans ce rapport, qui fait partie du commit. Ils sont transmis au propriétaire après la publication.

## 6. Écart de T13 et avenants

**Écart.** La dernière phrase du résultat attendu de T13, « La case (2,2) n'est pas non plus dans la zone atteignable », contredisait les règles de la fiche (A2, Q1.2, G4).
- Situation : carte de 5 × 6 cases, case (3,1) infranchissable, unité de 1 600 × 1 600 mm orientée N en (2,4), avec 60 TU et 100 d'énergie.
- Le moteur trouve (2,2) par [NE, NW], pour 12 TU et 6 d'énergie :
  - 1er pas NE : rotation horaire, passage N ;
  - 2e pas NW : rotation antihoraire, passage W, car par le passage N l'unité chevaucherait la case (3,1).
- L'unité arrive orientée NW. En diagonale, son emprise ne touche pas la case (3,1) ; orientée N, elle la chevaucherait.
- Un calcul indépendant du code C# l'a confirmé, puis le modèle indépendant du relecteur.
- La cause est une erreur de rédaction de ma part dans la fiche v4 : je n'avais considéré que l'arrivée orientée N.

**Traitement**, selon vos consignes :
- le moteur n'a pas été modifié, ni le test supprimé ou neutralisé ;
- le test a échoué tant que l'avenant n'était pas autorisé ;
- l'avenant a été proposé, puis autorisé.

**Avenant n° 1 :**
1. Registre, T13 : la phrase est remplacée par « La case (2,2) reste toutefois dans la zone atteignable : le chemin retenu est [NE, NW], pour 12 TU et 6 d'énergie ; l'unité y arrive orientée NW, et son emprise ne chevauche alors pas la case (3,1). »
2. Test : `Assert.DoesNotContain(At(2, 2), reachability.Zone)` est remplacé par cinq assertions :
   - (2,2) est dans la zone ;
   - un chemin existe ;
   - ce chemin est [NE, NW] ;
   - il coûte 12 TU et 6 d'énergie ;
   - l'orientation finale est NW.

**Avenant n° 2, complément de T13** (test seulement, registre inchangé) :
- la méthode s'appelle désormais `T13_TargetCellRemainsInTheReachableZoneAndIsReachedFacingNorthWest` ;
- un commentaire précise que la zone est calculée depuis l'état initial en (2,4), avec 60 TU et 100 d'énergie, et non depuis (2,3) ;
- l'exécution du chemin est complète ;
- les passages sont N puis W ;
- l'arrivée se fait en (2,2), orientée NW ;
- le solde est de 48 TU et 94 d'énergie.

Les assertions de l'avenant n° 1 sont conservées. La méthode `T13_VolumeMayExceedItsCellButMayNotOverlapAnImpassableCell` est inchangée : refus du 2e pas N, maintien de l'état, débit du seul 1er pas.

**Formulation du registre (RL-18).** La phrase de l'avenant n° 1, que j'ai rédigée, ne précise pas depuis quel état la zone est calculée. Depuis (2,3), après le 1er pas, (2,2) est aussi atteignable, mais par [E, NW], pour 10 TU et 5 d'énergie : sortie de `Rv07`, confirmée par le modèle indépendant. Conformément à l'avenant n° 2, le registre n'est pas modifié : la précision figure dans le test.

## 7. Relecture indépendante

### 7.1 Relecture générale du lot

**Relecteur :** un agent distinct, qui n'a écrit aucune ligne du lot. Il a travaillé sur une copie du dépôt, sans rien écrire dans `/home/user/bastion`.
**Rapport :** `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-2026-11-21.md`, copié sans modification (SHA-256 `3d5941ec36204a59b0e10f3c2f00655faf1a0620e5a68e7d10fdbf6cbedc4252`). Ses scripts, ses journaux et ses tests proposés (`RevueTests.cs`) sont restés hors du dépôt.
**Verdict :** « conforme sous réserves ». Aucun constat bloquant : ni non-conformité aux règles, ni erreur géométrique, ni test infidèle au registre.

**Travail du relecteur :**
- **Commandes du mandat**, relancées dans sa copie : toutes de code 0, 42 tests sur 42.
- **Diff du registre** : limité à la phrase de l'avenant n° 1.
- **Démonstrations géométriques**, établies par lecture et raisonnement, sans exécution qui les prouve :
  - la décomposition de la rotation donne exactement la surface balayée ;
  - les axes séparateurs suffisent ;
  - le préfiltre est conservatif ;
  - les contacts exacts sont admis.
- **Modèle indépendant** : écrit à partir du seul registre, avec des méthodes différentes (flottants, énumération exhaustive des chemins). Comparé au moteur sur 280 cartes aléatoires, soit 61 824 pas, 23 952 états au repos, 86 zones et 437 quasi-contacts, il ne montre aucun désaccord.
- **Mutation** : 23 défauts plausibles introduits un à un dans une copie ; 9 passaient inaperçus des tests du lot.

**Constats et suites.** Les gravités sont celles du relecteur.

| Constat | Gravité | Suite |
|---|---|---|
| RL-01 : collision au milieu d'une translation non démontrée (mandat, §3) | à corriger | test ajouté par l'avenant n° 2 ; mutant M1 détecté (§5.2) |
| RL-02 : contrôle physique du trajet en L non démontré ; passages de T13 non affirmés | à corriger | test ajouté et T13 complété par l'avenant n° 2 ; mutants ML, M6, M7, M7b et M8 détectés (§5.2) |
| RL-03 : arrêt de l'ordre au premier refus non démontré | à corriger | test ajouté par l'avenant n° 2 ; mutant M22 détecté (§5.2) |
| RL-04 à RL-07 : contact pendant une rotation, orientation dans la recherche, arrondi supérieur des TU, état rendu d'un refus faute de TU | observation | non traités : hors de l'avenant n° 2. Les tests `Rv14` à `Rv17` du relecteur réussissent sur le moteur |
| RL-08 : nom du test de zone de T13 contraire à son contenu | à corriger | méthode renommée par l'avenant n° 2 |
| RL-09 : arrivée de T13 seulement implicite | observation | traité par l'avenant n° 2 : achèvement, case (2,2) et solde affirmés |
| RL-10 : assertions partielles dans T10, T14, T15, T24 et T28 | observation | non traité : hors de l'avenant n° 2 |
| RL-11 : les accesseurs `init` publics de `UnitState` permettent, par `with`, un état que `CreateState` aurait refusé | à corriger | **réserve maintenue** : le moteur n'est pas modifié dans ce lot (avenant n° 2). `UnitState.cs`, l. 17-23 ; `Rv04` démontre le contournement |
| RL-12 : `ExecutePath` public permet un déplacement partiel vers une case hors zone | observation, point à décider | non traité |
| RL-13 : passage recalculé à l'exécution, sur un point laissé ouvert par MEC-0001 | observation, point à décider | **réserve maintenue** : comportement conservé et documenté comme observé, non validé (§3) |
| RL-14 : tolérance géométrique nulle | observation, limite à déclarer | déclarée au §8 |
| RL-15 : avenant n° 1 non archivé dans `docs/mandates/` | à corriger (traçabilité) | archivé et indexé par l'avenant n° 2 (§10) |
| RL-16, RL-17 : imprécisions de messages et de validation ; cache non sûr en accès concurrent | observation | non traités : modifications du moteur |
| RL-18 : état de référence de la zone non précisé dans T13 | observation | précisé dans le test ; registre inchangé (§6) |
| RL-19 : branche locale `main` périmée (sans effet) ; « État d'implémentation : non commencé » dans la fiche ; colonne « État » de T13 | observation | non traité : registre inchangé |

### 7.2 Relecture ciblée de l'avenant n° 2

**Relecteur :** le même agent indépendant, qui n'a écrit aucune ligne du lot. La relecture porte sur les seuls changements de l'avenant n° 2. Il a travaillé dans sa propre copie, sans rien écrire dans `/home/user/bastion`.
**Rapport :** `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-CIBLEE-AVENANT-2-2026-11-22.md`, copié sans modification (empreinte en annexe A).
**Verdict :** « conforme sous réserves ». Les changements faits sont conformes et restent dans le périmètre autorisé. Seule réserve : RC-08.

**Travail du relecteur :**
- **Commandes du mandat**, relancées dans sa copie : toutes de code 0, 46 tests sur 46.
- **Ses propres mutants**, sans se fier au script du développeur, qu'il a lu : 10 défauts en plus du témoin, chacun dans une copie jetable. Le tableau des tests en échec est dans son rapport, §2.
- **Recalcul indépendant** des valeurs des trois scénarios, avec le modèle de la revue générale ; celles de T13 l'avaient été lors de la revue générale.
- **Archives** : comparaison octet pour octet avec le journal de session.

**Réserves de la revue générale, selon le relecteur :**

| Réserve | Conclusion du relecteur | Preuve citée |
|---|---|---|
| RL-01 | levée | `RL01_…` échoue quand seules les positions initiale et finale sont contrôlées (A1), et réussit sur le moteur réel ; valeurs recalculées (RC-02) |
| RL-02 | levée | `RL02_…` échoue quand seuls le point intermédiaire et la destination sont contrôlés (A2a). Chaque segment est contrôlé séparément : A2b et A2c ne sont détectés que par leur cas. L'orientation pendant le L (A2e) est contrôlée. T13 affirme les passages N puis W (RC-03, RC-05) |
| RL-03 | levée | `RL03_…` échoue sous A3a (ordre poursuivi), A3b (nouveau calcul de chemin) et A3c (effets du 1er pas perdus) (RC-04) |
| RL-08, RL-09 | levées | nouvelle version de T13 (RC-05) |
| RL-15 | levée pour l'avenant n° 1 | archive exacte et ligne du README (RC-06, RC-07) |
| RL-11, RL-13 | maintenues, sur votre décision | — |
| RL-04 à RL-07, RL-10, RL-12, RL-14, RL-16 à RL-19 | maintenues : non traitées par l'avenant | — |

**Constats :**
- **Sans action, conformes :** RC-01 à RC-07 et RC-09 :
  - diff limité à l'autorisation ;
  - valeurs exactes des scénarios ;
  - T13 conforme ;
  - archives fidèles ;
  - lignes du README exactes.
- **RC-02, limite déclarée :** un moteur qui contrôlerait la translation au départ, au milieu et à l'arrivée ne serait pas détecté par `RL01_…`. L'avenant ne l'exige pas. Sur 450 cartes aléatoires (103 376 pas), un tel moteur donne exactement les résultats du vrai. C'est constaté, sans démonstration (§8).
- **RC-07 :** remarque mineure. La ligne du README sur le mandat initial pourrait préciser que l'autorisation de 21:09:26 UTC est un choix parmi des options proposées. J'ai ajouté cette précision.
- **RC-08 : à corriger.** Le relecteur a lu le rapport d'exécution dans son état d'avant l'avenant n° 2. L'origine et le statut de l'avenant n° 2, la documentation de RL-13, le maintien de RL-11 et l'actualisation du rapport n'étaient donc pas encore vérifiables.
  - Traitement : ces points figurent désormais aux §3, §5.2, §7, §8, §9 et §10 du présent rapport.
  - Contrôle de ces seuls ajouts : contrôlés par le relecteur, section 6 de son rapport (constats RC-10 à RC-17). Verdict actualisé : « conforme sous réserves », **RC-08 levée** ; RL-01, RL-02 et RL-03 restent levées.
  - **RC-14 et RC-15, à corriger :** la liste des réserves restantes au §1 comptait à tort RL-09 et RL-15, et le §5.2 ne comptait que les lignes non vides ajoutées. Les deux points sont corrigés dans la présente version.
  - **RC-16, imprécisions mineures :** elles sont corrigées.
    - Formulation des mutants.
    - Gravités du tableau du §7.1.
    - Tests du relecteur cités au §8.
    - Recalcul de T13 au §7.2.
    - Origine des consignes de T13 au §10.
  - **RC-17, conditions de clôture :** remplissage du présent paragraphe et de l'annexe A, et copie octet pour octet du rapport définitif dans `docs/reviews/`.
  - **Contrôle de ces dernières corrections :** fait par moi, mécaniquement, sur les conditions de clôture fixées par le relecteur (§5.2) ; elles n'ont pas été relues par le relecteur.

## 8. Limites et réserves restantes

- **RL-11.** L'invariant de `UnitState` reste contournable par une expression `with`. Le moteur n'est pas modifié dans ce lot.
- **RL-13.** Le passage d'un pas diagonal est recalculé à l'exécution. C'est un comportement observé dans le seul contexte des tests qui modifient la carte (A4 g), et non une règle de gameplay validée (§3).
- **Tolérance (RL-14).** Les contacts sont tranchés par un calcul exact, donc sans tolérance. Le registre laisse ouverte la tolérance des contacts (GE-05, l. 185). La contre-épreuve de T12 (1 402 mm) suppose qu'un chevauchement de 1 mm de chaque côté est refusé : elle serait à revoir si une tolérance de 1 mm ou plus était décidée un jour.
- **Couverture.** Les observations RL-04 à RL-07 et RL-10 du relecteur restent sans test dédié. Le code concerné est correct selon la relecture. Pour RL-04 à RL-07, les tests correspondants du relecteur réussissent sur le moteur, hors du dépôt ; RL-10 n'a pas de test du relecteur.
- **Tests hors registre.** Les tests de RL-01 à RL-03 vérifient des exigences du mandat (§3 et §4), et non des scénarios du registre.
- **Portée de RL-01 (RC-02).** Le test détecte un contrôle aux seules extrémités de la translation. Il ne détecterait pas un contrôle aux extrémités et au milieu. Selon le relecteur, un tel contrôle donne les mêmes résultats que le vrai sur 450 cartes aléatoires, probablement parce que les obstacles sont alignés sur les arêtes ; ce n'est pas démontré.
- **Index des mandats.** `docs/mandates/README.md` référence le mandat initial et l'avenant n° 1, comme l'autorise l'avenant n° 2. L'avenant n° 2, d'abord non indexé faute d'autorisation, y a été ajouté sur autorisation du 2026-11-22T09:43:00.852Z. Son origine et son statut sont indiqués au §10.
- **Transcriptions.** Le mandat et les deux avenants ont été reçus comme messages de la conversation. Leur identité avec un éventuel fichier d'origine n'est pas vérifiée.
- **SDK.** La version installée est la 10.0.115, et non la 10.0.114 citée par T-101 et par la question d'autorisation ; les deux sont compatibles avec `global.json`.
- **Performance.** Le calcul exact en grands entiers n'est mesuré que sur de petites cartes. La suite s'exécute en moins d'une seconde ; une zone de 20 × 20 cases à 60 TU se calcule en 672 ms, selon la mesure du relecteur, que je n'ai pas refaite.
- **Hauteur.** La hauteur de l'emprise est validée mais n'intervient pas : le contrôle se fait en plan dans ce périmètre (A2).
- **CI.** Elle n'avait pas tourné à la rédaction de ce rapport (§5.3).

## 9. Points à décider par le propriétaire

1. **Fusion** de la PR vers `main` : elle exige votre accord explicite. La publication et l'indexation de l'avenant n° 2 sont faites, sur autorisation du 2026-11-22T09:43:00.852Z.
2. **RL-11** : rendre les accesseurs de `UnitState` `internal init`. C'est une modification du moteur, à autoriser à part, dans un lot ultérieur.
3. **RL-13** : arbitrage de gameplay sur le repli d'un pas diagonal, dans le cadre de MEC-0001.
4. **Registre, plus tard :**
   - l'état d'implémentation de la fiche ;
   - la colonne « État » de T13 ;
   - la précision de l'état de référence de la zone dans T13 (RL-18, RL-19).
5. **Observations restantes**, pour un lot ultérieur : RL-04 à RL-07, RL-10, RL-12, RL-16 et RL-17.

## 10. Pièces documentaires du lot

| Pièce | Origine | Statut |
|---|---|---|
| Mandat initial : `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-transcription.md` | message du propriétaire du 2026-11-21T21:06:41.831Z, extrait mécaniquement du journal de session | autorisé le 2026-11-21 à 21:09:26 UTC ; exécuté ; publié avec le lot ; indexé dans `docs/mandates/README.md` |
| Consignes sur l'écart de T13 | réponse libre du propriétaire, du 2026-11-21T21:41:14.860Z, à une question posée par Claude Code | appliquées ; texte reproduit en annexe B.2 |
| Avenant n° 1 : `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-1-transcription.md` | message du propriétaire du 2026-11-21T22:18:31.802Z, extrait mécaniquement du journal de session | autorisé par le message lui-même ; exécuté ; indexé dans `docs/mandates/README.md` |
| Avenant n° 2 : `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-2-transcription.md` | message du propriétaire du 2026-11-22T04:51:30.049Z, extrait mécaniquement du journal de session | autorisé par le message lui-même ; exécuté ; publié avec le lot ; indexé dans `docs/mandates/README.md` sur autorisation du 2026-11-22T09:43:00.852Z |
| Autorisation de publication | message du propriétaire du 2026-11-22T09:43:00.852Z | appliquée ; texte reproduit en annexe B.5 |
| Relecture générale : `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-2026-11-21.md` | rapport original du relecteur indépendant | copie sans modification |
| Relecture ciblée : `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-CIBLEE-AVENANT-2-2026-11-22.md` | rapport original du relecteur indépendant | copie sans modification |

Les archives de `docs/mandates/` reproduisent le texte des messages octet pour octet, suivi d'un saut de ligne final, selon la convention de la transcription du mandat initial.

## Annexe A — Empreintes SHA-256

```
7b4931f37171ffbd66b825d53547413623303d3884564a6884fe2e75c4b0bbb7  docs/gameplay/GAMEPLAY-DECISIONS.md
c8d9a38f4fb91cac07da621dfad7a21e8324553513d940fb228f98dd9b6d5fd8  docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-transcription.md
6055e752655178b214df8804a1b8e373578388be7827258607272da2d79e74d3  docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-1-transcription.md
6027eb3215eff97212c8fcfef54cfccc95a1357fe9537c40cd209d59a8e8264f  docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-2-transcription.md
ebd4ded515d89fabf875245403c5938a7fbc029fc4a02c97009bc7743d8d52c5  docs/mandates/README.md
3d5941ec36204a59b0e10f3c2f00655faf1a0620e5a68e7d10fdbf6cbedc4252  docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-2026-11-21.md
2737a3b0ef9940bf64d063f5d2da16dcfface518f6114fae971c16e0e752ed86  docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-CIBLEE-AVENANT-2-2026-11-22.md
76bc1c513b03b9768aa03c6a1f54436e29c757144e4deac34b036e6a815a3008  src/Bastion.Simulation/Movement/Direction.cs
a990e2c672adf19797ea7373b4fa7cfd8a513ad9598c5ef7f992c92bd6e9fce8  src/Bastion.Simulation/Movement/Geometry/Box.cs
08d482890ae53e3613000f1a3d376c447c7a41a7ee12108ec6021d155f06c821  src/Bastion.Simulation/Movement/Geometry/Collision.cs
836d2eb639b5dfafaac34ede704a19d793100ddb48b532ace8b795d7c0653aae  src/Bastion.Simulation/Movement/Geometry/Rational.cs
9e8edaec2e044ddef6584332ebae6d37e0da32705efa1f90b381cddaafa1e4ff  src/Bastion.Simulation/Movement/Geometry/StepGeometry.cs
17ae0db1302862b6b113cccea942269bdb495da4c58d6c96ac6d7afc6d81e1cd  src/Bastion.Simulation/Movement/Geometry/Surd.cs
3dee3a4610333affe4d6caaf47cf3ab85ce228c36e88e8bcfe7c999527de78b9  src/Bastion.Simulation/Movement/Geometry/Vec.cs
e8cec362775964547e73ca3f5d5fb9f3380960cc2a2820e7c4933603dbcff8a4  src/Bastion.Simulation/Movement/GridPosition.cs
7b84383f919c5cbf82e336ae614dd8f886b0f7e6af3b5913e28e646606a469c1  src/Bastion.Simulation/Movement/Millimetres.cs
cf7de7c9043587b4831202d7b9fc47c058cf4c6396cfdcfbf17aed4a2ea89e6f  src/Bastion.Simulation/Movement/MovementModel.cs
1ffdabe312071c1eef81e0a5f0e86012d7b99c39820280b6df393b3c35a15cee  src/Bastion.Simulation/Movement/MovementRules.cs
533154c7f723d79edddbd9133b7859f664e56317a4cb3586067e16f3808c88ac  src/Bastion.Simulation/Movement/PathSearch.cs
c7bb8720cef5a65a337669b0e8cd1210e943d229c8d15d15885760e226b99694  src/Bastion.Simulation/Movement/StepResults.cs
9f3c2363215ce664582cd307ea8400887461f1e764b6ec6db37191c368724e9a  src/Bastion.Simulation/Movement/TacticalMap.cs
04470170425349b799ac4914482e6be3993b4c7aaacc19d1b4359bd3021fb7e7  src/Bastion.Simulation/Movement/TerrainType.cs
975eff3ed8ee54b3d10092f90a4a93a15921239b0a5e1eba80178a431ae33c17  src/Bastion.Simulation/Movement/UnitBody.cs
79a8d7861e3476c2ef4ec786da78377541dbfa9b58096e08b1199f2190db0c50  src/Bastion.Simulation/Movement/UnitState.cs
2f4c5f67010b411769e7f81098bf7ddcc2a1f40ff99148b0286b526eb61a5abf  src/Bastion.Simulation/Movement/WallType.cs
acbf96c7c4081e73bf8e2c4877f2f92b1d3c2a4e85e0f410d3c190cfe10ebec1  tests/Bastion.Simulation.Tests/Movement/ConfigurationTests.cs
f5cd488cc78e5e68d0816a0ae2b73905e2844abbecc5b1f043073b74501659db  tests/Bastion.Simulation.Tests/Movement/CostTests.cs
b79fc99e39403361da75be2369809eee153d1aa9536b3fe47dd3025004d2de7e  tests/Bastion.Simulation.Tests/Movement/GeometryTests.cs
700efad30b5f8d940b3c0e38a8926b3f877dd008da7204ac5078d33b9606941c  tests/Bastion.Simulation.Tests/Movement/SearchAndExecutionTests.cs
d72e2e04184fd6247d8efbe7573f171845f47304abf24b7653b0a5270ca2d9e0  tests/Bastion.Simulation.Tests/Movement/TestWorld.cs
```

Le registre avant l'avenant n° 1, identique à celui de `main`, avait pour empreinte `ee481509d3959889abf6c08cd92b8fde20093f8b31a318922f168966aaf80823`.

## Annexe B — Messages du propriétaire, mot pour mot

L'avenant n° 1 et l'avenant n° 2 sont aussi archivés dans `docs/mandates/` (§10).

### B.1 Autorisation d'exécution (2026-11-21T21:09:26.953Z)

Réponses aux deux questions posées par Claude Code :

> **Question :** « Le mandat d'implémentation MEC-0003 v1.0 est « en attente d'autorisation d'exécution ». Vérifications préalables conformes : base main 25e7a28d, MEC-0003 inscrite et « acceptée », branche claude/implementation-mec-0003-lot1 inexistante. Le conteneur n'a pas .NET : sans installation, ni la compilation ni les tests ne pourraient être exécutés localement. Le SDK 10.0.114 (celui de T-101, compatible avec global.json) peut être installé par apt dans le conteneur, sans toucher au dépôt. Autorisez-vous l'exécution du mandat ? »
> **Réponse :** « Autoriser, avec installation .NET (Recommandé) »
>
> **Question :** « Publication du mandat MEC-0003 (étape 6.5, « sous réserve de l'autorisation de publication du propriétaire ») : une fois les tests, la relecture indépendante et le rapport satisfaisants, puis-je commiter, pousser la seule branche claude/implementation-mec-0003-lot1 et ouvrir une PR en brouillon vers main, sans la fusionner ? »
> **Réponse :** « Oui, après contrôles (Recommandé) »

### B.2 Consignes sur l'écart de T13 (2026-11-21T21:41:14.860Z)

> BASTION — Écart documentaire T13 / MEC-0003
>
> L'anomalie est identifiée : l'assertion finale de T13 concernant la zone atteignable est incompatible avec les règles de déplacement et de collision de MEC-0003.
>
> **Consignes immédiates :**
>
> 1. Ne pas modifier le moteur C# pour satisfaire cette assertion.
> 2. Ne pas supprimer, ignorer ou neutraliser le test en échec.
> 3. Ne pas modifier le registre tant que la correction documentaire n'a pas été explicitement autorisée.
> 4. Consigner l'écart, son scénario de reproduction et le résultat réel des tests.
> 5. Proposer un avenant au mandat limité à la correction de la dernière phrase de T13, avec adaptation de l'assertion correspondante dans les tests C#.
>
> Après autorisation du propriétaire, appliquer uniquement cette correction, relancer les vérifications et soumettre le diff à revue.
>
> Ne modifier aucune autre règle de MEC-0003, ni MEC-0001 ou MEC-0002, ni le harnais. Ne pas publier ou fusionner sans autorisation distincte.

### B.3 Avenant n° 1 (2026-11-21T22:18:31.802Z)

> BASTION — Autorisation d'avenant n° 1 à MEC-0003 / T13
>
> Je valide la correction proposée pour T13.
>
> J'autorise exclusivement les deux modifications suivantes :
>
> 1. Registre "docs/gameplay/GAMEPLAY-DECISIONS.md"
>
> Dans le résultat attendu de T13, remplacer uniquement la dernière phrase :
>
> « La case (2,2) n'est pas non plus dans la zone atteignable »
>
> par :
>
> « La case (2,2) reste toutefois dans la zone atteignable : le chemin retenu est [NE, NW], pour 12 TU et 6 d'énergie ; l'unité y arrive orientée NW, et son emprise ne chevauche alors pas la case (3,1). »
>
> Toutes les autres phrases de T13, notamment le refus du deuxième pas N et la conservation de l'état après ce refus, doivent rester inchangées.
>
> 2. Test C# correspondant
>
> Remplacer exclusivement l'assertion erronée sur l'absence de (2,2) dans la zone atteignable par des assertions couvrant :
>
> - la présence de (2,2) dans la zone ;
> - le chemin [NE, NW] ;
> - son coût de 12 TU et 6 d'énergie ;
> - l'orientation finale NW.
>
> Conserver les vérifications existantes sur le refus du deuxième pas N et l'absence de débit lors de ce refus.
>
> Après correction :
>
> 1. Vérifier que le diff est strictement limité à ces deux modifications.
> 2. Relancer la compilation, les tests, le formatage et le harnais.
> 3. Faire contrôler l'ensemble du lot par un relecteur indépendant, avec une attention particulière à la géométrie, aux rotations, aux volumes balayés et à la conformité aux règles inscrites.
> 4. Préparer le rapport d'exécution et la revue.
>
> Restrictions :
>
> - Aucune modification supplémentaire du moteur C#.
> - Aucune modification des autres tests ou règles.
> - Aucun changement de MEC-0001 ou MEC-0002.
> - Aucun changement du harnais.
> - Aucun ajout à "docs/mandates/README.md" dans cet avenant.
> - Aucun commit, push ou PR sans autorisation de publication distincte.
>
> Cette autorisation ne porte que sur l'avenant n° 1 à T13.
>
> À l'issue des vérifications, présente le bilan et le diff avant toute publication.

### B.4 Avenant n° 2 (2026-11-22T04:51:30.049Z)

Le texte complet est archivé dans `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-2-transcription.md` ; son empreinte figure en annexe A.

### B.5 Autorisation de publication (2026-11-22T09:43:00.852Z)

> BASTION — MEC-0003 — Autorisation de publication du lot 1
> Je valide la clôture des vérifications du lot 1 de MEC-0003, sous les réserves documentées.
> J'autorise les opérations suivantes :
>
> 1. Ajouter uniquement l'avenant n° 2 à l'index `docs/mandates/README.md`, en respectant les conventions existantes.
> 2. Vérifier que les modifications définitives restent conformes au mandat initial et aux avenants n° 1 et n° 2.
> 3. Relancer les contrôles obligatoires après cette dernière modification documentaire.
> 4. Effectuer un commit unique contenant le lot MEC-0003, ses tests, les mandats et les rapports.
> 5. Pousser uniquement la branche `claude/implementation-mec-0003-lot1`.
> 6. Ouvrir une PR en brouillon vers `main`, avec la déclaration de traçabilité MEC-0003.
>
> Conditions :
>
> * Vérifier `origin/main` avant publication. Si la base a changé et nécessite une intervention sur l'historique, s'arrêter et me présenter la situation.
> * Ne pas modifier le moteur, les règles de gameplay ou les tests au-delà du périmètre déjà autorisé.
> * Conserver explicitement les réserves RL-11 et RL-13 ainsi que la limite de couverture signalée pour RL-01.
> * Ne pas présenter le recalcul du passage diagonal à l'exécution comme une règle validée.
> * Ne pas modifier MEC-0001, MEC-0002 ou le harnais.
> * Ne pas ajouter de correctifs ou de refactoring non demandés.
> * Ne pas effectuer de fusion.
>
> Après publication, transmettre le lien de la PR, le SHA du commit, le périmètre exact du diff et l'état réel de la CI.
> Cette autorisation concerne uniquement le commit, le push et la création de la PR en brouillon. La fusion nécessitera mon accord explicite.
