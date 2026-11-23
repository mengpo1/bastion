# Bastion.Client.Godot — prototype technique (lots 1D à 1F)

Ce prototype est une scène Godot 2D, vue du dessus, reliée au moteur `Bastion.Simulation`. On y clique sur une case de la zone atteignable, et l'unité s'y déplace selon le résultat du moteur. Depuis le lot 1F, c'est aussi un banc d'essai de MEC-0003 : trois scénarios fixes permettent d'observer un mur et des terrains. Ce n'est ni le design final de l'interface, ni une mécanique de gameplay.

## Ce que fait la scène

**Trois scénarios fixes**, choisis par les touches 1, 2 et 3. Ce sont des données de démonstration, et non des règles de jeu. Partout, la carte MEC-0003 compte 5 × 5 cases de 1 500 mm, et l'unité `UnitBody.StandardHuman` part de (1,4), orientée N, avec 20 TU et 10 d'énergie.

| Touche | Scénario | Carte |
|---|---|---|
| 1 | référence (lot 1D), chargé au lancement | terrain normal partout ; case infranchissable en (3,2) |
| 2 | mur et recherche de chemin | terrain normal partout ; mur standard sur l'arête est de (1,4) |
| 3 | coûts des terrains | terrain difficile en (2,4), très difficile en (3,4), normal ailleurs |

**Affichage :**
- en vert, la zone atteignable rendue par `ComputeReachability` ;
- en gris foncé barré, une case infranchissable ;
- en trait noir, un mur, à l'épaisseur donnée par le moteur ;
- un cadre orange pour le terrain difficile et un cadre brun pour le terrain très difficile ; sans cadre, le terrain est normal ;
- l'unité est un disque, avec un trait jaune qui indique son orientation ;
- sous la carte, la légende de ces couleurs ;
- à droite :
  - le numéro et le titre du scénario ;
  - la position, l'orientation, les TU, l'énergie et le nombre de cases atteignables ;
  - les directions du chemin choisi par le moteur pour le dernier ordre exécuté, par exemple « N → SE » ;
  - le dernier résultat et les commandes.

Les murs, les terrains et la case infranchissable sont lus dans la carte du moteur (`WallBetween`, `TerrainAt`, `IsBlocked`), et non recopiés par la scène.

**Commandes :**
- **clic gauche** sur une case : ordre transmis au moteur par `ExecuteOrder`. L'affichage reprend l'état rendu par le moteur, puis la zone est recalculée. Un ordre refusé ne change rien et affiche le message du moteur.
- **touches 1, 2 et 3** de la rangée des chiffres : chargent le scénario correspondant, dans son état initial. Sur un clavier AZERTY, ce sont les touches « & », « é » et « " », sans la touche Maj : la scène reconnaît la position de la touche. Le pavé numérique n'est pas pris en charge.
- **touche R** : recrée l'état initial du scénario courant. C'est une commande de débogage, pas une règle de gameplay.

La scène ne contient aucune règle : elle convertit les pixels en cases, transmet les ordres et affiche les résultats. Le déplacement est instantané. Dans le scénario 2, c'est le moteur qui décide si la case située derrière le mur reste atteignable par un autre chemin, et par lequel.

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

### macOS (six essais manuels déclarés conformes par le propriétaire ; non reproduits de façon indépendante)

Le 23 novembre 2026, le propriétaire a déclaré conformes six essais manuels du prototype sous macOS. C'est un retour d'utilisateur, et non une reproduction indépendante : ni la version de macOS, ni les commandes exactes employées ne sont connues ici. Les essais déclarés conformes sont les suivants :

1. grille 5 × 5 ;
2. case (3,2) barrée ;
3. état initial ;
4. déplacement vers (2,4) ;
5. refus d'une destination inaccessible ;
6. touche R.

Ces essais portent sur le prototype du lot 1D, avant l'ajout des scénarios 2 et 3 par le lot 1F. Ces deux scénarios et les touches 1, 2 et 3 n'ont pas été essayés sous macOS.

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
4. le retour au scénario 1 par la touche 1, transmise comme par un clavier AZERTY (« & »), depuis un état déplacé et un chemin affiché.

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

**Essais non effectués pour le lot 1F**, au moment de sa publication :
- **macOS :** aucun essai des scénarios 2 et 3 ni des touches 1, 2 et 3. Les six essais déclarés par le propriétaire portent sur le prototype du lot 1D.
- **Écran réel :** aucun essai, sous aucun système (Linux, macOS ou Windows). Le rendu n'est connu que par des captures automatiques sous affichage virtuel (Xvfb).
- **Clavier et souris physiques :** aucun essai. Les entrées sont simulées par le contrôle fumée et, lors de la relecture, par des événements X11 sous Xvfb.

**Ce qui est vérifié, et ses limites :**

- **Linux x86_64 :**
  - vérifié en mode headless, en local et dans la CI ;
  - vérifié sous Xvfb en local, avec le rendu logiciel OpenGL 3 de Mesa ;
  - jamais essayé sur un écran réel ni avec une souris physique.
- **Scénarios 2 et 3 (lot 1F) :**
  - vérifiés en local, par le contrôle fumée en mode headless et par des captures sous Xvfb ;
  - pas encore dans la CI au moment du lot 1F ;
  - aucune validation manuelle, sur aucun système.
- **Touches 1, 2 et 3 :**
  - vérifiées par des événements simulés : la touche 2 par son seul libellé ; les touches 3 et 1 comme un clavier AZERTY les transmet (libellé « " » ou « & », position de la touche) ;
  - lors de la relecture du lot, aussi par de vrais événements X11 sous Xvfb, avec une disposition AZERTY imitée ;
  - jamais avec un clavier physique.
- **macOS :** six essais manuels déclarés conformes par le propriétaire le 23 novembre 2026, sur le prototype du lot 1D. C'est un retour d'utilisateur, non reproduit de façon indépendante. Le contrôle fumée en ligne de commande et `gtimeout` n'y sont pas vérifiés.
- **Windows :** aucun essai.
- **CI :** compilation, format et contrôle fumée en mode headless seulement ; ni affichage, ni export.
- **Export :** aucun export de jeu n'est testé.
