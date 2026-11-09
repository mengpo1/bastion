# LOT-2F — Matrice de tests futurs de `MEC-0001`

Compagnon de `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` : les identifiants de règles (M, J, P, K, D, I) et de points ouverts (E) y sont définis.

**Aucun test n'est écrit ni exécuté.** Ce document décrit des scénarios ; il n'autorise aucune implémentation.

**Conventions.**
- Les coûts, poids, armures et caractéristiques notés « fictif » sont des **valeurs d'essai**, pas des valeurs du jeu. Ils ne viennent ni d'OXCE ni de X-COM.
- **Exécutabilité** :
  - **Spécifiable** : l'attendu découle entièrement de règles validées et de données fictives déclarées ;
  - **Partiel (E…)** : une partie de l'attendu est déterminée, l'autre dépend d'un point ouvert ;
  - **Bloqué (E…)** : l'attendu exact dépend d'un point ouvert. Aucune valeur n'est inventée.
- Positions `(x, y, z)` ; `z` = niveau. Tests de marche (T-M) : carte plane d'un seul niveau. Tests de saut et de chute : plusieurs niveaux, comme indiqué dans chaque test.

## 1. Marche et verticalité (registre)

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-M01 | Unité U en (2, 2, 0) avec 10 TU. Les 8 cases voisines sont franchissables, sans mur, avec un coût fictif de 2. | Un pas vers chacune des 8 voisines (8 essais) | Le pas est possible dans les 8 directions. Pas droit : 2 TU. | M01 ; pas droit = coût de la case d'arrivée : implicite, S2 ne visant que la diagonale | Partiel (registre : modèle de coût encore ouvert) |
| T-M02 | Pas en diagonale vers une case de coût fictif 1, 2, 3 ou 4 | Pas nord-est | 1, 3, 4 et 6 TU (`⌊1,5 × c⌋`) | M02 | Spécifiable |
| T-M03 | Pas nord-est. Mur entre (2, 2) et (2, 1) : passage par le nord fermé ; passage par l'est ouvert. | Pas nord-est | Permis | M03, M05 (N2) | Partiel (registre : géométrie des murs et définition d'un passage bloqué) |
| T-M04 | Pas nord-est, les deux passages fermés par des murs | Pas nord-est | Refusé | M03 | Partiel (idem) |
| T-M05 | Une unité sur chacune des deux cases orthogonales du coin ; aucun mur | Pas nord-est | Permis : une unité voisine n'est pas un obstacle | M04 | Spécifiable |
| T-M06 | U a 5 TU ; le trajet le moins cher vers la case C coûte 6 (fictif) | Sélection de C | C est hors de la zone atteignable : sélection refusée, donc aucune TU dépensée | M08 (Z1) ; absence de dépense dérivée de Z1 (P14 du LOT-2B non arbitré) | Spécifiable |
| T-M07 | Obstacle inconnu sur le trajet planifié | Exécution | Interruption à la rencontre ; l'obstacle est révélé et mémorisé | M11, M12 | Partiel (paiement des pas faits : proposition du LOT-2B non arbitrée) |
| T-M08 | Case jamais explorée | (a) Sélection comme destination. (b) Trajet qui passerait par elle. | (a) Refusée. (b) Aucun trajet de ce type proposé. | M09, M10 | Spécifiable |
| T-M09 | Unité connue sur une case | Choisir cette case comme destination, ou la traverser | Refusé | M13 | Spécifiable |
| T-M10 | Unité cachée sur le trajet | Exécution | L'unité est révélée | M14 | Partiel (suite du déplacement : E9 ; registre : cas d'une occupation inconnue) |
| T-M11 | Force fictive 30, poids porté fictif 40, TU récupérables fictives 60 | Début de tour | TU récupérées réduites selon le rapport Force / poids. Repère OXCE : `⌊0,75 × 60⌋ = 45`. Ni immobilisation ni surcoût par pas. | M16 (N14) | Partiel (transposition exacte ouverte ; E20) |

