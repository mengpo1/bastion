# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.3

**Date :** 19 novembre 2026
**Nature :** projet de consolidation documentaire, préparé pour une revue indépendante. Non revu, non inscrit.
**Statut :**
- MEC-0001 et MEC-0002 restent **reportées** dans leur ensemble ;
- aucun gameplay, aucune implémentation, aucune inscription n'est autorisé ;
- aucun test n'a été exécuté.

**Base :**
- dépôt `mengpo1/bastion`, `main` = `818c646c7d33b819d8b69b81679749be6e77eff9` ;
- registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, SHA-256 `9117d20c45aa95abbc218ce5cdcc2a095106eb86c64a342be76d8521ef14d39e`.

**Succède à :** la consolidation Q1–Q4 v0.2 (SHA-256 `062c5e9c8176d08fedb4dbbb9d67daeebf1caf53b0e7d76d28250f19819ca2a1`). Elle intègre :
- les 29 propositions et validations d'origine de Q1 à Q3 ;
- l'addendum Q5.1–Q5.2 ;
- l'addendum B3 et son rectificatif ;
- les corrections des revues (journal au §16).

## 0. Provenance : niveaux de preuve

| Code | Sens | Vaut décision ? |
|---|---|---|
| **[INS]** | inscrit au registre sur `main` ; ligne `R:NN` | oui |
| **[TR]** | texte transmis : proposition et validation d'origine, collées par le propriétaire le 19 novembre 2026 ; non archivé | oui |
| **[CIT]** | validation citée : message du propriétaire reproduit au §12 de la v0.2. L'identifiant et l'option sont attestés ; la formulation détaillée est un résumé de l'orchestrateur | oui, pour l'option ; la formulation reste à vérifier |
| **[DÉC]** | déclaration du propriétaire dans la conversation du 19 novembre 2026, sans le texte de la proposition d'origine | oui ; texte d'origine absent |
| **[PNV]** | proposé, non validé : aucune décision explicite trouvée | **non** |
| **[OUV]** | point ouvert, déclaré comme tel | **non** |
| **[DÉD]** | conséquence arithmétique ou logique de décisions sourcées, à vérifier | non (simple conséquence) |

Une règle n'est considérée comme décidée que si elle porte l'un des codes [INS], [TR], [CIT] ou [DÉC].

## 1. Périmètre et responsabilités

- **MEC-0001 :** la marche ordinaire, son cheminement, ses coûts en TU et en énergie, la visibilité du trajet, les portes et les connexions spéciales entre niveaux [INS] (PE-01, R:196 ; B3-05 [DÉC]).
- **MEC-0002 :** les sauts, chutes, contacts, collisions, esquives, repoussements et impacts [INS] (PE-01, PE-02, R:196-197). Les escaliers, échelles et ascenseurs sont hors de MEC-0002 [INS] (PE-03, R:198).
- Une perte de support transfère immédiatement la situation à MEC-0002 : Q4.3 [CIT].
- B3 n'autorise aucune nouvelle mécanique et ne change pas les règles de dégâts [DÉC].

## 2. Décisions inscrites et état actuel

| Règle | Ligne | État actuel | Ce qui la précise ou la modifie |
|---|---|---|---|
| S1 | R:71 | en vigueur | — |
| S2 | R:72 | en vigueur | coût d'entrée par terrain (Q3.1, Q3.13) ; aucun surcoût universel de mur (Q3.12) |
| S3 | R:73 | en vigueur | — |
| S4 | R:74 | restreinte | ARB-A, G1 |
| S5 | R:75 | **historique** | supplantée par Z1 pour la sélection normale |
| S6, S7 | R:76-77 | en vigueur | S7 appliquée au trajet physique (G1) |
| S8, S9 | R:78-79 | en vigueur | appliquées par Q3.4 et Q4.21 |
| S10 | R:80 | en vigueur | exceptions ARB-B et G2 ; **aucune exception de plus** par Q5.2 [DÉC] |
| S11 | R:81 | en vigueur | Q4.20 : une révélation seule n'interrompt pas la marche |
| S12 | R:82 | en vigueur | — |
| Z1 | R:90 | portée étendue | G3 : l'énergie entre dans la zone atteignable |
| N1 à N3 | R:91-93 | en vigueur | — |
| N4 | R:94 | en vigueur | ARB-C ; Q2.1 à Q2.4 |
| N5 à N10 | R:95-101 | historiques pour les chutes | MEC-0002 fait autorité |
| N11, N14 | R:102-111 | en vigueur | N14 : portée modifiée par G3 ; formule de surcharge par Q3.14 |
| ARB-A | R:121 | en vigueur | G1 |
| ARB-B | R:122 | en vigueur | Q4.19 : un corps n'empêche pas le repositionnement |
| ARB-C | R:123 | en vigueur | Q2.1 à Q2.4, Q3.3, Q3.10, Q3.12, Q4.7 à Q4.15, Q5.2 |
| ARB-D | R:124 | en vigueur | formule par Q3.14 ; profil initial par Q4.6 |
| ARB-E | R:125 | en vigueur | étendue aux transferts (Q4.13) ; précisée par Q5.1 |
| G1 | R:126-134 | en vigueur | priorité « X puis Y » : [PNV], voir PNV-7 |
| G2 | R:135-140 | en vigueur | Q4.19 |
| G3 | R:141 | en vigueur | barème par Q3.7 à Q3.9 et Q3.13 |
| G4 | R:142-147 | en vigueur | clé de départage par Q4.16 |
| GE-02 (MEC-0002) | R:203 | **à modifier** | B3 (§9) |
| GE-03 (MEC-0002) | R:204 | **à préciser** | B3, Q1.2, Q1.6 (§9) |

## 3. Géométrie

### 3.1 Décisions Q1

| Décision | Texte validé | Provenance |
|---|---|---|
| Q1.1=A | Largeur des cases uniforme par carte, configurable et paire, en millimètres. | [TR] |
| Q1.2=A | Dimensions configurables par type d'unité et par posture. Le volume peut dépasser sa case ; les collisions restent obligatoires. | [TR] |
| Q1.3=A | Épaisseur configurable par type de mur ; les murs ont un volume physique défini. | [TR] |
| Q1.4=A | Altitude configurable pour chaque niveau ; les étages pouvaient d'abord être séparés par des hauteurs différentes. **Historique**, supplantée pour la hauteur d'étage (§3.2). | [TR] |
| Q1.5 | Largeur initiale des cases : 1 500 mm (option B). | [TR] |
| Q1.6=A | Profil humain standard, en largeur × profondeur × hauteur : debout 600 × 600 × 1 800 mm ; agenouillé 600 × 600 × 1 200 mm ; couché 1 200 × 600 × 500 mm, orienté selon le corps. Ce sont des volumes de collision, pas des dimensions anatomiques. | [TR] |
| Q1.7 | Épaisseur initiale d'un mur standard : 100 mm (option A). | [TR] |
| Q1.8 | Écart initial entre les références de deux niveaux : 3 000 mm (option A). Le cadre configurable est supplanté (§3.2). | [TR] |
| Q1.9=A | Seuils initiaux de ressaut pour un humain debout : montée 200 mm, descente 300 mm. | [TR] |

**Portée de Q1.5 à Q1.9** [TR] : « Ces choix fixent uniquement les valeurs initiales de référence. Les autres types d'unités, postures, murs et cartes pourront utiliser des paramètres différents. » Ce sont donc des valeurs initiales configurables, **sauf la hauteur d'étage** (§3.2).

