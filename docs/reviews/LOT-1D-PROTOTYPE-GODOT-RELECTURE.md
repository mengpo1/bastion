# Relecture indépendante ciblée — Bastion, lot 1D (prototype Godot relié à la simulation)

**Date :** 22 novembre 2026 (19:53 à 20:06 UTC)
**Relecteur :** agent distinct de l'implémenteur ; aucune ligne du lot n'est de lui.
**Objet :** diff non commité de la branche `claude/lot-1d-prototype-godot`, base `origin/main` = `541018c8fb5f9b7b211c2128d68dea7eeeeb7670`.
**Référentiel :** `docs/mandates/BASTION-MANDAT-LOT-1D-v1.0.md`, `CLAUDE.md`.
**Méthode :** lecture du diff, puis réexécution de tout ce qui est cité. Les compilations, imports, exécutions Godot et mutants ont eu lieu dans des copies, sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/lot1d/relecture/` (`copie/` : clone + fichiers du lot ; `mut/` : mutants ; `frais/` : copie sans `.godot`). Rien n'a été écrit dans `/home/user/bastion` : à 20:05 UTC, `find . -newermt "2026-11-22 19:53:00"` n'y renvoie aucun fichier, et les empreintes ci-dessous sont celles du début de la relecture.

**États employés :** *vérifié* (commande jouée, sortie observée) ; *inspecté seulement* (lecture) ; *non vérifié*.

## Instantané relu (SHA-256)

```
ce712561aef6aa90102003f7f22060182a4a7c72e875f1d4f1b2c080c4b6bd3c  src/Bastion.Client.Godot/Bastion.Client.Godot.csproj
3b199580c9aac3630e59fdde0f560434f7a3e1136a81c22b0385afc44ca14cb6  src/Bastion.Client.Godot/Main.tscn
94f67ccff175870dd26f1c04bf34515ee4c7e2ce1655b98a4a7399a1e0c1ef2b  src/Bastion.Client.Godot/PrototypeScene.cs
9d093dcca11cfa5ada45fd7c1c4c2df98982f8e1b9925c49ca3b24af53251f6e  src/Bastion.Client.Godot/PrototypeScene.cs.uid
b945439c870e819f3f0f94fddf70fc6afd337ec6a17c47f372f1b875215cb690  src/Bastion.Client.Godot/README.md
6261cb245295d09f813e9fd045e36a1dbbed3a4723814f67fc0354cbabfda89e  src/Bastion.Client.Godot/SmokeTest.cs
42b1dc564515fa6c99ab33afafac8243f43beddbc1bdc27b72bfeec0ae01dfc9  src/Bastion.Client.Godot/SmokeTest.cs.uid
67e0b1c6cfd5dd66ac670ed246fa76439d6de0a9b57b987dd74032b0f1445676  src/Bastion.Client.Godot/project.godot
6b4d65b31219d49174761391d39074efba5c422ce66c8f9f1bcbcae87ba7f4dd  docs/mandates/README.md
7d1579b3ce8b6676b87563c57d8b416ce6de6516e3268fd417a91876c052a262  docs/mandates/BASTION-MANDAT-LOT-1D-v1.0.md
da58f33a1d0a8824e9cca073906e9b16015856af70cf8d477aa334b216b805b9  docs/reviews/LOT-1D-PROTOTYPE-GODOT.md   (apparu à 19:52:58 UTC, en cours de rédaction)
```

Toute modification ultérieure de ces fichiers sort du périmètre de cette relecture.

---

## Constats

### RX-01 — Périmètre respecté ; le client n'entre pas dans la chaîne existante
**Gravité :** observation (conforme). **État :** vérifié.

- `git status --porcelain -uall` (dépôt réel) : seuls `docs/mandates/README.md` (modifié, +1 ligne), l'archive du mandat, le rapport du lot et les 8 fichiers de `src/Bastion.Client.Godot/`.
- `git status --porcelain -uall -- src/Bastion.Simulation tests Bastion.slnx Directory.Build.props global.json .github scripts .claude CLAUDE.md docs/gameplay docs/decisions docs/references .gitignore .gitattributes README.md | wc -l` → `0`.
- Copie, `dotnet restore` → code 0, deux projets restaurés seulement (`Bastion.Simulation`, `Bastion.Simulation.Tests`) ; `dotnet build --no-restore --configuration Release` → code 0, « 0 Warning(s) 0 Error(s) », deux assemblages produits seulement.
- Non-régression, copie : `dotnet test --no-build --configuration Release` → code 0, « Passed: 46, Total: 46 » ; `dotnet format --verify-no-changes --no-restore` → code 0 ; `bash scripts/harness/test-hooks.sh` → code 0, « 75 tests, 0 échec(s) ».
- Ces chiffres (46, 75) confirment ceux du rapport du lot.

### RX-02 — Archive et index du mandat conformes au protocole
**Gravité :** observation. **État :** vérifié (identité) ; non vérifié (horodatage de l'autorisation).

- `cmp docs/mandates/BASTION-MANDAT-LOT-1D-v1.0.md <fichier joint>` → code 0 ; les deux SHA-256 valent `7d1579b3ce8b6676b87563c57d8b416ce6de6516e3268fd417a91876c052a262`, la valeur inscrite dans `docs/mandates/README.md:28`.
- Provenance « original `.md` » cohérente avec la définition du protocole (`docs/mandates/README.md:7`).
- L'autorisation « 22 novembre 2026, 19:45:23 UTC » citée à la ligne 28 relève de la conversation : non vérifiable par moi.
- La ligne 28 renvoie à `docs/reviews/LOT-1D-PROTOTYPE-GODOT.md`, qui existe désormais mais contient encore les espaces réservés `RELECTURE` (l. 177) et `EMPREINTES` (l. 204).

### RX-03 — Aucune règle de jeu recalculée côté Godot
**Gravité :** observation (conforme), avec une remarque mineure. **État :** vérifié (compilation, mutants) et inspecté.

- `PrototypeScene.cs` n'appelle que des API publiques du moteur : `TacticalMapBuilder`, `MovementModel`, `MovementRules.Initial`, `UnitBody.StandardHuman`, `CreateState`, `ComputeReachability`, `ExecuteOrder`, `OrderOutcome.Message`, `Reachability.Contains/Zone`, `TacticalMap.Contains/IsBlocked`, `Direction.Offset()`. Aucun `InternalsVisibleTo` dans `src/` ni `tests/` (`grep` → code 1) : la compilation prouve que seules des API publiques sont employées.
- `grep -nE "Tu\s*-|Energy\s*-|\.Steps|PlannedPath|Cost|Collision|Passage|IsDiagonal|Rules\." PrototypeScene.cs` → une seule ligne, la construction du modèle (l. 50). Ni chemin, ni coût, ni collision, ni calcul de zone.
- Le pré-filtre `_map.Contains(destination)` (`PrototypeScene.cs:115`) n'est pas une règle : il appelle le moteur et ne sert qu'au message « clic hors de la carte » ; sans lui, `ExecuteOrder` refuserait aussi (`TryGetPath` → faux).
- Remarque mineure (inspecté) : le rayon du disque (`PrototypeScene.cs:95`) lit `UnitBody.StandardHuman` et la constante `CellWidthMm` plutôt que `Model.Body` et `_map.CellWidthMm`. Pour l'affichage seulement, c'est une seconde source pour la même donnée ; sans effet aujourd'hui.

### RX-04 — Scénario du mandat §4 conforme
**Gravité :** observation (conforme). **État :** vérifié.

- Contrôle fumée nominal, copie : `"$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test` → **code 0**, 13 « SMOKE OK », « SMOKE : RÉUSSITE ». Sortie : état initial `(1,4), N, 20 TU, 10 d'énergie` ; zone de 22 cases ; clic (2,4) → `(2,4), E, 16 TU, 8 d'énergie` ; refus pour (3,2), (4,0) et hors carte ; 2e ordre → `(2,2), N, 8 TU, 4 d'énergie` ; zones 19 puis 10 ; touche R → état initial. Chiffres identiques à ceux du rapport du lot.
- Comportements du §4.2 que le contrôle livré ne couvre pas, vérifiés par un contrôle augmenté (T01, dans `mut/`, puis restauré) → code 0 :
  - clic sur la case de l'unité → « Ordre refusé : la destination (2,4) n'appartient pas à la zone atteignable. », état inchangé ;
  - clics en (10,300) et (300,10), à gauche et au-dessus de la grille → « Clic hors de la carte », état inchangé ; `FloorToInt` traite bien les coordonnées négatives.
