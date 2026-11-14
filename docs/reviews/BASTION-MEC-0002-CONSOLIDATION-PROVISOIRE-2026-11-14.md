# BASTION — MEC-0002 — Consolidation provisoire des décisions de conception

**Date :** 14 novembre 2026  
**Nature :** proposition documentaire de consolidation, établie par ChatGPT à partir des arbitrages explicites de cette conversation et des sources du dépôt.  
**Statut :** **NON INSCRIT AU REGISTRE ; AUCUNE AUTORISATION DE GAMEPLAY.**  
**Dépôt :** `mengpo1/bastion`.  
**Fiche prévue :** `MEC-0002 — Sauts, chutes et collisions`.  
**Fiche connexe :** `MEC-0001 — Déplacement élémentaire à pied` (reste `reportée`).  
**À ne pas confondre :** accord de conception, validation du texte final pour inscription au registre, et autorisation de développement sont trois actes distincts.

## 1. Sources et primauté

1. **Registre courant** : `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` (fichier SHA Git `a72df450487f65a864a65fdc8c683462018df384` à la consultation). Il ne contient actuellement que MEC-0001.
2. **Analyse antérieure** : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`, matrice de tests liée, `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`, `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md`, `docs/reviews/LOT-2H-TRACABILITE-ECARTS.md`.
3. **Décisions plus récentes** : arbitrages explicites du propriétaire dans la conversation du 14 novembre 2026, **prévalant pour la conception** lorsqu'ils modifient une hypothèse ancienne. Les 29 propositions de synthèse et les six réponses au QCM ont été acceptées ; l'interprétation « tentative spontanée, réussite probabiliste » a été explicitement choisie.
4. **Mandat en circulation** : `docs/mandates/BASTION-MANDAT-LOT-2I-INSCRIPTION-PARTIELLE-MEC-0001-v1.0.md`, branche `orchestration/mandats`, **préparé mais non autorisé**. Il ne reflète plus la séparation des fiches ni certaines règles amendées.

En cas de divergence, **signaler** l'ancienne formulation et la décision récente ; ne jamais effacer l'historique ni déduire une autorisation d'implémentation.

## 2. Périmètre et exclusions

- **MEC-0001** : marche ordinaire, cheminement, coûts de terrain, diagonales, visibilité du trajet, TU de déplacement ordinaire ; conserve S1–S12, Z1 et N1–N14 et une annotation historique à N7, sous réserve d'autorisation d'inscription.
- **MEC-0002** : saut simple, attaque sautée, chutes volontaire/involontaire, trajectoire balistique, contacts et collisions, réception, esquive réactive, repoussement, impact des corps, destruction sous impact et chaîne d'événements associés.
- Les escaliers, échelles, ascenseurs, les règles générales de brouillard, le renouvellement global des TU et la stabilité structurelle des bâtiments ne sont **pas** définis par MEC-0002.
- Une description de règle physique applicable à d'autres mécaniques ne les autorise pas (tir, explosion, destruction de cadavre, vol/apesanteur, etc.).

## 3. Repères, masse et posture

- Position des unités selon `(x, y, z)`, niveaux multiples.
- Largeur de case, hauteur d'étage et volumes des unités exprimés en **rapports proportionnels**, sans fixer de mètres pour la grille ; valeurs exactes non arrêtées.
- Chaque type d'unité possède un volume de collision rectangulaire configurable en 3D ; les postures debout, agenouillé et couché modifient le volume de collision.
- Pendant la phase balistique, la posture et l'orientation géométrique du volume sont conservées ; pas de rotation physique des pavés ni de changement volontaire de posture en vol.
- Un contact de surfaces suffit à détecter la rencontre ; sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés sans créer artificiellement d'énergie ou dédoubler un même impact.
- La **masse totale physique** `M` est celle du corps, de l'armure, de l'équipement et de l'inventaire, exprimée en kg.
- La **charge portée** pour la surcharge est armure + équipement + inventaire, en kg. Elle est distincte de `M` ; la Force doit être reliée à une capacité de portage en kg selon un modèle encore à définir.
- Les unités occupant plusieurs cases peuvent subir des chutes involontaires et des collisions ; **leurs sauts volontaires sont provisoirement indisponibles** (extension explicitement acceptée via la proposition 8/29 ; l'ancienne DS5.5 n'excluait que l'attaque sautée).

## 4. Sauts simples et attaques sautées

### 4.1 Distinction

- **Saut simple** : possible vers une destination admissible au même niveau ou en contrebas ; permet de franchir une ouverture ou un obstacle. Un saut volontaire vers une zone sans support immédiat est autorisé : le personnage peut continuer à tomber jusqu'à un support ou contact physique.
- **Attaque sautée** : possible uniquement si la cible se situe **au moins un étage plus bas**. Ne peut cibler intentionnellement un allié ou un neutre déjà identifié. Un ennemi actuellement visible peut être ciblé malgré la règle S10 de la marche.
- Une destination **visible ou déjà explorée** peut être choisie ; destination jamais explorée interdite. Les cases survolées peuvent être jamais explorées. Les obstacles et unités cachés ne sont révélés qu'à leur rencontre. Ennemi caché ou allié/neutre caché sur la case attaquée peuvent être percutés, avec le bonus d'attaque sautée même si la cible cachée était alliée ou neutre.
- **Saut simple percutant accidentellement une unité cachée** : collision physique et dégâts possibles ; **pas** de bonus offensif ×1,25.

### 4.2 Trajectoire

- Arc balistique continu sans contournement automatique des obstacles ; seule une destination dans la portée de Manhattan est autorisée, puis la trajectoire physique effective est vérifiée par les volumes.
- Le sol de la case de départ est ignoré lors du décollage, sans généraliser cette exception aux autres surfaces.
- Obstacle connu coupant la trajectoire : engagement interdit, sous réserve des cibles offensives explicitement autorisées. Obstacle inconnu : saut engagé puis collision, arrêt et révélation à l'impact.
- Pendant le vol : aucune modification volontaire de destination/impulsion ; vitesse horizontale constante tant qu'aucun contact ne la modifie ; fin de l'action lors d'une réception stable, sans glissement automatique.
- Un saut s'arrête au **premier choc** ; la collision puis les chutes consécutives constituent des événements distincts résolus chronologiquement.

### 4.3 Impulsions, gravité, portée

- Chaque type d'unité possède une **impulsion verticale** et une **capacité d'impulsion horizontale** distinctes et configurables.
- Loi retenue : **impulsion constante à effort égal** ; pour une unité donnée et des conditions comparables, la vitesse initiale varie en raison inverse de sa masse totale : `v = v_ref × (M_ref/M)`. À gravité constante, la hauteur varie avec le carré du rapport de masses ; la portée horizontale diminue aussi à masse plus élevée.
- La gravité influe sur la durée de vol, la hauteur et la portée. Plage d'autorisation des sauts propre au type d'unité ; bornes numériques non arrêtées.
- **Aucun saut balistique à 0 g** ; les déplacements en apesanteur sont hors périmètre. Une chute involontaire reste possible en gravité positive même lorsque les sauts sont interdits ; gravité négative invalide.
- **Référence révisée** à 1 g pour l'unité de référence : hauteur maximale **1/4 d'étage** ; portée **2 cases de Manhattan au même niveau** pour franchir un trou d'une case ; portée descendante d'un étage **supérieure à 2 cases**, valeur numérique à calculer. L'ancienne référence « 2 cases pour une descente d'un étage » est supplantée.
- Les sauts au même niveau ont, à capacités égales, une durée de vol et une portée inférieures à ceux avec un étage de descente.
- Portée horizontale : `|Δx| + |Δy|`, plafond entier **arrondi vers le bas**. Aucune portée horizontale minimale garantie lorsque le calcul donne moins d'une case.

### 4.4 Coûts en TU

- Distance **pour les TU** : `d_3D = |Δx| + |Δy| + |Δz|` ; distincte de la portée horizontale.
- `TU_simple = d_3D × C_saut`.
- `TU_attaque = d_3D × C_saut + max(1, floor(0,20 × TU_max))`.
- `C_saut` est configurable, propre aux sauts, indépendant de la marche ; sa valeur est **explicitement reportée** à l'équilibrage.
- Coût total payé intégralement à l'engagement, même si le saut est interrompu ou si la cible esquive ; pas de remboursement. Chute passive consécutive à la destination choisie : pas de surcoût en TU.
- Une action sans TU suffisantes est interdite. Prévisualisation de la destination, du coût et de la trajectoire limitée aux informations connues.

## 5. Chutes et réception

### 5.1 Volontaire / involontaire

- Un saut volontaire (simple ou offensif) d'**un étage**, sans surcharge et sans collision avec une unité, **n'inflige pas de dégâts de chute**.
- Si le personnage est **surchargé**, un saut volontaire d'un étage peut produire des dégâts.
- Une **chute involontaire** peut causer des dégâts dès un étage, **même sans surcharge** ; aucune distinction entre chute anticipée et surprise.
- Une réception sur une unité est une **collision** (potentiellement dommageable pour les deux parties), traitée distinctement des dégâts de chute au sol. Le bonus offensif ne concerne que les attaques sautées.
- Une cible qui esquive une attaque sautée laisse l'attaquant finir son saut vers le sol : ce saut conserve son **caractère volontaire**, et l'exemption d'un étage sans surcharge reste applicable.
- Si un obstacle interrompt la trajectoire puis cause une nouvelle chute, **cette chute est involontaire** ; collision et chute ultérieure sont comptées séparément.

### 5.2 Puissance de chute au sol

- Référence historique du LOT-2F conservée : `B(1)=8`, `B(2)=14`, `B(3)=22,1`, `B(4)=33,035`, progression des incréments de +6 puis ×1,35 pour les étages suivants.
- Hauteur réelle de chute, fractions d'étage incluses ; interpolation **linéaire** entre les points de référence.
- Seuil exemptant de dégâts : **hauteur de chute équivalente inférieure ou égale à 0,25 étage** ; pour `0,25 < h < 1`, interpolation de `(0,25;0)` à `(1;8)`.
- Gravité positive : la puissance de référence est pondérée par `g/g0` avec `g0 = 1 g` ; précision décimale conservée jusqu'aux étapes d'arrondi prévues.
- Vitesse verticale initiale **descendante** prise en compte par une hauteur équivalente : `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 0,25 porte sur cette hauteur équivalente. Pour une vitesse initiale ascendante, la montée se poursuit, le sommet est atteint puis la descente est résolue physiquement ; traiter ce cas avec la vitesse réelle à l'impact.
- Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse **verticale** ; la vitesse horizontale intervient dans les collisions avec les surfaces qui lui sont normales.
- **Plafond de puissance de base : 70** pour la chute au sol, **avant** multiplicateur de surcharge ; ce dernier peut porter la puissance au-delà de 70 avant le tirage. Les plafonds distincts du LOT-2F pour unité tombante (60), cible percutée (80) et obstacle (70) sont conservés pour leurs domaines respectifs, sous réserve d'une vérification de la chaîne de calcul.

