# Bastion — Lot 1D : premier prototype visuel Godot connecté à la simulation

**Date :** 22 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1D-v1.0.md`, fichier joint par le propriétaire le 2026-11-22T19:39:43Z et copié octet pour octet (SHA-256 `7d1579b3…a262`). Statut du fichier : « PRÉPARÉ — exécution non autorisée par le présent document ».
**Autorisation d'exécution :** 2026-11-22T19:45:23Z. En réponse à une question de Claude Code, le propriétaire a choisi « Autoriser, avec Xvfb (Recommandé) » : le mandat, plus une capture du rendu sous affichage virtuel avec des clics simulés par Godot. Elle n'autorise ni commit, ni push, ni PR.
**Base :** `origin/main` = `541018c8fb5f9b7b211c2128d68dea7eeeeb7670` (fusion de la PR #21), établie par `git fetch origin main` au démarrage.
**Branche :** `claude/lot-1d-prototype-godot`, créée à partir de `origin/main`.
**État :** lot exécuté, relu et vérifié localement. **Rien n'est commité ni publié.**

## 1. Résumé

Le prototype est un projet Godot 4.7.2 .NET indépendant, `src/Bastion.Client.Godot/`, en C# et `net10.0`, qui référence `Bastion.Simulation` par `ProjectReference`.

**La scène :**
- une scène 2D vue du dessus, avec une carte MEC-0003 de 5 × 5 cases de 1 500 mm et une case infranchissable en (3,2) ;
- une unité `StandardHuman` en (1,4), orientée N, avec 20 TU et 10 d'énergie, créée par `CreateState` ;
- la zone atteignable, rendue par `ComputeReachability`, est mise en évidence ;
- le clic gauche transmet un ordre par `ExecuteOrder` ;
- la touche R réinitialise le scénario ; c'est une commande de débogage.

La scène ne contient aucune règle de jeu.

**Résultats observés :**
- **Contrôle fumée en mode headless :** il passe par le code d'entrée de la scène et réussit ses 21 contrôles, avec le code de sortie 0.
- **Défauts introduits dans des copies jetables :** chacun est détecté (code 1 ou 2), ou borné par la limite de temps documentée (code 124).
- **Sous affichage virtuel Xvfb** (rendu logiciel OpenGL 3 de Mesa) : les mêmes contrôles réussissent, et 9 captures montrent la grille, la zone, l'unité, son orientation et le panneau.
- **Non-régression de Bastion :** tout est au vert, avec 46 tests sur 46.

**Relecture indépendante ciblée :** « conforme sous réserves », sans constat bloquant. Ses trois points à corriger sont traités (§5), ainsi que deux observations sur le contrôle fumée.

**Non vérifié :**
- un écran réel et une souris physique ;
- macOS et Windows ;
- l'export du jeu ;
- toute exécution par la CI, qui ne compile pas le client.

## 2. Fichiers

| Fichier | Rôle | Lignes |
|---|---|---|
| `src/Bastion.Client.Godot/project.godot` | projet Godot : scène principale `Main.tscn`, fenêtre de 800 × 528, assemblage `Bastion.Client.Godot`. Il est écrit au format de l'éditeur Godot, pour qu'une ouverture dans l'éditeur ne le modifie pas (RX-11) | 24 |
| `src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` | `Sdk="Godot.NET.Sdk/4.7.2"` (épinglage), `net10.0` explicite, `ProjectReference` vers `../Bastion.Simulation/Bastion.Simulation.csproj` | 12 |
| `src/Bastion.Client.Godot/Main.tscn` | scène unique : un `Node2D` portant le script, et un `Label` pour le panneau | 13 |
| `src/Bastion.Client.Godot/PrototypeScene.cs` | scénario, conversion pixels ↔ cases, transmission des ordres, dessin, panneau, touche R | 165 |
| `src/Bastion.Client.Godot/SmokeTest.cs` | contrôle fumée lancé par `-- --smoke-test`, capture facultative par `--capture=<dossier>` | 204 |
| `src/Bastion.Client.Godot/PrototypeScene.cs.uid`, `SmokeTest.cs.uid` | identifiants de ressources générés par Godot à l'import, stables, à conserver avec les scripts | 1 chacun |
| `src/Bastion.Client.Godot/README.md` | notice de démarrage Linux et macOS, avec les limites | 109 |
| `docs/mandates/BASTION-MANDAT-LOT-1D-v1.0.md` | mandat archivé, copie octet pour octet du fichier joint | 102 |
| `docs/mandates/README.md` | une ligne d'index ajoutée : provenance « original `.md` », statut, empreinte | +1 |
| `docs/reviews/LOT-1D-PROTOTYPE-GODOT.md` | ce rapport | — |
| `docs/reviews/LOT-1D-PROTOTYPE-GODOT-RELECTURE.md` | rapport de la relecture indépendante ciblée, copié sans modification | 416 |

**Fichiers inchangés :**
- le moteur `src/Bastion.Simulation/` et les tests `tests/Bastion.Simulation.Tests/` ;
- `Bastion.slnx`, `Directory.Build.props` et `global.json` ;
- la CI (`.github/workflows/`), le harnais et `CLAUDE.md` ;
- les registres `docs/gameplay`, `docs/decisions` et `docs/references`.

Le dossier `.godot/`, créé par Godot et par la compilation, est déjà ignoré par le `.gitignore` du dépôt.

## 3. Conception

**Scène (`PrototypeScene`).** Toutes les règles viennent du moteur. La scène :
- construit la carte (`TacticalMapBuilder` : 5 × 5, 1 500 mm, `Block((3,2))`) et le `MovementModel`, avec `MovementRules.Initial` et `UnitBody.StandardHuman` ;
- crée l'état initial par `CreateState`.

Elle se limite ensuite à quatre rôles :
- **conversion :** un pixel devient une case (cases de 96 pixels, origine en (24,24), arrondi à l'entier inférieur), et une case devient le centre de son dessin ;
- **transmission :**
  - un clic gauche dans la carte devient `ExecuteOrder(état, case)`, et l'état affiché devient l'état final rendu par le moteur ;
  - un clic hors de la carte ne transmet aucun ordre ;
  - la case de l'unité, la case infranchissable et les cases hors zone sont refusées par le moteur, dont le message est affiché ;
- **recalcul :** après chaque ordre et chaque réinitialisation, la zone est recalculée par `ComputeReachability` depuis le nouvel état ;
- **affichage :** les cases sont en vert si elles sont dans la zone du moteur, en gris foncé barré si elles sont infranchissables. L'unité est un disque de la largeur de son emprise (`Model.Body`), à l'échelle de la case (`Map.CellWidthMm`), avec un trait vers son orientation (`Direction.Offset()`). Le panneau montre la position, l'orientation, les TU, l'énergie, le nombre de cases atteignables et le dernier résultat.

**Ce qu'elle ne fait pas :**
- aucun chemin, coût, collision, choix de passage ni calcul de zone ;
- aucune animation, ni trajectoire, ni simulation parallèle ;
- pas de tours, de récupération des ressources, de visibilité ni d'autres unités ;
- aucun framework, injection de dépendances, bus de messages ni machine à états.

**Héritage de `Directory.Build.props`.** Le client se trouve sous `src/`, donc il hérite des réglages communs, sans modification : `Nullable`, `ImplicitUsings` et `TreatWarningsAsErrors`. Il compile sans avertissement.

**Hors de la chaîne existante.** Le client n'est pas ajouté à `Bastion.slnx`. `dotnet build` et `dotnet format` à la racine ne voient que la simulation et ses tests, et la CI ne le voit pas (T-103 reste à examiner).

**Contrôle fumée (`SmokeTest`).** Lancé par `-- --smoke-test`, il envoie des clics de souris et une touche R à la fenêtre par `Viewport.PushInput`. Ces entrées passent par le même gestionnaire que celles du joueur (`_UnhandledInput`).

Il compare l'état de la scène et le texte de son panneau aux résultats du moteur et aux valeurs du mandat :
1. la version de Godot : 4.7.2 stable ;
2. le scénario : carte de 5 × 5 cases de 1 500 mm, seule la case (3,2) infranchissable, unité `StandardHuman` ;
3. l'état initial (1,4), N, 20 TU, 10 d'énergie ; la zone, qui doit être celle du moteur ; le panneau ;
4. le clic sur (2,4), dont l'état et le message doivent être identiques à ceux d'`ExecuteOrder` depuis l'état initial, soit (2,4), E, 16 TU et 8 d'énergie ;
5. cinq clics sans effet : la case de l'unité, à droite de la carte, la case infranchissable, à gauche de la carte et une case hors zone. Pour chacun, l'état doit rester inchangé et le message attendu doit s'afficher ; deux messages consécutifs diffèrent toujours, ce qui prouve que chaque clic atteint la scène ;
6. un 2e ordre vers (2,2), qui doit être débité du coût du chemin indiqué par le moteur, avec une zone recalculée ;
7. la touche R, qui doit restituer l'état initial ;
8. le panneau, contrôlé après chaque étape.

Il quitte avec le code 0 si tout réussit, 1 si un contrôle échoue et 2 en cas d'exception, y compris pendant l'initialisation de la scène.

**Ce que le contrôle fumée ne couvre pas :**
- **le dessin** (grille, zone, unité) : seules les captures le montrent ;
- **l'absence de règles dans la scène :** une scène qui reproduirait elle-même le chemin du moteur donnerait le même résultat. C'est la lecture du code qui l'établit (RX-09) ;
- **une scène qui ne démarre pas**, par exemple si le projet n'est pas compilé en Debug : le contrôle ne s'exécute pas. La notice impose donc une limite de temps, `timeout`, qui rend alors le code 124 (RX-07).

## 4. Commandes et résultats

Toutes les commandes ont été exécutées dans `/home/user/bastion`, sauf mention contraire. `GODOT` désigne le binaire officiel `Godot_v4.7.2-stable_mono_linux.x86_64`, téléchargé et vérifié au lot 1C, dans le dossier temporaire de la session. Les résultats ci-dessous sont ceux de la version finale, après les corrections de la relecture.

### 4.1 Client Godot

| Étape | Commande | Code | Résultat |
|---|---|---|---|
| Compilation Release (mandat §5 D) | `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --configuration Release` | 0 | 0 avertissement, 0 erreur ; `Bastion.Simulation.dll`, puis `.godot/mono/temp/bin/Release/Bastion.Client.Godot.dll` |
| Compilation Debug, chargée par Godot | `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` | 0 | 0 avertissement, 0 erreur |
| Paquets et cible | `project.assets.json` du client | — | `Bastion.Simulation`, `GodotSharp` 4.7.2, `Godot.SourceGenerators` 4.7.2 ; cible unique `net10.0` |
| Format du client | `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes` | 0 | aucun écart |
| Import | `"$GODOT" --headless --path src/Bastion.Client.Godot --import` | 0 | import terminé |
| **Contrôle fumée, mode headless** | `timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test` | **0** | 21 « SMOKE OK », « SMOKE : RÉUSSITE » (§4.2) |
| **Contrôle fumée sous Xvfb**, avec rendu | `timeout 300 xvfb-run -a -s "-screen 0 1024x768x24" "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test --capture=<dossier>` | **0** | 21 contrôles et 9 captures réussis (30 « SMOKE OK ») (§4.4) |
| Ouverture dans l'éditeur, dans une copie | `timeout 120 xvfb-run -a "$GODOT" --editor --path <copie> --quit-after 600`, deux fois | 0 ; 0 | avec l'ancien `project.godot`, l'en-tête est réécrit (RX-11). Avec le format de l'éditeur, désormais adopté, le fichier n'est plus modifié ; `Main.tscn`, les `.uid` et le `.csproj` restent identiques |

