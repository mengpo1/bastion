# LOT-2G — Dossier d'arbitrage des 13 points bloquants de `MEC-0001`

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2G-v1.0.md`, publié sur la branche `orchestration/mandats` (commit `2ff8e1df53401ea8c5daa4ccb0e173a7a63f9dbd`). Archivé octet pour octet dans `docs/mandates/`, SHA-256 `735ca10d5c03f1f2939e8794fcb791f9b12ba46de9b61dadc0e22af824511b59`. |
| Autorisation | Propriétaire, 10 novembre 2026 : « Je t'autorise à exécuter le mandat LOT-2G v1.0 de Bastion. […] Utilise `main` comme base de travail […]. Aucune publication de tes résultats ni fusion sans autorisation distincte. » |
| Branche | `docs/lot-2g-mec-0001-arbitrages`, créée depuis `origin/main` = `72908389ea99f7267f7f723c57b488f640bfe441` (fusion de la PR n° 9), après `git fetch origin main`. |
| Référence OXCE | `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` (8.7.1). Lecture du code seulement, **aucune exécution**. |
| Nature | Dossier de propositions. **Aucune décision n'est prise ni présumée** : les 13 points restent ouverts jusqu'à une validation explicite du propriétaire. Le registre n'est pas modifié ; `MEC-0001` reste « reportée ». Aucun gameplay, aucun code, aucun test exécutable. |
| Compagnon | `docs/reviews/LOT-2G-IMPACTS-TESTS.md` : effet de chaque proposition sur les tests du LOT-2F. |
| Publication | Autorisée par le propriétaire le 13 novembre 2026 (« Tu peux publier ») : branche poussée et PR en brouillon vers `main`, **sans fusion**. |

## 0. Synthèse pour le propriétaire

Ce dossier prépare vos choix sur les **13 points** qui bloquent encore des tests exacts : E1, E2, E3, E5, E6, E7, E8, E9, E11, E12, E13, E17 et E24. Chaque recommandation est une **PROPOSITION NON VALIDÉE**. Les règles déjà acquises (registre, mandat LOT-2F, correctif E14, E18, E23) ne sont pas rediscutées.

### 0.1 Cinq décisions structurantes

Elles regroupent les points liés, pour éviter 13 questions isolées.

| # | Décision | Recommandation (non validée) | Alternative principale | Points |
|---|---|---|---|---|
| DS1 | **Géométrie** : faut-il une échelle en mètres ? Comment traiter le volume de l'unité et le sol qu'elle quitte ? | Règles **sans unité de longueur** : seuls comptent les rapports entre largeur de case, hauteur d'étage et taille des unités. Volume en **pavé** (boîte). Le sol de la case de départ ne bloque pas le saut qui la quitte. | Départ de l'arc au bord de la case ; ou grille de voxels | E1 |
| DS2 | **Saut** : hauteur, portée et gravité | Même vitesse verticale de départ pour toutes les unités, quelle que soit leur charge. Case atteignable si `\|Δx\| + \|Δy\| ≤ R(g, D)`, où `R` est la portée tirée de la durée du vol (2 à 1 g pour un étage) : un nombre réel, **sans arrondi**. Saut offensif disponible seulement dans une plage de gravité, jamais en apesanteur. | Portées entières fixées dans une table ; saut plus court pour une unité lourde | E2, E3, E11 |
| DS3 | **Comptage et nombres** | Une chute compte les **sols franchis vers le bas** ; moins d'un étage ne blesse pas. Calcul exact, puis un arrondi au plus proche juste avant le tirage aléatoire, un autre après le facteur de poids, puis ceux de l'enchaînement des dégâts (E7). | Tout étage entamé compte ; arrondi à l'inférieur | E12, E5 |
| DS4 | **Chocs** | Sol et collisions entre unités : dégâts de base `B(n)`. Mur ou plafond : choc selon le carré de la vitesse, calé sur 8 points pour l'atterrissage d'un saut d'un étage. Le poids compte **une seule fois** par choc, par un facteur **atténué**. Un type de dégâts « impact » propre à Bastion, traité comme dans OXCE (armure, puis santé et étourdissement). Tout atterrissage au sol compte comme une chute au sol. | Facteur de poids `min(M/80, 3)` aussi au sol ; hauteur équivalente | E5 à E8, E24 |
| DS5 | **Déroulement d'une action** | Pendant un saut, rien d'autre ne bouge que l'esquive et les chutes provoquées. Le vol s'arrête au premier choc. Le coût est payé en entier à l'engagement : `c_s` TU par case de portée, plus le supplément offensif. L'esquive utilise les TU restantes de la cible, vers une case voisine au même niveau. | Monde dynamique ; coût de déplacement nul | E9, E13, E17 |

### 0.2 Décisions dépendantes

Une fois les cinq choix faits, il restera des **valeurs de conception** à fixer. Aucune n'est retenue ici, et les valeurs « illustratives » de ce dossier ne sont que des exemples.

| Valeur | Sens | Point |
|---|---|---|
| `λ = L/H` | Largeur d'une case rapportée à la hauteur d'un étage | E1 |
| `w`, `h_u` | Largeur et hauteur du volume d'une unité (par type d'unité : donnée) | E1 |
| `γ_min`, `γ_max` | Plage de gravité où le saut offensif existe | E3 |
| `β`, `β_s` | Force du facteur de poids entre deux unités, puis au sol ; avec la formule proposée, la garantie de K08 demande `β < 2/7` (§4.2) | E6, E24 |
| Valeurs du type « impact » | Résistances, taux de conversion en santé et en étourdissement, facteur vers le terrain | E7, E8 |
| Tirage pour le terrain | Tirage propre ou reprise du tirage fait pour l'unité, comme les deux méthodes d'OXCE (§4.4) | E8 |
| `c_s` | TU par case de portée d'un saut | E13 |

### 0.3 Dérivable ou à choisir

- **Dérivable des règles acquises**, démontré sous les hypothèses indiquées :
  - les règles validées ne contiennent aucune longueur ni durée absolue : un modèle sans unité de longueur suffit (E1) ;
  - au sommet d'un saut, un choc contre un plafond a une vitesse normale nulle (E8, déjà au LOT-2F) ;
  - pour `n ≥ 1`, avec des Réactions positives ou nulles, la probabilité d'esquive vaut au moins 5 % (E12, déjà au LOT-2F).
- **Démontré sous une hypothèse non décidée** : si un saut part du centre de la case et que P07 s'applique à la lettre, un saut court bute contre le sol de départ dès que l'unité est un peu large (E1, D-E1b).
- **Interprétation à confirmer** : si K08 se lit « chacun des deux ordres de blessures reste possible », un tirage commun unique, multiplié par des facteurs fixes, est exclu. Des tirages indépendants suffisent ; d'autres solutions existent (E6, D-E6a).
- **Conséquences des recommandations**, si elles sont retenues :
  - avec E2 et E11, la portée dépend de `g` et de `D` comme l'exige P06, et vaut exactement 2 à 1 g pour un étage (P05) ;
  - avec E2 et E11, au-delà d'environ 2,76 g, aucune case n'est atteignable d'un étage plus haut (E3) ;
  - avec E9, une destination ne peut pas devenir occupée pendant le vol (T-X01).
- **Choix de conception** : tout le reste, en particulier le traitement du sol de départ, la plage de gravité, les formules de poids, le coût de déplacement d'un saut, le cas `n = 0` et la place finale de l'attaquant après une collision.

### 0.4 Constats à connaître avant de choisir

1. **Conflit démontré (E1)** : si un saut part du centre de la case (hypothèse non décidée) et si tout sol qui coupe le volume bloque le saut, comme l'écrit P07 à la lettre, alors **un saut court peut buter contre le bord du sol de départ**. À 1 g, pour une case d'écart et un étage de descente, cela arrive dès que l'unité est plus large qu'environ 24 % d'une case. À 2 g, cela arrive pour toute largeur. Les tests T-J02, T-J03 (case `(1, 1)`) et T-J11 du LOT-2F, classés « spécifiables », en dépendent (§3.1).
2. **Lacune relevée (E9)** : aucune règle ne dit où finit l'attaquant quand la cible n'esquive pas et reste debout. La case reste occupée (S10, K07).
3. **Tension créée par une proposition (E6, E24)** : dans une collision, un attaquant lourd serait **moins** blessé selon la formule proposée en E6 (PNV), alors que N9 et N10 disent que le poids **aggrave** une chute. Une variante compatible avec N9 et N10 existe (§4.2, alternative D ; §6.3).
4. **Conséquence (E8)** : une chute au sol ne dépend pas de la gravité (D03 : base fixée par le nombre d'étages), mais un choc contre un obstacle en dépend, par la vitesse réelle (D10). Ce n'est pas une contradiction, mais un effet à connaître.
5. **Conséquence (E2)** : avec la recommandation, à 1 g et deux étages de descente, la portée vaut 2,47. Une case à 3 de distance reste donc hors de portée, comme à un étage.
6. **Conséquence visible par le joueur (E8)** : si tout atterrissage au sol est une chute au sol, comme la recommandation E8 (a) le propose et comme E18 le prévoit après une esquive, **chaque saut offensif blesse le sauteur** : au moins 8 points de base pour un étage, tirés entre 4 et 12, avant poids et armure. L'autre choix est qu'un atterrissage prévu sur une case vide ne blesse pas (règle nouvelle).
7. **Cas `n = 0` (E12)** : une chute de moins d'un étage sur une unité, par exemple après un choc à mi-étage, n'a pas de base de dégâts (`B(0)` n'est pas défini), et l'esquive y vaudrait `clamp(Réactions, 0, 100)`. Ce cas est à trancher (§3.5).

### 0.5 Ordre d'arbitrage proposé

DS1, puis DS2, DS3, DS4 et DS5 ; enfin les valeurs du §0.2. Les questions à trancher sont regroupées au §7. Aucun lot supplémentaire n'est proposé. Une inscription au registre exigerait de toute façon un mandat distinct (mandat LOT-2G §8).

## 1. Sources, conventions et statuts

**Sources.**
- **R** : registre `docs/gameplay/GAMEPLAY-DECISIONS.md` (S1 à S12, Z1, N1 à N14).
- **M** : décisions du 9 novembre transcrites au LOT-2F (mandat LOT-2F §3), identifiants inchangés : M01 à M16, J01 à J13, P01 à P08, K01 à K08, D01 à D13, I01 à I04, H01 à H07 (`docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` §2).
- **P** : correctif du propriétaire (E14, E18, E23), confirmé par le mandat LOT-2G §2.
- **F** : spécification et matrice du LOT-2F. **E** : rapport LOT-2E.
- **C** : lecture du code OXCE au commit figé, pour ce lot ou les précédents (§6.5).

**Statut d'un élément de ce dossier.**
- **acquis** : règle validée (R, M ou P), reprise sans changement.
- **dérivé** : conséquence démontrée d'une règle acquise, sous des hypothèses écrites. Elle ne vaut décision que si le propriétaire l'accepte.
- **PROPOSITION NON VALIDÉE** (PNV) : solution suggérée par Claude Code.
- **illustratif** : valeur d'exemple, jamais retenue.
- Pour OXCE : **VC** (lecture du code), **INF** (inférence), **NV** (non vérifié). Aucune observation en exécution.

**Notations (sans dimension).** Longueurs en hauteurs d'étage (`H = 1`) ; temps en unités de `√(H/g0)` ; gravité `γ = g/g0` ; dénivelé `δ = D/H` ; largeur d'une case `λ = L/H`. Le volume d'une unité a une largeur `w` et une hauteur `h_u`. La vitesse verticale de départ `v_z0` vaut `1/√2` (P04, si E11 est lu comme une vitesse). La constante `φ' = 1 + √5 ≈ 3,2361` (le double du nombre d'or) apparaît dans les durées de vol.