### 5.3 Surcharge

- Capacité de portage définie en kg par la Force ; seuil de surcharge commun au principe N14 de récupération des TU.
- Dépassement relatif `S = max(0, Charge_portée / Capacité_portage − 1)` (capacité positive requise).
- Multiplicateur progressif et plafonné : `F_surcharge = min(2, 1 + 0,5 S)`.
- Ce facteur aggrave la puissance utilisée à la fois pour les blessures et pour l'étourdissement. L'armure applique ensuite ses protections spécifiques.
- La surcharge ne supprime pas le seuil de petite chute (0,25 étage).

### 5.4 Surfaces destructibles et successions

- La nature d'un sol (béton, terre, etc.) **ne modifie pas directement** les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol.
- L'impact peut néanmoins **endommager/détruire le support** ; si celui-ci cède, la chute continue. Chaque impact successif est résolu distinctement, et ses dommages corporels peuvent s'accumuler.
- La traversée d'une surface destructible absorbe de l'énergie cinétique, réduit la vitesse, puis la gravité peut réaccélérer le corps ; formule de perte d'énergie à définir.

## 6. Collisions et dégâts

- Détection des contacts fondée sur les volumes réels au moment du contact, y compris les changements de position liés à une esquive et les pertes de support.
- Puissance de base de collision `P = K × v_n²`, avec `v_n` la composante **normale** de la vitesse relative au contact entre deux unités (ou de la vitesse contre une surface statique). Deux coefficients distincts, configurables : `K_unités` et `K_obstacles`. **Leur valeur numérique est reportée** à des essais reproductibles.
- Pour les collisions entre unités, les blessures relatives dépendent de la masse : facteur appliqué séparément aux dégâts reçus par chacune, `F_i = clamp(sqrt(M_autre/M_i), 0,75, 1,5)`. Les valeurs de masse doivent être strictement positives.
- Pour les collisions contre le décor, la référence historique LOT-2F est `min(M/80,3)` pour le facteur de masse et un plafond de puissance de 70. Le point exact d'insertion de ce facteur dans la nouvelle chaîne de dégâts demande une revue de cohérence.
- Un type de dégâts **« impact » propre à Bastion** est retenu ; il utilise les zones corporelles exposées et les protections d'armure liées à la direction du choc, sans recopier de code/données OXCE.
- Blessures et étourdissement sont **des effets séparés** : une armure peut protéger davantage la santé que l'étourdissement ; un personnage peut être étourdi sans perdre de santé.
- Chaque type d'unité possède une sensibilité configurable à l'étourdissement ; un coefficient égal à 0 signifie immunité aux étourdissements dus aux impacts. Une unité consciente mais étourdie peut encore tenter une esquive avec Réactions réduites (règle numérique de pénalité ouverte).
- Tirage aléatoire d'intensité **50–150 %**, réalisé une fois par événement de collision ; résultat partagé par les deux unités d'une collision unité-unité, ou par l'unité et l'obstacle d'une collision unité-obstacle. Les résistances et effets sont appliqués séparément à chaque participant. Des collisions réellement **distinctes**, même rapprochées, ont des tirages distincts.
- Ordre général retenu : puissance initiale, facteur de gravité si applicable, plafond de **base**, bonus de surcharge et/ou d'attaque applicables, arrondi au plus proche (moitié supérieure), tirage, facteur de masse applicable, second arrondi au plus proche, puis effets/protections séparés pour santé et étourdissement. **Réconcilier explicitement** les termes historiques D09/D10 et éviter tout double comptage masse ou gravité avant un test numérique exact.
- Bonus d'attaque sautée `×1,25` uniquement aux dégâts infligés à la cible d'une **attaque sautée**, après plafond et avant tirage ; pas aux blessures de l'attaquant. Cible alliée/neutre cachée percutée lors d'une attaque sautée : le bonus reste applicable.
- Contacts simultanés contre plusieurs surfaces d'un **même choc** : les surfaces peuvent être endommagées, mais aucune duplication artificielle de la puissance corporelle. Collision contre plusieurs unités réellement distinctes : calcul séparé par cible, avec regroupement éventuel au niveau d'un même événement de contact ; revoir les détails à l'implémentation.

