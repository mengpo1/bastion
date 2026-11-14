# LOT-2H — Traçabilité des principes DS1 à DS5 et écarts

Compagnon de `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md`. **Aucune décision nouvelle** : ce document rattache chaque principe de la consolidation du 13 novembre 2026 à sa source, aux règles antérieures et au texte proposé. Le registre n'est pas modifié.

**Sources.**
- **C** : consolidation `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`, SHA-256 `dee88998…f335f`. « §2 » à « §6 » désignent ses sections DS1 à DS5. Son texte fait foi.
- **R** : registre `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` (S1 à S12, Z1, N1 à N14).
- **F** : spécification et matrice du LOT-2F, sur `main`. Les règles P, J, K, D et I y sont des décisions du 9 novembre 2026 (sauf D07 et I04, encore ouvertes) ; J13 et les points E14, E18 et E23 viennent du correctif du propriétaire ; les autres points E restent ouverts ; les H sont des décisions historiques ; les M transcrivent le registre. Aucune de ces règles n'est **inscrite au registre**, hormis ce que les M reprennent de lui.
- **G** : dossier du LOT-2G, branche `docs/lot-2g-mec-0001-arbitrages` (PR n° 10, non fusionnée, tête `2a14a50`). Ses recommandations ne valent que reprises par C.

**Statuts** (mandat LOT-2H §3 A) : **accepté en conversation** ; **à définir** ; **conflit/écart** (dont « à vérifier »).

## 1. Matrice de traçabilité

« Statut au registre » décrit l'état actuel sur `main`. « Texte proposé » renvoie à la proposition, §2 (identifiant DS) ou §3 (autres lignes de la fiche).

### 1.1 DS1 — Géométrie

| ID | Élément source (C §2) | Règles antérieures touchées | Statut au registre | Texte proposé | Statut |
|---|---|---|---|---|---|
| DS1.1 | item 1 : « proportions entre largeur de case, hauteur d'étage et taille des unités, sans imposer d'échelle physique en mètres » | E1 (F) | absent : point ouvert du LOT-2F | DS1.1 | accepté en conversation |
| DS1.2 | item 2 : « volumes 3D de forme rectangulaire (pavés) » ; collisions sur le volume | P07, E1 (F) | absent : P07 non inscrite | DS1.2 | accepté en conversation |
| DS1.3 | item 3 : « Le sol de la case de départ est ignoré pendant le saut de l'unité qui quitte cette case » | P07 (F) ; constat C1 de G | absent | DS1.3, avec l'exception annotée | accepté en conversation ; conflit/écart avec la lettre de P07 (contrôle B1) |
| DS1.4 | item 4 : la cible effective reste une cible de collision, « notamment les ennemis actuellement visibles » | E14, J13, M13 (F) ; S10 (R) | S10 inscrite ; E14 et J13 non inscrites | DS1.4 | accepté en conversation |
| DS1-AD | « À DÉFINIR » : rapport case/étage, dimensions, surfaces, contacts, précision, fin de chute | E1 (F) | — | « Encore ouvert », géométrie | à définir |
| DS1-EC | « ÉCART À TRAITER » : exception au traitement littéral du sol de départ, sans extension | P07 (F) | — | annotation de DS1.3 | conflit/écart |

### 1.2 DS2 — Sauts, charge et gravité

| ID | Élément source (C §3) | Règles antérieures touchées | Statut au registre | Texte proposé | Statut |
|---|---|---|---|---|---|
| DS2.1 | item 1 : « Une unité plus lourde saute moins haut ET moins loin » ; vitesse égale pour toutes les masses rejetée | P02, P04, P05, E11 (F) ; E11 de G ; N11, N14 (R) | N11 et N14 inscrites ; P non inscrites | DS2.1 | accepté en conversation ; conflit/écart avec la recommandation E11 de G (contrôle B2) |
| DS2.2 | item 2 : portée selon Manhattan ; « une diagonale (1,1) compte pour deux cases » | P05, H02, E2 (F) | absent | DS2.2 | accepté en conversation |
| DS2.3 | item 3 : références à 1 g « rattachées à une masse de référence » | P04, P05 (F) | absent | DS2.3 | accepté en conversation ; masse de référence à définir |
| DS2.4 | item 4 : plage de gravité ; indisponible en apesanteur et hors plage | P01, E3 (F) | absent | DS2.4 | accepté en conversation ; bornes à définir |
| DS2-AD | « À DÉFINIR » : masse de référence, loi de pénalisation, masses en jeu, limites de gravité, portée numérique ; loi de propulsion « n'est pas validé[e] » | E2, E3, E11 (F) | — | « Encore ouvert », sauts | à définir |
| DS2-EC | « ÉCART À TRAITER » : recalculer les formules et tests E2/E11 de G | G : E1, E2, E3, E8, E11, D-E1b ; tests listés au §4 | — | aucun texte au registre (§4 ci-dessous) | conflit/écart |