## 2. Saut : portée, élévation, obstacles

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-J01 | U au niveau 1 ; case visée au niveau 1 | Saut offensif | Refusé (aucun dénivelé vers le bas) | J01 | Spécifiable |
| T-J02 | g = 1 g ; U en (2, 2, 1) ; case visée en (3, 2, 0) : Manhattan 1, dénivelé d'exactement un étage `H`. Aucun obstacle ; aucun contact avec un plafond. | Saut | Permis | P05, J02 | Spécifiable |
| T-J03 | g = 1 g ; dénivelé d'exactement un étage `H` ; aucun obstacle ni contact avec un plafond ; cases visées à (Δx, Δy) = (2, 0), (1, 1) et (2, 1) | Saut | (2, 0) et (1, 1) permis (Manhattan 2). (2, 1) refusé (Manhattan 3). | P05 | Spécifiable |
| T-J04 | Cases visées à Manhattan 3 : (a) 0,5 g, un étage ; (b) 2 g, un étage ; (c) 1 g, deux étages | Saut | Sens dérivé du modèle balistique (P02 à P04), non écrit au mandat : portée plus grande en (a) et (c), plus petite en (b). Acceptation exacte non déterminée. | P06 | Bloqué (E2, E5) |
| T-J05 | Saut à 1 g, 0,5 g, puis 2 g | Mesure du sommet | Élévation au-dessus du départ : `H/4`, `H/2`, `H/8` | P02, P04 (dérivé, spécification §3.2) | Partiel (E1 pour une valeur métrique ; E11) |
| T-J06 | Obstacle **connu** qui coupe l'arc | Sélection | Action interdite avant engagement ; aucune TU dépensée | P08 | Partiel (E1 : géométrie) |
| T-J07 | Obstacle **non détecté** qui coupe l'arc ; vide sous le point de contact | Engagement | Coût offensif dépensé ; arrêt au premier contact ; obstacle révélé ; chute verticale depuis le contact | P08, D13, J09 | Partiel (E1, E13) |
| T-J08 | Obstacle bas : (a) son sommet reste sous le bas du volume pendant tout le survol ; (b) il coupe le volume | Saut | (a) Permis. (b) Bloqué. | P07 | Bloqué (E1 : dimensions) |
| T-J09 | Mur ou plafond coupant le volume, dont un plafond atteint à faible gravité | Saut | Bloqué s'il est connu ; interrompu s'il est inconnu | P07 ; spécification §3.4 | Bloqué (E1, E3) |
| T-J10 | Contacts : plafond en montée, plafond au sommet, sol en descente, mur | Impact | Vitesse normale conforme à la spécification §3.5 (nulle au sommet contre un plafond ; constante contre un mur) ; aucun coefficient de phase | D11 | Partiel (vitesse : spécifiable ; dégâts : E8) |

