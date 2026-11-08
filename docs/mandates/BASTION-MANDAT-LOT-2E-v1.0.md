# BASTION — Mandat LOT-2E v1.0
## Étude de référence OXCE : déplacements verticaux et chutes

**Statut : PRÉPARÉ — exécution et publication non autorisées par la seule présence de ce mandat.**  
**Dépôt :** `mengpo1/bastion`  
**Branche de référence des mandats :** `orchestration/mandats`  
**Base attendue :** `main` au commit `4c884fb5da7d2bb9def4ba24c188f6ef8b40a7ad` ; vérifier avant exécution.  
**Branche de travail proposée :** `research/lot-2e-verticalite-oxce`.

## 1. Objet et périmètre

Étudier **sans modifier le gameplay** les comportements de référence d'OpenXcom Extended (OXCE) pour :
1. **Escaliers** : montée et descente, terrain en pente, changement de niveau, cases de départ/d'arrivée, coûts et limites.
2. **Échelles** : franchissement vertical, conditions (position, orientation, pieds/étage), coût en TU et énergie.
3. **Élévateurs / grav-lifts** : mécanisme réellement présent dans OXCE, déplacements entre niveaux, conditions et coûts ; **ne pas supposer qu'il s'agit d'un ascenseur mécanique** ni de l'ascenseur envisagé pour Bastion.
4. **Chutes** : entrée dans le vide, cases sans plancher, déclencheurs involontaires, éventuelle chute volontaire et son contrôle utilisateur, arrêt/atterrissage, collision avec unités, nombre de niveaux.
5. **Conséquences des chutes** : **vérifier explicitement** s'il existe des dégâts de chute dans OXCE **et, si oui seulement**, les déclencheurs, formule, seuil de hauteur, dégâts cumulés, éventuelle dépendance aux caractéristiques (Force, santé, armure), poids total et objets. Si aucun calcul n'est trouvé, consigner « aucun calcul identifié dans le périmètre examiné » avec les recherches menées, sans conclure à une absence universelle.
6. **Coûts et interruptions** : TU, énergie, mécanismes de paiement et arrêt en mouvement vertical et en chute ; comparaison selon marche normale, unités volantes, taille 1, règles par défaut.
7. **Portée du moteur et des données** : différencier fonctionnalités du moteur OXCE, terrains réellement disponibles dans le jeu de règles `xcom1` sans mods, comportements non activés et extrapolations.

**Ce lot ne tranche aucune règle de MEC-0001**, n'inscrit aucune décision dans les registres et ne code ni mécanique, ni tests de gameplay, ni interface.

## 2. Référence figée

- Projet : `MeridianOXC/OpenXcom`, branche d'origine `oxce-plus` indicative.
- **Commit immuable** : `441cae1b071d249d40a223858cb6bd07fd5d791b` (OXCE 8.7.1).
- Règles : `xcom1` (UFO: Enemy Unknown), options par défaut à ce commit, aucun mod.
- Registre : `docs/references/OXCE-BASELINE.md` ; étude précédente : `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`.
- **D4** : ne reprendre ni code, ni données, ni assets d'OXCE/X-COM ; documenter les comportements et les références de code, sans copier des implémentations.

### Pistes de lecture déjà repérées — non exhaustives

Pistes **vérifiées comme existantes** par lecture du code au commit figé ; elles **ne prouvent pas** encore les comportements complets :

- `src/Battlescape/Pathfinding.cpp:100-145` : résolution des destinations, escaliers et absence de plancher.
- `src/Battlescape/Pathfinding.cpp:246-765` : transitions de niveau, test des escaliers, échelles, `GravLift`, coûts.
- `src/Battlescape/Pathfinding.cpp:1017-1178` : `canFallDown`, `isOnStairs`, transitions `GravLift` et échelles.
- `src/Battlescape/UnitWalkBState.cpp:125-185` et `:270-389` : déclenchement de la chute et paiement de pas.
- `src/Battlescape/UnitFallBState.cpp` : gestion de la chute, à lire en entier.
- `src/Savegame/Tile.cpp`, `src/Savegame/BattleUnit.cpp`, `src/Battlescape/TileEngine.cpp`, `src/Mod/Armor.cpp` et leurs en-têtes : à explorer si nécessaire.

**Recherches obligatoires sur le reste du code** : `fallDamage`, `falling`, `gravity`, `height`, `noFloor`, `hasLadder`, `gravLift`, `climb`, `hit`, `applyDamage` et variantes/cas pertinents. Des noms anglais apparents ne constituent pas en eux-mêmes la preuve d'une mécanique.

## 3. Questions structurantes à traiter dans le rapport