## 7. Esquives réactives

### 7.1 Principe et probabilité

- Le moteur **déclenche automatiquement la tentative**, sans intervention du joueur, mais la réussite **n'est pas automatique** ; elle dépend d'un tirage et de la compétence **Réactions**.
- Condition : menace **vue juste avant l'impact**, TU suffisantes et une case de déplacement admissible. Un personnage qui découvre une menace pendant sa chute peut tenter l'esquive.
- **Bonus de visibilité initiale +10 points** si l'unité menacée voyait la menace **dès le départ** du saut ou le déclenchement d'une chute involontaire. Sinon bonus 0 ; même logique pour les corps en chute, selon les perceptions de la cible.
- Bonus de **+5 points par étage** selon `n = |z_depart - z_arrivée|` pour une menace descendante ; le calcul de `n` pour impacts à hauteur intermédiaire reste à préciser.
- `P = clamp(R_effectif + B_visibilité + 5n, 0,100)` en pourcentage, où `R_effectif` est Réactions après pénalité éventuelle d'étourdissement.
- Tirage entier uniforme `t ∈ {1,2,…,100}` ; réussite si `t ≤ P`. **À préciser** : traitement des probabilités non entières après pénalités.
- Personnage inconscient ou mort : aucune esquive. Les corps qui tombent peuvent, en revanche, être esquivés.