### 4.2 Sortie du contrôle fumée en mode headless

```
Godot Engine v4.7.2.stable.mono.official.ed1daf0bf - https://godotengine.org

SMOKE OK : version de Godot épinglée 4.7.2 stable (4.7.2-stable (official))
SMOKE OK : carte de 5 × 5 cases de 1500 mm, case infranchissable (3,2), unité de 600 × 600 × 1800 mm (StandardHuman attendue)
SMOKE OK : état initial (1,4), N, 20 TU, 10 d'énergie : (1,4), N, 20 TU, 10 d'énergie
SMOKE OK : zone affichée = zone du moteur (22 cases)
SMOKE OK : panneau conforme à l'état initial
SMOKE OK : clic sur (2,4) = résultat d'ExecuteOrder : (2,4), E, 16 TU, 8 d'énergie (Destination (2,4) atteinte.)
SMOKE OK : arrivée en (2,4), E, 16 TU, 8 d'énergie
SMOKE OK : panneau conforme à l'état après le 1er ordre
SMOKE OK : (3,2) et (4,0) sont hors de la zone du moteur
SMOKE OK : clic sur la case de l'unité : état inchangé (Ordre refusé : la destination (2,4) n'appartient pas à la zone atteignable.)
SMOKE OK : clic à droite de la carte : état inchangé (Clic hors de la carte : aucun ordre transmis.)
SMOKE OK : clic sur la case infranchissable (3,2) : état inchangé (Ordre refusé : la destination (3,2) n'appartient pas à la zone atteignable.)
SMOKE OK : clic à gauche de la carte : état inchangé (Clic hors de la carte : aucun ordre transmis.)
SMOKE OK : clic sur la case hors zone (4,0) : état inchangé (Ordre refusé : la destination (4,0) n'appartient pas à la zone atteignable.)
SMOKE OK : panneau conforme à l'état après les clics refusés
SMOKE OK : (2,2) est dans la zone du moteur après le 1er ordre
SMOKE OK : 2e ordre vers (2,2), débité du coût du chemin du moteur : (2,2), N, 8 TU, 4 d'énergie
SMOKE OK : zone recalculée depuis le nouvel état (19 puis 10 cases)
SMOKE OK : panneau conforme à l'état après le 2e ordre
SMOKE OK : touche R : état initial restitué ((1,4), N, 20 TU, 10 d'énergie)
SMOKE OK : panneau conforme à l'état après la touche R
SMOKE : RÉUSSITE
```