### 1.3 DS3 — Chutes et arrondis

| ID | Élément source (C §4) | Règles antérieures touchées | Statut au registre | Texte proposé | Statut |
|---|---|---|---|---|---|
| DS3.1 | item 1 : chute d'un seul étage, pas de dégâts pour l'unité qui tombe « si elle n'est pas ralentie par son poids » | D01, D03, E18, E24 (F) ; N7 (R) | N7 inscrite [À vérifier] ; D et E18 non inscrites | DS3.1 ; annotation de N7 | accepté en conversation ; conflit/écart avec D03 et avec le statut de N7 (contrôle B3) |
| DS3.2 | item 2 : même seuil de surcharge que pour les TU (N14), sans seuil autonome | N14 (R) ; E20, E23 (F) | N14 inscrite | DS3.2 ; « Encore ouvert », surcharge | accepté en conversation ; seuil binaire à définir |
| DS3.3 | item 3 : plusieurs étages, exemption non applicable ; « les dégâts précis demeurent à calculer » | D03, D04 (F) ; N7 (R) | N7 inscrite [À vérifier] ; D non inscrites | DS3.3 ; annotation de N7 | accepté en conversation |
| DS3.4 | item 4 : l'unité percutée « peut subir des dégâts dès une chute d'un étage » | D01, K02 (F) ; N7 (R) | N7 inscrite [À vérifier] ; D et K non inscrites | DS3.4 ; annotation de N7 | accepté en conversation |
| DS3.5 | item 5 : arrondi au plus proche, moitié vers le haut, avant le tirage puis après le facteur de poids | D04, D06, E5 (F) | absent | DS3.5 | accepté en conversation |
| DS3-AD | « À DÉFINIR » : seuil binaire, charge portée et poids total, dégâts en surcharge ou au-delà, moins d'un étage sur une unité, comptage des étages, facteurs de poids | E12, E20, E24 (F) | — | « Encore ouvert », chutes | à définir |
| DS3-EC | « ÉCART À TRAITER » : portée de D03 à aménager ; E18 pertinente sous réserve de l'exemption ; chute sur une unité non assimilée à une chute au sol | D03, E18 (F) | — | annotations de DS3.1 et DS3.4 | conflit/écart |

### 1.4 DS4 — Collisions, masses et type « impact »

| ID | Élément source (C §5) | Règles antérieures touchées | Statut au registre | Texte proposé | Statut |
|---|---|---|---|---|---|
| DS4.1 | item 1 : la masse « tend à protéger la plus lourde et à aggraver les blessures de la plus légère » ; armure et tirages interviennent | K02, K08, E6 (F) ; N9, N10 (R) | N9 et N10 inscrites ; K non inscrites | DS4.1 | accepté en conversation ; formule à définir ; conflit/écart avec la formule E6 de G (contrôle B5) |
| DS4.2 | item 2 : puissance « proportionnelle au carré de la composante normale de la vitesse » ; ×4 si la vitesse double | D10, D11, E8 (F) | absent | DS4.2 | accepté en conversation ; constante à définir |
| DS4.3 | item 3 : poids total E23 ; plafond de 70 pour les obstacles conservé | E23, D05, D10 (F) | absent | DS4.3 | accepté en conversation |
| DS4.4 | item 4 : type « impact » propre à Bastion, traitement inspiré d'OXCE, sans copie | D07, E7 (F) ; décision D4 (`docs/references/OXCE-BASELINE.md`) | absent | DS4.4 | accepté en conversation ; champ d'application et paramètres à définir |
| DS4.5 | item 5 : « même tirage aléatoire d'intensité du choc » pour l'unité et l'obstacle | D12 (F) ; E8 (e) de G | absent | DS4.5 | accepté en conversation |
| DS4-AD | « À DÉFINIR » : constante, coefficients, côté d'armure, effet relatif des masses, amortissement, dégâts au sol, collisions multiples | E6, E7, E8, E9, E24 (F) | — | « Encore ouvert », collisions | à définir |
| DS4-EC | « ÉCART À TRAITER » : E6 de G non validée numériquement ; N9 et N10 distincts de l'effet relatif | E6 de G ; N9, N10 (R) | — | annotation de DS4.1 | conflit/écart |

