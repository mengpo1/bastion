# LOT-2I — Consolidation de `MEC-0002` : sauts, chutes et collisions

> **Document de travail. Rien n'est inscrit au registre, aucun gameplay n'est autorisé.** « Validé en conception » ne vaut ni texte final d'inscription ni autorisation d'implémentation : ce sont trois actes distincts (consolidation provisoire, en-tête).

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2I-v1.1.md`, sur `orchestration/mandats` (commit `58d3ebc96d1921f83b88728d2f41b31e7173138f`, SHA-256 `6ac95b0d996cd75b47253818ff65edbd79b1dd18ff3aece250f2c2e97e3c6ef6`). **Non archivé** dans `docs/mandates/` : le propriétaire ne l'a pas encore autorisé. |
| Autorisation | Propriétaire, 14 novembre 2026 : exécution du mandat LOT-2I v1.1 « uniquement dans son périmètre documentaire », puis confirmation « L'exécution documentaire du mandat LOT-2I v1.1 reste autorisée ». Branche validée : `docs/lot-2i-consolidation-mec-0002`. Archivage du mandat et modification de `docs/mandates/README.md` : **non autorisés**. Aucun push, aucune PR, aucune fusion. |
| Document de travail | `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` sur `orchestration/mandats` (commit `d028c52f500ed8daeca917adbcb9a9e1eb3ff8bd`, objet Git `2cd7e97a…`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`), écrit par l'orchestrateur. Noté **C2** ci-dessous. Lu, non copié dans le dépôt. |
| Preuve des arbitrages | Déclaration du propriétaire du 14 novembre 2026, notée **D2** : « les 29 propositions de conception et les six arbitrages complémentaires (1A à 6A) ont été acceptés le 14 novembre 2026, avec la précision concernant les esquives spontanées dont la réussite dépend de la caractéristique Réactions. Cette confirmation constitue une preuve déclarative de mes arbitrages. » |
| Branche | `docs/lot-2i-consolidation-mec-0002`, créée depuis `origin/main` = `74faa2974da7a4645725b4271eb66ae2a512e98a`, après `git fetch origin main`. Locale. |
| Compagnons | `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` (provenance, écarts, tests futurs) ; `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md` (texte proposé, non appliqué) ; `docs/reviews/LOT-2I-EXECUTION.md` (contrôles, revue, limites). |

## 0. En bref

- La consolidation compte **105 règles** identifiées (§2 à §9) : les 103 règles de C2, plus 2 règles de DS1 à DS5 que C2 ne redit pas mais ne modifie pas (GE-09, RP-09). Chacune a un statut et dit ce qu'elle remplace ou précise :
  - **64** sont « validées en conception » sans réserve ;
  - **33** sont validées dans leur principe, mais dépendent d'au moins un paramètre ouvert ;
  - **8** sont validées, mais leur texte est **à confirmer avant inscription** : PE-01, GE-09, CH-01, CH-04, CH-09, CO-08, RP-01 et RP-09 ;
  - aucune n'est « ouverte » en entier : C2 range les sujets non tranchés dans sa liste de paramètres, reprise au §12.
- **Interactions avec `MEC-0001`** : la marche reste dans `MEC-0001` ; les sauts, chutes, collisions, esquives et repoussements passent dans `MEC-0002`. Les sous-décisions N5 à N10 de `MEC-0001`, qui parlent de chutes, deviennent l'historique de `MEC-0002` (§10).
- **Contradictions et écarts** : les 8 points du mandat (§11.1) et 12 autres constats (§11.2). Les plus importants :
  - le **tirage commun** aux deux unités d'une collision, avec un facteur de masse déterministe, fixe l'ordre des blessures avant l'armure : à puissances égales, la plus légère est toujours la plus blessée. DS4.1 dit que le poids ne doit pas décider seul (§11.1, point 8). Ce constat dépend d'une lecture de DS4.1 et de K08, à confirmer ;
  - l'unité qui tombe d'un étage sans surcharge **sur une unité** n'est plus exemptée de dégâts, changement que C2 ne signale pas (§11.2, X12) ;
  - l'exemption de petite chute dépend de la gravité et de la masse d'une façon peu cohérente (§11.2, X3 et X4).
- **28 ambiguïtés** à trancher avant une implémentation déterministe, dont **8 avant même l'inscription** (§12).
- **Limite de traçabilité** : C2 ne numérote pas les 29 propositions ni les réponses 1A à 6A. Aucune règle ne peut donc être rattachée à une proposition précise, sauf l'exclusion des grandes unités (« proposition 8/29 »). La preuve D2 couvre l'ensemble, de façon déclarative (§13).

## 1. Sources, statuts et conventions

**Sources** (par ordre de priorité, selon C2 §1) :
- **D2** et **C2** : arbitrages du 14 novembre 2026, qui **prévalent pour la conception** quand ils modifient une hypothèse ancienne.
- **DS** : principes DS1 à DS5 du 13 novembre 2026 (`docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`).
- **M** et **P** : décisions du 9 novembre 2026 et correctif du propriétaire (E14, E18, E23), transcrits au LOT-2F (`docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`). Non inscrits au registre.
- **R** : registre `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` (S1 à S12, Z1, N1 à N14), SHA-256 `c2a3a55e…3968`.
- **G** et **H** : dossiers LOT-2G et LOT-2H. Leurs propositions ne valent que si C2 les reprend.

**Statuts** (mandat v1.1 §2.2) :
- **validé en conception** : décision de C2 couverte par D2, sans paramètre ouvert ;
- **validé en conception, paramètre ouvert** : le principe est décidé, mais une valeur ou un détail ne l'est pas (colonne « Ouvert ») ;
- **validé en conception, à confirmer avant inscription** : le principe est décidé, mais son texte dépend d'un point à confirmer par le propriétaire avant toute inscription (ambiguïtés « inscription » du §12) ;
- **ouvert** : non décidé.