### 4.3 Défauts introduits pour éprouver le contrôle fumée

**Méthode.** Le script `mutants.py`, hors dépôt, introduit un défaut à la fois dans une copie jetable, compile en Debug (sauf mention), importe, puis lance `timeout 60 "$GODOT" --headless --path <copie> -- --smoke-test`. Le dépôt n'est jamais modifié.

| Défaut introduit | Code | Contrôles en échec |
|---|---|---|
| aucun (témoin) | 0 | — |
| état initial à 21 TU | 1 | état initial ; arrivée en (2,4) |
| exception pendant l'initialisation de la scène | 2 | « SMOKE EXCEPTION à l'initialisation de la scène » |
| panneau affichant des TU fausses | 1 | 5 contrôles du panneau |
| carte de 6 × 6 | 1 | scénario |
| cases de 1 000 mm | 1 | scénario |
| conversion pixel → case par troncature | 1 | 5, dont le clic à gauche de la carte, qui ordonne un déplacement vers (0,2) |
| clics jamais transmis au moteur | 1 | 9 |
| projet non compilé | **124** | aucun : la scène ne démarre pas ; la limite de temps arrête Godot |
| compilation Release seule | **124** | idem |
| capture demandée en mode headless | 1 | « capture demandée en mode headless : impossible sans affichage » |

