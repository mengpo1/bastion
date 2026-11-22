# BASTION — Mandat LOT-1D v1.0
## Premier prototype visuel Godot connecté à la simulation

**Statut : PRÉPARÉ — exécution non autorisée par le présent document**  
**Dépôt :** `mengpo1/bastion`  
**Branche de travail proposée :** `claude/lot-1d-prototype-godot`  
**Base :** `origin/main` après la fusion de la PR #21, à vérifier par Claude Code au démarrage.  
**Références :** `CLAUDE.md` ; décisions T-001, T-002, T-101 et T-103 ; MEC-0003 ; rapport `docs/reviews/LOT-1C-QUALIFICATION-GODOT-DOTNET.md`.

## 1. Objectif

Créer le **premier prototype technique jouable** de Bastion sous Godot .NET. Il permet de sélectionner une destination sur une grille et d'observer le déplacement d'une unité **exclusivement calculé par le moteur C# `Bastion.Simulation`**.

Ce lot vérifie la liaison entre une interface Godot et la simulation déjà intégrée. Il **ne constitue ni le design final de l'interface ni une nouvelle mécanique de gameplay**.

**Règle fondamentale : simplicité avant tout.** Choisir l'implémentation la plus directe, lisible et suffisante. Ne pas anticiper les fonctionnalités futures.

## 2. Préparation et autorisations

1. Attendre une **autorisation explicite d'exécution** du propriétaire, distincte de ce mandat préparé.
2. Vérifier `git status`, exécuter `git fetch origin main` et établir le SHA exact de départ ; ne pas réutiliser aveuglément un ancien SHA.
3. Créer la seule branche `claude/lot-1d-prototype-godot` depuis `origin/main`. Ne jamais travailler sur `main`.
4. Archiver ce mandat tel que reçu dans `docs/mandates/` et indexer sa provenance et son empreinte SHA-256 dans `docs/mandates/README.md`, conformément au protocole existant. Si seul le texte collé est disponible, indiquer « transcription depuis la conversation ; identité avec le fichier original non vérifiée ».
5. Respecter `CLAUDE.md` et les hooks. Aucun commit, push, PR ou fusion ne découle automatiquement de l'autorisation d'exécution ; la publication requiert l'accord distinct du propriétaire.

## 3. Périmètre technique

- Utiliser **Godot 4.7.2 stable .NET**, identifié dans T-002 et qualifié au lot 1C, en **épinglant cette version dans le projet**. C'est une version de travail provisoire pour ce prototype ; **ne pas transformer T-002 en validation définitive**.
- Utiliser **C# et `net10.0`**.
- Créer un projet Godot indépendant, de nom technique de travail **`Bastion.Client.Godot`**, sous `src/Bastion.Client.Godot/` (ou expliquer un autre chemin avant toute modification).
- Référencer le projet existant `src/Bastion.Simulation/Bastion.Simulation.csproj` par `ProjectReference`. Ne copier aucun code du moteur.
- Garder **`Bastion.Simulation` sans référence à Godot**.
- Utiliser uniquement les API publiques existantes, en particulier `TacticalMapBuilder`, `MovementModel`, `CreateState`, `ComputeReachability`, `ExecuteOrder`, `UnitState`, `GridPosition` et `Direction`.
- Ne pas modifier `Bastion.slnx`, `Directory.Build.props` ou les scripts de CI pour faire entrer artificiellement le projet Godot dans la chaîne de compilation existante. Compiler le client séparément et documenter cette limite ; T-103 reste à examiner dans un lot ultérieur.

## 4. Prototype à réaliser

### 4.1 Scène unique

- Une scène Godot **2D vue du dessus**, avec une grille de **5 colonnes × 5 lignes**. Il s'agit uniquement d'une visualisation provisoire ; aucune orientation définitive de caméra n'est décidée.
- Le modèle de carte reste une carte MEC-0003 de **cases de 1 500 mm** ; convertir ces coordonnées en pixels uniquement pour le dessin et la saisie.
- Terrain plat normal, sans niveaux, sans unités supplémentaires. Placer **une case infranchissable en (3,2)**, visible sur la grille.
- Une seule unité utilisant `UnitBody.StandardHuman`, position initiale **(1,4)**, orientation **N**, **20 TU** et **10 points d'énergie** ; créer son état au moyen de `MovementModel.CreateState`.
- Visuels de débogage simples, dessinés avec les primitives de Godot : cases, obstacle, symbole d'unité et indication de son orientation. Aucun sprite, modèle 3D ou asset sous licence tierce.

### 4.2 Interaction minimale