**B3** [DÉC] (addendum B3, §B3-01 à B3-03, et son rectificatif) :
- MEC-0001 et MEC-0002 partagent un même référentiel physique : coordonnées, dimensions des cases, niveaux, surfaces, volumes, postures et orientations ;
- les dimensions configurées s'expriment en millimètres ;
- une même unité n'a pas de dimensions différentes selon qu'elle marche, saute ou tombe.

**Configurations admissibles** (rectificatif B3, §4) :
- la parité de la largeur des cases est sourcée : Q1.1 [TR] ;
- les dimensions minimales, les tolérances et les autres conventions d'arrondi restent [OUV] ;
- le rectificatif ne crée aucune contrainte.

### 3.2 Hauteur des étages : chronologie et règle applicable

1. **GE-02** [INS] (R:203), précisée par l'arbitrage A3A et reprise par CH-08 (R:249) : 3 m fixes entre deux sols d'étages consécutifs. CH-01 et CH-03 (R:242, R:244) assimilent un étage à 3 m.
2. **Q1.4=A** [TR] : altitude configurable par niveau, hauteurs libres. *Écart avec GE-02 à cette date ; la v0.2 ne le signalait pas.*
3. **Q1.8** [TR] : 3 000 mm comme écart initial de référence, dans un cadre configurable.
4. **Q4.1=A** [CIT] : 3 m fixes entre sols de référence d'étages tactiques consécutifs, avec des dénivelés locaux possibles. C'est la rectification de Q1.4.

**Règle applicable :** 3 000 mm **fixes** entre les sols de référence de deux étages tactiques consécutifs (GE-02, précisée par Q4.1). Seuls les dénivelés locaux des supports varient. Pour cette valeur, Q1.4 et le cadre configurable de Q1.8 sont historiques. B3 conserve cette hauteur et n'ajoute aucune valeur (rectificatif, §2). **Elle ne figure donc pas parmi les valeurs configurables de B3-02** (correction C-30, §16).

**Restent ouverts** [OUV] : les bornes des dénivelés locaux, et le rattachement d'une case à un étage.

### 3.3 Murs et enveloppes (conventions reportées de Q1)

- **Q2.5=A** [TR] : un mur est centré sur la frontière commune ; un mur de 100 mm occupe 50 mm dans chaque case.
- **Q2.6=A** [TR] : l'enveloppe englobante (AABB) d'un volume orienté est agrandie au plus petit nombre pair de millimètres qui la contient entièrement.
- **B3-04** [DÉC] : les enveloppes de calcul ne remplacent pas, sans justification, les volumes réels qu'exige CO-01 (R:265).

### 3.4 Contacts

- **Q4.2=A** [CIT] (résumé v0.2) : un contact de surfaces est détectable. Le contact seul ne bloque pas la marche, contrairement au chevauchement intérieur, qui est interdit. Impacts et dégâts restent sous MEC-0002.
- **ARB-A et G1** [INS] : le volume ne traverse ni une autre unité consciente, ni un obstacle.
- **GE-05** reste inchangée ; sa tolérance numérique reste [OUV].

### 3.5 Formulations sans source : résultat de la recherche

| N° | Formulation de la v0.2 | Recherche d'une décision explicite | Statut en v0.3 |
|---|---|---|---|
| PNV-1 | Repère : x vers l'est, y vers le sud, z vers le haut ; origine au nord-ouest ; indices à partir de zéro ; centres de case en (i + 0,5) × L (D:29) | N3 et GE-01 ne donnent que des positions (x, y, z) ; Q1.1, une largeur uniforme | positions (x, y, z) : [INS] ; le reste : **[PNV]** |
| PNV-2 | Toutes les données géométriques en millimètres entiers ; conversion des valeurs externes « vers demi-entiers », la moitié arrondie en s'éloignant de zéro (D:30) | Q1.1 (largeur paire en mm), Q2.6 (enveloppes paires) ; le rectificatif B3, §1, n'étend pas les entiers aux calculs de MEC-0002 | largeur et enveloppes : [TR] ; le reste : **[PNV]** |
| PNV-3 | Orientations sur huit directions (D:32) | S1 [INS] (huit directions de déplacement) ; Q4.17 [CIT] (orientation vers le pas engagé) ; Q1.6 dit seulement « orienté selon le corps » | **[PNV]** comme liste fermée d'orientations ; l'exemple à 45° en dépend (§3.6) |
| PNV-4 | Support uniforme et valide sous tout le volume horizontal ; unité stable au centre de case à l'arrivée (D:34) | Q2.1 (positions stables), Q2.2 (supports horizontaux), Q4.19 (« avec support ») | positions stables horizontales : [TR] ; « uniforme », « tout le volume », « au centre de case » : **[PNV]** |
| PNV-5 | Au-delà des seuils de Q1.9, marche refusée, sans chute ni saut automatique (D:35) | ARB-C [INS] : pas de changement de niveau implicite ; sauts et chutes relèvent de MEC-0002 (PE-01, PE-02) | pas de changement de niveau implicite : [INS] ; refus de la marche et absence de chute automatique au-delà du seuil : **[PNV]** |
| PNV-6 | Phases d'un pas : montée d'abord verticale puis translation ; descente d'abord horizontale puis abaissement ; volume balayé de chaque pas vérifié (D:36) | G1 [INS] : le volume emprunte un passage sans traverser d'obstacle (diagonale) ; Q4.17 [CIT] : volume balayé de la rotation | phases : **[PNV]** ; volume balayé : [INS] pour la diagonale, **[PNV]** pour les autres pas |
| PNV-7 | Diagonale : priorité au passage X, puis Y (D:37) | G1 [INS] parle de « l'un des passages praticables », sans priorité. Q4.16 [CIT] renvoie à une « règle X d'abord Q1 » qui ne figure dans aucune des neuf sous-décisions Q1 : **renvoi circulaire** | **[PNV]** jusqu'au texte d'origine de Q4.16 |
| PNV-8 | Réveil simultané : ordre par identifiant croissant, voisins dans l'ordre N, NE, E, SE, S, SW, W, NW, sans nouvelle tentative en boucle (D:39) | Q4.19 [CIT] : ordre des voisins, aucune nouvelle recherche automatique. Q3.5 [TR] ne vise que les événements « sur le trajet » | ordre des voisins et absence de nouvelle tentative : [CIT] (Q4.19) ; ordre de traitement de plusieurs réveils simultanés : **[PNV]** ; l'attribution à Q1 est retirée |
| PNV-9 | Représenter l'ordre du trajet physique et la position exacte des rencontres (D:40) | cas sourcés : perte de support (Q4.3 [CIT]), tir de réaction (Q5.1 [DÉC]), obstacle inconnu (Q3.4 [TR], S8 [INS]) ; ordre des événements (Q3.5 [TR]) | cas énumérés : sourcés ; exigence générale : **[PNV]** |

### 3.6 Conséquences des valeurs sourcées [DÉD]

- Largeur intérieure entre deux murs standards : 1 500 − 2 × 50 = **1 400 mm** (Q1.5, Q1.7, Q2.5).
- Enveloppe à 45° : 1 272,8 → **1 274 mm** pour le profil couché, 848,5 → **850 mm** debout et agenouillé (Q1.6, Q2.6). Ce calcul dépend de **PNV-3**.
- Étendue horizontale maximale du profil couché pendant une rotation : **1 341,6 mm** (vers 26,6°). C'est moins que 1 400 mm, mais le volume balayé reste [OUV].
- Rapport case / étage initial : 1 500 / 3 000 = **0,5**.
- Le profil humain initial ne dépasse jamais sa case horizontalement (600, 1 200 et 1 274 mm, pour 1 500 mm). D'autres types d'unités le pourront (Q1.2).