### 1.5 DS5 — Ordre d'action, déplacement des corps et esquive

| ID | Élément source (C §6) | Règles antérieures touchées | Statut au registre | Texte proposé | Statut |
|---|---|---|---|---|---|
| DS5.1 | item 1 : monde figé, sauf esquives automatiques et chutes provoquées | I03, E9 (F) ; « interruptions non encore spécifiées » (R, encore ouvert) | I non inscrites ; interruptions encore ouvertes | DS5.1 ; « Encore ouvert », interruptions | accepté en conversation |
| DS5.2 | item 2 : arrêt au premier choc ; ordre chronologique ; rien de caché révélé d'avance | D13, I01, I03, P08 (F) ; S8, S9, S11 (R) | S8, S9 et S11 inscrites ; D et I non inscrites | DS5.2 | accepté en conversation |
| DS5.3 | item 3 : cible « repoussée sur une case voisine libre », attaquant sur la case initiale de la cible | K07 (F) ; S10 (R) | S10 inscrite ; K07 non inscrite | DS5.3, avec « à vérifier » | accepté en conversation ; conflit/écart à vérifier avec K07 (contrôle B7) |
| DS5.4 | item 4 : sinon la cible reste, l'attaquant « retombe à proximité » ; jamais deux unités sur une case | S10 (R) ; K07 (F) | S10 inscrite | DS5.4 | accepté en conversation ; rayon et cas impossible à définir |
| DS5.5 | item 5 : exclusion provisoire des unités de plusieurs cases, pour le saut offensif seulement | E9 (F) ; « taille des unités » (R, encore ouvert) | encore ouvert | DS5.5 ; « Encore ouvert », géométrie | accepté en conversation |
| DS5.6 | item 6 : coût proportionnel à Manhattan + `max(1, floor(0,20 × TU_max))`, payé à l'engagement, non remboursé | J09, J10, E13 (F) | absent | DS5.6 | accepté en conversation ; tarif à définir |
| DS5.7 | item 7 : voir l'unité ; TU restantes, même au tour adverse ; huit voisines au même niveau, accessibles et payables ; informations du camp ; débit en cas de réussite ; Réactions + 5 points par étage, bornée | K03 à K07, E17 (F) ; S1, S2, S6 à S8 (R) ; « capital et renouvellement des TU », « visibilité » (R, encore ouverts) | S inscrites ; K non inscrites | DS5.7 ; « Encore ouvert », TU | accepté en conversation ; règle numérique à définir |
| DS5-AD | « À DÉFINIR » : case de repousse, plusieurs cases, lieu de repli, aucun lieu valide, cible hors de combat, effets d'une poussée, tarif, probabilité d'esquive, loi de la case, destination inconnue ou occupée | E9, E13, E17, E22 (F) | — | « Encore ouvert », placement et TU | à définir |
| DS5-AV | « À VÉRIFIER » : lecture de « cible immobile » (K07) | K07 (F) | — | annotation de DS5.3 | conflit/écart |

**Décompte** : 25 principes acceptés (DS1.1 à DS5.7), chacun avec une source et un statut ; 5 groupes « à définir » ; 5 écarts (DS1-EC à DS4-EC, DS5-AV).

## 2. Contrôles de contradiction (mandat LOT-2H §3 B)

