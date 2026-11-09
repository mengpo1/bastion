# LOT-2F — Spécification documentaire de `MEC-0001` : verticalité, sauts offensifs, chutes, esquives et collisions

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2F-v1.0.md`, fichier joint par le propriétaire. Archivé octet pour octet dans `docs/mandates/`, SHA-256 `a68395e12475b364bb442c0ee66199404a86f743b9cca45fbcb9bd7f309bd3b5`. |
| Autorisation | Propriétaire, 9 novembre 2026 : « Je l'autorise », en réponse au modèle d'autorisation proposé (exécution, archivage, rapports, revue, branche poussée et PR en brouillon, sans fusion). |
| Branche | `docs/lot-2f-mec-0001-specification`, créée depuis `origin/main` = `4077db2f8ec8cd47b06091ae37f5db3d85a8d964` (après `git fetch origin main`). |
| Source des décisions du 9 novembre | La **synthèse du §3 du mandat**, attribuée au mandat. La conversation du 9 novembre n'a pas été fournie : **aucune comparaison avec elle n'a été faite**. |
| Référence OXCE | `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` (8.7.1), règles `xcom1`, options par défaut. Lecture du code seulement, **aucune exécution**. |
| Nature | Documentaire. **Aucune décision inscrite au registre, aucun gameplay, aucun test exécutable.** Au registre, `MEC-0001` reste « reportée ». |
| Compagnon | Matrice de tests : `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md`. |
| Correctif | Demande de correctif documentaire du propriétaire, reçue le 9 novembre 2026 après la revue de l'orchestrateur, sur la même branche et la même PR (n° 9). Elle confirme trois décisions présentées par le propriétaire comme déjà validées : E14 (ennemi actuellement visible ciblable), E18 (chute au sol de l'attaquant après une esquive) et E23 (contenu du poids total `M`). Voir §6. |

## 0. En bref

- **Traçabilité (§2)** : 62 règles et 7 décisions historiques, réparties en 7 familles :
  - marche et verticalité du registre ;
  - saut offensif ;
  - modèle physique ;
  - esquive et collisions ;
  - dégâts ;
  - information ;
  - historique.
- **Contradictions historiques** :
  - **N7** (registre : pas de dégâts pour les petites chutes) est **contredite** par les dégâts dès un étage (D01) ;
  - la **portée fixe de deux cases** (décision antérieure, non inscrite au registre) est **remplacée** par une référence à 1 g et à un étage de descente (P05, P06).
- **Formules transcrites (§3)** :
  - dégâts de base `B(n)` ;
  - plafonds ;
  - bonus `× 1,25` ;
  - coût offensif `max(1, ⌊0,20 × TU_max⌋)` ;
  - facteur de poids `min(M/80, 3)` contre un obstacle ;
  - élévation de référence `H/4` à 1 g.
- **Formules manquantes, classées « ouvert » (§5)** :
  - conversion de la portée ;
  - arrondis ;
  - rapport de poids entre deux unités ;
  - conversion d'un choc en puissance ;
  - coût de déplacement d'un saut ;
  - type de dégâts ;
  - échelle physique.
- **OXCE (§4)** : le tirage « explosion », l'enchaînement des dégâts et la résistance du terrain ont été lus dans le code. Aucune règle propre à Bastion n'est attribuée à OXCE.
- **Points ouverts (§5)** : 24 points, dont 3 tranchés par le correctif du propriétaire (E14, E18, E23) ; 21 restent ouverts, dont 13 bloquants pour des tests exacts.

## 1. Sources, statuts et conventions

**Sources.**
- **R** : registre `docs/gameplay/GAMEPLAY-DECISIONS.md` (S1 à S12, Z1, N1 à N14).
- **M** : mandat LOT-2F, §3 (synthèse de travail des décisions du 9 novembre, non comparée à la conversation).
- **E** : rapport LOT-2E.
- **A** : rapport LOT-2A.
- **C** : lecture du code OXCE pour ce lot (§4).
- **P** : demande de correctif du propriétaire, reçue le 9 novembre 2026 après la revue de l'orchestrateur. Elle confirme trois décisions présentées comme déjà validées, sans en préciser la date de validation initiale.

**Statut de la règle.**
- **validé (R)** : sous-décision acceptée au registre, tandis que `MEC-0001` reste globalement « reportée ».
- **validé (M)** : décision du 9 novembre selon le §3 du mandat.
- **validé (P)** : décision confirmée par la demande de correctif du propriétaire.
- **proposition technique (non validée)** : formulation de Claude Code.
- **ouvert** : non arbitré, ou déclaré « à formaliser », « à vérifier » ou « provisoire » par le mandat.
- **contredit** : remplacé par une décision plus récente.
- Pour les décisions historiques du §2.7 seulement :
  - **historique** : déjà supplantée au registre ;
  - **concordant** : précisée par une décision plus récente, sans contradiction ;
  - **nuancé** : restreinte par une décision plus récente, sans être remplacée.

**Catégorie.**
- **référence OXCE** : le comportement lu dans le code d'OXCE (VC) concorde dans son principe ; aucune fidélité observée.
- **adaptation Bastion** : règle propre à Bastion.
- **non établi** : rapport à OXCE inconnu.

**Preuve OXCE.** VC (lecture du code), INF (inférence), NV (non vérifié). Aucune observation à l'exécution (OE).

## 2. Matrice de traçabilité (A)

Les identifiants des tests renvoient à la matrice `LOT-2F-MATRICE-TESTS-MEC-0001.md`.

### 2.1 Marche et verticalité (registre)

| ID | Règle courante | Source | Statut | Catégorie | Tests |
|---|---|---|---|---|---|
| M01 | Huit directions, diagonales incluses | R : S1, N1 | validé (R) | référence OXCE (A §2 l. 2) | T-M01 |
| M02 | Pas en diagonale : coût de la case d'arrivée × 1,5, arrondi à l'inférieur | R : S2 | validé (R) | référence OXCE (A §2 l. 4) | T-M02 |
| M03 | Diagonale permise si au moins un des deux passages orthogonaux est ouvert ; interdite si les deux sont bloqués | R : S3, N2 | validé (R) | adaptation Bastion (écart établi, R : N2) | T-M03, T-M04 |
| M04 | Une unité voisine n'est pas un obstacle pour la diagonale | R : S4 | validé (R) | référence OXCE (A §2 l. 3) | T-M05 |
| M05 | Terrain en cases et murs séparant les cases | R : N1 | validé (R) | référence OXCE, dans le principe (A §2 l. 11) | T-M03 |
| M06 | Plusieurs niveaux ; positions (x, y, z) | R : N3 | validé (R) | référence OXCE (A §2 l. 1) | T-J02 |
| M07 | Escaliers, échelles et ascenseurs prévus | R : N4 | validé (R) ; règles précises ouvertes | escaliers et échelles : référence OXCE dans le principe (E) ; ascenseurs : non établi | — |
| M08 | Zone atteignable selon les TU et les informations connues ; destination hors zone non sélectionnable. S5 (déplacement partiel) est supplantée pour la sélection normale. | R : Z1, S5 | validé (R) | adaptation Bastion (écart établi) | T-M06, T-I03 |
| M09 | Destinations : cases visibles ou déjà explorées | R : S6 | validé (R) | non établi | T-M08 |
| M10 | Trajet en cases visibles ou déjà explorées | R : S7 | validé (R) ; application aux sauts : ouvert (E15) | non établi | T-M08 |
| M11 | Trajet sur le dernier état connu ; interruption devant un obstacle inconnu | R : S8 | validé (R) | non établi | T-M07 |
| M12 | Un obstacle inconnu rencontré devient connu | R : S9 | validé (R) | non établi | T-M07, T-I05 |
| M13 | Case occupée par une autre unité : infranchissable pour la traversée comme pour la destination (S10). Le mandat restreint cette règle à la « marche normale » et demande de circonscrire les exceptions des sauts offensifs. Exceptions validées : J05, J07 et J13. Les cas dynamiques (case devenue occupée pendant le vol) restent ouverts (E9, T-X01). | R : S10 ; M §3.1 ; P | validé (R) ; restriction à la marche normale : validé (M) ; exceptions : validé (M, P) (H07) | référence OXCE (A §2 l. 12) | T-M09, T-J11, T-J12, T-J14 |
| M14 | Une unité cachée rencontrée est révélée | R : S11 | validé (R) | non établi | T-M10 |
| M15 | Une unité révélée redevient cachée lorsqu'elle n'est plus observable | R : S12 | validé (R) | non établi | — |
| M16 | Surcharge selon OXCE : poids de l'armure + inventaire ; rapport Force / charge sur la récupération des TU ; ni seuil d'immobilisation ni surcoût par pas | R : N10 à N14 ; M §3.1 | validé (R) ; transposition exacte ouverte | référence OXCE (VC, LOT-2D) | T-M11 |

### 2.2 Saut offensif (M §3.2)

| ID | Règle courante | Source | Statut | Catégorie | Tests |
|---|---|---|---|---|---|
| J01 | L'attaque par saut exige au moins un étage de dénivelé vers le bas | M §3.2 | validé (M) | adaptation Bastion | T-J01 |
| J02 | La destination est choisie librement parmi les cases atteignables | M §3.2 | validé (M) | adaptation Bastion | T-J02, T-J03 |
| J03 | Une case explorée mais non visible peut être visée à l'aveugle | M §3.2 | validé (M) | adaptation Bastion | T-J15 |
| J04 | Une case jamais explorée ne peut pas être choisie | M §3.2 ; R : S6 | validé (M) | adaptation Bastion | T-J16 |
| J05 | Un ennemi caché sur la case visée peut être percuté et révélé (exception à S10) | M §3.2 | validé (M) | adaptation Bastion | T-J12 |
| J06 | Les alliés et neutres identifiés ne peuvent pas être ciblés volontairement | M §3.2 | validé (M) | adaptation Bastion | T-J13 |
| J07 | Un allié ou un neutre caché sur une case visée à l'aveugle peut être percuté (exception à S10) | M §3.2 | validé (M) | adaptation Bastion | T-J14 |
| J08 | Le bonus offensif s'applique aussi à un allié ou un neutre caché percuté | M §3.2 | validé (M) | adaptation Bastion | T-D06 |
| J09 | Coût additionnel `max(1, ⌊0,20 × TU_max⌋)`, en plus du déplacement, dépensé à l'engagement, même en cas d'échec ou d'esquive | M §3.2 | validé (M) ; coût du déplacement du saut : ouvert (E13) | adaptation Bastion | T-J17, T-J18 |
| J10 | TU insuffisantes : attaque impossible | M §3.2 | validé (M) ; seuil exact ouvert (E13) | adaptation Bastion | T-J19 |
| J11 | Bonus `× 1,25` sur les dégâts infligés à la cible, après le plafond et avant le tirage aléatoire | M §3.2, §3.5 | validé (M) | adaptation Bastion | T-D05 |
| J12 | Aucun bonus sur les blessures de l'attaquant | M §3.2 | validé (M) | adaptation Bastion | T-D05 |
| J13 | Une attaque par saut peut viser un ennemi **actuellement visible** : exception explicite à S10 | P | validé (P) | adaptation Bastion | T-J11 |

### 2.3 Modèle physique du saut (M §3.3)

| ID | Règle courante | Source | Statut | Catégorie | Tests |
|---|---|---|---|---|---|
| P01 | Gravité configurable selon l'environnement, initialement 1 g (≈ 9,81 m/s²) | M §3.3 | validé (M) ; g = 0 et gravité hors plage : ouvert (E3) | adaptation Bastion | T-X05 |
| P02 | Modèle balistique simplifié : impulsion verticale initiale constante pour une même unité et une même action | M §3.3 | validé (M) ; sens d'« impulsion » ouvert (E11) | adaptation Bastion | T-J05 |
| P03 | La composante horizontale s'adapte à la destination, dans les limites des capacités de saut | M §3.3 | validé (M) ; limites ouvertes (E2) | adaptation Bastion | T-J04 |
| P04 | À 1 g, élévation maximale de référence : ¼ de la hauteur d'un étage ; plus haute si la gravité est moindre, plus basse si elle est plus forte | M §3.3 | validé (M) | adaptation Bastion | T-J05 |
| P05 | À 1 g et pour un étage de descente, portée de référence : 2 cases selon Manhattan (`|Δx| + |Δy|`) | M §3.3 | validé (M) | adaptation Bastion | T-J02, T-J03 |
| P06 | La portée dépend de la gravité et du dénivelé réel ; règles de conversion à formaliser | M §3.3 | validé (M) dans le principe ; conversion ouverte (E2, E5) | adaptation Bastion | T-J04 |
| P07 | Arc calculé sans contournement des obstacles ; un obstacle bas est franchi si tout le volume de l'unité le survole ; un mur, un sol ou un plafond qui coupe ce volume bloque | M §3.3 | validé (M) ; dimensions ouvertes (E1) | adaptation Bastion | T-J08, T-J09 |
| P08 | Obstacle connu bloquant : action interdite avant engagement. Obstacle non détecté : action engagée puis interrompue à l'impact, l'obstacle étant révélé | M §3.3 | validé (M) | adaptation Bastion | T-J06, T-J07 |

### 2.4 Esquive et collisions (M §3.4)

| ID | Règle courante | Source | Statut | Catégorie | Tests |
|---|---|---|---|---|---|
| K01 | Collision possible après une chute accidentelle ou un saut volontaire | M §3.4 | validé (M) | adaptation Bastion (OXCE écarte l'unité dessous ou la met hors de combat : E C7) | T-D12 |
| K02 | Les deux unités peuvent subir des dégâts distincts et de l'étourdissement | M §3.4 | validé (M) | adaptation Bastion | T-K04 |
| K03 | Esquive automatique seulement si la cible voit **actuellement** l'unité qui tombe, a les TU du pas et dispose d'une case voisine libre et accessible | M §3.4 | validé (M) ; précisions ouvertes (E17) | adaptation Bastion | T-K01 |
| K04 | Choix aléatoire d'une case valide | M §3.4 | validé (M) ; loi du tirage ouverte | adaptation Bastion | T-K05 |
| K05 | Probabilité fondée sur les Réactions, + 5 points de pourcentage par niveau traversé, bornée à [0, 100]. Formulation provisoire : `clamp(Réactions + 5 × |z_dép − z_arr|, 0, 100)` % | M §3.4 | validé (M) dans le principe ; formulation exacte ouverte (E12) | adaptation Bastion | T-K02, T-K06 |
| K06 | Esquive réussie : la cible se déplace et paie les TU du pas, ne subit pas le choc ; l'attaquant termine par une chute au sol, selon les règles de la chute au sol : plafond de 70 sur les dégâts de base, appliqué avant le tirage | M §3.4 ; P | validé (M, P) | adaptation Bastion | T-K03 |
| K07 | Esquive échouée : cible immobile, aucune TU dépensée pour l'essai, collision résolue | M §3.4 | validé (M) | adaptation Bastion | T-K04 |
| K08 | Le poids influe sur les dégâts des deux unités, sans désigner mécaniquement la plus blessée | M §3.4 | validé (M) dans le principe ; formule ouverte (E6) | adaptation Bastion | T-D14 |

### 2.5 Dégâts (M §3.5)

| ID | Règle courante | Source | Statut | Catégorie | Tests |
|---|---|---|---|---|---|
| D01 | Chute blessante possible dès un étage | M §3.5 | validé (M) ; **contredit N7** (H01) | adaptation Bastion (OXCE : aucun calcul identifié, E C8) | T-D01 |
| D02 | La nature du sol n'influence pas les dégâts | M §3.5 | validé (M) | adaptation Bastion | T-D08 |
| D03 | Base : 8 à un étage ; premier incrément 6 ; chaque incrément suivant × 1,35 | M §3.5 | validé (M) | adaptation Bastion | T-D01, T-D02 |
| D04 | `B(n) = 8 + 6 × Σ(k=0..n−2) 1,35^k`, somme vide pour n = 1, avant arrondi | M §3.5 | validé (M) ; arrondi ouvert (E5) | adaptation Bastion | T-D02 |
| D05 | Plafonds avant le tirage : chute au sol 70, unité qui tombe dans une collision 60, unité percutée 80, impact contre un obstacle 70 | M §3.5 | validé (M) ; base des collisions entre unités ouverte (E8) | adaptation Bastion | T-D03 |
| D06 | Tirage aléatoire « type explosion OXCE » : 50 à 150 % de la puissance tirée | M §3.5 | validé (M) ; nombres entiers ouverts (E5) | référence OXCE pour le tirage (C : §4) | T-D04 |
| D07 | Conversion finale en santé et en étourdissement : le mandat décrit les règles distinctes du moteur, sans écrire qu'elles sont reprises dans Bastion | M §3.5 | ouvert (E7) : reprise implicite, à confirmer | référence OXCE (C : §4) | T-D13 |
| D08 | En collision volontaire, bonus `× 1,25` après le plafond, avant le tirage | M §3.5 | validé (M) | adaptation Bastion | T-D05, T-D07 |
| D09 | Facteurs de poids et protection de l'armure ensuite, « selon l'ordre accepté » ; ordre numérique précis et type de dégâts à formaliser | M §3.5 | validé (M) dans le principe (après le tirage) ; ordre et formules ouverts (E6, E7, E24) | non établi | T-D13, T-D14 |
| D10 | Choc contre un obstacle : puissance commune selon la vitesse réelle au point de contact et le « poids total `M` (équipement inclus) » ; facteur `min(M/80, 3)` (référence universelle 80 kg, sans minimum) ; ce n'est pas le rapport de masses entre deux unités | M §3.5 ; P | validé (M) pour le facteur ; contenu de `M` validé (P) : poids propre de l'unité + armure + équipement et inventaire ; formule de puissance ouverte (E8) | adaptation Bastion | T-D09 |
| D11 | Distinguer la vitesse normale à la surface de la vitesse tangentielle ; phases début, milieu et fin pour le diagnostic seulement | M §3.5 | validé (M) | adaptation Bastion | T-J10 |
| D12 | Obstacle destructible endommagé ou détruit selon les règles de résistance du terrain d'OXCE ; obstacle indestructible épargné | M §3.5 | validé (M) | référence OXCE (C : §4) | T-D10, T-D11 |
| D13 | Le saut s'arrête à l'impact, même si l'obstacle est détruit ; puis chute verticale depuis le point de contact si l'unité est sans support ; dégâts d'impact et de chute résolus séparément | M §3.5 | validé (M) | adaptation Bastion | T-D12 |

### 2.6 Information et interface (M §3.6)

| ID | Règle courante | Source | Statut | Catégorie | Tests |
|---|---|---|---|---|---|
| I01 | N'afficher que l'information connue ; aucune fuite sur une unité ou un obstacle cachés | M §3.6 | validé (M) | adaptation Bastion | T-I01, T-I02, T-I04 |
| I02 | Prévisualiser destination, trajectoire estimée et coût en TU, dans les limites de la connaissance courante | M §3.6 | validé (M) ; coût du saut ouvert (E13) | adaptation Bastion | T-I02 |
| I03 | Résolution chronologique : trajectoire, impacts, esquives, atterrissages, pertes de support, collisions ultérieures | M §3.6 | validé (M) | adaptation Bastion | T-D12 |
| I04 | Destination devenue occupée, plusieurs unités sur le trajet, atterrissage sans support : cas identifiés, sans résultat automatique | M §3.6 | ouvert (E9) | non établi | T-X01 à T-X03 |

### 2.7 Décisions historiques remplacées ou à rapprocher

| ID | Décision historique | Remplacée ou nuancée par | Statut |
|---|---|---|---|
| H01 | N7 (registre) : « Pas de dégâts pour les petites chutes ; seuil exact à décider » | D01 : dégâts dès un étage | **contredit**. Le registre n'est pas modifié par ce lot (mandat distinct requis). |
| H02 | Portée fixe de deux cases (décision antérieure au 9 novembre, non inscrite au registre ; connue seulement par le mandat, §4 A) | P05 et P06 : référence de 2 cases à 1 g et un étage, dépendant ensuite de la gravité et du dénivelé | **contredit** (remplacée) |
| H03 | S5 : déplacement partiel si TU insuffisantes | Z1, déjà supplantée au registre (LOT-2D) | historique |
| H04 | Hypothèse du LOT-2B « toutes les unités sont connues » | S6 à S12, déjà écartée au registre | historique |
| H05 | N6 : dégâts croissants avec la hauteur | Précisée par D03 et D04 (incréments géométriques) | concordant |
| H06 | N8 à N10 : caractéristiques, équipements, armure et poids lors d'une chute | Précisées en partie par K08, D09 et D10 (collisions et obstacles) ; aucune formule pour une chute au sol (E24) | concordant, incomplet |
| H07 | S10 : case occupée infranchissable pour la traversée comme pour la destination | Restreinte à la « marche normale » par M §3.1 ; exceptions J05, J07 (M) et J13 (P), toutes validées | nuancé |

## 3. Spécification mathématique (B)

Les définitions ci-dessous sont **symboliques**. Aucune échelle métrique n'est attribuée aux cases ni aux étages (E1). Les formules marquées « dérivé » découlent algébriquement des règles validées. Celles marquées « proposition technique » sont **non validées**.

### 3.1 Repère et grandeurs

| Symbole | Sens | Statut |
|---|---|---|
| `(x, y, z)` | Position entière d'une case ; `z` = niveau | validé (R : N3) |
| `L`, `H` | Largeur d'une case, hauteur d'un étage | symboles ; valeurs non fixées (E1) |
| `g`, `g0` | Gravité de l'environnement ; `g0` = 1 g | validé (M : P01) ; unité physique dépendante de `L` et `H` (E1) |
| `n = z_dép − z_arr` | Étages descendus (n ≥ 1 pour un saut offensif) | proposition technique ; définition ouverte (E12) |
| `D = n × H` | Dénivelé vertical | proposition technique : on néglige les hauteurs de terrain dans un niveau (E12) |
| `V(t)` | Volume de l'unité à l'instant `t` : translation d'un volume de référence `V0` | validé (M : P07) dans le principe ; forme et dimensions ouvertes (E1) |
| `v_z0`, `v_h` | Vitesse verticale initiale ; vitesse horizontale (vecteur du plan) | `v_z0` constante pour une même unité et une même action, si « impulsion » désigne une vitesse (E11) |
| `TU_max` | TU maximales de l'unité | validé (M) |
| `M` | Poids total utilisé pour les collisions, en kg (référence universelle 80 kg) : poids propre de l'unité + poids de son armure + poids de son équipement et de son inventaire. À ne pas confondre avec la charge portée de la surcharge (N14, armure + inventaire comme dans OXCE). | validé (M, P) ; valeurs du poids propre des unités non fixées ; unité de la charge portée : E20 |

### 3.2 Trajectoire (validé dans le principe, P02 à P04)

Point de référence (proposition technique) : le bas du volume, au centre de l'emprise.
- Hauteur : `z(t) = z_dép·H + v_z0·t − ½·g·t²`.
- Position horizontale : `p(t) = p_dép + v_h·t`, avec `v_h` constant pendant le vol, sans frottement (hypothèse du modèle simplifié).
- Sommet : atteint à `t_s = v_z0 / g`, à une élévation `h_max(g) = v_z0² / (2g)` au-dessus du départ.
- **Calibrage (dérivé de P04)** : `h_max(g0) = H/4` donne `v_z0 = √(g0·H/2)`.
- **Invariant (dérivé de P02 et P04, sous E11)** : `h_max(g) = (g0/g) × H/4`. D'où `H/2` à 0,5 g et `H/8` à 2 g.
- **Durée de vol** jusqu'à un dénivelé `D > 0` : `t_v(g, D) = [v_z0 + √(v_z0² + 2·g·D)] / g` (dérivé).
  - À `g0`, pour `D = H` : `t_v = (1 + √5)·√(H / (2·g0)) ≈ 2,288·√(H/g0)`.
- **Vitesses à l'instant `t`** : `v_z(t) = v_z0 − g·t` ; à l'atterrissage, `v_z = −√(v_z0² + 2·g·D)`. La vitesse horizontale reste `v_h`.
- **Vitesse horizontale requise (dérivé de P03)** : pour une destination à la distance euclidienne `d` (dans le plan), `‖v_h‖ = d / t_v`. Elle doit rester dans les capacités de saut, non définies (E2).

### 3.3 Portée (P05 validée ; conversion ouverte)

- **Validé** : portée de référence `R_ref = 2` cases selon Manhattan, à `g0` et `D = H`.
- **Incohérence à arbitrer (E2)** :
  - une limite physique sur `‖v_h‖` donne une portée **euclidienne**, en cercle ;
  - la limite validée est en **Manhattan**, en losange ;
  - elles ne coïncident que sur les axes. Par exemple, (1, 1) a une distance de Manhattan de 2 mais une distance euclidienne de `√2·L`.
- **Proposition technique A (non validée)** : capacité horizontale `v_h,max` constante, calibrée pour que `R(g0, H) = 2`. On en tire `R(g, D) = 2 × t_v(g, D) / t_v(g0, H)`, en cases, avant toute conversion en nombre entier.

| `g / g0` | `D / H` | `t_v / t_v(g0, H)` | `R` (cases, avant conversion) |
|---|---|---|---|
| 1 | 1 | 1 | 2 |
| 0,5 | 1 | 1,6885 | 3,377 |
| 2 | 1 | 0,6180 | 1,236 |
| 1 | 2 | 1,2361 | 2,472 |
| 1 | 3 | 1,4232 | 2,846 |
| 0,5 | 2 | 2,0000 | 4,000 |

La règle de conversion (troncature, arrondi, limite euclidienne ou de Manhattan) n'est **pas décidée** : les tests exacts sont bloqués (E2, E5).

- **g = 0** : l'unité ne redescend jamais (`z(t)` ne fait que croître). Aucun comportement n'est arbitré (E3).

### 3.4 Collision d'un volume

- **Blocage** (validé, P07) : le trajet est bloqué si `V(t)` coupe un mur, un sol ou un plafond pendant le vol.
  - Formulation proposée (proposition technique, **non validée**) : un instant `t` de `]0, t_v[`, la surface d'atterrissage étant exclue.
  - Une **autre unité** sur le trajet n'est pas tranchée : cas ouvert (I04, E9).
- **Obstacle bas survolé** : à chaque instant où `V(t)` est au-dessus de l'obstacle, le bas de `V(t)` est plus haut que le sommet de l'obstacle.
- **Premier contact** : `t* = min { t : V(t) ∩ S ≠ ∅ }` sur tous les solides `S`.
  - **Avant engagement** (P08, I01) : on ne teste que les solides **connus**. Un contact avec un solide connu interdit l'action.
  - **Pendant l'exécution** : le premier contact avec un solide inconnu interrompt le saut à `t*` et révèle ce solide (P08). Si l'unité est alors sans support, elle chute verticalement (D13).
- **Plafond** (dérivé ; à vérifier une fois l'échelle connue) : une unité de hauteur `h_u` touche le plafond du niveau de départ si `h_u + h_max(g) > H`.
  - À 1 g, la condition sans contact est `h_u ≤ 3H/4` ;
  - à 0,5 g, `h_u ≤ H/2` ;
  - quand `g` tend vers 0, le contact devient inévitable (E1, E3).

### 3.5 Vitesse normale au point de contact (D11)

On note `n̂` la normale unitaire de la surface, orientée vers l'unité.
- **Vitesse normale** : `v_n = −v·n̂` (positive à l'approche).
- **Vitesse tangentielle** : `v_t = v − (v·n̂)·n̂`.

| Surface | `v_n` | Selon la phase |
|---|---|---|
| Sol (`n̂ = +z`) | `−v_z(t*)` | Positive seulement en descente |
| Plafond (`n̂ = −z`) | `v_z(t*)` | Positive seulement en montée ; nulle au sommet |
| Mur vertical (`n̂ = n̂_m`) | `−v_h·n̂_m` | Constante pendant tout le vol |

Les phases montée (`t < t_s`), sommet (`t = t_s`) et descente (`t > t_s`) servent **uniquement au diagnostic** (D11). Leur effet passe par `v_n`, sans coefficient. Un contact au sommet contre un plafond donne `v_n = 0`. Ce que la formule de dégâts d'impact en fera reste ouvert (E8).

### 3.6 Dégâts

**Base `B(n)`** (validé, D03 et D04 ; valeurs non arrondies) : `B(n) = 8 + 6 × Σ(k=0..n−2) 1,35^k`. Forme fermée équivalente (dérivé) : `B(n) = 8 + (6 / 0,35) × (1,35^(n−1) − 1)`.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Incrément depuis n − 1 | — | 6 | 8,1 | 10,935 | 14,76225 | 19,9290375 | 26,904200625 | 36,32067084375 |
| `B(n)` | 8 | 14 | 22,1 | 33,035 | 47,79725 | 67,7262875 | 94,630488125 | 130,95115896875 |

**Plafonds** (validé, D05) :

| Cas | Plafond | Premier `n` plafonné |
|---|---|---|
| Chute au sol | 70 | 7 |
| Unité qui tombe dans une collision | 60 | 6 |
| Unité percutée | 80 | 7 |
| Impact contre un obstacle | 70 | Base non définie (E8) |

La base de dégâts d'une collision entre unités n'est pas écrite : `B(n)` est une hypothèse (E8).

**Chaîne de calcul, d'après le §3.5 du mandat :**

| Étape | Contenu | Statut |
|---|---|---|
| 1 | Base : `B(n)` (chute au sol) ; collision entre unités : base ouverte ; obstacle : puissance d'impact `P_obs`, fonction de `v_n` et de `f_M = min(M/80, 3)` | validé pour `B(n)` et `f_M` ; reste ouvert (E8) |
| 2 | Plafond selon le cas | validé |
| 3 | `× 1,25` pour la cible d'un saut offensif, y compris un allié ou un neutre caché ; jamais pour l'attaquant | validé |
| 4 | Tirage 50 à 150 % (« type explosion OXCE ») | validé ; nombres entiers ouverts (E5) |
| 5 | Facteurs de poids et protection de l'armure, puis conversion en santé et en étourdissement. Poids : entre deux unités (E6), lors d'une chute au sol (E24) ; contre un obstacle, il est déjà compté dans `f_M` à l'étape 1 et ne doit pas être recompté. | validé dans le principe (après le tirage) ; ordre et formules ouverts (E6, E7, E24) |

**Exemples**, calculés seulement avec des valeurs entières validées :
- chute au sol d'un étage : puissance 8. Avec la règle entière d'OXCE (§4), le tirage serait uniforme sur [4, 12] ;
- unité percutée, 7 étages, **si la base d'une collision est `B(n)`** (hypothèse, E8) : `B(7) ≈ 94,63`, plafonné à 80, puis `× 1,25` = 100 avant le tirage. Avec la règle d'OXCE, le tirage serait sur [50, 150] ;
- à partir de 3 étages, `B(n)` n'est pas entier : la puissance tirée dépend d'un arrondi non décidé (E5).

**Facteur de poids contre un obstacle** (validé, D10). `M` désigne le poids total : poids propre de l'unité + armure + équipement et inventaire (validé, P).

| M (kg) | 40 | 80 | 160 | 240 | 320 |
|---|---|---|---|---|---|
| `f_M` | 0,5 | 1 | 2 | 3 | 3 |

**Coût offensif** (validé, J09) : `C_att = max(1, ⌊0,20 × TU_max⌋)`.
- Pour un `TU_max` entier, c'est égal à `max(1, ⌊TU_max / 5⌋)`. Cette forme entière est une précaution contre d'éventuels arrondis en virgule flottante ; aucun écart n'a été constaté (proposition technique, de calcul seulement).
- Exemples : `TU_max` de 1 à 9 → 1 ; 10 → 2 ; 54 → 10 ; 80 → 16.
- Coût total : `C_dép + C_att`, où le coût de déplacement d'un saut, `C_dép`, n'est pas défini (E13).

**Probabilité d'esquive** (K05, provisoire) : `p = clamp(R + 5·n, 0, 100)` %, où `R` désigne les Réactions.
- Comme `n ≥ 1` pour un saut ou une chute, `p ≥ 5 %` dès que `R ≥ 0`. Le cas « 0 % » n'est atteignable qu'avec des Réactions négatives (E12).
- Dans OXCE, un test de pourcentage réussit quand un entier tiré dans [0, 99] est inférieur à la valeur (`src/Engine/RNG.cpp:177-180`, puis `src/Engine/RNG.h:52-55`, VC). Le tirage de Bastion n'est pas décidé.

## 4. Mécanismes OXCE vérifiés (C)

Lecture du code au commit `441cae1`, sans exécution. Comportement lu dans OXCE, distinct des règles de Bastion.

| Point | Comportement OXCE | Preuve | Statut |
|---|---|---|---|
| Coûts des changements de niveau | Escalier : sol d'arrivée + 1 TU à la montée. Échelle : coût de la pièce, ou 8. Grav-lift : 8 TU, 0 énergie. Chute : 0 TU, 0 énergie. | LOT-2E E5, L4, G3, C5 (non relus pour ce lot) | VC |
| Chutes | Niveau par niveau ; **aucun calcul de dégâts identifié** dans le périmètre examiné | LOT-2E C1 à C10 (non relus pour ce lot) | VC (absence universelle : NV) |
| Unité sous une chute | Chute planifiée : case occupée par une unité connue refusée. Sinon : unité écartée sans TU, ou mise hors de combat (assommée, ou tuée si elle n'est pas capturable). | LOT-2E C7 (non relu pour ce lot) | VC |
| Tirage « explosion » | Le type de dégâts explosifs (HE) est défini avec un tirage « explosion » (`src/Mod/Mod.cpp:520-522`) ; par défaut, le constructeur prévoit un tirage standard (`src/Mod/RuleDamageType.cpp:31`). Écart de 50 % par défaut (`Mod.cpp:254`), aussi fixé à 50 par `xcom1` (`bin/standard/xcom1/difficulty.rul`, `explosiveDamageRange`). Bornes : `⌊P × 50 / 100⌋` et `⌊P × 150 / 100⌋` en arithmétique entière, pour une puissance `P` entière. Tirage entier uniforme, bornes comprises (reste d'une division). | `RuleDamageType.cpp:81-131` (dont `:117-118`, `:126-130`) ; `src/Engine/RNG.cpp:142-145`, puis `:90-93` | VC |
| Ordre des dégâts sur une unité | 1. Tirage aléatoire **avant** l'application (`src/Battlescape/TileEngine.cpp:3233`, puis `hitUnit`, `:3134-3148`).<br>2. Modificateur de résistance de l'armure au type de dégâts, arrondi à l'inférieur (`src/Savegame/BattleUnit.cpp:1640`, `:2976-2979`).<br>3. Côté et partie du corps selon la position relative ; côté « dessous » si l'impact vient d'en dessous (`:1642-1710`).<br>4. Points d'accroche de script (`:1716-1738`).<br>5. Soustraction de l'armure du côté touché, multipliée par l'efficacité d'armure (`:1796-1801`).<br>6. Si le reste est positif : conversion en étourdissement, moral, TU, santé, mana, énergie, blessures, usure de l'armure (`:1803-1828`).<br>7. Application bornée. L'étourdissement est ignoré pour une armure insensible à la douleur ; il est plafonné à un multiple de la santé (`:1839-1860`). | Lignes citées | VC |
| Conversion par défaut d'un type de dégâts | Santé × 1,0 ; étourdissement × 0,25 (tirage entre 0 et le dégât, puis arrondi) ; usure de l'armure × 0,1 ; blessures aléatoires. Arrondi au plus proche. Les valeurs propres à chaque type de dégâts ne sont pas vérifiées. | `src/Mod/RuleDamageType.cpp:26-38`, `:213-227`, `:234-330` | VC (valeurs par défaut) ; NV (par type) |
| Résistance du terrain | **Impact direct** (`hit`) :<br>- avec la méthode 1 (défaut du constructeur, `RuleDamageType.cpp:37`), le dégât au terrain est tiré uniformément entre `⌊P/2⌋` et `⌊3P/2⌋` ;<br>- avec la méthode 2 (celle du type HE, `Mod.cpp:528`), il reprend le tirage fait pour l'unité (`RuleDamageType.cpp:141`) ;<br>- puis × 0,5 et arrondi, avec un plafond optionnel.<br>**Explosion** : aucun tirage pour le terrain (`TileEngine.cpp:3392`).<br>**Destruction** : une partie de case est **détruite si ce dégât atteint son armure**, sans accumulation. Elle est remplacée par sa version détruite, et une partie explosive déclenche une explosion en chaîne. Une partie grav-lift (sol, échelle) n'est **jamais détruite**. Un sol détruit au niveau 0 est remplacé par de la terre brûlée.<br>**Armure 255** : traitée comme indestructible pour le feu et dans `detonate` ; pour un impact direct, ce n'est qu'un seuil élevé. | `TileEngine.cpp:3233-3268`, `:3392`, `:3590-3592` ; `RuleDamageType.cpp:139-142`, `:296-303` ; `src/Savegame/Tile.cpp:535-578` ; `src/Savegame/SavedBattleGame.cpp:2433`, `:2447` | VC (armure 255 pour un impact direct : INF) |
| Esquive | Aucun mécanisme d'esquive pour une unité sous une chute (écartement ou mise hors de combat) | LOT-2E C7 | VC |

**Non vérifié** :
- les dégâts au terrain par explosion (propagation) ;
- les valeurs de conversion de chaque type de dégâts dans les règles `xcom1` ;
- le comportement réel en jeu (aucune exécution).

## 5. Revue de cohérence et points ouverts (E)

Aucune proposition ci-dessous n'est validée. Les lignes marquées « Tranché par le correctif (P) » rapportent des décisions confirmées par la demande de correctif du propriétaire (§1, source P).

| # | Question | Règles | Risque | Choix nécessaires | Proposition facultative | Bloquant |
|---|---|---|---|---|---|---|
| E1 | Taille physique des cases et des étages ; repère, point de référence et dimensions du volume de l'unité | P01 à P08, D10 | Trajectoires et contacts incalculables ; « 9,81 m/s² » sans valeur de `H` | Fixer `L` et `H` (en mètres), ou rester sans dimension (rapports `g/g0`) ; dimensions du volume | Rester sans dimension, volumes en fractions de `L` et de `H` | Oui |
| E2 | Trajectoire continue, vitesse horizontale adaptable et limite de Manhattan | P03, P05, P06 | Incohérence en diagonale (`√2·L` contre 2) ; portée non entière | Choisir la limite qui gouverne et la règle de conversion | Proposition A (§3.3), à arbitrer | Oui |
| E3 | `g = 0` ou gravité hors de la plage prévue (T-X05) | P01, P06 | Aucun atterrissage ; division par zéro | Plage de gravité admise ; comportement hors plage | Interdire le saut hors plage | Oui (pour ces cas) |
| E4 | Phases début, milieu, fin | D11 | Usage abusif comme modificateur | Définition pour l'affichage seulement | Signe de `v_z` | Non |
| E5 | Arrondis : `B(n)`, bonus, entrée entière du tirage, produits de coefficients, valeurs extrêmes | D03 à D10, J09, P06 | Arrondis silencieux ; résultats non reproductibles | Où et comment arrondir | — | Oui (tests exacts de dégâts) |
| E6 | Formule atténuée du rapport de poids entre deux unités (portant sur le poids total `M` de chacune, E23) | K08, D09 | Aucun calcul possible | Formule, bornes, place dans la chaîne | — | Oui |
| E7 | Type de dégâts OXCE ; côté d'armure (par exemple « dessous ») ; conditions d'étourdissement | D07, D09 | Pipeline indéterminé | Type de dégâts, côté, conversion | — | Oui |
| E8 | Conversion d'un choc en puissance : `v_n`, vitesse initiale, dénivelé ; double comptage avec `B(n)` ; base d'une collision entre unités ; contact au sommet (`v_n = 0`) | D03, D05, D10, D11 | Deux bases concurrentes | Formule de `P_obs` ; base des collisions | — | Oui |
| E9 | Collisions multiples ; case devenue occupée ou libre ; grandes unités ; atterrissage sans support (T-X01 à T-X04) | I03, I04, D13, K01 à K08 | Résultats indéfinis | Règles dédiées | — | Oui (pour ces cas) |
| E10 | Portée des validations du 9 novembre par rapport aux autres sous-domaines encore ouverts de `MEC-0001` : portes ; géométrie des murs et des angles ; coûts (terrain, murs, changements de niveau) ; règles précises des escaliers, échelles et ascenseurs ; visibilité détaillée et brouillard ; capital et renouvellement des TU ; coût minimal et départage ; orientation, énergie, interruptions ; taille des unités ; autres propositions du LOT-2B | toutes | Lecture comme une acceptation globale | Confirmer la portée ; inscription au registre par un mandat distinct | — | Non (pour ce document) |
| E11 | « Impulsion verticale constante » : vitesse ou quantité de mouvement ? | P02, P04 | Avec une quantité de mouvement, la hauteur dépendrait du poids porté | Préciser | — | Oui (si le poids varie) |
| E12 | Comptage des étages `n` : « niveaux traversés » ou `|z_dép − z_arr|` ; hauteur du sommet au-dessus du départ ; hauteurs de terrain dans un niveau ; chute depuis un point de contact situé entre deux niveaux, ou de moins d'un étage (`B(n)` n'est défini que pour un `n` entier ≥ 1) ; esquive à 0 % inatteignable | D03, D13, K05 | Comptes incohérents | Définition | — | Oui |
| E13 | Coût en TU du déplacement d'un saut (« en plus du déplacement ») | J09, J10, I02 | Prévisualisation et seuil impossibles | Modèle du coût | — | Oui |
| E14 | **Tranché par le correctif (P).** Exceptions à S10 propres aux sauts : J05 et J07 (unités cachées, M) et J13 (ennemi actuellement visible, P), toutes validées. Les cas dynamiques (case devenue occupée pendant le vol) restent ouverts (E9, T-X01). | J02, J05, J07, J13, M13, H07 | — | — | — | Non (tranché) |
| E15 | S7 (trajet en cases visibles ou explorées) s'applique-t-elle à l'arc d'un saut et aux cases survolées ? | M10, J03, P07 | Ambiguïté | Préciser | — | Non |
| E16 | Quels sont les « trois blocs » validés le 9 novembre ? Le §3 n'a pas été comparé à la conversation | M §3 entier | Traçabilité incomplète | Confirmation du propriétaire avant inscription | — | Non (tests) ; oui avant inscription |
| E17 | Esquive : « TU du déplacement requis » pendant le tour adverse ; pas diagonal ; « case voisine » : 8 voisines, même niveau ? | K03, K06 | Ambiguïté | Préciser | — | Oui |
| E18 | **Tranché par le correctif (P).** Après une esquive réussie, l'attaquant termine sa chute au sol et relève des règles de la chute au sol : plafond de 70 sur les dégâts de base, avant le tirage | K06, D05 | — | — | — | Non (tranché) |
| E19 | Chute volontaire hors attaque (N5) : mécanisme et commande | R : N5 ; J01 | Lacune | Préciser | — | Non |
| E20 | Unité de la **charge portée** de la surcharge (N14) : kg dans Bastion, ou « unités de Force » d'OXCE ? Cette charge est distincte du poids total `M` des collisions (E23, tranché), mais l'armure, l'équipement et l'inventaire entrent dans les deux grandeurs : leur unité doit rester cohérente. | D10, M16 ; R : N14 | Conversion indéfinie | Unité de référence | — | Non (tests de `f_M`) ; oui pour la transposition exacte de la surcharge (T-M11) |
| E21 | N7 contredite au registre | H01 | Registre incohérent jusqu'à sa mise à jour | Mandat d'inscription distinct | — | Non (tests) ; oui avant implémentation |
| E22 | Loi du tirage de la case d'esquive (uniforme ?) | K04 | Tests statistiques impossibles | Préciser | Uniforme | Non |
| E23 | **Tranché par le correctif (P).** Le poids total `M` des collisions comprend le poids propre de l'unité, celui de son armure, et celui de son équipement et de son inventaire. Il ne se confond pas avec la charge portée de la surcharge (N14). Les valeurs du poids propre des unités restent à fixer (données de jeu, pas une règle). | D10, K08, M16 | — | — | — | Non (tranché) |
| E24 | Effet du poids, de l'armure et des caractéristiques sur une **chute au sol** (N8 à N10) : aucune formule ; risque de double comptage avec `f_M` | H06, D09 ; R : N8 à N10 | Dégâts au sol non calculables | Formule et place dans la chaîne | — | Oui (dégâts exacts au sol) |

**Récapitulatif.**
- 3 points ont été tranchés par le correctif du propriétaire : E14, E18 et E23.
- 13 points restent bloquants pour des tests exacts : E1 à E3, E5 à E9, E11 à E13, E17 et E24.
- 3 autres ne bloquent qu'une étape ultérieure : E16 (avant inscription), E20 (transposition exacte de la surcharge, T-M11) et E21 (avant implémentation).

Les tests concernés sont marqués « partiels » ou « bloqués » dans la matrice.

## 6. Vérifications, limites et revue indépendante

**Vérifications** (pour les deux documents et l'archivage du mandat) :

| Commande ou contrôle | Résultat | Code de retour |
|---|---|---|
| `git fetch origin main` | `origin/main` = `4077db2` | 0 |
| `cp` du fichier joint, puis `cmp` et `sha256sum` sur la copie archivée | Copie identique ; SHA-256 `a68395e1…bd3b5`, comme le fichier joint | 0 |
| `git status --short` | Fichiers : `docs/mandates/BASTION-MANDAT-LOT-2F-v1.0.md` (nouveau), `docs/mandates/README.md` (une ligne ajoutée), les deux rapports `LOT-2F` (nouveaux) | 0 |
| `git diff --check` (fichiers suivis) | Aucune sortie | 0 |
| `git diff --no-index --check /dev/null`, sur chaque rapport | Aucune erreur d'espacement | 1 (attendu : fichier différent de `/dev/null`) |
| Recherche d'espaces en fin de ligne dans les rapports et l'index | Aucune ligne | 1 (aucune correspondance) |
| Espaces en fin de ligne dans le mandat archivé | 6 lignes (sauts de ligne Markdown du fichier reçu), conservées pour l'identité octet pour octet | — |
| Renvois `T-…` de la spécification présents dans la matrice | Tous présents | 0 |
| Fichiers protégés non autorisés (registre, `docs/decisions/`, `docs/references/`, `CLAUDE.md`, harnais, code) | Non modifiés | — |

Tests .NET non lancés : non requis pour ce lot documentaire, et aucun code n'est modifié.

**Limites.**
- Les décisions du 9 novembre ne sont connues que par le §3 du mandat, sans comparaison avec la conversation.
- OXCE a été lu, pas exécuté.
- Aucune échelle physique n'est fixée.
- Les formules marquées « proposition technique » ne sont pas validées.
- La source P n'est connue que par le texte de la demande de correctif ; la validation initiale des trois décisions n'est pas vérifiée ; rien n'est inscrit au registre.

**Revue indépendante.**
- **Relecteur** : agent distinct du développeur, en lecture seule (aucune écriture dans le dépôt). Il a relu les quatre fichiers, le mandat, le registre, les études LOT-2A, LOT-2B et LOT-2E, et le code OXCE aux lignes citées.
- **Contrôles** : il a recalculé toutes les valeurs numériques (en fractions exactes) et vérifié l'archivage (`cmp` et SHA-256) ainsi que le périmètre.
- **Résultat** : 20 constats, dont 0 bloquant, 4 importants et 16 mineurs.
- **Tous intégrés**, après vérification par le développeur :
  - **constats importants :**
    - le blocage par une autre unité n'est plus présenté comme validé (I04, E9) ; l'intervalle de temps et l'exclusion de la surface d'atterrissage sont marqués « proposition technique » (§3.4) ;
    - `M` est transcrit mot pour mot (« poids total `M` (équipement inclus) ») ; point ouvert E23 sur la masse corporelle ;
    - les exceptions à S10 sont circonscrites : M13, J05, J07, E14 et nouvelle entrée H07 ;
    - point ouvert E24 sur l'effet du poids, de l'armure et des caractéristiques lors d'une chute au sol ; risque de double comptage avec `f_M` signalé ;
  - **constats mineurs :**
    - statuts de K05, D07 et D09 ajustés ;
    - sens de T-J04 qualifié de dérivé ;
    - hypothèse `B(n)` rappelée dans les exemples et dans T-D03 et T-D05 ;
    - critère de décompte des points bloquants précisé (15) ;
    - T-M06 rattaché à Z1 ;
    - préconditions de T-J02, T-J03 et T-J12 complétées ;
    - T-K04 reformulé et T-K06 ajouté (100 % et 0 %) ;
    - colonnes de T-X01 à T-X05 complétées ;
    - D13 ajoutée à E12 ;
    - précisions OXCE : type HE (`Mod.cpp:520-528`), méthode de dégâts au terrain, explosion sans tirage pour le terrain, armure 255 dans `detonate`, renvois du générateur aléatoire, lignes du LOT-2E non relues ;
    - citation de l'index corrigée ;
    - statuts historiques définis au §1 ;
    - E10 détaillé ;
    - formulation de la forme entière du coût offensif.
- **Limites de la revue** :
  - la conversation du 9 novembre et le message d'autorisation ne sont pas vérifiables par le relecteur ;
  - OXCE a été lu, pas exécuté ;
  - le relecteur est du même type que le développeur ; sa revue ne vaut pas validation.

**Correctif documentaire (demande du propriétaire, après la revue de l'orchestrateur).**
- **Décisions confirmées** par le propriétaire comme déjà validées (source P, demande reçue le 9 novembre 2026), sans date de validation initiale précisée :
  - **E14** : une attaque par saut peut viser un ennemi actuellement visible ; c'est une exception explicite à S10 (J13) ;
  - **E18** : après une esquive réussie, l'attaquant termine sa chute au sol, avec les règles de la chute au sol : plafond de 70 sur les dégâts de base, avant le tirage (K06) ;
  - **E23** : le poids total `M` des collisions comprend le poids propre de l'unité, son armure, son équipement et son inventaire. Il est distinct de la charge portée de la surcharge (N14).
- **Changements** :
  - spécification : en-tête, §0, sources et statuts (§1), M13, J13, K06, D10, H07, définition de `M` (§3.1 et §3.6), introduction du §5, E6, E14, E18, E20, E23, récapitulatif (§5), limites (§6) ;
  - matrice : T-J11, T-K03, T-D09, récapitulatif.
- **Inchangés** : les autres points restent ouverts ; E6 et E20 sont seulement reformulés pour renvoyer à E23, sans être tranchés. Le registre, le mandat archivé, son index et le compte rendu de la première revue ne sont pas modifiés.
- **Contrôles du correctif** (exécutés avant le commit) :
  - `git diff --stat` : seuls les deux rapports sont modifiés (code 0) ; `git status --porcelain` ne liste aucun fichier non suivi ;
  - `git diff --check` : aucune sortie, code 0 ; recherche d'espaces en fin de ligne (`grep -nE ' +$'`) : aucune ligne, code 1 ;
  - `git diff --quiet HEAD -- docs/gameplay docs/decisions docs/references docs/mandates .claude scripts .github CLAUDE.md src tests` : code 0 (aucun changement) ;
  - `sha256sum` du mandat archivé : `a68395e12475b364bb442c0ee66199404a86f743b9cca45fbcb9bd7f309bd3b5`, inchangé ;
  - renvois : chaque `T-…` de la spécification existe dans la matrice, chaque `E…` de la matrice existe dans la spécification ;
  - décomptes : 60 tests (24 spécifiables, 26 partiels, 10 bloqués) ; 13 points bloquants ; tableaux au nombre de colonnes cohérent ;
  - `bash scripts/harness/test-hooks.sh` : 75 tests, 0 échec, code 0 ;
  - `bash scripts/harness/check-simulation-trace.sh origin/main` avec la description de la PR : « Aucun fichier de src/Bastion.Simulation/ modifié », code 0 ;
  - `dotnet` n'est pas installé dans l'environnement : build, format et tests .NET sont laissés à la CI.
- **Revue indépendante du correctif** (agent distinct, lecture seule) : 12 constats, 0 bloquant, 2 importants, 10 mineurs. Tous sont intégrés :
  - E20 garde D10 dans ses règles, note la cohérence d'unité entre `M` et la charge portée, et revient au récapitulatif comme point bloquant une étape ultérieure (T-M11) ;
  - la source P est datée (demande reçue le 9 novembre 2026), l'en-tête reprend « présentées par le propriétaire comme déjà validées », et une limite est ajoutée ;
  - mineurs : « actuellement » dans l'en-tête ; statut de K06 ; T-J11 dans M13 ; cas dynamiques (E9, T-X01) dans M13 et E14 ; T-K03 et T-J11 complétés ; formulations du §0 et du §5 ; mention « Inchangés » précisée ; ajout au compte rendu de la première revue retiré ; contrôles consignés ici ; description de la PR mise à jour.
- **Limites du correctif** : la demande et les validations initiales ne sont pas vérifiables par le relecteur ; la revue ne vaut pas validation par le propriétaire.