- Mettre en évidence les cases de la **zone atteignable renvoyée par `ComputeReachability`**, sans en recalculer les règles dans Godot.
- Un **clic gauche** sur une case atteignable adresse un ordre au moteur via **`ExecuteOrder`**. Utiliser le `FinalState` renvoyé pour mettre à jour l'affichage.
- Un clic hors de la carte, sur la case de départ, sur une case infranchissable ou hors de la zone ne provoque pas de déplacement ni de débit. Le refus peut être annoncé par un court message ; aucun chemin de remplacement ne doit être calculé par l'interface.
- Après chaque ordre, recalculer l'affichage de la zone atteignable à partir du **nouvel état** de l'unité.
- Afficher : **position, orientation, TU restantes, énergie restante** et dernier résultat de l'ordre.
- Permettre de **réinitialiser le scénario avec la touche R**, en recréant l'état initial validé ; ceci est une commande de débogage et **non une règle de gameplay**.
- Le déplacement peut être **instantané** à l'écran. Ne pas créer d'animation, de moteur de trajectoire ou de simulation parallèle dans Godot.

### 4.3 Code

- Préférer une scène et un petit nombre de scripts C# clairement nommés. N'introduire ni DI, ni framework UI supplémentaire, ni système d'événements générique, ni bus de messages, ni machine à états artificielle.
- La logique de la scène convertit uniquement les coordonnées souris/cases, transmet les commandes et affiche les résultats ; elle ne choisit ni chemins, ni coûts, ni collisions.
- Ne pas inventer de règles de tour, de récupération des ressources, de visibilité ou de sélection d'autres unités.
- Les textes affichés peuvent être simples et localisables ultérieurement ; ne pas développer un système de traduction dans ce lot.

## 5. Vérifications attendues

**A — Intégrité de l'architecture**
- `Bastion.Simulation` compile sans dépendance Godot ; aucun fichier existant sous `src/Bastion.Simulation/` ni sous `tests/Bastion.Simulation.Tests/` n'est modifié.
- Le projet Godot compile explicitement en `net10.0` avec la référence de projet vers la simulation.

**B — Contrôles de comportement**
- À l'initialisation : unité en (1,4), N, 20 TU, 10 énergie ; la zone affichée provient du moteur.
- Un clic sur **(2,4)** depuis l'état initial conduit à **(2,4), E, 16 TU, 8 énergie** ; comparer au résultat réel de `ExecuteOrder`.
- Une case bloquée et une case hors zone ne changent ni la position, ni l'orientation, ni les ressources.
- Deux ordres successifs utilisent bien les ressources restantes ; la zone est mise à jour entre les ordres.
- La touche R restitue l'état initial du scénario de démonstration.

**C — Exécution Godot**
- Si le binaire Godot est disponible dans l'environnement d'exécution, démarrer réellement le projet **en mode headless** et exécuter un contrôle fumée automatique de l'intégration qui se termine explicitement avec un **code 0 en cas de succès et non nul en cas d'échec**. Réutiliser le même code d'application, pas une deuxième simulation factice.
- Si l'affichage graphique est accessible, réaliser un contrôle manuel de la grille et des clics et rapporter les observations. **Ne pas déclarer le rendu ou les clics graphiques validés lorsqu'ils n'ont pas été testés.**
- Fournir une notice de démarrage reproductible sur **macOS et Linux** : prérequis, commande de compilation explicite du projet, ouverture du projet avec Godot 4.7.2 .NET, commandes de contrôle. Les instructions macOS restent **non vérifiées** tant qu'aucun essai macOS n'a eu lieu.

**D — Non-régression Bastion**
- `dotnet restore`, `dotnet build --configuration Release`, `dotnet test --configuration Release`, `dotnet format --verify-no-changes`, `bash scripts/harness/test-hooks.sh` ; rapporter les sorties et codes réels.
- Compiler séparément le client Godot : `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --configuration Release` (adapter uniquement si le chemin convenu diffère).
- Le fait que la CI actuelle ne compile ni n'exécute Godot doit rester **explicitement signalé** ; ne pas annoncer une qualification CI du client sans l'avoir mise en place et exécutée.

## 6. Hors périmètre

- Gameplay hors de MEC-0003, dont MEC-0001 et MEC-0002 non acceptées dans leur ensemble.
- Nouveaux mouvements, changements de coûts, collisions physiques Godot, personnages multiples, tirs, inventaire, tours, IA et animations.
- Architecture multi-scènes, édition de niveau, chargement externe de cartes, modding, traductions, sprites, modèles 3D, sons, sauvegardes et export de jeu.
- Modification des registres protégés, du harnais, des workflows GitHub, de `Bastion.slnx`, de `Directory.Build.props` ou du moteur de simulation.
- Toute affirmation de compatibilité macOS/Windows ou de rendu graphique sans essai réel.

## 7. Livrables et revue

1. Projet Godot minimal exécutable et fichier(s) d'instructions de lancement sous son dossier, avec les limites de plateforme.
2. Mandat archivé et indexé selon le protocole.
3. Rapport `docs/reviews/LOT-1D-PROTOTYPE-GODOT.md` : fichiers, commandes, résultats observés, contrôles non exécutés, réserves, et bilan d'architecture.
4. Relecture indépendante **ciblée** du diff : périmètre, absence de règles dupliquées, dépendances, risques et tests ; ne pas entreprendre de refactoring spéculatif.
5. Présentation au propriétaire du diff final et du rapport **avant toute publication**.

**Aucun commit, push, PR ou fusion sans autorisation distincte.** Fin du lot après les livrables ; ne pas engager le lot suivant.