- Rendu, sous Xvfb : `xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test --capture=<dossier>` → code 0, 20 « SMOKE OK » (13 + 7 captures). J'ai examiné moi-même les captures 01, 02, 03, 06 et 07 :
  - grille 5 × 5 ;
  - (3,2) gris foncé barré ;
  - zone en vert ;
  - disque bleu et trait jaune vers N, puis E, puis N ;
  - panneau avec position, orientation, TU, énergie, nombre de cases et dernier résultat ;
  - aucune animation.
  Rendu logiciel OpenGL 3 (llvmpipe), pas d'écran réel.

### RX-05 — Dépendances conformes ; réglages communs hérités
**Gravité :** observation (conforme). **État :** vérifié.

- `src/Bastion.Simulation/obj/project.assets.json` : cible `net10.0`, aucune bibliothèque ni référence de projet. Le seul « godot » de `src/Bastion.Simulation` est le commentaire du `.csproj` qui l'interdit.
- `.godot/mono/temp/obj/project.assets.json` du client : cible unique `net10.0` ; bibliothèques `Godot.SourceGenerators/4.7.2`, `GodotSharp/4.7.2`, `GodotSharpEditor/4.7.2`, `Bastion.Simulation/1.0.0` ; référence de projet vers `src/Bastion.Simulation/Bastion.Simulation.csproj`.
- `dotnet msbuild … -getProperty` sur le client : `TargetFramework=net10.0`, `TreatWarningsAsErrors=true`, `Nullable=enable`, `ImplicitUsings=enable`, `DirectoryBuildPropsPath=<racine>/Directory.Build.props`. Preuve d'effet : un mutant contenant du code inatteignable échoue sur `error CS0162`, un autre sur `error CS8600` et `CS8604`.
- Compilations du client, copie : `--configuration Release` → code 0, 0 avertissement ; Debug → code 0, 0 avertissement.
- Épinglage :
  - `Sdk="Godot.NET.Sdk/4.7.2"` dans le `.csproj` ;
  - contrôle de version à l'exécution (`SmokeTest.cs:53-55`), observé « 4.7.2-stable (official) » ;
  - `project.godot` ne porte que la fonctionnalité « 4.7 ».