**Identifiants proposés** (à confirmer lors d'une inscription) : PE (périmètre), GE (géométrie, masse, posture), SA (sauts), CH (chutes), CO (collisions), ES (esquives), RP (repoussement), EN (environnement et événements).

**Fidélité** : les règles reprennent C2 en phrases simplifiées, sans changement de sens. Le texte de C2 fait foi.

## 2. Périmètre (C2 §2)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| PE-01 | `MEC-0001` garde la marche ordinaire : cheminement, coûts de terrain, diagonales, visibilité du trajet, TU du déplacement ordinaire. Elle conserve S1 à S12, Z1 et N1 à N14, avec une annotation historique de N7, sous réserve d'autorisation d'inscription. | validé en conception, à confirmer avant inscription | Rattachement de la fiche (LOT-2H, §5 ligne 12) | primauté entre les deux fiches (A24) |
| PE-02 | `MEC-0002` couvre le saut simple, l'attaque sautée, les chutes volontaires et involontaires, la trajectoire, les contacts et collisions, la réception, l'esquive réactive, le repoussement, l'impact des corps, la destruction sous impact et la chaîne d'événements associée. | validé en conception | — | — |
| PE-03 | Hors de `MEC-0002` : escaliers, échelles, ascenseurs, règles générales du brouillard, renouvellement global des TU, stabilité structurelle des bâtiments. | validé en conception | — | — |
| PE-04 | Décrire une règle physique utilisable ailleurs n'autorise pas d'autres mécaniques (tir, explosion, destruction de cadavre, vol, apesanteur, etc.). | validé en conception | — | — |

## 3. Géométrie, masse et posture (C2 §3)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| GE-01 | Positions `(x, y, z)`, plusieurs niveaux. | validé en conception | N3 (R) | — |
| GE-02 | Largeur de case, hauteur d'étage et volumes des unités en proportions, sans mètres pour la grille. | validé en conception, paramètre ouvert | DS1.1 | rapports exacts |
| GE-03 | Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. | validé en conception, paramètre ouvert | DS1.2 ; postures : nouveau | dimensions par type et posture |
| GE-04 | Pendant le vol, posture et orientation du volume sont conservées : pas de rotation des pavés, pas de changement de posture. | validé en conception | nouveau | — |
| GE-05 | Un contact de surfaces suffit à détecter la rencontre. Sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés, sans créer d'énergie ni dédoubler un impact. | validé en conception, paramètre ouvert | D11 ; contacts : nouveau | tolérance numérique |
| GE-06 | La masse physique totale `M` comprend le corps, l'armure, l'équipement et l'inventaire, en kg. | validé en conception, paramètre ouvert | E23 (P) | masses par type et par objet |
| GE-07 | La charge portée, pour la surcharge, comprend l'armure, l'équipement et l'inventaire, en kg ; elle est distincte de `M`. La Force se traduit en capacité de portage en kg, selon un modèle à définir. | validé en conception, paramètre ouvert | N10, N14 (R) ; E20 (LOT-2F) | modèle Force → capacité |
| GE-08 | Les unités de plusieurs cases peuvent subir des chutes involontaires et des collisions. Leurs sauts volontaires sont provisoirement indisponibles (« proposition 8/29 »). | validé en conception | étend DS5.5, qui excluait l'attaque sautée faite par ces unités et contre elles | — |
| GE-09 | Une unité de plusieurs cases n'est pas choisie comme cible d'une attaque sautée. **Maintenue de DS5.5** : C2 ne la redit pas, mais ne la modifie pas. | validé en conception, à confirmer avant inscription | DS5.5 | confirmation (A12) |

## 4. Sauts (C2 §4)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| SA-01 | Saut simple vers une destination admissible au même niveau ou plus bas ; il permet de franchir une ouverture ou un obstacle. Un saut vers une zone sans support immédiat est permis : l'unité continue de tomber jusqu'à un support ou un contact. | validé en conception | nouveau ; N5 (R) | — |
| SA-02 | L'attaque sautée n'est possible que si la cible est au moins un étage plus bas. | validé en conception | J01 (M) | — |
| SA-03 | Un allié ou un neutre déjà identifié ne peut pas être ciblé intentionnellement. | validé en conception | J06 (M) | — |
| SA-04 | Un ennemi actuellement visible peut être ciblé malgré S10. | validé en conception | J13, E14 (P) ; DS1.4 | — |
| SA-05 | Destination visible ou déjà explorée ; jamais explorée : interdite. | validé en conception | J03, J04 (M) ; S6 (R) | — |
| SA-06 | Les cases survolées peuvent n'avoir jamais été explorées. | validé en conception | tranche E15 (LOT-2F) | — |
| SA-07 | Obstacles et unités cachés ne sont révélés qu'à leur rencontre. | validé en conception | P08, I01 (M) ; DS5.2 | — |
| SA-08 | Un ennemi caché, ou un allié ou neutre caché, sur la case attaquée peut être percuté, avec le bonus d'attaque sautée même s'il était allié ou neutre. | validé en conception | J05, J07, J08 (M) | — |
| SA-09 | Un saut simple qui percute par accident une unité cachée : collision et dégâts possibles, **sans** bonus × 1,25. | validé en conception | nouveau ; D08 (M) | — |
| SA-10 | Arc balistique continu, sans contournement des obstacles. Seule une destination à portée de Manhattan est permise ; la trajectoire réelle est ensuite vérifiée avec les volumes. | validé en conception | P07 (M) ; DS1.2 | — |
| SA-11 | Le sol de la case de départ est ignoré au décollage, sans étendre cette exception aux autres surfaces. | validé en conception | DS1.3 | — |
| SA-12 | Obstacle connu sur la trajectoire : engagement interdit, sauf pour les cibles offensives permises. Obstacle inconnu : saut engagé, puis collision, arrêt et révélation à l'impact. | validé en conception | P08 (M) | — |
| SA-13 | En vol : aucune modification volontaire de destination ni d'impulsion ; vitesse horizontale constante tant qu'aucun contact ne la modifie ; fin de l'action à une réception stable, sans glissement automatique. | validé en conception | nouveau | — |
| SA-14 | Le saut s'arrête au premier choc ; la collision et les chutes qui suivent sont des événements distincts, résolus dans l'ordre chronologique. | validé en conception | DS5.2 ; D13 (M) | — |
| SA-15 | Chaque type d'unité a une impulsion verticale et une capacité d'impulsion horizontale distinctes et configurables. | validé en conception, paramètre ouvert | P02, P03 (M) | valeurs par type |
| SA-16 | Loi : impulsion constante à effort égal. Pour une unité donnée et des conditions comparables, la vitesse initiale varie en raison inverse de sa masse totale, `v = v_ref × (M_ref/M)`. À gravité constante, la hauteur varie comme le carré du rapport des masses ; la portée diminue aussi quand la masse augmente. | validé en conception, paramètre ouvert | DS2.1 ; tranche E11 (quantité de mouvement) ; écarte la recommandation E11 de G | `M_ref`, `v_ref` par type |
| SA-17 | La gravité influe sur la durée de vol, la hauteur et la portée. Chaque type d'unité a sa plage de gravité où il peut sauter. | validé en conception, paramètre ouvert | P01 (M) ; DS2.4 (plage par type au lieu d'une plage unique) | bornes |
| SA-18 | Aucun saut balistique à 0 g ; l'apesanteur est hors périmètre. Une chute involontaire reste possible en gravité positive, même quand les sauts sont interdits. Une gravité négative est invalide. | validé en conception | DS2.4 ; E3 (LOT-2F) | — |
| SA-19 | Référence à 1 g, pour l'unité de référence : sommet à un quart d'étage ; portée de 2 cases de Manhattan **au même niveau**, pour franchir un trou d'une case ; portée pour un étage de descente **supérieure à 2 cases**, valeur à calculer. | validé en conception, paramètre ouvert | P04 (M) inchangée ; **remplace** P05 (M) et la portée de DS2.3 | valeur de la portée en descente |
| SA-20 | À capacités égales, un saut au même niveau a une durée de vol et une portée inférieures à un saut avec un étage de descente. | validé en conception | conséquence de SA-16 à SA-19 | — |
| SA-21 | Portée horizontale `\|Δx\| + \|Δy\|`, plafond entier arrondi vers le bas. Aucune portée minimale garantie quand le calcul donne moins d'une case. | validé en conception | P05 (M) ; DS2.2 ; tranche la conversion de E2 | — |
| SA-22 | Distance pour les TU : `d_3D = \|Δx\| + \|Δy\| + \|Δz\|`, distincte de la portée horizontale. | validé en conception | précise DS5.6 (« distance de Manhattan ») | — |
| SA-23 | `TU_simple = d_3D × C_saut`. | validé en conception, paramètre ouvert | nouveau | `C_saut` ; coût non entier |
| SA-24 | `TU_attaque = d_3D × C_saut + max(1, ⌊0,20 × TU_max⌋)`. | validé en conception, paramètre ouvert | J09 (M) ; DS5.6 | `C_saut` ; coût non entier |
| SA-25 | `C_saut` est propre aux sauts, indépendant de la marche ; sa valeur est explicitement reportée à l'équilibrage. | validé en conception, paramètre ouvert | E13 (LOT-2F) | valeur |
| SA-26 | Coût payé en entier à l'engagement, même si le saut est interrompu ou si la cible esquive ; aucun remboursement. Une chute passive qui suit la destination choisie ne coûte pas de TU en plus. | validé en conception | J09 (M) ; DS5.6 | — |
| SA-27 | Une action sans TU suffisantes est interdite. Destination, coût et trajectoire sont prévisualisés dans les limites des informations connues. | validé en conception | J10, I02 (M) | — |

