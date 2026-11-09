# BASTION — Mandat LOT-2F v1.0
## Formalisation technique et qualification documentaire de MEC-0001

**Statut : PRÉPARÉ — NON ENCORE AUTORISÉ À L'EXÉCUTION**  
**Dépôt :** `mengpo1/bastion`  
**Base :** `origin/main` à vérifier par `git fetch origin main` au démarrage  
**Branche proposée :** `docs/lot-2f-mec-0001-specification`  
**Nature :** étude et documentation uniquement, sans implémentation  
**Référence OXCE :** `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` (version de référence 8.7.1)  
**Origine des arbitrages supplémentaires :** déclarations explicites du propriétaire dans la conversation Bastion du 9 novembre 2026, à retranscrire fidèlement ; elles ne sont pas encore inscrites au registre protégé sur `main`.

## 1. Objet du mandat

Produire une spécification technique contrôlable des déplacements verticaux, sauts offensifs, chutes, esquives et collisions prévus dans MEC-0001, en réunissant :

- les sous-décisions historiques S1–S12, Z1, N1–N14 figurant dans `docs/gameplay/GAMEPLAY-DECISIONS.md` ;
- les observations du rapport `docs/reviews/LOT-2E-VERTICALITE-OXCE.md` ;
- les décisions de conception validées par le propriétaire après LOT-2E, puis les trois blocs consolidés validés le 9 novembre 2026 ;
- une matrice de tests futurs permettant de vérifier les comportements.

**Ne pas déduire que toute MEC-0001 est prête à implémenter :** le registre actuel couvre également la marche, les portes, les escaliers, échelles, ascenseurs, les coûts et le brouillard, dont des détails demeurent ouverts. La validation conversationnelle des blocs de sauts et dégâts doit être tracée, sans inventer des validations pour ces autres sujets.

## 2. Règles impératives