**Rubriques de chaque point (§3 à §5).** Un tableau homogène de neuf rubriques :
1. énoncé et règles concernées ;
2. décidé et non décidé ;
3. recommandation ;
4. alternative ;
5. équations et exemples ;
6. compatibilité avec les règles acquises ;
7. risques, cas limites et dépendances ;
8. critère de test et tests du LOT-2F ;
9. question au propriétaire.

## 2. Vue d'ensemble

### 2.1 Les 13 points

| ID | Paquet | Question courte | Recommandation (PNV) | Nature | Dépend de | Tests LOT-2F |
|---|---|---|---|---|---|---|
| E1 | 1 | Repère, dimensions, volume, premier contact | Sans dimension ; pavé ; sol de départ exclu | choix (conflit démontré sous une hypothèse) | — | T-J02, T-J03, T-J05 à T-J11 |
| E2 | 1 | Portée en Manhattan et trajectoire continue | `\|Δx\| + \|Δy\| ≤ R(γ, δ)`, sans arrondi | choix ; formule qui en découle | E11 | T-J03, T-J04 |
| E3 | 1 | Gravité nulle ou extrême | Plage `[γ_min, γ_max]` ; action indisponible hors plage | choix | E1, E2 | T-X05, T-J09 |
| E11 | 1 | Impulsion : vitesse ou quantité de mouvement | Vitesse identique pour tous | choix (lecture la plus directe) | — | T-J04, T-J05 |
| E12 | 1 | Nombre d'étages `n` ; bornes de l'esquive | Sols franchis vers le bas ; `n = 0` sans dégâts au sol | choix ; cas `n = 0` à trancher | E1, E11 | T-K02, T-K03, T-K06, T-D12 |
| E5 | 2 | Arrondis et ordre des étapes | Calcul exact ; arrondi au plus proche avant le tirage, puis après le poids | choix | E8 | T-D01 à T-D05 |
| E6 | 2 | Rapport de poids entre deux unités | Tirages indépendants ; facteur borné `1 ± β` | choix ; contrainte calculée pour la formule proposée | E5, E8 | T-D14, T-K04 |
| E7 | 2 | Type de dégâts, armure, étourdissement | Type « impact » de Bastion, enchaînement d'OXCE | choix | E5 | T-D13, T-D01 |
| E8 | 2 | Vitesse au contact et puissance | Obstacle : `8 × (v_n/v_ref)² × f_M`, plafond 70 ; collisions : `B(n)` | choix | E1, E11, E12 | T-D03, T-D05, T-D09, T-D10, T-D12, T-J10 |
| E24 | 2 | Poids, armure, caractéristiques au sol | Facteur atténué `1 ± β_s` après le tirage ; armure du dessous | choix | E5, E7, E8 | T-D01, T-K03 |
| E9 | 3 | Ordre des événements et cas limites | Monde figé ; arrêt au premier contact ; file chronologique | choix ; un cas rendu impossible par la recommandation | E1, E8, E12, E17 | T-X01 à T-X04, T-D12 |
| E13 | 3 | Coût en TU du déplacement d'un saut | `c_s × (\|Δx\| + \|Δy\|)`, payé à l'engagement | choix | E2 | T-J07, T-J15, T-J18, T-J19 |
| E17 | 3 | Esquive : TU, cases, visibilité | TU restantes ; 8 voisines au même niveau, payables et connues | choix | E12 | T-K01, T-K03 |

**Complétude** : exactement 13 points, ceux du mandat LOT-2G §3, sans doublon ni oubli (contrôle au §8).

### 2.2 Points du LOT-2F hors de ce lot

E4, E10, E15, E16, E19, E20, E21 et E22 restent ouverts, avec leur statut du LOT-2F. Ils **ne font pas partie** des 13 blocages. Leurs liens directs avec les propositions sont relevés au §6.4.

## 3. Paquet 1 — Géométrie et physique (E1, E2, E3, E11, E12)

Hypothèses communes à ce paquet, sauf mention contraire :
- trajectoire balistique sans frottement, à gravité constante pendant le vol (LOT-2F §3.2) ;
- vitesse verticale de départ constante (recommandation de E11) ;
- vitesse horizontale constante pendant le vol, dirigée vers le centre de la case visée.

### 3.1 E1 — Repère, dimensions, volume et premier contact

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Fixer ce dont les trajectoires et les contacts ont besoin : taille des cases (`L`) et des étages (`H`), repère, forme et dimensions du volume de l'unité, surfaces des solides, définition et position du premier contact. Règles : P01, P04, P07, P08, M05 (N1), M06 (N3) ; LOT-2F §3.1 et §3.4. |
| 2. Décidé / non décidé | **Acquis** : collision du **volume** entier, pas d'un point (P07) ; obstacle connu = action interdite, obstacle inconnu = interruption et révélation (P08) ; cases et murs (N1) ; positions `(x, y, z)` (N3) ; gravité de référence 1 g (P01) ; pas d'échelle métrique sans arbitrage (mandat).<br>**Non décidé** : échelle ; rapport `L/H` ; forme et taille du volume ; point de départ de l'arc ; épaisseur des sols et des murs ; contact tangent ; contacts simultanés ; case de rattachement après un arrêt. |
| 3. Recommandation (PNV) | a) **Sans dimension** : longueurs en hauteurs d'étage, temps en `√(H/g0)`. « 9,81 m/s² » reste le nom de 1 g.<br>b) **Paramètre** `λ = L/H`, valeur à choisir.<br>c) **Solides** : la case `(x, y, z)` occupe `[xλ, (x+1)λ] × [yλ, (y+1)λ] × [z, z+1]`. Son sol est un rectangle horizontal sans épaisseur à la hauteur `z`. Un mur est un rectangle vertical sans épaisseur sur un bord de case. Un objet est un pavé, dont les dimensions sont des données de terrain.<br>d) **Volume de l'unité** : pavé aligné sur les axes, de base carrée de côté `w ≤ λ` et de hauteur `h_u < 1`. Point de référence : centre de la face inférieure. Au départ, l'unité est centrée sur sa case.<br>e) **Contact** : l'intérieur du volume coupe l'intérieur d'un objet, ou l'intérieur relatif d'une surface (sol, mur) ; un simple contact tangent n'est pas un choc. Le premier contact `t*` se calcule exactement, axe par axe, par l'intervalle de temps où les projections se chevauchent ; aucun échantillonnage.<br>f) **Sol de départ** : il n'est pas testé contre l'unité qui quitte la case. C'est une exception à la lettre de P07, à trancher (démonstration D-E1b).<br>g) **Contacts simultanés** : un seul événement de choc, sans cumul. Si une surface tournée vers le haut en fait partie, c'est une chute au sol (E8 a) ; sinon un choc contre un obstacle, avec la plus grande vitesse normale.<br>h) **Rattachement** : la chute verticale part de la position du contact, sans recentrage (D13). Le support cherché est le sol de la case qui contient le point de référence, sol de départ compris : l'exception (f) ne vaut que pendant le vol. L'unité est recentrée dans cette case à l'atterrissage.<br>i) **Cible** : son volume est un solide comme un autre pour le calcul du premier contact ; ce contact déclenche la collision prévue (E8 c, E9 d). |
| 4. Alternative | **A1 — départ au bord** : l'arc part avec le bord avant du volume au bord de la case et arrive au centre de la case visée. La contrainte du sol de départ reste, mais plus faible (`w ≤ 0,447 λ` à 1 g, une case, un étage ; sans effet pour deux cases, `w ≤ 1,342 λ`). Il faut alors définir le pas d'approche et son coût (E13).<br>**A2 — grille de voxels**, comme la représentation d'OXCE (case de 16 × 16 × 24 voxels, `src/Battlescape/Position.h:34-35`, VC), avec un échantillonnage dans le temps. C'est proche de la référence, mais le résultat dépend du pas d'échantillonnage, et c'est plus lourd à tester. Mentionnée pour comparaison, sans reprise (D4).<br>**A3 — échelle en mètres** : utile seulement pour l'affichage ou l'animation ; aucune règle validée ne l'exige.<br>**A4 — appliquer P07 à la lettre** : accepter que des sauts courts soient impossibles pour des unités larges. |
| 5. Équations et exemples | **D-E1a (dérivé)** : avec `x̃ = x/H` et `t̃ = t·√(g0/H)`, la hauteur s'écrit `z̃(t̃) = z̃_0 + ṽ_z0·t̃ − ½·γ·t̃²`, avec `ṽ_z0 = 1/√2` (P04, lu comme une vitesse : E11). Les contacts, portées et sommets ne dépendent donc que de `γ`, `δ`, `λ`, `w` et `h_u`. Aucune règle validée ne contient de longueur ou de durée absolue ; « 80 kg » (D10) est une masse.<br>**D-E1b** : voir sous le tableau. |
| 6. Compatibilité | P04, P05, P06 et P08 sont inchangées. P07 est respectée, sauf le sol de départ (f), qui est une exception soumise au propriétaire. Le modèle sans dimension ne contredit pas « 1 g ≈ 9,81 m/s² », qui n'est qu'une étiquette. |
| 7. Risques et dépendances | Égalités en virgule flottante aux contacts tangents (prévoir une tolérance fixe ou un calcul exact). Murs sans épaisseur : pas de traversée avec la méthode exacte. Valeurs de `w` et `h_u` par type d'unité : données. `λ` influe sur la force des chocs contre un mur (E8). Plafond à faible gravité : E3. Volume des autres unités : E9. Arc au-dessus de cases non explorées : E15 (hors des 13).<br>**Contact latéral avec la cible** (calculé) : à 1 g, une case, un étage, avec `λ = 1`, `w = 0,3` et `h_u = 0,9`, les emprises se recouvrent à 70 % du vol, quand le bas de l'attaquant est à 0,85 au-dessus du sol d'arrivée. Le premier contact touche donc le côté de la cible. Avec `h_u = 0,6`, il vient du dessus. D'où la règle (i). |
| 8. Critère de test | Pour `λ`, `w`, `h_u` et une géométrie déclarés, l'instant, la surface et la normale du premier contact sont uniques et calculables. Tests : T-J05 à T-J10 ; **T-J02, T-J03 `(1, 1)` et T-J11 dépendent du choix (f)** (voir `LOT-2G-IMPACTS-TESTS.md`). |
| 9. Question | « Les règles peuvent-elles se passer de mètres, en ne gardant que les proportions entre une case, un étage et une unité ? Le sol que l'unité quitte peut-il bloquer un saut court, ou faut-il l'ignorer ? » |

**D-E1b — Conflit entre le volume, le sol de départ et les sauts courts (démonstration).**

Hypothèses :
- départ au centre de la case ;
- trajet en ligne droite le long d'un axe, sur `k` cases ;
- la case voisine du départ, au niveau de départ, n'a pas de sol (c'est le trou par lequel l'unité descend) ;
- sols sans épaisseur ; volume de base carrée de côté `w`.

Raisonnement :
1. Le bas du volume repasse sous le niveau du sol de départ à l'instant `t_r = 2·v_z0/g`, après le sommet.
2. La part du vol déjà faite vaut alors `ρ = t_r / t_v = 2 / (1 + √(1 + 4γδ))`. L'unité a parcouru `ρ·k·λ` horizontalement.
3. Pour ne pas couper le sol de départ, le bord arrière du volume doit avoir quitté la case : `ρ·k·λ ≥ (λ + w)/2`.
4. D'où la condition `w ≤ (2ρk − 1)·λ`.

