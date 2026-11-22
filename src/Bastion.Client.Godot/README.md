# Bastion.Client.Godot — prototype technique (lot 1D)

Ce prototype est une scène Godot 2D, vue du dessus, reliée au moteur `Bastion.Simulation`. On y clique sur une case de la zone atteignable, et l'unité s'y déplace selon le résultat du moteur. Il vérifie la liaison entre une interface Godot et la simulation. Ce n'est ni le design final de l'interface, ni une mécanique de gameplay.

## Ce que fait la scène

**Scénario fixe :**
- carte MEC-0003 de 5 × 5 cases de 1 500 mm, sur terrain normal ;
- une case infranchissable en (3,2) ;
- une unité `UnitBody.StandardHuman` en (1,4), orientée N, avec 20 TU et 10 d'énergie.

**Affichage :**
- en vert, la zone atteignable rendue par `ComputeReachability` ;
- en gris foncé barré, la case infranchissable ;
- l'unité est un disque, avec un trait jaune qui indique son orientation ;
- à droite : position, orientation, TU, énergie et dernier résultat.

**Commandes :**
- **clic gauche** sur une case : ordre transmis au moteur par `ExecuteOrder`. L'affichage reprend l'état rendu par le moteur, puis la zone est recalculée. Un ordre refusé ne change rien et affiche le message du moteur.
- **touche R** : recrée l'état initial du scénario. C'est une commande de débogage, pas une règle de gameplay.

La scène ne contient aucune règle : elle convertit les pixels en cases, transmet les ordres et affiche les résultats. Le déplacement est instantané.

## Prérequis

- **SDK .NET 10** (`global.json` du dépôt).
- **Godot 4.7.2 stable .NET**, la version épinglée par `Sdk="Godot.NET.Sdk/4.7.2"` dans `Bastion.Client.Godot.csproj` (T-002, version de référence provisoire). Il faut l'édition « .NET » de Godot, téléchargeable sur la page officielle de la version `4.7.2-stable`. Le contrôle fumée vérifie cette version au lancement. `project.godot` garde le format qu'écrit l'éditeur Godot, pour qu'une ouverture dans l'éditeur ne le modifie pas.
- **Accès à NuGet** (nuget.org) lors de la première compilation, pour les paquets Godot 4.7.2.

## Compilation

Le client **ne fait pas partie de `Bastion.slnx`** : `dotnet build` à la racine du dépôt ne le compile pas, et la CI ne le compile ni ne l'exécute. Le format lancé à la racine ne le contrôle pas non plus.

**Avant tout lancement**, depuis la racine du dépôt, compiler le client en **Debug**. C'est la compilation que Godot charge quand il lance le projet depuis son dossier ; une compilation Release seule ne suffit pas.

```bash
dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj
```

Compilation Release, demandée par le mandat comme contrôle :

```bash
dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --configuration Release
```

## Ouverture et lancement

### Linux (vérifié en mode headless et sous affichage virtuel Xvfb ; pas sur un écran réel)

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

### macOS (non vérifié : aucun essai n'a eu lieu sous macOS)

Avec l'application officielle `Godot_mono.app` 4.7.2 placée dans `/Applications` :

```bash
GODOT=/Applications/Godot_mono.app/Contents/MacOS/Godot
```

Les commandes de compilation et de lancement sont ensuite les mêmes que sous Linux. On peut aussi ouvrir l'application Godot et importer le fichier `src/Bastion.Client.Godot/project.godot`.

## Contrôle fumée

Le contrôle fumée envoie des clics et une touche R à la scène, par le même code que les entrées du joueur. Il compare ensuite l'état de la scène et le texte de son panneau aux résultats du moteur et aux valeurs du mandat. Le dessin de la grille n'est pas contrôlé automatiquement : seules les captures le montrent.

Sans affichage, après la compilation Debug :

```bash
timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test
echo $?
```

Codes de sortie :
- **0** : tous les contrôles réussissent ;
- **1** : au moins un contrôle échoue ;
- **2** : une exception est survenue ;
- **124** (code de `timeout`) : la scène n'a pas démarré le contrôle, par exemple parce que le projet n'est pas compilé en Debug. Godot ne quitterait alors jamais de lui-même ; d'où la limite de temps.

Sous macOS, `timeout` n'existe pas par défaut ; `gtimeout`, du paquet `coreutils` de Homebrew, joue le même rôle (non vérifié).

Avec un affichage, l'option `--capture=<dossier existant>` enregistre une image de la fenêtre après chaque étape. En mode headless, elle est comptée comme un échec, faute de rendu. Sous Linux sans écran, on peut passer par Xvfb :

```bash
timeout 300 xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test --capture=/tmp/captures
```

## Limites

- **Plateformes :** seul Linux x86_64 a été essayé, en mode headless et sous Xvfb avec le rendu logiciel OpenGL 3 de Mesa. Ni un écran réel, ni une souris physique, ni macOS, ni Windows n'ont été essayés.
- **CI :** elle ne compile ni n'exécute ce client.
- **Export :** aucun export de jeu n'est prévu dans ce lot.
