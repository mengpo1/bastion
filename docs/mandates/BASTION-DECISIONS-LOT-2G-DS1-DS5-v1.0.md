# BASTION — Consolidation des arbitrages DS1 à DS5 de LOT-2G — v1.0

**Nature :** transcription de décisions de conception exprimées par le propriétaire dans la conversation Bastion, après la publication de la PR n° 10.  
**Date de consolidation :** 13 novembre 2026.  
**Statut :** décisions partielles du propriétaire ; **pas une inscription au registre protégé** et **pas une autorisation d'implémentation**.  
**Dépôt :** `mengpo1/bastion`.  
**Références :** PR n° 9 (LOT-2F, fusionnée), PR n° 10 (LOT-2G, dossier de propositions), `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main`.  
**Provenance principale :** réponses successives du propriétaire dans la conversation de conception DS1 à DS5. Les propositions de Claude Code ne deviennent pas validées au seul motif qu'elles figurent dans LOT-2G.

## 1. Règle d'interprétation

- **ACCEPTÉ — principe :** décision exprimée dans les échanges avec le propriétaire, dans les limites précisées ici.
- **À DÉFINIR :** quantité, formule, variante ou comportement qui n'a pas fait l'objet d'un choix explicite.
- **ÉCART À TRAITER :** divergence entre une règle antérieure du registre ou LOT-2F et une décision plus récente. Ne pas modifier silencieusement les sources antérieures.
- Le présent document ne prononce aucune validation globale de `MEC-0001`. Dans `main`, son statut est toujours « reportée » ; aucune programmation de gameplay n'est autorisée à ce titre.

## 2. DS1 — Géométrie

**ACCEPTÉ — principes :**

1. Les calculs géométriques emploient des **proportions entre largeur de case, hauteur d'étage et taille des unités**, sans imposer d'échelle physique en mètres.
2. Les unités sont représentées par des **volumes 3D de forme rectangulaire (pavés)**. Les collisions portent sur le volume, pas simplement sur le centre de l'unité.
3. **Le sol de la case de départ est ignoré pendant le saut de l'unité qui quitte cette case.** Les autres obstacles restent soumis au calcul normal des collisions.
4. Les unités qui constituent la cible effective d'un saut offensif restent des cibles de collision, notamment les ennemis actuellement visibles (E14 du LOT-2F).

**À DÉFINIR :** rapport exact largeur de case/hauteur d'étage ; largeur et hauteur des unités ; épaisseur ou représentation des surfaces ; contact tangent, contacts simultanés, précision numérique ; règles de fin de chute. Les détails de l'algorithme géométrique proposés au LOT-2G restent des propositions tant qu'ils ne sont pas confirmés.

**ÉCART À TRAITER :** préciser dans le registre l'exception nouvelle au traitement littéral du sol de départ (P07 du LOT-2F), sans étendre cette exception à d'autres sols.

## 3. DS2 — Sauts, charge et gravité

**ACCEPTÉ — principes :**

1. **Une unité plus lourde saute moins haut ET moins loin**, à conditions comparables. La proposition LOT-2G d'une vitesse de décollage égale pour toutes les masses est rejetée.
2. La distance de portée horizontale est mesurée selon **Manhattan** : une diagonale (1,1) compte pour deux cases.
3. Les règles de référence déjà acceptées — à 1 g, hauteur maximale d'un quart d'étage et portée de deux cases pour une descente d'un étage — doivent être **rattachées à une masse de référence** afin de rendre l'effet du poids cohérent.
4. Le saut offensif n'est disponible que dans une **plage de gravité** à déterminer ; il est indisponible en apesanteur et hors de cette plage.

**À DÉFINIR :** masse ou charge de référence ; fonction de pénalisation de la hauteur et de la portée ; différence entre masse corporelle, masse totale et surcharge pour le saut ; limites de gravité et cas de valeurs extrêmes ; règles numériques de portée. Le choix entre quantité de mouvement, énergie et autre loi de propulsion **n'est pas validé**.

