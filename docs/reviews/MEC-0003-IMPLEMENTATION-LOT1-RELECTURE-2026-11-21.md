# Relecture indépendante — MEC-0003, lot 1 (marche sur terrain plat)

| Champ | Valeur |
|---|---|
| Date | 21 novembre 2026 |
| Relecteur | agent relecteur indépendant, distinct du développeur (aucune ligne du lot écrite par lui) |
| Objet | lot d'implémentation non commité de la fiche `MEC-0003` |
| Dépôt relu | `/home/user/bastion`, branche `claude/implementation-mec-0003-lot1`, `HEAD` = `origin/main` = `25e7a28d18d29fea3753f3313a10f27126c3f274` |
| Références | `CLAUDE.md` ; registre `docs/gameplay/GAMEPLAY-DECISIONS.md` (fiche `MEC-0003`, l. 444-626, et règles de `MEC-0001` citées) ; mandat archivé `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-transcription.md` ; `docs/decisions/TECHNICAL-DECISIONS.md` ; avenant n° 1, tel que transmis dans l'ordre de relecture |
| Portée de l'avis | Ce rapport ne valide ni le commit, ni la publication, ni la fusion : ces décisions appartiennent au propriétaire. |

Conventions d'état : **vérifié** = commande exécutée par le relecteur, sortie et code de sortie observés ; **inspecté seulement** = lecture du code ou des documents, sans exécution qui le prouve ; **non vérifié** = ni l'un ni l'autre.

Aucune écriture n'a été faite dans `/home/user/bastion`. Git n'y a servi qu'en lecture (`status`, `diff`, `log`, `show`, `ls-files`, `rev-parse`). Toutes les compilations et tous les tests ont été lancés dans une copie : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-mec0003-lot1/copie/`.

---

## 1. Empreintes vérifiées

| Contrôle | Commande | Code | Résultat | État |
|---|---|---|---|---|
| 25 fichiers du lot | `cd /home/user/bastion && sha256sum -c /tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/impl/empreintes-lot.txt` | 0 | 25 × `OK` (registre modifié, mandat archivé, 18 sources, 5 fichiers de tests) | vérifié |
| Copie de travail fidèle | même commande, lancée dans la copie | 0 | 25 × `OK` | vérifié |
| Registre d'avant l'avenant | `git show HEAD:docs/gameplay/GAMEPLAY-DECISIONS.md \| sha256sum` ; `sha256sum …/impl/registre-avant-avenant.md …/impl/registre-25e7a28.md` | 0 | les trois valent `ee481509d3959889abf6c08cd92b8fde20093f8b31a318922f168966aaf80823` | vérifié |
| Registre après l'avenant | (première ligne) | 0 | `7b4931f37171ffbd66b825d53547413623303d3884564a6884fe2e75c4b0bbb7` | vérifié |

Empreintes du lot, telles que vérifiées :

```
7b4931f37171ffbd66b825d53547413623303d3884564a6884fe2e75c4b0bbb7  docs/gameplay/GAMEPLAY-DECISIONS.md
c8d9a38f4fb91cac07da621dfad7a21e8324553513d940fb228f98dd9b6d5fd8  docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-transcription.md
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
ffa0fd7033b56546e786b3ba30a60cecb49dd53d77f0a860ecc630d7c66009fa  tests/Bastion.Simulation.Tests/Movement/GeometryTests.cs
779db7ddca23f48d552efcc64a5eb5dd7428302923a9327f933604049011d62c  tests/Bastion.Simulation.Tests/Movement/SearchAndExecutionTests.cs
d72e2e04184fd6247d8efbe7573f171845f47304abf24b7653b0a5270ca2d9e0  tests/Bastion.Simulation.Tests/Movement/TestWorld.cs
```

## 2. Vérifications faites

| N° | Vérification | Commande (dans la copie, sauf mention) | Code | Résultat | État |
|---|---|---|---|---|---|
| V1 | État Git du dépôt relu | `git status`, `git status --ignored --porcelain`, `git rev-parse HEAD origin/main`, `git ls-files --others --exclude-standard` (dans `/home/user/bastion`) | 0 | 1 fichier modifié (registre) ; 24 fichiers non suivis, tous dans `src/Bastion.Simulation/Movement/`, `tests/Bastion.Simulation.Tests/Movement/` et le mandat archivé ; seuls `bin/` et `obj/` sont ignorés ; `HEAD` = `origin/main` = `25e7a28` | vérifié |
| V2 | Diff du registre limité à la phrase de l'avenant | `git diff`, `git diff --word-diff=porcelain` ; script `python3 -I` : remplacement exact de l'ancienne phrase par la nouvelle dans la version `HEAD` | 0 | une seule ligne différente (l. 610) ; `old.replace(ancienne, nouvelle) == new` vaut `True` ; texte identique à celui de l'avenant, point final compris | vérifié |
| V3 | Restauration | `dotnet restore` | 0 | — | vérifié |
| V4 | Compilation | `dotnet build --configuration Release` | 0 | 0 avertissement, 0 erreur (`TreatWarningsAsErrors` actif) | vérifié |
| V5 | Tests du lot | `dotnet test --configuration Release` | 0 | 42 tests, 42 réussis (40 du lot, 2 tests fumée) | vérifié |
| V6 | Format | `dotnet format --verify-no-changes` | 0 | aucune sortie | vérifié |
| V7 | Harnais | `bash scripts/harness/test-hooks.sh` | 0 | « 75 tests, 0 échec(s) » | vérifié |
| V8 | Godot, OXCE, X-COM | `grep -rniE "godot\|oxce\|openxcom\|x-com\|xcom"` sur les deux dossiers `Movement/` | 1 (aucune occurrence) | test fumée `SimulationDoesNotReferenceGodot` réussi (V5) | vérifié |
| V9 | Modèle indépendant sur les scénarios du registre | `python3 -I indep/registre_checks.py …/indep` | 0 | T05, T07 à T14, T20 à T28 retrouvés, dont l'avenant de T13 : chemin [NE, NW], 12 TU, 6 d'énergie ; marges T25/T26 = 134,31 mm ; T28 : −7,11 mm dans les deux sens | vérifié |
| V10 | Comparaison aléatoire, moteur C# contre modèle indépendant | `python3 -I indep/comparer.py …/indep …/dump/bin/Release/net10.0/Dump <graine> 70`, graines 2 à 5 | voir §4.8 | voir §4.8 | vérifié |
| V11 | Tests de mutation (23 mutants) | `python3 -I mutations.py …/copie …/mut` puis `mutations2.py`, `mutation-m5.py`, `mutation-une.py … M17` | 0 | voir §5.3 | vérifié |
| V12 | Tests du relecteur (cas limites) | `dotnet test --configuration Release --filter FullyQualifiedName~RevueTests` ; suite complète de la copie : `dotnet test --configuration Release` | 0 ; 0 | 22 tests réussis sur le moteur non modifié ; suite complète : 64 tests réussis (42 + 22) | vérifié |
| V13 | Lecture intégrale du code et des tests du lot | — | — | les 25 fichiers ont été lus en entier | inspecté seulement |
| V14 | CI GitHub | — | — | rien n'est publié ; la CI n'a pas tourné sur ce lot | non vérifié |