### 7.2 Cases, coût et répétitions

- Une unité peut se déplacer vers l'une des **huit cases voisines du même niveau**, diagonales incluses, avec support valide ; pas de saut dans le vide lors de l'esquive.
- Coût habituel de la marche vers la case choisie (terrain et facteur diagonal), payable par les TU restantes même pendant un tour adverse.
- Une esquive **réussie et effectivement exécutée** débite les TU ; en cas d'échec du tirage ou d'impossibilité de déplacer l'unité, aucun débit de TU.
- Choix aléatoire **uniforme** parmi les destinations admissibles. Une case ne peut être choisie grâce à une information cachée. Une découverte d'obstacle bloque/révèle la tentative sans débiter de TU.
- Pas d'échange simultané de cases ; pas de passage de deux volumes l'un à travers l'autre ; destination libre au début de la résolution. Plusieurs esquives conflictuelles : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager aléatoirement les combinaisons équivalentes.
- Si plusieurs menaces **visibles et simultanées** visent une même unité lors d'un même événement, une seule tentative : choisir une case évitant toutes les menaces **connues**, calculer `n` à partir de la menace visible venant du plus grand nombre d'étages. Les menaces cachées ne sont pas prises en compte dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée.
- Si des dangers se présentent **successivement**, nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte est traitée selon le moteur séquentiel.