Le premier essai du défaut « exception pendant l'initialisation » ne compilait pas : le `throw` inconditionnel rendait du code inaccessible, ce que `TreatWarningsAsErrors` refuse. Il a été réécrit avec une condition non constante.

**Premier contrôle négatif.** Lors d'une première version, le contrôle négatif a révélé que l'état initial était comparé aux constantes de la scène elle-même, ce qui ne prouvait rien. Le contrôle compare désormais aux valeurs écrites dans le mandat.

### 4.4 Rendu sous affichage virtuel

**Rendu.** Sous Xvfb, Godot a signalé l'absence de Vulkan et basculé sur OpenGL 3 (« Mesa llvmpipe », rendu logiciel). L'audio est passé sur le pilote factice. Le contrôle fumée a réussi, avec le code 0, et enregistré 9 captures de 800 × 528 pixels, une après chaque étape.

**Ce que j'ai observé sur les captures :**
- **Initiale :**
  - grille de 5 × 5 ;
  - case (3,2) en gris foncé barré ;
  - 22 cases vertes ; restent grises la case de l'unité et (4,0), trop coûteuse en TU ;
  - unité en (1,4), trait vers le nord ;
  - panneau : (1,4), N, 20 TU, 10 d'énergie, 22 cases.
- **Après le clic sur (2,4) :** unité en (2,4), trait vers l'est, 16 TU, 8 d'énergie, 19 cases, « Destination (2,4) atteinte ».
- **Clics refusés :** l'unité et les ressources sont inchangées. Le panneau affiche le message du moteur, ou « Clic hors de la carte : aucun ordre transmis. ».
- **Après le 2e ordre :** unité en (2,2), trait vers le nord, 8 TU, 4 d'énergie, 10 cases vertes autour de l'unité.
- **Après la touche R :** retour à l'image initiale, avec « Scénario réinitialisé (touche R). ».

