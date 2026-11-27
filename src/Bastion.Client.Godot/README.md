# Bastion.Client.Godot — prototype technique (lots 1D à 1G)

Ce prototype est une scène Godot 2D, vue du dessus, reliée au moteur `Bastion.Simulation`. On y clique sur une case de la zone atteignable, et l'unité s'y déplace selon le résultat du moteur. Depuis le lot 1F, c'est aussi un banc d'essai de MEC-0003 : trois scénarios fixes permettent d'observer un mur et des terrains. Ce n'est ni le design final de l'interface, ni une mécanique de gameplay. Depuis le lot 1G, un quatrième scénario permet d'essayer la gestion élémentaire des tours de MEC-0004 : fin de tour et récupération des TU et de l'énergie.

## Ce que fait la scène

**Quatre scénarios fixes**, choisis par les touches 1 à 4. Ce sont des données de démonstration, et non des règles de jeu. Partout, la carte MEC-0003 compte 5 × 5 cases de 1 500 mm, et l'unité `UnitBody.StandardHuman` part de (1,4), orientée N. Elle dispose de 20 TU et de 10 d'énergie dans les scénarios 1 à 3, et de 12 TU et de 35 d'énergie dans le scénario 4.

| Touche | Scénario | Carte |
|---|---|---|
| 1 | référence (lot 1D), chargé au lancement | terrain normal partout ; case infranchissable en (3,2) |
| 2 | mur et recherche de chemin | terrain normal partout ; mur standard sur l'arête est de (1,4) |
| 3 | coûts des terrains | terrain difficile en (2,4), très difficile en (3,4), normal ailleurs |
| 4 | gestion des tours (MEC-0004), au tour 1 | celle du scénario 1 |

**Affichage :**
- en vert, la zone atteignable rendue par `ComputeReachability` ;
- en gris foncé barré, une case infranchissable ;
- en trait noir, un mur, à l'épaisseur donnée par le moteur ;
- un cadre orange pour le terrain difficile et un cadre brun pour le terrain très difficile ; sans cadre, le terrain est normal ;
- l'unité est un disque, avec un trait jaune qui indique son orientation ;
- sous la carte, la légende de ces couleurs ;
- à droite :
  - le numéro et le titre du scénario ;
  - dans le seul scénario 4, le numéro du tour ;
  - la position, l'orientation, les TU, l'énergie et le nombre de cases atteignables ;
  - les directions du chemin choisi par le moteur pour le dernier ordre exécuté, par exemple « N → SE » ;
  - le dernier résultat et les commandes. Dans le scénario 4, la commande T s'y ajoute.

Les murs, les terrains et la case infranchissable sont lus dans la carte du moteur (`WallBetween`, `TerrainAt`, `IsBlocked`), et non recopiés par la scène.

**Commandes :**
- **clic gauche** sur une case : ordre transmis au moteur par `ExecuteOrder`. L'affichage reprend l'état rendu par le moteur, puis la zone est recalculée. Un ordre refusé ne change rien et affiche le message du moteur.
- **touches 1 à 4** de la rangée des chiffres : chargent le scénario correspondant, dans son état initial ; dans le scénario 4 déjà actif, la touche 4 le réinitialise. Sur un clavier AZERTY, ce sont les touches « & », « é », « " » et « ' », sans la touche Maj : la scène reconnaît la position de la touche. Le pavé numérique n'est pas pris en charge.
- **touche T**, dans le seul scénario 4 : termine le tour. Le moteur de tours (`TurnRules.EndTurn`) récupère les TU et l'énergie, plafonnées (60 TU récupérées pour 60 au plus, 20 d'énergie pour 100 au plus), et passe au tour suivant. La position, l'orientation et le chemin du dernier déplacement sont conservés ; le dernier résultat devient le compte rendu du moteur. La touche T est sans effet dans les scénarios 1 à 3.
- **touche R** : recrée l'état initial du scénario courant. C'est une commande de débogage, pas une règle de gameplay. Dans le scénario 4, elle restaure aussi le tour 1 et le message initial du scénario.

La scène ne contient aucune règle : elle convertit les pixels en cases, transmet les ordres et affiche les résultats. Le déplacement est instantané. Dans le scénario 2, c'est le moteur qui décide si la case située derrière le mur reste atteignable par un autre chemin, et par lequel. Dans le scénario 4, les récupérations et le numéro de tour viennent du moteur de tours ; la scène ne les calcule pas.

## Prérequis