**ÉCART À TRAITER :** recalculer les formules et tests proposés en E2/E11 du LOT-2G : ils supposaient une impulsion verticale indépendante du poids.

## 4. DS3 — Chutes et arrondis

**ACCEPTÉ — principes :**

1. Lors d'une **chute d'un seul étage**, **l'unité qui tombe ne subit pas de dégâts si elle n'est pas ralentie par son poids**.
2. Le critère retenu pour savoir si le poids la ralentit est **le même seuil de surcharge que celui utilisé pour la réduction de ses TU** (N14) ; aucun seuil additionnel autonome n'est instauré.
3. Lors d'une **chute de plusieurs étages**, l'exemption ci-dessus ne s'applique pas ; les dégâts précis demeurent à calculer.
4. Une unité sur laquelle tombe un autre personnage **peut subir des dégâts dès une chute d'un étage**, indépendamment de l'exemption qui concerne l'unité tombante.
5. Pour les dégâts, **arrondi à l'entier le plus proche, moitié vers le haut**, une fois après base/plafond/bonus et avant tirage aléatoire, puis une seconde fois après application du facteur de poids. Les étapes ultérieures de conversion suivent leurs règles propres.

**À DÉFINIR :** traduction précise de la surcharge N14 en seuil binaire pour cette exemption ; rapport entre la charge portée de N14 et la masse totale de collision E23 ; dégâts de l'unité tombante si surchargée et pour les hauteurs supérieures ; cas d'une chute de moins d'un étage sur une unité ; **mode exact de comptage des étages franchis**, non expressément confirmé lors de l'échange DS3 ; paramètres des facteurs de poids.