## 5. Chutes et réception (C2 §5)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| CH-01 | Un saut volontaire (simple ou offensif) d'**un étage**, sans surcharge et sans collision avec une unité, n'inflige pas de dégâts de chute. | validé en conception, à confirmer avant inscription | précise DS3.1 (« volontaire ») ; N7 (R) | définition de « un étage » (§12, A3) |
| CH-02 | En surcharge, un saut volontaire d'un étage peut produire des dégâts. | validé en conception | DS3.1, DS3.2 | — |
| CH-03 | Une chute **involontaire** peut blesser dès un étage, même sans surcharge, qu'elle soit prévue ou subie par surprise. | validé en conception | D01 (M) ; restreint l'exemption de DS3.1 | — |
| CH-04 | Une réception sur une unité est une collision, qui peut blesser les deux unités, distincte d'une chute au sol. Le bonus offensif ne vaut que pour l'attaque sautée. | validé en conception, à confirmer avant inscription | DS3.4 ; K01, K02, D08 (M) ; **restreint** DS3.1 : l'unité qui tombe d'un étage sans surcharge sur une unité n'est plus exemptée | changement de DS3.1 à confirmer (A25) |
| CH-05 | Si la cible esquive, l'attaquant finit son saut au sol : ce saut reste **volontaire**, et l'exemption d'un étage sans surcharge s'applique. | validé en conception | E18 (P) ; DS3.1 | — |
| CH-06 | Si un obstacle interrompt la trajectoire puis provoque une nouvelle chute, cette chute est **involontaire** ; collision et chute sont comptées séparément. | validé en conception | D13 (M) | — |
| CH-07 | La puissance de référence d'une chute au sol reste celle du LOT-2F : `B(1) = 8`, `B(2) = 14`, `B(3) = 22,1`, `B(4) = 33,035`, incréments de + 6 puis × 1,35. | validé en conception | D03, D04 (M) | — |
| CH-08 | Hauteur réelle de chute, fractions d'étage comprises ; interpolation linéaire entre les points de référence. | validé en conception | nouveau ; tranche le comptage de E12 pour les dégâts | — |
| CH-09 | Hauteur équivalente ≤ 0,25 étage : aucun dégât. Entre 0,25 et 1 étage : interpolation de `(0,25 ; 0)` à `(1 ; 8)`. | validé en conception, à confirmer avant inscription | précise N7 (R) ; tranche « moins d'un étage » (DS3) | portée du seuil selon la gravité (§12, A4) |
| CH-10 | En gravité positive, la puissance de référence est multipliée par `g/g0`, avec `g0 = 1 g` ; la précision décimale est gardée jusqu'aux arrondis prévus. | validé en conception, paramètre ouvert | **modifie** D03, qui ne dépendait pas de la gravité | point d'application (§12, A5) |
| CH-11 | Vitesse verticale initiale descendante : hauteur équivalente `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 0,25 porte sur `H_eq`. Vitesse initiale montante : la montée, le sommet et la descente sont résolus physiquement, avec la vitesse réelle à l'impact. | validé en conception | nouveau | — |
| CH-12 | Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse verticale ; la vitesse horizontale compte contre les surfaces qui lui sont normales. | validé en conception | D11 (M) | — |
| CH-13 | Plafond de puissance de base 70 pour une chute au sol, **avant** le multiplicateur de surcharge, qui peut porter la puissance au-delà de 70 avant le tirage. Les plafonds 60 (unité qui tombe), 80 (cible percutée) et 70 (obstacle) restent pour leurs domaines, sous réserve d'une vérification de la chaîne. | validé en conception, paramètre ouvert | D05 (M) ; déroge à D09 (M), qui plaçait les facteurs de poids après le tirage | vérification de la chaîne (§12, A6) |
| CH-14 | Capacité de portage en kg selon la Force ; seuil de surcharge commun à N14. | validé en conception, paramètre ouvert | DS3.2 ; N14 (R) | modèle Force → kg |
| CH-15 | Dépassement relatif `S = max(0, charge / capacité − 1)`, avec une capacité strictement positive. | validé en conception | nouveau | — |
| CH-16 | Multiplicateur `F_surcharge = min(2, 1 + 0,5 × S)`. | validé en conception | nouveau ; tranche E24 pour le poids au sol | — |
| CH-17 | Ce multiplicateur aggrave la puissance utilisée pour les blessures et pour l'étourdissement ; l'armure applique ensuite ses protections. | validé en conception | N9, N10 (R) | — |
| CH-18 | La surcharge ne supprime pas le seuil de 0,25 étage. | validé en conception | nouveau | — |
| CH-19 | La nature du sol ne modifie pas directement les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol. | validé en conception | D02 (M) | — |
| CH-20 | L'impact peut endommager ou détruire le support ; s'il cède, la chute continue. Chaque impact successif est résolu à part, et les dommages corporels peuvent s'additionner. | validé en conception | D12, D13 (M) | — |
| CH-21 | Traverser une surface destructible absorbe de l'énergie et ralentit le corps ; la gravité peut ensuite le réaccélérer. | validé en conception, paramètre ouvert | nouveau | formule de perte d'énergie |

## 6. Collisions et dégâts (C2 §6)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| CO-01 | Détection des contacts sur les volumes réels au moment du contact, y compris après un déplacement d'esquive ou une perte de support. | validé en conception | DS1.2 | — |
| CO-02 | Puissance de base `P = K × v_n²`, où `v_n` est la composante normale de la vitesse relative au contact (entre deux unités, ou contre une surface fixe). Deux coefficients distincts et configurables : `K_unités` et `K_obstacles`. | validé en conception, paramètre ouvert | étend DS4.2 aux collisions entre unités ; D10 (M) | `K_unités`, `K_obstacles` |
| CO-03 | Entre unités, facteur appliqué aux dégâts reçus par chacune : `F_i = clamp(√(M_autre/M_i), 0,75 ; 1,5)`, masses strictement positives. | validé en conception, paramètre ouvert | DS4.1 ; K08 (M) ; formule E6 de G non reprise | interaction avec le tirage commun (§11.1, point 8) |
| CO-04 | Contre le décor : référence du LOT-2F `min(M/80, 3)` pour le facteur de masse, et plafond de 70. Le point d'insertion de ce facteur dans la nouvelle chaîne reste à revoir. | validé en conception, paramètre ouvert | D10, D05 (M) | point d'insertion (§12, A7) |
| CO-05 | Type de dégâts « impact » propre à Bastion : zones corporelles exposées et protections d'armure liées à la direction du choc, sans recopier de code ni de données d'OXCE. | validé en conception, paramètre ouvert | DS4.4 ; D07 (LOT-2F, ouverte : E7) | protections par zone |
| CO-06 | Blessures et étourdissement sont des effets séparés ; une armure peut protéger plus la santé que l'étourdissement ; on peut être étourdi sans perdre de santé. | validé en conception, paramètre ouvert | K02 (M) | coefficients santé / étourdissement |
| CO-07 | Chaque type d'unité a une sensibilité à l'étourdissement ; 0 vaut immunité aux étourdissements d'impact. Une unité consciente mais étourdie peut encore tenter une esquive, avec des Réactions réduites. | validé en conception, paramètre ouvert | nouveau | pénalité sur les Réactions |
| CO-08 | Tirage d'intensité de 50 à 150 %, **une fois par événement de collision**, partagé par les deux unités d'une collision entre unités, ou par l'unité et l'obstacle. Résistances et effets s'appliquent ensuite à chacun. Des collisions réellement distinctes, même rapprochées, ont des tirages distincts. | validé en conception, à confirmer avant inscription | D06 (M) ; **étend** DS4.5 aux collisions entre unités | conflit avec DS4.1 (A8) ; nature et normalisation du tirage (A26) |
| CO-09 | Ordre : puissance initiale ; facteur de gravité s'il s'applique ; plafond de base ; bonus de surcharge et/ou d'attaque applicables ; arrondi au plus proche, moitié vers le haut ; tirage ; facteur de masse s'il s'applique ; second arrondi ; puis effets et protections séparés pour la santé et l'étourdissement. Les termes D09 et D10 sont à réconcilier, sans double comptage. | validé en conception, paramètre ouvert | DS3.5 ; D10 (M) ; déroge à D09 (M) : la surcharge, facteur lié au poids, précède le tirage | réconciliation (§12, A6 à A8) ; détail des deux arrondis et du tirage (A26) |
| CO-10 | Bonus × 1,25 uniquement sur les dégâts infligés à la cible d'une attaque sautée, après le plafond et avant le tirage ; jamais pour l'attaquant. Une cible alliée ou neutre cachée le reçoit aussi. | validé en conception | J08, J11, J12, D08 (M) | — |
| CO-11 | Contacts simultanés d'un même choc : les surfaces peuvent être endommagées, sans dupliquer la puissance corporelle. Contre plusieurs unités distinctes : un calcul par cible, regroupé au besoin dans un même événement. | validé en conception, paramètre ouvert | nouveau | détails d'implémentation |

## 7. Esquives réactives (C2 §7)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| ES-01 | Le moteur déclenche la tentative tout seul, sans le joueur ; la réussite n'est pas automatique : elle dépend d'un tirage et des Réactions. | validé en conception | K03, K05 (M) ; DS5.7 ; précision de D2 | — |
| ES-02 | Conditions : menace vue **juste avant l'impact**, TU suffisantes, case admissible. Une unité qui découvre la menace pendant la chute peut tenter l'esquive. | validé en conception, paramètre ouvert | K03 (M) ; DS5.7 | instant exact (§12, A15) |
| ES-03 | Bonus de + 10 points si l'unité menacée voyait la menace **dès le départ** du saut ou dès le début d'une chute involontaire ; sinon 0. Même logique pour les corps qui tombent, selon ce que perçoit la cible. | validé en conception | nouveau | — |
| ES-04 | Bonus de + 5 points par étage, `n = \|z_départ − z_arrivée\|`, pour une menace qui descend. | validé en conception, paramètre ouvert | K05 (M) | `n` pour un impact à hauteur intermédiaire |
| ES-05 | `P = clamp(R_effectif + B_visibilité + 5n, 0, 100)` %, où `R_effectif` est la valeur des Réactions après une éventuelle pénalité d'étourdissement. | validé en conception, paramètre ouvert | K05 (M) ; DS5.7 | pénalité d'étourdissement |
| ES-06 | Tirage entier uniforme `t` dans {1, …, 100} ; réussite si `t ≤ P`. | validé en conception, paramètre ouvert | nouveau ; G (E12 e) non repris | `P` non entier |
| ES-07 | Une unité inconsciente ou morte n'esquive pas ; les corps qui tombent peuvent, eux, être esquivés. | validé en conception | nouveau | — |
| ES-08 | Déplacement vers l'une des 8 cases voisines du même niveau, diagonales comprises, avec un support valide ; pas de saut dans le vide en esquivant. | validé en conception | DS5.7 | — |
| ES-09 | Coût habituel de la marche vers la case choisie (terrain, facteur diagonal), payé avec les TU restantes, même pendant le tour adverse. | validé en conception, paramètre ouvert | DS5.7 ; S2 (R) | coûts de terrain (`MEC-0001`) |
| ES-10 | Esquive réussie et effectivement faite : TU débitées. Échec du tirage ou déplacement impossible : aucun débit. | validé en conception | K06, K07 (M) | — |
| ES-11 | Choix aléatoire uniforme parmi les destinations admissibles. Une information cachée ne permet pas de choisir une case. La découverte d'un obstacle bloque et révèle la tentative, sans débit de TU. | validé en conception | K04 (M) ; tranche E22 (loi uniforme) | — |
| ES-12 | Pas d'échange simultané de cases ni de volumes qui se traversent ; destination libre au début de la résolution. Esquives en conflit : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager au hasard les combinaisons équivalentes. | validé en conception, paramètre ouvert | nouveau | algorithme (§12, A17) |
| ES-13 | Plusieurs menaces visibles et simultanées sur une même unité dans un même événement : une seule tentative ; la case doit éviter toutes les menaces **connues** ; `n` vient de la menace visible qui tombe du plus d'étages. Les menaces cachées ne comptent pas dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée. | validé en conception | nouveau | — |
| ES-14 | Dangers successifs : nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte suit le moteur séquentiel. | validé en conception | nouveau | — |

## 8. Repoussement et retombées (C2 §8)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| RP-01 | Esquive réussie : déplacement volontaire, pas de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un repoussement **après** l'impact. | validé en conception, à confirmer avant inscription | **tranche** le point « à vérifier » K07 (M) / DS5.3 | confirmation explicite demandée par la consolidation DS (A27) |
| RP-02 | Cible touchée : repoussement en priorité dans la direction de l'impact, sinon vers les directions voisines les plus proches, égalités tirées au hasard. Une case au-dessus du vide est admissible pour un repoussement forcé et entraîne une chute involontaire. | validé en conception | précise DS5.3 | — |
| RP-03 | Une case occupée par une autre unité n'est pas admissible : pas de repoussement en chaîne. | validé en conception | S10 (R) | — |
| RP-04 | Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort garde sa masse et son volume. | validé en conception | tranche « cible hors de combat » (DS5) | — |
| RP-05 | Si la cible ne peut pas être repoussée, l'attaquant cherche une case adjacente (8 voisines) pour retomber, en priorité du côté d'où il vient, puis par proximité de direction ; pas de recherche au-delà. | validé en conception | précise DS5.4 (rayon : cases adjacentes) | — |
| RP-06 | Impossibilité entièrement connue avant l'engagement : l'attaque sautée est refusée, sans révéler de données cachées. Impossibilité révélée en vol : l'attaquant s'arrête au contact, puis retombe verticalement depuis sa dernière position libre, sans pénétrer la cible. | validé en conception, paramètre ouvert | nouveau | issue de la retombée (§12, A19) |
| RP-07 | Une collision accidentelle, un cadavre ou un corps inconscient peut repousser ; aucune intention n'est requise, et aucun bonus offensif n'est créé. | validé en conception | nouveau | — |
| RP-08 | Plusieurs impacts vraiment simultanés : la direction du repoussement combine intensités et directions ; cela n'introduit pas d'attaques volontaires simultanées. | validé en conception | nouveau | — |
| RP-09 | Après le repoussement de la cible, l'attaquant prend la case initiale de la cible. **Maintenue de DS5.3** : C2 ne la redit pas, mais la suppose (RP-05). | validé en conception, à confirmer avant inscription | DS5.3 | confirmation (A18) |

## 9. Environnement destructible et événements (C2 §9)

| ID | Règle | Statut | Remplace ou précise | Ouvert |
|---|---|---|---|---|
| EN-01 | Murs, portes, planchers et autres décors destructibles ont des points de résistance **cumulatifs** : les dégâts successifs les réduisent. Les éléments indestructibles restent intacts. | validé en conception, paramètre ouvert | **modifie** D12 (M), qui suivait le seuil sans cumul d'OXCE | résistances, unité des dégâts du terrain |
| EN-02 | Tant que leur résistance reste strictement positive, les éléments gardent leur blocage et leurs collisions ; l'apparence peut changer, sans fissure fonctionnelle automatique. | validé en conception | nouveau | — |
| EN-03 | À zéro : destruction immédiate ; perte de support et chutes immédiates. Pas d'effondrement automatique des éléments voisins. | validé en conception | D12 (M) ; PE-03 | — |
| EN-04 | Un même événement qui produit plusieurs impacts simultanés sur un même plancher additionne leurs dégâts avant de décider de la destruction ; à distinguer de chutes successives. | validé en conception | nouveau | — |
| EN-05 | Tour par tour : une action offensive volontaire est résolue jusqu'au bout avant l'action de combat suivante. | validé en conception | DS5.1 | — |
| EN-06 | Si plusieurs unités perdent leur support à cause d'un même événement, leurs chutes sont traitées **l'une après l'autre**, dans un ordre stable (par exemple les identifiants internes), en file FIFO ; les nouvelles chutes passent après celles qui attendent. | validé en conception, paramètre ouvert | précise DS5.1 et DS5.2 ; I03 (M) | clé d'ordre ; articulation avec la chronologie (§11.1, point 3) |
| EN-07 | À chaque traitement : réévaluer positions, vitesses, santé et supports ; annuler un événement devenu caduc ; un seul événement de chute en attente par unité. | validé en conception | nouveau | — |
| EN-08 | Les corps morts ou inconscients peuvent tomber, heurter d'autres unités et provoquer dégâts, étourdissement ou repoussement. Un cadavre ne subit plus de pertes de santé ni d'étourdissement ; la destruction des corps est hors périmètre. | validé en conception | nouveau | — |
| EN-09 | Les collisions d'un même événement peuvent toucher plusieurs surfaces ou cibles, sans réintroduire plusieurs actions offensives simultanées. | validé en conception | nouveau | — |
| EN-10 | Hasard contrôlable par une graine ; ordre de traitement déterministe en dehors du hasard choisi ; tests reproductibles. | validé en conception | nouveau | — |

## 10. Interactions avec `MEC-0001`

| Règle de `MEC-0001` | Interaction avec `MEC-0002` |
|---|---|
| S1, S2 (huit directions, coût diagonal) | L'esquive suit le coût habituel de la marche (ES-08, ES-09). |
| S6, S7 (cases visibles ou explorées) | Destination d'un saut : comme S6 (SA-05). Trajet survolé : peut traverser des cases jamais explorées (SA-06), contrairement à la marche (S7). |
| S8, S9, S11 (obstacles et unités inconnus) | Même principe de révélation à la rencontre (SA-07, SA-12). |
| S10 (case occupée infranchissable) | Exceptions : la cible d'une attaque sautée (SA-04, SA-08). Le repoussement respecte S10 (RP-03). |
| Z1 (zone atteignable) | Pas de règle de zone pour les sauts ; la prévisualisation suit SA-27. |
| N3 (plusieurs niveaux) | GE-01. |
| N4 (escaliers, échelles, ascenseurs) | Hors de `MEC-0002` (PE-03). |
| N5, N6, N7, N8, N9, N10 (chutes, dégâts, caractéristiques, armure, poids) | Leur sujet passe dans `MEC-0002`. Leur texte reste dans `MEC-0001` comme historique, avec renvoi : N5 → SA-01, CH-03 ; N6 → CH-07, CH-08 ; N7 → CH-01, CH-03, CH-09 ; N8 → CH-14 à CH-17, ES-05 ; N9 → CH-17, CO-05 ; N10 → GE-07, CH-14. |
| N11 à N14 (poids et surcharge) | Le seuil de surcharge de N14 sert aussi aux chutes (CH-14). Aucun surcoût des pas de marche n'est ajouté. |
| « Capital initial et renouvellement des TU » (encore ouvert) | L'esquive pendant le tour adverse suppose des TU restantes (ES-09) ; PE-03 laisse le renouvellement hors de `MEC-0002`. |

## 11. Contradictions et écarts

### 11.1 Points imposés par le mandat (v1.1 §2.3)

| # | Points en présence | Constat | Conclusion |
|---|---|---|---|
| 1 | **N7 / DS3** | N7 (R) : « pas de dégâts pour les petites chutes ; seuil exact à décider ». Le LOT-2F la disait contredite (H01). C2 fixe maintenant un seuil (0,25 étage de hauteur équivalente, CH-09), une exemption du saut volontaire d'un étage sans surcharge (CH-01) et des dégâts dès un étage pour une chute involontaire (CH-03). N7 n'est donc plus contredite : son seuil est décidé. | Compatible. N7 reste au registre avec une annotation (diff proposé) ; H01 et E21 du LOT-2F seraient à requalifier en « précisée ». Voir aussi X12 : l'exemption ne vaut plus en cas de collision avec une unité. |
| 2 | **P05 / portée au même niveau** | P05 (M, 9 novembre) et DS2.3 (13 novembre) : 2 cases pour une descente d'un étage. C2 (SA-19) : 2 cases **au même niveau** ; en descente, plus de 2 cases. La décision la plus récente prévaut. | Écart assumé : P05 et la portée de DS2.3 sont remplacées. Les tests T-J02, T-J03, T-J04 et T-J11 du LOT-2F sont à recalculer (matrice, §4). |
| 3 | **DS5 / chutes FIFO** | DS5.1 fige le monde pendant un saut, sauf esquives et chutes provoquées ; DS5.2 et I03 demandent une résolution chronologique. EN-06 traite les chutes nées d'un même événement **l'une après l'autre**, en file FIFO stable. Le tableau de C2 (§10) décrit DS5.1 comme « chutes supposées simultanées » : DS5.1 ne le dit pas. La proposition E9 b de G (file par instant, puis identifiant) n'a pas été reprise. | Pas de contradiction avec DS5.1. **Tension** avec la chronologie physique : deux chutes de durées différentes, traitées l'une après l'autre, peuvent se croiser. EN-07 (réévaluer, annuler l'événement caduc) atténue le risque sans le régler (§12, A20). |
| 4 | **K07 / repoussement forcé** | K07 (M) : « cible immobile, aucune TU dépensée pour l'essai ». RP-01 : aucun déplacement d'esquive en cas d'échec, mais repoussement possible après l'impact. C'est la lecture que le LOT-2H marquait « à vérifier ». | **Tranché** par C2 et D2. La consolidation DS (« À VÉRIFIER »), le mandat v1.0 (§0, point 4) et le LOT-2H (§5, ligne 7) demandaient toutefois une confirmation explicite avant inscription : la preuve D2 est globale et déclarative (A27). |
| 5 | **D12 / résistance cumulative** | D12 (M) reprenait les règles de résistance du terrain d'OXCE : destruction si le dégât atteint l'armure de la partie, sans cumul (lecture du code, LOT-2F §4). EN-01 rend la résistance **cumulative**. | Écart assumé : D12 devient une adaptation de Bastion et n'est plus une référence à OXCE. L'attendu de T-D10 du LOT-2F (« seuil d'OXCE, sans accumulation ») est remplacé. |
| 6 | **Grandes unités : DS5.5** | DS5.5 : pas d'attaque sautée **par** une grande unité, ni **contre** elle. GE-08 : aucun saut volontaire pour ces unités ; chutes involontaires et collisions possibles. C2 ne redit pas l'exclusion comme **cible**, mais ne la modifie pas : selon C2 §1, une décision récente ne prévaut que si elle modifie une hypothèse ancienne. | Extension assumée côté sauteur (GE-08). Exclusion comme cible maintenue (GE-09), à confirmer (§12, A12). |
| 7 | **Coût du saut simple ou offensif** | DS5.6 : coût proportionnel à la distance de Manhattan, plus le supplément offensif. C2 : distance 3D `\|Δx\| + \|Δy\| + \|Δz\|` (SA-22) ; saut simple sans supplément (SA-23) ; attaque avec supplément (SA-24). Le tableau de C2 résume DS5.6 par « + 20 % », alors que le supplément vaut `max(1, ⌊0,20 × TU_max⌋)`, et non 20 % du coût. | Précision assumée (distance 3D) et règle nouvelle (saut simple). Formulation de C2 à corriger. Coût non entier ouvert (§12, A10). |
| 8 | **Tirages communs et arrondis** | CO-08 étend le tirage commun (DS4.5) aux deux unités d'une collision. Avec un tirage commun, le rapport des dégâts avant armure vaut `(P_i × F_i) / (P_j × F_j)` : il est fixe, et le hasard ne change plus l'ordre des blessures (G, D-E6a). Or DS4.1 dit que « le poids ne doit pas déterminer à lui seul qui est le plus blessé » et que « les tirages aléatoires continuent d'intervenir ». À armures égales ou absentes, le facteur de masse (CO-03), le plafond et le bonus désignent mécaniquement l'unité la plus blessée. Le mandat v1.0 (§2 B) demandait d'ailleurs de ne pas étendre le tirage commun aux collisions entre unités ; C2 l'étend, et D2 couvre ce choix. Arrondis : les deux arrondis de DS3.5 sont gardés, avec de nouvelles étapes (gravité, surcharge) avant le premier. | **Contradiction à arbitrer** entre CO-08 et DS4.1 (§12, A8) ; elle dépend de la lecture de DS4.1 et de K08 (G, D-E6a), à confirmer. Arrondis : principe compatible ; le détail des deux étapes et la nature du tirage restent ouverts (C2 §11.6 ; A26). |

### 11.2 Autres constats

| # | Constat | Règles | Nature | Conclusion |
|---|---|---|---|---|
| X1 | La portée en descente d'un étage, « à calculer » (SA-19), dépend du modèle de la capacité horizontale, qui n'est pas fixé. Calcul **indicatif**, si la portée de Manhattan est proportionnelle à la durée de vol (proposition A du LOT-2F §3.3, reprise par G en E2 b ; non reprise par C2) : un étage de descente donne `2 × (1 + √5)/2 ≈ 3,24`, soit 3 cases après arrondi vers le bas. | SA-15, SA-19, SA-21 | paramètre ouvert | Non validé ; à décider avec le calibrage (§12, A9). |
| X2 | Avec SA-16 appliquée aux deux composantes, la portée au même niveau d'une même unité varie comme le carré de `M_ref/M` selon sa charge. Exemple **illustratif**, avec `M_ref = 80` kg (hypothèse) : 2 cases à 80 kg, 1,28 donc 1 case à 100 kg, 0,89 donc **0 case** à 120 kg. Une unité un peu plus chargée ne pourrait plus franchir un trou d'une case. | SA-16, SA-21 | conséquence visible | À connaître avant de fixer `M_ref` et les capacités par type. |
| X3 | L'exemption CH-01 vise un saut volontaire « d'un étage ». Or la hauteur réelle d'un tel saut inclut le sommet (1,25 étage pour l'unité de référence à 1 g, soit `B = 9,5` sans exemption). Il faut préciser si « un étage » signifie un niveau d'écart, ou une hauteur. | CH-01, CH-08, CH-11 | ambiguïté | §12, A3. |
| X4 | Le seuil de 0,25 porte sur `H_eq` **avant** la pondération par `g/g0` (CH-09 à CH-11). Un saut volontaire **au même niveau** n'est pas couvert par CH-01. Il retombe donc de toute la hauteur de son sommet : 0,25 étage pour l'unité de référence à 1 g (aucun dégât), mais 0,5 étage à 0,5 g (puissance 2,67 × 0,5 = 1,33), ou environ 0,44 étage pour une unité de 60 kg avec `M_ref = 80` (puissance 2,07). Un saut au même niveau peut ainsi blesser, alors qu'un saut d'un étage plus bas ne blesse pas. À 1 g et 0,5 g, la vitesse à l'impact est pourtant la même. | CH-01, CH-09 à CH-11, SA-16 | incohérence potentielle | §12, A4. |
| X5 | CH-10 multiplie `B(H_eq)` par `g/g0`. Comme `B` n'est pas linéaire, `B(H) × g/g0` diffère de `B(H × g/g0)`. C2 signale elle-même le risque de double comptage de la gravité (C2 §11.6). | CH-07 à CH-11 | point d'application | §12, A5. |
| X6 | Surcharge et D09 : D09 (M) plaçait les facteurs de poids après le tirage. La surcharge (CH-16), facteur lié au poids, s'applique après le plafond de 70, mais **avant** le tirage (CH-13, CO-09). On ne sait pas non plus si elle s'applique dans une collision, ni où (CO-09 : « bonus de surcharge et/ou d'attaque applicables »). | CH-13, CH-16, CO-09 ; D09 | écart et ambiguïté | Écart assumé pour la place ; ambiguïté pour les collisions (§12, A6). |
| X7 | Collision contre le décor : C2 cumule `P = K_obstacles × v_n²` (CO-02) et le facteur `min(M/80, 3)` (CO-04, D10), sans dire où se place ce facteur, ni s'il y a un second arrondi. | CO-02, CO-04, CO-09 | ambiguïté | §12, A7. |
| X8 | DS5.3 disait que l'attaquant prend la case initiale de la cible repoussée. C2 (§8) ne le redit pas, mais le suppose (RP-05 ne traite que le cas où la cible ne peut pas être repoussée). | RP-02, RP-05 ; DS5.3 | règle maintenue | Maintenue (RP-09), à confirmer lors de l'inscription (§12, A18). |
| X9 | RP-06 : si la dernière position libre de l'attaquant est au-dessus de la cible, une retombée verticale la percute à nouveau, ce qui contredit « sans pénétrer la cible ». | RP-06 | ambiguïté | §12, A19. |
| X10 | Les sous-décisions N5 à N10 restent dans `MEC-0001` (PE-01), mais leur sujet passe dans `MEC-0002`. Sans règle de primauté, deux fiches parleraient des chutes. | PE-01, PE-02 ; N5 à N10 | structure du registre | Le diff proposé les annote dans `MEC-0001`, avec renvoi à `MEC-0002`, qui prévaut pour ces sujets. À confirmer. |
| X11 | Le tableau des écarts de C2 décrit des règles anciennes de façon inexacte : DS5.1 « chutes supposées simultanées » ; K05 et DS5.7 « visibilité juste avant le choc » (DS5.7 dit seulement que la cible doit voir l'unité qui tombe) ; DS5.6 « + 20 % ». | C2 §10 | traçabilité | Signalé ; la matrice cite les textes d'origine. |
| X12 | **Exemption et collision.** DS3.1 exemptait l'unité qui tombe d'un seul étage sans surcharge ; DS3.4 précisait que l'unité percutée peut être blessée « indépendamment de l'exemption qui concerne l'unité tombante ». C2 limite l'exemption au saut « sans collision avec une unité » (CH-01) et fait de la réception sur une unité une collision qui peut blesser les deux (CH-04). Un attaquant qui saute d'un étage sans surcharge et touche sa cible peut donc être blessé (plafond 60). C2 ne signale pas ce changement dans son tableau des écarts. | CH-01, CH-04 ; DS3.1, DS3.4 | écart non signalé | C2 prévaut, mais le changement est à confirmer avant inscription (§12, A25). |

## 12. Registre des ambiguïtés à trancher avant une implémentation déterministe

« Avant » indique le moment où le point doit être réglé.

| # | Ambiguïté | Règles | Avant |
|---|---|---|---|
| A1 | Valeurs géométriques : rapport case/étage, dimensions par type et posture, épaisseur des surfaces, tolérance des contacts | GE-02, GE-03, GE-05 | implémentation |
| A2 | Masses et capacités de référence par type (`M_ref`, `v_ref`, impulsions) ; masses des corps et des objets | SA-15, SA-16, GE-06 | implémentation |
| A3 | Sens de « un étage » dans l'exemption CH-01 : niveau d'écart ou hauteur réelle | CH-01, CH-08 | inscription (texte) |
| A4 | Seuil de 0,25 : avant ou après `g/g0` ; exemption, ou non, des sauts volontaires au même niveau | CH-09 à CH-11 ; §11.2 X4 | inscription |
| A5 | Point d'application de `g/g0` : sur `B(H_eq)` ou sur la hauteur | CH-10 | implémentation |
| A6 | La surcharge s'applique-t-elle aux collisions, et où ; interaction des plafonds 60, 70, 80 avec la surcharge et le bonus | CH-13, CO-09 | implémentation |
| A7 | Place de `min(M/80, 3)` contre le décor, et second arrondi | CO-02, CO-04 | implémentation |
| A8 | **Tirage commun entre deux unités contre DS4.1** : accepter que seule l'armure départage, ou garder une part de hasard propre à chaque unité | CO-03, CO-08 ; DS4.1 | **inscription** |
| A9 | Modèle et calibrage de la capacité horizontale ; valeur de la portée en descente | SA-15, SA-19, SA-21 | implémentation |
| A10 | Coût en TU non entier (`C_saut` fractionnaire) | SA-23, SA-24 | implémentation |
| A11 | Plage de gravité par type ; très faible gravité | SA-17 | implémentation |
| A12 | Confirmer le maintien de DS5.5 : une grande unité ne peut pas être la **cible** d'une attaque sautée | GE-09 ; DS5.5 | inscription |
| A13 | Modèle Force → capacité de portage en kg ; cohérence avec la pénalité de TU de N14 | GE-07, CH-14 | implémentation |
| A14 | `K_unités`, `K_obstacles` ; absorption d'énergie des planchers ; conversion de la résistance en énergie | CO-02, CH-21, EN-01 | implémentation |
| A15 | Instant où l'unité « voit » la menace (début d'une chute involontaire, corps dissimulés, plusieurs cibles) | ES-02, ES-03 | implémentation |
| A16 | `n` pour un impact à hauteur intermédiaire ; `P` non entier ; pénalité d'étourdissement sur les Réactions | ES-04 à ES-06, CO-07 | implémentation |
| A17 | Algorithme des esquives en conflit (« combinaison qui maximise ») : définition, départage, coût de calcul | ES-12 | implémentation |
| A18 | Confirmer le maintien de DS5.3 : l'attaquant prend la case de la cible repoussée | RP-09 ; DS5.3 | inscription |
| A19 | Issue de la retombée verticale de RP-06 quand la dernière position libre est au-dessus de la cible | RP-06 | implémentation |
| A20 | Ordre FIFO des chutes et chronologie physique (DS5.2, I03) : chutes qui se croisent ; clé d'ordre stable | EN-06, EN-07 ; DS5.2 | implémentation (le principe FIFO est décidé par C2) |
| A21 | Protections d'armure par zone et direction ; coefficients santé et étourdissement ; sensibilités par type | CO-05 à CO-07 | implémentation |
| A22 | Propriétés et résistances initiales des décors ; unité des dégâts du terrain | EN-01 | implémentation |
| A23 | Emplacement des cadavres ; collisions imbriquées et multi-cibles ; nombre maximal d'événements en chaîne | EN-08, CO-11, RP-06 | implémentation |
| A24 | Règle de primauté entre `MEC-0001` (N5 à N10) et `MEC-0002` | PE-01, PE-02 | inscription |
| A25 | Confirmer que l'unité qui tombe d'un étage sans surcharge **sur une unité** n'est plus exemptée (C2 restreint DS3.1 et DS3.4) | CH-01, CH-04 | inscription |
| A26 | Nature du tirage de 50 à 150 % (entier ou réel, bornes, loi) et normalisation ; détail des deux arrondis ; limites numériques éventuelles (C2 §11.5, §11.6) | CO-08, CO-09 | implémentation |
| A27 | Confirmation explicite de la lecture de K07 : aucun déplacement d'esquive en cas d'échec, puis repoussement possible après l'impact | RP-01 ; K07 ; DS5.3 | inscription |
| A28 | Vitesse après un choc qui interrompt le saut : chute verticale depuis le contact (D13) et hauteur équivalente avec `v0` (CH-11) ; vitesse résiduelle après la traversée d'une surface (CH-21) | CH-06, CH-11, CH-21 | implémentation |

Les sujets marqués « inscription » (A3, A4, A8, A12, A18, A24, A25, A27) touchent le texte même de la fiche. Les autres peuvent rester ouverts dans une inscription partielle, comme le prévoit C2 (§11, dernière phrase).

## 13. Limites de traçabilité

- **Numérotation absente** : C2 ne liste ni les 29 propositions ni les réponses 1A à 6A, et ne cite qu'une seule fois un numéro (« proposition 8/29 », GE-08). Aucune règle ne peut donc être rattachée à une proposition ou à une réponse précise. Si C2 résume mal une proposition, ce lot ne peut pas le détecter.
- **Preuve déclarative** : D2 confirme l'acceptation des 29 propositions et des six arbitrages, avec la précision sur les esquives. Elle ne dit pas que **tout** le texte de C2 a été relu et accepté mot pour mot. Les règles de C2 qui reprennent des décisions antérieures (M, P, DS) gardent aussi leur preuve d'origine.
- **Messages d'origine** : la conversation du 14 novembre n'a pas été fournie ; aucune comparaison n'a été faite avec elle.
- **Copie de C2** : rien ne prouve que la version publiée au commit `d028c52` est identique au « document local remis au propriétaire » dont parle le mandat v1.1 (§1) ; le propriétaire l'a désignée comme le document à lire.
- **Copie des messages** : le mandat v1.1 (§1) demande une copie approuvée des messages d'arbitrage si Claude Code n'y a pas accès. Elle n'a pas été fournie ; D2 en tient lieu, de façon déclarative.
- **Auteur** : C2 a été écrite par l'orchestrateur. Elle est traitée comme une transcription à vérifier, non comme une source infaillible (mandat v1.1 §1). Ses inexactitudes sur l'historique sont relevées au §11.2 (X11).
- **Mandat v1.0** : il reste une archive sur `orchestration/mandats`. Sa demande d'une « tranche de développement initiale » de `MEC-0001` ne fait pas partie du périmètre v1.1, et n'est pas traitée ici.
