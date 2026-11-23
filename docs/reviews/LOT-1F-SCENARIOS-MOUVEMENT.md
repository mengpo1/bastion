# Bastion — Lot 1F : banc d'essai visuel de MEC-0003

**Date :** 23 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1F-v1.0-transcription.md`. C'est une transcription du message du propriétaire du 2026-11-23T13:32:13Z, extraite mécaniquement du journal de session (SHA-256 `72f548a7…5432`) ; son identité avec un fichier original n'est pas vérifiée. Statut du texte : « PRÉPARÉ — exécution non autorisée ».
**Autorisation d'exécution :** 2026-11-23T13:33:54Z. En réponse à une question de Claude Code, le propriétaire a choisi « Autoriser, avec Xvfb (Recommandé) » : exécution locale, avec des captures du rendu sous affichage virtuel. Ces captures sont présentées comme un rendu automatisé, et non comme une validation manuelle. L'autorisation n'ouvre ni commit, ni push, ni PR.
**Base :** `origin/main` = `ccd3cdf033c1ecc53244b3d9812eecd48ded5235` (fusion de la PR #23), établie par `git fetch origin main` au démarrage.
**Branche :** `claude/lot-1f-scenarios-mouvement`, créée localement à partir de `origin/main`.
**Publication :** autorisée par le propriétaire (message « BASTION — Lot 1F — Autorisation de publication ») : un commit des 9 fichiers du lot, le push de la seule branche du lot et une PR en brouillon vers `main`. La publication est conditionnée à une seconde relecture indépendante des corrections et à la vérification de la CI.
**État :** lot exécuté, relu par trois agents indépendants successifs et vérifié localement. Ce rapport ne peut pas citer le SHA ni la CI du commit qui le contient : ils sont donnés dans le message de fin de lot.

## 1. Résumé

La scène unique du prototype propose désormais trois scénarios fixes, chargés par les touches 1, 2 et 3 :

| Touche | Scénario | Carte |
|---|---|---|
| 1 | référence (lot 1D), chargé au lancement | case infranchissable en (3,2) |
| 2 | mur et recherche de chemin | mur standard sur l'arête est de (1,4) |
| 3 | coûts des terrains | terrain difficile en (2,4), très difficile en (3,4) |

Dans les trois scénarios, la carte compte 5 × 5 cases de 1 500 mm, et l'unité `StandardHuman` part de (1,4), orientée N, avec 20 TU et 10 d'énergie.

**Ce que la scène affiche :**
- les murs, à l'épaisseur donnée par le moteur ;
- les terrains, par un cadre de couleur, avec une légende sous la carte ;
- dans le panneau : le scénario, les commandes, et la suite des directions choisies par le moteur pour le dernier ordre exécuté.

Tout est lu par les API publiques du moteur. La scène ne contient aucun calcul de chemin, de coût, de collision ou de rotation. `Bastion.Simulation`, ses tests, la CI, le harnais, `Bastion.slnx` et les registres sont inchangés.

**Résultats observés :**
- **Contrôle fumée en mode headless :** 66 contrôles réussis, code de sortie 0. Les 21 contrôles du lot 1D sont inchangés. Les 45 nouveaux couvrent les scénarios 2 et 3, le chemin affiché, les changements de scénario, la touche R et des touches sans effet.
- **Valeurs du mandat confirmées par le moteur :**
  - scénario 3 : un clic sur (2,4) donne 14 TU et 7 d'énergie ; un clic suivant sur (3,4) donne 6 TU et 3 d'énergie ;
  - scénario 2 : le moteur refuse le pas direct vers l'est (« un mur occupe l'arête à traverser »), mais (2,4) reste atteignable. Il choisit le chemin N → SE, pour 10 TU et 5 d'énergie.
- **Sous affichage virtuel Xvfb :** les mêmes contrôles réussissent, et 23 captures montrent les trois scénarios. Sur la zone de la carte, le scénario 1 est **identique au pixel près** à `main`, aux neuf étapes du lot 1D.
- **Défauts introduits dans des copies jetables :** douze défauts, tous détectés (code 1). Six viennent des relectures (quatre de la première, deux de la seconde) : ils passaient d'abord au vert et ont conduit à renforcer les contrôles (§6).
- **Non-régression :** 46 tests sur 46, 75 tests des hooks, compilations sans avertissement, format conforme.

**Relectures indépendantes ciblées :** trois agents distincts, chacun « conforme sous réserves », sans constat bloquant. La deuxième, exigée par le propriétaire, porte sur les corrections faites après la première ; la troisième, sur celles faites après la deuxième. Les constats à corriger sont traités (§6). Les dernières retouches, faites après la troisième relecture, ne touchent que ce rapport (RZ-01 à RZ-03) et ne sont pas relues.

**Non vérifié :**
- aucune validation manuelle graphique, sur aucun système ;
- les touches 1, 2 et 3 sur un clavier physique ;
- macOS et Windows ;
- la CI, au moment de la rédaction : son résultat sur le commit publié est donné dans le message de fin de lot.

## 2. Fichiers

| Fichier | Rôle | Changement |
|---|---|---|
| `src/Bastion.Client.Godot/PrototypeScene.cs` | scène : cartes des trois scénarios, touches 1, 2 et 3, dessin des murs et des terrains, légende, panneau | +163 −19 (309 lignes) |
| `src/Bastion.Client.Godot/SmokeTest.cs` | contrôle fumée : 45 contrôles ajoutés après les 21 du scénario 1, qui ne changent pas | +191 −1 (394 lignes) |
| `src/Bastion.Client.Godot/project.godot` | hauteur de la fenêtre : 528 → 640 pixels, pour la légende | +1 −1 |
| `src/Bastion.Client.Godot/Main.tscn` | bas du panneau : 504 → 616 | +1 −1 |
| `src/Bastion.Client.Godot/README.md` | notice : scénarios, affichage, commandes, contrôle fumée, essais non effectués, limites | +64 −12 (185 lignes) |
| `docs/mandates/BASTION-MANDAT-LOT-1F-v1.0-transcription.md` | mandat archivé (transcription) | 88 lignes, nouveau |
| `docs/mandates/README.md` | une ligne d'index : provenance, statut, empreinte | +1 |
| `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md` | ce rapport | nouveau |
| `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT-RELECTURE.md` | rapports des trois relectures indépendantes, copiés sans modification les uns à la suite des autres | 780 lignes, nouveau |

Ces décomptes viennent de `git diff --numstat` contre `origin/main` ; la transcription est comptée comme nouvelle.

**Inchangés** (vérifié par `git diff --stat origin/main`, sans aucune sortie) :
- `src/Bastion.Simulation/` et `tests/` ;
- `.github/`, `scripts/`, `.claude/`, `CLAUDE.md` et `Bastion.slnx` ;
- `docs/gameplay/`, `docs/decisions/` et `docs/references/` ;
- `Bastion.Client.Godot.csproj` et les fichiers `.uid` du client.

## 3. Conception

### 3.1 Scénarios : des données, et non des règles

Une seule méthode, `BuildMap(int scenario)`, décrit les trois cartes avec le constructeur public du moteur (`TacticalMapBuilder.Block`, `AddWall`, `SetTerrain`). `LoadScenario` construit ensuite un `MovementModel` avec `MovementRules.Initial` et `UnitBody.StandardHuman`, puis place l'unité dans l'état initial commun. Il n'y a ni système de scènes, ni chargeur de niveaux, ni configuration externe.

### 3.2 Entrées

- **Clic gauche :** inchangé. Il transmet la case visée à `ExecuteOrder` ; la scène reprend `FinalState` et `Message`.
- **Touche R :** inchangée. Elle recrée l'état initial du scénario courant, et efface désormais le chemin affiché.
- **Touches 1, 2 et 3 :**
  - Elles sont reconnues par leur libellé (`Keycode`) ou par leur position (`PhysicalKeycode`).
  - Sur un clavier AZERTY, elles donnent « & », « é » et « " » sans la touche Maj. Sans la position, la relecture a constaté sous X11 que « & » et « " » n'étaient pas reconnues ; « é » l'était par son libellé. La position sert donc au moins pour les touches 1 et 3.
  - Le pavé numérique n'est pas pris en charge.
  - Charger un scénario reconstruit sa carte et remet l'unité dans l'état initial.

### 3.3 Affichage

- **Cases :** même fond qu'au lot 1D, sans changement. Vert pour la zone atteignable, gris pour le reste de la carte, gris foncé barré pour une case infranchissable.
- **Terrains :** un cadre intérieur de 10 pixels, orange pour « difficile » et brun pour « très difficile », d'après `TerrainAt`. Le terrain normal n'a pas de cadre, si bien que le scénario 1 garde exactement son dessin.
- **Murs :** pour chaque case, les arêtes est et sud sont lues par `WallBetween`. Le mur est tracé en noir, avec l'épaisseur du `WallType` ramenée à l'échelle de la case (100 mm → 6,4 pixels). Ces deux arêtes suffisent : le moteur range tout mur intérieur comme l'arête est ou sud de sa case ouest ou nord.
- **Légende :**
  - sous la carte, six pastilles (zone atteignable, hors de la zone, case infranchissable, mur, deux terrains) et la ligne « Sans cadre : terrain normal » ;
  - les noms des terrains sont ceux du moteur (`TerrainType.Name`) ;
  - c'est pour la légende que la fenêtre passe à 800 × 640.
- **Panneau :**
  - le scénario, par exemple « Scénario 2 : mur et recherche de chemin » ;
  - la position, l'orientation, les TU, l'énergie et le nombre de cases atteignables ;
  - « Chemin du dernier ordre exécuté » : les directions de `OrderOutcome.Path.Steps`, jointes (par exemple « N → SE ») ;
  - le dernier résultat, puis les commandes.

  Un ordre refusé ne modifie pas le chemin affiché, puisqu'il n'est pas exécuté. La touche R et le changement de scénario l'effacent : il redevient « aucun ».

Les lignes du panneau qu'utilisent les contrôles du lot 1D (position, orientation, TU, énergie, dernier résultat) gardent exactement leur format.

## 4. Commandes et résultats

Toutes les commandes ont été lancées dans le dépôt de travail, sur son état final. `GODOT` désigne le binaire officiel de Godot 4.7.2 stable .NET, vérifié au lot 1C.

### 4.1 Compilation et format du client

| Commande | Code | Résultat |
|---|---|---|
| `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` (Debug) | 0 | 0 Warning(s), 0 Error(s) |
| `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --configuration Release` | 0 | 0 Warning(s), 0 Error(s) |
| `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes --no-restore` | 0 | aucune sortie |

La première compilation a échoué sur une erreur de syntaxe : CS1002, un appel chaîné après une expression `switch`. Une variable locale l'a corrigée ; c'est la seule erreur rencontrée, et elle n'a laissé aucun journal.

### 4.2 Contrôle fumée en mode headless

```
timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test
```

Le code de sortie est 0, avec 66 lignes « SMOKE OK ». Les 21 premières sont celles du lot 1D, identiques au mot près à la sortie obtenue avant les corrections (`diff`, sans écart). Les 45 nouvelles :

```
SMOKE OK : panneau conforme à l'état après un ordre vers (2,4)
SMOKE OK : panneau : scénario 1, chemin « E » attendu après un ordre vers (2,4) (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : touche 2 : scénario 2 chargé, état initial (1,4), N, 20 TU, 10 d'énergie
SMOKE OK : carte du scénario 2 : 5 × 5 cases de 1500 mm, murs : (1,4) E standard ; cases infranchissables : aucune ; terrains non normaux : aucun
SMOKE OK : zone affichée = zone du moteur (23 cases)
SMOKE OK : panneau conforme à l'état au chargement du scénario 2
SMOKE OK : panneau : scénario 2, chemin « aucun » attendu au chargement du scénario 2 (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE OK : pas direct E depuis (1,4) refusé par le moteur : Pas E refusé : un mur occupe l'arête à traverser.
SMOKE OK : (2,4) reste dans la zone du moteur, par un autre chemin que le pas direct : N → SE
SMOKE OK : clic sur (2,4) = résultat d'ExecuteOrder : (2,4), SE, 10 TU, 5 d'énergie, chemin N → SE (Destination (2,4) atteinte.)
SMOKE OK : panneau conforme à l'état après l'ordre vers (2,4)
SMOKE OK : panneau : scénario 2, chemin « N → SE » attendu après l'ordre vers (2,4) (LastPath : « N → SE » ; panneau : « Chemin du dernier ordre exécuté : N → SE »)
SMOKE OK : clic sur (4,0), hors de la zone du moteur : état inchangé (Ordre refusé : la destination (4,0) n'appartient pas à la zone atteignable.)
SMOKE OK : panneau conforme à l'état après l'ordre refusé
SMOKE OK : panneau : scénario 2, chemin « N → SE » attendu après l'ordre refusé (LastPath : « N → SE » ; panneau : « Chemin du dernier ordre exécuté : N → SE »)
SMOKE OK : second ordre vers (3,4) = résultat d'ExecuteOrder, au chemin différent du premier : (3,4), E, 6 TU, 3 d'énergie, chemin E
SMOKE OK : panneau conforme à l'état après le second ordre
SMOKE OK : panneau : scénario 2, chemin « E » attendu après le second ordre (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : touche R : scénario 2 conservé, état initial restitué ((1,4), N, 20 TU, 10 d'énergie)
SMOKE OK : panneau conforme à l'état après la touche R
SMOKE OK : panneau : scénario 2, chemin « aucun » attendu après la touche R (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE OK : après R, clic sur (2,4) : même résultat ((2,4), SE, 10 TU, 5 d'énergie)
SMOKE OK : panneau conforme à l'état après le nouvel ordre vers (2,4)
SMOKE OK : panneau : scénario 2, chemin « N → SE » attendu après le nouvel ordre vers (2,4) (LastPath : « N → SE » ; panneau : « Chemin du dernier ordre exécuté : N → SE »)
SMOKE OK : touche 3 : scénario 3 chargé, état initial (1,4), N, 20 TU, 10 d'énergie
SMOKE OK : carte du scénario 3 : 5 × 5 cases de 1500 mm, murs : aucun ; cases infranchissables : aucune ; terrains non normaux : (2,4) difficile, (3,4) très difficile
SMOKE OK : zone affichée = zone du moteur (23 cases)
SMOKE OK : panneau conforme à l'état au chargement du scénario 3
SMOKE OK : panneau : scénario 3, chemin « aucun » attendu au chargement du scénario 3 (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE OK : clic sur (2,4), terrain difficile = résultat d'ExecuteOrder, 14 TU et 7 d'énergie attendues : (2,4), E, 14 TU, 7 d'énergie
SMOKE OK : clic sur (3,4), terrain très difficile = résultat d'ExecuteOrder, 6 TU et 3 d'énergie attendues : (3,4), E, 6 TU, 3 d'énergie
SMOKE OK : panneau conforme à l'état après les deux ordres
SMOKE OK : panneau : scénario 3, chemin « E » attendu après les deux ordres (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : touche R : scénario 3 conservé, état initial restitué ((1,4), N, 20 TU, 10 d'énergie)
SMOKE OK : panneau conforme à l'état après la touche R
SMOKE OK : panneau : scénario 3, chemin « aucun » attendu après la touche R (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE OK : après R, clic sur (2,4) : même résultat ((2,4), E, 14 TU, 7 d'énergie)
SMOKE OK : panneau conforme à l'état après le nouvel ordre vers (2,4)
SMOKE OK : panneau : scénario 3, chemin « E » attendu après le nouvel ordre vers (2,4) (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : touche 1 du pavé numérique et espace : aucun effet ((2,4), E, 14 TU, 7 d'énergie)
SMOKE OK : panneau conforme à l'état après les touches sans effet
SMOKE OK : panneau : scénario 3, chemin « E » attendu après les touches sans effet (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : touche 1 : scénario 1 rechargé dans son état initial ((1,4), N, 20 TU, 10 d'énergie, murs : aucun ; cases infranchissables : (3,2) ; terrains non normaux : aucun)
SMOKE OK : panneau conforme à l'état après le retour au scénario 1
SMOKE OK : panneau : scénario 1, chemin « aucun » attendu après le retour au scénario 1 (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE : RÉUSSITE
```

**Comment les contrôles sont faits :**
- Les clics et les touches passent par `Viewport.PushInput`, puis par le même `_UnhandledInput` que les entrées du joueur.
- **Touches :**
  - la touche 2 est envoyée par son **seul libellé** (`Key2`, sans position) ;
  - les touches 3 et 1 sont envoyées comme un clavier AZERTY : libellés `Quotedbl` et `Ampersand`, positions `Key3` et `Key1` ;
  - chaque voie de reconnaissance est donc contrôlée à part.
- **Résultats des ordres :** chacun est comparé à celui d'`ExecuteOrder`, calculé par le contrôle depuis le même état. Le refus du pas direct est donné par `EvaluateStep`.
- **Valeurs du mandat :** 14 TU et 7 d'énergie, puis 6 TU et 3 d'énergie. Elles sont écrites en constantes dans le contrôle, indépendamment de la scène.
- **Chemins attendus :** ils viennent de `OrderOutcome.Path` ou valent « aucun ». Le contrôle ne les relit jamais dans la scène. En cas d'échec, le message cite `LastPath` et la ligne réellement affichée dans le panneau.
- **Dernier ordre :** dans le scénario 2, un second ordre consécutif, au chemin différent (E après N → SE), doit remplacer le chemin affiché.
- **Touches sans effet :** la touche 1 du pavé numérique et la barre d'espace ne doivent changer ni le scénario, ni l'état, ni le dernier résultat.
- **Effacement du chemin :** chaque changement de scénario part d'un chemin affiché qui n'est pas « aucun ». L'effacement est donc réellement mis à l'épreuve.
- **Cartes :** elles sont décrites par les API publiques (`WallBetween`, `IsBlocked`, `TerrainAt`), et non par le code de la scène.

### 4.3 Rendu sous affichage virtuel (Xvfb)

```
timeout 300 xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test --capture=<dossier>
```

- **Résultat :** code 0, « SMOKE : RÉUSSITE », et 89 lignes « SMOKE OK » : les 66 contrôles et 23 captures enregistrées.
- **Rendu :** logiciel, OpenGL 3 avec Mesa llvmpipe, après un avertissement sur l'absence de Vulkan.
- **Captures :** dans le dossier temporaire de la session (`…/scratchpad/lot1f/captures/`), non versionnées :
  - `01` à `10` : scénario 1 ;
  - `11` à `16` : scénario 2 ;
  - `17` à `22` : scénario 3 ;
  - `23` : retour au scénario 1.

**Ce que montrent les captures** (examen visuel par Claude Code, confirmé par la relecture) :
- **Scénario 2, au chargement :** le mur noir est sur l'arête est de (1,4). La zone verte couvre 23 cases, dont (2,4) ; seules (4,0) et la case de l'unité sont hors de la zone.
- **Scénario 2, après l'ordre vers (2,4) :** l'unité est en (2,4), orientée SE. Le panneau affiche « Chemin du dernier ordre exécuté : N → SE », 10 TU et 5 d'énergie.
- **Scénario 3, après les deux ordres :** un cadre orange en (2,4), un cadre brun en (3,4), et l'unité en (3,4). Le panneau affiche 6 TU et 3 d'énergie, et la légende est lisible.

Ce sont des captures d'un rendu automatisé, et non une validation manuelle.

**Scénario 1 identique à `main` :**
- Les mêmes captures ont été faites avec le code de `main` (`ccd3cdf`), dans un clone jetable et dans les mêmes conditions.
- La zone de la carte (pixels 0 à 527 en largeur, 0 à 511 en hauteur) a été comparée avec Pillow (`ImageChops.difference`).
- Résultats, tous **identiques** :
  - les neuf captures `01` à `09` ;
  - la capture `10` (premier ordre du lot 1F vers (2,4)), comparée à `02-ordre-2-4` de `main` ;
  - la capture `23` (retour par la touche 1), comparée à `01-initial` de `main`.
- Témoin : la capture `11-scenario-2`, comparée à `01-initial` de `main`, est bien signalée comme différente.
- Seuls changent le texte du panneau et la bande de légende sous la carte.

Les trois relectures ont refait cette comparaison de leur côté, avec le même résultat.

### 4.4 Vérifications négatives (copies jetables)

**Méthode.** Le script `negatifs.sh`, placé dans le dossier temporaire de la session :
- copie l'arbre de travail, sans `.git`, `bin`, `obj` ni `.godot` ;
- introduit un seul défaut dans `PrototypeScene.cs` ;
- compile le client en Debug, puis lance le contrôle fumée headless.

Le dépôt de travail n'est pas touché, et les copies sont supprimées.

**Origine des cas :**
- les défauts A à F sont les miens ;
- les défauts G à J reprennent N1, N2, N3 et N5 de la première relecture, et K et M deux défauts de la seconde. Tous passaient **au vert** avant les corrections, et sont maintenant détectés.

| Défaut | Premier contrôle en échec (extrait) | Code |
|---|---|---|
| A. mur retiré du scénario 2 | carte du scénario 2 ; « pas direct E … : Pas E exécuté vers (2,4). » | 1 |
| B. terrains intervertis dans le scénario 3 | carte du scénario 3 ; « … 14 TU et 7 d'énergie attendues : (2,4), E, 12 TU, 6 d'énergie » | 1 |
| C. position des touches ignorée | « touche 3 : scénario 3 chargé, état initial (2,4), SE, 10 TU, 5 d'énergie » | 1 |
| D. chemin du dernier ordre jamais mis à jour | « panneau : scénario 1, chemin « E » attendu … (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun ») » | 1 |
| E. la scène retouche l'état du moteur (1 TU de plus) | dès le premier ordre du scénario 1 : « (2,4), E, 15 TU, 8 d'énergie » | 1 |
| F. effacement du chemin retiré de `ResetScenario` (R et changement de scénario) | « touche 2 : scénario 2 chargé, état initial (1,4), N, 20 TU, 10 d'énergie » (le chemin « E » n'est pas effacé) | 1 |
| G. le changement de scénario garde le chemin (N1) | même premier contrôle que F | 1 |
| H. un ordre refusé remplace le chemin (N2) | « chemin « N → SE » attendu après l'ordre refusé (LastPath : « chemin inventé par le client » ; panneau : « … chemin inventé par le client ») » | 1 |
| I. chemin mis à jour dans le seul scénario 2 (N3) | « scénario 1, chemin « E » attendu » ; « scénario 3, chemin « E » attendu après les deux ordres » | 1 |
| J. libellé ignoré, position seule (N5) | « touche 2 : scénario 2 chargé, état initial (2,4), E, 16 TU, 8 d'énergie » | 1 |
| K. chemin remplacé seulement s'il vaut « aucun » (seconde relecture) | « chemin « E » attendu après le second ordre (LastPath : « N → SE » … ) » | 1 |
| M. toute autre touche charge le scénario 1 (seconde relecture) | « touche 1 du pavé numérique et espace : aucun effet ((1,4), N, 20 TU, 10 d'énergie) » | 1 |

Dans les douze cas, la compilation Debug réussit et le contrôle fumée sort avec le code 1. Dans la CI, l'étape « contrôle fumée » échouerait.

Les défauts de compilation, de format et d'intégrité de Godot ont été vérifiés au lot 1E. Ce lot ne touche pas à ces étapes.

### 4.5 Non-régression du dépôt

Ces commandes ont été relancées après les dernières corrections. Toutes renvoient le code 0.

| Commande | Résultat |
|---|---|
| `dotnet restore` | — |
| `dotnet build --no-restore --configuration Release` | 0 Warning(s), 0 Error(s) |
| `dotnet test --no-build --configuration Release` | « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » |
| `dotnet format --verify-no-changes --no-restore` | aucune sortie |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |

## 5. Ce que le moteur montre, sans interprétation

**Scénario 2 :**
- Le pas direct E depuis (1,4) est refusé, avec le motif `WallOnEdge`.
- Le moteur atteint quand même (2,4), par N puis SE. Le pas SE est un pas diagonal de (1,3) vers (2,4), qui passe par l'extrémité nord du mur.
- C'est le moteur qui admet ce passage : le client ne fait que transmettre l'ordre et afficher le chemin rendu. Ce lot ne modifie pas le moteur, et ce rapport ne juge pas ce comportement au regard de MEC-0003.
- Le coût total est de 10 TU (4 + 6) et de 5 d'énergie (2 + 3).

**Scénario 3 :**
- Les coûts suivent le terrain de la case d'arrivée :
  - (2,4), terrain difficile : 6 TU et 3 d'énergie ;
  - (3,4), terrain très difficile : 8 TU et 4 d'énergie.
- Les valeurs du mandat sont donc obtenues : 14/7, puis 6/3.

## 6. Relectures indépendantes ciblées

Les deux rapports sont copiés sans modification, l'un à la suite de l'autre, dans `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT-RELECTURE.md`.

### 6.1 Première relecture

Un agent distinct du développeur a relu l'arbre de travail avant les corrections.

**Ce que la relecture a exécuté elle-même :**
- les empreintes, les décomptes et l'absence de changement des zones protégées ;
- la compilation, le format et le contrôle fumée : 48 contrôles, code 0 ;
- les 21 contrôles du lot 1D, comparés à ceux de `main` dans le code et dans la sortie ;
- le rendu Xvfb et la comparaison au pixel avec `main` ;
- les six défauts du développeur, plus cinq défauts à elle ;
- de vrais événements clavier X11 sous Xvfb, avec une disposition AZERTY imitée ;
- la non-régression à la racine.

Elle n'a rien modifié : `git status` et les empreintes sont identiques avant et après.

**Verdict :** « conforme sous réserves », sans constat bloquant. La réserve porte sur RX-01. La relecture ne s'accorde pas la validation finale.

| Constat | Classement | Traitement |
|---|---|---|
| RX-01 : l'effacement du chemin au changement de scénario n'était gardé par aucun contrôle, et trois lignes « chemin » relisaient la valeur qu'elles vérifiaient | à corriger | **Corrigé** dans `SmokeTest.cs`. `CheckScenario` reçoit le chemin attendu (moteur ou « aucun ») et compare `LastPath`, au lieu de le relire. Un ordre est exécuté dans le scénario 1 avant la touche 2, et un nouvel ordre dans le scénario 2 avant la touche 3 : chaque changement de scénario part ainsi d'un chemin affiché. Le chemin est vérifié après les ordres du scénario 3 et après la touche R. Les défauts G (N1) et I (N3) sont maintenant détectés. Le libellé du défaut F est corrigé. |
| RX-02 : « un ordre refusé ne modifie pas le chemin » n'était gardé par aucun contrôle | observation | **Traité.** Dans le scénario 2, un clic sur (4,0), hors de la zone, suit le détour ; le contrôle vérifie que l'état et le chemin « N → SE » ne changent pas. Le défaut H (N2) est maintenant détecté. |
| RX-03 : la reconnaissance par libellé n'était pas isolée, et le rapport surestimait le rôle de la position pour la touche 2 | observation | **Traité.** La touche 2 est envoyée par son seul libellé, et le défaut J (N5) est maintenant détecté. Le §3.2 et la notice sont reformulés, et la notice mentionne l'essai X11 de la relecture. |
| RX-04 : le chemin affiché est le chemin planifié, et non les pas exécutés | observation | **Non modifié.** Avec ce moteur, un ordre de la zone ne peut pas être interrompu (constat de la relecture). Le libellé du mandat, « directions choisies par le moteur », est respecté. |
| RX-05 : un autre type de terrain serait dessiné sans cadre et présenté comme « normal » | observation | **Non modifié.** Les données sont fixes : seuls les trois terrains du moteur existent. |
| RX-06 : imprécisions du rapport (case de l'unité hors zone ; défaut E cité comme preuve d'absence de règle ; sections « en cours ») | observation | **Corrigé.** Le §4.3 cite la case de l'unité. Au §8, l'absence de règle repose sur la lecture du code ; le défaut E montre seulement que la scène ne retouche pas l'état du moteur. Le §6 est complété. |

Ces corrections ont ensuite été relues par la seconde relecture (§6.2).

### 6.2 Seconde relecture, exigée avant publication

**Demande :** le propriétaire a exigé « une relecture indépendante ciblée des corrections effectuées après la première relecture, notamment RX-01 et les nouveaux contrôles contre les défauts introduits ». Un second agent, ni développeur ni auteur de la première relecture, a relu la différence entre la copie conservée par la première relecture et l'arbre de travail.

**Ce qu'il a exécuté lui-même :**
- la vérification du périmètre des corrections : seuls `SmokeTest.cs`, la notice et ce rapport ont changé ; la scène, `Main.tscn`, `project.godot`, la simulation, la CI, le harnais et les registres sont identiques ;
- les 21 contrôles du lot 1D, rejoués sur `main` et comparés ;
- la compilation, le format, le contrôle fumée (60 contrôles, code 0), le rendu Xvfb et la comparaison au pixel, avec un témoin ;
- les dix défauts A à J ;
- treize défauts à lui, dont N1, N2, N3 et N5 reformulés ;
- un rendu de la notice par pandoc ;
- la non-régression à la racine.

Il n'a rien modifié.

**Verdict :** « conforme sous réserves », sans constat bloquant. RX-01, RX-02 et RX-03 sont jugés réellement corrigés. Il ne s'accorde pas la validation finale.

| Constat | Classement | Traitement |
|---|---|---|
| RY-01 : le caractère « dernier » du chemin affiché n'était gardé par aucun contrôle. Le défaut K (chemin remplacé seulement s'il vaut « aucun ») passait au vert | à corriger | **Corrigé.** Dans le scénario 2, un second ordre consécutif vers (3,4), au chemin différent (E après N → SE), doit remplacer le chemin affiché. Le contrôle vérifie aussi que les deux chemins diffèrent. Le défaut K est maintenant détecté. |
| RY-02 : une fois rendue, la liste « Essais non effectués » de la notice se fondait dans la liste des limites qui la suit | à corriger | **Corrigé.** Un intertitre « Ce qui est vérifié, et ses limites » sépare les deux listes. Pandoc (GFM) rend désormais la première liste seule, avec ses trois éléments. Le rendu sur GitHub n'est pas vérifié. |
| RY-03 : décompte et empreinte de la notice périmés dans le rapport | à corriger | **Corrigé.** Le §2 et l'annexe A ont été recalculés sur l'état final. |
| RY-04 : passages du rapport à mettre à jour (« pas relu une seconde fois », « réserve levée », 304 lignes, premier contrôle en échec des défauts F et G) | observation | **Corrigé** dans les §1, §2, §4.4 et §6. |
| RY-05 : aucune touche « sans effet » n'était envoyée ; une reconnaissance qui accepterait toute touche (défaut M) passait au vert | observation | **Traité.** La touche 1 du pavé numérique et la barre d'espace sont envoyées dans le scénario 3. Elles ne doivent changer ni le scénario, ni l'état, ni le dernier résultat, ni le chemin. Le défaut M est maintenant détecté. |
| RY-06 : le message de `CheckScenario` présentait `LastPath` comme la valeur « affichée » | observation | **Corrigé.** Le message cite `LastPath` et la ligne réellement lue dans le panneau. |

**Après ces corrections, toutes les vérifications du §4 ont été relancées :**
- 66 contrôles, code 0 ;
- les 21 lignes du lot 1D, toujours identiques ;
- 89 « SMOKE OK » et 23 captures sous Xvfb ;
- le scénario 1 identique au pixel près à `main` ;
- douze défauts détectés ;
- la non-régression à la racine.

Ces corrections (RY-01 à RY-06) ont ensuite été relues par la troisième relecture (§6.3).

### 6.3 Troisième relecture, sur les corrections RY-01 à RY-06

**Relecteur :** un troisième agent, ni développeur ni auteur des deux relectures précédentes. Il a relu la différence entre la copie conservée par la deuxième relecture et l'arbre de travail.

**Ce qu'il a exécuté lui-même :**
- la vérification du périmètre des corrections ;
- les 21 contrôles du lot 1D, rejoués sur `main` ;
- la compilation, le format, le contrôle fumée (66 contrôles, code 0) et le rendu Xvfb (89 « SMOKE OK », 23 captures identiques à celles du développeur) ;
- les défauts K et M, maintenant détectés, plus six défauts à lui (K2, M1, M2, M3, P, P2), tous détectés ;
- les douze défauts du script du développeur ;
- le rendu de la notice par pandoc (deux listes, de 3 et de 7 éléments) ;
- les décomptes et les 16 empreintes de l'annexe A ;
- la non-régression à la racine, sauf les tests des hooks, que le harnais inchangé ne justifiait pas.

Il n'a rien modifié.

**Verdict :** « conforme sous réserves », sans constat bloquant. RY-01, RY-02, RY-03, RY-05 et RY-06 sont jugés corrigés. Il ne s'accorde pas la validation finale.

| Constat | Classement | Traitement |
|---|---|---|
| RZ-01 : le rapport deviendrait faux une fois cette relecture ajoutée (« relu deux fois », « pas relues par un troisième agent », nombre de lignes et empreinte du fichier de relecture) | à corriger | **Corrigé** après la copie de la troisième relecture : en-tête, §1, §2, §6 et annexe A. |
| RZ-02 : deux extraits du §4.4 (défauts D et H) citaient l'ancien format du message (« affiché ») | observation | **Corrigé** d'après le journal `negatifs3.log`. |
| RZ-03 : la deuxième relecture a introduit treize défauts, et non douze | observation | **Corrigé** au §6.2. |
| RZ-04 : l'autorisation de publication citée par le rapport n'est pas vérifiable par le relecteur | observation | **Non modifié.** Seul le propriétaire peut la confirmer : c'est son message « BASTION — Lot 1F — Autorisation de publication ». |
| RZ-05 : l'arrivée des touches sans effet n'est prouvée que par sabotage ; si une touche cessait d'atteindre la scène, le contrôle passerait sans rien vérifier | observation | **Non modifié** ; limite ajoutée au §7. |

Les retouches faites pour RZ-01 à RZ-03 ne touchent que ce rapport. Elles n'ont pas été relues par un quatrième agent.

## 7. Limites et contrôles non exécutés

**Essais non effectués, explicitement :**
- **macOS :** aucun essai du lot 1F (scénarios 2 et 3, touches 1, 2 et 3, légende, panneau). Les six essais manuels déclarés par le propriétaire le 23 novembre 2026 portent sur le prototype du lot 1D. Ils ne valent pas pour le lot 1F.
- **Écran réel :** aucun essai, sous aucun système (Linux, macOS ou Windows). Le rendu du lot 1F n'est connu que par des captures automatiques sous Xvfb, avec un rendu logiciel.
- **Clavier et souris physiques :** aucun essai.
- **Windows :** aucun essai, de quelque nature que ce soit.

**Autres limites :**
- **Touches 1, 2 et 3 :**
  - vérifiées par des événements simulés dans le contrôle fumée ;
  - vérifiées aussi, lors de la relecture, par de vrais événements X11 avec une disposition AZERTY imitée, ce qui n'est pas une disposition XKB complète ;
  - jamais avec un clavier physique ;
  - le pavé numérique n'est pas pris en charge.
- **CI :** au moment de la rédaction, rien n'est poussé. Le workflow n'a pas à changer : son étape lance `--smoke-test`, qui inclut les nouveaux scénarios. Le résultat de la CI du commit publié est donné dans le message de fin de lot.
- **Dessin :** le contrôle fumée vérifie l'état, la carte et le texte du panneau, mais pas les pixels. La comparaison au pixel du §4.3 est une vérification ponctuelle, hors du contrôle fumée.
- **Chemin affiché :** c'est le chemin planifié par le moteur (RX-04).
- **Touches sans effet :** le contrôle prouve qu'elles ne changent rien, mais pas qu'elles atteignent la scène. Si une touche cessait d'y arriver, il passerait sans rien vérifier (RZ-05). Aujourd'hui, la troisième relecture a établi par sabotage qu'elles arrivent.

## 8. Conformité au mandat

| Exigence | Réalisation | Preuve |
|---|---|---|
| §2 scène unique, trois scénarios, touches 1, 2 et 3 | `BuildMap` et `LoadScenario` ; touches reconnues par libellé ou par position, chaque voie contrôlée | §3, §4.2 |
| §2 scénario 1 et contrôles existants inchangés | 21 contrôles du lot 1D identiques et réussis ; carte identique au pixel près à `main` | §4.2, §4.3 |
| §2 scénario 2 : mur affiché ; accès décidé par le moteur ; chemin affiché | pas direct refusé (`WallOnEdge`) ; (2,4) atteint par N → SE ; panneau « Chemin du dernier ordre exécuté » | §4.2, §4.3, §5 |
| §2 scénario 3 : couleurs et légende ; 14/7 puis 6/3 confirmés par le moteur | cadres orange et brun, légende ; comparaison à `ExecuteOrder` et aux constantes du mandat | §4.2, §4.3 |
| §3 interface : touches, R, clic, panneau ; murs et terrains lus dans le moteur | `WallBetween`, `TerrainAt`, `IsBlocked` | §3.3 |
| §3 présentation 2D minimale, sans sprite ni animation | rectangles, traits, disque et texte | `PrototypeScene.cs` |
| §4 simulation inchangée, API publiques seulement | `git diff` vide sur `src/Bastion.Simulation/` ; aucun `InternalsVisibleTo` (relecture) | §2 |
| §4 aucune règle de chemin, coût, collision ou rotation dans le client | lecture du code, par le développeur et la relecture. Le défaut E montre seulement que la scène ne retouche pas l'état rendu par le moteur | §3, §6 |
| §4 ni framework, ni chargeur, ni configuration externe | une méthode `BuildMap` | §3.1 |
| §4 MEC-0001, MEC-0002, registres, `Bastion.slnx`, harnais et CI intacts | `git diff --stat` vide sur ces chemins | §2 |
| §5.1 contrôles du scénario initial préservés | sortie identique au mot près | §4.2 |
| §5.2 et §5.3 contrôles fumée des scénarios 2 et 3 par les entrées Godot ; murs, terrains, changements de scénario, ressources, touche R | 45 contrôles | §4.2 |
| §5.4 comparaison au moteur et aux constantes du mandat | voir la preuve | §4.2 |
| §5.5 tests, format, harnais, contrôles du client | voir la preuve | §4.1, §4.5 |
| §5.6 relecture indépendante ciblée | trois relectures successives, chacune « conforme sous réserves » ; constats à corriger traités | §6 |
| §5 aucune validation manuelle déclarée sans avoir été faite | voir la preuve | §7 |
| §6 livrables | prototype, notice, mandat archivé et indexé, ce rapport, relecture | §2 |
| §7 aucun commit, push ni PR sans autorisation | publication autorisée séparément par le propriétaire : un commit des 9 fichiers, push de la seule branche du lot, PR en brouillon | message « BASTION — Lot 1F — Autorisation de publication » |

## 9. Points à décider par le propriétaire

1. **Fusion :** la publication (commit, push, PR en brouillon) est autorisée. La fusion dans `main` demande une autorisation distincte.
2. **Validation manuelle :** si vous le souhaitez, essayer les scénarios 2 et 3 et les touches 1, 2 et 3 sur un écran et un clavier réels, par exemple sous macOS.
3. **Passage diagonal près du mur (§5) :** c'est le comportement actuel du moteur, que le banc d'essai rend visible. S'il ne correspond pas à ce que vous attendez, la question porte sur MEC-0003 et non sur le client ; elle relèverait d'un autre mandat.

## Annexe A — Empreintes SHA-256

| Fichier | Sur `origin/main` (`ccd3cdf`) | Dans l'arbre de travail du lot |
|---|---|---|
| `src/Bastion.Client.Godot/PrototypeScene.cs` | `62b2cce35de4a372352365e0714b7d85aeed62aec598189d1a549fd1e1675f27` | `f767b204fe4575e625aa8e3e86a122006120e051a35416f1f3601ca7d0b29623` |
| `src/Bastion.Client.Godot/SmokeTest.cs` | `eedf802f690c187e25b5c35665e5175a811ebd603ab1a4875670bfd4983fa207` | `4af6d1ad2d35031cf1278a70dc3f720b8c7103a953db5748e707010c155841e3` |
| `src/Bastion.Client.Godot/README.md` | `df74c7e5b7b67749da17e5315cbf8823a899a00db47030ee51a4ec7062d32372` | `82a208e80dbd3becaa701aced8fadbad3e2f73ba1879b253ed29d30805831b8b` |
| `src/Bastion.Client.Godot/Main.tscn` | `3b199580c9aac3630e59fdde0f560434f7a3e1136a81c22b0385afc44ca14cb6` | `5b101ac563da2c4d50aecbc315cd6ec9fe1d94457fb4571978e8782be21b43e6` |
| `src/Bastion.Client.Godot/project.godot` | `2c112d9a28b989f518bdab36c2fd17b17f51916b8f8909f16bdd60d38dbd7fe9` | `e96064e768b9f310fa5e5ac8cb89447a958ad5498f4309adb4b9bd773aef026d` |
| `docs/mandates/README.md` | `8cd9953a75cc44bf1d01f501330111f35b42b3b7e1093960bcd59b2fb4cce7aa` | `0e1d27abc0ecd9a11a06800944b9e4f10f260eb20734e2989b7aae4049116fbb` |
| `docs/mandates/BASTION-MANDAT-LOT-1F-v1.0-transcription.md` | absent | `72f548a7090dec71523b1cb26679985fc6b241cd9fddf32fc77c534c6a295432` |
| `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT-RELECTURE.md` | absent | `a8f1e5f20a56c109f209ffa1a8ffac5c8edc7ce83ab84f5d7053d24585719f73` |

Ce rapport ne peut pas porter sa propre empreinte.