- **SDK .NET 10** (`global.json` du dépôt).
- **Godot 4.7.2 stable .NET**, la version épinglée par `Sdk="Godot.NET.Sdk/4.7.2"` dans `Bastion.Client.Godot.csproj` (T-002, version de référence provisoire). Il faut l'édition « .NET » de Godot, téléchargeable sur la page officielle de la version `4.7.2-stable`. Le contrôle fumée vérifie cette version au lancement. `project.godot` garde le format qu'écrit l'éditeur Godot, pour qu'une ouverture dans l'éditeur ne le modifie pas.
- **Accès à NuGet** (nuget.org) lors de la première compilation, pour les paquets Godot 4.7.2.

## Compilation

Le client **ne fait pas partie de `Bastion.slnx`** : `dotnet build` et `dotnet format` à la racine du dépôt ne le voient pas.

La CI le contrôle par des étapes dédiées, depuis le lot 1E :
- restauration ;
- compilation Release ;
- format ;
- installation de Godot 4.7.2 stable .NET, depuis la distribution officielle, vérifiée par son empreinte SHA-512 ;
- compilation Debug ;
- contrôle fumée en mode headless, limité à 300 s.

Tout code de sortie non nul fait échouer la CI. La CI n'exécute pas le client avec un affichage et ne l'exporte pas.

**Avant tout lancement**, depuis la racine du dépôt, compiler le client en **Debug**. C'est la compilation que Godot charge quand il lance le projet depuis son dossier ; une compilation Release seule ne suffit pas.

```bash
dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj
```

Compilation Release, demandée par le mandat comme contrôle :

```bash
dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --configuration Release
```

## Ouverture et lancement

### Linux (vérifié en mode headless, en local et dans la CI GitHub Actions sous ubuntu-24.04, et sous affichage virtuel Xvfb en local ; pas sur un écran réel)

Dans les commandes ci-dessous, `GODOT` désigne le binaire `Godot_v4.7.2-stable_mono_linux.x86_64` de l'archive officielle, qui doit rester à côté de son dossier `GodotSharp/`.

Importer le projet (facultatif : le lancement fonctionne aussi sans import préalable) :

```bash
"$GODOT" --headless --path src/Bastion.Client.Godot --import
```

Lancer la scène dans une fenêtre :

```bash
"$GODOT" --path src/Bastion.Client.Godot
```

Ouvrir le projet dans l'éditeur Godot :

```bash
"$GODOT" --editor --path src/Bastion.Client.Godot
```

### macOS (essais manuels déclarés par le propriétaire : six le 23 novembre 2026, sept le 25 novembre 2026 ; non reproduits de façon indépendante)

#### Essais déclarés le 23 novembre 2026, sur le prototype du lot 1D

Le 23 novembre 2026, le propriétaire a déclaré conformes six essais manuels du prototype sous macOS. C'est un retour d'utilisateur, et non une reproduction indépendante : ni la version de macOS, ni les commandes exactes employées ne sont connues ici. Les essais déclarés conformes sont les suivants :

1. grille 5 × 5 ;
2. case (3,2) barrée ;
3. état initial ;
4. déplacement vers (2,4) ;
5. refus d'une destination inaccessible ;
6. touche R.

Ces essais portent sur le prototype du lot 1D, avant l'ajout des scénarios 2 et 3 par le lot 1F et du scénario 4 par le lot 1G. Ils ne couvrent ni ces trois scénarios, ni les touches 1 à 4 et T.

#### Essais déclarés le 25 novembre 2026, sur le prototype du lot 1G

Le 25 novembre 2026, après les essais du lot 1G sous macOS, le propriétaire a transmis directement dans la conversation Bastion le compte rendu suivant. Il est reproduit à l'annexe A de `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`.

| Essai | Résultat déclaré |
|---|---|
| Charger le scénario 4 | Satisfaisant |
| Terminer le premier tour | Satisfaisant |
| Terminer le deuxième tour | Satisfaisant |
| Déplacer puis terminer le tour | Satisfaisant |
| Réinitialiser | Satisfaisant |
| Vérifier les anciens scénarios | Satisfaisant |
| Vérifier la fenêtre | Satisfaisant |

D'après ce compte rendu, les essais portaient notamment sur :
- l'état initial du scénario 4 : tour 1, 12 TU, 35 d'énergie ;
- la première fin de tour : tour 2, 60 TU, 55 d'énergie ;
- la deuxième fin de tour : tour 3, 60 TU, 75 d'énergie ;
- la conservation de la position, de l'orientation et du chemin après un déplacement et une fin de tour ;
- la réinitialisation avec R et 4 ;
- l'absence d'effet de T dans les scénarios 1 à 3 ;
- la lisibilité de la fenêtre de 800 × 720 pixels.