| # | Règles en présence | Analyse | Conclusion |
|---|---|---|---|
| B1 | DS1.3 ; P07 (F : tout sol qui coupe le volume bloque) | L'exception ne porte que sur le sol de la case quittée, pendant le saut de l'unité qui la quitte. Le texte proposé le dit et exclut toute extension. Les autres sols restent bloquants : en diagonale, les sols des deux cases orthogonales voisines peuvent encore couper le volume (constat de G, D-E1b). Les largeurs limites calculées par G supposent une vitesse de départ indépendante de la masse (voir B2). | Compatible. Écart consigné (DS1-EC). |
| B2 | DS2.1, DS2.3 ; P04, P05 (F) ; E11 de G | Le poids réduit la hauteur **et** la portée. P04 et P05 restent des références, valables pour une masse de référence encore à fixer. La recommandation E11 de G (vitesse égale pour toutes les masses) est écartée. Ses alternatives (quantité de mouvement, énergie) n'ont pas été choisies : leurs exemples restent illustratifs. La consolidation ne dit pas si la capacité horizontale dépend aussi du poids ou si seule la durée de vol diminue. P02 (impulsion verticale initiale constante pour une même unité et une même action) reste compatible avec DS2.1 si l'impulsion est une quantité de mouvement ou une énergie : à impulsion égale, une unité plus lourde part moins vite. Elle ne l'est pas avec la lecture « même vitesse », écartée. Une « autre loi » devrait être vérifiée face à P02. | Écart à traiter avant implémentation (§4). Aucune formule n'est inscrite. |
| B3 | DS3.1 à DS3.4 ; D01, D03, E18 (F) ; N7 (R) | La **puissance de base** reste `B(n)` (D03, D04), avec 8 pour un étage. Le **dégât appliqué** à l'unité qui tombe d'un seul étage sans surcharge est nul. D01 (« chute blessante possible dès un étage ») reste vraie pour l'unité percutée (DS3.4) et pour l'unité en surcharge. Au-delà d'un étage, pas d'exemption (DS3.3). E18 (chute au sol de l'attaquant après une esquive) suit la même exemption. N7 n'est plus simplement « contredite » (H01 du LOT-2F) : elle est précisée pour l'unité qui tombe. D'où une annotation, sans réécriture. | Compatible si la base et le dégât appliqué sont distingués, comme le fait le texte proposé. H01 et E21 du LOT-2F sont à requalifier (proposition §5, ligne 14). |
| B4 | DS3.1, DS5.7 ; E12 (F) ; E12 de G | La consolidation ne tranche pas le mode de comptage des étages (« non expressément confirmé »). Le texte proposé dit « chute d'un seul étage » sans définir le comptage. La recommandation E12 de G (sols franchis vers le bas, `n = 0` sans dégâts) n'est pas reprise. Aucune règle n'est inventée pour une chute de moins d'un étage, au sol ou sur une unité. Le bonus de + 5 points par étage de l'esquive dépend aussi d'un comptage des étages ; qu'il soit le même que pour les chutes (E12 b de G) n'est pas décidé. | Ouvert ; listé dans « Encore ouvert » et au §5 de la proposition (ligne 3). |
| B5 | DS4.1 ; N9, N10 (R) ; K08, E6, E24 (F) ; C3 de G | Dans une collision entre unités, la masse relative protège la plus lourde (DS4.1). Lors d'une chute au sol, le poids aggrave (N9, N10). Les deux effets restent distincts, comme le demande la consolidation. Cela correspond à l'option (i) du constat C3 de G, pour le sens de l'effet seulement. La formule E6 de G (`β`, borne `2/7`) n'est pas validée. Tirages communs ou séparés entre deux unités : non décidé (DS4.5 ne vise que l'unité et l'obstacle). | Compatible. Formules ouvertes. |
| B6 | DS4.2, DS4.3, DS4.5, DS3.5 ; D05, D10, D11, D12 (F) ; E8 de G | Le carré de la vitesse normale, le poids total, le plafond de 70 et le type « impact » sont acceptés. Le facteur `min(M/80, 3)` de D10 reste en vigueur ; « à masse égale » dans DS4.2 est cohérent avec un facteur multiplicatif. La constante est ouverte : le calage de G (8 points pour l'atterrissage d'un saut d'un étage, coefficient 3,2) n'est pas repris, et il supposait en outre une vitesse de référence indépendante de la masse. Le tirage est commun à l'unité et à l'obstacle (DS4.5). Dans OXCE, cela correspond à la méthode 2, qui reprend pour le terrain le tirage fait pour l'unité ; ce n'est pas la méthode par défaut, qui fait un tirage propre (`src/Mod/RuleDamageType.cpp:37`, `:139-142`, commit `441cae1`, lecture du code, citée par G). Pour un obstacle, le poids entre dans la base (D10), avant le tirage : le « second arrondi après le facteur de poids » de DS3.5 n'y a pas d'objet, sauf facteur appliqué plus tard. Base d'une collision entre unités : non décidée, car une chute sur une unité n'est pas assimilée à une chute au sol (C §4). | Compatible. Constante, base des collisions entre unités et précision de DS3.5 pour les obstacles : à définir. |
| B7 | DS5.3, DS5.4 ; K07 (F) ; S10 (R) | K07 dit « cible immobile, aucune TU dépensée pour l'essai » en cas d'esquive échouée. DS5.3 repousse la cible **après** la collision non esquivée : aucun déplacement d'esquive n'a lieu avant. L'attaquant prend la case de la cible si la poussée est possible ; sinon il retombe à proximité (DS5.4). S10 est respectée : jamais deux unités sur une case. Rayon, cas impossible et cible hors de combat : non décidés. | Écart à confirmer avant une inscription définitive (proposition §5, ligne 7). |
| B8 | DS5.1, DS5.2, DS5.5 à DS5.7 ; E9, E13, E17 (F) ; registre « encore ouvert » | Monde figé hors esquives et chutes ; arrêt au premier choc ; grandes unités exclues à titre provisoire, pour le saut seulement ; coût complet à l'engagement ; esquive avec les TU restantes vers huit voisines payables, selon les informations du camp. Restent ouverts : tarif par case, coûts du terrain (pas d'esquive), règles de visibilité, renouvellement des TU (DS5.7 suppose des TU gardées pendant le tour adverse). La consolidation garde « destination inconnue ou occupée en cours d'action » à définir : la conséquence tirée par G (cas impossible sous monde figé) n'est pas reprise. | Compatible. Données de coûts et de visibilité non fixées. |

## 3. Effet sur les 13 points bloquants du LOT-2F

Aucun des 13 points n'est entièrement résolu : les principes sont tranchés, pas les formules ni les valeurs.

| Point | Tranché en principe par | Reste ouvert | État |
|---|---|---|---|
| E1 | DS1.1 à DS1.4 | Rapport case/étage, dimensions, surfaces, contacts, précision | principe tranché ; paramètres ouverts |
| E2 | DS2.2 (Manhattan, déjà P05) ; DS2.1 (effet du poids) | Règles numériques de la portée ; loi du poids | partiellement tranché |
| E3 | DS2.4 | Bornes de gravité ; valeurs extrêmes | principe tranché ; bornes ouvertes |
| E5 | DS3.5 | Entrée entière du tirage (D06) ; calcul exact ou approché ; cas d'un obstacle (aucun facteur après le tirage) ; valeurs extrêmes | partiellement tranché |
| E6 | DS4.1 (sens de l'effet) | Formule ; tirages communs ou séparés | sens tranché ; formule ouverte |
| E7 | DS4.4 | Côté d'armure ; résistances ; conversions | principe tranché ; paramètres ouverts |
| E8 | DS4.2, DS4.3, DS4.5 | Constante ; base des collisions entre unités | partiellement tranché |
| E9 | DS5.1 à DS5.5 | Repousse et repli ; collisions multiples ; destination inconnue ou occupée | partiellement tranché |
| E11 | DS2.1 (le poids réduit hauteur et portée) | Loi et masse de référence | sens tranché ; loi ouverte |
| E12 | DS3.1 (exemption d'un étage) | Comptage des étages, pour les chutes et pour l'esquive ; chute de moins d'un étage, au sol ou sur une unité | ouvert |
| E13 | DS5.6 | TU par case | principe tranché ; tarif ouvert |
| E17 | DS5.7 | Règle numérique ; loi du choix de la case ; moment où « voit » est évalué | partiellement tranché |
| E24 | DS3.1 à DS3.3 ; DS4.1 (distinction avec N9, N10) | Formule au sol ; effet des caractéristiques | partiellement tranché |

## 4. Propositions du LOT-2G : reprises, écartées, non reprises

Les lettres renvoient aux sous-propositions de la rubrique 3 de chaque point de G. « Principe seulement » : C reprend l'idée, pas les détails de G.

| Catégorie | Éléments de G |
|---|---|
| **Reprises par C, en principe seulement** | E1 a et d, en partie : proportions sans mètres, forme en pavé ; E1 f : sol de départ ignoré ; E1 i et E9 d, pour la cible seulement : elle reste percutable ; E3 a et b : plage de gravité, apesanteur exclue ; E5 b, d et e : deux arrondis au plus proche, puis les règles propres des conversions ; E7 a, principe seulement : type « impact » propre à Bastion, inspiré d'OXCE (armure, puis santé et étourdissement) ; E8 b, principe seulement : carré de la vitesse normale, **sans** le calage ; E9 a et c : monde figé, arrêt au premier choc ; E9 i, pour le saut offensif seulement ; E13 a et b, principe seulement : coût proportionnel à Manhattan, payé en entier à l'engagement ; E17 a, b et c, en partie : TU restantes, huit voisines au même niveau accessibles et payables, informations du camp. La mesure en Manhattan (E2) était déjà acquise (P05). |
| **Alternatives de G retenues** | Place finale : la cible est repoussée (alternative C de E9) ; si elle ne peut pas l'être, l'attaquant se place à proximité, comme le proposait déjà E9 h, sans en reprendre les détails (case voisine tirée comme pour l'esquive, sans TU) ; tirage commun pour l'unité et l'obstacle (E8 e, option de reprise du tirage) |
| **Écartée** | Vitesse de départ égale pour toutes les masses (recommandation E11) |
| **Non reprises : restent des propositions** | E1 a (unité de temps `√(H/g0)`), b, c, détails de d (base carrée, alignement sur les axes, `w ≤ λ`, `h_u < 1`, point de référence, départ centré), e, g et h ; E2 a à d, dont `R(γ, δ)` et la tolérance ; E3 c et d, dont les seuils de gravité ; E5 a, c (tirage entier) et f ; E6 a à c, dont `1 ± β` et la borne `2/7`, et l'alternative D ; E7 détails de a (écart 50, modificateur de résistance, côté, armure × efficacité), b (côtés), c (taux) et d (mise hors de combat) ; E8 a, calage de b, c (base `B(n)` des collisions entre unités) et d ; E9 b, détails de d (`n = z_dép − z_arr`, renvoi à E8 c), e (impossibilité de T-X01), f, g, détails de h, et « hors de `MEC-0001` » de i ; E12 a à e ; E13 c, d et la valeur de `c_s` ; E17 détails de b, échec de c sur une case occupée inconnue, d et e ; E24 a à d |
| **Nouveau dans C, absent de G** | Exemption d'un étage pour l'unité qui tombe sans surcharge, avec le seuil de N14 (DS3.1, DS3.2) ; l'attaquant prend la case initiale de la cible repoussée (DS5.3) |

Pour comparaison seulement : dans OXCE, l'unité qui se trouve sous une chute est écartée vers une case voisine quand elle est inconnue ou que la chute n'est pas planifiée ; une chute planifiée vers une unité connue est refusée (LOT-2E C7, lecture du code au commit `441cae1`). DS5.3 n'est donc pas une reprise de ce comportement.

**Calculs du LOT-2G à ne pas reprendre en l'état.** Ils supposent une vitesse de départ indépendante de la masse, que DS2.1 écarte. Ils ne vaudraient, au mieux, que pour la masse de référence, et seulement si la loi retenue lui donne la vitesse calée par P04 :
- portée `R(γ, δ)` et son tableau ; seuils de 2,764 g, 4,292 g et 5,820 g (G, E2 et E3) ;
- part du vol `ρ` et largeurs limites de D-E1b (`0,236 λ`, etc.) (G, E1) ;
- élévations et conditions de plafond selon la gravité (G, E3) ;
- calage `v_ref² = 2,5` et exemples de chocs (G, E8) ;
- calcul du contact latéral avec la cible (« 70 % du vol », G, E1 rubrique 7) ;
- tableau de E11 : ses alternatives restent des illustrations ;
- attendus des impacts de G :
  - T-J04 et T-J05 (portée et élévation) ;
  - T-J09 (plafond touché si `h_u > 1 − 1/(4γ)`) ;
  - T-J10, T-D09 et T-D10 (coefficient 3,2, tiré de `v_ref² = 2,5`) ;
  - le tableau de requalification de T-J02, T-J03 et T-J11 (`0,236 λ`, `0,447 λ`, `1,342 λ`, tirés de `ρ`) ;
  - T-G01, T-G02, T-G03 et T-G14 ;
  - T-G05, **contredit** par DS2.1 (même élévation et même portée quel que soit le poids).

T-G04 (`γ = 0` : saut indisponible) ne dépend pas de la vitesse de départ et concorde avec DS2.4. Plus largement, tous les attendus des impacts de G reposent sur ses recommandations : seuls ceux dont C reprend le principe restent pertinents, et leurs valeurs restent à recalculer.

## 5. Ce qu'une future écriture au registre nécessiterait

- Une autorisation explicite et distincte du propriétaire, et un mandat d'écriture du registre.
- La confirmation du contenu de la consolidation, avec sa date (proposition §5, ligne 13).
- De préférence, l'inscription préalable ou simultanée des décisions du 9 novembre et du correctif (E16 du LOT-2F), auxquelles DS1 à DS5 renvoient (proposition §5, ligne 11).
- Un choix sur le rattachement à `MEC-0001` (ligne 12) et sur l'annotation de N7 (ligne 14).
- L'application du diff de la proposition (§4), vérifiée sur le registre de `main` au commit `7290838`. Si le registre change d'ici là, le diff serait à régénérer.