## 8. Repoussement et retombées

- Esquive réussie : déplacement **volontaire** pour éviter le choc, **pas** de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un **repoussement après impact**.
- Cible touchée : repoussement prioritaire dans la direction de l'impact ; sinon directions voisines les plus proches géométriquement, égalités résolues aléatoirement. Une case au-dessus du vide est admissible pour un **repoussement forcé** et entraîne une chute involontaire.
- Une case occupée par une autre unité n'est pas admissible : **pas de repoussement en chaîne**.
- Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort conserve masse et volume.
- Si la cible ne peut pas être repoussée, l'attaquant cherche une **case adjacente** (huit voisines) pour retomber, en priorité du côté de sa provenance puis par proximité de direction. Pas de recherche au-delà.
- Si l'impossibilité est entièrement connue avant l'engagement, l'attaque sautée est refusée, sans révéler de données cachées ; si elle est révélée en vol, l'attaquant s'arrête au contact puis retombe **verticalement depuis sa dernière position libre**, sans pénétrer la cible.
- Une collision accidentelle, un cadavre ou un corps inconscient peut provoquer un repoussement ; aucune intention d'attaque n'est requise pour la physique, mais aucun bonus offensif n'est créé.
- Lorsque plusieurs impacts constituent réellement un même instant, la direction de repoussement résulte des intensités et directions combinées ; cette règle n'introduit **pas** des attaques volontaires simultanées dans le tour par tour.

## 9. Environnement destructible et événements

- Murs, portes, planchers et autres décors destructibles disposent de points de résistance **cumulatifs** ; les sources successives de dégâts peuvent les réduire. Les éléments indestructibles restent intacts.
- Tant que leur résistance demeure strictement positive, les éléments conservent leur blocage et leurs propriétés de collision ; une variation d'apparence est possible, sans fissure fonctionnelle automatique.
- À zéro point de résistance : destruction **immédiate** ; perte de support et éventuelles chutes déclenchées immédiatement. Pas d'effondrement structurel automatique des éléments voisins (« bâtiment porteur » hors périmètre).
- Pour un **même événement physique** produisant plusieurs impacts simultanés sur le même plancher, les dégâts se cumulent avant d'en décider la destruction ; ne pas confondre avec plusieurs chutes d'unités résolues successivement.
- **Tour par tour** : une action offensive volontaire est résolue jusqu'au bout avant la prochaine action de combat.
- Si plusieurs unités perdent leur support à cause d'un même événement : le moteur traite les chutes **successivement**, suivant un **ordre stable** (par exemple identifiants internes), via une file **FIFO**. Les nouvelles chutes sont ajoutées après celles qui attendent déjà.
- À chaque traitement, réévaluer positions, vitesses, santé et supports actuels ; annuler un événement devenu caduc. **Un seul événement de chute en attente par unité** ; pas de traitement redondant.
- Des corps morts/inconscients peuvent tomber, heurter d'autres unités et provoquer dégâts/étourdissement/repoussement. Les cadavres ne reçoivent plus de pertes de santé ni d'étourdissement ; les règles de destruction des corps sont hors périmètre.
- Des collisions d'un même événement peuvent rencontrer plusieurs surfaces ou cibles ; les règles d'un événement partagé ne doivent pas réintroduire implicitement une simulation de plusieurs actions offensives simultanées.
- Randomisation contrôlable par graine, ordre de traitement déterministe hors hasard explicitement choisi, tests reproductibles.