| `γ` | `δ` | `ρ` (calculé) | `w` maximal, `k = 1` | `w` maximal, `k = 2` |
|---|---|---|---|---|
| 1 | 1 | 0,6180 | 0,236 λ | 1,472 λ (sans effet) |
| 0,5 | 1 | 0,7321 | 0,464 λ | sans effet |
| 2 | 1 | 0,5 | 0 : **aucune largeur** | 1,000 λ (hors de portée : `R = 1,236`) |
| 1 | 2 | 0,5 | 0 : **aucune largeur** | 1,000 λ |

En diagonale `(1, 1)`, le volume quitte l'emprise de la case dès qu'un des deux axes se sépare. Chaque axe avance de `λ`, d'où la même limite qu'avec `k = 1`. Même si le sol de départ est ignoré (recommandation f), cette limite reste vraie lorsque les deux cases orthogonales voisines ont un sol au niveau de départ : c'est alors l'application normale de P07. Conclusion : si l'on applique P07 à la lettre en partant du centre, un saut d'une case est impossible pour une unité plus large qu'environ un quart de case à 1 g, et pour toute unité à 2 g ou pour deux étages de descente. Les règles acquises ne disent pas lequel de ces éléments doit céder. Les solutions sont la recommandation (f), l'alternative A1 ou l'alternative A4 ; **aucune n'est adoptée**.