### RX-06 — Le contrôle fumée passe par le vrai chemin d'entrée ; codes 0, 1 et 2 fiables quand il s'exécute
**Gravité :** observation (conforme). **État :** vérifié par mutants.

Chaque mutant a été appliqué seul dans `mut/`, compilé en Debug, exécuté avec `timeout 60`, puis restauré. La restauration a été contrôlée par comparaison d'empreinte avec l'original ; empreintes finales de `PrototypeScene.cs` et `SmokeTest.cs` identiques à l'instantané.

| Mutant | Code | Détecté |
|---|---|---|
| M01 la scène déplace l'unité elle-même | 1 (7 échecs) | oui |
| M02 zone jamais recalculée | 1 (2) | oui |
| M03 touche R inerte | 1 (1) | oui |
| M04 (3,2) non bloquée | 1 (5) | oui |
| M09 exception dans `_UnhandledInput` | 1 (4) | oui : les clics passent bien par le gestionnaire du joueur |
| M10 ordre refusé mais unité déplacée | 1 (3) | oui |
| M11 orientation initiale E | 1 (1) | oui |
| M17 21 TU (contrôle négatif cité par le rapport du lot) | 1 (2 : état initial, arrivée) | oui, chiffre du rapport confirmé |
| T02 exception levée dans le contrôle | **2** (« SMOKE EXCEPTION ») | oui |

Les attentes ne sont pas tautologiques :
- l'état initial et l'arrivée sont comparés à des littéraux du mandat ;
- le 1er ordre est comparé à un appel direct d'`ExecuteOrder` hors du chemin du clic ;
- les prémisses des refus sont établies (« (3,2) et (4,0) sont hors de la zone du moteur »).

Asynchronisme : `PushInput` est traité de façon synchrone, et le contrôle attend deux images avant chaque vérification. Aucun faux positif observé.