## 10. Registre des écarts à l'historique

| Référence | Formulation historique | Statut après arbitrages récents |
|---|---|---|
| `MEC-0001` | Marche et verticalité mêlées | Séparer la mécanique de sauts/chutes/collisions en `MEC-0002` ; garder la marche dans MEC-0001. |
| `N7` / `H01` / `E21` | Petite chute sans dégâts, puis « contradictoire » avec dégâts possibles dès un étage | Garder N7 comme historique, **annoter** avec distinctions volontaire/involontaire, surcharge et seuil de 0,25 étage ; ne pas effacer les sources. |
| `DS3.1` | Exemption d'un étage pour l'unité non surchargée, sans préciser volontaire | Exemption **uniquement du saut volontaire d'un étage sans surcharge** ; chute involontaire peut blesser dès un étage. |
| `P05` / `DS2.3` | 2 cases de portée à 1 g pour une descente d'un étage | Référence remplacée : 2 cases au **même niveau** ; descente d'un étage davantage. |
| `P02` / `E11` | Ambiguïté vitesse vs impulsion | Quantité de mouvement/impulsion à effort égal ; masse totale affecte hauteur et portée ; capacités horizontale/verticale distinctes. |
| `K05` / `DS5.7` | Réactions +5/étage ; visibilité juste avant le choc | Ajout +10 si menace vue au départ ; Réactions après pénalité d'étourdissement ; tirage entier 1–100 ; visibilité juste avant impact demeure nécessaire. |
| `K07` / `DS5.3` | « Cible immobile » après échec vs poussée après choc | Aucun déplacement **d'esquive** sur échec ; repoussement **forcé** ensuite possible. |
| `D02` | Nature du sol sans effet sur dégâts | Conservé pour les dégâts corporels ; **destruction du sol et perte de vitesse** restent possibles et distinctes. |
| `D12` / OXCE | Destruction par seuil individuel, sans accumulation | Résistance cumulative généralisée pour les éléments destructibles de Bastion. |
| `D13` | Collision puis chute depuis le contact | Chute consécutive **involontaire**, distincte du saut volontaire initial. |
| `DS5.1` / événements | Chutes supposées simultanées | Les **chutes d'unités** sont traitées successivement en FIFO déterministe ; contacts simultanés d'un événement unique restent traités comme tels. |
| `DS5.5` | Exclusion des grandes unités uniquement des attaques sautées | Extension provisoire : **tout saut volontaire** des unités multicas interdit ; chutes involontaires autorisées. |
| `DS5.6` | Coût de saut offensif +20 % | Saut simple **sans** supplément ; saut offensif **avec** supplément. Distance du coût = Manhattan 3D, portée = Manhattan horizontal. |
| `DS4.5` | Tirage commun entre unité et obstacle | **Étendu explicitement** au choc entre deux unités (un tirage commun pour les deux), séparé par événement de collision distinct. |

## 11. Paramètres et questions encore ouverts — à ne pas inventer

