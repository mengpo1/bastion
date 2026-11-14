# LOT-2G — Effet des propositions sur les tests du LOT-2F

Compagnon de `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. Les identifiants des tests (T-…) sont ceux de `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md`. Les règles (M, J, P, K, D, I) et les points ouverts (E) sont ceux du LOT-2F.

**Aucun test n'est écrit ni exécuté. Aucune décision n'est prise.** Ce document dit seulement quels scénarios deviendraient exacts **si** le propriétaire retenait les recommandations du dossier. La matrice du LOT-2F n'est pas modifiée : elle reste le point de départ vérifiable.

## 1. Conventions

- **Statut LOT-2F** : statut actuel, inchangé.
- **Spécifiable (R)** : deviendrait spécifiable si deux conditions sont réunies :
  - les recommandations des points cités sont retenues ;
  - les valeurs de conception sont déclarées : `λ`, `w`, `h_u`, plage de gravité, `β`, `β_s`, `c_s`, valeurs du type « impact » et facteur vers le terrain. Dans un test, elles peuvent être fictives, comme les coûts et les poids du LOT-2F. Leurs valeurs de jeu restent à fixer.
- **Inchangé** : le test dépend d'un point qui n'est pas parmi les 13 (registre, E20, E22, LOT-2B).
- Les attendus de la dernière colonne découlent des **recommandations non validées**. Ils changeraient si une alternative était choisie.

## 2. Tests déjà spécifiables à requalifier (constat C2)

La démonstration D-E1b du dossier montre que trois tests classés « spécifiables » au LOT-2F dépendent en fait du traitement du sol de départ (E1). Leur statut au LOT-2F n'est pas modifié ici ; il serait à requalifier lors d'une mise à jour autorisée de la matrice.

| Test | Configuration | Avec la recommandation E1 (f) : sol de départ ignoré | Avec A1 : départ au bord | Avec A4 : P07 à la lettre, départ au centre |
|---|---|---|---|---|
| T-J02 | 1 g ; une case `(1, 0)` ; un étage | Permis | Permis si `w ≤ 0,447 λ` | Permis seulement si `w ≤ 0,236 λ` |
| T-J03 | 1 g ; `(2, 0)`, `(1, 1)`, `(2, 1)` ; un étage | `(2, 0)` permis ; `(1, 1)` permis si les deux cases orthogonales voisines n'ont pas de sol au niveau de départ, ou si `w ≤ 0,236 λ` ; `(2, 1)` refusé | `(2, 0)` permis (`w ≤ 1,342 λ`, sans effet) ; `(1, 1)` : non calculé, le « bord avant » d'un saut en diagonale restant à définir | `(1, 1)` permis seulement si `w ≤ 0,236 λ` ; `(2, 0)` permis |
| T-J11 | Comme T-J02, ennemi visible sur la case | Sélection permise | Permise si `w ≤ 0,447 λ` | Permise seulement si `w ≤ 0,236 λ` |

## 3. Correspondance par test

Seuls figurent les tests partiels ou bloqués au LOT-2F, et ceux dont l'attendu se complète.

### 3.1 Marche (T-M)

| Test | Statut LOT-2F | Points requis | Autres dépendances | Statut si recommandations retenues |
|---|---|---|---|---|
| T-M01 | Partiel | — | registre : modèle de coûts | Inchangé |
| T-M03, T-M04 | Partiel | — | registre : géométrie des murs et passage bloqué pour N2 | Inchangé (E1 décrit les murs pour les sauts, pas la règle N2 de la marche) |
| T-M07 | Partiel | — | LOT-2B : paiement des pas faits | Inchangé |
| T-M10 | Partiel | — | registre : suite d'un déplacement à pied après révélation | Inchangé (E9 ne traite que les sauts et les chutes) |
| T-M11 | Partiel | — | E20 | Inchangé |

### 3.2 Saut : portée, élévation, obstacles (T-J01 à T-J10)

| Test | Statut LOT-2F | Points requis | Statut si recommandations retenues | Attendu sous les recommandations |
|---|---|---|---|---|
| T-J04 | Bloqué (E2, E5) | E2, E11 | Spécifiable (R) | (a) 0,5 g, un étage, distance 3 : permis (`3 ≤ 3,377`), sans plafond ou si `h_u ≤ 0,5`. (b) 2 g : refusé (`3 > 1,236`). (c) 1 g, deux étages : **refusé** (`3 > 2,472`). Aucun arrondi n'est nécessaire. |
| T-J05 | Partiel (E1, E11) | E1 (a), E11 | Spécifiable (R) | Élévation de `1/4`, `1/2` et `1/8` d'étage, quel que soit le poids. |
| T-J06 | Partiel (E1) | E1 | Spécifiable (R) | Avec une géométrie déclarée : action interdite avant engagement ; aucune TU dépensée. |
| T-J07 | Partiel (E1, E13) | E1, E13, E9 (c) | Spécifiable (R) | `C = C_dép + C_att` payé ; arrêt au premier contact ; obstacle révélé ; chute verticale dans la case de rattachement (E1 h). |
| T-J08 | Bloqué (E1) | E1 | Spécifiable (R) | (a) Permis. (b) Bloqué. Le contact est calculé exactement, axe par axe. |
| T-J09 | Bloqué (E1, E3) | E1, E3 | Spécifiable (R) | Bloqué s'il est connu, interrompu s'il ne l'est pas. Plafond touché à faible gravité si `h_u > 1 − 1/(4γ)`. |
| T-J10 | Partiel (dégâts : E8) | E8, E5, E1 (`λ`), E12 | Spécifiable (R) | Vitesse normale du LOT-2F §3.5. Plafond et mur : `P_obs = min(70, 3,2 × ṽ_n² × f_M)`, 0 au sommet contre un plafond. Sol en descente : chute au sol, base `B(n)`, sans `v_n` (E8 a). |

### 3.3 Saut : choix de la cible (T-J11 à T-J16)

| Test | Statut LOT-2F | Points requis | Statut si recommandations retenues | Attendu sous les recommandations |
|---|---|---|---|---|
| T-J12 | Partiel (E5 à E8) | E5, E6, E7, E8, E12 | Spécifiable (R) | Cible : `B(n)` plafonnée à 80, × 1,25, arrondie, tirage, `f_soi`, armure sans direction. Attaquant : `B(n)` plafonnée à 60, arrondie, tirage, `f_soi`, armure du dessous. Place finale : E9 (h). |
| T-J14 | Partiel (dégâts) | comme T-J12 | Spécifiable (R) | Comme T-J12, pour un allié puis un neutre caché. |
| T-J15 | Partiel (E13) | E13, E8, E12, E5, E7, E24 | Spécifiable (R) | `C = C_dép + C_att` payé en entier à l'engagement. L'atterrissage est une chute au sol (E8 a) : le sauteur subit `B(n)` plafonnée à 70, arrondie, tirée, puis `f_sol` et l'armure du dessous. |

### 3.4 Coût offensif (T-J17 à T-J19)

| Test | Statut LOT-2F | Points requis | Statut si recommandations retenues | Attendu sous les recommandations |
|---|---|---|---|---|
| T-J18 | Spécifiable pour `C_att` ; coût total partiel (E13) | E13 | Spécifiable (R), coût total compris | `C` payé dans les trois cas, jamais remboursé. |
| T-J19 | Spécifiable ; seuil complet (E13) | E13 | Spécifiable (R), seuil complet | Attaque impossible si les TU restantes sont inférieures à `C`. |

### 3.5 Esquive (T-K)

| Test | Statut LOT-2F | Points requis | Statut si recommandations retenues | Attendu sous les recommandations |
|---|---|---|---|---|
| T-K01 | Partiel (E17) | E17 | Spécifiable (R) | (a) Aucune esquive. (b) Aucune case candidate payable : aucune esquive. (c) Aucune case candidate : aucune esquive. Collision dans les trois cas. |
| T-K02 | Partiel (E12) | E12 | Spécifiable (R) | 5 %, 60 % et 100 %, avec `n = z_dép − z_arr` et un test entier sur [0, 99]. |
| T-K03 | Partiel (E17 ; E12 ; E5, E7, E24) | E5, E7, E12, E17, E24 | Spécifiable (R) | Cible déplacée sur une case candidate, pas payé. Attaquant : `B(n)` plafonnée à 70, arrondie, tirage, `f_sol`, armure du dessous. |
| T-K04 | Partiel (E6 à E8) | E5, E6, E7, E8 | Spécifiable (R) | Cible immobile, aucune dépense. Deux tirages indépendants ; dégâts pour les deux. Place finale : E9 (h). |
| T-K05 | Spécifiable (loi : E22) | — | Inchangé | La loi du tirage reste E22, hors des 13. |
| T-K06 | Partiel (tirage ; E12) | E12 | Partiel | (a) Spécifiable : esquive à chaque fois. (b) Suppose des Réactions ≤ `−5n` : le modèle des caractéristiques n'est pas décidé (hors des 13). |

### 3.6 Dégâts (T-D)

| Test | Statut LOT-2F | Points requis | Statut si recommandations retenues | Attendu sous les recommandations |
|---|---|---|---|---|
| T-D01 | Partiel (E5 ; E7 ; E24) | E5, E7, E12, E24 | Spécifiable (R) | `P = 8` ; tirage dans [4, 12] ; `f_sol(M)` ; armure du dessous ; conversion. |
| T-D02 | Spécifiable ; arrondi bloqué (E5) | E5 | Spécifiable (R), arrondi compris | Après arrondi : 14, 22 et 33 (même résultat à l'inférieur pour ces trois valeurs). |
| T-D03 | Partiel (E8) | E8 | Spécifiable (R) | Valeurs du LOT-2F pour le sol et, base `B(n)` confirmée, pour les deux unités d'une collision. Colonne obstacle : sans objet, la base d'un obstacle est `P_obs`, pas `B(n)`. |
| T-D04 | Partiel (E5) | E5 | Spécifiable (R) | [4, 12] et [50, 150], tirage entier uniforme. |
| T-D05 | Partiel (E8 ; E5) | E8, E5 | Spécifiable (R) | Cible 100, attaquant 60, avant tirage ; ce sont déjà des entiers. |
| T-D06 | Partiel | E5, E8 | Spécifiable (R) | Bonus × 1,25 appliqué à l'allié, base `B(n)`. |
| T-D07 | Partiel | E5, E8 | Spécifiable (R) | Aucun bonus ; base `B(n)`. |
| T-D09 | Spécifiable (facteur) ; dégâts bloqués (E8) | E8 | Spécifiable (R), dégâts compris | `P_obs = min(70, 3,2 × ṽ_n² × f_M)`, pour une vitesse déclarée. |
| T-D10 | Partiel (E8) | E8 | Spécifiable (R) | Dégât au terrain : tirage selon la méthode choisie (tirage propre sur `[⌊P/2⌋, ⌊3P/2⌋]`, ou reprise du tirage de l'unité), puis facteur vers le terrain, puis comparaison avec l'armure `A` (seuil d'OXCE, sans accumulation). |
| T-D12 | Partiel (E8, E9) | E1, E8, E9, E12 | Spécifiable (R) | Arrêt ; chute dans la case de rattachement ; `n` selon E12 ; atterrissage sur l'unité : collision accidentelle, sans bonus. |
| T-D13 | Bloqué (E7) | E7, E5 | Spécifiable (R) | Avec des valeurs fictives d'armure et de conversion : résultat exact. |
| T-D14 | Bloqué (E6) | E6, E5, E8 | Spécifiable (R) | Tirages indépendants. Avec `β < 2/7` et des armures égales ou absentes, les deux ordres de blessures apparaissent sur un grand nombre d'essais. |

### 3.7 Cas non arbitrés (T-X)

| Test | Statut LOT-2F | Points requis | Statut si recommandations retenues | Attendu sous les recommandations |
|---|---|---|---|---|
| T-X01 | Bloqué (E9) | E9 (a), (e) | Spécifiable (R), comme test d'impossibilité | Le cas ne peut pas se produire : pendant le vol, aucune unité autre que la cible ne bouge. |
| T-X02 | Bloqué (E9) | E9 (c), (d) ; E1 | Spécifiable (R) | Unités connues : saut interdit. Inconnues : arrêt au premier contact ; unité révélée. |
| T-X03 | Bloqué (E9) | E9 (f) ; E12 | Spécifiable (R) | Chute verticale jusqu'au premier support ; `n` compté depuis le niveau de départ. |
| T-X04 | Bloqué (E9) | E9 (i) | Spécifiable (R) | Refus : les grandes unités sont exclues. |
| T-X05 | Bloqué (E3) | E3 | Spécifiable (R) | Action indisponible hors de la plage de gravité, et toujours à `g = 0` ; aucune TU dépensée. |

## 4. Correspondance par point

| Point | Tests concernés (§3) | Scénarios complémentaires (§5) |
|---|---|---|
| E1 | T-J02, T-J03, T-J05 à T-J10, T-J11, T-D12, T-X02 | T-G01, T-G14 |
| E2 | T-J03, T-J04 | T-G02, T-G03 |
| E3 | T-J09, T-X05 | T-G03, T-G04 |
| E5 | T-J10, T-J12, T-J14, T-J15, T-K03, T-K04, T-D01 à T-D07, T-D13, T-D14 | T-G07 |
| E6 | T-J12, T-J14, T-K04, T-D14 | T-G08 |
| E7 | T-J12, T-J14, T-J15, T-K03, T-K04, T-D01, T-D13 | — |
| E8 | T-J10, T-J12, T-J14, T-J15, T-K04, T-D03, T-D05 à T-D07, T-D09, T-D10, T-D12, T-D14 | T-G09 |
| E9 | T-J07, T-J12, T-K04, T-X01 à T-X04, T-D12 | T-G12, T-G14 |
| E11 | T-J04, T-J05 | T-G05 |
| E12 | T-J10, T-J12, T-J14, T-J15, T-K02, T-K03, T-K06, T-D01, T-D12, T-X03 | T-G06 |
| E13 | T-J07, T-J15, T-J18, T-J19 | T-G10 |
| E17 | T-K01, T-K03 | T-G11 |
| E24 | T-J15, T-K03, T-D01 | T-G13 |

## 5. Scénarios complémentaires suggérés

Ces scénarios ne figurent pas dans la matrice du LOT-2F. Ils ne seraient ajoutés que si les recommandations correspondantes étaient retenues. Toutes les valeurs sont fictives. Sauf mention contraire : aucun obstacle, aucun plafond sur l'arc, armures égales ou absentes.

| ID | Point | Préconditions | Résultat attendu sous la recommandation |
|---|---|---|---|
| T-G01 | E1 | `λ = 1`, `w = 0,3`, 1 g, saut d'une case `(1, 0)`, un étage | Permis si le sol de départ est ignoré (f) ; refusé si P07 s'applique à la lettre (`0,3 > 0,236`) |
| T-G02 | E2 | `γ = 0,5`, `δ = 2`, case à distance 4, sans plafond | Permis : `R = 4` exactement, malgré les erreurs de calcul approché |
| T-G03 | E2, E3 | `γ = 3`, `δ = 1` | Aucune case atteignable (`R = 0,949`) |
| T-G04 | E3 | `γ = 0` | Saut offensif indisponible ; aucune TU dépensée |
| T-G05 | E11 | Unités de 40 et de 160 kg, 1 g, un étage | Même élévation (`1/4` d'étage), même portée (2) |
| T-G06 | E12 | Mur inconnu touché à mi-descente, `z_s = 0,5` au-dessus du niveau 0 | `n = 0` : aucun dégât de chute ; le choc contre le mur est traité seul |
| T-G07 | E5 | Cible percutée par un saut offensif, `n = 2` | `17,5` arrondi à 18 ; tirage dans [9, 27] |
| T-G08 | E6 | Même collision répétée, poids différents, `β < 2/7` | Les deux ordres de blessures apparaissent |
| T-G09 | E8 | Contact avec un plafond exactement au sommet | `v_n = 0`, donc `P_obs = 0` |
| T-G10 | E13 | Même case visée, avec ou sans unité ou obstacle caché | Même coût `C` affiché |
| T-G11 | E17 | Cible avec 3 TU ; voisines de coût 2 (droite), 3 (diagonale `⌊1,5 × 2⌋`) et 4 (droite) | Candidates : les deux premières |
| T-G12 | E9 | Collision non esquivée, cible debout ; une seule voisine libre avec un sol | L'attaquant y est placé, sans dépense de TU ; s'il n'y en a aucune : cas à arbitrer |
| T-G13 | E24 | Même tirage forcé, `M = 40`, puis `M = 320` kg | Dégâts plus élevés à 320 kg, avant armure |
| T-G14 | E1, E9 | 1 g, une case, un étage, `λ = 1`, `w = 0,3` ; ennemi visible sur la case visée, de hauteur `h_u = 0,9`, puis `0,6` | Saut permis (E14). Premier contact sur le côté de la cible (0,9), puis par le dessus (0,6) ; collision dans les deux cas, avec `n = 1` |

## 6. Récapitulatif

Décompte des 60 tests du LOT-2F, avant et après retenue de **toutes** les recommandations :

| Famille | LOT-2F (spéc. / part. / bloq.) | Si recommandations retenues |
|---|---|---|
| Marche (T-M) | 5 / 6 / 0 | 5 / 6 / 0 |
| Saut : portée, élévation, obstacles | 3 / 4 / 3 | 10 / 0 / 0 |
| Saut : cible | 3 / 3 / 0 | 6 / 0 / 0 |
| Coût offensif | 3 / 0 / 0 | 3 / 0 / 0 |
| Esquive (T-K) | 1 / 5 / 0 | 5 / 1 / 0 |
| Dégâts (T-D) | 4 / 8 / 2 | 14 / 0 / 0 |
| Information (T-I) | 5 / 0 / 0 | 5 / 0 / 0 |
| Non arbitrés (T-X) | 0 / 0 / 5 | 5 / 0 / 0 |
| **Total** | **24 / 26 / 10** | **53 / 7 / 0** |

- 29 tests deviendraient spécifiables : 19 partiels et 10 bloqués.
- Les 7 tests qui restent partiels dépendent de points hors des 13 : le registre (T-M01, T-M03, T-M04, T-M10), le LOT-2B (T-M07), E20 (T-M11) et le modèle des caractéristiques (T-K06 b).
- Trois tests (T-J02, T-J03, T-J11) sont comptés spécifiables au LOT-2F, mais leur attendu dépend de E1 (constat C2, statut à requalifier). Sous la recommandation E1 (f), leur attendu est confirmé, avec la réserve de la diagonale (§2) ; sous les alternatives A1 et A4, il dépend de `w`.
- Si le propriétaire choisit une alternative, la plupart des statuts deviennent aussi spécifiables ; seuls les attendus changent. Exceptions : A1 en diagonale (non calculé), E3 C (renvoi à un autre mandat), E9 A (règles de priorité à écrire), E12 C (interpolation non validée).

## 7. Limites

- Les attendus sont **conditionnels** : aucun n'est validé.
- Aucun test n'a été écrit ni exécuté ; OXCE n'a pas été exécuté.
- Les valeurs illustratives du dossier (`β = 0,25`, `c_s = 4`, etc.) ne sont pas des valeurs de jeu.