1. Lire `CLAUDE.md`, `docs/mandates/README.md`, le registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/references/OXCE-BASELINE.md` et les rapports LOT-2A à LOT-2E pertinents.
2. **Ne pas modifier** `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/decisions/TECHNICAL-DECISIONS.md`, `docs/references/`, `CLAUDE.md`, le harnais, le code de simulation ou les tests exécutables. Une mise à jour du registre protégé exige un mandat et une autorisation explicites distincts.
3. Ne pas recopier de code, données ou assets d'OXCE/X-COM (décision D4). Référencer le comportement et citer les emplacements du code source si vérifiés.
4. Ne pas confondre « observé en exécution », « établi par lecture du code », « inféré » et « propre à Bastion ». Aucune fidélité à OXCE ne peut être prétendue sans preuve comportementale appropriée.
5. Ne modifier aucun paramètre accepté et ne combler aucune lacune par une règle implicite. Les propositions techniques sont clairement étiquetées **non validées**.
6. Un relecteur indépendant doit examiner les livrables en lecture seule, sans s'attribuer la validation du propriétaire.
7. Aucun `push`, aucune PR, aucune fusion et aucune écriture sur `main` sans autorisation explicite, limitée au lot et à la branche correspondante. Le présent fichier n'accorde pas cette autorisation.

## 3. Règles de conception à retranscrire

Les éléments ci-dessous constituent une **synthèse de travail**, à comparer intégralement avec les décisions enregistrées et la conversation fournie par le propriétaire avant transcription officielle.

### 3.1 Marche et verticalité déjà documentées

- Huit directions ; coût diagonal de la case d'arrivée ×1,5, arrondi à l'inférieur ; diagonale permissive lorsque l'un des deux passages orthogonaux est ouvert ; une unité adjacente n'est pas un obstacle de coin.
- Terrain en cases et murs distincts ; positions `(x,y,z)` ; escaliers, échelles et ascenseurs prévus.
- Zone atteignable selon les TU et la connaissance du terrain ; impossibilité de sélectionner normalement une destination hors zone ; trajet en cases actuellement visibles ou déjà explorées ; interruption et révélation lorsqu'un obstacle ou une unité auparavant inconnus sont rencontrés.
- Une case occupée est infranchissable pour la marche normale. Les exceptions propres aux sauts offensifs doivent être explicitement circonscrites.
- Surcharge selon OXCE : poids d'armure et inventaire, rapport Force/charge sur la récupération des TU, sans seuil d'immobilisation additionnel ni surcoût spécifique par pas.

### 3.2 Saut offensif et choix de destination

- Une attaque par saut nécessite au moins un étage de dénivelé vers le bas.
- Une destination peut être choisie librement parmi les cases atteignables. Une case déjà explorée mais non actuellement visible peut être visée à l'aveugle ; une case jamais explorée ne peut pas être choisie.
- Une unité ennemie cachée dans la case ciblée peut être percutée et révélée. Les alliés et neutres **identifiés** ne peuvent pas être volontairement ciblés ; s'ils sont cachés sur la case visée à l'aveugle, la collision reste possible.
- Le bonus offensif s'applique également si une attaque à l'aveugle percute un allié ou un neutre caché.
- Coût additionnel : `max(1, floor(0,20 × TU_max))`, en plus du déplacement ; dépensé à l'engagement, même si l'attaque échoue ou si la cible esquive. TU insuffisantes : attaque impossible.
- Bonus offensif sur les dégâts infligés à la cible : `×1,25`, après le plafond des dégâts de base et avant le tirage aléatoire. Aucun bonus sur les blessures de l'attaquant.

### 3.3 Modèle physique des sauts

- Gravité configurable selon l'environnement, initialement `1 g` (`≈ 9,81 m/s²`).
- Modèle balistique simplifié avec impulsion verticale initiale et gravité. Pour une même unité et une même action, l'impulsion verticale initiale est constante ; la composante horizontale s'adapte à la destination dans les limites des capacités de saut.
- À 1 g, élévation maximale de référence : **¼ de la hauteur d'un étage**. À gravité moindre, élévation plus forte ; à gravité plus élevée, élévation moindre.
- À 1 g et pour une descente d'un étage, portée horizontale de référence : **2 cases selon Manhattan** (`|Δx|+|Δy|`). La portée dépend ensuite de la gravité et du dénivelé réel ; les règles exactes de conversion doivent être formalisées.
- Arc calculé d'après les conditions de départ et la destination, sans contournement adaptatif des obstacles ; un obstacle bas est franchissable si **tout le volume de l'unité** le survole. Un mur, sol ou plafond qui intersecte ce volume bloque le trajet.
- Obstacle connu bloquant : action interdite avant engagement. Obstacle non détecté : l'action peut s'engager, puis être interrompue à l'impact ; l'obstacle est révélé à cet instant.

### 3.4 Esquive et collisions entre unités

- Collision possible après chute accidentelle ou saut volontaire. Les deux unités peuvent subir des dégâts distincts et de l'étourdissement.
- Esquive **automatique** seulement si la cible voit **actuellement** l'unité qui tombe, possède les TU du déplacement requis et dispose d'une case voisine libre et accessible.
- Choix aléatoire d'une case valide ; probabilité de réussite fondée sur **Réactions** et un bonus de `+5 points de pourcentage par niveau traversé`, bornée à `[0,100]`. Formulation conversationnelle provisoire : `clamp(Réactions + 5 × |z_départ - z_arrivée|, 0, 100)` ; vérifier que « niveaux traversés » et le repérage exact de `z` concordent.
- Esquive réussie : déplacement sur la case choisie et paiement des TU normales du pas ; la cible ne subit pas le choc, et l'attaquant termine par une chute au sol.
- Esquive échouée : cible immobile, **aucune TU dépensée pour l'essai**, collision résolue.
- L'influence du poids porte sur les dégâts des **deux** unités. Leur poids relatif influe sur les résultats sans déterminer mécaniquement laquelle est la plus blessée.

### 3.5 Dégâts : paramètres initiaux acceptés

- Chute blessante possible dès **1 étage** : ceci remplace l'ancienne formulation N7 sur l'absence de dégâts pour une petite chute. La nature du sol n'influence pas les dégâts.
- Dégâts de base à 1 étage : **8** ; premier incrément entre le 1er et le 2e étage : **6** ; chaque incrément ultérieur est multiplié par **1,35**. La progression porte sur les incréments, pas sur une formule quadratique.
- Expression de référence à documenter, **avant arrondi** : pour `n≥1` étages, `B(n)=8 + 6 × Σ(k=0..n-2) 1,35^k`, somme vide pour `n=1`. Aucun arrondi numérique non validé ne doit être introduit silencieusement.
- Plafonds appliqués **avant l'aléatoire** : chute au sol **70**, unité qui tombe dans une collision **60**, unité percutée **80**, impact contre un obstacle **70**.
- Variation aléatoire de type **explosion OXCE**, `50–150 %` de la puissance soumise au tirage ; le moteur comporte également des règles distinctes de conversion finale en santé et étourdissement. La distribution et le comportement des valeurs entières doivent être vérifiés au commit figé.
- En collision volontaire avec une unité, le bonus `×1,25` est appliqué **après le plafond**, avant l'aléatoire. Les facteurs de poids pertinents et la protection des armures interviennent ensuite selon l'ordre accepté ; l'ordre numérique précis et le type de dégâts OXCE demeurent à formaliser.
- Pour un choc contre un obstacle : puissance d'impact commune avant la résolution des effets sur l'unité et le terrain, influencée par la vitesse réelle au point de contact et par le poids total `M` (équipement inclus). Référence universelle **80 kg** ; facteur `min(M/80,3)`, sans minimum artificiel. Ceci **ne constitue pas** la formule du rapport de masses entre deux unités.
- La vitesse **dirigée vers la surface heurtée** doit être distinguée de la vitesse tangentielle. Début, milieu et fin de course sont identifiés pour le diagnostic ; aucune prime ou pénalité arbitraire liée à une phase n'est autorisée.
- L'impact peut endommager ou détruire un obstacle destructible, en réutilisant les règles de résistance/destruction du terrain d'OXCE ; un obstacle indestructible ne l'est pas.
- À l'impact contre un obstacle, le saut est interrompu même si l'obstacle est détruit. Ensuite, si l'unité est sans support, elle chute **verticalement** depuis la position de contact. Dégâts d'impact et de chute consécutive sont résolus **séparément**.

### 3.6 Informations et interface

- N'afficher que les informations connues du joueur ; aucune divulgation de la présence d'une unité ou d'un obstacle cachés dans les prévisualisations.
- Prévisualiser destination, trajectoire estimée et coût en TU, dans les limites de la connaissance courante.
- Résoudre chronologiquement événements de trajectoire, impacts, esquives, atterrissages, pertes de support et collisions ultérieures.
- Les cas de destination devenue occupée, d'unités multiples sur le trajet et d'atterrissage sans support doivent être identifiés explicitement : ne pas leur inventer un résultat automatique faute de validation.

## 4. Travail demandé

### A — Matrice de traçabilité

Pour chaque règle : identifiant stable, source documentaire ou citation exacte de l'arbitrage du propriétaire, statut (**validé / proposition technique / ouvert / contredit**), catégorie (**référence OXCE / adaptation Bastion / non établi**), règle courante et cas de test correspondant.

Signaler les décisions historiques remplacées, notamment N7 et la portée initialement fixe de deux cases, désormais référence à 1 g et à un étage de descente.

### B — Spécification mathématique

Fournir définitions, unités, hypothèses explicites et expressions des trajectoires, durées de vol, vitesses au contact, collisions géométriques et dégâts. Ne pas attribuer d'échelle métrique aux cases ou aux étages sans validation du propriétaire. Pour les calculs nécessitant une telle échelle, utiliser des symboles (`H`, largeur de case, etc.) et montrer les invariants attendus.

**Repères à vérifier, sans imposer de nouveaux choix :**

- À accélération constante `g > 0`, l'élévation du centre de référence suit `h(t)=v_z0 × t − ½gt²`; si le saut culmine à `H/4` à `g0`, alors `v_z0²/(2g0)=H/4`.
- Distinguer temps de vol physique, distance géométrique et limite de portée selon Manhattan ; une simplification de l'un ne doit pas modifier silencieusement les deux autres.
- Décrire la collision d'un **volume**, pas d'un point, avec les éléments de terrain et les unités ; tenir compte du premier contact sur la trajectoire.
- Clarifier comment l'impact en montée, au sommet ou en descente se rapporte à la vitesse normale à la surface, sans appliquer de coefficient « début/milieu/fin » non décidé.

### C — Mécanismes OXCE

Vérifier par lecture du commit figé : coûts de changement de niveau, chutes, ordre de dégâts/armure/étourdissement, tirage « explosion », résistance des terrains et traitement des unités sous une chute. Séparer strictement la mécanique lue dans OXCE des comportements nouveaux décidés pour Bastion. Consigner les points non vérifiés expérimentalement.

### D — Matrice de tests futurs

Construire des tests identifiés, avec préconditions, déclencheur, résultat attendu, provenance de l'attendu et statut d'exécutabilité. Inclure au minimum :

- Marches à huit directions, diagonales permissives et murs ; TU insuffisantes ; surcharge ; brouillard et obstacle découvert.
- Sauts d'une case et de deux cases Manhattan à 1 g sur un dénivelé d'un étage ; diagonale `(1,1)` ; cas de portée augmentée/diminuée par la gravité et par le dénivelé.
- Élévation `¼ d'étage` à 1 g, plus haute à 0,5 g et plus basse à 2 g, sous réserve de l'échelle définie.
- Obstacles connus ou cachés ; obstacle bas survolé ; mur/plafond coupant le volume ; impact en phase ascendante, près du sommet et descendante.
- Cible visible, cachée, ennemie, alliée et neutre ; case explorée vide ; case jamais explorée refusée.
- Esquive possible/impossible, 0 %/100 %, TU suffisantes/insuffisantes ; dépense des TU en réussite et non-dépense en échec.
- Coût offensif `20 %` arrondi à l'inférieur avec minimum `1`, coût payé même si la cible esquive ou la case est vide.
- Dégâts du premier étage, incréments géométriques, quatre plafonds, variation 50–150 %, bonus offensif et ses exceptions ; résistance du terrain ; poids 40/80/160/240/320 kg contre obstacle.
- Collision en chaîne : choc contre obstacle, destruction éventuelle, chute verticale consécutive, impact au sol ou sur une unité.
- Tests négatifs de **non-fuite d'information** pour terrain et occupants cachés.