### 3.2 E2 — Portée en Manhattan et trajectoire continue

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Rendre compatibles la trajectoire physique continue (P02 à P04), la vitesse horizontale ajustable (P03) et la portée en distance de Manhattan (P05, P06) ; dire quelles cases sont atteignables selon `γ` et `δ`. |
| 2. Décidé / non décidé | **Acquis** : portée de référence de 2 cases en Manhattan, à 1 g et pour un étage de descente (P05) ; portée dépendante de la gravité et du dénivelé réel (P06) ; vitesse horizontale adaptée à la destination, dans les limites des capacités (P03) ; portée fixe de deux cases remplacée (H02) ; pas de portée euclidienne non décidée (mandat).<br>**Non décidé** : forme de la « capacité » ; règle de conversion ; cas des diagonales. |
| 3. Recommandation (PNV) | a) La capacité horizontale est bornée **en norme de Manhattan** : `\|v_x\| + \|v_y\| ≤ v_M`, avec `v_M` calé par P05.<br>b) Conséquence (dérivée de a) : une case est atteignable si et seulement si `\|Δx\| + \|Δy\| ≤ R(γ, δ)`, avec `R = 2 × t_v(γ, δ) / t_v(1, 1)`. On compare un entier à un réel : **aucun arrondi ni conversion**. C'est la proposition A du LOT-2F (§3.3), lue comme une borne de Manhattan sur la vitesse.<br>c) Le mouvement réel suit la ligne droite vers le centre de la case visée, à la vitesse `d / t_v`, où `d` est la distance euclidienne. La borne porte sur la norme de Manhattan, jamais sur la norme euclidienne.<br>d) Une tolérance numérique fixe traite les égalités exactes, par exemple `R(0,5 ; 2) = 4`. |
| 4. Alternative | **B — table de portées entières** fixée par le propriétaire, par tranche de gravité et nombre d'étages. Simple, sans calcul, facile à tester, mais arbitraire entre les tranches.<br>**Écartées** : portée fixe de 2 quelles que soient la gravité et la hauteur (contredit P06) ; borne euclidienne sur la vitesse (exclue par le mandat, non décidée). |
| 5. Équations et exemples | `t_v(γ, δ) = (ṽ_z0/γ) × [1 + √(1 + 4γδ)]` (LOT-2F §3.2, sans dimension), d'où `R(γ, δ) = 2 × [1 + √(1 + 4γδ)] / (γ × φ')`. Valeurs (calculées) :<br>- `γ = 1`, `δ = 1` : `R = 2` ; distance maximale 2 ;<br>- `γ = 0,5`, `δ = 1` : 3,377 ; distance maximale 3 ;<br>- `γ = 2`, `δ = 1` : 1,236 ; distance maximale 1 ;<br>- `γ = 1`, `δ = 2` : 2,472 ; distance maximale 2 ;<br>- `γ = 1`, `δ = 4` : 3,166 ; distance maximale 3 ;<br>- `γ = 0,5`, `δ = 2` : 4 exactement ; distance maximale 4 ;<br>- `γ = 3`, `δ = 1` : 0,949 ; aucune case. |
| 6. Compatibilité | P05 exacte (`R(1, 1) = 2`) ; P06 respectée ; distance de Manhattan conservée ; aucune limite euclidienne. La diagonale `(1, 1)` reste à distance 2, comme le veut P05. |
| 7. Risques et dépendances | `R` croît sans limite quand la gravité baisse (E3). La formule suppose une vitesse verticale constante (E11). Une distance permise peut rester bloquée par le volume ou un obstacle (E1, P07). À 1 g, la distance entière n'augmente qu'à partir de quatre étages de descente. |
| 8. Critère de test | Pour `(γ, δ)` déclarés, l'ensemble des cases permises est exactement `{\|Δx\| + \|Δy\| ≤ R}`. Tests : T-J03 (inchangé), **T-J04** : (a) permis, sans plafond ou si `h_u ≤ 0,5` ; (b) refusé ; (c) refusé (`R = 2,472`). |
| 9. Question | « La portée doit-elle rester comptée en cases (`\|Δx\| + \|Δy\|` : une diagonale compte deux cases) et grandir avec la durée du vol, sans arrondi ? » |

### 3.3 E3 — Gravité nulle ou extrême

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Comportement d'un saut à `g = 0` et aux gravités extrêmes ; plage admise ; issue d'un saut dont le vol ne se terminerait pas. |
| 2. Décidé / non décidé | **Acquis** : gravité configurable, 1 g au départ (P01) ; élévation plus haute à gravité plus faible (P04) ; aucune règle de gravité nulle (mandat).<br>**Non décidé** : plage admise ; comportement hors plage ; chutes en apesanteur. |
| 3. Recommandation (PNV) | a) Le saut offensif n'est proposé que si `γ_min ≤ γ ≤ γ_max`, deux valeurs à choisir. Hors de cette plage, l'action est indisponible et ne coûte rien.<br>b) `γ = 0` est toujours hors de la plage : aucun atterrissage n'est possible.<br>c) Pour `γ > 0`, tout vol se termine. L'arc rejoint la destination ; s'il n'y trouve pas de support, l'unité chute verticalement jusqu'au premier support (E9). Le niveau 0 est toujours un support, comme dans OXCE où une chute s'arrête au plus tard au niveau 0 (LOT-2E C4, VC).<br>d) Borne haute naturelle, conséquence des recommandations de E2 et E11 : si `R < 1`, aucune case n'est atteignable. |
| 4. Alternative | **A — aucune plage**, seulement `γ > 0` : le plus simple, mais la portée vaut 13 cases à 0,1 g et environ 124 à 0,01 g.<br>**B — plafond de portée** `R_max` et d'élévation, au lieu d'une plage de gravité.<br>**C — renvoyer** l'apesanteur et la très faible gravité à un mandat dédié aux environnements spéciaux (ce serait un lot supplémentaire, signalé au §6.6). |
| 5. Équations et exemples | Valeurs calculées :<br>- élévation `h_max = 1/(4γ)` étage : 1 étage à 0,25 g, 0,5 à 0,5 g, 0,125 à 2 g ;<br>- sous un plafond, le volume ne le touche pas si `h_u ≤ 1 − 1/(4γ)` : 0,75 à 1 g, 0,5 à 0,5 g ; à 0,25 g ou moins, tout saut sous un plafond le touche ;<br>- `R < 1` dès `γ > 2,764` pour un étage de descente, `γ > 4,292` pour deux, `γ > 5,820` pour trois ;<br>- `R(0,25 ; 1) = 5,97` et `R(0,1 ; 1) = 13,49`. |
| 6. Compatibilité | P01, P04 et P06 sont inchangées. Interdire l'action hors plage est en soi une décision, soumise au propriétaire. |
| 7. Risques et dépendances | Les chutes en apesanteur (une unité sans support tombe-t-elle ?) relèvent des chutes involontaires (N5) et du registre, hors des 13. La gravité est supposée constante pendant une mission. À faible gravité, les sauts sous un plafond deviennent impossibles (E1). |
| 8. Critère de test | Hors plage, la sélection est refusée, sans dépense. Tests : T-X05 ; T-J09, pour le plafond à faible gravité. |
| 9. Question | « Le saut offensif doit-il exister seulement dans une plage de gravité (bornes à fixer ensuite), et être simplement indisponible en dehors, et toujours en apesanteur ? » |

### 3.4 E11 — Sens de l'« impulsion verticale constante »

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | L'impulsion verticale initiale, constante pour une même unité et une même action (P02), est-elle une **vitesse** ou une **quantité de mouvement** (ou une énergie) ? Le poids porté doit-il changer la hauteur et la portée d'un saut ? |
| 2. Décidé / non décidé | **Acquis** : impulsion constante (P02) ; à 1 g, sommet à un quart d'étage (P04) ; sommet plus haut à gravité plus faible (P04) ; poids : effet sur le déplacement normal seulement par les TU, sans surcoût des pas (N11, N14).<br>**Non décidé** : effet de la charge ou du type d'unité sur le saut. |
| 3. Recommandation (PNV) | **Vitesse verticale de départ identique pour toutes les unités et toutes les charges** : `v_z0 = √(g0·H/2)`. C'est la seule lecture qui rend P04 et P05 vraies pour toute unité **sans paramètre nouveau** ; elle n'ajoute aucun effet du poids, conformément à N14. |
| 4. Alternative | **A — quantité de mouvement constante** : `v_z0 × (80/M)`, avec la référence de 80 kg de D10. L'élévation devient `(1/4)(80/M)²` étage.<br>**B — énergie constante** : `v_z0 × √(80/M)`. L'élévation devient `(1/4)(80/M)` étage.<br>**C — vitesse par type d'unité** (donnée), sans effet de la charge.<br>A et B ajoutent un effet du poids sur les sauts : c'est une mécanique nouvelle, à décider. |
| 5. Équations et exemples | À 1 g, un étage (calculé ; la capacité horizontale `v_M` est supposée inchangée) :<br>- A, 40 kg : élévation 1 étage ; `R = 2,98` ;<br>- A, 160 kg : élévation 0,0625 étage ; `R = 1,58` ;<br>- B, 40 kg : élévation 0,5 étage ; `R = 2,39` ;<br>- B, 160 kg : élévation 0,125 étage ; `R = 1,75`.<br>Avec la recommandation : 0,25 étage et `R = 2` pour tout poids. |
| 6. Compatibilité | Recommandation : P02, P04 et P05 valent pour tous. A et B : P04 et P05 ne valent plus que pour 80 kg, ce qui réinterprète ces règles et appartient au propriétaire. |
| 7. Risques et dépendances | E2 (formule de `R`), E8 (vitesse à l'atterrissage), E12 (sommet). Aucun lien avec la surcharge (N14) dans la recommandation. |
| 8. Critère de test | L'élévation mesurée ne dépend pas du poids. Test : T-J05, qui devient exact sans dimension (`1/4`, `1/2`, `1/8` d'étage). |
| 9. Question | « Une unité lourdement chargée doit-elle sauter moins haut et moins loin ? Recommandation : non. » |

### 3.5 E12 — Nombre d'étages traversés et bornes de l'esquive

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Définir `n` pour les dégâts (D03 à D05) et pour l'esquive (K05) : niveaux traversés ou `\|z_dép − z_arr\|` ; sommet au-dessus du départ ; hauteurs de terrain dans un niveau ; chute depuis un point de contact situé entre deux niveaux ; chute de moins d'un étage ; probabilités aux bornes. |
| 2. Décidé / non décidé | **Acquis** : `B(n)` pour `n` entier ≥ 1, dégâts possibles dès un étage (D01, D03, D04) ; + 5 points par niveau traversé, bornés à [0, 100] (K05), avec la formulation provisoire `\|z_dép − z_arr\|` ; impact et chute résolus séparément (D13).<br>**Non décidé** : `n` après un contact ; `n = 0` ; sommet ; tirage du pourcentage. |
| 3. Recommandation (PNV) | a) `n = ⌊z_s⌋ − z_a`, en étages. `z_s` est la hauteur du bas du volume au début de la chute : le sol de départ pour un saut, d'où `n = z_dép − z_arr` ; la hauteur du contact pour une chute verticale après un choc. `z_a` est le niveau du support atteint. Autrement dit, on compte les **sols franchis vers le bas**, celui du départ compris pour un saut.<br>b) Le **même `n`** sert à `B(n)` et à l'esquive : `p = clamp(Réactions + 5n, 0, 100)`.<br>c) Le sommet ne compte pas ; les hauteurs de terrain dans un niveau non plus (aucun modèle décidé).<br>d) `n = 0` au sol : aucun dégât de chute, puisque `B` n'est défini qu'à partir d'un étage. **`n = 0` sur une unité** (chute de moins d'un étage sur une unité, par exemple après un choc à mi-étage) : aucune règle ne s'applique, à trancher. Options : aucun dégât de base pour les deux ; collision traitée comme `n = 1`. Pour l'esquive dans ce cas : `p = clamp(Réactions, 0, 100)`, ou pas d'esquive.<br>e) Test de pourcentage entier, comme dans OXCE : entier uniforme `r` dans [0, 99], réussite si `r < p` (`src/Engine/RNG.cpp:177-180`, puis `src/Engine/RNG.h:52-55`, VC). `p` est entier, car les Réactions et `5n` le sont. |
| 4. Alternative | **A — tout étage entamé compte** : `n = ⌈z_s⌉ − z_a`. Un choc juste au-dessus du sol d'arrivée vaut alors un étage.<br>**B — compter depuis le sommet** : l'élévation compte à très faible gravité.<br>**C — `n` réel** (hauteur réelle divisée par `H`), avec `B` prolongé entre les entiers : interpolation non validée. |
| 5. Équations et exemples | Exemples :<br>- saut du niveau 2 au niveau 0 : `n = 2` ;<br>- choc contre un mur à mi-descente au-dessus du niveau 0 (`z_s = 0,5`) : `n = 0`, alors que l'alternative A donne 1 ;<br>- choc contre un plafond en montée au-dessus du trou, puis chute au niveau inférieur : `n = 1` ;<br>- esquive : `(R = 0, n = 1)` donne 5 % ; `(50, 2)` donne 60 % ; `(97, 1)` donne 100 % ;<br>- 0 % seulement si les Réactions sont ≤ `−5n`. |
| 6. Compatibilité | K05 : bornes respectées ; D01 : dégâts dès un étage ; `B` reste défini pour les seuls entiers ; aucune interpolation. Le cas `n = 0` sur une unité n'est couvert par aucune règle acquise. |
| 7. Risques et dépendances | Saut de `n` de part et d'autre d'un plan de sol (inévitable avec un comptage entier). Hauteur exactement sur un plan : calcul exact, ou règle d'appartenance. Escaliers et hauteurs de terrain : registre, N4. Esquive : pour `n ≥ 1`, 0 % est inatteignable avec des Réactions positives ou nulles, sans contradiction (la borne est un écrêtage) ; pour `n = 0`, 0 % est atteint dès que les Réactions sont nulles. Le sommet ne compte pas, mais il dépend de E11 (alternative B). |
| 8. Critère de test | `n` est unique pour toute chute déclarée. Tests : T-K02, T-K03 (comptage de `n`), T-K06, T-D12. |
| 9. Question | « Pour compter les étages d'une chute, ne faut-il compter que les sols franchis vers le bas (un étage commencé ne compte pas) ? Une chute de moins d'un étage reste-t-elle sans dégâts au sol ? Et sur une unité ? » |

## 4. Paquet 2 — Dégâts et masses (E5, E6, E7, E8, E24)

### 4.0 Chaîne de calcul qui résulterait des recommandations (PNV)

Ce tableau assemble les recommandations de E5 à E8 et de E24, pour vérifier leur cohérence. Il ne vaut pas décision. Les étapes 1 à 4 et leur ordre sont acquis (D03 à D10, J11, J12) ; le contenu marqué PNV ne l'est pas.

| Choc | 1. Base | 2. Plafond | 3. Bonus | Arrondi, puis 4. tirage | 5. Poids, puis armure et conversion |
|---|---|---|---|---|---|
| Chute au sol | `B(n)` (acquis) ; `n` : E12 | 70 | — | E5 | `f_sol(M)` (E24), puis type « impact », côté dessous (E7) |
| Unité qui tombe sur une unité | `B(n)` (PNV, E8) | 60 | jamais (J12) | E5 | `f_soi` (E6), puis côté dessous (E7) |
| Unité percutée | `B(n)` (PNV, E8) | 80 | × 1,25 si saut offensif (J11, D08) | E5 | `f_soi` (E6), puis côté sans direction (E7) |
| Obstacle | `8 × (v_n/v_ref)² × f_M` (PNV, E8 ; `f_M` acquis) | 70 | — | E5 | aucun poids de plus ; armure selon la direction (E7) |
| Unité touchée en vol, hors cible (E9 d) | `P_obs` proposé, à arbitrer | 70 ou 80 : à arbitrer | bonus de J08 : à arbitrer | E5 | à arbitrer |

**Un seul terme de poids par choc** : `f_M` pour l'obstacle, à l'étape 1 ; `f_soi` entre deux unités et `f_sol` au sol, à l'étape 5. Les plafonds bornent la puissance soumise au tirage. Les facteurs de l'étape 5 viennent après, comme le prévoit D09 : ils ne déplacent pas les plafonds.

### 4.1 E5 — Arrondis et ordre numérique

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Où et comment arrondir : `B(n)`, plafonds, bonus, entrée entière du tirage, produits de coefficients, valeurs extrêmes. |
| 2. Décidé / non décidé | **Acquis** : `B(n)` avant arrondi (D04) ; plafonds avant le tirage (D05) ; bonus après le plafond et avant le tirage (J11, D08) ; tirage de 50 à 150 %, « type explosion OXCE » (D06) ; poids et armure après le tirage (D09, dans le principe) ; aucun arrondi implicite (mandat).<br>**Non décidé** : mode et place des arrondis ; type de nombres. |
| 3. Recommandation (PNV) | a) **Calcul exact** des étapes propres à Bastion : `1,35 = 27/20` et `1,25 = 5/4`, en fractions ou en décimaux exacts. Pas de calcul binaire approché aux seuils d'arrondi. `P_obs` contient des racines carrées (par la durée de vol) : il demande une règle d'évaluation numérique et une tolérance fixes, comme en E2 (d).<br>b) **Arrondi avant le tirage** : `P = arrondi(min(base, plafond) × bonus)`, au plus proche, la moitié vers le haut.<br>c) **Tirage** entier uniforme sur `[⌊P/2⌋, ⌊3P/2⌋]`, bornes comprises : c'est la règle entière lue dans OXCE pour le tirage « explosion » (`src/Mod/RuleDamageType.cpp:81-131`, VC ; LOT-2F §4).<br>d) **Second arrondi, après le poids** (E6, E24) : `Y = arrondi(X × f)`, même règle.<br>e) Ensuite, les arrondis propres à l'enchaînement retenu en E7. Dans OXCE : modificateur de résistance arrondi à l'inférieur, conversions au plus proche (LOT-2F §4, VC).<br>f) **Extrêmes** : `P = 0` ne donne aucun dégât. `f_M` étant sans minimum, une puissance nulle est possible. |
| 4. Alternative | **A — arrondi à l'inférieur partout** : biais vers le bas (`B(5)` devient 47 au lieu de 48). Dans OXCE, les bornes du tirage et le modificateur de résistance sont arrondis à l'inférieur, mais les conversions au plus proche (LOT-2F §4, VC).<br>**B — tirage réel** uniforme sur `[0,5 P ; 1,5 P]`, arrondi à la fin : s'éloigne du tirage entier « type explosion ».<br>**C — moitié au pair** : sans biais, mais moins lisible. |
| 5. Équations et exemples | Valeurs exactes (calculées) ; recommandation, puis alternative A :<br>- cible percutée, `n = 1` : 10 → 10 ;<br>- `n = 2` : 17,5 → **18** (A : 17), seul cas de moitié exacte jusqu'à `n = 8` ;<br>- `n = 3` : 27,625 → 28 (A : 27) ;<br>- `n = 5` : 59,7465625 → 60 (A : 59) ;<br>- `n = 6` : 84,657859375 → 85 (A : 84) ;<br>- `n ≥ 7` : 100 → 100.<br>Chute au sol : `B(5) = 47,79725` → 48 (A : 47) ; `B(6) = 67,7262875` → 68 (A : 67). Bornes du tirage : `P = 18` donne [9, 27] ; `P = 17` donne [8, 25]. |
| 6. Compatibilité | D04 : `B` reste exact avant l'arrondi. D05 et D06 respectées ; ordre de J11 et D08 respecté ; D09 respectée. |
| 7. Risques et dépendances | Un second arrondi après le poids crée un petit biais. Une fonction de puissance en virgule flottante n'est pas reproductible d'une plateforme à l'autre : multiplier exactement `27/20` plutôt qu'appeler une puissance. Dépend de E6, E7, E8 et E24 pour les étapes suivantes. |
| 8. Critère de test | Chaque valeur intermédiaire est entière ou exacte, à une étape déclarée. Tests : T-D01, T-D02 (arrondi), T-D03, T-D04, T-D05. |
| 9. Question | « Faut-il arrondir au plus proche à deux moments, juste avant le tirage aléatoire et après l'effet du poids, les étapes suivantes gardant leurs propres règles ? Par exemple, 17,5 deviendrait 18. » |

### 4.2 E6 — Rapport de poids entre deux unités

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Formule **atténuée** du rapport de poids entre deux unités qui se heurtent, et ses effets sur chacune. |
| 2. Décidé / non décidé | **Acquis** : dégâts et étourdissement distincts pour les deux (K02) ; le poids influe sur les deux, sans désigner mécaniquement la plus blessée (K08) ; formule distincte de `f_M` (D10) ; plafonds 60 et 80 (D05) ; bonus de la seule cible (J11, J12) ; poids total `M` (E23, P) ; poids après le tirage, avant l'armure (D09).<br>**Non décidé** : formule, bornes, tirages communs ou séparés. |
| 3. Recommandation (PNV) | a) **Deux tirages indépendants**, un par unité : solution suffisante pour K08, sous la lecture de D-E6a.<br>b) Facteur borné, appliqué après le tirage et avant l'armure : `f_soi = 1 + β × (M_autre − M_soi) / (M_autre + M_soi)`, avec `0 ≤ β < 1`. Il vaut 1 à poids égaux et reste compris entre `1 − β` et `1 + β`.<br>c) Pour garantir K08 avant l'armure, pour toutes les hauteurs et tous les poids : `β < 2/7 ≈ 0,286` (dérivé : D-E6b). Valeur illustrative : `β = 0,25`. |
| 4. Alternative | **A — loi de puissance bornée** : `f = min(max((M_autre/M_soi)^α, a), b)`, avec `b/a < 1,8` pour la même garantie.<br>**B — partage linéaire** `2 × M_autre / (M_autre + M_soi)` : non atténué. Le rapport des facteurs croît sans borne, et K08 est violée pour de grands écarts de poids.<br>**C — aucun facteur** : contredit K08 (« le poids influe »).<br>**D — poids propre aggravant** : `f_soi = f_sol(M_soi)` (E24). Le poids de chaque unité aggrave ses propres blessures, comme N9 et N10 ; à tirage égal, la plus lourde est la plus touchée. Avec cette famille de facteurs, la même borne (`β_s < 2/7`) garantit K08. |
| 5. Équations et exemples | **D-E6a** : avec un tirage commun `X` multiplié par des facteurs fixes, le rapport des dégâts avant armure vaut `(P_t × f_t) / (P_f × f_f)`. Il est fixe : l'ordre des blessures est toujours le même. Si K08 se lit « chacun des deux ordres reste possible » (**lecture à confirmer**), ce schéma est exclu. Des tirages indépendants suffisent ; d'autres solutions existent, par exemple un aléa sur le facteur de poids.<br>**D-E6b** (pour la formule proposée) : avec des tirages indépendants, chaque unité peut être la plus touchée si `1/3 < (P_t × f_t) / (P_f × f_f) < 3`, car `1,5 / 0,5 = 3`. Rapport des bases `P_t / P_f`, avec `B(n)` comme base (E8) : de 1,25 à 5/3 pour un saut offensif, de 1 à 4/3 pour une chute accidentelle. Pour le cas le plus défavorable, `(1 + β)/(1 − β) < 3 / (5/3) = 1,8`, d'où `β < 2/7`.<br>**Exemple** (illustratif, `β = 0,25`) : cible de 80 kg, attaquant de 160 kg : `f_t = 1,083`, `f_f = 0,917`. |
| 6. Compatibilité | K02, K08, D05, J11 et J12 respectées ; `f_M` intact ; poids total `M` (E23) utilisé tel quel. |
| 7. Risques et dépendances | La garantie ne vaut qu'avant l'armure : une grande différence d'armure peut décider seule de l'ordre des blessures. Avec la formule (b), un attaquant lourd est moins blessé : tension avec N9 et N10 (§6.3, C3), que l'alternative D évite. Dépend de E8 (base `B(n)`) et de E5 (arrondis). |
| 8. Critère de test | Pour deux poids déclarés, sur un grand nombre de tirages, chacun des deux ordres de blessures apparaît. Tests : T-D14 ; T-K04. |
| 9. Question | « Quand une unité tombe sur une autre, l'écart de poids doit-il changer les blessures de chacune par un facteur borné, avec un tirage par unité, pour que le hasard puisse encore décider laquelle est la plus touchée ? La force du facteur serait fixée ensuite (§0.2). » |

### 4.3 E7 — Type de dégâts, armure, santé et étourdissement

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Type de dégâts ; interaction avec les protections d'OXCE ; côté d'armure ; santé, étourdissement et mise hors de combat. |
| 2. Décidé / non décidé | **Acquis** : tirage « type explosion OXCE » (D06) ; étourdissement possible pour les deux unités (K02) ; l'armure peut protéger (N9) ; résistance du terrain d'OXCE (D12). La conversion finale décrite par le mandat comme règle du moteur n'est pas déclarée reprise (D07, ouvert).<br>**Non décidé** : type, côté, valeurs de conversion, mise hors de combat. |
| 3. Recommandation (PNV) | a) Un **type de dégâts propre à Bastion, « impact »**, dont le mécanisme suit l'enchaînement lu dans OXCE (LOT-2F §4, VC) : tirage de type explosion, écart 50 ; modificateur de résistance de l'armure au type ; côté ; armure du côté × efficacité ; conversion ; application. Les valeurs (résistances, taux de conversion) sont des données de Bastion, à fixer. **Aucune valeur d'un type OXCE n'est reprise** (D4).<br>b) **Côté** :<br>- unité qui tombe, au sol ou sur une unité : côté **dessous**, comme OXCE le choisit pour un impact venu d'en dessous (`src/Savegame/BattleUnit.cpp:1644-1647`, VC) ;<br>- unité percutée par le haut : côté par défaut, **sans direction**. Dans OXCE, un type sans direction garde le côté avant et le torse (`:1630-1631`, `:1642`, VC), sauf si un script (`:1716-1738`) ou un forçage du côté ou de la partie touchée (`:1741-1748`) les change ;<br>- obstacle : côté selon la direction relative, par la règle d'OXCE (`:1648-1684`, VC).<br>c) **Conversion** en santé et en étourdissement (K02), taux à fixer.<br>d) **Mise hors de combat** comme dans OXCE : santé ≤ 0, ou santé ≤ étourdissement (`BattleUnit.cpp:2172-2175`, VC). |
| 4. Alternative | **A — sans direction pour tous les chocs** : le plus simple, une seule armure (l'avant).<br>**B — reprendre un type existant d'OXCE** (explosif ou mêlée) : cela reprendrait ses valeurs de règles, contraire à D4.<br>**C — nouveau côté « dessus »** : nouvelle donnée d'armure. OXCE n'a pas de côté « dessus » (`src/Mod/Unit.h:44`, VC). |
| 5. Équations et exemples | Lecture d'OXCE (VC) : pour un impact venu exactement d'au-dessus, le code calcule une direction relative fixe (9). Il en tire un côté qui dépend de l'orientation de l'unité (`BattleUnit.cpp:1648-1684`). La tête n'est touchée que si la hauteur relative de l'impact atteint la taille de l'unité (`:1686-1689`, VC) ; qu'un impact venu exactement d'au-dessus la remplisse est une inférence (INF). C'est pourquoi la recommandation (b) ne le reprend pas pour l'unité percutée. Taux de conversion par défaut d'un type dans OXCE (VC, `RuleDamageType.cpp:35-36`) : santé × 1,0 ; étourdissement × 0,25, tiré au hasard ; usure de l'armure × 0,1 ; terrain × 0,5. Ils sont cités pour comparaison, sans reprise. |
| 6. Compatibilité | D06 : le tirage est une propriété du type « impact » ; D07 serait tranché comme « mécanisme repris, valeurs propres à Bastion », si le propriétaire l'accepte ; D12 séparée ; N9 respectée. |
| 7. Risques et dépendances | Les valeurs fixent l'équilibrage, qui appartient au propriétaire. L'étourdissement tiré au hasard ajoute un second aléa. Insensibilité à la douleur (OXCE : étourdissement ignoré). Dépend de E5 ; sert à E24. |
| 8. Critère de test | Avec des valeurs d'armure et de conversion fictives déclarées, l'enchaînement donne des dégâts exacts. Tests : T-D13 ; T-D01 (conversion). |
| 9. Question | « Les chutes et les collisions doivent-elles avoir un type de dégâts propre à Bastion, traité comme dans OXCE (armure, puis santé et étourdissement), avec l'armure du dessous pour l'unité qui tombe ? » |

### 4.4 E8 — Vitesse au contact et puissance d'impact

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Convertir la vitesse normale au contact `v_n` en puissance d'impact ; l'articuler avec `B(n)` et les collisions entre unités ; éviter de compter deux fois une même contribution ; cas du contact au sommet. |
| 2. Décidé / non décidé | **Acquis** : contre un obstacle, puissance commune fondée sur la vitesse réelle au contact et sur `M`, avec le facteur `f_M = min(M/80, 3)` (D10) ; vitesse normale distincte de la vitesse tangentielle ; phases pour le seul diagnostic (D11) ; plafonds obstacle 70, unité qui tombe 60, cible 80, sol 70 (D05) ; impact et chute résolus séparément (D13).<br>**Non décidé** : formule de `P_obs` ; base des collisions entre unités ; classement des surfaces. |
| 3. Recommandation (PNV) | a) **Classer le contact** par la normale de la surface touchée. Surface tournée vers le haut (sol, dessus d'un objet) : chute au sol, base `B(n)` (E12) ; cela vaut aussi pour l'atterrissage prévu d'un saut. Toute autre surface (mur, côté d'un objet, plafond) : obstacle. Contact avec le volume d'une unité, sur n'importe quelle face : collision entre unités (c).<br>b) **Obstacle** : `P_obs = min(70, 8 × (v_n / v_ref)² × f_M)`. `v_ref` est la vitesse d'atterrissage du saut de référence (1 g, un étage) : `v_ref² = v_z0² + 2·g0·H = 2,5·g0·H`. Sans dimension : `P_obs = min(70, 3,2 × ṽ_n² × f_M)`.<br>c) **Collisions entre unités** : base `B(n)`, avec le même `n` que la chute (`n = z_dép − z_arr` pour un saut sur la cible). C'est la lecture la plus directe de D03 à D05, à confirmer. Plafonds 60 et 80 ; la vitesse n'intervient pas. Cas `n = 0` : E12 (d).<br>d) **Pas de double comptage** : la vitesse ne sert qu'aux obstacles, la hauteur `n` qu'aux chutes et aux collisions, le poids une seule fois par choc (§4.0).<br>e) **Puissance commune** : `P_obs`, avant le tirage, sert aussi au terrain (D12). Pour un impact direct, OXCE fait un tirage pour le terrain : un tirage propre sur `[⌊P/2⌋, ⌊3P/2⌋]` (méthode 1, par défaut) ou la reprise du tirage fait pour l'unité (méthode 2), puis un facteur, 0,5 par défaut (`RuleDamageType.cpp:35`, `:37`, `:139-142`, VC ; LOT-2F §4). La méthode et le facteur sont à choisir (§0.2). |
| 4. Alternative | **A — hauteur équivalente** : `n_eq = v_n² / (2·g0·H)`, et `B` prolongé aux nombres réels (interpolation non validée).<br>**B — linéaire en vitesse** : `8 × (v_n / v_ref) × f_M`, plus fort pour les chocs lents.<br>**C — `B(n)` aussi pour les obstacles** : ignore la vitesse réelle, contraire à D10. |
| 5. Équations et exemples | Calculés, sans dimension ; `P_obs / f_M` avant plafond :<br>- atterrissage du saut de référence : `ṽ² = 2,5`, donc 8, égal à `B(1)` (calage) ;<br>- mur à 1 g, un étage, `λ = 1` : 0,61 pour une case, 2,44 pour deux cases ;<br>- même mur avec `λ = 1,5` : 1,38 et 5,5 ;<br>- plafond en montée à 1 g : 1,6 au départ, 0,8 à `1/8` d'étage, **0 au sommet** (`v_n = 0`) ;<br>- le plafond de 70 est atteint quand `ṽ_n² × f_M ≥ 21,875`. |
| 6. Compatibilité | D10 (vitesse réelle, `f_M`), D05 (plafond 70 pour l'obstacle ; quatre plafonds inchangés), D11 (vitesse normale, aucun coefficient de phase), D12 (règles de terrain d'OXCE) et D13 respectées. |
| 7. Risques et dépendances | `λ` change beaucoup la force des chocs contre un mur (E1). Les chocs latéraux sont faibles, donc les obstacles rarement détruits : effet d'équilibrage, à juger par le propriétaire. Surfaces obliques : absentes du modèle en pavés. Contacts simultanés : E1 (g). Différence de dépendance à la gravité avec les chutes au sol : §6.3.<br>**Conséquence visible** : avec (a), tout saut offensif vers une case vide blesse le sauteur (chute au sol, `B(n) ≥ 8` avant le tirage), comme E18 le prévoit après une esquive. Autre choix : un atterrissage prévu ne blesse pas (règle nouvelle). |
| 8. Critère de test | Pour une vitesse normale et un poids déclarés, `P_obs` est exact. Tests : T-D03 (la colonne obstacle devient sans objet), T-D05 (base `B(n)`), T-D09 (dégâts), T-D10, T-D12, T-J10 (dégâts), T-J15 (blessure du sauteur). |
| 9. Question | « Contre un mur ou un plafond, la force du choc doit-elle suivre le carré de la vitesse, avec pour repère l'atterrissage d'un saut d'un étage (8 points) ? Une chute sur une unité utilise-t-elle les mêmes dégâts de base qu'une chute au sol ? » |

### 4.5 E24 — Poids, armure et caractéristiques lors d'une chute au sol

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Effets du poids total, de l'armure, des caractéristiques et de l'équipement sur une chute au sol, sans double comptage. |
| 2. Décidé / non décidé | **Acquis** : les caractéristiques et équipements **peuvent** modifier les conséquences (N8) ; l'armure peut protéger, mais son poids peut aggraver (N9) ; le poids de l'inventaire compte (N10) ; base fixée par le nombre d'étages (D03), plafond 70 (D05), tirage (D06) ; poids et armure après le tirage (D09) ; poids total `M` (E23).<br>**Non décidé** : formule ; effet des caractéristiques. |
| 3. Recommandation (PNV) | a) `Y = arrondi(X × f_sol(M))`, avec `f_sol(M) = 1 + β_s × (M − 80) / (M + 80)` : même famille atténuée que E6, avec la référence de 80 kg de D10.<br>b) Puis l'armure du dessous, avec le type « impact » (E7).<br>c) Aucun effet des caractéristiques au départ (N8 dit « peuvent ») ; l'équipement agit seulement par son poids (dans `M`) et par l'armure.<br>d) `f_M` n'est pas utilisé pour une chute au sol : le poids n'est compté qu'une fois. |
| 4. Alternative | **A — `f_M` après le tirage** : aucune formule nouvelle, mais un effet fort et non plafonné, jusqu'à `70 × 1,5 × 3 = 315` avant armure.<br>**B — `f_M` avant le plafond**, comme pour un obstacle : la base ne serait plus fixée par la seule hauteur, contraire à D03.<br>**C — une caractéristique** (par exemple les Réactions) réduit les dégâts : mécanisme nouveau, que N8 permet, à décider plus tard. |
| 5. Équations et exemples | `f_sol` avec `β_s = 0,25` (illustratif), pour M = 40, 80, 160, 240 et 320 kg : 0,917 ; 1 ; 1,083 ; 1,125 ; 1,15 (calculés). Exemple : chute de deux étages, `P = 14`, tirage dans [7, 21] ; à 160 kg, `Y = arrondi(X × 1,083)`. |
| 6. Compatibilité | N8 respectée (« peuvent ») ; N9 : protection par l'armure, aggravation par son poids dans `M` ; N10 respectée ; D03 et D05 : base et plafond inchangés ; D10 : `f_M` intact. |
| 7. Risques et dépendances | Tension avec la formule proposée en E6 pour l'unité qui tombe sur une autre (§6.3, C3). Les valeurs fixent l'équilibrage. Dépend de E7 (côté), de E5 (arrondi) et de E8 (classement d'un atterrissage en chute au sol). |
| 8. Critère de test | Avec un poids et une armure fictifs déclarés, les dégâts d'une chute au sol sont exacts, et croissent avec `M` à tirage égal. Tests : T-D01 ; T-K03 (attaquant). |
| 9. Question | « Dans une chute au sol, le poids total doit-il aggraver un peu les blessures, par un facteur borné dont la force serait fixée ensuite (§0.2), l'armure protégeant ensuite, sans effet des caractéristiques pour l'instant ? » |

## 5. Paquet 3 — Règles d'action et résolution (E9, E13, E17)

### 5.1 E9 — Ordre des événements et cas limites

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Ordre des collisions multiples ; destination devenue occupée ou libre ; tailles d'unités ; perte de support ; chaîne de chutes. Règles : I03, I04, D13, K01 à K08 ; tests T-X01 à T-X04. |
| 2. Décidé / non décidé | **Acquis** : résolution chronologique (I03) ; arrêt à l'impact contre un obstacle, même détruit, puis chute verticale si l'unité est sans support, dégâts séparés (D13) ; aucun résultat automatique pour les cas non arbitrés (I04) ; aucune révélation anticipée (I01) ; cible cachée percutée (J05, J07) ; esquive (K03 à K07) ; chute au sol de l'attaquant après une esquive (E18, P).<br>**Non décidé** : le reste, dont la place finale de l'attaquant après une collision (sous-question relevée, h). |
| 3. Recommandation (PNV) | a) **Monde figé** : pendant une action, seules bougent l'unité qui agit et les unités que l'action met en mouvement (esquive, chute).<br>b) **File d'événements chronologique**. À temps égal, ordre fixe : l'unité qui agit d'abord, puis par identifiant croissant.<br>c) **Le vol s'arrête au premier contact**, quel qu'il soit (extension de D13). Un même vol ne connaît donc jamais plusieurs chocs ; une chaîne ne vient que des chutes qui suivent.<br>d) **Unité sur l'arc, autre que la cible** : connue, elle interdit le saut avant l'engagement (comme un obstacle connu, P08). Inconnue, elle arrête le vol et est révélée (S11). Pour le choc, proposition : obstacle pour le sauteur, unité percutée pour l'autre, sur la base `P_obs` ; le plafond (70 ou 80) et l'éventuel bonus de J08 sont à arbitrer. **La cible** (unité sur la case visée : J05, J07, J13) est exclue de cette règle : le premier contact avec son volume, sur n'importe quelle face, déclenche la collision prévue (E8 c), avec `n = z_dép − z_arr`. Sans cette exclusion, viser un ennemi visible serait interdit, contrairement à E14.<br>e) **Destination libérée** par une esquive : chute au sol de l'attaquant (E18, acquis). **Destination devenue occupée** pendant le vol : impossible sous (a) (dérivé : seule la cible peut bouger, et seulement en quittant la case).<br>f) **Arrivée sans support** (sol absent ou inconnu) : chute verticale jusqu'au premier support. Une seule chute est comptée depuis le niveau de départ (E12). Si une unité s'y trouve, c'est une collision accidentelle, sans bonus : ce n'est pas la case visée.<br>g) **Perte de support** (sol détruit, D12) : les unités qui s'y trouvent tombent (N5). Leurs chutes entrent dans la file à l'instant de la destruction, avec les mêmes règles (esquive, collision).<br>h) **Place finale après une collision non esquivée** : si la cible est hors de combat et ne compte plus comme occupant la case au sens de S10 (point non décidé), l'attaquant reste sur la case. Sinon, il est placé sur une case voisine libre, avec un sol, au même niveau, tirée comme pour l'esquive, sans dépense de TU. S'il n'y en a aucune : à arbitrer (options : écarter la cible comme le fait OXCE, LOT-2E C7, VC ; mettre l'attaquant hors de combat ; chercher plus loin).<br>i) **Grandes unités** : hors de `MEC-0001` jusqu'à un mandat dédié (lot supplémentaire, signalé au §6.6). Elles ne sautent pas ; une case occupée par une grande unité ne peut pas être visée. |
| 4. Alternative | **A — monde dynamique** : d'autres unités peuvent agir pendant le vol (réactions). Il faut alors des règles de priorité.<br>**B — unités toujours solides** : la cible elle-même bloquerait le saut, ce qui contredit J05, J07 et J13.<br>**C — reprendre la règle d'OXCE pour la place finale** : la cible est écartée vers une case voisine (LOT-2E C7). Cela peut contredire « cible immobile » (K07) si on lit cette règle au sens large. |
| 5. Équations et exemples | Chaîne type, avec les recommandations : saut, choc contre un mur inconnu (`P_obs`), chute verticale d'un étage (`n = 1`), sol (`B(1) = 8`). Chaque choc a son propre tirage. |
| 6. Compatibilité | I03 et D13 respectées. I04 aussi : chaque résultat proposé est soumis au propriétaire, aucun n'est adopté. |
| 7. Risques et dépendances | Le monde figé exclut toute réaction pendant le vol. Dans OXCE, des réactions sont possibles à l'atterrissage (LOT-2E C6) ; les interruptions restent ouvertes au registre. L'ordre par identifiant est arbitraire, mais déterministe. Exclure les grandes unités restreint le jeu. Le contact latéral avec la cible est possible avec un volume en pavé (E1, rubrique 7). Dépend de E1 (volumes), E8 (chocs), E12 et E17. |
| 8. Critère de test | Chaque scénario déclaré donne une suite unique d'événements. Tests : T-X01 (devient un test d'impossibilité), T-X02, T-X03, T-X04 (refus), T-D12 ; place finale : T-J12, T-K04. |
| 9. Question | « Pendant un saut, faut-il considérer que rien d'autre ne bouge (sauf l'esquive et les chutes provoquées), que le vol s'arrête au premier choc, et que les grandes unités sont exclues pour l'instant ? Où l'attaquant finit-il quand la cible n'esquive pas et reste debout ? » |

### 5.2 E13 — Coût en TU du déplacement d'un saut

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Coût en TU du déplacement qui compose un saut (`C_dép`) et moment du paiement. |
| 2. Décidé / non décidé | **Acquis** : supplément `C_att = max(1, ⌊0,20 × TU_max⌋)`, en plus du déplacement, payé à l'engagement, jamais remboursé, même en cas d'échec ou d'esquive (J09) ; TU insuffisantes : attaque impossible (J10) ; prévisualisation du coût dans les limites de la connaissance (I02).<br>**Non décidé** : `C_dép` ; son paiement ; remboursement en cas d'interruption ; seuil complet. |
| 3. Recommandation (PNV) | a) `C_dép = c_s × (\|Δx\| + \|Δy\|)`, où `c_s` est un nombre entier de TU par case de portée, à choisir.<br>b) Le total `C = C_dép + C_att` est **payé en entier à l'engagement** et jamais remboursé, comme J09.<br>c) Sélection permise seulement si les TU restantes sont ≥ `C` (seuil de J10).<br>d) La prévisualisation affiche `C`. Il ne dépend que de la case visée : aucune information cachée ne peut l'influencer (I01). |
| 4. Alternative | **A — coût de marche d'un trajet fictif** en ligne droite, sur les cases survolées : dépend du modèle de coûts du terrain, encore ouvert au registre.<br>**B — `C_dép = 0`**, comme une chute dans OXCE (0 TU, LOT-2E C5, VC) : seul `C_att` compte, et « en plus du déplacement » devient sans objet.<br>**C — `C_dép` payé à l'atterrissage**, remboursé en cas d'interruption : plus complexe, et la prévisualisation devient incertaine. |
| 5. Équations et exemples | Exemple illustratif : `c_s = 4`, `TU_max = 54` (`C_att = 10`), distance 2 : `C = 8 + 10 = 18`. Avec 17 TU restantes, le saut est refusé. |
| 6. Compatibilité | J09, J10 et I02 respectées. |
| 7. Risques et dépendances | `c_s` est une valeur d'équilibrage. La surcharge (N14) réduit les TU disponibles, donc les sauts possibles. Indépendance vis-à-vis du modèle de coûts du terrain, ce qui est un avantage. La diagonale `(1, 1)` coûte autant que `(2, 0)`, en cohérence avec la portée en Manhattan. |
| 8. Critère de test | Pour `c_s` et `TU_max` déclarés, `C` est exact et payé en entier dans tous les cas. Tests : T-J07, T-J15, T-J18 (coût total), T-J19 (seuil complet). |
| 9. Question | « Le déplacement d'un saut doit-il coûter un nombre fixe de TU par case de portée, payé avec le supplément offensif au moment du saut, sans remboursement ? » |

### 5.3 E17 — Esquive : TU, cases voisines et visibilité

| Rubrique | Contenu |
|---|---|
| 1. Énoncé | Esquive pendant le tour adverse ; TU utilisées ; cases voisines valides (diagonales, niveau, visibilité) ; moment où la condition « voit » est évaluée. |
| 2. Décidé / non décidé | **Acquis** : esquive automatique seulement si la cible voit actuellement l'unité qui tombe, a les TU du pas et une case voisine libre et accessible (K03) ; choix aléatoire d'une case valide (K04) ; probabilité (K05) ; paiement des TU normales du pas en cas de réussite seulement (K06) ; aucune dépense en cas d'échec (K07).<br>**Non décidé** : quelles TU ; cases valides ; informations utilisées ; moment de l'évaluation. |
| 3. Recommandation (PNV) | a) **TU** : celles qui restent à la cible au moment de la chute, quel que soit le tour. Dans OXCE, les TU d'une unité ne sont renouvelées qu'au début du tour de sa faction (`src/Savegame/SavedBattleGame.cpp:1599-1602`, VC). Cette recommandation suppose le même renouvellement dans Bastion, encore ouvert au registre (« capital initial et renouvellement des TU »).<br>b) **Cases candidates** : les 8 voisines au même niveau, atteignables par un pas de marche normal (S1 à S4, N1, N2, S10), avec un sol, et dont le coût du pas (× 1,5 en diagonale, S2) ne dépasse pas les TU restantes.<br>c) **Informations** : celles du camp de la cible, comme pour la marche (S6 à S8). Si la case tirée contient une unité inconnue de ce camp, celle-ci est révélée (S11) et l'esquive échoue, sans dépense.<br>d) **« Voit actuellement »** : évalué au début de la chute (engagement du saut, ou début d'une chute accidentelle), selon les règles de visibilité, encore ouvertes au registre.<br>e) **Ordre** : conditions, puis tirage de `p` (E12), puis choix au hasard parmi les candidates (loi : E22, hors des 13), puis paiement du pas. |
| 4. Alternative | **A — état réel du terrain** : plus simple, mais l'absence d'esquive vers une case qui paraît libre peut trahir une unité cachée.<br>**B — visibilité vérifiée pendant tout le vol** (ligne de vue le long de l'arc) : plus réaliste, plus coûteux.<br>**C — tirer une case parmi toutes les valides**, puis échouer si ses TU ne suffisent pas : plus d'échecs arbitraires. |
| 5. Équations et exemples | Exemple fictif : la cible a 3 TU. Voisines : un pas droit de coût 2, une diagonale de coût `⌊1,5 × 2⌋ = 3`, un pas droit de coût 4. Les candidates sont les deux premières. |
| 6. Compatibilité | K03 à K07 respectées, ainsi que S2, N2 et S10. |
| 7. Risques et dépendances | Dépend des règles de visibilité, du modèle de coûts du terrain et du renouvellement des TU, ouverts au registre. Escaliers et échelles exclus de l'esquive ; grandes unités : E9 (i) ; loi du tirage : E22. |
| 8. Critère de test | Pour un terrain, des TU et une visibilité déclarés, l'ensemble des cases candidates est unique. Tests : T-K01, T-K03 (esquive) ; T-K05 reste inchangé (loi du tirage : E22). |
| 9. Question | « L'esquive doit-elle utiliser les TU qui restent à la cible depuis son propre tour, vers l'une des 8 cases voisines au même niveau, connue de son camp et qu'elle peut payer ? » |

## 6. Paquet 4 — Vérification transversale

### 6.1 Compatibilité avec les règles acquises

| Règle acquise | Source | Effet des recommandations | Préservée ? |
|---|---|---|---|
| Élévation d'un quart d'étage à 1 g, plus haute à faible gravité | P04 | E11 la rend vraie pour toutes les unités ; E2 et E3 l'utilisent telle quelle | oui |
| Portée de 2 cases en Manhattan à 1 g et un étage ; dépendance à `g` et `D` | P05, P06 | E2 : `R(1, 1) = 2` exactement ; aucune borne euclidienne | oui |
| Collision du volume ; mur, sol ou plafond qui coupe le volume bloque | P07 | E1 : appliquée, **sauf le sol de départ** (exception soumise au propriétaire) | à trancher (§6.3, C1) |
| Obstacle connu : action interdite ; inconnu : interruption et révélation | P08 | E1, E9 : appliquée, et étendue aux unités sur l'arc (proposition) | oui |
| Plafonds 70, 60, 80 et 70, avant le tirage | D05 | §4.0 : les quatre plafonds sont appliqués avant le tirage, sans changement | oui |
| Bonus × 1,25 après le plafond, avant le tirage ; jamais pour l'attaquant | J11, J12, D08 | §4.0 : même place | oui |
| Tirage de 50 à 150 %, type explosion OXCE | D06 | E5 : règle entière lue dans OXCE ; E7 : propriété du type « impact » | oui |
| `B(n)` exact avant arrondi ; dégâts dès un étage | D01, D03, D04 | E5 : calcul exact ; E12 : `n` entier, aucune interpolation | oui |
| Facteur `min(M/80, 3)` contre un obstacle, sans minimum | D10 | E8 : utilisé à l'étape 1, et seulement pour les obstacles | oui |
| Supplément offensif, payé à l'engagement, jamais remboursé | J09, J10 | E13 : le coût de déplacement suit la même règle | oui |
| + 5 points par niveau traversé, borné à [0, 100] | K05 | E12 : même `n` que pour les dégâts | oui |
| Esquive : conditions, choix aléatoire, paiement en cas de réussite seulement | K03 à K07 | E17 : précisée sans changement | oui |
| E14, E18 et E23 | P | Ni remises en cause ni réinterprétées : E9 (e) et E8 les utilisent | oui |
| Surcharge selon OXCE, sans effet du poids sur les pas | N11, N14 | E11 : aucun effet du poids sur les sauts | oui |

### 6.2 Dépendances entre les points

| Point | Dépend de | Influence |
|---|---|---|
| E1 | — | E3 (plafond), E8 (`λ` et chocs latéraux), E9 (volumes, cible), E12 (hauteur d'un contact) |
| E11 | — | E2 (`R`), E8 (vitesse à l'atterrissage), E12 (sommet, alternative B) |
| E2 | E11 | E3 (borne haute), E13 (distance payée) |
| E3 | E1, E2 | — |
| E12 | E1, E11 | E8 (`n` des collisions), E9 (chaînes), E17 (`p`) |
| E8 | E1, E11, E12 | E5 (valeurs à arrondir), E6 (base des collisions), E9 (chocs), E24 (atterrissage = chute au sol) |
| E5 | E8 | E6, E7, E24 (arrondis suivants) |
| E6 | E5, E8 | — (même famille de facteur que E24) |
| E7 | E5 | E24 (côté dessous) |
| E24 | E5, E7, E8 | — |
| E9 | E1, E8, E12, E17 | — |
| E13 | E2 | — (indépendant du modèle de coûts du terrain) |
| E17 | E12 | E9 (place des unités) |

### 6.3 Incompatibilités et tensions relevées

| # | Constat | Règles en jeu | Nature | Solutions (aucune adoptée) |
|---|---|---|---|---|
| C1 | Un saut court parti du centre de la case coupe le sol de départ dès que l'unité est un peu large (D-E1b) | P07, P04, P05 ; départ au centre (non décidé) | **incompatibilité démontrée**, sous hypothèses | E1 (f), A1 ou A4 |
| C2 | Les tests T-J02, T-J03 `(1, 1)` et T-J11 sont classés « spécifiables » au LOT-2F, mais leur résultat dépend de C1 | C1 ; matrice du LOT-2F | statut à requalifier lors d'une mise à jour autorisée ; **la matrice du LOT-2F n'est pas modifiée ici** | voir `LOT-2G-IMPACTS-TESTS.md` §2 |
| C3 | Dans une collision, un attaquant plus lourd est **moins** blessé avec la formule proposée en E6, alors que N9 et N10 disent que le poids **aggrave** une chute | E6 (PNV), N9, N10 ; K08 ne fixe pas le sens de l'effet | tension créée par la proposition | (i) formule de E6 dans une collision, N9 et N10 pour la chute au sol seulement (recommandé) ; (ii) appliquer aussi `f_sol` à l'attaquant (deux termes de poids : double comptage possible) ; (iii) alternative D de E6 : le poids propre de chaque unité aggrave ses propres blessures, compatible avec N9 et N10 |
| C4 | Une chute au sol ne dépend pas de la gravité (base fixée par la hauteur), un choc contre un obstacle si (vitesse réelle) | D03, D10 | conséquence, pas une contradiction | aucune action ; une dépendance à la gravité des chutes modifierait D03 et sortirait de ce lot |
| C5 | Aucune règle ne place l'attaquant après une collision non esquivée, la cible restant sur sa case | S10, K07 | lacune | E9 (h) |
| C6 | Pour `n ≥ 1`, avec des Réactions positives ou nulles, l'esquive réussit au moins 5 % du temps ; pour `n = 0`, elle peut valoir 0 % | K05 | conséquence (LOT-2F, E12) | aucune action pour `n ≥ 1` ; cas `n = 0` : E12 (d) |

### 6.4 Liens avec les points hors des 13

| Point | Lien direct avec les propositions |
|---|---|
| E4 (phases) | Les propositions n'utilisent aucune phase ; `v_n` porte seule l'effet (E8). |
| E10 (portée des validations) | Inchangé : ce dossier ne couvre que les 13 points. |
| E15 (S7 et arc du saut) | Les cases survolées doivent-elles être explorées ? Les propositions de E1 et E9 ne le supposent pas. |
| E16 (« trois blocs ») | À confirmer avant toute inscription au registre. |
| E19 (chute volontaire) | Une chute volontaire utiliserait E12, E24 et E7. |
| E20 (unité de la charge portée) | E6 et E24 utilisent `M` en kg ; l'unité de la charge portée reste ouverte. |
| E21 (N7 au registre) | Inchangé : N7 reste contredite au registre par D01. La recommandation de E12 (`n = 0` au sol sans dégâts) est compatible avec D01. |
| E22 (loi du tirage de la case d'esquive) | Utilisée par E17 (e) et E9 (h). |
| Registre, « encore ouvert » | Modèle de coûts du terrain (coût du pas d'esquive, E17) ; règles de visibilité (E17) ; capital initial et renouvellement des TU (E17 a) ; interruptions et réactions (E9) ; escaliers et hauteurs de terrain (E12) ; taille des unités (E9) ; chutes involontaires en apesanteur (E3). |

### 6.5 Références OXCE utilisées

Lecture du code au commit `441cae1`, sans exécution. Ces références décrivent OXCE. Aucune ne fait d'une proposition une « référence OXCE » : les propositions restent des adaptations de Bastion.

| Comportement lu | Emplacement | Statut | Utilisé pour |
|---|---|---|---|
| Une case compte 16 × 16 × 24 voxels | `src/Battlescape/Position.h:34-35` | VC | E1 (comparaison) |
| Côtés d'armure : avant, gauche, droit, arrière, dessous ; aucun côté « dessus » | `src/Mod/Unit.h:44` | VC | E7 |
| Côté dessous si l'impact vient exactement d'en dessous ; sinon, côté selon la direction relative et l'orientation | `src/Savegame/BattleUnit.cpp:1642-1688` | VC | E7 |
| Type sans direction : côté avant et torse par défaut, sauf script ou forçage | `BattleUnit.cpp:1630-1631`, `:1642`, `:1716-1738`, `:1741-1748` | VC | E7 |
| Tête touchée si la hauteur relative de l'impact atteint la taille de l'unité | `BattleUnit.cpp:1686-1689` | VC (cas d'un impact venu d'au-dessus : INF) | E7 |
| Tirage pour le terrain : méthode 1 (tirage propre, par défaut) ou 2 (reprise du tirage de l'unité) | `src/Mod/RuleDamageType.cpp:37`, `:139-142` | VC | E8 |
| Hors de combat si santé ≤ 0 ou santé ≤ étourdissement | `BattleUnit.cpp:2172-2175` | VC | E7 |
| Taux par défaut d'un type de dégâts (santé, étourdissement, armure, terrain) | `src/Mod/RuleDamageType.cpp:35-36` | VC | E7, E8 |
| Tirage « explosion » entier sur `[⌊P/2⌋, ⌊3P/2⌋]` | `RuleDamageType.cpp:81-131` (LOT-2F §4) | VC | E5 |
| Test de pourcentage : entier dans [0, 99] inférieur à la valeur | `src/Engine/RNG.cpp:177-180`, puis `src/Engine/RNG.h:52-55` (LOT-2F §3.6) | VC | E12 |
| TU renouvelées au début du tour de la faction de l'unité seulement | `src/Savegame/SavedBattleGame.cpp:1599-1602` ; `BattleUnit.cpp:2837-2887` | VC | E17 |
| Chute arrêtée au plus tard au niveau 0 ; coût nul ; unité dessous écartée ou mise hors de combat | LOT-2E C4, C5, C7 | VC (LOT-2E) | E3, E9, E13 |

### 6.6 Lotissement

Aucun lot supplémentaire n'est proposé pour l'arbitrage lui-même. Sont signalés :
- les arbitrages peuvent se faire en deux temps, d'abord DS1 et DS2, puis DS3 à DS5 ;
- leur inscription au registre exigera un mandat distinct, expressément autorisé (mandat LOT-2G §8) ;
- deux propositions renvoient à un futur mandat dédié, qui serait un lot supplémentaire : les grandes unités (E9 i) et, si l'alternative C de E3 était choisie, l'apesanteur et la très faible gravité.

## 7. Questions au propriétaire

Rien n'est décidé tant que vous n'avez pas répondu. Une question par décision structurante, chacune avec ses sous-points ; chaque sous-point renvoie à la recommandation du point indiqué. Les valeurs chiffrées (§0.2) ne sont demandées qu'ensuite.

1. **DS1 — Géométrie.**
   - a) Les règles peuvent-elles se passer de mètres, en ne gardant que les proportions entre une case, un étage et une unité ? (E1)
   - b) Le sol que l'unité quitte peut-il bloquer un saut court ? Recommandation : non, on l'ignore pendant le vol. (E1, C1)
   - c) Le volume d'une unité est-il une boîte, et la cible visée déclenche-t-elle la collision quelle que soit la face touchée ? (E1, E9)
2. **DS2 — Saut.**
   - a) Une unité lourdement chargée doit-elle sauter moins haut et moins loin ? Recommandation : non. (E11)
   - b) La portée reste-t-elle comptée en cases, une diagonale comptant deux cases, et grandit-elle avec la durée du vol, sans arrondi ? (E2)
   - c) Le saut offensif n'existe-t-il que dans une plage de gravité, et est-il indisponible en dehors et en apesanteur ? (E3)
3. **DS3 — Comptage et nombres.**
   - a) Ne compte-t-on que les sols franchis vers le bas ? Une chute de moins d'un étage reste-t-elle sans dégâts au sol ? Que se passe-t-il si elle se termine sur une unité ? (E12)
   - b) Arrondit-on au plus proche avant le tirage, puis après l'effet du poids, les étapes suivantes gardant leurs propres règles ? (E5)
4. **DS4 — Chocs.**
   - a) Une chute sur une unité a-t-elle les mêmes dégâts de base qu'une chute au sol ? Un atterrissage prévu sur une case vide blesse-t-il le sauteur comme une chute au sol ? (E8)
   - b) Contre un mur ou un plafond, la force suit-elle le carré de la vitesse, avec 8 points pour l'atterrissage d'un saut d'un étage ? (E8)
   - c) Entre deux unités, l'écart de poids change-t-il les blessures par un facteur borné, chacune ayant son propre tirage ? Le poids propre doit-il réduire ou aggraver ses propres blessures ? (E6, C3)
   - d) Au sol, le poids total aggrave-t-il un peu les blessures, l'armure protégeant ensuite, sans effet des caractéristiques pour l'instant ? (E24)
   - e) Les chutes et collisions ont-elles un type de dégâts propre à Bastion, traité comme dans OXCE, avec l'armure du dessous pour l'unité qui tombe ? Pour le terrain, faut-il un tirage propre ou la reprise du tirage de l'unité ? (E7, E8)
5. **DS5 — Déroulement d'une action.**
   - a) Pendant un saut, rien d'autre ne bouge-t-il que l'esquive et les chutes provoquées, et le vol s'arrête-t-il au premier choc ? (E9)
   - b) Où finit l'attaquant quand la cible n'esquive pas et reste debout ? (E9, C5)
   - c) Les grandes unités sont-elles exclues des sauts pour l'instant ? (E9)
   - d) Le déplacement d'un saut coûte-t-il un nombre fixe de TU par case, payé avec le supplément offensif au moment du saut ? (E13)
   - e) L'esquive utilise-t-elle les TU restantes de la cible, vers une case voisine au même niveau, connue de son camp et payable ? (E17)

Ensuite seulement viendront les valeurs du §0.2.

## 8. Rapport de fin de lot : vérifications, limites et revue indépendante

**Résumé.**
- Les 13 points bloquants sont exposés, chacun avec une proposition arbitrable, une alternative, ses dépendances et ses effets sur les tests.
- Les décisions à prendre sont séparées des règles acquises (§0.3, §6.1) et posées sous forme de cinq questions, une par décision structurante, avec leurs sous-points (§7).
- Rien n'est décidé ; le registre n'est pas modifié ; `MEC-0001` reste « reportée ».

**Fichiers du lot.**
- `docs/mandates/BASTION-MANDAT-LOT-2G-v1.0.md` : copie octet pour octet du mandat.
- `docs/mandates/README.md` : une ligne d'index (SHA-256).
- `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md` : ce dossier.
- `docs/reviews/LOT-2G-IMPACTS-TESTS.md` : effet sur les tests du LOT-2F.

**Contrôles** (exécutés le 10 novembre 2026, après intégration de la revue ; fichiers indexés, avant le commit) :
- `git fetch origin main`, puis `git rev-parse HEAD origin/main` : `72908389…` pour les deux ; `git merge-base --is-ancestor origin/main HEAD` : code 0.
- Archive du mandat :
  - `cmp` avec `git show origin/orchestration/mandats:docs/mandates/BASTION-MANDAT-LOT-2G-v1.0.md` : code 0 ;
  - `sha256sum` : `735ca10d5c03f1f2939e8794fcb791f9b12ba46de9b61dadc0e22af824511b59`.
- `git diff --cached --check origin/main` : code 2. Seules les 6 lignes du mandat archivé qui finissent par des espaces sont signalées ; elles sont d'origine (6 lignes aussi dans le fichier publié) et doivent rester. Hors de l'archive : aucune sortie, code 0.
- Espaces en fin de ligne dans les deux rapports et l'index (`grep -nE ' +$'`) : aucune ligne, code 1.
- Fichiers protégés : `git diff --cached --quiet origin/main -- docs/gameplay docs/decisions docs/references CLAUDE.md .claude scripts .github src tests`, plus les livrables et le mandat du LOT-2F : code 0 (aucun changement).
- `git diff --cached --name-status origin/main` : 4 fichiers, ceux du mandat (§5) : l'archive, l'index, les deux rapports.
- Complétude : 13 sections, exactement E1, E2, E3, E5, E6, E7, E8, E9, E11, E12, E13, E17 et E24, sans doublon ; 13 lignes au §2.1 ; 9 rubriques par point ; 13 recommandations marquées PNV.
- Renvois : chaque test cité existe dans la matrice du LOT-2F, sauf les T-G, définis dans `LOT-2G-IMPACTS-TESTS.md` §5 ; chaque point (E) et chaque règle (M, J, P, K, D, I, H) cités existent dans la spécification du LOT-2F.
- Tableaux : nombre de colonnes cohérent (24 tableaux ici, 11 dans les impacts, 1 dans l'index) ; aucune barre verticale non échappée dans le code d'une cellule.
- Calculs : refaits par script Python (fractions exactes pour `B(n)`), puis indépendamment par le relecteur.
- Citations d'OXCE : relues dans le clone au commit `441cae1`.
- `bash scripts/harness/test-hooks.sh` : 75 tests, 0 échec, code 0.
- Aucun fichier sous `src/` : le contrôle de traçabilité de la simulation est sans objet.
- `dotnet` n'est pas installé dans l'environnement, et le lot ne touche ni au code ni aux tests : aucune commande .NET n'a été lancée.
- Aucun identifiant de modèle dans les fichiers du lot.

**Limites.**
- Les décisions du 9 novembre ne sont connues que par la synthèse du mandat LOT-2F (§3) et par le correctif P, sans comparaison avec la conversation (comme au LOT-2F).
- OXCE a été lu, pas exécuté. Les lectures du code faites aux lots précédents (LOT-2E, LOT-2F) ne sont pas toutes relues ; les nouvelles sont citées au §6.5.
- Les démonstrations valent sous leurs hypothèses écrites : départ au centre, mouvement le long d'un axe, sols sans épaisseur, volume en pavé.
- Les valeurs illustratives ne sont pas des valeurs de jeu.
- Aucun test .NET n'a été lancé : le lot ne touche ni au code ni aux tests.

**Revue indépendante** (agent distinct, en lecture seule, sur les fichiers indexés) :
- **Verdict** : 0 constat bloquant, 8 importants, 14 mineurs. Tous les chiffres recalculés sont justes et les citations d'OXCE exactes ; le diff contient les 4 fichiers attendus.
- **Importants, tous intégrés** :
  1. séparation plus stricte du dérivable, de l'interprétation et des conséquences des recommandations (§0.3, E3, E6) ;
  2. sens de l'effet du poids dans une collision attribué à la formule proposée, non à K08 ; ajout de l'alternative D de E6 (§0.4, C3) ;
  3. valeurs illustratives retirées des questions ; questions regroupées par décision structurante (§7) ;
  4. contact avec le volume de la cible défini, la cible étant exclue de la règle « unité sur l'arc », pour respecter E14 (E1 i, E8 a, E9 d, T-G14) ;
  5. blessure du sauteur à chaque atterrissage montrée au propriétaire (§0.4, E8, T-J15) ;
  6. tirage pour le terrain ajouté aux choix (E8 e, §0.2, T-D10) ;
  7. second arrondi, après le poids, rendu visible (DS3, E5, question 3 b) ;
  8. cas `n = 0` sur une unité ajouté aux choix ; C6 limité à `n ≥ 1` (E12 d, §0.4, §0.3).
- **Mineurs, tous intégrés** : hypothèse du départ au centre marquée ; diagonale et alternative A1 précisées ; définitions géométriques (contact, contacts simultanés, rattachement) ; citations d'OXCE précisées (`RNG.h:52-55`, tête en inférence, scripts et forçages) ; cas de l'unité touchée en vol et place finale ; dépendance au renouvellement des TU ; tolérance pour `P_obs` ; renvois croisés ; tableaux de dépendances harmonisés ; généralisation corrigée dans les impacts ; attendus complétés ; lots futurs signalés ; formulations clarifiées ; troisième type de provenance expliqué dans l'index.
- **Limites de la revue** : le relecteur n'a vérifié ni la conversation du propriétaire ni le texte d'autorisation ; OXCE a été lu, pas exécuté ; les lignes du LOT-2E n'ont pas été relues dans le code ; le relecteur est du même type d'agent que le développeur, et sa revue ne vaut pas validation.

**Publication.** Le lot a d'abord été commité sur la seule branche locale (`fefbbb5`), sans push ni PR, faute d'autorisation. Le propriétaire a ensuite autorisé la publication le 13 novembre 2026 (« Tu peux publier ») : la branche `docs/lot-2g-mec-0001-arbitrages` est poussée et une PR en brouillon est ouverte vers `main`. Aucune fusion n'est autorisée.