Ces captures restent dans le dossier temporaire de la session et ne sont pas ajoutées au dépôt.

**Ce que cela ne prouve pas :** les clics ont été simulés par Godot (`Viewport.PushInput`), et non produits par une souris. Le rendu a été vu sur des captures, et non sur un écran réel. Ce n'est donc pas le contrôle manuel prévu au §5 C du mandat : il reste à faire par un humain.

### 4.5 Non-régression de Bastion

| Commande | Code | Résultat |
|---|---|---|
| `dotnet restore` | 0 | — |
| `dotnet build --configuration Release` | 0 | 0 avertissement, 0 erreur ; ne compile que `Bastion.Simulation` et `Bastion.Simulation.Tests` |
| `dotnet test --configuration Release` | 0 | 46 tests, 46 réussis |
| `dotnet format --verify-no-changes` | 0 | aucun écart (ce format ne couvre pas le client : voir §4.1) |
| `bash scripts/harness/test-hooks.sh` | 0 | « 75 tests, 0 échec(s) » |
| `bash scripts/harness/check-simulation-trace.sh origin/main …` | 0 | « Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise ». Contrôle sans portée ici : il compare des commits, et rien n'est commité ; il ne s'applique de toute façon qu'à `src/Bastion.Simulation/` |

### 4.6 Intégrité de l'architecture (mandat §5 A)

| Contrôle | Commande | Résultat |
|---|---|---|
| Fichiers de la simulation et des tests inchangés | `git status --porcelain -- src/Bastion.Simulation tests Bastion.slnx Directory.Build.props global.json .github scripts .claude CLAUDE.md docs/gameplay docs/decisions docs/references` | 0 ligne |
| `Bastion.Simulation` sans dépendance Godot | `project.assets.json` de `Bastion.Simulation`, après la compilation du client | aucun paquet ; cible `net10.0` ; test fumée `SimulationDoesNotReferenceGodot` réussi (§4.5) |
| Client en `net10.0` avec la référence de projet | `project.assets.json` du client | cible unique `net10.0` ; `Bastion.Simulation` 1.0.0 en référence de projet |
| Archive du mandat | comparaison octet pour octet avec le fichier joint | identique, `7d1579b3…a262` |

## 5. Relecture indépendante ciblée

**Relecteur :** un agent indépendant, distinct de l'implémenteur, sans aucune ligne du lot écrite par lui. Il a travaillé dans des copies, sans rien écrire dans le dépôt.
**Rapport :** `docs/reviews/LOT-1D-PROTOTYPE-GODOT-RELECTURE.md`, copié sans modification (SHA-256 `b376081109f6c051b196aa720d9d9b2a865db11dbaf72691aea571737cf44c30`). Ses scripts, copies et journaux sont restés hors du dépôt.

**Première relecture : « conforme sous réserves », sans constat bloquant.**