Ces sept résultats sont des déclarations du propriétaire, sans reproduction indépendante. Ils sont distincts des six essais du 23 novembre 2026. Le compte rendu n'établit ni la version de macOS, ni le commit essayé, ni les modalités d'affichage, ni les périphériques utilisés.

#### Chemin et commandes

Le chemin et les commandes ci-dessous n'ont pas été vérifiés de façon indépendante sous macOS. Avec l'application officielle `Godot_mono.app` 4.7.2 placée dans `/Applications` :

```bash
GODOT=/Applications/Godot_mono.app/Contents/MacOS/Godot
```

Les commandes de compilation et de lancement sont ensuite les mêmes que sous Linux. On peut aussi ouvrir l'application Godot et importer le fichier `src/Bastion.Client.Godot/project.godot`.

## Contrôle fumée

Le contrôle fumée envoie des clics et des touches à la scène, par le même code que les entrées du joueur. Il compare ensuite l'état de la scène et le texte de son panneau aux résultats du moteur et aux valeurs des mandats. Le dessin de la grille n'est pas contrôlé automatiquement : seules les captures le montrent.

Il parcourt dans l'ordre :
1. le scénario 1 :
   - les contrôles du lot 1D, inchangés ;
   - puis un ordre dont le panneau affiche le chemin ;
2. le scénario 2, chargé par la touche 2 donnée par son seul libellé :
   - le chemin affiché est effacé au chargement ;
   - le moteur refuse le pas direct vers l'est, à cause du mur ;
   - (2,4) reste atteignable par un autre chemin ;
   - le clic sur (2,4) donne le résultat d'`ExecuteOrder`, et le panneau affiche le chemin choisi ;
   - un clic refusé ne modifie pas ce chemin ;
   - un second ordre, au chemin différent, le remplace ;
   - la touche R restaure l'état initial et efface le chemin ;
3. le scénario 3, chargé par la touche 3 telle qu'un clavier AZERTY la transmet (« " » à la position de la touche 3) :
   - un clic sur (2,4) donne 14 TU et 7 d'énergie ;
   - un clic suivant sur (3,4) donne 6 TU et 3 d'énergie ;
   - ces valeurs sont comparées à celles du mandat et au résultat d'`ExecuteOrder`, et le chemin affiché à celui du moteur ;
   - la touche R est vérifiée aussi ;
   - la touche 1 du pavé numérique et la barre d'espace restent sans effet ;
4. le retour au scénario 1 par la touche 1, transmise comme par un clavier AZERTY (« & »), depuis un état déplacé et un chemin affiché ;
5. la touche T dans les scénarios 1 à 3, après un déplacement : aucun effet (lot 1G, T10) ;
6. le scénario 4 (lot 1G), chargé par la touche 4 telle qu'un clavier AZERTY la transmet (« ' » à la position de la touche 4) :
   - état initial : (1,4), N, 12 TU, 35 d'énergie, tour 1 (T12) ;
   - deux fins de tour : tour 2 avec 60 TU et 55 d'énergie, puis tour 3 avec 60 TU et 75 d'énergie (T01, T02) ;
   - un déplacement, puis une fin de tour : position, orientation et chemin conservés, dernier résultat actualisé (T05, T16) ;
   - les touches R et 4 : réinitialisation complète (T11) ;
   - chaque fin de tour est comparée au résultat du moteur de tours, et les valeurs de MEC-0004 sont vérifiées en constantes ;
7. le retour au scénario 1, où aucun tour n'est affiché.

Les chemins attendus viennent du moteur, ou valent « aucun ». Le contrôle ne les relit jamais dans la scène.

Sans affichage, après la compilation Debug :

```bash
timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test
echo $?
```

Codes de sortie :
- **0** : tous les contrôles réussissent ;
- **1** : au moins un contrôle échoue ;
- **2** : une exception est survenue ;
- **124** (code de `timeout`) : Godot n'a pas quitté dans le délai. Ce n'est pas un contrôle en échec. Soit la scène n'a pas démarré le contrôle (par exemple parce que le projet n'est pas compilé en Debug), soit le contrôle s'est bloqué, soit il s'est terminé sans que Godot quitte. Godot ne quitterait alors jamais de lui-même ; d'où la limite de temps.

Sous macOS, `timeout` n'existe pas par défaut ; `gtimeout`, du paquet `coreutils` de Homebrew, joue le même rôle (non vérifié).