**ÉCART À TRAITER :** la formule LOT-2F `D03 donne une base de 8 pour un étage ; sa portée doit être aménagée pour ne pas attribuer automatiquement ces dégâts à l'unité tombante sans surcharge. La règle E18 après une esquive (chute au sol, plafond 70 avant tirage) reste pertinente, sous réserve de cette nouvelle exemption. Ne pas assimiler automatiquement une chute sur une unité à une chute au sol.

## 5. DS4 — Collisions, masses et type « impact »

**ACCEPTÉ — principes :**

1. Lorsqu'une unité plus lourde tombe sur une unité plus légère, **le rapport de masse tend à protéger la plus lourde et à aggraver les blessures de la plus légère**. L'armure et les tirages aléatoires continuent d'intervenir ; le poids ne doit pas déterminer à lui seul qui est le plus blessé.
2. Pour un choc contre un mur, un plafond ou un obstacle, la **puissance de base est proportionnelle au carré de la composante normale de la vitesse au contact**. À masse égale, doubler cette vitesse multiplie cette puissance par quatre, avant plafond.
3. Le poids total de collision défini en E23 (corps + armure + équipement + inventaire) intervient ; le **plafond de base de 70 pour les obstacles** est conservé.
4. Création d'un **type de dégâts « impact » propre à Bastion** : mécanisme de traitement inspiré de celui d'OXCE (armure, puis santé et étourdissement), avec paramètres propres à Bastion, sans copie de données ni de code.
5. Lorsqu'une collision endommage potentiellement une unité et un obstacle destructible, le **même tirage aléatoire d'intensité du choc** sert aux deux ; protections, résistances et coefficients sont ensuite appliqués séparément.

**À DÉFINIR :** constante de conversion vitesse/puissance et ses unités ; coefficients et résistances du type « impact » ; côté d'armure applicable aux différents contacts ; formule exacte de l'effet relatif des deux masses ; coefficients de protection/amortissement ; dégâts au sol et effets des caractéristiques ; sort d'une collision avec plusieurs unités ou objets.

**ÉCART À TRAITER :** la formule E6 recommandée au LOT-2G n'est **pas validée numériquement** ; seul le sens de l'effet relatif des masses l'est. L'effet aggravant de la charge sur une chute au sol (N9/N10) demeure à distinguer de l'effet relatif de protection dans une collision entre unités.

## 6. DS5 — Ordre d'action, déplacement des corps et esquive

**ACCEPTÉ — principes :**

1. Pendant la résolution d'un saut, **le monde est momentanément figé**, sauf esquives automatiques et chutes provoquées.
2. Le saut **s'arrête au premier choc**. Collisions, dégâts, déplacement et chutes consécutives se résolvent chronologiquement. Aucun obstacle ni aucune unité cachée n'est révélé avant d'être rencontré.
3. Après un **saut offensif et une collision non esquivée**, la cible est **repoussée sur une case voisine libre** et l'attaquant prend la case initiale de la cible.
4. **Si aucune case voisine ne peut accueillir la cible**, la cible reste en place et **l'attaquant retombe à proximité**, sur un emplacement valide. Ne pas faire occuper durablement une même case par deux unités.
5. **Exclusion provisoire des unités occupant plusieurs cases** : elles n'effectuent pas de saut offensif et ne sont pas choisies comme cible de ce type de saut. Cela ne statue pas sur la marche ou les chutes involontaires.
6. Coût du saut offensif : **coût de déplacement proportionnel à la distance de Manhattan** plus `max(1, floor(0,20 × TU_max))` de supplément offensif. **La totalité est payée à l'engagement et non remboursée**, même en cas d'interruption ou d'esquive.
7. Esquive automatique : la cible doit voir l'unité qui tombe ; elle utilise **les TU qui lui restent**, même pendant le tour adverse ; elle peut se déplacer vers une des **huit cases voisines au même niveau**, diagonales comprises, si cette case est accessible et payable ; seules les informations de son camp sont utilisées ; **les TU sont débitées uniquement en cas de réussite**. La règle antérieure sur Réactions et **+5 points de probabilité par étage**, bornée 0–100 %, est maintenue en principe.

**À DÉFINIR :** choix aléatoire ou déterministe de la case de repousse ; réaction lorsque plusieurs cases sont disponibles ; rayon et recherche du lieu où retombe l'attaquant ; cas où aucun emplacement valide à proximité n'existe ; devenir d'une cible hors de combat ; effets collatéraux d'une poussée ; tarif exact en TU par case de saut ; règle numérique finale de la probabilité d'esquive et loi de sélection d'une case ; comportement en cas de destination inconnue ou occupée en cours d'action.

**À VÉRIFIER :** conformité du déplacement forcé de la cible avec les mentions antérieures de cible « immobile » en cas d'esquive échouée (K07) : interpréter « immobile » comme **pas de déplacement d'esquive**, puis appliquer le repoussement **après résolution de l'impact** ; cette articulation doit être confirmée avant inscription définitive.

## 7. Synthèse des points restant ouverts

| Domaine | Paramètres ou cas non tranchés |
|---|---|
| Géométrie | Rapport case/étage, dimensions des volumes, contacts tangents ou simultanés |
| Sauts | Formule et masse de référence, hauteur et portée selon poids et gravité, bornes de gravité |
| Chutes | Application exacte du seuil N14, comptage des niveaux, chute de moins d'un étage, formule des dégâts |
| Collisions | Loi relative des masses, coefficient vitesse², protections et conversions du type « impact » |
| Placement | Choix des cases de repousse et de repli, absence de place valide, cas d'une cible hors combat |
| TU et esquive | TU par case de saut, tirage d'esquive, règles de visibilité et de coûts encore ouvertes au registre |

## 8. Suite documentaire autorisable

Ce document sert de **source de transcription des décisions partielles** et de base à un mandat séparé de **préparation de l'inscription**. Le travail suivant peut produire une **proposition de diff du registre** et une table de traçabilité, sans modifier `docs/gameplay/GAMEPLAY-DECISIONS.md`. Toute écriture ultérieure dans le registre protégé, toute publication d'une branche de travail et toute fusion exigent les autorisations propres à ces actes.

**Aucun gameplay ni test exécutable n'est autorisé par ce document.**