| Constat | Gravité | Suite |
|---|---|---|
| RX-01 à RX-06 : périmètre tenu, archive conforme, aucune règle de jeu côté Godot, scénario conforme, dépendances conformes, vrai chemin d'entrée et codes fiables | observation | — |
| RX-07 : le contrôle fumée ne se termine pas si la scène échoue avant de le lancer (exception à l'initialisation, projet non compilé, compilation Release seule) | à corriger | exception à l'initialisation : code 2. Projet non compilé et compilation Release seule : limite de temps imposée par la notice, code 124 ; c'est une limite déclarée |
| RX-08 : en mode headless, `--capture` bloque | observation | échec explicite, code 1 |
| RX-09 : le contrôle ne compare pas l'affichage, contrairement à ce qu'annonçaient la notice, le code et le rapport | à corriger | formulations corrigées ; le texte du panneau est désormais contrôlé ; le dessin et l'absence de règles restent hors de portée du contrôle (§3, §6) |
| RX-10 : mutants non détectés (carte, largeur de case, conversion, débit sur la case de départ, refus non prouvés) | observation | contrôles du scénario, de la case de l'unité, des clics à gauche de la carte et des messages ajoutés ; tous ces défauts sont désormais détectés |
| RX-11 : l'ouverture de l'éditeur réécrit `project.godot` | à corriger | fichier écrit au format de l'éditeur, désormais stable |
| RX-12 : le format et la traçabilité de la CI ne couvrent pas le client | observation | déclaré (§4.5, §6) |
| RX-13 : notice exacte sous Linux ; l'accès à NuGet n'était pas mentionné | observation | ajouté à la notice |
| RX-14 : `.godot/` ignoré, `.uid` stables, encodage correct | observation | — |

**Contrôle des corrections : verdict actualisé « conforme ».** Constats RX-15 à RX-23, tous vérifiés par exécution dans des copies.

**Corrections vérifiées :**
- **RX-15 (RX-07) :** l'exception à l'initialisation donne le code 2. Le projet non compilé et la compilation Release seule donnent 124 avec la commande de la notice ; c'est une limite déclarée.
- **RX-16 (RX-08) :** capture en mode headless, code 1.
- **RX-17 (RX-09) :** les défauts du panneau sont détectés. Deux cas restent non détectés, et sont déclarés : la zone jamais dessinée, et une scène qui rejouerait le chemin du moteur en imitant ses messages.
- **RX-18 (RX-11) :** deux ouvertures de l'éditeur ne modifient plus aucun fichier.
- **RX-19 (RX-10) :** les mutants auparavant manqués sont détectés, ainsi que trois défauts nouveaux.

**Autres constats :**
- **RX-20 :** le rayon de l'unité suit désormais `Model.Body` ; le rendu est inchangé.
- **RX-21 :** aucune règle de jeu ajoutée, simplicité tenue. Remarque : le diagnostic du contrôle de scénario affichait toujours « unité StandardHuman ».
- **RX-22 :** non-régression au vert.
- **RX-23 :** rapport fidèle, avec trois écarts :
  - (a) `project.godot` compte 24 lignes, pas 23 ;
  - (b) la portée du contrôle de traçabilité n'était pas déclarée ;
  - (c) la notice affirmait, sans l'avoir observé, que Godot importe le projet au premier lancement.

**Corrections faites après le contrôle des corrections**, non relues par le relecteur et vérifiées par moi :
- les trois écarts de RX-23 ;
- le diagnostic de RX-21, qui affiche désormais les dimensions de l'unité.

Ensuite, la compilation Debug et Release du client, son format, le contrôle fumée (code 0, 21 contrôles), le contrôle sous Xvfb (code 0, 30 contrôles, 9 captures) et toute la non-régression de Bastion ont été relancés, tous au vert.

## 6. Contrôles non exécutés et réserves

- **Contrôle manuel du rendu et des clics** sur un écran réel, avec une souris : non exécuté, faute d'écran (§4.4).
- **macOS et Windows :** aucun essai. Les instructions macOS de la notice sont marquées non vérifiées, y compris l'usage de `gtimeout`.
- **CI :** elle ne compile, ne formate ni n'exécute le client. Aucune qualification CI du client n'est annoncée. Le contrôle de traçabilité de la CI ne concerne que `src/Bastion.Simulation/` : il ne voit pas le client (RX-12).
- **Export du jeu :** hors périmètre et non testé.
- **Rendu :** sous Xvfb, c'est le moteur de rendu de compatibilité, OpenGL 3, qui a fonctionné ; le rendu Forward+ par Vulkan n'a pas pu être exercé. Le projet garde le moteur de rendu par défaut de Godot.
- **Limites du contrôle fumée :**
  - il ne contrôle pas le dessin ;
  - il ne peut pas prouver l'absence de règles dans la scène ;
  - il ne s'exécute pas si la scène ne démarre pas, d'où la limite de temps de la notice (§3).
- **Coordonnées de saisie :** la conversion pixel → case suppose l'absence de caméra et d'agrandissement de la fenêtre, ce qui est le cas dans ce prototype.
- **Réserves du lot 1 maintenues :** RL-11 (validation de `UnitState` contournable), RL-13 (passage diagonal recalculé à l'exécution) et la limite de couverture de RL-01. Le client ne les touche pas.

## 7. Bilan d'architecture

- La séparation T-001 tient : la simulation ignore Godot, et le client n'en est qu'une vue. Il ne contient aucune règle, ce qu'établit la lecture de son code (§3), confirmée par le relecteur. Le contrôle fumée confirme, lui, que l'état affiché est celui que rend le moteur.
- L'API publique de `Bastion.Simulation` a suffi, sans aucune modification : `TacticalMapBuilder`, `TacticalMap`, `MovementModel`, `CreateState`, `ComputeReachability`, `ExecuteOrder`, `OrderOutcome.Message`, `Reachability`, `UnitState`, `UnitBody`, `GridPosition` et `Direction`.
- **Point à examiner plus tard (T-103) :** le client se compile à part. Il faudra décider s'il rejoint `Bastion.slnx`, le format et la CI, ce qui supposerait d'installer Godot ou de compiler sans lui en CI.

## 8. Points à décider par le propriétaire

1. **Publication :** commit, push de la seule branche `claude/lot-1d-prototype-godot` et PR en brouillon. Elle attend votre autorisation distincte.
2. **Contrôle manuel** sur un poste avec écran, sous Linux ou macOS, en suivant la notice du client.
3. **T-103 :** intégration éventuelle du client à la solution, au format et à la CI, dans un lot ultérieur.

## Annexe A — Empreintes SHA-256

```
2c112d9a28b989f518bdab36c2fd17b17f51916b8f8909f16bdd60d38dbd7fe9  src/Bastion.Client.Godot/project.godot
ce712561aef6aa90102003f7f22060182a4a7c72e875f1d4f1b2c080c4b6bd3c  src/Bastion.Client.Godot/Bastion.Client.Godot.csproj
3b199580c9aac3630e59fdde0f560434f7a3e1136a81c22b0385afc44ca14cb6  src/Bastion.Client.Godot/Main.tscn
62b2cce35de4a372352365e0714b7d85aeed62aec598189d1a549fd1e1675f27  src/Bastion.Client.Godot/PrototypeScene.cs
9d093dcca11cfa5ada45fd7c1c4c2df98982f8e1b9925c49ca3b24af53251f6e  src/Bastion.Client.Godot/PrototypeScene.cs.uid
eedf802f690c187e25b5c35665e5175a811ebd603ab1a4875670bfd4983fa207  src/Bastion.Client.Godot/SmokeTest.cs
42b1dc564515fa6c99ab33afafac8243f43beddbc1bdc27b72bfeec0ae01dfc9  src/Bastion.Client.Godot/SmokeTest.cs.uid
5198592713bf7f824dd9338b024cdee5682b69f2513281a0ec3123db069562b0  src/Bastion.Client.Godot/README.md
7d1579b3ce8b6676b87563c57d8b416ce6de6516e3268fd417a91876c052a262  docs/mandates/BASTION-MANDAT-LOT-1D-v1.0.md
6b4d65b31219d49174761391d39074efba5c422ce66c8f9f1bcbcae87ba7f4dd  docs/mandates/README.md
b376081109f6c051b196aa720d9d9b2a865db11dbaf72691aea571737cf44c30  docs/reviews/LOT-1D-PROTOTYPE-GODOT-RELECTURE.md
```