### RX-07 — Le contrôle fumée ne se termine pas si la scène échoue avant de le lancer
**Gravité :** **à corriger** (écart partiel au §5 C : « se termine explicitement avec … un code non nul en cas d'échec »). **État :** vérifié.

**Emplacement :**
- le contrôle n'est lancé qu'à la fin de `PrototypeScene._Ready` (`PrototypeScene.cs:46-56`) ;
- s'il ne démarre pas, rien n'appelle `Quit` et Godot tourne indéfiniment.

**Preuves** (toutes avec `timeout 60`) :

| Cas | Code | Sortie |
|---|---|---|
| M08 : `GetNode<Label>("HUD")` lève dans `_Ready` | **124** (tué par `timeout`) | « ERROR: Node not found: "HUD" » puis `NullReferenceException` |
| H1 : copie fraîche, projet non compilé | **124** | « ERROR: Cannot instantiate C# script because the associated class could not be found. Script: 'res://PrototypeScene.cs' » |
| H2 : seule la compilation Release (la première commande de la notice, `README.md:34`) | **124** | même erreur. Cela confirme au passage que Godot charge la compilation Debug, comme l'indique `README.md:37`. |

**Conséquences :**
- Les défaillances d'intégration les plus probables (assemblage absent ou non chargeable, scène cassée) ne rendent pas un code non nul : elles bloquent la commande documentée `"$GODOT" --headless … -- --smoke-test; echo $?`.
- Une future CI (T-103) resterait suspendue jusqu'à son propre délai.
- La phrase « puis quitte avec le code 0 si tout réussit, et un code non nul sinon » (`README.md:79`) est fausse dans ces trois cas.
- Aucun faux succès n'en résulte : ni code 0, ni « RÉUSSITE ».

### RX-08 — `--capture` en mode headless bloque au lieu d'échouer
**Gravité :** observation. **État :** vérifié.

- H3 : `"$GODOT" --headless … -- --smoke-test --capture=<dossier>` → **124**. Seule la vérification de version s'affiche, puis l'attente de `FramePostDraw` (`SmokeTest.cs:45`) ne se termine jamais.
- La notice et le commentaire (`SmokeTest.cs:11-12`) disent que la capture demande un affichage : la limite est déclarée, mais elle se manifeste par un blocage silencieux.
- À l'inverse, un dossier de capture inexistant, sous Xvfb (H5), est bien signalé : code 1 et « SMOKE ÉCHEC : capture … » à chaque étape.

### RX-09 — Formulations qui surévaluent ce que prouve le contrôle fumée
**Gravité :** **à corriger** (exactitude des affirmations). **État :** vérifié par mutants.

**Emplacements :**
- `SmokeTest.cs:9` et `README.md:79` : « compare l'état affiché au résultat du moteur » ;
- rapport du lot, `docs/reviews/LOT-1D-PROTOTYPE-GODOT.md:191` : « Il ne contient aucune règle, comme le montrent le code (§3) et le contrôle fumée, qui compare l'affichage aux résultats du moteur ».

En réalité, le contrôle lit les propriétés `State`, `Reachability` et `LastResult`, ni le panneau ni le dessin. Mutants passés **avec le code 0** :

| Mutant | Code |
|---|---|
| M12 : le panneau affiche toujours `StartTu` (20) au lieu des TU restantes | 0 |
| M13 : la zone n'est jamais dessinée en vert | 0 |
| M15 : la scène n'appelle plus `ExecuteOrder` ; elle applique elle-même le chemin de `Reachability.TryGetPath` (position, dernière direction, débit `path.Tu` / `path.Energy`) et affiche « refus maison » | 0 |

**Conséquences :**
- L'affichage n'est garanti que par l'examen humain des captures (RX-04).
- L'usage d'`ExecuteOrder` et l'absence de règles côté client ne sont établis que par la lecture du code (RX-03), pas par le contrôle fumée. Dans ce scénario, chaque chemin s'exécute en entier : appliquer le chemin du moteur ou appeler `ExecuteOrder` donne le même résultat.

### RX-10 — Couverture du contrôle fumée : propriétés du scénario non établies
**Gravité :** observation (le §5 B ne les exige pas toutes). **État :** vérifié par mutants.

Mutants non détectés, **code 0** :

| Mutant | Raison |
|---|---|
| M05 : carte 6 × 6 | 31 cases ; toutes les comparaisons passent par `scene.Model` |
| M06 : cases de 1 000 mm | — |
| M07 : conversion pixel → case par troncature | le seul clic hors carte est en (700,300), à droite de la grille |
| M14 : un clic sur la case de l'unité débite 1 TU | le clic sur la case de départ, exigé au §4.2, n'est pas testé ; le comportement réel est conforme (RX-04, T01) |

Les contrôles de refus (`SmokeTest.cs:78-86`) passent aussi quand le clic n'atteint pas la scène : sous M09, les trois refus sont « OK », avec « Scénario initialisé. » comme dernier résultat. Ils ne vérifient pas que le clic a été traité. Le contrôle échoue néanmoins, grâce aux autres vérifications.

### RX-11 — Ouvrir l'éditeur, comme l'indique la notice, réécrit `project.godot`
**Gravité :** **à corriger**. **État :** vérifié.

**Emplacement :** `project.godot:1-2` (commentaires d'épinglage) ; commande `README.md:64`.

**Preuve :**
- copie `frais/` : `timeout 90 xvfb-run -a "$GODOT" --editor --path src/Bastion.Client.Godot --quit-after 600` → code 0 ;
- puis `diff -u` avec l'original : les deux lignes « ; Prototype technique du lot 1D … » et « ; Version de Godot épinglée : 4.7.2 stable .NET (T-002 …) » sont remplacées par l'en-tête standard de Godot (« ; Engine configuration file. … ») ;
- `Main.tscn`, les `.uid` et le `.csproj` restent inchangés ;
- l'import headless et l'exécution (headless et Xvfb) ne modifient aucun fichier : vérifié par `cmp`.

**Conséquence :** la première ouverture de l'éditeur salit l'arbre de travail sur un fichier suivi, et efface silencieusement la mention d'épinglage. L'épinglage effectif, `Sdk="Godot.NET.Sdk/4.7.2"`, n'est pas touché.

### RX-12 — Les contrôles automatiques existants ne voient pas le client
**Gravité :** observation (constat de structure ; le harnais et la CI sont hors périmètre du lot). **État :** vérifié.

- **Format :** dans `mut/`, défaut d'indentation introduit dans `PrototypeScene.cs:13`. `dotnet format --verify-no-changes` à la racine (la commande de la CI) → **code 0**. La commande ciblée `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes` → code 2 (`error WHITESPACE`). Fichier restauré, empreinte `94f67ccf…` contrôlée.
- **Traçabilité :** dans le clone de relecture (branche locale jetable `essai-trace`), commit des fichiers du client. `bash scripts/harness/check-simulation-trace.sh 541018c… <description vide>` → code 0, « Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise ».
- **Conséquence :** une règle de jeu ajoutée plus tard dans `src/Bastion.Client.Godot/` n'exigerait aucune déclaration de traçabilité. Un écart de format du client ne serait pas signalé par la CI.
- La notice (`README.md:97`) et le rapport ne déclarent que « la CI ne compile ni n'exécute ce client ». Format et traçabilité ne sont pas mentionnés. À rattacher à T-103.

### RX-13 — Notice : commandes exactes, avec des imprécisions mineures
**Gravité :** observation. **État :** vérifié pour Linux ; non vérifié pour macOS.

**Commandes Linux réexécutées :**

| Commande | Résultat |
|---|---|
| import headless | code 0 |
| contrôle fumée headless | code 0 |
| Xvfb avec `--capture` | code 0 |
| `--editor` | code 0, avec l'effet de RX-11 |
| compilations Release et Debug | code 0 |

**Imprécisions :**
- L'import préalable n'est pas nécessaire au contrôle fumée : copie sans `.godot`, compilation Debug seule, puis contrôle → code 0, 13 OK (H4). L'étape est sans danger.
- Les prérequis ne mentionnent pas l'accès à NuGet : `Godot.NET.Sdk`, `GodotSharp`, `GodotSharpEditor` et `Godot.SourceGenerators` 4.7.2 viennent de `nuget.org`, la seule source configurée. Ce point est inspecté seulement.
- Construire en Release seule mène au blocage de RX-07 (H2) ; la notice dit bien que Godot charge la compilation Debug.
- macOS est marqué « non vérifié » (`README.md:67`). Le chemin `/Applications/Godot_mono.app/Contents/MacOS/Godot` est **non vérifié**.
- Les limites sont déclarées (`README.md:94-98`) : plateformes, CI, export.

### RX-14 — Fichiers générés et sorties de compilation
**Gravité :** observation. **État :** vérifié.

- `.godot/` est ignoré par le `.gitignore` de la base depuis `7532b04` (ligne 12). `git check-ignore -v` couvre `src/Bastion.Client.Godot/.godot/`, `bin/` et `obj/`.
- Le SDK Godot place les sorties dans `.godot/mono/temp/{bin,obj}` (`BaseOutputPath` et `BaseIntermediateOutputPath` mesurés).
- Dans le dépôt réel, `src/Bastion.Client.Godot/.godot/` existe déjà : compilations Debug et Release et cache d'éditeur, horodatés de 19:48 à 19:51 UTC, donc avant cette relecture. L'implémenteur a compilé et importé dans `/home/user/bastion`. Rien n'est suivi par Git ; aucun effet sur le diff.
- Les deux `.uid` sont à conserver, comme il est d'usage depuis Godot 4.4 ; ni l'import ni l'éditeur ne les modifient.
- Encodage : pas de BOM, LF, pas d'espace en fin de ligne, saut de ligne final (`od`, `grep`) ; `git diff --check` → code 0.

---

## Verdict

**CONFORME, sous réserves.** Aucun constat bloquant.

**Établi par exécution :**
- le périmètre est tenu et le client reste hors de la chaîne existante ;
- la scène ne recalcule aucune règle ;
- le scénario du §4 est exact ;
- les dépendances sont conformes ;
- le contrôle fumée emprunte le vrai chemin d'entrée et détecte les défauts de comportement de la scène, avec des codes 0, 1 et 2 fiables dès qu'il s'exécute.

**À corriger, de préférence avant le commit :**
- **RX-07** : le contrôle ne se termine pas quand la scène ou l'assemblage C# ne se charge pas. C'est un écart partiel au §5 C, et la notice affirme le contraire.
- **RX-09** : la notice, le commentaire et le rapport du lot affirment que le contrôle compare l'affichage et montre l'absence de règles. Il ne fait ni l'un ni l'autre.
- **RX-11** : ouvrir l'éditeur réécrit `project.godot` et efface la mention d'épinglage.

**Observations :** RX-01 à RX-06, RX-08, RX-10, RX-12 à RX-14.

Cette relecture ne valide ni commit ni publication.

---

## Contrôle des corrections

**Date :** 22 novembre 2026, de 20:17 à 20:30 UTC.
**Objet :** les seules corrections apportées après la relecture ci-dessus. Ce n'est pas une nouvelle revue générale.
**Copies de travail :** `corr/` (clone et fichiers du lot corrigés), `mut2/` (mutants), `frais2/` à `frais5/` (copies sans `.godot`), toutes sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/lot1d/relecture/`. Rien n'a été écrit dans `/home/user/bastion`.

**Fichiers contrôlés :** leurs empreintes sont identiques, dans le dépôt réel, à celles de `…/scratchpad/lot1d/empreintes-soumises.txt`. `docs/mandates/README.md` (`6b4d65b3…`) et l'archive du mandat (`7d1579b3…`) n'ont pas changé.

```
2c112d9a28b989f518bdab36c2fd17b17f51916b8f8909f16bdd60d38dbd7fe9  src/Bastion.Client.Godot/project.godot
62b2cce35de4a372352365e0714b7d85aeed62aec598189d1a549fd1e1675f27  src/Bastion.Client.Godot/PrototypeScene.cs
72e4607b8e0361ed5d446600de624abe9e0db3b0187174ccac81a41bb2f2abc5  src/Bastion.Client.Godot/SmokeTest.cs
9ad75aa8215d953d99dc12d25fd4657dde415eb8970175b474ad9e9cec42de8d  src/Bastion.Client.Godot/README.md
c2a188e37ebebd6407aeb8b730d539ae143395ae5097cc99d1805165ac3d16ef  docs/reviews/LOT-1D-PROTOTYPE-GODOT.md   (= …/scratchpad/lot1d/rapport-soumis.md)
```

Le `.csproj`, `Main.tscn` et les deux `.uid` sont inchangés (mêmes empreintes que dans l'instantané initial).

**Méthode des mutants :** un mutant à la fois dans `mut2/`, compilation Debug, puis `timeout 60 "$GODOT" --headless --path <copie> -- --smoke-test`, puis restauration. Chaque restauration est contrôlée par empreinte. Empreintes finales de `mut2/` : `62b2cce3…` et `72e4607b…`, identiques aux fichiers soumis.

### RX-15 — RX-07 traité ; la limite résiduelle est déclarée et bornée
**Gravité :** observation (constat levé). **État :** vérifié.

- **Cas M08 réglé :** mutant `GetNode<Label>("HUD")`, rejoué à l'identique → **code 2**, « SMOKE EXCEPTION à l'initialisation de la scène : System.NullReferenceException … ». Avant la correction : 124.
- **Hors contrôle fumée, comportement inchangé :** le même mutant lancé sans `--smoke-test` → 124 sous `timeout 20`, aucune ligne SMOKE, « ERROR: Node not found: "HUD" » puis `NullReferenceException`. Le filtre `when (smokeTest)` (`PrototypeScene.cs:59`) ne change donc rien hors contrôle.
- **Classe C# impossible à charger, borné par la limite de temps :** `_Ready` ne s'exécute pas, donc le contrôle ne peut pas quitter de lui-même.
  - H1, copie sans compilation, avec la commande exacte de la notice (`timeout 300 "$GODOT" --headless … -- --smoke-test`) → **124** au bout de 300 s (20:21:08 → 20:26:08 UTC), aucune ligne SMOKE, « Cannot instantiate C# script … », aucun processus Godot restant (`pgrep` → 0).
  - H2, compilation Release seule, `timeout 60` → **124**, « Cannot instantiate C# script … ».
- **Limite déclarée :**
  - table des codes 0, 1, 2 et 124 (`README.md:91-95`) ;
  - en-tête de `SmokeTest.cs:13-15` ;
  - rapport du lot, §3 l. 102 et §6 l. 226.
- **Conclusion :** le §5 C est tenu par la commande documentée (code non nul dans tous les cas mesurés). La terminaison de H1 et H2 repose sur `timeout`, pas sur le contrôle lui-même. C'est déclaré.

### RX-16 — RX-08 traité
**Gravité :** observation (constat levé). **État :** vérifié.

- H3, mode headless avec `--capture=<dossier>`, `timeout 60` → **code 1**, « SMOKE ÉCHEC : capture demandée en mode headless : impossible sans affichage », « SMOKE : ÉCHEC (1 contrôle(s)) ». Les 21 autres contrôles passent et aucune image n'est écrite. Avant la correction : 124.
- L'échec n'est pas immédiat : le contrôle se poursuit puis rend 1. La notice (`README.md:99`, « comptée comme un échec ») et `SmokeTest.cs:17` le décrivent exactement.

### RX-17 — RX-09 traité ; formulations exactes et panneau contrôlé
**Gravité :** observation (constat levé). **État :** vérifié.

- **Formulations corrigées :** `SmokeTest.cs:9-12`, `README.md:82` et le rapport du lot (§3 l. 87 et 99-101, §7 l. 232) ne disent plus que le contrôle vérifie le dessin ni qu'il prouve l'absence de règles.
- **Panneau désormais contrôlé** (`SmokeTest.cs:65-74`, après chaque étape) :

| Mutant | Code | Échecs |
|---|---|---|
| M12, panneau à `StartTu` | **1** | 3, après les étapes où les TU diffèrent de 20 |
| M21, énergie + 1 | **1** | 5 |
| M22, dernier résultat absent | **1** | 5 |
| M24, TU + 1 (mutant du rapport du lot) | **1** | 5 |

- **Messages désormais contrôlés :** M15, chemin appliqué par la scène avec messages « maison » → **1** (4 échecs).
- **Résidus non détectés, tous deux déclarés** (`SmokeTest.cs:10-12`, `README.md:82`, rapport §3 l. 100-101, §6 l. 224-225) :
  - M13, zone jamais dessinée → **0** ;
  - **M23**, nouveau : la scène applique elle-même le chemin de `Reachability.TryGetPath` et imite les messages du moteur → **0**.

### RX-18 — RX-11 traité
**Gravité :** observation (constat levé). **État :** vérifié.

- `project.godot` est identique, octet pour octet, au fichier que l'éditeur avait écrit lors de mon essai de RX-11 (`cmp` → 0 ; `2c112d9a…`).
- Copie `frais4/` : deux ouvertures successives par `timeout 120 xvfb-run -a "$GODOT" --editor --path src/Bastion.Client.Godot --quit-after 600` → codes 0 et 0. Les empreintes de tous les fichiers du dossier sont inchangées après chaque passage, et aucun fichier n'est créé.
- L'import et les exécutions, en mode headless et sous Xvfb, ne modifient aucun fichier de `corr/` (`cmp` avec le dépôt réel).
- La mention d'épinglage se trouve désormais dans la notice (`README.md:27`) et dans le commentaire du `.csproj`, inchangé ; l'épinglage effectif `Sdk="Godot.NET.Sdk/4.7.2"` est intact.

### RX-19 — RX-10 : mutants auparavant non détectés
**Gravité :** observation. **État :** vérifié.

| Mutant | Avant | Après |
|---|---|---|
| M05, carte 6 × 6 | 0 | **1** (contrôle du scénario) |
| M06, cases de 1 000 mm | 0 | **1** (scénario) |
| M07, troncature | 0 | **1** (5 échecs ; « clic à gauche de la carte : … Destination (0,2) atteinte. ») |
| M14, débit sur la case de départ | 0 | **1** (6 échecs) |

Nouveaux mutants contre les nouveaux contrôles :

| Mutant | Code |
|---|---|
| M18, pré-filtre de zone muet dans la scène | **1** (3 échecs ; l'alternance des messages le révèle) |
| M19, obstacle supplémentaire en (0,0) | **1** |
| M20, emprise 600 × 600 × 1 700 | **1** |
| M09, exception dans le gestionnaire de clic | **1** (9 échecs, dont les 5 clics refusés) |

Les contrôles de refus prouvent désormais que chaque clic arrive à la scène.

Mutants d'origine toujours détectés :

| Mutant | Code |
|---|---|
| M01 | 1 (7) |
| M02 | 1 (2) |
| M03 | 1 (2) |
| M04 | 1 (6) |
| M10 | 1 (3) |
| M11 | 1 (1) |
| M17 | 1 (2) |

Seuls M13 et M23 restent non détectés (RX-17), et ils sont déclarés.

### RX-20 — Remarque de RX-03 traitée sans effet visible
**Gravité :** observation. **État :** vérifié.

- Le rayon utilise désormais `Model.Body` et `_map.CellWidthMm` (`PrototypeScene.cs:109`).
- Capture initiale sous Xvfb après correction : identique octet pour octet à celle d'avant correction (`cmp` de `captures/01-initial.png` et `captures-corr/01-initial.png` → 0).
- Rendu examiné sur `06-clic-hors-carte-gauche.png` et `08-ordre-2-2.png` : conforme.

### RX-21 — Aucune règle de jeu ajoutée ; périmètre et simplicité tenus
**Gravité :** observation, avec une remarque mineure. **État :** vérifié et inspecté.

- **Diff de la scène limité à trois points :**
  - l'accesseur en lecture `HudText` ;
  - le `try/catch` filtré de `_Ready` ;
  - le calcul du rayon.
- **Recherche de logique de jeu :** `grep -nE "Tu\s*-|Energy\s*-|\.Steps|PlannedPath|Cost|Collision|Passage|IsDiagonal|Rules\." PrototypeScene.cs` → une seule ligne, la construction du modèle (l. 56).
- **Simplicité :** aucun nouveau type, aucun framework, ni événement ni délégué. `SmokeTest.cs` passe de 145 à 204 lignes, avec des fonctions locales et un tableau de tuples. Le parcours de la carte qui collecte les cases bloquées vit dans le contrôle, pas dans la scène.
- **Remarque mineure :** le libellé du contrôle de scénario (`SmokeTest.cs:98`) affiche toujours « unité StandardHuman », même en échec. Sous M20, la ligne s'écrit « SMOKE ÉCHEC : carte de 5 × 5 cases de 1500 mm, case infranchissable (3,2), unité StandardHuman ». Le diagnostic est trompeur, mais le code de sortie est juste.

### RX-22 — Non-régression
**Gravité :** observation (conforme). **État :** vérifié (copie `corr/`).

| Commande | Code | Résultat |
|---|---|---|
| `dotnet restore` | 0 | 2 projets restaurés |
| `dotnet build --no-restore --configuration Release` | 0 | 0 avertissement |
| `dotnet test --no-build --configuration Release` | 0 | 46/46 |
| `dotnet format --verify-no-changes --no-restore` | 0 | — |
| `bash scripts/harness/test-hooks.sh` | 0 | « 75 tests, 0 échec(s) » |
| client, Release puis Debug | 0, 0 | 0 avertissement |
| `dotnet format` du client | 0 | — |
| chemins protégés | — | 0 ligne |
| contrôle fumée headless | **0** | 21 « SMOKE OK » |
| contrôle fumée sous Xvfb avec `--capture` | **0** | 30 « SMOKE OK », 9 captures |
| contrôle fumée sans import préalable (`frais5/`) | 0 | 21 OK |

Encodage : pas de BOM, LF, aucun espace final ; `git diff --check` → 0.

### RX-23 — Fidélité du rapport réécrit (`c2a188e3…`)
**Gravité :** **à corriger**, pour le seul point (a) ; observations pour les autres. **État :** vérifié, sauf mention contraire.

**Chiffres confirmés par mes propres exécutions :**
- 21 contrôles (§1 l. 24, §4.1, §4.2) ;
- 30 « SMOKE OK » et 9 captures (§1 l. 26, §4.1 l. 118, §4.4) ;
- chaque ligne du tableau §4.3, rejouée par un mutant identique ou équivalent : témoin 0 ; 21 TU → 1 (2) ; exception à l'initialisation → 2 ; TU + 1 → 1 (5) ; 6 × 6 → 1 ; 1 000 mm → 1 ; troncature → 1 (5, avec (0,2)) ; clics non transmis → 1 (9) ; non compilé → 124 ; Release seule → 124 ; capture headless → 1 ;
- ouverture de l'éditeur (§4.1 l. 119) ;
- non-régression (§4.5) ;
- nombre de lignes du §2 : 12, 13, 165, 204, 109 et 102.

L'anecdote du §4.3 l. 168 (compilation refusée par `TreatWarningsAsErrors`) est corroborée par le journal de l'implémenteur (`mutants.log` : « exception à l'initialisation : COMPILATION ÉCHOUÉE (code 1) »). Inspecté seulement.

Aucune réserve n'est annoncée levée sans preuve. Le §1 l. 29 dit les trois points « traités » ; pour RX-07, la limite résiduelle est déclarée aux §3 et §6 (voir RX-15).

**Écarts :**
- **(a)** §2 l. 41 : `project.godot` compte **24** lignes (`wc -l`), pas 23. L'orchestrateur l'a déjà annoncé.
- **(b)** §4.5 l. 201 : le contrôle de traçabilité, lancé contre `origin/main`, ne pouvait rien trouver. Il compare des commits, rien n'est commité, et `HEAD` = `origin/main`. Son résultat ne prouve rien sur ce diff. Le §6 l. 220 ne mentionne pas non plus que ce contrôle ignore `src/Bastion.Client.Godot/` (RX-12, observation maintenue).
- **(c)** Notice, `README.md:52` : « Godot le fait aussi au premier lancement » n'est pas observé. Dans `frais5/`, après compilation Debug et contrôle fumée sans import (code 0, 21 OK), `.godot/` ne contient que `mono/` : ni `imported/` ni `uid_cache.bin`. Le caractère facultatif de l'import est confirmé, mais pas la parenthèse.

### Verdict actualisé

**CONFORME.** Aucun constat bloquant.

- Les trois constats à corriger de la relecture sont traités et vérifiés par exécution :
  - **RX-07** pour le cas d'initialisation, avec une limite résiduelle déclarée et bornée par `timeout` (RX-15) ;
  - **RX-09** (RX-17) ;
  - **RX-11** (RX-18).
- Les observations RX-08 et RX-10 sont traitées (RX-16, RX-19). Restent non détectés, et déclarés : le dessin (M13) et une scène qui rejouerait le chemin du moteur en imitant ses messages (M23).
- Les corrections n'ajoutent aucune règle de jeu et restent dans le périmètre.
- Reste **à corriger** : RX-23 (a), une coquille déjà annoncée.
- Observations : RX-21 (libellé du contrôle de scénario), RX-23 (b) et (c), RX-12 maintenu.

Cette relecture ne valide ni commit ni publication.