1. **Géométrie** : ratio largeur case/hauteur étage, dimensions précises des unités/postures, tolérance numérique des contacts, épaisseur des surfaces.
2. **Saut** : masses/capacités de référence par type, calibration horizontale pour 2 cases au même étage, trajectoires à très faible gravité, plage de g par type, `C_saut`, comportement si coût calculé non entier (si TU fractionnaires/non fractionnaires).
3. **Marche/TU** : coûts des cases et diagonales, capital de TU, renouvellement, règles complètes de visibilité, sous la responsabilité de MEC-0001 / mécaniques transversales.
4. **Force/charge** : formule de capacité de portage en kg à partir de Force ; cohérence avec N14 (pénalité TU) ; valeurs des masses de corps/objets.
5. **Dégâts** : `K_unités`, `K_obstacles`, coefficients d'absorption d'énergie des planchers, conversion résistance → énergie ; éventuelles limites numériques ; niveau de protection selon zone, coefficient santé/stun ; pénalité d'étourdissement sur Réactions.
6. **Chaîne de calcul** : place exacte du facteur de masse `min(M/80,3)` pour obstacles, interactions des plafonds 60/70/80 avec bonus, gravité et surcharge ; rôle de l'armure, deux étapes d'arrondi et normalisation de 50–150 % ; aucune double prise en compte gravité/vitesse/masse.
7. **Visibilité** : moment exact où l'unité « voyait » une menace involontaire (début de perte de support), objets/corps initialement dissimulés, visibilité multi-cibles ; calcul de `n` en cas de trajectoire interrompue et de niveau partiel.
8. **Esquive** : arrondi des probabilités non entières ; pénalité liée à l'étourdissement ; gestion détaillée des chemins physiques et de la compatibilité des esquives coordonnées ; éventuel nombre maximal d'événements en chaîne.
9. **Données de décor** : propriétés destructible/indestructible, résistance initiale et unité de dégâts du terrain, règles d'application d'autres sources (armes/explosions) non autorisées ici.
10. **Cas de placement** : emplacements précis des cadavres, collisions imbriquées et multi-cibles, modes d'arrêt sur le dernier volume libre ; robustesse moteur à tester.

Ces points ouverts ne constituent ni une permission de choisir des valeurs par défaut silencieusement, ni nécessairement des obstacles à une **inscription partielle** des décisions claires.

## 12. Préconisations de tests documentaires et exécutables futurs (non autorisés)

- Vérifier qu'un saut d'un étage sans surcharge et sans obstacle n'inflige pas de dégâts au sauteur, mais qu'une chute involontaire comparable peut en infliger.
- Vérifier bonus d'esquive +10 visible au départ / 0 non visible au départ, mais vu avant le contact ; +5 par étage ; tirage entier 1..100 avec graine connue.
- Comparer attaque sautée, saut simple, collision accidentelle avec allié caché ; bonus ×1,25 seulement pour l'attaque sautée.
- Tester paiement intégral des TU dès engagement, saut simple vs offensif, coût Manhattan 3D, sans remboursement après collision.
- Tester chute équivalente 0,25 (0 dégât) et >0,25, interpolation à 1,5 étages, gravité 0,5 g et 2 g.
- Tester rapport de masse 120/60 kg (facteurs 0,75 et ~1,414) et séparation blessures/étourdissement avec armure et immunité.
- Tester obstacle destructible en impacts successifs, collision qui détruit un plancher, vitesse résiduelle et deuxième impact.
- Tester file FIFO stable A/B/C, réévaluation d'un événement devenu caduc, déduplication d'une chute déjà en attente.
- Tester repoussement dans le vide, absence de place libre, esquive impossible sans TU, collision de cadavre et destination cachée.
- Tester que MEC-0001 demeure inchangée fonctionnellement et qu'aucune information cachée n'est révélée avant contact.

## 13. Prochaine étape documentaire proposée

1. Relire cette consolidation contre les **messages datés** de validation et les rapports LOT-2F/2G/2H ; corriger tout raccourci de formulation.
2. Faire produire par Claude Code, sous mandat documentaire spécifique et après autorisation d'exécution, un **tableau de traçabilité règle → décision → formulation → test → écart historique**, puis un **diff proposé uniquement**, sans écrire dans `docs/gameplay/GAMEPLAY-DECISIONS.md`.
3. Revue indépendante de la traçabilité et de toutes les exclusions.
4. Proposer séparément au propriétaire un texte final et un périmètre précis d'inscription. **Aucune inscription, publication, PR, fusion ni implémentation n'est implicitement autorisée par le présent document.**