Les cas dont le résultat exact dépend d'un paramètre non décidé doivent être marqués **bloqués**, et non simulés à l'aide d'une valeur inventée.

### E — Revue de cohérence et points ouverts

Rassembler les difficultés dans un tableau unique : **question**, **règles concernées**, **risque**, **choix nécessaires**, **proposition facultative**, **caractère bloquant ou non**.

Vérifier en particulier :

1. Taille physique des cases/étages et repère des positions/volumes.
2. Cohérence entre trajectoire balistique continue, vitesse horizontale adaptable et distance de Manhattan.
3. Portée et trajectoires lorsque `g=0` ou lorsque la gravité sort des plages prévues : **aucun comportement n'a été arbitré pour ces cas**.
4. Définition précise des phases début/milieu/fin pour l'affichage ou le diagnostic ; aucun effet sur les dégâts sans validation.
5. Arrondis des dégâts intermédiaires, du tirage et du produit des coefficients ; comportement aux valeurs extrêmes.
6. Formule atténuée du **rapport de poids entre deux unités**, distincte de `min(M/80,3)` contre les obstacles.
7. Type de dégâts et zones d'armure dans le pipeline OXCE, et conditions exactes d'étourdissement.
8. Conversion d'un choc en puissance brute : vitesse normale à la surface, vitesse initiale et dénivelé réellement parcouru ; éviter le double comptage d'une même contribution.
9. Résolution des collisions multiples, des cases occupées devenant libres, des grandes unités et des cas sans support.
10. Portée des décisions globalement validées le 9 novembre par rapport aux autres sous-domaines historiques encore ouverts de MEC-0001.