Fichiers du relecteur (tous hors du dépôt), dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-mec0003-lot1/` : `indep/modele_independant.py`, `indep/comparer.py`, `indep/comparer_zones.py`, `indep/registre_checks.py`, `dump/Program.cs`, `mutations.py`, `mutations2.py`, `mutation-m5.py`, `mutation-une.py`, `copie/tests/Bastion.Simulation.Tests/Movement/RevueTests.cs` ; journaux `*.log`.

## 3. Conformité aux règles

| Point | Règles | Constat | État |
|---|---|---|---|
| Coûts et arrondis | S2, Q3.1, Q3.2, Q3.7 à Q3.9, Q3.13, A6 | `MovementRules.CostOf` (l. 56-67) : base × facteur commun, arrondi supérieur pour chaque ressource ; diagonale : TU × 1,5 arrondi inférieur, énergie × multiplicateur propre arrondi supérieur. Terrain d'arrivée seul. Coûts identiques au modèle indépendant sur 61 824 pas (§4.8). | vérifié |
| Pas à 0 TU (A4 d) | A4 (d) | `baseTu ≥ 1` (l. 15-21) et facteur > 0 (`TerrainType`, l. 12-19) ; avec l'arrondi supérieur, aucun pas ne peut coûter 0 TU (même en diagonale : ⌊1 × 1,5⌋ = 1). Refus limité à la configuration ; rien n'est modifié dans `MEC-0001`. | inspecté, et testé par T19 |
| Passages diagonaux | S3, N2, ARB-A, G1, A2, A3 | Trajet en L, centre à centre, unité orientée vers le pas engagé sur les deux branches ; priorité N, E, S, W ; un seul pas facturé une fois. Les contrôles topologiques préalables (case intermédiaire, murs sur les deux arêtes) sont toujours impliqués par le contrôle physique : ils ne changent que le motif du refus, jamais le résultat. | vérifié (§4.8, mutants M6 à M8, M13) |
| Rotations | Q4.17, A5, A7, A8 | Rotation au centre de la case de départ ; côté le plus court pour 45°, 90° et 135° ; demi-tour horaire puis antihoraire ; surface balayée exacte (§4.3) ; largeur perpendiculaire à la face. Un refus du côté court n'est pas rattrapé par le côté long, ce qui est conforme (constat du registre, l. 555). | vérifié |
| Translations | A2 | Volume balayé = enveloppe convexe des deux emprises extrêmes, contrôlée sur tout le trajet, pas seulement aux extrémités. | vérifié (Rv10, §4.8) |
| Contact et chevauchement | Q4.2 | Chevauchement = intersection des intérieurs ; le contact ne bloque pas, y compris pendant une rotation (arc tangent à une face ou à un coin). | vérifié (T12, Rv01 à Rv03, Rv16) |
| Zone atteignable | Z1, G3 | Les deux ressources bornent la recherche ; une destination hors zone est refusée sans débit. La case de départ est exclue de la zone, ce que T05 impose (12 cases). | vérifié |
| Choix du chemin | G4, Q4.16 | Recherche « meilleur d'abord » sur (case, orientation), clé (TU, énergie, suite de directions). Preuve de correction en §4.9 ; identité avec une énumération exhaustive sur 86 zones aléatoires (§4.8). | vérifié |
| Exécution | A9, A4 (e), Q3.4, M-05, Q4.21 | Pas évalué sans effet de bord (état immuable) ; nouvel état seulement si tous les contrôles réussissent ; coût réel calculé sur la carte courante ; arrêt au premier refus, sans recalcul. | vérifié (T13, T16, T17, T24, T28, Rv13, Rv15) |
| Résultat d'un pas | fiche, l. 571 | `StepOutcome` porte le sens de rotation, le passage et le motif d'arrêt. | inspecté |
| Règles inventées | CLAUDE.md §3 | Aucune règle de jeu inventée trouvée. Choix techniques à signaler : tolérance géométrique nulle (RL-14) ; passage choisi de nouveau à l'exécution (RL-13). | inspecté |

## 4. Géométrie, en profondeur

### 4.1 Calcul exact

- `Rational` (BigInteger, toujours réduit, dénominateur > 0) et `Surd` (a + b√2) : opérations correctes. Le signe de a + b√2 est exact : à signes opposés, la comparaison de a² et 2b² suffit, l'égalité étant impossible pour a, b ≠ 0 (√2 irrationnel). La division par la norme c² − 2e² ne s'annule que pour un diviseur nul. **Inspecté.**
- Toutes les coordonnées utiles sont dans ℚ(√2) : centres et pavés rationnels, vecteurs de face et latéraux à 0, ±1 ou ±√2/2, intersections de découpage obtenues par division dans ℚ(√2). Aucune racine d'autre nombre n'est nécessaire, car le rayon n'intervient que par son carré. **Inspecté.**
- La double représentation de zéro dans `Rational` (`default` contre 0/1) est sans effet : aucune égalité de valeurs n'est utilisée sur ces types (`grep`, code 0 : seule occurrence `sense == RotationSense.Clockwise`). **Vérifié.**

### 4.2 Axes séparateurs pour la translation

- Les pas en translation sont toujours orthogonaux : un pas diagonal est décomposé en deux branches orthogonales (A2).
- L'enveloppe convexe d'un rectangle translaté selon un axe a pour arêtes celles du rectangle (normales : face et latéral) et deux arêtes parallèles au déplacement, dont la normale est l'un des axes x ou y.
- Le pavé n'a que les normales x et y. Les axes `forward`, `right`, x et y suffisent donc, et le théorème vaut aussi pour la séparation faible : deux polygones convexes ont des intérieurs disjoints si et seulement s'il existe un axe, normal à une arête de l'un d'eux, où leurs projections se touchent au plus. Le test `<= 0` (`Collision.cs`, l. 24) traite donc exactement le contact comme admis.
- Les huit points projetés donnent la projection exacte de l'enveloppe, sans la construire. **Inspecté ; vérifié par comparaison (§4.8) et par Rv10.**

### 4.3 Rotation : est-ce bien la surface balayée exacte ?

Oui. Démonstration, pour un huitième de tour d'angle φ = 45° autour du centre O :

1. **Inclusion des secteurs.** À l'instant t, le segment [O, coin j] est dans l'emprise R(t), qui est convexe et contient O. Le secteur balayé par ce segment est donc dans la surface balayée S.
2. **Recouvrement.** Soit p ∈ R(t), à distance r de O. Sur le cercle de rayon r, l'ensemble des angles où le rectangle est présent est une réunion d'arcs (le cercle entier si r ≤ demi-côté court). Chaque arc contient la direction d'au moins un coin : pour un rectangle de demi-côtés a ≥ b, si b < r ≤ a, les deux arcs centrés sur ±x contiennent les directions ±arctan(b/a) ; si a < r < R, les quatre arcs contiennent chacun la direction de leur coin. L'arc I qui porte p au temps t balaie, pendant le huitième de tour, I ∪ … ∪ (I + φ). La partie qui n'est ni dans I (emprise de départ) ni dans I + φ (emprise d'arrivée) est comprise entre α_c et α_c + φ, à un rayon r < R : elle est dans le secteur du coin c.
3. **Intérieurs.** Les pièces (deux rectangles, quatre secteurs de 45°) sont des convexes fermés en nombre fini. L'intérieur de S rencontre l'intérieur du pavé si et seulement si l'une des pièces le fait, et cela équivaut à l'existence d'un instant t où l'intérieur de R(t) rencontre celui du pavé (argument de mesure : chaque point de rayon r < R reste couvert pendant un intervalle de temps de longueur non nulle).
4. **Correspondance des coins.** `Offsets` (`StepGeometry.cs`, l. 124-138) garde le rang de chaque coin d'une orientation à la suivante ; le coin j décrit bien l'arc qui va de `Offsets(from)[j]` à `Offsets(to)[j]`. Le secteur de 45° entre deux vecteurs est unique et ne dépend pas du sens, ce qui rend la décomposition valable dans les deux sens.

Conséquence attendue et retrouvée : un demi-tour balaie le disque de rayon égal à la demi-diagonale (constat du registre, l. 556). **Inspecté (démonstration) ; vérifié par comparaison à un échantillonnage angulaire indépendant (§4.8), par T28 et par les mutants M2 et M3.**

### 4.4 Test secteur–pavé

- Le pavé est découpé par les deux demi-plans du coin angulaire : leur intersection est le cône, puisque l'angle est inférieur à 180°.
- Si le polygone découpé est d'aire nulle, les intérieurs du cône et du pavé sont disjoints : pas de chevauchement.
- Sinon, l'intérieur du secteur rencontre celui du pavé si et seulement si la distance du sommet au polygone découpé est strictement inférieure au rayon : le polygone est convexe et d'intérieur non vide, donc un point à distance < R se rapproche de points intérieurs.
- Le découpage de Sutherland-Hodgman retient les sommets de signe nul sans les dupliquer ; la distance au polygone traite le cas « sommet intérieur » (distance nulle) et les arêtes de longueur nulle.

**Inspecté ; vérifié par Rv16** : un arc qui passe exactement par le coin d'un mur, à 500 mm, est un contact ; à 499,40 mm (mur de 202 mm), la rotation est refusée.

### 4.5 Préfiltre `Near`

`BeyondReach` (`StepGeometry.cs`, l. 118) écarte un pavé seulement si son écart, selon x ou selon y, au pavé englobant du trajet du centre est au moins égal à la demi-diagonale R. Tout point de l'unité reste à une distance au plus R du centre, donc son abscisse (ou son ordonnée) diffère de celle du centre de R au plus. Un pavé écarté ne peut être que touché, jamais chevauché. Le préfiltre est donc conservatif ; à l'égalité, il écarte un pavé seulement tangent, ce qui est exact. **Inspecté ; vérifié par le mutant M23**, préfiltre resserré, détecté par T14 et T28.

### 4.6 Obstacles, repère et orientations

- **Cases infranchissables** : pavé de la case entière. **Murs** : centrés sur l'arête, épaisseur répartie de part et d'autre (Q2.5), longueur exactement d'un coin à l'autre de l'arête (fiche, l. 469). Au croisement de deux murs perpendiculaires, il reste une encoche de ½ épaisseur × ½ épaisseur côté extérieur : c'est la lecture littérale de la fiche, et l'encoche n'ouvre aucun passage, car elle n'est jamais reliée au côté intérieur. **Inspecté.**
- **Bords** : quatre pavés extérieurs, d'épaisseur largeur + profondeur + case, plus grande que tout débordement possible (≤ R − demi-case). Le modèle indépendant traite les bords autrement (coins de l'emprise hors du rectangle de la carte), avec le même résultat (§4.8). **Vérifié.**
- **Repère** : x vers l'est, y vers le sud ; cap θ compté du nord dans le sens horaire ; face = (sin θ, −cos θ), latéral droit = (cos θ, sin θ). Les huit lignes de `Frame` (l. 157-173) ont été recalculées une à une ; les valeurs d'énumération croissent dans le sens horaire (N = 0 … NW = 7), d'où un pas de +1 pour le sens horaire. **Inspecté ; vérifié** par T25, T26 et T27, et par les mutants M10 à M12.
- **A8** : demi-largeur portée par le vecteur latéral, demi-profondeur par le vecteur de face. **Vérifié** (mutant M12 détecté par T12, T25 et T26).

### 4.7 Contacts exacts

| Cas | Attendu | Résultat | État |
|---|---|---|---|
| Couloir, largeur 1 400 contre faces à ± 700 (T12) | contact, admis | admis ; 1 402 refusé | vérifié |
| Arc d'un coin tangent à la face d'un mur (Rv01 : unité 600 × 800, R = 500, mur de 498, 500 ou 502 mm) | admis, admis, refusé | idem | vérifié |
| Disque d'un demi-tour tangent à une case infranchissable (Rv02) ou au bord de la carte (Rv03) | admis | admis | vérifié |
| Arc d'un coin passant par le coin d'un mur, en (400, −300) (Rv16 : mur de 198, 200 ou 202 mm) | admis, admis, refusé | idem | vérifié |
| Translation glissant le long d'une face (Rv16, pas E) | admis | admis | vérifié |

### 4.8 Contre-vérification indépendante

**Méthode** (`indep/modele_independant.py`, écrit à partir du registre seul, sans reprendre le code C#) :
- géométrie en flottants, séparation signée par axes séparateurs ;
- rotation : 360 échantillons par huitième de tour, puis raffinement par section dorée autour de chaque minimum local ;
- translation : recherche ternaire, la séparation étant convexe en fonction de la position ;
- bords : coins de l'emprise hors du rectangle de la carte ;
- aucun contrôle topologique : seule la physique décide ;
- chemins : énumération exhaustive de toutes les suites de pas payables, puis minimum de (TU, énergie, suite) ; ni file de priorité ni dominance.

Le programme `dump/Program.cs` n'interroge que l'API publique du lot (`CreateState`, `EvaluateStep`, `ComputeReachability`, `ExecutePath`).

**Scénarios aléatoires** :
- cartes de 2 à 5 × 2 à 5 cases, cases de 1 000, 1 200, 1 500 ou 2 000 mm ;
- murs de 50 à 300 mm sur 18 % des arêtes, 12 % de cases infranchissables, terrains à 1,25, 1,5 ou 2 ;
- multiplicateur d'énergie des diagonales de 1,5, 2 ou 3 ; emprises de 100 mm à deux fois la case ;
- comparaisons : admissibilité au repos de chaque (case, orientation) ; pour chaque état admissible et chaque direction, catégorie du refus, sens de rotation, passage et coût ; zone, meilleur chemin et exécution de chaque chemin (achèvement, position, ressources).

| Graine | Scénarios | États au repos | Pas comparés | Zones | Désaccords | Quasi-contacts (marge absolue < 10⁻³ mm), tous concordants | Code |
|---|---|---|---|---|---|---|---|
| 2 | 70 | 5 752 | 14 976 | 24 | 0 | 44 | 0 |
| 3 | 70 | 6 096 | 13 824 | 13 | 0 | 137 | 0 |
| 4 | 70 | 6 160 | 16 736 | 25 | 0 | 202 | 0 |
| 5 | 70 | 5 944 | 16 288 | 24 | 0 | 54 | 0 |
| **Total** | **280** | **23 952** | **61 824** | **86** | **0** | **437** | — |

Un essai préalable (graine 1, 15 scénarios : 1 064 états, 2 064 pas, 4 zones) a donné aussi 0 désaccord (code 0). Journal : `comparaison-aleatoire.log`.

**Sensibilité du dispositif** : branché sur le mutant M17 (recherche qui ignore l'orientation), il ne trouve aucun désaccord sur 44 zones aléatoires (`python3 -I indep/comparer_zones.py … 11 150`, code 0). Les cartes aléatoires ne produisent donc pas les cas où l'orientation conditionne la suite du chemin. Ce point repose sur la démonstration du §4.9 et sur le test construit Rv17 (RL-05).

### 4.9 Correction de la recherche de chemin (inspecté)

- Les étiquettes sortent de la file par clé (TU, énergie, suite) croissante, et chaque pas coûte au moins 1 TU : un enfant a une clé strictement supérieure à son parent.
- Une étiquette L écartée par une étiquette L′ du même état (case, orientation), avec TU′ ≤ TU et énergie′ ≤ énergie, a des prolongements tous au moins aussi bons, car les contrôles d'un pas ne dépendent que de l'état. À TU et énergie égales, L′ précède L dans l'ordre lexicographique sans en être un préfixe, puisqu'un préfixe coûterait moins de TU ; la concaténation préserve donc l'ordre.
- La première étiquette retenue sur une case est donc son meilleur chemin au sens de G4 et Q4.16. La recherche termine, car chaque pas coûte au moins 1 TU et les ressources sont bornées.
- Déterminisme : l'ordre est total sur des suites distinctes ; aucun hasard, aucune dépendance à l'ordre de hachage dans les résultats.

## 5. Tests

### 5.1 Les 30 scénarios du registre

| Scénario | Test | Fidélité au résultat attendu | Remarque |
|---|---|---|---|
| T01 | `CostTests.T01_…` | oui (4/2, débit exécuté) | — |
| T02 | `CostTests.T02_…` | oui (6/3) | coût seul |
| T03 | `CostTests.T03_…` | oui (6/3, 9/5, 8/4, 12/6) | — |
| T03b | `CostTests.T03b_…` | oui (5/3, 7/5, puis 7/6) | — |
| T04 | `CostTests.T04_…` | oui (4/2) | — |
| T05 | `SearchAndExecutionTests.T05_…` | oui (12 cases, puis les 8 voisines) | — |
| T06 | `…T06_…` | oui (refus, état identique) | — |
| T07 | `…T07_…` | oui ([E, NE], 11/6) | carte 3 × 2 (taille non fixée par le registre) |
| T08 | `…T08_…` | oui ([N, E] 8/4 ; [NE] 6/6) | — |
| T09 | `…T09_…` | oui ([NE, E], 10/5) | — |
| T10 | `GeometryTests.T10_…` | oui | débit non affirmé (RL-10) |
| T11 | `…T11_…` | oui | — |
| T12 | `…T12_…` et contre-test 1 402 | oui | — |
| T13 | `…T13_VolumeMayExceed…` et `…T13_TargetCellIsNotInTheReachableZone` | oui, avec l'avenant n° 1 | nom du second test contraire à son contenu (RL-08) ; passages et position finale non affirmés (RL-02, RL-09) |
| T14 | `…T14_…` | oui | 45° et 180° seulement (RL-10) |
| T15 | `…T15_…` | oui | totaux seulement (RL-10) |
| T16 | `…T16_…` | oui (coût réel 6/3, 0 TU, 95) | — |
| T17 | `…T17_…` | oui (toutes les valeurs) | — |
| T18 | `…T18_…` | oui (deux modèles distincts) | — |
| T19 | `ConfigurationTests.T19_…` (4 tests) | oui (4 cas, messages explicites) | — |
| T20 à T22 | `…T20_T21_T22_…` (théorie, 4 cas) | oui | — |
| T23 | `…T23_…` | oui | — |
| T24 | `…T24_…` | oui | rotation libre déduite de l'ordre des contrôles (RL-10) |
| T25, T26 | `…T25_…`, `…T26_…` | oui | — |
| T27 | `…T27_…` | oui | — |
| T28 | `…T28_…` | oui | les deux sens, pris un à un, ne sont pas observables (RL-10) |
| T29 | `…T29_…` (théorie, 4 cas) | oui | — |

Les 30 scénarios sont présents. Aucun résultat attendu n'est modifié, hors l'avenant de T13, dont le contenu est fidèlement repris (présence de (2,2), chemin [NE, NW], 12 TU et 6 d'énergie, orientation finale NW, vérifications du 2e pas N conservées). **Inspecté ; exécuté et réussi (V5).** L'avenant a été recalculé indépendamment (V9) : il est exact.

### 5.2 Points du §4 du mandat

| Point | Démontré par | Réserve |
|---|---|---|
| Calcul des TU et de l'énergie | T01 à T04, T03b | l'arrondi supérieur des TU n'est jamais sollicité (RL-06) |
| Choix déterministe des chemins | T07 à T09, T13, T18 | l'orientation dans l'état de recherche n'est pas protégée par un test (RL-05) |
| Diagonale quand un seul trajet en L est praticable | T10, T23, T25, T26 | seulement des cas topologiques (RL-02) |
| Contrôle réel des rotations et des collisions | T14, T25, T26, T28 | collisions en translation non démontrées hors extrémités (RL-01) |
| Contact admis, chevauchement interdit | T12 et contre-test | contact en rotation non démontré (RL-04) |
| Conservation de l'état lors d'un refus | T13, T17, T24, T28 | arrêt de l'ordre non démontré (RL-03) ; état rendu d'un refus faute de ressources non affirmé (RL-07) |
| Calculs de chemin et de zone sans modification | `ZoneAndPathComputationsDoNotModify…` | — |

### 5.3 Tests de mutation

Chaque mutant introduit, dans une copie séparée, un défaut plausible. Commandes : `python3 -I mutations.py …`, puis `mutations2.py`, `mutation-m5.py` et `mutation-une.py … M17`, toutes de code 0. Dans la première passe, M9 et M13, écrits avec un `if (false)`, ne compilaient pas : `TreatWarningsAsErrors` refuse le code inaccessible. Ils ont été réécrits avec une condition non constante dans `mutations2.py`.

| Mutant | Tests du lot | Avec les tests du relecteur |
|---|---|---|
| M1 translation contrôlée aux extrémités seulement | **survit** | tué (Rv10) |
| M2 rotation sans secteurs | tué (T28) | — |
| M3 rotation par disque circonscrit | tué (T25, T26) | — |
| M4 contact compté comme chevauchement | tué (T12, T28) | — |
| M5 secteur : contact au rayon compté comme chevauchement | **survit** | tué (Rv16) |
| M6 branches du L sans contrôle physique | **survit** | tué (Rv11) |
| M7 seconde branche du L non contrôlée | **survit** | tué (Rv11) |
| M8 branches du L contrôlées avec l'orientation de départ | **survit** | tué (Rv12) |
| M9 rotation de 45° à 135° non contrôlée | tué (T14) | — |
| M10 côté long pour 45° à 135° | tué (T18, T25, T26) | — |
| M11 demi-tour antihoraire d'abord | tué (T29) | — |
| M12 largeur et profondeur inversées | tué (T12, T25, T26) | — |
| M13 sans contrôle topologique du mur | tué (T24, par le seul motif du refus) | — |
| M14 ordre des directions inversé | tué (T08, T09, T13) | — |
| M15 énergie ignorée au départage | tué (T07) | — |
| M16 zone sans contrôle d'énergie | tué (T05, T08) | — |
| M17 recherche sans orientation dans l'état | **survit** | tué (Rv17) |
| M18 énergie diagonale arrondie à l'inférieur | tué (T03, T03b, T07) | — |
| M19 TU arrondies à l'inférieur après le facteur | **survit** | tué (Rv14) |
| M20 rotation appliquée lors d'un refus | tué (T13, T24, T28) | — |
| M21 débit lors d'un refus faute de TU | **survit** | tué (Rv15) |
| M22 exécution poursuivie après un refus | **survit** | tué (Rv13) |
| M23 préfiltre trop serré | tué (T14, T28) | — |

Le moteur non modifié réussit les 22 tests du relecteur (V12). Ces tests ne sont pas dans le dépôt : ce sont des propositions.

## 6. Périmètre

| Point | Constat | État |
|---|---|---|
| Fichiers touchés | `src/Bastion.Simulation/Movement/**` (18), `tests/Bastion.Simulation.Tests/Movement/**` (5), mandat archivé dans `docs/mandates/`, registre (avenant). Tous autorisés par le §5 du mandat ou par l'avenant. Aucun fichier de `.claude/`, `scripts/harness/`, `.github/workflows/`, ni `CLAUDE.md`, ni `docs/decisions/`, ni `docs/references/` | vérifié (V1) |
| Diff du registre | strictement la phrase de l'avenant (V2) | vérifié |
| Godot | aucune référence ; projet sans paquet ajouté | vérifié (V8) |
| OXCE | aucune mention ; algorithmes (calcul exact dans ℚ(√2), axes séparateurs, secteurs) sans équivalent dans le moteur d'OXCE | inspecté seulement (une absence de copie ne se prouve pas par `grep`) |
| Architecture générique | non : tout est propre à la marche en plan de `MEC-0003` ; `Geometry` est `internal` ; la hauteur est conservée sans usage (A8, documenté) | inspecté |
| Rapport de fin dans `docs/reviews/` | absent à ce stade, comme prévu par le §6 du mandat (après la relecture) | vérifié (V1) |

## 7. Qualité

- **Lisibilité** : bonne. Commentaires en français, qui citent la règle appliquée à chaque endroit ; découpage clair (modèle, coûts, géométrie, recherche, résultats). **Inspecté.**
- **Simplicité** : le calcul exact (`Rational`, `Surd`) ajoute environ 150 lignes, mais il évite toute tolérance numérique et rend les contacts des tests exacts. C'est justifié, et il reste interne. **Inspecté.**
- **Messages d'erreur** : explicites, en français, avec la règle citée ; quelques imprécisions mineures (RL-16). **Inspecté ; vérifié pour T19.**
- **Déterminisme** : vérifié (T18 ; comparaisons reproductibles par graine).
- **Performance** : zone sur une carte de 20 × 20 avec 60 TU : 399 cases en 672 ms (Rv06). Suffisant pour ce lot. **Vérifié.**

## 8. Constats

Aucun constat **bloquant** n'a été trouvé : ni non-conformité aux règles, ni erreur géométrique, ni test infidèle aux résultats attendus du registre.

### RL-01 — Collision en cours de translation : aucun test ne la démontre
- **Gravité :** à corriger.
- **Où :** `tests/Bastion.Simulation.Tests/Movement/GeometryTests.cs` (absence) ; code correct dans `src/Bastion.Simulation/Movement/Geometry/StepGeometry.cs`, l. 67-76.
- **Constat :** le mandat (§3) exige « la vérification des collisions sur l'ensemble du mouvement, pas uniquement aux positions de départ et d'arrivée ». Le mutant M1, qui ne contrôle que les deux emprises extrêmes, réussit les 42 tests. Les murs traversés sont tous arrêtés par le contrôle topologique préalable.
- **Reproduction (Rv10) :**
  - carte de 3 × 3, mur entre (1,0) et (2,0) ;
  - unité de 1 700 × 600 mm orientée E en (1,1), pas E ;
  - ni le départ ni l'arrivée ne touchent le mur, mais le balayage le chevauche de 100 mm ;
  - le moteur refuse à juste titre (`VolumeCollision`), et le test échoue sous M1.
- **Correction suggérée :** ajouter ce test, ou un équivalent.

### RL-02 — Contrôle physique du trajet en L (ARB-A, G1, A2) non démontré
- **Gravité :** à corriger.
- **Où :** `GeometryTests.cs`, l. 83-96 (T13), et tests T10, T11, T23, T25, T26 ; code correct dans `MovementModel.cs`, l. 227-242.
- **Constat :** tous les refus de passage des tests sont topologiques (mur sur l'arête, case intermédiaire infranchissable). Les mutants M6 (aucun contrôle physique des branches), M7 (seconde branche non contrôlée) et M8 (branches contrôlées avec l'orientation de départ au lieu du pas engagé, contre A2) réussissent les 42 tests. T13 n'affirme pas les passages du chemin [NE, NW], alors que le second pas n'emprunte le passage W que parce que le passage N est physiquement impraticable.
- **Reproduction :**
  - Rv11 : carte de 5 × 6, (3,1) infranchissable, unité de 1 600 mm orientée N en (2,3), pas NE ; aucun mur, cases intermédiaires franchissables, refus attendu `NoPracticablePassage` ;
  - Rv12 : carte de 4 × 3, unité de 1 400 × 200 orientée N en (1,1), mur nord de (1,1) et mur de 200 mm à l'est de (2,1), pas NE ; passage E attendu, praticable seulement si l'unité est orientée NE ;
  - exécution de T13 (Rv07) : passages N puis W.
- **Correction suggérée :** affirmer les passages [N, W] dans le test T13 (dans la limite de l'avenant, à confirmer par le propriétaire), et ajouter Rv11 et Rv12, ou des équivalents.

### RL-03 — Arrêt de l'ordre au premier refus (Q3.4, Q4.21) non démontré
- **Gravité :** à corriger.
- **Où :** `SearchAndExecutionTests.cs`, l. 110-126 (T17) ; code correct dans `MovementModel.cs`, l. 113-123.
- **Constat :** dans T17, le pas refusé est le dernier du chemin. Le mutant M22, qui poursuit l'exécution après un refus, réussit donc tous les tests.
- **Reproduction (Rv13) :** carte de 3 × 2, (2,1) infranchissable, chemin [E, E, N] depuis (0,1). Attendu : 2 résultats de pas, unité en (1,1), 56 TU et 98 d'énergie. Le test échoue sous M22.
- **Correction suggérée :** ajouter un test où un pas exécutable suit le pas refusé.

### RL-04 — Contact pendant une rotation non testé
- **Gravité :** observation.
- **Où :** `Collision.cs`, l. 55.
- **Constat :** le mutant M5, qui compte comme chevauchement un arc tangent, réussit les 42 tests. Une tangence dont le point de contact est aligné avec le centre selon x ou y (Rv01 à Rv03) n'atteint jamais ce test : le pavé est déjà écarté par le préfiltre, ce qui est exact. Le cas sensible est l'arc qui passe par le coin d'un pavé.
- **Reproduction (Rv16) :** case de 800 mm, mur de 200 mm sur l'arête nord de (2,1), unité de 600 × 800 en (1,1) orientée N, pas E. Attendu : admis ; avec un mur de 202 mm : `RotationBlocked`.
- **Correction suggérée :** ajouter Rv16, qui complète T12 pour la distinction entre contact et chevauchement demandée au §4 du mandat.

### RL-05 — L'orientation dans l'état de recherche n'est protégée par aucun test
- **Gravité :** observation.
- **Où :** `PathSearch.cs`, l. 45.
- **Constat :** le mutant M17, qui compare les étiquettes par case seulement, réussit les 42 tests du lot. Le code est correct (§4.9), mais les cartes aléatoires du §4.8 ne sollicitent pas ce point : M17 n'y produit aucun désaccord (44 zones).
- **Reproduction (Rv17) :**
  - carte de 3 × 5, couloir de la colonne 1 sur les lignes 2 à 4 ;
  - unité de 1 300 mm orientée N en (1,3), 24 TU ;
  - (1,4) n'est atteignable qu'en sortant du couloir pour faire demi-tour en (1,1) : [N, N, S, S, S], 20 TU et 10 d'énergie, valeurs confirmées par le modèle indépendant ;
  - le moteur trouve ce chemin, et M17 fait échouer le test (`python3 -I mutation-une.py … M17`, code 0, « détecté »).
- **Correction suggérée :** ajouter Rv17, ou un scénario équivalent où la suite du chemin dépend de l'orientation d'arrivée sur une case intermédiaire.

### RL-06 — Arrondi supérieur des TU (Q3.13) jamais sollicité
- **Gravité :** observation.
- **Où :** `MovementRules.cs`, l. 59 ; `CostTests.cs`.
- **Constat :** tous les facteurs des tests donnent un nombre entier de TU (4 × 1,25, 4 × 1,5, 4 × 2). Le mutant M19, qui arrondit à l'inférieur, réussit les 42 tests.
- **Reproduction (Rv14) :** facteur 1,1. Attendu : orthogonal 5 TU et 3 d'énergie ; diagonal 7 TU et 5 d'énergie.
- **Correction suggérée :** ajouter ce cas, comme test complémentaire hors registre.

### RL-07 — État rendu lors d'un refus faute de ressources non affirmé au niveau du pas
- **Gravité :** observation.
- **Où :** `SearchAndExecutionTests.cs`, l. 117-125.
- **Constat :** T17 affirme `FinalState`, qui est l'état précédent, et non l'état porté par le résultat du pas refusé. Le mutant M21, qui débite les TU dans ce résultat, réussit les 42 tests, alors que la documentation de `StepOutcome` promet l'état initial (A9).
- **Correction suggérée :** dans T17, `Assert.Same(outcome.Steps[0].State, outcome.Steps[1].State)` ; ou ajouter Rv15.

### RL-08 — Nom du second test T13 contraire à son contenu
- **Gravité :** à corriger.
- **Où :** `GeometryTests.cs`, l. 84.
- **Constat :** `T13_TargetCellIsNotInTheReachableZone` affirme désormais que (2,2) **est** dans la zone. La proposition d'avenant du développeur prévoyait un nouveau nom (`T13_TargetCellIsReachedWithADiagonalOrientation`), mais le texte autorisé ne parle que des assertions.
- **Correction suggérée :** renommer la méthode. Le propriétaire dit si un renommage entre dans l'avenant n° 1.

### RL-09 — T13 : arrivée en (2,2) seulement implicite
- **Gravité :** observation.
- **Où :** `GeometryTests.cs`, l. 95.
- **Constat :** seule l'orientation finale NW est affirmée. Elle implique l'exécution du pas NW, donc l'arrivée en (2,2), mais de façon indirecte.
- **Correction suggérée :** affirmer aussi `Completed`, la position (2,2) et les ressources restantes (48 TU, 94 d'énergie), comme dans Rv07. Le résultat attendu, « l'unité y arrive orientée NW », le permet.

### RL-10 — Assertions partielles dans plusieurs tests fidèles
- **Gravité :** observation.
- **Constat, test par test :**
  - **T10** (l. 28) : « au coût d'un seul pas diagonal » ; le coût est affirmé, pas le débit (54 TU, 97 d'énergie) ;
  - **T14** (l. 99-107) : « une rotation de 45° ou plus » ; 45° et 180° sont testés, 90° et 135° ne le sont pas ;
  - **T15** (`SearchAndExecutionTests.cs`, l. 90-91) : totaux seulement, pas le débit pas à pas ;
  - **T24** (l. 136-149) : « la rotation N → E serait libre » ; ce n'est déduit que de l'ordre des contrôles, qui place le motif `WallOnEdge` après la rotation ;
  - **T28** (l. 191-204) : chaque sens n'est pas observable séparément, car `RotationIsFree` est interne.
- **Correction suggérée :** compléter les assertions. Par exemple : T14 en théorie sur les sept directions ; pour T24, un contre-test sans mur, où le pas E est admis avec une rotation horaire.

### RL-11 — `UnitState` : validation de `CreateState` contournable
- **Gravité :** à corriger.
- **Où :** `src/Bastion.Simulation/Movement/UnitState.cs`, l. 17-23.
- **Constat :** les accesseurs `init` publics permettent `état with { Position = …, Tu = -7 }` depuis tout code appelant. La documentation (l. 4-5) affirme pourtant qu'un état se crée par `CreateState`, qui le valide. On obtient ainsi un état hors invariants (TU négatives, position en chevauchement). Les pas évalués depuis un tel état restent refusés quand le volume chevauche, mais l'invariant n'est plus garanti par le type.
- **Reproduction :** Rv04.
- **Correction suggérée :** accesseurs `private init` ou `internal init`, le moteur produisant lui-même les états suivants.

### RL-12 — `ExecutePath` public : déplacement partiel vers une case hors zone
- **Gravité :** observation, point à décider.
- **Où :** `MovementModel.cs`, l. 107.
- **Constat :** un appelant peut exécuter une suite de pas quelconque et s'arrêter faute de TU, comme le permettait S5, que Z1 supplante pour la sélection normale. Dans le lot, les ordres passent par `ExecuteOrder`, qui applique Z1 ; `ExecutePath` sert aux tests de A4 (g).
- **Reproduction (Rv05) :** carte de 5 × 1, 8 TU, chemin [E, E, E, E] ; (4,0) est hors zone, et l'unité s'arrête en (2,0).
- **Correction suggérée :** réserver `ExecutePath` au moteur et aux tests (`internal`, avec `InternalsVisibleTo`), ou documenter sa portée.

### RL-13 — Passage choisi de nouveau à l'exécution
- **Gravité :** observation, point à décider.
- **Où :** `MovementModel.cs`, l. 210-217 ; `PlannedPath` ne mémorise pas les passages.
- **Constat :** à l'exécution, le passage d'un pas diagonal est recalculé selon A3 sur la carte courante. Si la carte change entre le calcul et l'exécution (A4 g, tests seulement), le pas emprunte l'autre passage au lieu d'être refusé. `MEC-0001` laisse ouvert le « repli d'un pas diagonal sur l'autre passage orthogonal » (l. 232 et 258). Le cas est inaccessible hors des tests dans ce périmètre, puisque tout est connu et que rien ne change. Aucun test ne le couvre.
- **Correction suggérée :** le signaler dans le rapport de fin comme choix d'implémentation sur un point ouvert, et laisser le propriétaire trancher.

### RL-14 — Tolérance géométrique nulle
- **Gravité :** observation, limite à déclarer.
- **Où :** `Collision.cs`, l. 24 et 55.
- **Constat :** le calcul est exact, donc sans aucune tolérance. Ce choix est cohérent avec T12 et T28 (contacts sur des millimètres entiers) et avec la fiche, qui laisse ouvertes la méthode et la précision (l. 482). `MEC-0001` laisse ouverte la tolérance des contacts (Q4.2, l. 185).
- **Correction suggérée :** le mentionner dans les limites du rapport de fin.

### RL-15 — Avenant n° 1 non archivé
- **Gravité :** à corriger (traçabilité).
- **Où :** `docs/mandates/` ; le registre, l. 610, est modifié sous son autorité.
- **Constat :** le registre est modifié au titre d'un avenant dont le texte n'est pas dans le dépôt. Le mandat archivé porte « Statut : mandat préparé, en attente d'autorisation d'exécution du propriétaire » et ne mentionne pas l'avenant. `CLAUDE.md` §3 exige une validation explicite du propriétaire pour toute modification d'un registre ; sa preuve n'est pas traçable dans le dépôt.
- **Correction suggérée :** archiver le texte de l'avenant n° 1 dans `docs/mandates/`, fichier autorisé par le §5 du mandat sous réserve de l'accord du propriétaire, et le citer dans le rapport de fin.

### RL-16 — Robustesse et précision des messages
- **Gravité :** observation.
- **Constat, point par point :**
  - `MovementRules.cs`, l. 59-66 : un facteur ou une base énorme lève une `OverflowException` brute, sans message (Rv09, facteur 10⁹) ;
  - `Millimetres.cs`, l. 17-22 : une valeur supérieure à `int.MaxValue` reçoit le message « strictement positif » ;
  - `MovementModel.cs`, l. 45-48 : le paramètre nommé est `tu`, même quand l'énergie est négative ;
  - `TacticalMap.cs`, l. 86-89 : `nameof(columns)` est cité aussi pour les lignes ;
  - `TacticalMap.cs`, l. 128-146 : l'épaisseur d'un mur n'est pas bornée par la largeur de case (Rv08 : mur de 5 000 mm sur des cases de 100 mm) ;
  - `TacticalMap.cs`, l. 144 : un second `AddWall` sur la même arête remplace le premier sans le dire.
- **Correction suggérée :** facultative ; messages et validations à préciser.

### RL-17 — Cache des plans non sûr en accès concurrent
- **Gravité :** observation.
- **Où :** `MovementModel.cs`, l. 13 et 145-155.
- **Constat :** `Dictionary` est modifié pendant les calculs. Sans effet en usage séquentiel, qui est le seul usage actuel, mais un même `MovementModel` ne doit pas être partagé entre fils d'exécution.
- **Correction suggérée :** le documenter.

### RL-18 — T13 : état de référence de la zone non précisé par le registre
- **Gravité :** observation.
- **Où :** registre, l. 610.
- **Constat :** la phrase de l'avenant ne dit pas depuis quel état la zone est calculée. Le chemin [NE, NW] n'atteint (2,2) que depuis l'état initial en (2,4), et c'est ce que le test calcule. Depuis (2,3), après le 1er pas, (2,2) est aussi atteignable, par [E, NW] pour 10 TU et 5 d'énergie : calcul indépendant (V9) et C# (Rv07).
- **Correction suggérée :** aucune dans ce lot. À préciser si la fiche est révisée.

### RL-19 — Divers, sans effet sur le lot
- **Gravité :** observation.
- **Constat, point par point :**
  - dans le clone relu, la branche locale `main` pointe encore sur `9e45c5d`, ancienne, alors que `origin/main` = `HEAD` = `25e7a28` ; la base du lot est donc correcte ;
  - la fiche garde « État d'implémentation : non commencé » et « Aucun n'est écrit ni exécuté », ce qui est normal, puisque le mandat interdit de toucher au registre hors de l'avenant ;
  - la colonne « État » de T13 vaut toujours « vérifié », c'est-à-dire « calculé par un script de préparation », alors que la nouvelle phrase a été établie par le moteur et par un script de contre-vérification.
- **Correction suggérée :** mise à jour éventuelle, par décision du propriétaire.

## 9. Verdict

**Conforme sous réserves.**

Motifs :
- **Règles :** le moteur applique les règles inscrites de `MEC-0003` et celles de `MEC-0001` auxquelles elle renvoie, sans règle de jeu inventée. Les deux choix sur des points ouverts (RL-13, RL-14) restent à signaler.
- **Géométrie :** elle est exacte. La surface balayée par une rotation est exactement décomposée (démonstration au §4.3). Les axes séparateurs suffisent, le préfiltre est conservatif, et les contacts exacts sont traités comme admis. Sur 280 cartes aléatoires (61 824 pas, 23 952 états au repos, 86 zones, dont 437 quasi-contacts), le moteur concorde sans aucun désaccord avec un modèle indépendant de méthode différente.
- **Tests :** les 30 scénarios sont implémentés, fidèlement au registre et à l'avenant n° 1, dont le contenu est exact. Le diff du registre se limite à la phrase autorisée. Les commandes du mandat réussissent.
- **Réserves :**
  - plusieurs exigences du mandat ne sont démontrées par aucun test, bien que le code soit correct : collisions sur tout le mouvement (RL-01), contrôle physique du L (RL-02), arrêt de l'ordre (RL-03) ;
  - le nom d'un test contredit son contenu (RL-08) ;
  - l'invariant de `UnitState` est contournable (RL-11) ;
  - l'avenant n'est pas archivé (RL-15).

  Aucune de ces réserves ne met en cause un comportement du moteur. Elles se corrigent par des tests et des retouches locales, sans toucher aux règles.

## 10. Limites de la relecture

- **Comparaison indépendante :**
  - elle est numérique, en flottants, avec un seuil de contact de 10⁻⁷ mm ;
  - les 437 quasi-contacts (marge absolue < 10⁻³ mm) ont tous concordé ;
  - les contacts exacts ont été tranchés par des tests exacts (§4.7) ;
  - l'énumération exhaustive limite les zones aléatoires à 24 TU au plus.
- **OXCE :** l'absence de copie n'est établie que par lecture et par recherche textuelle.
- **CI GitHub :** non vérifiée, car rien n'est publié.
- **Mandat archivé :** sa transcription n'a pas pu être comparée à l'original, qui n'est pas disponible ; il est inspecté seulement.
- **Tests du relecteur :** `RevueTests.cs`, 22 tests, n'existe que dans la copie du relecteur. Ce sont des propositions, non intégrées au lot.