## 4. Connexions, passages et portes

| Décision | Texte validé | Provenance |
|---|---|---|
| Q2.1=A | Escaliers : connexions explicites entre positions stables ; trajet physique praticable ; pas de changement implicite du niveau tactique. | [TR] |
| Q2.2=A | Rampes : passages spéciaux entre supports horizontaux ; extrémités en positions stables horizontales ; collisions du trajet contrôlées. | [TR] |
| Q2.3=A | Échelles : action spécifique avec connexion définie ; accès réservé aux unités compatibles ; entrée et sortie explicites ; volume de passage contrôlé ; aucun déplacement vertical ordinaire implicite. | [TR] |
| Q2.4=A | Ascenseurs : plateforme à états explicites, avec un niveau courant ; les connexions d'accès dépendent de l'état. L'option de téléportation est écartée. | [TR] |
| Q3.3=A | Coût défini pour chaque connexion, configurable en TU et en énergie ; aucun double débit automatique des segments. | [TR] |
| Q3.10=B | Coûts obligatoirement définis par connexion ; aucun barème universel ; valeurs de test fixées dans chaque scénario. Les chiffres de l'option A, écartée, ne sont pas repris. | [TR] |
| Q3.12=A | Aucun surcoût universel lié au mur. Un mur infranchissable bloque ; un passage ouvert suit le coût du terrain ou de sa connexion ; ouvrir une porte est une action distincte. | [TR] |
| Q4.7=A | Porte ordinaire : ouverture manuelle explicite, initialement 4 TU / 0 énergie ; aucun pas automatique ensuite ; les portes particulières ont leurs propres règles. | [CIT] ; valeurs [DÉC] (initiales, configurables) |
| Q4.8=A | Connexion avec occupation physique et capacité ; admission, collision et sortie vérifiées ; coûts par connexion sans double débit des segments ; pas d'animation universelle requise ; aucun transfert par téléportation. | [CIT] |
| Q4.9=A | Transfert interrompu : la position et l'état atteints sont conservés, sans arrivée complétée automatiquement. Perte de support : Q4.3 et MEC-0002. | [CIT] |
| Q4.10=A | Transit interrompu mais soutenu : état suspendu, qui conserve la position, l'orientation et le lien avec la connexion ; reprise possible. Support perdu : MEC-0002. Cet état n'est pas une station tactique ordinaire. | [CIT] |
| Q4.11=A | Coût intégral du transfert payé à l'engagement, après vérification ; aucun remboursement si le transfert est interrompu ; pas de refacturation des segments d'un même transfert. Une nouvelle action a un nouveau coût. Le coût par pas de marche n'est pas modifié. | [CIT] |
| Q4.12=A | Reprise du même transfert, dans le même sens, sans nouveau paiement, après vérification. Le retour vers l'entrée est une nouvelle action, avec son propre coût et sans remboursement. | [CIT] |
| Q4.15=A | Chaque connexion définit sa capacité ; plusieurs utilisateurs sont possibles si la capacité et les volumes le permettent, sans chevauchement intérieur, avec un accès et une sortie physiquement valides. | [CIT] |
| Q5.2=A | Voir ci-dessous. | [DÉC] |

**Q5.2=A** [DÉC] (message du propriétaire du 19 novembre, puis addendum Q5.1–Q5.2, §B) :
- une connexion peut avoir une capacité supérieure à une unité, sans que cela supprime les règles d'occupation de S10 ;
- chaque unité consciente en position stable occupe un emplacement tactique stable distinct ;
- aucune superposition volontaire de deux unités conscientes sur un même emplacement stable n'est autorisée ;
- une plateforme à plusieurs emplacements peut accueillir plusieurs unités si sa capacité et les volumes le permettent. Avec un seul emplacement, elle ne peut pas en porter deux, conscientes, à cet emplacement ;
- le transit reste soumis aux contrôles de volume et d'occupation de Q4.8 et Q4.15 ;
- l'exception transitoire de G2 au réveil est inchangée ;
- **Q4.15 n'est pas une exception supplémentaire à S10.**

*Notes :*
- La relation entre « emplacement tactique stable » et « case » n'est pas formulée [OUV]. Tant qu'elle ne l'est pas, S10 (R:80) s'applique telle qu'inscrite.
- Le mot « volontaire » ne crée pas d'exception : seule l'exception transitoire de G2 est inscrite, et les situations propres à MEC-0002 relèvent de ses règles.

**Restent ouverts** [OUV] : les profils complets des connexions (géométrie, support pendant le transit et en cas d'inconscience, accès, sortie, capacité, états d'ascenseur, coûts par instance) ; la personne ou l'action qui déclenche la reprise d'un transfert suspendu ; le réveil d'une unité restée dans une connexion ; le chemin et le coût d'un retour partiel (Q4.12).

## 5. Coûts, ressources et surcharge