## 3. Saut : choix de la cible

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-J11 | Ennemi **visible** sur la case visée | Saut offensif | À confirmer : exception à S10 | J13 | Bloqué (E14) |
| T-J12 | Ennemi caché sur une case explorée, non visible ; l'ennemi ne voit pas actuellement l'attaquant (pas d'esquive possible, K03) | Saut à l'aveugle | Collision ; ennemi révélé ; bonus × 1,25 sur la cible | J03, J05, J11 | Partiel (dégâts : E5 à E8) |
| T-J13 | Allié ou neutre **identifié** sur la case | Sélection | Refusée | J06 | Spécifiable |
| T-J14 | Allié caché, puis neutre caché, sur une case visée à l'aveugle | Saut | Collision possible ; bonus × 1,25 appliqué à l'unité percutée | J07, J08 | Partiel (dégâts) |
| T-J15 | Case explorée, vide, non visible | Saut à l'aveugle | Permis ; atterrissage ; coût offensif payé | J03, J09 | Partiel (coût total : E13) |
| T-J16 | Case jamais explorée | Sélection | Refusée | J04 | Spécifiable |

## 4. Coût offensif

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-J17 | `TU_max` ∈ {1, 4, 5, 9, 10, 54, 80} (fictif) | Calcul de `C_att` | 1, 1, 1, 1, 2, 10, 16 | J09 | Spécifiable |
| T-J18 | (a) La cible esquive. (b) La case est vide. (c) L'attaque est interrompue par un obstacle. | Engagement | `C_att` est dépensé dans les trois cas | J09 | Spécifiable pour `C_att` ; coût total : Partiel (E13) |
| T-J19 | `TU_max` 54 (`C_att` = 10) ; 9 TU restantes | Sélection | Attaque impossible | J10 | Spécifiable (seuil complet avec `C_dép` : E13) |

## 5. Esquive

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-K01 | (a) La cible ne voit pas actuellement l'unité qui tombe. (b) Elle la voit, mais ses TU sont inférieures au coût du pas. (c) Aucune case voisine n'est libre et accessible. | Chute sur la cible | Pas d'esquive ; collision | K03 | Partiel (E17) |
| T-K02 | Réactions et étages fictifs : (R = 0, n = 1) ; (R = 50, n = 2) ; (R = 97, n = 1) | Calcul de p | 5 % ; 60 % ; 100 % (borné). Le cas 0 % est inatteignable si R ≥ 0. | K05 | Partiel (formulation provisoire : E12) |
| T-K03 | Esquive possible, tirage forcé à la réussite | Chute | Cible déplacée sur une case valide ; TU du pas dépensées ; aucun dégât pour la cible ; l'attaquant finit par une chute au sol | K06 | Partiel (E17, E18) |
| T-K04 | Esquive possible, tirage forcé à l'échec | Chute | Cible immobile ; aucune TU dépensée pour l'essai ; collision, avec des dégâts possibles pour les deux (K02) | K07, K02 | Partiel (dégâts : E6 à E8) |
| T-K05 | Plusieurs cases d'esquive valides | Esquive réussie | La case choisie appartient à l'ensemble des cases valides | K04 | Spécifiable (loi du tirage : E22) |
| T-K06 | Conditions d'esquive remplies (K03) ; (a) p = 100 % ; (b) p = 0 %, atteignable seulement avec des Réactions négatives | Nombreuses chutes | (a) Esquive à chaque fois. (b) Jamais d'esquive. | K05 | Partiel (tirage non décidé ; E12) |

## 6. Dégâts

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-D01 | Chute au sol d'un étage | Atterrissage | Base 8. Avec la règle entière d'OXCE, tirage dans [4, 12]. | D01, D03, D06 | Partiel (E5 ; conversion : E7 ; poids, armure et caractéristiques : E24) |
| T-D02 | n = 2, 3 et 4 | Calcul de `B(n)` | 14 ; 22,1 ; 33,035 (avant arrondi). Incréments : 6 ; 8,1 ; 10,935. | D03, D04 | Spécifiable (valeurs réelles) ; arrondi : Bloqué (E5) |
| T-D03 | n = 6, 7 et 8, pour chacun des quatre cas | Plafond | Chute au sol : 67,7262875 ; 70 ; 70. Unité qui tombe, si sa base est `B(n)` : 60 ; 60 ; 60. Unité percutée, si sa base est `B(n)` : 67,7262875 ; 80 ; 80. Obstacle : non déterminé. | D05 | Partiel (E8) |
| T-D04 | Puissance entière fictive soumise au tirage : 8, puis 100 | Tirage | Bornes [4, 12] et [50, 150] ; loi uniforme si la règle d'OXCE est reprise | D06 | Partiel (E5) |
| T-D05 | Saut offensif, cible percutée, n = 7 ; base des collisions supposée égale à `B(n)` | Dégâts avant tirage | Cible : `min(B(7), 80) × 1,25` = 100. Attaquant : `min(B(7), 60)` = 60, sans bonus. | J11, J12, D08 | Partiel (base des collisions : E8 ; E5) |
| T-D06 | Allié caché percuté à l'aveugle | Dégâts | Bonus × 1,25 appliqué à l'allié | J08 | Partiel |
| T-D07 | Chute accidentelle sur une unité | Dégâts | Aucun bonus | D08 | Partiel |
| T-D08 | Même chute sur deux sols de natures différentes | Dégâts avant tirage | Identiques | D02 | Spécifiable |
| T-D09 | M = 40, 80, 160, 240, 320 kg (fictif) | Facteur `f_M` | 0,5 ; 1 ; 2 ; 3 ; 3 | D10 | Spécifiable (facteur) ; dégâts : Bloqué (E8) |
| T-D10 | Obstacle destructible d'armure fictive A ; dégât au terrain ≥ A, puis < A | Impact | Détruit, puis intact (seuil d'OXCE, sans accumulation) | D12 | Partiel (puissance d'impact : E8) |
| T-D11 | Obstacle marqué indestructible | Impact | Intact | D12 | Spécifiable |
| T-D12 | Saut ; obstacle inconnu détruit à l'impact ; vide en dessous ; unité au sol plus bas | Enchaînement | Arrêt à l'impact, même si l'obstacle est détruit ; chute verticale depuis le contact ; dégâts d'impact puis de chute, résolus séparément ; atterrissage sur l'unité : collision | D13, I03 | Partiel (E8, E9) |
| T-D13 | Unité en armure fictive touchée | Conversion | Armure puis santé et étourdissement, selon le type de dégâts | D07, D09 | Bloqué (E7) |
| T-D14 | Collision entre deux unités de poids différents | Dégâts | Le poids influe sur les deux, sans désigner mécaniquement la plus blessée | K08 | Bloqué (E6) |

## 7. Information : tests de non-fuite

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-I01 | Ennemi caché sur la case visée | Prévisualisation | Aucune différence avec une case vide : même destination, même trajectoire, même coût | I01, I02 | Spécifiable |
| T-I02 | Obstacle inconnu sur l'arc | Prévisualisation | Trajectoire affichée comme libre, sans aucun indice | I01 | Spécifiable |
| T-I03 | Élément caché sur la carte | Calcul de la zone atteignable | La zone ne dépend que des informations connues | M08, I01 | Spécifiable |
| T-I04 | Case explorée, non visible | Visée à l'aveugle | Aucune information sur l'occupation avant l'impact | I01, J03 | Spécifiable |
| T-I05 | Obstacle révélé par un impact | Après l'impact | L'obstacle est connu et mémorisé | M12 | Spécifiable |

## 8. Cas non arbitrés

Pour ces cas, aucun résultat n'est inventé (mandat §3.6).

| ID | Préconditions | Déclencheur | Résultat attendu | Provenance | Exécutabilité |
|---|---|---|---|---|---|
| T-X01 | Case visée vide à l'engagement ; une unité l'occupe pendant le vol | Atterrissage | Non arbitré | I04 | Bloqué (E9) |
| T-X02 | Deux unités sur l'arc du saut | Saut | Non arbitré | I04 | Bloqué (E9) |
| T-X03 | Case d'arrivée sans support, hors du cas de D13 | Atterrissage | Non arbitré | I04 | Bloqué (E9) |
| T-X04 | Unité de grande taille, qui saute ou qui est percutée | Saut ou chute | Non arbitré | E9 (grandes unités hors périmètre, LOT-2E) | Bloqué (E9) |
| T-X05 | g = 0, ou gravité hors de la plage prévue | Saut | Non arbitré | P01 | Bloqué (E3) |

## 9. Récapitulatif

| Famille | Tests | Spécifiables | Partiels | Bloqués |
|---|---|---|---|---|
| Marche (T-M) | 11 | 5 | 6 | 0 |
| Saut : portée, élévation, obstacles (T-J01 à T-J10) | 10 | 3 | 4 | 3 |
| Saut : cible (T-J11 à T-J16) | 6 | 2 | 3 | 1 |
| Coût offensif (T-J17 à T-J19) | 3 | 3 | 0 | 0 |
| Esquive (T-K) | 6 | 1 | 5 | 0 |
| Dégâts (T-D) | 14 | 4 | 8 | 2 |
| Information (T-I) | 5 | 5 | 0 | 0 |
| Non arbitrés (T-X) | 5 | 0 | 0 | 5 |
| **Total** | **60** | **23** | **26** | **11** |

T-J18, T-J19, T-D02 et T-D09 sont comptés comme spécifiables pour la partie déterminée ; le reste de leur attendu dépend des points ouverts indiqués.

## 10. Vérifications et revue

Voir la spécification, §6.