Pour **chacun** des moyens de déplacement, préciser :
- Déclencheur, conditions d'accès et cheminement (y compris passage d'un étage à l'autre).
- Coût TU/énergie et moment de consommation ; variations suivant l'unité ou les données.
- Obstacles et unités rencontrées, annulation, interruption, visibilité si pertinent.
- Résultat final et cas limites (étage supérieur, étage inférieur, chute de plusieurs étages, absence de destination).
- Différences entre **fonctionnalité prévue par le moteur** et **présence prouvée dans les règles `xcom1` sans mods**.
- Statut de preuve **VC** (vérifié en lecture de code), **OE** (observé en exécution), **INF** (inférence), **NV** (non vérifié). **Ne pas utiliser OE sans test réellement exécuté**.

Comparer ensuite aux **décisions déjà prises** pour Bastion et présentes dans `docs/gameplay/GAMEPLAY-DECISIONS.md` (MEC-0001, N3 à N10), avec quatre catégories : similaire au comportement de référence établi, écart volontaire ou potentiel, non comparable, à vérifier. Une décision déjà acceptée du propriétaire reste acceptée ; cette étude n'a **aucun pouvoir de la changer**.

Ne pas proposer de valeurs finales d'équilibrage et ne pas confondre les exemples hypothétiques avec des valeurs des règles du jeu d'origine.

## 4. Livrable limité

Créer **un seul document** sur la branche de recherche :
`docs/reviews/LOT-2E-VERTICALITE-OXCE.md`.

Structure souhaitée :
1. Résumé exécutif : ce qui est établi et ce qui ne l'est pas.
2. Méthode et périmètre : commit, règles, options, restrictions, recherches effectuées, exécution ou non.
3. Tableau de référence par mécanisme (escaliers, échelles, grav-lifts, chutes, dégâts et charge), avec liens `fichier:lignes` précis, statut VC/OE/INF/NV.
4. Explications pédagogiques des parcours types avec schémas textuels simples si utiles (exemples **explicitement hypothétiques**).
5. Cas limites, ambiguïtés, mécanismes OXCE absents/non établis et dépendances éventuelles aux fichiers terrain.
6. Comparaison avec MEC-0001 **sans décider à la place du propriétaire**.
7. Liste **courte et priorisée** des arbitrages futurs, par importance pour jouer et tester ; distinguer règles déjà décidées et simples paramètres.
8. Vérifications exécutées (preuves, commandes, sorties), limites et compte rendu de la revue indépendante.

**Fichier autorisé unique** : `docs/reviews/LOT-2E-VERTICALITE-OXCE.md`.

**Interdits de modification** : `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/references/OXCE-BASELINE.md`, `docs/decisions/`, `docs/mandates/`, `src/`, `tests/`, `CLAUDE.md`, `.claude/`, `scripts/`, `.github/` et tout autre fichier. Aucun développement ou restructuration.

## 5. Protocole d'exécution et livraison

1. Attendre l'**autorisation expresse du propriétaire** pour exécuter ce mandat, y compris pousser une branche et ouvrir une PR en brouillon. La présence du mandat sur GitHub n'autorise rien.
2. Lire **directement** le mandat depuis `orchestration/mandats` au SHA publié par l'orchestrateur ; ne pas le copier dans la branche de travail.
3. Lancer `git fetch origin main` et vérifier l'état de `main` ; si celui-ci diffère du SHA attendu, arrêter et demander une revue de l'écart.
4. Créer `research/lot-2e-verticalite-oxce` depuis `origin/main`. Étudier le code OXCE au commit figé en lecture seule, sans importer de sources dans Bastion.
5. Produire le rapport ; **ne pas affirmer avoir exécuté OXCE** si seuls les sources ont été étudiées. Si les données du jeu d'origine nécessaires manquent, signaler la limite.
6. Faire relire par un **agent indépendant en lecture seule** le texte et les liens aux passages OXCE, la séparation fait / inférence / inconnu, la fidélité à la politique D4 et la non-modification des décisions de Bastion. Corriger les erreurs avant publication.
7. Vérifier `git status --short`, `git diff --check`, **un seul fichier autorisé**. Tests .NET non requis pour une étude documentaire ; ne pas inventer de résultats.
8. Sous autorisation d'exécution : committer/pousser **seulement** la branche de recherche et ouvrir une **PR en brouillon** vers `main`, sans fusion. Ne pas ajouter de commit, notes ou actions hors du périmètre.
9. Arrêter le travail. Informer brièvement le propriétaire du lien vers la PR, du SHA de branche, du chemin du rapport et de l'état de CI **constaté** ; ChatGPT examinera la PR directement après « Claude a terminé ».

## 6. Condition d'arrêt

Fin du LOT-2E = rapport de recherche publié dans une PR en brouillon, **aucune mécanique enregistrée ou autorisée**. Les décisions de gameplay et un éventuel mandat d'implémentation exigent des accords distincts.