## 5. Livrables autorisés

Sur la branche du lot **uniquement après autorisation explicite d'exécution** :

1. `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` — spécification, traçabilité, formules, preuves OXCE et tableau des ambiguïtés.
2. `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md` — matrice de scénarios, sans tests exécutables.
3. Archivage **octet pour octet** du mandat transmis par le propriétaire dans `docs/mandates/` et mise à jour minimale de son index SHA-256, conformément à la convention actuelle, sans en réécrire le contenu.

**Hors périmètre :** modification du registre des décisions gameplay, décision globale « acceptée » dans GitHub, code C#, scènes Godot, exécution de tests de gameplay, changement de harnais, nouvelle architecture, changement d'équilibrage.

## 6. Vérifications et revue indépendante

- Actualiser `origin/main` avant tout travail et confirmer la branche de base.
- Vérifier le périmètre du diff et l'absence de modification des fichiers protégés.
- Contrôler les liens et références OXCE, les formules, les libellés de statut et les cas de test.
- Exécuter les contrôles documentaires pertinents (`git diff --check`, recherche de blancs de fin de ligne, cohérence des renvois), avec commandes, sorties et codes de retour consignés.
- Mandater un relecteur indépendant, en **lecture seule**, avec rapport des constats bloquants, importants et mineurs. Corriger les défauts dans le périmètre du lot, ou signaler les blocages nécessitant un choix du propriétaire.
- Si une publication est **autorisée séparément** : pousser uniquement la branche dédiée et ouvrir une PR **en brouillon** vers `main`, fournir URL, SHA, état réel de CI. Aucune fusion automatique.

## 7. Conditions de clôture

Le lot documentaire est clos si :

- toutes les décisions pertinentes sont traçables, avec contradictions historiques identifiées ;
- aucune règle propre à Bastion n'est attribuée par erreur à OXCE ;
- les formules validées sont transcrites et les formules manquantes sont explicitement classées ;
- la matrice de tests couvre les scénarios ordinaires et les cas limites ;
- les ambiguïtés bloquantes sont isolées et non résolues par conjecture ;
- le périmètre de fichiers, la revue indépendante et les preuves des contrôles sont consignés.

**Arrêt impératif à la fin du LOT-2F.** Ne pas inscrire l'acceptation globale de MEC-0001 dans le registre, ne pas implémenter et ne pas commencer un autre lot sans mandat distinct.
