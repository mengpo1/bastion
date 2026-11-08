# BASTION — Mandat LOT-2A v1.0
## Étude du déplacement tactique (sans gameplay)

**Statut : PRÉPARÉ — exécution non autorisée par la seule publication du présent document.**  
**Dépôt :** `mengpo1/bastion`  
**Mandat publié sur :** `orchestration/mandats`, `docs/mandates/BASTION-MANDAT-LOT-2A-v1.0.md`  
**Base attendue :** `main`, commit `8b1bc3f09b8d1e2b3d15df0ad3ebb6fecc0798bd` (à revérifier au démarrage)  
**Branche proposée :** `research/lot-2a-mouvement-tactique`

## 1. Objet

**Étudier, sans implémenter, le déplacement tactique à pied dans OXCE 8.7.1** afin de présenter au propriétaire une première mécanique de Bastion à arbitrer. Le propriétaire a autorisé **le choix du déplacement tactique comme premier sujet d'étude**, pas encore ses règles.

**Référence obligatoire :** `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, règles `xcom1`, options par défaut, aucun mod, conformément à `docs/references/OXCE-BASELINE.md`.

**Règle première : simplicité.** Ne pas explorer ou reproduire tout OXCE : commencer par un déplacement élémentaire sur une carte tactique, en distinguant ce qui doit être décidé plus tard.

## 2. Travail d'analyse limité

Examiner dans le code, les fichiers de règles et, si possible, par un test observable d'OXCE à la référence figée :

1. **Représentation de la position et des cases :** coordonnées, voisinage horizontal ; statut des déplacements diagonaux et leur éventuel coût.
2. **Déplacement et coût :** unités de temps (TU), coût par pas, terrain et modes pertinents pour une unité se déplaçant à pied ; conduite à tenir lorsque les TU manquent.
3. **Franchissabilité et occupation :** murs, obstacles, unités déjà présentes, chemins bloqués et destinations invalides.
4. **Trajet et exécution :** sélection d'une destination, calcul de chemin, mouvement pas à pas, arrêt ou interruption, uniquement ce qui est nécessaire pour comprendre le comportement de référence.

**Limites explicites de cette première étude :** les escaliers, niveaux multiples, vol, sauts, unités de grande taille, portes complexes, feu de réaction, visibilité, animations et interface détaillée sont **à signaler comme sujets connexes ou inconnus**, sans chercher à les spécifier intégralement dans ce lot. Si l'un de ces sujets conditionne une réponse, l'indiquer et proposer un arbitrage, sans supposer.

**Méthode :** chaque affirmation de comportement cite son origine exacte (chemin, fonction/ligne, commit, donnée, ou observation reproductible). Distinguer **vérifié dans le code**, **observé à l'exécution**, **inférence** et **non vérifié**. Un comportement seulement lu dans le code n'est pas annoncé comme validé par une exécution. Les valeurs de TU ou de diagonale ne sont jamais inventées.

**Propriété intellectuelle :** ne copier aucun code, donnée, règle YAML ou asset OXCE dans Bastion. Seules des observations, reformulations et références courtes sont permises dans le rapport, conformément à la décision D4.

## 3. Livrable de conception

Rédiger `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md` avec :

- un tableau court **« question / comportement OXCE / preuve / limites / décision à prendre »** ;
- quelques scénarios précis de comportement attendu (cas normal, destination bloquée, TU insuffisantes, diagonale si applicable), en signalant ceux qui n'ont pas été exécutés ;
- **une proposition de périmètre minimal pour `MEC-0001`** : déplacement élémentaire à pied, premier système candidat de Bastion ;
- les points sur lesquels Bastion devra choisir de **reproduire la référence ou modifier volontairement** son fonctionnement, sans préjuger du choix du propriétaire ;
- les fonctionnalités à reporter explicitement.

**Ne créer aucune fiche `MEC-0001` dans le registre.** Le document présente un projet de décision, pas une décision acceptée. Aucun gameplay ne peut être implémenté à ce stade.

## 4. Deux harmonisations documentaires déjà décidées

Dans cette même PR documentaire, corriger **seulement** deux formulations héritées, conformément aux décisions antérieures du propriétaire :

1. Dans `docs/references/OXCE-BASELINE.md`, remplacer la règle « Utiliser OXCE comme référence d'une mécanique exige une décision au statut “Validée” dans `docs/gameplay/GAMEPLAY-DECISIONS.md` » par une règle cohérente avec le registre : **une fiche `MEC` exige une décision explicite, datée et « acceptée » du propriétaire** ; distinguer le statut de décision du champ de classification `MODIFICATION-VALIDEE`.
2. Dans `docs/references/OXCE-BASELINE.md` et `CLAUDE.md` §4, remplacer la formulation laissant ouverte la copie après audit par l'interdiction claire décidée en D4 : **aucune reprise de code, données ou assets OXCE ou X-COM** dans Bastion. Conserver l'indication que les licences sont à examiner si la politique devait être réexaminée ultérieurement, sans suggérer que la reprise est actuellement autorisée.

Ces retouches sont **documentaires** ; ne toucher à aucune autre règle ou au harnais. En cas d'incompatibilité inattendue avec les décisions existantes, **arrêter et demander un arbitrage**.

## 5. Fichiers autorisés

- `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md` — **nouveau rapport d'étude**.
- `docs/references/OXCE-BASELINE.md` — **deux seules harmonisations du §4**.
- `CLAUDE.md` — **une seule harmonisation de la règle de propriété intellectuelle (§4)**.

**Aucun autre changement**. Ne modifier ni `docs/gameplay/GAMEPLAY-DECISIONS.md`, ni code C#, ni Godot, ni CI, ni scripts de harnais, ni décisions techniques. Ne créer aucune dépendance ni nouvel outil. Ne pas enregistrer comme validée une mécanique simplement examinée.

## 6. Gouvernance et contrôles

- Avant tout : `git fetch origin main`, vérifier la branche et l'absence d'avancement imprévu de `main` ; lire ce mandat **directement sur `orchestration/mandats`** sans le recopier ou l'archiver.
- Si le propriétaire autorise explicitement ce mandat, créer `research/lot-2a-mouvement-tactique` à partir de `main`.
- Faire réaliser une **revue indépendante en lecture seule** portant sur les sources OXCE, les faits contre les inférences, les limites, la cohérence de D4 et l'absence de décisions implicitement approuvées.
- Contrôler le diff pour les **trois fichiers autorisés** et `git diff --check`. Les tests C# ne sont pas obligatoires pour un lot documentaire ; signaler précisément ceux qui ont ou n'ont pas été lancés et relever la CI réellement observée.
- **Publication autorisée uniquement après approbation explicite du propriétaire pour l'exécution de ce mandat :** commits et push sur la seule branche `research/lot-2a-mouvement-tactique` ; PR **en brouillon** vers `main`. Aucun push direct sur `main`, aucune fusion, aucune réécriture de l'historique.
- Informer le propriétaire à la fin : chemin GitHub du rapport, branche, commit, PR, état réel de la CI ; la revue ChatGPT n'est pas automatique.

## 7. Arrêt

Le lot est terminé à la publication du **rapport d'étude et des deux corrections documentaires**. S'arrêter et **attendre le choix du propriétaire pour MEC-0001**. Ne programmer aucun déplacement et ne fusionner aucune PR.