**Décisions :**
- **Q3.1=A** [TR] : barème par type de terrain ; chaque terrain définit un coût d'entrée en TU et en énergie, celui de la case d'arrivée (S2) ; les règles existantes en déduisent le coût des diagonales.
- **Q3.2=A** [TR] : l'énergie d'une diagonale a son propre multiplicateur ; le multiplicateur des TU de S2 est inchangé.
- **Q3.7=A** [TR] : pas orthogonal sur terrain normal, 4 TU et 2 d'énergie ; la diagonale coûte 6 TU (S2).
- **Q3.8=A** [TR] : trois catégories initiales : normal (coût de base), difficile (+50 % de TU et d'énergie), très difficile (+100 %).
- **Q3.9=A** [TR] : facteur initial de 1,5 pour l'énergie d'une diagonale, arrondi vers le haut (3 devient 5).
- **Q3.13=A** [TR] : le coût de base est multiplié par le facteur de terrain, puis arrondi vers le haut pour chaque ressource. La diagonale applique ensuite ses règles : TU × 1,5 arrondies vers le bas (S2), énergie × 1,5 arrondie vers le haut (Q3.9). Chaque coût final est entier et calculé une seule fois, avant le pas.

**Barème initial** [DÉD], valeurs initiales configurables :

| Terrain | Orthogonal | Diagonal |
|---|---|---|
| Normal | 4 TU, 2 énergie | 6 TU, 3 énergie |
| Difficile (+50 %) | 6 TU, 3 énergie | 9 TU, 5 énergie |
| Très difficile (+100 %) | 8 TU, 4 énergie | 12 TU, 6 énergie |

**Ressources :**
- **Q3.6=A** [TR] : l'énergie a un maximum et une récupération distincts de ceux des TU ; les valeurs seront fixées séparément.
- **Q3.11=B** [TR] : la réserve et la récupération d'énergie restent configurables, sans valeur fixée à ce stade.
- **Q4.6=A** [CIT], valeurs [DÉC] : profil initial de test, configurable et non universel : 60 TU maximales, 60 TU récupérées par tour, 100 d'énergie maximale, 20 d'énergie récupérée par tour. Ces valeurs viennent de Q4.6 et non de Q3.11. Elles sont identiques à celles de l'option A de Q3.11, qui avait été écartée.

**Surcharge :**
- **ARB-D** [INS] (R:124) : TU disponibles = min(solde + récupération, TU maximales), puis réduction sur ce total plafonné ; énergie récupérée séparément.
- **Q3.14=A** [TR] : capacité de portage en kg, déduite de la Force par une conversion configurable ; facteur = min(1, capacité / charge), et facteur 1 si la charge est nulle ; appliqué au total plafonné ; résultat arrondi vers le bas.

```text
F = 1                         si charge = 0
F = min(1, capacité / charge) si charge > 0
TU_après = ⌊ min(TU_restantes + TU_récupérées, TU_max) × F ⌋
```

- **Q4.5=A** [CIT] : conversion de la Force en kg configurable par type d'unité, unique pour les deux mécaniques, capacités positives. Les valeurs restent ouvertes. La mention « aucune formule Force × 10 universelle » ne vient que du résumé de la v0.2.
- **Charge portée** [INS] (GE-07, R:208) : armure, équipement et inventaire, distincte de la masse totale (GE-06).
- La surcharge ne majore pas le prix des pas et n'immobilise pas : N14 et ARB-D [INS].
- La surcharge ne réduit pas l'énergie. C'est une **lecture d'ARB-D** (« énergie récupérée séparément »), pas une décision formulée à part.

**Restent ouverts** [OUV] : les autres pénalités de TU et leur ordre ; la table Force → kg ; l'indicateur « encombré » ; la précision des calculs, qui devra se faire en arithmétique exacte (voir T20).

## 6. Exécution d'un pas et événements

**Décisions :**
- **G3** [INS] (R:141) : chaque pas coûte des TU et de l'énergie, et n'est exécuté que si les deux suffisent.
- **Q3.4=A** [TR] : vérification avant chaque pas, avec interruption si nécessaire ; un pas non commencé n'est pas débité ; les pas accomplis gardent leur coût ; les découvertes mettent la connaissance à jour (S8 à S11).
- **Q3.5=A** [TR] : les priorités propres aux règles s'appliquent d'abord ; les égalités restantes se départagent par identifiant unique croissant ; l'applicabilité est réévaluée après chaque résolution.
- **Q4.4=A** [CIT] : les chutes nées d'un même événement suivent un ordre stable, en file par identifiant croissant ; les chutes secondaires s'ajoutent en fin de file, avec revalidation selon EN-07 ; Q3.5 ne renverse pas ces priorités.

**États d'un pas :**

| État | Règle | Source |
|---|---|---|
| Non commencé | aucun débit | Q3.4 [TR] ; Q4.3, Q4.21 [CIT] |
| Engagé | débité une seule fois, débit conservé | Q4.3 [CIT] ; Q5.1 [DÉC] |
| Achevé | coût conservé, sans remboursement | Q3.4 [TR] ; ARB-E [INS] (« pas déjà effectué ») |
| Interrompu par un événement physique prioritaire | effet immédiat à la position physique du moment ; relais à MEC-0002 ; pas engagé débité ; pas non commencé non facturé ; ni retour, ni téléportation | Q4.3 [CIT] ; Q5.1 [DÉC] |

L'instant précis où un pas passe de « non commencé » à « engagé » n'est défini nulle part [OUV]. Le support pendant les phases intermédiaires d'un pas est [OUV] lui aussi ; il dépend de PNV-6.

**Q5.1=A** [DÉC] (message du propriétaire du 19 novembre, puis addendum Q5.1–Q5.2, §A) :
- le tir de réaction qui interrompt une marche est résolu à la frontière du pas engagé, une fois ce pas achevé ;
- l'unité atteint la destination du pas avant la résolution du tir ;
- le pas est débité une seule fois ;
- le tir effectivement tiré interrompt l'ordre, même s'il manque ;
- un pivot sans tir ne suffit pas ;
- la perte de support et les autres événements physiques prioritaires s'appliquent immédiatement (Q4.3, MEC-0002) ;
- la détection, le déclenchement et les coûts de la surveillance (Overwatch) restent hors de cet arbitrage.

**Autres interruptions :**
- **Q4.13=A** [CIT] : un tir de réaction effectivement tiré contre une unité en transfert interrompt aussi l'action, même sans toucher. Le coût et la position atteinte sont conservés ; le transfert n'est pas complété. Pendant la marche, la règle applicable est celle de Q5.1.
- **Q4.14=A** [CIT] : une incapacité interrompt l'action, puis le support est contrôlé. L'unité reste en place si elle est soutenue ; sinon elle chute sous MEC-0002. Il n'y a pas de chute automatique indépendante du support.
- **Q4.20=A** [CIT] : une révélation seule, sans obstacle au trajet ni tir déclenché, n'interrompt pas la marche. Si elle bloque réellement le trajet, S8 à S11 s'appliquent.
- **Q4.21=A** [CIT] : quand le pas suivant n'est plus exécutable (coût réel supérieur aux ressources restantes, occupation, obstacle), l'unité s'arrête sans débit de ce pas non commencé. La connaissance et la zone atteignable sont mises à jour. Il n'y a ni nouveau calcul ni reprise automatique : le joueur donne un nouvel ordre. La précision « aux ressources restantes » est la lecture de « non exécutable ».

**Restent ouverts** [OUV] : un coût réel plus élevé mais encore payable ; le repli d'une diagonale sur le passage Y quand X devient impraticable ; les conditions de la surveillance.

## 7. Choix du chemin

- **G4** [INS] (R:142-147) : TU minimales, puis énergie minimale, puis départage déterministe, parmi les chemins admissibles calculés sur l'état connu.
- **Q4.16=A** [CIT] : après les TU et l'énergie, départage lexicographique des suites de directions dans l'ordre N, NE, E, SE, S, SW, W, NW ; connexions spéciales départagées par identifiant stable ; aucune information cachée exploitée. La priorité « X d'abord » : voir PNV-7.
- **Réserve** [OUV] : sur un graphe fini à coûts positifs ou nuls, le coût minimal existe et un chemin sans répétition l'atteint ; le minimum lexicographique existe parmi ces chemins. La réserve porte sur les **cycles gratuits** (0 TU, 0 énergie), la terminaison de la recherche et le départage, si l'on admet des chemins qui repassent par les mêmes cases. La méthode retenue reste à choisir.
- L'algorithme de recherche est [OUV].

## 8. Orientation, posture et réveil

- **Q4.17=A** [CIT] : l'unité s'oriente vers le pas engagé, sans supplément de TU ni d'énergie ; le volume balayé par la rotation est contrôlé ; les rotations autonomes sont un autre sujet. La définition du volume balayé est [OUV] ; voir aussi PNV-3.
- **Q4.18=A** [CIT] : se coucher, s'agenouiller, se relever sont des actions distinctes, à coûts configurables, soumises à la validité physique ; ni la recherche ni l'exécution d'une marche ne changent la posture.
- Les seuils de ressaut des autres postures, et la marche agenouillée ou couchée, sont [OUV].
- **G2** [INS] (R:135-140) et **Q4.19=A** [CIT] :
  - au réveil sur une case occupée, l'unité va sur la première case voisine admissible, dans l'ordre N, NE, E, SE, S, SW, W, NW : au même niveau, avec un support, un volume admissible et sans chevauchement intérieur avec une unité consciente ;
  - un corps inerte n'empêche pas ce repositionnement ;
  - à défaut, l'unité se réveille sur place, couchée, sans se relever d'elle-même ni relancer de recherche.

  Q4.19 tranche ainsi deux points laissés ouverts par G2 : la case portant un corps, et la correspondance de l'état « au sol » avec une posture (« couché »).
- **Critères restant ouverts pour Q4.19** [OUV] : un mur ou une porte entre les deux cases ; une voisine en diagonale (N2, G1) ; l'état connu face à la vérité cachée ; l'orientation ; le dénivelé admis. L'ordre de traitement de réveils simultanés : PNV-8.

## 9. Effets sur MEC-0002 (à inscrire seulement par un mandat qui la couvre)

| Règle | Effet | Décisions | Provenance |
|---|---|---|---|
| **GE-02** (R:203) | **Modifiée.** La clause « largeur de case et volumes des unités en proportions, sans mètres fixés » est remplacée par des valeurs métriques configurables, communes aux deux fiches : case de 1 500 mm et mur de 100 mm en valeurs initiales. La hauteur de 3 m reste fixe. | B3 (B3-02, rectificatif §2 et §3) ; Q1.1, Q1.3, Q1.5, Q1.7 ; Q4.1 | [DÉC] + [TR] + [CIT] |
| **GE-03** (R:204) | **Précisée.** Dimensions configurables par type et par posture, communes aux deux fiches ; profil humain initial de Q1.6 ; le volume peut dépasser sa case. | B3-03 ; Q1.2, Q1.6 | [DÉC] + [TR] |
| GE-04 (R:205) | inchangée | B3-03 | — |
| GE-05 (R:206) | inchangée ; tolérance [OUV] | B3-04 | — |
| CO-01 (R:265) | inchangée ; une enveloppe ne remplace pas un volume réel | B3-04 | — |
| CH-08 (R:249) | inchangée, compatible : 3 m = 3 000 mm ; les entiers de Q1 ne s'étendent pas aux grandeurs calculées par MEC-0002 | rectificatif B3, §1 | [DÉC] |
| GE-07, CH-14 (R:208, R:255) | **Précisées.** Conversion Force → kg configurable par type, unique pour les deux fiches ; valeurs [OUV] | Q4.5 | [CIT] |
| EN-06 (R:310) | **Précisée.** Ordre en file par identifiant croissant ; chutes secondaires en fin de file ; revalidation selon EN-07 | Q4.4 | [CIT] |
| ES-09, ES-10 (R:286-287) | coûts de terrain fournis par Q3 ; aucune énergie ajoutée à l'esquive | Q3 ; G3 | [TR] ; [INS] |
| ES-08, ES-11, ES-12 ; RP-03, RP-05 ; sauts | inchangées ; l'admissibilité d'une case portant un corps reste du ressort de MEC-0002 | G2 | [INS] |
| « Encore ouvert », ligne Géométrie (R:336) | **À actualiser.** Le principe métrique est décidé (B3) et les valeurs initiales sont sourcées (Q1). Restent ouverts : l'épaisseur des surfaces, la tolérance des contacts, les dimensions des autres types d'unités. | B3 ; Q1 | [DÉC] + [TR] |

## 10. Points ouverts du registre tranchés ou précisés

| Point du registre | Tranché ou précisé par | Ce qui reste ouvert |
|---|---|---|
| R:151, géométrie des murs et passages, portes, taille des unités | Q1.1, Q1.3, Q1.5, Q1.7, Q2.5 ; Q1.2, Q1.6 ; Q4.7 | définition d'un passage « bloqué » pour N2 ; trajectoire (PNV-6, PNV-7) ; tolérance |
| R:152, coûts (terrain, murs, changements de niveau) | Q3.1, Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.3, Q3.10 | coûts de chaque connexion ; autres terrains |
| R:153, escaliers, échelles, ascenseurs | Q2.1 à Q2.4 | profils détaillés des connexions |
| R:160, surcharge | Q3.14 (formule, arrondi) ; Q4.5 (modèle) | table Force → kg ; autres pénalités ; indicateur « encombré » |
| R:161, capital et récupération | Q4.6 (profil initial de test) | valeurs des autres types d'unités |
| R:162, calcul de chemin | Q4.16 (clé de départage) | algorithme ; cycles gratuits |
| R:163, orientation, énergie, interruptions | Q4.17 ; Q3.6, Q3.7 à Q3.9, Q4.6 ; Q4.20 ; Q5.1 | rotations autonomes ; surveillance |
| R:166, trajet devenu non payable | Q4.21, Q3.4 | coût plus élevé mais encore payable |
| R:167, propositions du LOT-2B (paiement de chaque pas avant de le faire) | précisé par Q3.4 (vérification avant chaque pas) et Q3.13 (coût calculé avant le pas) | instant exact du débit |
| G1, « Ouvert » (R:134) | Q1.2, Q1.5, Q1.6 ; Q1.1 ; Q1.3, Q1.7 ; Q3.9 | trajectoire, sous-segments, tolérance, événements pendant la traversée |
| G2, « Ouvert » (R:140) | Q4.19 (ordre, corps, « couché ») ; Q4.18 | critères de la section 8 ; contacts pendant la coexistence |
| G3, « Ouvert » (R:141) | Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.6, Q4.6 | hausse imprévue d'un coût encore payable |
| G4, « Ouvert » (R:147) | Q4.16 | algorithme |
| ARB-C, ARB-D, ARB-E, « Ouvert » (R:123-125) | Q2, Q3.3, Q3.10, Q4.7 ; Q3.14, Q4.5, Q4.6 ; Q5.1, Q4.13 | détails d'interaction ; table Force → kg ; surveillance |
| MEC-0002 | voir le §9 | — |

## 11. Rapport à OXCE

Lecture du code par le LOT-2A, sans exécution. **Aucune fidélité n'est affirmée.**

| Décision | Rapport | Référence |
|---|---|---|
| Q3.7 à Q3.9, G3 | **Écart de principe** : OXCE fait coûter la marche 100 % des TU et 50 % en énergie, tronqué. Bastion a un barème propre, un multiplicateur indépendant et un arrondi supérieur. Les valeurs initiales coïncident avec ⌊TU/2⌋, sauf la diagonale difficile (5 contre 4). Ce n'est qu'une coïncidence. | LOT-2A §2, ligne 6 |
| Q3.7 | Valeur coïncidente : OXCE prend une base de 4 TU quand le coût de la case est nul. | LOT-2A §2, ligne 5 |
| Q4.20 | **Écart** : OXCE arrête la marche quand un nouvel ennemi est repéré. | LOT-2A §2, ligne 16 |
| ARB-E, Q5.1 | Concordance de principe : OXCE arrête la marche sur un tir de réaction. La frontière du pas n'a pas été étudiée. | LOT-2A §2, ligne 16 |
| Q4.21 | Concordance de principe : OXCE arrête si le pas suivant devient impossible. | LOT-2A §2, ligne 16 |
| ARB-C, Q4.7 | **Écart établi** : OXCE ouvre les portes au passage. | R:123 ; `UnitWalkBState.cpp:337-354` |
| G4, Q4.16 | **Écart établi** (inférence) : OXCE ne garantit pas le chemin minimal. | R:142-147 ; LOT-2A §2, ligne 14 |
| ARB-D, Q3.14 | Concordance d'ordre et de troncature | R:111 (N14, « Vérifié ») |
| Autres | non étudiés | — |

## 12. Matrice de traçabilité

| Décision | Sujet | Provenance | Inscrit sur `main` | Scénarios |
|---|---|---|---|---|
| Q1.1 | largeur uniforme, paire, en mm | [TR] | non | T26 |
| Q1.2 | dimensions par type et posture ; dépassement de case | [TR] | non | T26 |
| Q1.3 | épaisseur de mur configurable | [TR] | non | T26 |
| Q1.4 | altitude libre (historique) | [TR] | non | T27 |
| Q1.5 | case de 1 500 mm | [TR] | non | T26 |
| Q1.6 | profil humain | [TR] | non | T26 |
| Q1.7 | mur de 100 mm | [TR] | non | T26 |
| Q1.8 | 3 000 mm (cadre configurable supplanté) | [TR] | non | T27 |
| Q1.9 | ressauts de 200 / 300 mm | [TR] | non | T04 |
| Q2.1 à Q2.4 | escaliers, rampes, échelles, ascenseurs | [TR] | non | T12, T13, T25 |
| Q2.5 | mur centré | [TR] | non | T26 |
| Q2.6 | enveloppe arrondie au pair supérieur | [TR] | non | T26 |
| Q3.1, Q3.2 | barème par terrain ; multiplicateur d'énergie | [TR] | non | T01, T02 |
| Q3.3 | coût par connexion | [TR] | non | T12 |
| Q3.4 | vérification avant chaque pas | [TR] | non | T08 |
| Q3.5 | ordre des événements | [TR] | non | T16 |
| Q3.6 | réserve d'énergie | [TR] | non | T21, T22 |
| Q3.7 à Q3.9 | barème initial | [TR] | non | T01, T02, T18 |
| Q3.10 | pas de barème universel des connexions | [TR] | non | T12 |
| Q3.11 | valeurs d'énergie laissées ouvertes | [TR] | non | — |
| Q3.12 | pas de surcoût de mur | [TR] | non | T06 |
| Q3.13 | ordre des arrondis | [TR] | non | T18, T19 |
| Q3.14 | formule de surcharge | [TR] | non | T20, T21 |
| Q4.1 | hauteur d'étage fixe | [CIT] | non | T27 |
| Q4.2 | contact non bloquant | [CIT] | non | T30 |
| Q4.3 | perte de support | [CIT] | non | T15 |
| Q4.4 | ordre des chutes | [CIT] | non | T16 |
| Q4.5 | conversion Force → kg | [CIT] | non | T31 |
| Q4.6 | profil de ressources | [CIT] ; valeurs [DÉC] | non | T01, T21 |
| Q4.7 | portes | [CIT] ; valeurs [DÉC] | non | T06 |
| Q4.8 à Q4.12 | transferts : occupation, interruption, suspension, paiement, reprise | [CIT] | non | T12, T13 |
| Q4.13 | tir de réaction en transfert | [CIT] | non | T11b |
| Q4.14 | incapacité et support | [CIT] | non | T14 |
| Q4.15 | capacité d'une connexion | [CIT] | non | T24, T25 |
| Q4.16 | départage du chemin | [CIT] | non | T05, T33 |
| Q4.17 | orientation | [CIT] | non | T28 |
| Q4.18 | postures | [CIT] | non | T29 |
| Q4.19 | réveil | [CIT] | non | T10, T36 |
| Q4.20 | révélation | [CIT] | non | T07 |
| Q4.21 | imprévu | [CIT] | non | T08 |
| Q5.1 | tir de réaction pendant un pas | [DÉC] | non | T11a |
| Q5.2 | occupation d'une plateforme | [DÉC] | non | T24 |
| B3 | géométrie commune ; GE-02, GE-03 | [DÉC] | non | T26, T27 |
| ARB-A à ARB-E, G1 à G4 | arbitrages du 17 novembre | [INS] | oui (R:121-147) | T03, T09 à T11, T22, T23 |
| PNV-1 à PNV-9 | formulations sans source | **aucune** | non | T25, T26 et T04 (conditionnels) |

## 13. Scénarios de vérification (non exécutés)

Statut : **Sp** spécifiable ; **Pa** partiel (dépendance indiquée) ; **Ou** ouvert. Les valeurs « fictives » sont des données de test, pas des réglages.

Sauf indication contraire :
- profil initial : 60 TU et 100 d'énergie (Q4.6) ;
- barème du §5 ;
- terrain normal ;
- aucun mur ni unité.

| ID | Situation | Résultat attendu | Sources | Statut |
|---|---|---|---|---|
| T01 | un pas orthogonal | 4 TU et 2 d'énergie débités, il reste 56 et 98 | Q3.7, G3 | Sp |
| T02 | une diagonale en terrain difficile, passage praticable | 9 TU et 5 d'énergie, il reste 51 et 95 ; écart avec la loi d'OXCE, qui donnerait 4 d'énergie | Q3.8, Q3.9, Q3.13, S2 | Sp |
| T03 | diagonale permise par N2, mais volume bloqué par une unité consciente dans le seul passage ouvert | refus, sans débit | ARB-A, G1, Q3.4 | Pa (géométrie, PNV-6) |
| T04 | ressauts de +200 mm et −300 mm, humain debout ; puis de +201 mm et −301 mm | admis si volumes et support valides ; au-delà, résultat dépendant de PNV-5 | Q1.9 | Pa |
| T05 | destination à deux cases à l'est et une au nord ; chemins [NE, E] et [E, NE], chacun à 10 TU et 5 d'énergie | [NE, E] est retenu | Q4.16, G4 | Sp (sur la formulation résumée de Q4.16) |
| T06 | porte ordinaire fermée sur le trajet | ouverture explicite à 4 TU et 0 énergie ; aucun pas automatique ensuite ; aucune ouverture pendant la marche | Q4.7, ARB-C, Q3.12 | Sp |
| T07 | ennemi caché révélé hors du trajet, sans tir | la marche continue | Q4.20 | Sp |
| T08 | obstacle inconnu devant le pas suivant | arrêt, révélation, pas suivant non débité, aucune reprise automatique | Q3.4, Q4.21, S8, S9 | Sp |
| T09 | corps mort ou inconscient sur la case de destination | traversée et arrêt possibles ; aucun impact du seul fait du chevauchement ; volume conservé pour MEC-0002 | ARB-B | Sp |
| T10 | réveil sur une case occupée : (a) N libre ; (b) N occupée, NE libre ; (c) aucune voisine | (a) N ; (b) NE ; (c) couché sur place, sans se relever tant que la case est occupée | G2, Q4.19 | Pa (critères ouverts de Q4.19) |
| T11a | ordre de trois pas orthogonaux ; tir de réaction manqué pendant le premier | premier pas achevé jusqu'à sa destination ; il reste 56 TU et 98 d'énergie ; ordre interrompu ; deuxième pas ni exécuté ni débité | Q5.1, ARB-E | Sp (tir simulé) |
| T11b | tir de réaction manqué pendant un transfert | action interrompue ; position atteinte et coût du transfert conservés ; pas d'arrivée complétée | Q4.13, Q4.9, Q4.11 | Pa (profil de connexion) |
| T12 | transfert payé puis interrompu, l'unité restant soutenue | état suspendu ; la reprise dans le même sens n'est pas refacturée | Q4.10 à Q4.12 | Pa (profil de connexion) |
| T13 | retour vers l'entrée depuis un état suspendu | nouvelle action, avec un nouveau coût | Q4.12 | Pa (chemin et coût du retour) |
| T14 | plateforme soutenant une unité devenue inconsciente | pas de chute automatique | Q4.14 | Sp |
| T15 | support détruit pendant un pas engagé | arrêt immédiat à la position physique du moment ; relais à MEC-0002 ; pas engagé débité | Q4.3 | Pa (support pendant le pas) |
| T16 | trois chutes nées d'un même événement, puis une chute secondaire | file par identifiant croissant ; la chute secondaire en fin de file ; revalidation selon EN-07 | Q4.4, EN-06, EN-07 | Sp |
| T17 | esquive de MEC-0002 | coût habituel de la marche en TU ; aucune énergie | ES-09, ES-10, G3 | Sp |
| T18 | base fictive de 3 TU et 1 d'énergie, terrain difficile | orthogonal : 5 TU et 2 d'énergie ; diagonal : 7 TU et 3 d'énergie. L'option B, écartée, donnerait 6 TU en diagonale | Q3.13 | Sp |
| T19 | coût d'arrivée fictif de 5 TU, pas diagonal | 7 TU | S2, Q3.13 | Sp |
| T20 | surcharge, valeurs fictives : capacité 30 kg, charge 40 kg, total 60 ; charge nulle ; total 22, capacité 15, charge 22 | 45 ; 60 ; 15 (un calcul naïf en virgule flottante donne 14) | Q3.14 | Sp |
| T21 | plafond d'ARB-D, valeurs fictives avec un maximum de 20 : (solde 7, récupération 15, facteur 0,75) ; (2, 15, sans surcharge) ; (4, 12, 0,75) ; (total 20, facteur 30/45) | 15 ; 17 ; 12 ; 13. Avec le profil Q4.6 (60 récupérées sur 60), le plafond n'est jamais exercé | ARB-D, Q3.14 | Sp |
| T22 | carte de 2 × 2 cases, départ et arrivée aux coins opposés, arrivée en terrain normal, cases intermédiaires difficiles ; budget de 20 TU et 2 d'énergie ; variante avec 3 d'énergie | diagonale à 6 TU et 3 d'énergie, détours à 10 TU et 5 d'énergie : aucun chemin admissible, destination hors zone ; variante : la diagonale seule devient admissible | G3, Z1 | Sp (passages praticables) |
| T23 | candidats injectés A (17 TU, 11 d'énergie) et B (18 TU, 2 d'énergie) ; budget de 20 TU et 12 d'énergie, puis de 20 TU et 10 d'énergie | A, puis B | G4 | Sp (sélection abstraite) |
| T24 | plateforme à deux emplacements, capacité 2, deux unités conscientes ; plateforme à un emplacement, deuxième unité | admises ; deuxième unité refusée | Q5.2, Q4.15, S10 | Pa (relation emplacement / case) |
| T25 | connexion dont la capacité est déjà atteinte | admission refusée | Q4.15, Q4.8 | Sp |
| T26 | géométrie des valeurs initiales | largeur intérieure de 1 400 mm ; enveloppes de 1 274 mm (couché) et de 850 mm à 45° ; volumes de Q1.6 | Q1.1 à Q1.3, Q1.5 à Q1.7, Q2.5, Q2.6 | Pa (l'angle de 45° dépend de PNV-3) |
| T27 | deux étages tactiques consécutifs | 3 000 mm entre sols de référence ; les dénivelés locaux sont distincts | GE-02, Q4.1 | Sp |
| T28 | pas après une orientation opposée | aucun supplément : 4 TU et 2 d'énergie | Q4.17 | Pa (volume balayé) |
| T29 | ordre de marche donné à une unité agenouillée | aucun changement automatique de posture | Q4.18 | Pa (marche dans les autres postures) |
| T30 | deux volumes tangents | marche permise ; contact détecté ; pas de dégât | Q4.2, GE-05 | Sp |
| T31 | même unité, surcharge de MEC-0001 et seuil CH-14 | même capacité Force → kg | Q4.5, CH-14 | Pa (table ouverte) |
| T32 | destination sélectionnée dans la zone, sans imprévu | destination atteinte ; TU et énergie dépensées inférieures ou égales aux budgets | G3, Z1 | Sp |
| T33 | deux chemins de même coût ne différant que par la connexion empruntée | celui de la connexion à l'identifiant stable le plus petit | Q4.16 | Sp (sur la formulation résumée) |
| T34 | cycle de connexions à 0 TU et 0 d'énergie | recherche qui se termine, résultat déterministe | G4, Q4.16 | Ou (méthode à choisir) |
| T35 | ennemi repéré, puis perdu de vue | aucun repère persistant de sa dernière position | S12 | Sp (visibilité simulée) |
| T36 | réveil ; la seule voisine libre porte un corps inerte | repositionnement sur cette case | Q4.19, ARB-B | Sp |

Les anciennes matrices sont historiques : celle du LOT-2F (son bandeau le dit) et celle du §5 de la v1.4.1. Celle de la v1.4.1 donnait 1 d'énergie au pas orthogonal normal, contre 2 dans Q3.7. Ses cas encore pertinents sont repris ici. Son contre-exemple G1-05 dépend de PNV-7.

## 14. Réserves et points ouverts

**Réserves documentaires :**
- **RD-1 — Archivage.** Aucune pièce du §15 n'est archivée. C'est un préalable à toute inscription : le registre exige une preuve explicite, datée et vérifiable.
- **RD-2 — Formulations de Q4.** Ce sont des résumés de l'orchestrateur, sauf les valeurs de Q4.6 et Q4.7. Cela touche PNV-7 (Q4.16) et PNV-8 (Q4.19).
- **RD-3 — Q5.1, Q5.2 et B3.** Le texte des options d'origine n'est pas joint.
- **RD-4 — Les neuf formulations PNV** (§3.5) ne valent pas règle.
- **RD-5 — Q1.1 à Q1.4.** Seules les options retenues ont été transmises, pas les options écartées.
- **RD-6 — Revue.** La v0.3 n'a pas été revue ; aucun test n'a été exécuté.

**Points ouverts** [OUV], sans décision attendue pour la consolidation :
- **Pas :** instant de l'engagement ; support pendant les phases du pas.
- **Chemin :** cycles gratuits, terminaison et départage ; algorithme de recherche.
- **Géométrie :** bornes des dénivelés et rattachement d'une case à un étage ; volume balayé par la rotation ; grille de conversion et précision des calculs, y compris ceux de MEC-0002 ; définition d'un passage « bloqué » pour N2 ; tolérance de GE-05.
- **Réveil :** critères ouverts de Q4.19 ; relation emplacement / case (Q5.2).
- **Imprévus :** coût plus élevé mais encore payable ; repli d'une diagonale sur le passage Y.
- **Postures :** seuils et marche des autres postures.
- **Réserves conservées de la v0.2 :**
  - **RF-01 :** profils de connexions (complété ici par le déclenchement de la reprise, le réveil dans une connexion, et le chemin et le coût d'un retour partiel) ;
  - **RF-02 :** coûts et géométrie des changements de posture et des rotations autonomes ;
  - **RF-03 :** table Force → kg et données physiques des unités ;
  - **RF-04 :** cas limites des coûts ;
  - **RF-05 :** interfaces avec MEC-0002.
- **Autres :** surveillance (Overwatch) ; autres pénalités de surcharge ; indicateur « encombré ».

**Hors périmètre, inchangé depuis la v0.2 :** équilibrage des autres unités, interface, animations, détail de la surveillance, dégâts de chute et de collision complets, stabilité des bâtiments hors événements EN.

## 15. Pièces justificatives à archiver

**A. Textes transmis** (proposition et validation d'origine), à archiver tels que reçus le 19 novembre 2026. L'indication horaire donnée (14 h 26 à 14 h 47 UTC) sert seulement à les identifier.
1. **Q1.1 à Q1.4** : texte des options retenues, et message « Pour Bastion MEC-0001, lot Q1 Géométrie, je valide Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A. […] ». Les options écartées ne sont pas jointes.
2. **Q1.5 à Q1.9** : propositions A, B et C avec leur paragraphe de portée, et message « […] lot Q1 Géométrie, je valide les paramètres initiaux suivants : Q1.5 largeur de case=1500 mm ; Q1.6 profil humain=A ; Q1.7 mur standard=100 ; Q1.8 écart de référence des niveaux=3000 ; Q1.9 seuils de ressaut=A. […] ».
3. **Q2.1 à Q2.6** : propositions, et message « […] lot Q2, je valide Q2.1=A […] Q2.6=A (arrondi AABB). […] ».
4. **Q3.1 à Q3.6** : propositions et paragraphe « Portée de cette validation », et message « […] lot Q3 Ressources et événements, je valide Q3.1=A, […] Q3.6=A. […] ».
5. **Q3.7 à Q3.12** : propositions, et message « […] je valide Q3.7=A, Q3.8=A, Q3.9=A, Q3.10=B, Q3.11=B, Q3.12=A. […] ».
6. **Q3.13 et Q3.14** : propositions avec l'exemple fictif, et message « […] je valide Q3.13=A concernant les arrondis et Q3.14=A concernant la formule de surcharge ARB-D. […] ».

**B. Validations citées, sans la proposition d'origine :**
7. **Q4.1 à Q4.21** : les six messages reproduits au §12 de la v0.2, de « […] audit Q4, je valide Q4.1=A […] » à « […] audit Q4-B, je valide Q4.16=A […] Q4.21=A (imprévu). […] ». Les propositions d'origine manquent ; les formulations sont celles des §5 à §8 de la v0.2.
8. *Déjà archivé sur `main` :* les citations d'ARB-A à ARB-E et de G1 à G4, au §1.2 de `docs/reviews/BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md`.

**C. Déclarations du propriétaire, sans la proposition d'origine :**
9. **Valeurs de Q4.6 et Q4.7** : message « […] Pour Q4.6 et Q4.7, les valeurs 60/60/100/20 et 4 TU/0 énergie figuraient expressément dans les propositions acceptées par option A. […] ».
10. **Q5.1=A et Q5.2=A** : message « Pour Bastion MEC-0001, prends en compte les précisions suivantes […] », puis « Addendum documentaire Q5.1–Q5.2 et rectifications de la revue ».
11. **B3=A** : « Addendum B3 — Géométrie physique commune à MEC-0001 et MEC-0002 », puis « Rectificatif de l'addendum B3 ».

**D. Documents de travail à archiver :**
12. La consolidation Q1–Q4 v0.2 (SHA-256 `062c5e9c…a2a1`).
13. Le mandat de revue indépendante Q1–Q4, transmis en texte.
14. Les rapports de revue et de vérification du 19 novembre : la revue indépendante Q1–Q4, les mises à jour n° 1 et n° 2, les vérifications de provenance.
15. La présente v0.3, après revue.

## 16. Journal des corrections intégrées depuis la v0.2

| N° | Origine | Correction | Où |
|---|---|---|---|
| C-01 | anomalie 1 | énoncés rattachés à leurs sous-numéros et à leur niveau de preuve ; « acceptée » justifié par Q3.13 | §0, §3 à §8 |
| C-02 | anomalie 2, addendum Q5 (point 1) | Q5.1 intégrée ; quatre états d'un pas ; instant d'engagement déclaré ouvert | §6 |
| C-03 | anomalie 3, addendum Q5 (point 2) | Q5.2 intégrée ; aucune exception à S10 ; relation emplacement / case ouverte ; portée de « volontaire » | §4 |
| C-04 | anomalie 4, addendum Q5 (point 3), B3 | B3 intégrée ; GE-02 et GE-03 identifiées explicitement | §3.1, §9 |
| C-05 | anomalie 5 | tableau des points ouverts tranchés | §10 |
| C-06 | anomalie 6 | statut des valeurs : initiales et configurables, sauf la hauteur d'étage | §3.1, §5 |
| C-07 | anomalie 7 | scénarios complétés (T18 à T36), T11 scindé, chemin attendu dans T05 | §13 |
| C-08 | anomalie 8, corrigée, et addendum Q5 (point 4) | réserve limitée aux cycles gratuits, à la terminaison et au départage | §7 |
| C-09 | anomalie 9 | bornes des dénivelés et rattachement à un étage déclarés ouverts | §3.2 |
| C-10 | anomalie 10 | critères ouverts de Q4.19 | §8 |
| C-11 | anomalie 11 | « aux ressources restantes » ; coût payable et repli sur Y déclarés ouverts | §6 |
| C-12 | anomalie 12 | volume balayé ouvert, avec la remarque des 1 341,6 mm | §3.6, §8 |
| C-13 | anomalie 13 | coût d'entrée = case d'arrivée ; arithmétique exacte (T20) ; grille de conversion en PNV-2 | §5, §3.5 |
| C-14 | anomalie 14 | « X puis Y » en PNV-7 ; G1-05 conditionnel | §3.5, §13 |
| C-15 | anomalie 15 | rapport à OXCE | §11 |
| C-16 | anomalie 16 | anciens identifiants P1 à P4 remplacés par les codes du §0 ; réserves RF complétées | §0, §14 |
| C-17 | B3, point 1 | unités compatibles avec CH-08 ; entiers non étendus à MEC-0002 | §9 |
| C-18 | B3, point 2 | source de la hauteur d'étage : GE-02, puis Q4.1 | §3.2 |
| C-19 | B3, point 3, et ligne R:336 | points ouverts de GE-02, GE-03 et R:336 actualisés | §9 |
| C-20 | B3, point 4 | configurations admissibles : parité sourcée par Q1.1, le reste ouvert | §3.1 |
| C-21 | provenance | « le volume peut dépasser sa case » (Q1.2) | §3.1 |
| C-22 | provenance | chronologie GE-02 → Q1.4 → Q1.8 → Q4.1 | §3.2 |
| C-23 | provenance | Q2.5 et Q2.6 citées | §3.3 |
| C-24 | provenance | rédactions de Q2.1 à Q2.3 complétées | §4 |
| C-25 | provenance | terminologie de D:67 alignée sur Q3.4 et Q5.1 | §6 |
| C-26 | provenance | phrase omise de Q3.13 ; formulation de Q3.12 | §5, §4 |
| C-27 | provenance | énergie non réduite par la surcharge présentée comme lecture d'ARB-D | §5 |
| C-28 | provenance | lien entre Q3.11 et Q4.6 | §5 |
| C-29 | provenance | ligne « Réaction » de l'ancienne matrice rattachée à ARB-E, Q5.1 et Q4.13 | §12 |
| C-30 | provenance | hauteur d'étage retirée des valeurs configurables de B3-02 | §3.2 |
| C-31 | addendum Q5 (point 5) | corrections omises intégrées : C-01, C-10, C-11, C-13 à C-16 | ci-dessus |

**Aucune règle nouvelle :** chaque énoncé décisionnel porte une source [INS], [TR], [CIT] ou [DÉC] ; les autres sont marqués [PNV], [OUV] ou [DÉD].

## 17. Points à contrôler en priorité par le relecteur

1. La fidélité des 29 décisions [TR] au texte transmis.
2. La chronologie de la hauteur d'étage et la règle applicable (§3.2).
3. Le classement des neuf formulations PNV, et l'absence de règle ajoutée.
4. Les effets sur MEC-0002 (§9), en particulier GE-02 et GE-03.
5. Les calculs des scénarios T01 à T36.
6. L'exhaustivité du journal des corrections et de la liste des pièces à archiver.
7. La cohérence de Q5.1, Q5.2 et B3 avec le registre.