Avec un affichage, l'option `--capture=<dossier existant>` enregistre une image de la fenêtre après chaque étape. En mode headless, elle est comptée comme un échec, faute de rendu. Sous Linux sans écran, on peut passer par Xvfb :

```bash
timeout 300 xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test --capture=/tmp/captures
```

## Limites

**Essais non effectués pour les lots 1F et 1G**, au moment de leur réalisation :
- **macOS :** à la réalisation des lots, aucun essai des scénarios 2 à 4 ni des touches 1 à 4 et T ; les six essais déclarés par le propriétaire le 23 novembre 2026 portent sur le prototype du lot 1D. Depuis, le 25 novembre 2026, le propriétaire a déclaré satisfaisants sept essais du prototype du lot 1G sous macOS (section macOS ci-dessus), sans reproduction indépendante.
- **Écran réel :** aucun essai par Claude Code ni par la CI, sous aucun système (Linux, macOS ou Windows). Trois sources distinctes, à ne pas confondre :
  - **CI GitHub Actions :** tests automatisés, dont le contrôle fumée en mode headless, sans affichage ni capture d'écran ;
  - **vérifications locales sous Xvfb :** captures automatiques sous affichage virtuel, qui permettent d'examiner le rendu ;
  - **macOS :** sept essais manuels déclarés satisfaisants par le propriétaire le 25 novembre 2026, sans reproduction indépendante ni précision sur les modalités matérielles.
- **Clavier et souris physiques :** aucun essai par Claude Code ni par la CI. Les entrées sont simulées par le contrôle fumée et, lors de la relecture, par des événements X11 sous Xvfb. Les essais manuels déclarés par le propriétaire sous macOS ne précisent pas les périphériques utilisés.

**Ce qui est vérifié, et ses limites :**

- **Linux x86_64 :**
  - vérifié en mode headless, en local et dans la CI ;
  - vérifié sous Xvfb en local, avec le rendu logiciel OpenGL 3 de Mesa ;
  - jamais essayé sur un écran réel ni avec une souris physique.
- **Scénarios 2 et 3 (lot 1F) :**
  - vérifiés en local, par le contrôle fumée en mode headless et par des captures sous Xvfb ;
  - pas encore dans la CI au moment du lot 1F ;
  - validation manuelle : aucune au moment du lot 1F. Le 25 novembre 2026, l'essai « Vérifier les anciens scénarios » du propriétaire sous macOS est déclaré satisfaisant, sans reproduction indépendante ; le compte rendu cite l'absence d'effet de la touche T dans les scénarios 1 à 3, sans détailler les autres points vérifiés. Aucune sur un autre système.
- **Scénario 4 (lot 1G) :**
  - vérifié en local, par le contrôle fumée en mode headless et par des captures sous Xvfb ;
  - pas encore dans la CI au moment du lot 1G ;
  - validation manuelle : cinq des sept essais déclarés satisfaisants par le propriétaire sous macOS le 25 novembre 2026 portent sur ce scénario (chargement, deux fins de tour, déplacement puis fin de tour, réinitialisation ; section macOS), sans reproduction indépendante. Aucune sur un autre système.
- **Touches 1 à 4 et T :**
  - vérifiées par des événements simulés : la touche 2 par son seul libellé ; les touches 3, 1 et 4 comme un clavier AZERTY les transmet (libellé « " », « & » ou « ' », position de la touche) ;
  - aussi par de vrais événements X11 sous Xvfb, avec une disposition AZERTY imitée : les touches 1 à 3 et R lors de la relecture du lot 1F, les touches 4, T, R et 1 lors de celle du lot 1G (résultat inspecté sur des captures) ;
  - jamais avec un clavier physique par Claude Code ni par la CI. Les essais déclarés par le propriétaire sous macOS le 25 novembre 2026 citent les touches R, 4 et T, sans préciser le clavier ni sa disposition.
- **macOS :** six essais manuels déclarés conformes par le propriétaire le 23 novembre 2026, sur le prototype du lot 1D, et sept essais déclarés satisfaisants le 25 novembre 2026, sur le prototype du lot 1G (scénario 4, anciens scénarios et fenêtre). Ce sont des retours d'utilisateur, non reproduits de façon indépendante ; le compte rendu du 25 novembre n'établit ni le commit essayé, ni les modalités d'affichage, ni les périphériques. Le contrôle fumée en ligne de commande et `gtimeout` n'y sont pas vérifiés.
- **Windows :** aucun essai.
- **CI :** compilation, format et contrôle fumée en mode headless seulement ; ni affichage, ni export.
- **Export :** aucun export de jeu n'est testé.
