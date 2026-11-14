# LOT-2I — Diff proposé du registre : `MEC-0001` annotée et nouvelle fiche `MEC-0002`

> **PROPOSITION DOCUMENTAIRE — NON APPLIQUÉE.** Rien de ce document n'est écrit dans `docs/gameplay/GAMEPLAY-DECISIONS.md`. Une inscription exigera une autorisation distincte du propriétaire et un mandat d'écriture du registre. **Aucune implémentation n'est autorisée**, même après une inscription : les deux fiches resteraient « reportées ».

| | |
|---|---|
| Base | Registre sur `origin/main` = `74faa2974da7a4645725b4271eb66ae2a512e98a` ; objet Git `a72df450…`, SHA-256 `c2a3a55e7b1ed3d08089b5d814cded324b94313792982c8556d0e9d19a7e3968`. Lu, **non modifié**. |
| Contenu | Les règles de `MEC-0002` reprennent mot pour mot la colonne « Règle » de `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md`, générées depuis ce fichier. Seules les abréviations propres au LOT-2I (« C2 », « D2 », « G ») y sont écrites en toutes lettres. |
| Remplace | La proposition du LOT-2H (`docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md`), qui mettait DS1 à DS5 dans `MEC-0001`. Elle n'a pas été appliquée ; ses principes deviennent des sources de `MEC-0002`. |

## 0. Lecture rapide

**Ce qu'une écriture future changerait au registre** (diff exact au §3) :
1. la phrase d'introduction : « Deux fiches sont enregistrées » ;
2. `MEC-0001` :
   - son bandeau renvoie les sauts, chutes, collisions, esquives et repoussements à `MEC-0002` ;
   - le champ « Éléments exclus » les exclut ;
   - N7 reçoit une annotation, sans réécriture ;
   - une annotation sous N10 dit que N5 à N10 sont précisées par `MEC-0002` ;
   - la ligne « Chutes » de « Encore ouvert » garde ses quatre sous-points et en reçoit un cinquième, qui renvoie à `MEC-0002` ;
3. une nouvelle fiche `MEC-0002 — Sauts, chutes et collisions`, avec :
   - les champs du gabarit ;
   - **« Décision du propriétaire : reportée »** ;
   - les 105 principes PE-01 à EN-10 ;
   - les décisions antérieures remplacées ou modifiées ;
   - sa liste « Encore ouvert ».

**Ce qui n'est pas modifié** : la classe (`MODIFICATION-PROPOSEE`), l'état (« non commencé ») et le périmètre (« aucun changement de gameplay ») de `MEC-0001` ; le texte de S1 à S12, Z1 et N1 à N14 ; les champs « Décision du propriétaire » de `MEC-0001`.

**Huit principes portent la mention « à confirmer avant inscription définitive »** :
- PE-01 (A24 : primauté entre `MEC-0001` et `MEC-0002`) ;
- GE-09 (A12 : maintien de DS5.5, grande unité non ciblée) ;
- CH-01 (A3 : sens de « un étage ») ;
- CH-04 (A25 : fin de l'exemption d'un étage en cas de collision avec une unité) ;
- CH-09 (A4 : seuil de 0,25 et gravité) ;
- CO-08 (A8 : tirage commun contre DS4.1) ;
- RP-01 (A27 : confirmation explicite de la lecture de K07) ;
- RP-09 (A18 : maintien de DS5.3, l'attaquant prend la case de la cible).

Les autres ouvertures figurent dans la liste « Encore ouvert » de la fiche.

## 1. Modifications de `MEC-0001`

| # | Emplacement | Aujourd'hui | Proposition |
|---|---|---|---|
| 1 | Introduction du registre | « Une seule fiche est enregistrée : `MEC-0001` » | « Deux fiches sont enregistrées : `MEC-0001` et `MEC-0002` », proposées et incomplètes |
| 2 | Bandeau de `MEC-0001` | Sous-décisions S1 à S12, Z1, N1 à N14 | Ajoute : « Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`. » |
| 3 | Éléments exclus | Ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | Ajoute les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002` |
| 4 | N7 | « Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] » | Texte gardé ; annotation : précisée par CH-01, CH-03 et CH-09, avec leurs réserves |
| 5 | Sous N10 | — | Annotation : N5 à N10 précisées par `MEC-0002` ; texte conservé. La primauté entre les deux fiches reste à confirmer (A24) |
| 6 | Encore ouvert : chutes | Quatre sous-points sur les chutes | Les quatre sous-points sont gardés ; un cinquième renvoie à `MEC-0002` |

## 2. Texte proposé de la fiche `MEC-0002`

À ajouter à la fin du registre, après `MEC-0001`. **Non inscrit.**

### MEC-0002 — Sauts, chutes et collisions

**Fiche de conception incomplète. Des principes de conception sont acceptés (PE-01 à EN-10, du 14 novembre 2026, sauf GE-09 et RP-09, du 13 novembre 2026), dont huit restent à confirmer avant une inscription définitive, mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**

| Champ | Valeur |
|---|---|
| Système | Combat tactique : sauts simples et attaques sautées, chutes volontaires et involontaires, trajectoire balistique, collisions, réception, esquives réactives, repoussements, destruction sous impact et chaîne d'événements associée. |
| Description | Une unité peut sauter vers une case admissible, tomber, heurter des unités ou le décor, esquiver une unité qui tombe ou être repoussée. Règles partielles ci-dessous. |
| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** ; aucun calcul de dégâts de chute n'y a été identifié (`docs/reviews/LOT-2E-VERTICALITE-OXCE.md`, C8). Les règles ci-dessous sont des adaptations de Bastion, sans reprise de code, de données ni d'assets (D4). Spécification : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Arbitrage : `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. Principes DS1 à DS5 : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`. Consolidation : `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` et `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`. |
| Changement demandé | Fixer les sauts, chutes et collisions de Bastion à partir des principes PE-01 à EN-10 ci-dessous. Les points encore ouverts sont listés plus bas. |
| Décision du propriétaire | reportée — inscription partielle des principes de conception. Principes acceptés le 14 novembre 2026 : 29 propositions et arbitrages complémentaires 1A à 6A, consolidés dans `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` (branche `orchestration/mandats`, commit `d028c52f500ed8daeca917adbcb9a9e1eb3ff8bd`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`). Preuve : déclaration du propriétaire du 14 novembre 2026 (preuve déclarative), qui précise que les esquives sont des tentatives automatiques dont la réussite dépend d'un tirage et des Réactions. GE-09 et RP-09 reprennent DS5.5 et DS5.3 (13 novembre 2026), que la consolidation ne modifie pas. Ces principes reprennent ou modifient les décisions du 9 novembre 2026 et le correctif du propriétaire (identifiants du LOT-2F), ainsi que les principes DS1 à DS5 du 13 novembre 2026. |
| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
| Éléments exclus | Tous les points listés sous « Encore ouvert » ; escaliers, échelles et ascenseurs ; règles générales du brouillard ; renouvellement des TU ; stabilité structurelle des bâtiments ; toute autre mécanique (tir, explosion, destruction de cadavre, vol, apesanteur). |
| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` §3). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
| Tests de modification | Critères futurs seulement. Aucun test écrit ni exécuté. |
| État d'implémentation | non commencé |

#### Principes de conception acceptés le 14 novembre 2026

Ils n'autorisent, seuls, aucun gameplay. Les identifiants PE, GE, SA, CH, CO, ES, RP et EN ont été proposés par le LOT-2I. Entre crochets, la décision antérieure reprise, précisée ou modifiée. S, Z et N renvoient à `MEC-0001` (R : registre). Les autres identifiants (J, K, D, I, P, E) renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` (M : décision du 9 novembre 2026 ; P : correctif du propriétaire). DS*n*.*m* renvoie à la consolidation DS1 à DS5 du 13 novembre 2026. « Ouvert » nomme le paramètre qui reste à fixer. « À confirmer avant inscription définitive » : principe accepté dont le texte attend une confirmation du propriétaire.

- **Périmètre**
  - **PE-01** — `MEC-0001` garde la marche ordinaire : cheminement, coûts de terrain, diagonales, visibilité du trajet, TU du déplacement ordinaire. Elle conserve S1 à S12, Z1 et N1 à N14, avec une annotation historique de N7, sous réserve d'autorisation d'inscription. [Rattachement de la fiche (LOT-2H, §5 ligne 12).] Ouvert : primauté entre les deux fiches (A24). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A24).
  - **PE-02** — `MEC-0002` couvre le saut simple, l'attaque sautée, les chutes volontaires et involontaires, la trajectoire, les contacts et collisions, la réception, l'esquive réactive, le repoussement, l'impact des corps, la destruction sous impact et la chaîne d'événements associée.
  - **PE-03** — Hors de `MEC-0002` : escaliers, échelles, ascenseurs, règles générales du brouillard, renouvellement global des TU, stabilité structurelle des bâtiments.
  - **PE-04** — Décrire une règle physique utilisable ailleurs n'autorise pas d'autres mécaniques (tir, explosion, destruction de cadavre, vol, apesanteur, etc.).

- **Géométrie, masse et posture**
  - **GE-01** — Positions `(x, y, z)`, plusieurs niveaux. [N3 (R).]
  - **GE-02** — Largeur de case, hauteur d'étage et volumes des unités en proportions, sans mètres pour la grille. [DS1.1.] Ouvert : rapports exacts.
  - **GE-03** — Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. [DS1.2 ; postures : nouveau.] Ouvert : dimensions par type et posture.
  - **GE-04** — Pendant le vol, posture et orientation du volume sont conservées : pas de rotation des pavés, pas de changement de posture. [nouveau.]
  - **GE-05** — Un contact de surfaces suffit à détecter la rencontre. Sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés, sans créer d'énergie ni dédoubler un impact. [D11 ; contacts : nouveau.] Ouvert : tolérance numérique.
  - **GE-06** — La masse physique totale `M` comprend le corps, l'armure, l'équipement et l'inventaire, en kg. [E23 (P).] Ouvert : masses par type et par objet.
  - **GE-07** — La charge portée, pour la surcharge, comprend l'armure, l'équipement et l'inventaire, en kg ; elle est distincte de `M`. La Force se traduit en capacité de portage en kg, selon un modèle à définir. [N10, N14 (R) ; E20 (LOT-2F).] Ouvert : modèle Force → capacité.
  - **GE-08** — Les unités de plusieurs cases peuvent subir des chutes involontaires et des collisions. Leurs sauts volontaires sont provisoirement indisponibles (« proposition 8/29 »). [étend DS5.5, qui excluait l'attaque sautée faite par ces unités et contre elles.]
  - **GE-09** — Une unité de plusieurs cases n'est pas choisie comme cible d'une attaque sautée. **Maintenue de DS5.5** : la consolidation du 14 novembre ne la redit pas, mais ne la modifie pas. [DS5.5.] Ouvert : confirmation (A12). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A12).

- **Sauts**
  - **SA-01** — Saut simple vers une destination admissible au même niveau ou plus bas ; il permet de franchir une ouverture ou un obstacle. Un saut vers une zone sans support immédiat est permis : l'unité continue de tomber jusqu'à un support ou un contact. [nouveau ; N5 (R).]
  - **SA-02** — L'attaque sautée n'est possible que si la cible est au moins un étage plus bas. [J01 (M).]
  - **SA-03** — Un allié ou un neutre déjà identifié ne peut pas être ciblé intentionnellement. [J06 (M).]
  - **SA-04** — Un ennemi actuellement visible peut être ciblé malgré S10. [J13, E14 (P) ; DS1.4.]
  - **SA-05** — Destination visible ou déjà explorée ; jamais explorée : interdite. [J03, J04 (M) ; S6 (R).]
  - **SA-06** — Les cases survolées peuvent n'avoir jamais été explorées. [tranche E15 (LOT-2F).]
  - **SA-07** — Obstacles et unités cachés ne sont révélés qu'à leur rencontre. [P08, I01 (M) ; DS5.2.]
  - **SA-08** — Un ennemi caché, ou un allié ou neutre caché, sur la case attaquée peut être percuté, avec le bonus d'attaque sautée même s'il était allié ou neutre. [J05, J07, J08 (M).]
  - **SA-09** — Un saut simple qui percute par accident une unité cachée : collision et dégâts possibles, **sans** bonus × 1,25. [nouveau ; D08 (M).]
  - **SA-10** — Arc balistique continu, sans contournement des obstacles. Seule une destination à portée de Manhattan est permise ; la trajectoire réelle est ensuite vérifiée avec les volumes. [P07 (M) ; DS1.2.]
  - **SA-11** — Le sol de la case de départ est ignoré au décollage, sans étendre cette exception aux autres surfaces. [DS1.3.]
  - **SA-12** — Obstacle connu sur la trajectoire : engagement interdit, sauf pour les cibles offensives permises. Obstacle inconnu : saut engagé, puis collision, arrêt et révélation à l'impact. [P08 (M).]
  - **SA-13** — En vol : aucune modification volontaire de destination ni d'impulsion ; vitesse horizontale constante tant qu'aucun contact ne la modifie ; fin de l'action à une réception stable, sans glissement automatique. [nouveau.]
  - **SA-14** — Le saut s'arrête au premier choc ; la collision et les chutes qui suivent sont des événements distincts, résolus dans l'ordre chronologique. [DS5.2 ; D13 (M).]
  - **SA-15** — Chaque type d'unité a une impulsion verticale et une capacité d'impulsion horizontale distinctes et configurables. [P02, P03 (M).] Ouvert : valeurs par type.
  - **SA-16** — Loi : impulsion constante à effort égal. Pour une unité donnée et des conditions comparables, la vitesse initiale varie en raison inverse de sa masse totale, `v = v_ref × (M_ref/M)`. À gravité constante, la hauteur varie comme le carré du rapport des masses ; la portée diminue aussi quand la masse augmente. [DS2.1 ; tranche E11 (quantité de mouvement) ; écarte la recommandation E11 du LOT-2G.] Ouvert : `M_ref`, `v_ref` par type.
  - **SA-17** — La gravité influe sur la durée de vol, la hauteur et la portée. Chaque type d'unité a sa plage de gravité où il peut sauter. [P01 (M) ; DS2.4 (plage par type au lieu d'une plage unique).] Ouvert : bornes.
  - **SA-18** — Aucun saut balistique à 0 g ; l'apesanteur est hors périmètre. Une chute involontaire reste possible en gravité positive, même quand les sauts sont interdits. Une gravité négative est invalide. [DS2.4 ; E3 (LOT-2F).]
  - **SA-19** — Référence à 1 g, pour l'unité de référence : sommet à un quart d'étage ; portée de 2 cases de Manhattan **au même niveau**, pour franchir un trou d'une case ; portée pour un étage de descente **supérieure à 2 cases**, valeur à calculer. [P04 (M) inchangée ; **remplace** P05 (M) et la portée de DS2.3.] Ouvert : valeur de la portée en descente.
  - **SA-20** — À capacités égales, un saut au même niveau a une durée de vol et une portée inférieures à un saut avec un étage de descente. [conséquence de SA-16 à SA-19.]
  - **SA-21** — Portée horizontale `|Δx| + |Δy|`, plafond entier arrondi vers le bas. Aucune portée minimale garantie quand le calcul donne moins d'une case. [P05 (M) ; DS2.2 ; tranche la conversion de E2.]
  - **SA-22** — Distance pour les TU : `d_3D = |Δx| + |Δy| + |Δz|`, distincte de la portée horizontale. [précise DS5.6 (« distance de Manhattan »).]
  - **SA-23** — `TU_simple = d_3D × C_saut`. [nouveau.] Ouvert : `C_saut` ; coût non entier.
  - **SA-24** — `TU_attaque = d_3D × C_saut + max(1, ⌊0,20 × TU_max⌋)`. [J09 (M) ; DS5.6.] Ouvert : `C_saut` ; coût non entier.
  - **SA-25** — `C_saut` est propre aux sauts, indépendant de la marche ; sa valeur est explicitement reportée à l'équilibrage. [E13 (LOT-2F).] Ouvert : valeur.
  - **SA-26** — Coût payé en entier à l'engagement, même si le saut est interrompu ou si la cible esquive ; aucun remboursement. Une chute passive qui suit la destination choisie ne coûte pas de TU en plus. [J09 (M) ; DS5.6.]
  - **SA-27** — Une action sans TU suffisantes est interdite. Destination, coût et trajectoire sont prévisualisés dans les limites des informations connues. [J10, I02 (M).]

- **Chutes et réception**
  - **CH-01** — Un saut volontaire (simple ou offensif) d'**un étage**, sans surcharge et sans collision avec une unité, n'inflige pas de dégâts de chute. [précise DS3.1 (« volontaire ») ; N7 (R).] Ouvert : définition de « un étage ». **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A3).
  - **CH-02** — En surcharge, un saut volontaire d'un étage peut produire des dégâts. [DS3.1, DS3.2.]
  - **CH-03** — Une chute **involontaire** peut blesser dès un étage, même sans surcharge, qu'elle soit prévue ou subie par surprise. [D01 (M) ; restreint l'exemption de DS3.1.]
  - **CH-04** — Une réception sur une unité est une collision, qui peut blesser les deux unités, distincte d'une chute au sol. Le bonus offensif ne vaut que pour l'attaque sautée. [DS3.4 ; K01, K02, D08 (M) ; **restreint** DS3.1 : l'unité qui tombe d'un étage sans surcharge sur une unité n'est plus exemptée.] Ouvert : changement de DS3.1 à confirmer (A25). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A25).
  - **CH-05** — Si la cible esquive, l'attaquant finit son saut au sol : ce saut reste **volontaire**, et l'exemption d'un étage sans surcharge s'applique. [E18 (P) ; DS3.1.]
  - **CH-06** — Si un obstacle interrompt la trajectoire puis provoque une nouvelle chute, cette chute est **involontaire** ; collision et chute sont comptées séparément. [D13 (M).]
  - **CH-07** — La puissance de référence d'une chute au sol reste celle du LOT-2F : `B(1) = 8`, `B(2) = 14`, `B(3) = 22,1`, `B(4) = 33,035`, incréments de + 6 puis × 1,35. [D03, D04 (M).]
  - **CH-08** — Hauteur réelle de chute, fractions d'étage comprises ; interpolation linéaire entre les points de référence. [nouveau ; tranche le comptage de E12 pour les dégâts.]
  - **CH-09** — Hauteur équivalente ≤ 0,25 étage : aucun dégât. Entre 0,25 et 1 étage : interpolation de `(0,25 ; 0)` à `(1 ; 8)`. [précise N7 (R) ; tranche « moins d'un étage » (DS3).] Ouvert : portée du seuil selon la gravité. **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A4).
  - **CH-10** — En gravité positive, la puissance de référence est multipliée par `g/g0`, avec `g0 = 1 g` ; la précision décimale est gardée jusqu'aux arrondis prévus. [**modifie** D03, qui ne dépendait pas de la gravité.] Ouvert : point d'application.
  - **CH-11** — Vitesse verticale initiale descendante : hauteur équivalente `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 0,25 porte sur `H_eq`. Vitesse initiale montante : la montée, le sommet et la descente sont résolus physiquement, avec la vitesse réelle à l'impact. [nouveau.]
  - **CH-12** — Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse verticale ; la vitesse horizontale compte contre les surfaces qui lui sont normales. [D11 (M).]
  - **CH-13** — Plafond de puissance de base 70 pour une chute au sol, **avant** le multiplicateur de surcharge, qui peut porter la puissance au-delà de 70 avant le tirage. Les plafonds 60 (unité qui tombe), 80 (cible percutée) et 70 (obstacle) restent pour leurs domaines, sous réserve d'une vérification de la chaîne. [D05 (M) ; déroge à D09 (M), qui plaçait les facteurs de poids après le tirage.] Ouvert : vérification de la chaîne.
  - **CH-14** — Capacité de portage en kg selon la Force ; seuil de surcharge commun à N14. [DS3.2 ; N14 (R).] Ouvert : modèle Force → kg.
  - **CH-15** — Dépassement relatif `S = max(0, charge / capacité − 1)`, avec une capacité strictement positive. [nouveau.]
  - **CH-16** — Multiplicateur `F_surcharge = min(2, 1 + 0,5 × S)`. [nouveau ; tranche E24 pour le poids au sol.]
  - **CH-17** — Ce multiplicateur aggrave la puissance utilisée pour les blessures et pour l'étourdissement ; l'armure applique ensuite ses protections. [N9, N10 (R).]
  - **CH-18** — La surcharge ne supprime pas le seuil de 0,25 étage. [nouveau.]
  - **CH-19** — La nature du sol ne modifie pas directement les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol. [D02 (M).]
  - **CH-20** — L'impact peut endommager ou détruire le support ; s'il cède, la chute continue. Chaque impact successif est résolu à part, et les dommages corporels peuvent s'additionner. [D12, D13 (M).]
  - **CH-21** — Traverser une surface destructible absorbe de l'énergie et ralentit le corps ; la gravité peut ensuite le réaccélérer. [nouveau.] Ouvert : formule de perte d'énergie.

- **Collisions et dégâts**
  - **CO-01** — Détection des contacts sur les volumes réels au moment du contact, y compris après un déplacement d'esquive ou une perte de support. [DS1.2.]
  - **CO-02** — Puissance de base `P = K × v_n²`, où `v_n` est la composante normale de la vitesse relative au contact (entre deux unités, ou contre une surface fixe). Deux coefficients distincts et configurables : `K_unités` et `K_obstacles`. [étend DS4.2 aux collisions entre unités ; D10 (M).] Ouvert : `K_unités`, `K_obstacles`.
  - **CO-03** — Entre unités, facteur appliqué aux dégâts reçus par chacune : `F_i = clamp(√(M_autre/M_i), 0,75 ; 1,5)`, masses strictement positives. [DS4.1 ; K08 (M) ; formule E6 du LOT-2G non reprise.] Ouvert : interaction avec le tirage commun.
  - **CO-04** — Contre le décor : référence du LOT-2F `min(M/80, 3)` pour le facteur de masse, et plafond de 70. Le point d'insertion de ce facteur dans la nouvelle chaîne reste à revoir. [D10, D05 (M).] Ouvert : point d'insertion.
  - **CO-05** — Type de dégâts « impact » propre à Bastion : zones corporelles exposées et protections d'armure liées à la direction du choc, sans recopier de code ni de données d'OXCE. [DS4.4 ; D07 (LOT-2F, ouverte : E7).] Ouvert : protections par zone.
  - **CO-06** — Blessures et étourdissement sont des effets séparés ; une armure peut protéger plus la santé que l'étourdissement ; on peut être étourdi sans perdre de santé. [K02 (M).] Ouvert : coefficients santé / étourdissement.
  - **CO-07** — Chaque type d'unité a une sensibilité à l'étourdissement ; 0 vaut immunité aux étourdissements d'impact. Une unité consciente mais étourdie peut encore tenter une esquive, avec des Réactions réduites. [nouveau.] Ouvert : pénalité sur les Réactions.
  - **CO-08** — Tirage d'intensité de 50 à 150 %, **une fois par événement de collision**, partagé par les deux unités d'une collision entre unités, ou par l'unité et l'obstacle. Résistances et effets s'appliquent ensuite à chacun. Des collisions réellement distinctes, même rapprochées, ont des tirages distincts. [D06 (M) ; **étend** DS4.5 aux collisions entre unités.] Ouvert : conflit avec DS4.1 (A8) ; nature et normalisation du tirage (A26). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A8).
  - **CO-09** — Ordre : puissance initiale ; facteur de gravité s'il s'applique ; plafond de base ; bonus de surcharge et/ou d'attaque applicables ; arrondi au plus proche, moitié vers le haut ; tirage ; facteur de masse s'il s'applique ; second arrondi ; puis effets et protections séparés pour la santé et l'étourdissement. Les termes D09 et D10 sont à réconcilier, sans double comptage. [DS3.5 ; D10 (M) ; déroge à D09 (M) : la surcharge, facteur lié au poids, précède le tirage.] Ouvert : réconciliation ; détail des deux arrondis et du tirage (A26).
  - **CO-10** — Bonus × 1,25 uniquement sur les dégâts infligés à la cible d'une attaque sautée, après le plafond et avant le tirage ; jamais pour l'attaquant. Une cible alliée ou neutre cachée le reçoit aussi. [J08, J11, J12, D08 (M).]
  - **CO-11** — Contacts simultanés d'un même choc : les surfaces peuvent être endommagées, sans dupliquer la puissance corporelle. Contre plusieurs unités distinctes : un calcul par cible, regroupé au besoin dans un même événement. [nouveau.] Ouvert : détails d'implémentation.

- **Esquives réactives**
  - **ES-01** — Le moteur déclenche la tentative tout seul, sans le joueur ; la réussite n'est pas automatique : elle dépend d'un tirage et des Réactions. [K03, K05 (M) ; DS5.7 ; précision du propriétaire du 14 novembre 2026.]
  - **ES-02** — Conditions : menace vue **juste avant l'impact**, TU suffisantes, case admissible. Une unité qui découvre la menace pendant la chute peut tenter l'esquive. [K03 (M) ; DS5.7.] Ouvert : instant exact.
  - **ES-03** — Bonus de + 10 points si l'unité menacée voyait la menace **dès le départ** du saut ou dès le début d'une chute involontaire ; sinon 0. Même logique pour les corps qui tombent, selon ce que perçoit la cible. [nouveau.]
  - **ES-04** — Bonus de + 5 points par étage, `n = |z_départ − z_arrivée|`, pour une menace qui descend. [K05 (M).] Ouvert : `n` pour un impact à hauteur intermédiaire.
  - **ES-05** — `P = clamp(R_effectif + B_visibilité + 5n, 0, 100)` %, où `R_effectif` est la valeur des Réactions après une éventuelle pénalité d'étourdissement. [K05 (M) ; DS5.7.] Ouvert : pénalité d'étourdissement.
  - **ES-06** — Tirage entier uniforme `t` dans {1, …, 100} ; réussite si `t ≤ P`. [nouveau ; LOT-2G (E12 e) non repris.] Ouvert : `P` non entier.
  - **ES-07** — Une unité inconsciente ou morte n'esquive pas ; les corps qui tombent peuvent, eux, être esquivés. [nouveau.]
  - **ES-08** — Déplacement vers l'une des 8 cases voisines du même niveau, diagonales comprises, avec un support valide ; pas de saut dans le vide en esquivant. [DS5.7.]
  - **ES-09** — Coût habituel de la marche vers la case choisie (terrain, facteur diagonal), payé avec les TU restantes, même pendant le tour adverse. [DS5.7 ; S2 (R).] Ouvert : coûts de terrain (`MEC-0001`).
  - **ES-10** — Esquive réussie et effectivement faite : TU débitées. Échec du tirage ou déplacement impossible : aucun débit. [K06, K07 (M).]
  - **ES-11** — Choix aléatoire uniforme parmi les destinations admissibles. Une information cachée ne permet pas de choisir une case. La découverte d'un obstacle bloque et révèle la tentative, sans débit de TU. [K04 (M) ; tranche E22 (loi uniforme).]
  - **ES-12** — Pas d'échange simultané de cases ni de volumes qui se traversent ; destination libre au début de la résolution. Esquives en conflit : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager au hasard les combinaisons équivalentes. [nouveau.] Ouvert : algorithme.
  - **ES-13** — Plusieurs menaces visibles et simultanées sur une même unité dans un même événement : une seule tentative ; la case doit éviter toutes les menaces **connues** ; `n` vient de la menace visible qui tombe du plus d'étages. Les menaces cachées ne comptent pas dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée. [nouveau.]
  - **ES-14** — Dangers successifs : nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte suit le moteur séquentiel. [nouveau.]

- **Repoussement et retombées**
  - **RP-01** — Esquive réussie : déplacement volontaire, pas de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un repoussement **après** l'impact. [**tranche** le point « à vérifier » K07 (M) / DS5.3.] Ouvert : confirmation explicite demandée par la consolidation DS (A27). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A27).
  - **RP-02** — Cible touchée : repoussement en priorité dans la direction de l'impact, sinon vers les directions voisines les plus proches, égalités tirées au hasard. Une case au-dessus du vide est admissible pour un repoussement forcé et entraîne une chute involontaire. [précise DS5.3.]
  - **RP-03** — Une case occupée par une autre unité n'est pas admissible : pas de repoussement en chaîne. [S10 (R).]
  - **RP-04** — Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort garde sa masse et son volume. [tranche « cible hors de combat » (DS5).]
  - **RP-05** — Si la cible ne peut pas être repoussée, l'attaquant cherche une case adjacente (8 voisines) pour retomber, en priorité du côté d'où il vient, puis par proximité de direction ; pas de recherche au-delà. [précise DS5.4 (rayon : cases adjacentes).]
  - **RP-06** — Impossibilité entièrement connue avant l'engagement : l'attaque sautée est refusée, sans révéler de données cachées. Impossibilité révélée en vol : l'attaquant s'arrête au contact, puis retombe verticalement depuis sa dernière position libre, sans pénétrer la cible. [nouveau.] Ouvert : issue de la retombée.
  - **RP-07** — Une collision accidentelle, un cadavre ou un corps inconscient peut repousser ; aucune intention n'est requise, et aucun bonus offensif n'est créé. [nouveau.]
  - **RP-08** — Plusieurs impacts vraiment simultanés : la direction du repoussement combine intensités et directions ; cela n'introduit pas d'attaques volontaires simultanées. [nouveau.]
  - **RP-09** — Après le repoussement de la cible, l'attaquant prend la case initiale de la cible. **Maintenue de DS5.3** : la consolidation du 14 novembre ne la redit pas, mais la suppose (RP-05). [DS5.3.] Ouvert : confirmation (A18). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A18).

- **Environnement destructible et événements**
  - **EN-01** — Murs, portes, planchers et autres décors destructibles ont des points de résistance **cumulatifs** : les dégâts successifs les réduisent. Les éléments indestructibles restent intacts. [**modifie** D12 (M), qui suivait le seuil sans cumul d'OXCE.] Ouvert : résistances, unité des dégâts du terrain.
  - **EN-02** — Tant que leur résistance reste strictement positive, les éléments gardent leur blocage et leurs collisions ; l'apparence peut changer, sans fissure fonctionnelle automatique. [nouveau.]
  - **EN-03** — À zéro : destruction immédiate ; perte de support et chutes immédiates. Pas d'effondrement automatique des éléments voisins. [D12 (M) ; PE-03.]
  - **EN-04** — Un même événement qui produit plusieurs impacts simultanés sur un même plancher additionne leurs dégâts avant de décider de la destruction ; à distinguer de chutes successives. [nouveau.]
  - **EN-05** — Tour par tour : une action offensive volontaire est résolue jusqu'au bout avant l'action de combat suivante. [DS5.1.]
  - **EN-06** — Si plusieurs unités perdent leur support à cause d'un même événement, leurs chutes sont traitées **l'une après l'autre**, dans un ordre stable (par exemple les identifiants internes), en file FIFO ; les nouvelles chutes passent après celles qui attendent. [précise DS5.1 et DS5.2 ; I03 (M).] Ouvert : clé d'ordre ; articulation avec la chronologie.
  - **EN-07** — À chaque traitement : réévaluer positions, vitesses, santé et supports ; annuler un événement devenu caduc ; un seul événement de chute en attente par unité. [nouveau.]
  - **EN-08** — Les corps morts ou inconscients peuvent tomber, heurter d'autres unités et provoquer dégâts, étourdissement ou repoussement. Un cadavre ne subit plus de pertes de santé ni d'étourdissement ; la destruction des corps est hors périmètre. [nouveau.]
  - **EN-09** — Les collisions d'un même événement peuvent toucher plusieurs surfaces ou cibles, sans réintroduire plusieurs actions offensives simultanées. [nouveau.]
  - **EN-10** — Hasard contrôlable par une graine ; ordre de traitement déterministe en dehors du hasard choisi ; tests reproductibles. [nouveau.]

#### Décisions antérieures remplacées ou modifiées

Ces décisions restent dans leurs sources d'origine, comme historique ; elles ne sont pas effacées.

- P05 et la portée de DS2.3 (deux cases pour une descente d'un étage) : remplacées par SA-19 (deux cases au même niveau).
- D03 (base selon le nombre d'étages, sans gravité) : modifiée par CH-10 (pondération par `g/g0`).
- D09 (facteurs de poids après le tirage) : la surcharge, facteur lié au poids, s'applique après le plafond, mais avant le tirage (CH-13, CO-09).
- D12 (résistance du terrain d'OXCE, sans cumul) : modifiée par EN-01 (résistance cumulative).
- DS3.1 (exemption d'un étage sans surcharge) : restreinte au saut volontaire sans collision avec une unité (CH-01, CH-04) ; une chute involontaire peut blesser dès un étage (CH-03).
- DS4.5 (tirage commun entre l'unité et l'obstacle) : étendu aux collisions entre unités (CO-08).
- DS5.5 (grandes unités exclues de l'attaque sautée, comme sauteurs et comme cibles) : étendu à tout saut volontaire (GE-08) ; l'exclusion comme cible est maintenue (GE-09).
- DS5.3 (l'attaquant prend la case de la cible repoussée) : maintenue (RP-09).
- DS5.6 (coût proportionnel à la distance de Manhattan) : distance 3D pour les TU, et saut simple sans supplément (SA-22 à SA-24).
- Recommandation E11 du LOT-2G (même vitesse pour toutes les masses) : écartée par SA-16.

#### Encore ouvert

- Géométrie : rapport case/étage ; dimensions des unités par type et par posture ; épaisseur des surfaces ; tolérance des contacts.
- Sauts : masses et capacités de référence par type ; calibrage horizontal et portée en descente ; plage de gravité par type et très faible gravité ; valeur de `C_saut` ; coût en TU non entier.
- Force et charge : capacité de portage en kg selon la Force ; cohérence avec N14 ; masses des corps et des objets.
- Chutes : sens de « un étage » dans CH-01 ; seuil de 0,25 avant ou après `g/g0`, et cas des sauts volontaires au même niveau ; point d'application de `g/g0`.
- Dégâts : `K_unités`, `K_obstacles` ; absorption d'énergie des planchers ; conversion de la résistance en énergie ; protections par zone et direction ; coefficients de santé et d'étourdissement ; pénalité d'étourdissement sur les Réactions.
- Chaîne de calcul : place de `min(M/80, 3)` contre le décor ; surcharge dans les collisions ; interaction des plafonds 60, 70 et 80 avec les bonus, la gravité et la surcharge ; nature et normalisation du tirage de 50 à 150 % ; détail des deux arrondis ; limites numériques éventuelles ; double comptage de la gravité, de la vitesse et de la masse.
- Vitesse après un choc qui interrompt le saut, et vitesse résiduelle après la traversée d'une surface.
- Tirage commun entre deux unités (CO-08) et principe selon lequel le poids ne décide pas seul de l'unité la plus blessée (DS4.1) : à concilier.
- Esquive : instant où la menace est « vue » ; `n` pour un impact à hauteur intermédiaire ; probabilité non entière ; algorithme des esquives en conflit.
- Repoussement : retombée verticale de l'attaquant au-dessus de la cible (RP-06).
- Événements : ordre FIFO des chutes et chronologie physique ; clé d'ordre stable ; emplacement des cadavres ; collisions imbriquées et multi-cibles ; nombre maximal d'événements en chaîne.
- Décor : propriétés destructible ou indestructible, résistances initiales, unité des dégâts du terrain.
- Marche et TU : coûts des cases, capital et renouvellement des TU, visibilité, sous la responsabilité de `MEC-0001`.
- Primauté entre `MEC-0001` (N5 à N10) et `MEC-0002` pour les chutes.
- Décisions du 9 novembre 2026 et correctif du propriétaire (LOT-2F) : reprises ici par leurs identifiants, sans inscription propre.

Cette liste n'est pas exhaustive : tout ce que PE-01 à EN-10 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.

## 3. Diff exact proposé

Diff unifié (contexte d'une ligne) du registre de `main` vers le texte proposé. **Il n'est pas appliqué.** Les lignes de contexte vides y sont sans espace initial ; `git apply` et `patch` les acceptent (contrôles dans `LOT-2I-EXECUTION.md`).

```diff
diff --git a/docs/gameplay/GAMEPLAY-DECISIONS.md b/docs/gameplay/GAMEPLAY-DECISIONS.md
--- a/docs/gameplay/GAMEPLAY-DECISIONS.md
+++ b/docs/gameplay/GAMEPLAY-DECISIONS.md
@@ -4,3 +4,3 @@

-**Une seule fiche est enregistrée : `MEC-0001`, proposée et incomplète, sans décision globale « acceptée ».** Aucune mécanique n'est acceptée dans son ensemble : aucune mécanique de jeu ne peut donc être implémentée.
+**Deux fiches sont enregistrées : `MEC-0001` et `MEC-0002`, proposées et incomplètes, sans décision globale « acceptée ».** Aucune mécanique n'est acceptée dans son ensemble : aucune mécanique de jeu ne peut donc être implémentée.

@@ -50,3 +50,3 @@

-**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**
+**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé. Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`.**

@@ -61,3 +61,3 @@
 | Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
-| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas. |
+| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas ; les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002`. |
 | Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
@@ -96,3 +96,3 @@
 - **N6** — Dégâts de chute croissants avec la hauteur. [À vérifier.]
-- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.]
+- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] Précisée par `MEC-0002` pour les sauts et les chutes : voir CH-01 (saut volontaire d'un étage), CH-03 (chute involontaire) et CH-09 (seuil de 0,25 étage), avec leurs réserves. *(Annotation ajoutée lors de l'inscription de `MEC-0002`.)*
 - **N8** — Les caractéristiques individuelles et les équipements peuvent modifier les conséquences d'une chute. [À vérifier.]
@@ -100,2 +100,3 @@
 - **N10** — Le poids de l'inventaire (armes, munitions, matériel) contribue aussi à l'effet de la charge lors d'une chute. [Effet sur les chutes : à vérifier. Vérifié : dans OXCE, le poids porté est le poids de l'armure plus celui des objets de l'inventaire (`src/Savegame/BattleUnit.cpp:4852-4861`).]
+  *(Annotation ajoutée lors de l'inscription de `MEC-0002` : pour les sauts, les chutes et leurs conséquences, N5 à N10 sont précisées par `MEC-0002` ; leur texte est conservé ici.)*
 - **N11** — Le poids total porté affecte aussi le déplacement normal. [Vérifié : dans OXCE, l'effet est indirect, par la réduction des TU, qui touche toutes les actions ; voir N12 à N14.]
@@ -120,3 +121,4 @@
   - hauteur de chute sans dégâts ;
-  - effet précis des caractéristiques, équipements, armure et charge.
+  - effet précis des caractéristiques, équipements, armure et charge ;
+  - principes et points encore ouverts : voir `MEC-0002`.
 - Surcharge : transposition exacte du principe d'OXCE (formule, arrondi, ordre avec les autres pénalités) ; présentation de l'indicateur « encombré ».
@@ -133 +135,179 @@
 L'hypothèse provisoire du LOT-2B « toutes les unités sont connues » n'est pas retenue : S6 à S9 introduisent les cases explorées et le terrain mémorisé, S11 et S12 les unités cachées.
+
+### MEC-0002 — Sauts, chutes et collisions
+
+**Fiche de conception incomplète. Des principes de conception sont acceptés (PE-01 à EN-10, du 14 novembre 2026, sauf GE-09 et RP-09, du 13 novembre 2026), dont huit restent à confirmer avant une inscription définitive, mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**
+
+| Champ | Valeur |
+|---|---|
+| Système | Combat tactique : sauts simples et attaques sautées, chutes volontaires et involontaires, trajectoire balistique, collisions, réception, esquives réactives, repoussements, destruction sous impact et chaîne d'événements associée. |
+| Description | Une unité peut sauter vers une case admissible, tomber, heurter des unités ou le décor, esquiver une unité qui tombe ou être repoussée. Règles partielles ci-dessous. |
+| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
+| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** ; aucun calcul de dégâts de chute n'y a été identifié (`docs/reviews/LOT-2E-VERTICALITE-OXCE.md`, C8). Les règles ci-dessous sont des adaptations de Bastion, sans reprise de code, de données ni d'assets (D4). Spécification : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Arbitrage : `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. Principes DS1 à DS5 : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`. Consolidation : `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` et `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`. |
+| Changement demandé | Fixer les sauts, chutes et collisions de Bastion à partir des principes PE-01 à EN-10 ci-dessous. Les points encore ouverts sont listés plus bas. |
+| Décision du propriétaire | reportée — inscription partielle des principes de conception. Principes acceptés le 14 novembre 2026 : 29 propositions et arbitrages complémentaires 1A à 6A, consolidés dans `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` (branche `orchestration/mandats`, commit `d028c52f500ed8daeca917adbcb9a9e1eb3ff8bd`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`). Preuve : déclaration du propriétaire du 14 novembre 2026 (preuve déclarative), qui précise que les esquives sont des tentatives automatiques dont la réussite dépend d'un tirage et des Réactions. GE-09 et RP-09 reprennent DS5.5 et DS5.3 (13 novembre 2026), que la consolidation ne modifie pas. Ces principes reprennent ou modifient les décisions du 9 novembre 2026 et le correctif du propriétaire (identifiants du LOT-2F), ainsi que les principes DS1 à DS5 du 13 novembre 2026. |
+| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
+| Éléments exclus | Tous les points listés sous « Encore ouvert » ; escaliers, échelles et ascenseurs ; règles générales du brouillard ; renouvellement des TU ; stabilité structurelle des bâtiments ; toute autre mécanique (tir, explosion, destruction de cadavre, vol, apesanteur). |
+| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` §3). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
+| Tests de modification | Critères futurs seulement. Aucun test écrit ni exécuté. |
+| État d'implémentation | non commencé |
+
+#### Principes de conception acceptés le 14 novembre 2026
+
+Ils n'autorisent, seuls, aucun gameplay. Les identifiants PE, GE, SA, CH, CO, ES, RP et EN ont été proposés par le LOT-2I. Entre crochets, la décision antérieure reprise, précisée ou modifiée. S, Z et N renvoient à `MEC-0001` (R : registre). Les autres identifiants (J, K, D, I, P, E) renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` (M : décision du 9 novembre 2026 ; P : correctif du propriétaire). DS*n*.*m* renvoie à la consolidation DS1 à DS5 du 13 novembre 2026. « Ouvert » nomme le paramètre qui reste à fixer. « À confirmer avant inscription définitive » : principe accepté dont le texte attend une confirmation du propriétaire.
+
+- **Périmètre**
+  - **PE-01** — `MEC-0001` garde la marche ordinaire : cheminement, coûts de terrain, diagonales, visibilité du trajet, TU du déplacement ordinaire. Elle conserve S1 à S12, Z1 et N1 à N14, avec une annotation historique de N7, sous réserve d'autorisation d'inscription. [Rattachement de la fiche (LOT-2H, §5 ligne 12).] Ouvert : primauté entre les deux fiches (A24). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A24).
+  - **PE-02** — `MEC-0002` couvre le saut simple, l'attaque sautée, les chutes volontaires et involontaires, la trajectoire, les contacts et collisions, la réception, l'esquive réactive, le repoussement, l'impact des corps, la destruction sous impact et la chaîne d'événements associée.
+  - **PE-03** — Hors de `MEC-0002` : escaliers, échelles, ascenseurs, règles générales du brouillard, renouvellement global des TU, stabilité structurelle des bâtiments.
+  - **PE-04** — Décrire une règle physique utilisable ailleurs n'autorise pas d'autres mécaniques (tir, explosion, destruction de cadavre, vol, apesanteur, etc.).
+
+- **Géométrie, masse et posture**
+  - **GE-01** — Positions `(x, y, z)`, plusieurs niveaux. [N3 (R).]
+  - **GE-02** — Largeur de case, hauteur d'étage et volumes des unités en proportions, sans mètres pour la grille. [DS1.1.] Ouvert : rapports exacts.
+  - **GE-03** — Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. [DS1.2 ; postures : nouveau.] Ouvert : dimensions par type et posture.
+  - **GE-04** — Pendant le vol, posture et orientation du volume sont conservées : pas de rotation des pavés, pas de changement de posture. [nouveau.]
+  - **GE-05** — Un contact de surfaces suffit à détecter la rencontre. Sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés, sans créer d'énergie ni dédoubler un impact. [D11 ; contacts : nouveau.] Ouvert : tolérance numérique.
+  - **GE-06** — La masse physique totale `M` comprend le corps, l'armure, l'équipement et l'inventaire, en kg. [E23 (P).] Ouvert : masses par type et par objet.
+  - **GE-07** — La charge portée, pour la surcharge, comprend l'armure, l'équipement et l'inventaire, en kg ; elle est distincte de `M`. La Force se traduit en capacité de portage en kg, selon un modèle à définir. [N10, N14 (R) ; E20 (LOT-2F).] Ouvert : modèle Force → capacité.
+  - **GE-08** — Les unités de plusieurs cases peuvent subir des chutes involontaires et des collisions. Leurs sauts volontaires sont provisoirement indisponibles (« proposition 8/29 »). [étend DS5.5, qui excluait l'attaque sautée faite par ces unités et contre elles.]
+  - **GE-09** — Une unité de plusieurs cases n'est pas choisie comme cible d'une attaque sautée. **Maintenue de DS5.5** : la consolidation du 14 novembre ne la redit pas, mais ne la modifie pas. [DS5.5.] Ouvert : confirmation (A12). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A12).
+
+- **Sauts**
+  - **SA-01** — Saut simple vers une destination admissible au même niveau ou plus bas ; il permet de franchir une ouverture ou un obstacle. Un saut vers une zone sans support immédiat est permis : l'unité continue de tomber jusqu'à un support ou un contact. [nouveau ; N5 (R).]
+  - **SA-02** — L'attaque sautée n'est possible que si la cible est au moins un étage plus bas. [J01 (M).]
+  - **SA-03** — Un allié ou un neutre déjà identifié ne peut pas être ciblé intentionnellement. [J06 (M).]
+  - **SA-04** — Un ennemi actuellement visible peut être ciblé malgré S10. [J13, E14 (P) ; DS1.4.]
+  - **SA-05** — Destination visible ou déjà explorée ; jamais explorée : interdite. [J03, J04 (M) ; S6 (R).]
+  - **SA-06** — Les cases survolées peuvent n'avoir jamais été explorées. [tranche E15 (LOT-2F).]
+  - **SA-07** — Obstacles et unités cachés ne sont révélés qu'à leur rencontre. [P08, I01 (M) ; DS5.2.]
+  - **SA-08** — Un ennemi caché, ou un allié ou neutre caché, sur la case attaquée peut être percuté, avec le bonus d'attaque sautée même s'il était allié ou neutre. [J05, J07, J08 (M).]
+  - **SA-09** — Un saut simple qui percute par accident une unité cachée : collision et dégâts possibles, **sans** bonus × 1,25. [nouveau ; D08 (M).]
+  - **SA-10** — Arc balistique continu, sans contournement des obstacles. Seule une destination à portée de Manhattan est permise ; la trajectoire réelle est ensuite vérifiée avec les volumes. [P07 (M) ; DS1.2.]
+  - **SA-11** — Le sol de la case de départ est ignoré au décollage, sans étendre cette exception aux autres surfaces. [DS1.3.]
+  - **SA-12** — Obstacle connu sur la trajectoire : engagement interdit, sauf pour les cibles offensives permises. Obstacle inconnu : saut engagé, puis collision, arrêt et révélation à l'impact. [P08 (M).]
+  - **SA-13** — En vol : aucune modification volontaire de destination ni d'impulsion ; vitesse horizontale constante tant qu'aucun contact ne la modifie ; fin de l'action à une réception stable, sans glissement automatique. [nouveau.]
+  - **SA-14** — Le saut s'arrête au premier choc ; la collision et les chutes qui suivent sont des événements distincts, résolus dans l'ordre chronologique. [DS5.2 ; D13 (M).]
+  - **SA-15** — Chaque type d'unité a une impulsion verticale et une capacité d'impulsion horizontale distinctes et configurables. [P02, P03 (M).] Ouvert : valeurs par type.
+  - **SA-16** — Loi : impulsion constante à effort égal. Pour une unité donnée et des conditions comparables, la vitesse initiale varie en raison inverse de sa masse totale, `v = v_ref × (M_ref/M)`. À gravité constante, la hauteur varie comme le carré du rapport des masses ; la portée diminue aussi quand la masse augmente. [DS2.1 ; tranche E11 (quantité de mouvement) ; écarte la recommandation E11 du LOT-2G.] Ouvert : `M_ref`, `v_ref` par type.
+  - **SA-17** — La gravité influe sur la durée de vol, la hauteur et la portée. Chaque type d'unité a sa plage de gravité où il peut sauter. [P01 (M) ; DS2.4 (plage par type au lieu d'une plage unique).] Ouvert : bornes.
+  - **SA-18** — Aucun saut balistique à 0 g ; l'apesanteur est hors périmètre. Une chute involontaire reste possible en gravité positive, même quand les sauts sont interdits. Une gravité négative est invalide. [DS2.4 ; E3 (LOT-2F).]
+  - **SA-19** — Référence à 1 g, pour l'unité de référence : sommet à un quart d'étage ; portée de 2 cases de Manhattan **au même niveau**, pour franchir un trou d'une case ; portée pour un étage de descente **supérieure à 2 cases**, valeur à calculer. [P04 (M) inchangée ; **remplace** P05 (M) et la portée de DS2.3.] Ouvert : valeur de la portée en descente.
+  - **SA-20** — À capacités égales, un saut au même niveau a une durée de vol et une portée inférieures à un saut avec un étage de descente. [conséquence de SA-16 à SA-19.]
+  - **SA-21** — Portée horizontale `|Δx| + |Δy|`, plafond entier arrondi vers le bas. Aucune portée minimale garantie quand le calcul donne moins d'une case. [P05 (M) ; DS2.2 ; tranche la conversion de E2.]
+  - **SA-22** — Distance pour les TU : `d_3D = |Δx| + |Δy| + |Δz|`, distincte de la portée horizontale. [précise DS5.6 (« distance de Manhattan »).]
+  - **SA-23** — `TU_simple = d_3D × C_saut`. [nouveau.] Ouvert : `C_saut` ; coût non entier.
+  - **SA-24** — `TU_attaque = d_3D × C_saut + max(1, ⌊0,20 × TU_max⌋)`. [J09 (M) ; DS5.6.] Ouvert : `C_saut` ; coût non entier.
+  - **SA-25** — `C_saut` est propre aux sauts, indépendant de la marche ; sa valeur est explicitement reportée à l'équilibrage. [E13 (LOT-2F).] Ouvert : valeur.
+  - **SA-26** — Coût payé en entier à l'engagement, même si le saut est interrompu ou si la cible esquive ; aucun remboursement. Une chute passive qui suit la destination choisie ne coûte pas de TU en plus. [J09 (M) ; DS5.6.]
+  - **SA-27** — Une action sans TU suffisantes est interdite. Destination, coût et trajectoire sont prévisualisés dans les limites des informations connues. [J10, I02 (M).]
+
+- **Chutes et réception**
+  - **CH-01** — Un saut volontaire (simple ou offensif) d'**un étage**, sans surcharge et sans collision avec une unité, n'inflige pas de dégâts de chute. [précise DS3.1 (« volontaire ») ; N7 (R).] Ouvert : définition de « un étage ». **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A3).
+  - **CH-02** — En surcharge, un saut volontaire d'un étage peut produire des dégâts. [DS3.1, DS3.2.]
+  - **CH-03** — Une chute **involontaire** peut blesser dès un étage, même sans surcharge, qu'elle soit prévue ou subie par surprise. [D01 (M) ; restreint l'exemption de DS3.1.]
+  - **CH-04** — Une réception sur une unité est une collision, qui peut blesser les deux unités, distincte d'une chute au sol. Le bonus offensif ne vaut que pour l'attaque sautée. [DS3.4 ; K01, K02, D08 (M) ; **restreint** DS3.1 : l'unité qui tombe d'un étage sans surcharge sur une unité n'est plus exemptée.] Ouvert : changement de DS3.1 à confirmer (A25). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A25).
+  - **CH-05** — Si la cible esquive, l'attaquant finit son saut au sol : ce saut reste **volontaire**, et l'exemption d'un étage sans surcharge s'applique. [E18 (P) ; DS3.1.]
+  - **CH-06** — Si un obstacle interrompt la trajectoire puis provoque une nouvelle chute, cette chute est **involontaire** ; collision et chute sont comptées séparément. [D13 (M).]
+  - **CH-07** — La puissance de référence d'une chute au sol reste celle du LOT-2F : `B(1) = 8`, `B(2) = 14`, `B(3) = 22,1`, `B(4) = 33,035`, incréments de + 6 puis × 1,35. [D03, D04 (M).]
+  - **CH-08** — Hauteur réelle de chute, fractions d'étage comprises ; interpolation linéaire entre les points de référence. [nouveau ; tranche le comptage de E12 pour les dégâts.]
+  - **CH-09** — Hauteur équivalente ≤ 0,25 étage : aucun dégât. Entre 0,25 et 1 étage : interpolation de `(0,25 ; 0)` à `(1 ; 8)`. [précise N7 (R) ; tranche « moins d'un étage » (DS3).] Ouvert : portée du seuil selon la gravité. **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A4).
+  - **CH-10** — En gravité positive, la puissance de référence est multipliée par `g/g0`, avec `g0 = 1 g` ; la précision décimale est gardée jusqu'aux arrondis prévus. [**modifie** D03, qui ne dépendait pas de la gravité.] Ouvert : point d'application.
+  - **CH-11** — Vitesse verticale initiale descendante : hauteur équivalente `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 0,25 porte sur `H_eq`. Vitesse initiale montante : la montée, le sommet et la descente sont résolus physiquement, avec la vitesse réelle à l'impact. [nouveau.]
+  - **CH-12** — Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse verticale ; la vitesse horizontale compte contre les surfaces qui lui sont normales. [D11 (M).]
+  - **CH-13** — Plafond de puissance de base 70 pour une chute au sol, **avant** le multiplicateur de surcharge, qui peut porter la puissance au-delà de 70 avant le tirage. Les plafonds 60 (unité qui tombe), 80 (cible percutée) et 70 (obstacle) restent pour leurs domaines, sous réserve d'une vérification de la chaîne. [D05 (M) ; déroge à D09 (M), qui plaçait les facteurs de poids après le tirage.] Ouvert : vérification de la chaîne.
+  - **CH-14** — Capacité de portage en kg selon la Force ; seuil de surcharge commun à N14. [DS3.2 ; N14 (R).] Ouvert : modèle Force → kg.
+  - **CH-15** — Dépassement relatif `S = max(0, charge / capacité − 1)`, avec une capacité strictement positive. [nouveau.]
+  - **CH-16** — Multiplicateur `F_surcharge = min(2, 1 + 0,5 × S)`. [nouveau ; tranche E24 pour le poids au sol.]
+  - **CH-17** — Ce multiplicateur aggrave la puissance utilisée pour les blessures et pour l'étourdissement ; l'armure applique ensuite ses protections. [N9, N10 (R).]
+  - **CH-18** — La surcharge ne supprime pas le seuil de 0,25 étage. [nouveau.]
+  - **CH-19** — La nature du sol ne modifie pas directement les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol. [D02 (M).]
+  - **CH-20** — L'impact peut endommager ou détruire le support ; s'il cède, la chute continue. Chaque impact successif est résolu à part, et les dommages corporels peuvent s'additionner. [D12, D13 (M).]
+  - **CH-21** — Traverser une surface destructible absorbe de l'énergie et ralentit le corps ; la gravité peut ensuite le réaccélérer. [nouveau.] Ouvert : formule de perte d'énergie.
+
+- **Collisions et dégâts**
+  - **CO-01** — Détection des contacts sur les volumes réels au moment du contact, y compris après un déplacement d'esquive ou une perte de support. [DS1.2.]
+  - **CO-02** — Puissance de base `P = K × v_n²`, où `v_n` est la composante normale de la vitesse relative au contact (entre deux unités, ou contre une surface fixe). Deux coefficients distincts et configurables : `K_unités` et `K_obstacles`. [étend DS4.2 aux collisions entre unités ; D10 (M).] Ouvert : `K_unités`, `K_obstacles`.
+  - **CO-03** — Entre unités, facteur appliqué aux dégâts reçus par chacune : `F_i = clamp(√(M_autre/M_i), 0,75 ; 1,5)`, masses strictement positives. [DS4.1 ; K08 (M) ; formule E6 du LOT-2G non reprise.] Ouvert : interaction avec le tirage commun.
+  - **CO-04** — Contre le décor : référence du LOT-2F `min(M/80, 3)` pour le facteur de masse, et plafond de 70. Le point d'insertion de ce facteur dans la nouvelle chaîne reste à revoir. [D10, D05 (M).] Ouvert : point d'insertion.
+  - **CO-05** — Type de dégâts « impact » propre à Bastion : zones corporelles exposées et protections d'armure liées à la direction du choc, sans recopier de code ni de données d'OXCE. [DS4.4 ; D07 (LOT-2F, ouverte : E7).] Ouvert : protections par zone.
+  - **CO-06** — Blessures et étourdissement sont des effets séparés ; une armure peut protéger plus la santé que l'étourdissement ; on peut être étourdi sans perdre de santé. [K02 (M).] Ouvert : coefficients santé / étourdissement.
+  - **CO-07** — Chaque type d'unité a une sensibilité à l'étourdissement ; 0 vaut immunité aux étourdissements d'impact. Une unité consciente mais étourdie peut encore tenter une esquive, avec des Réactions réduites. [nouveau.] Ouvert : pénalité sur les Réactions.
+  - **CO-08** — Tirage d'intensité de 50 à 150 %, **une fois par événement de collision**, partagé par les deux unités d'une collision entre unités, ou par l'unité et l'obstacle. Résistances et effets s'appliquent ensuite à chacun. Des collisions réellement distinctes, même rapprochées, ont des tirages distincts. [D06 (M) ; **étend** DS4.5 aux collisions entre unités.] Ouvert : conflit avec DS4.1 (A8) ; nature et normalisation du tirage (A26). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A8).
+  - **CO-09** — Ordre : puissance initiale ; facteur de gravité s'il s'applique ; plafond de base ; bonus de surcharge et/ou d'attaque applicables ; arrondi au plus proche, moitié vers le haut ; tirage ; facteur de masse s'il s'applique ; second arrondi ; puis effets et protections séparés pour la santé et l'étourdissement. Les termes D09 et D10 sont à réconcilier, sans double comptage. [DS3.5 ; D10 (M) ; déroge à D09 (M) : la surcharge, facteur lié au poids, précède le tirage.] Ouvert : réconciliation ; détail des deux arrondis et du tirage (A26).
+  - **CO-10** — Bonus × 1,25 uniquement sur les dégâts infligés à la cible d'une attaque sautée, après le plafond et avant le tirage ; jamais pour l'attaquant. Une cible alliée ou neutre cachée le reçoit aussi. [J08, J11, J12, D08 (M).]
+  - **CO-11** — Contacts simultanés d'un même choc : les surfaces peuvent être endommagées, sans dupliquer la puissance corporelle. Contre plusieurs unités distinctes : un calcul par cible, regroupé au besoin dans un même événement. [nouveau.] Ouvert : détails d'implémentation.
+
+- **Esquives réactives**
+  - **ES-01** — Le moteur déclenche la tentative tout seul, sans le joueur ; la réussite n'est pas automatique : elle dépend d'un tirage et des Réactions. [K03, K05 (M) ; DS5.7 ; précision du propriétaire du 14 novembre 2026.]
+  - **ES-02** — Conditions : menace vue **juste avant l'impact**, TU suffisantes, case admissible. Une unité qui découvre la menace pendant la chute peut tenter l'esquive. [K03 (M) ; DS5.7.] Ouvert : instant exact.
+  - **ES-03** — Bonus de + 10 points si l'unité menacée voyait la menace **dès le départ** du saut ou dès le début d'une chute involontaire ; sinon 0. Même logique pour les corps qui tombent, selon ce que perçoit la cible. [nouveau.]
+  - **ES-04** — Bonus de + 5 points par étage, `n = |z_départ − z_arrivée|`, pour une menace qui descend. [K05 (M).] Ouvert : `n` pour un impact à hauteur intermédiaire.
+  - **ES-05** — `P = clamp(R_effectif + B_visibilité + 5n, 0, 100)` %, où `R_effectif` est la valeur des Réactions après une éventuelle pénalité d'étourdissement. [K05 (M) ; DS5.7.] Ouvert : pénalité d'étourdissement.
+  - **ES-06** — Tirage entier uniforme `t` dans {1, …, 100} ; réussite si `t ≤ P`. [nouveau ; LOT-2G (E12 e) non repris.] Ouvert : `P` non entier.
+  - **ES-07** — Une unité inconsciente ou morte n'esquive pas ; les corps qui tombent peuvent, eux, être esquivés. [nouveau.]
+  - **ES-08** — Déplacement vers l'une des 8 cases voisines du même niveau, diagonales comprises, avec un support valide ; pas de saut dans le vide en esquivant. [DS5.7.]
+  - **ES-09** — Coût habituel de la marche vers la case choisie (terrain, facteur diagonal), payé avec les TU restantes, même pendant le tour adverse. [DS5.7 ; S2 (R).] Ouvert : coûts de terrain (`MEC-0001`).
+  - **ES-10** — Esquive réussie et effectivement faite : TU débitées. Échec du tirage ou déplacement impossible : aucun débit. [K06, K07 (M).]
+  - **ES-11** — Choix aléatoire uniforme parmi les destinations admissibles. Une information cachée ne permet pas de choisir une case. La découverte d'un obstacle bloque et révèle la tentative, sans débit de TU. [K04 (M) ; tranche E22 (loi uniforme).]
+  - **ES-12** — Pas d'échange simultané de cases ni de volumes qui se traversent ; destination libre au début de la résolution. Esquives en conflit : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager au hasard les combinaisons équivalentes. [nouveau.] Ouvert : algorithme.
+  - **ES-13** — Plusieurs menaces visibles et simultanées sur une même unité dans un même événement : une seule tentative ; la case doit éviter toutes les menaces **connues** ; `n` vient de la menace visible qui tombe du plus d'étages. Les menaces cachées ne comptent pas dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée. [nouveau.]
+  - **ES-14** — Dangers successifs : nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte suit le moteur séquentiel. [nouveau.]
+
+- **Repoussement et retombées**
+  - **RP-01** — Esquive réussie : déplacement volontaire, pas de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un repoussement **après** l'impact. [**tranche** le point « à vérifier » K07 (M) / DS5.3.] Ouvert : confirmation explicite demandée par la consolidation DS (A27). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A27).
+  - **RP-02** — Cible touchée : repoussement en priorité dans la direction de l'impact, sinon vers les directions voisines les plus proches, égalités tirées au hasard. Une case au-dessus du vide est admissible pour un repoussement forcé et entraîne une chute involontaire. [précise DS5.3.]
+  - **RP-03** — Une case occupée par une autre unité n'est pas admissible : pas de repoussement en chaîne. [S10 (R).]
+  - **RP-04** — Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort garde sa masse et son volume. [tranche « cible hors de combat » (DS5).]
+  - **RP-05** — Si la cible ne peut pas être repoussée, l'attaquant cherche une case adjacente (8 voisines) pour retomber, en priorité du côté d'où il vient, puis par proximité de direction ; pas de recherche au-delà. [précise DS5.4 (rayon : cases adjacentes).]
+  - **RP-06** — Impossibilité entièrement connue avant l'engagement : l'attaque sautée est refusée, sans révéler de données cachées. Impossibilité révélée en vol : l'attaquant s'arrête au contact, puis retombe verticalement depuis sa dernière position libre, sans pénétrer la cible. [nouveau.] Ouvert : issue de la retombée.
+  - **RP-07** — Une collision accidentelle, un cadavre ou un corps inconscient peut repousser ; aucune intention n'est requise, et aucun bonus offensif n'est créé. [nouveau.]
+  - **RP-08** — Plusieurs impacts vraiment simultanés : la direction du repoussement combine intensités et directions ; cela n'introduit pas d'attaques volontaires simultanées. [nouveau.]
+  - **RP-09** — Après le repoussement de la cible, l'attaquant prend la case initiale de la cible. **Maintenue de DS5.3** : la consolidation du 14 novembre ne la redit pas, mais la suppose (RP-05). [DS5.3.] Ouvert : confirmation (A18). **À confirmer avant inscription définitive** (LOT-2I, ambiguïté A18).
+
+- **Environnement destructible et événements**
+  - **EN-01** — Murs, portes, planchers et autres décors destructibles ont des points de résistance **cumulatifs** : les dégâts successifs les réduisent. Les éléments indestructibles restent intacts. [**modifie** D12 (M), qui suivait le seuil sans cumul d'OXCE.] Ouvert : résistances, unité des dégâts du terrain.
+  - **EN-02** — Tant que leur résistance reste strictement positive, les éléments gardent leur blocage et leurs collisions ; l'apparence peut changer, sans fissure fonctionnelle automatique. [nouveau.]
+  - **EN-03** — À zéro : destruction immédiate ; perte de support et chutes immédiates. Pas d'effondrement automatique des éléments voisins. [D12 (M) ; PE-03.]
+  - **EN-04** — Un même événement qui produit plusieurs impacts simultanés sur un même plancher additionne leurs dégâts avant de décider de la destruction ; à distinguer de chutes successives. [nouveau.]
+  - **EN-05** — Tour par tour : une action offensive volontaire est résolue jusqu'au bout avant l'action de combat suivante. [DS5.1.]
+  - **EN-06** — Si plusieurs unités perdent leur support à cause d'un même événement, leurs chutes sont traitées **l'une après l'autre**, dans un ordre stable (par exemple les identifiants internes), en file FIFO ; les nouvelles chutes passent après celles qui attendent. [précise DS5.1 et DS5.2 ; I03 (M).] Ouvert : clé d'ordre ; articulation avec la chronologie.
+  - **EN-07** — À chaque traitement : réévaluer positions, vitesses, santé et supports ; annuler un événement devenu caduc ; un seul événement de chute en attente par unité. [nouveau.]
+  - **EN-08** — Les corps morts ou inconscients peuvent tomber, heurter d'autres unités et provoquer dégâts, étourdissement ou repoussement. Un cadavre ne subit plus de pertes de santé ni d'étourdissement ; la destruction des corps est hors périmètre. [nouveau.]
+  - **EN-09** — Les collisions d'un même événement peuvent toucher plusieurs surfaces ou cibles, sans réintroduire plusieurs actions offensives simultanées. [nouveau.]
+  - **EN-10** — Hasard contrôlable par une graine ; ordre de traitement déterministe en dehors du hasard choisi ; tests reproductibles. [nouveau.]
+
+#### Décisions antérieures remplacées ou modifiées
+
+Ces décisions restent dans leurs sources d'origine, comme historique ; elles ne sont pas effacées.
+
+- P05 et la portée de DS2.3 (deux cases pour une descente d'un étage) : remplacées par SA-19 (deux cases au même niveau).
+- D03 (base selon le nombre d'étages, sans gravité) : modifiée par CH-10 (pondération par `g/g0`).
+- D09 (facteurs de poids après le tirage) : la surcharge, facteur lié au poids, s'applique après le plafond, mais avant le tirage (CH-13, CO-09).
+- D12 (résistance du terrain d'OXCE, sans cumul) : modifiée par EN-01 (résistance cumulative).
+- DS3.1 (exemption d'un étage sans surcharge) : restreinte au saut volontaire sans collision avec une unité (CH-01, CH-04) ; une chute involontaire peut blesser dès un étage (CH-03).
+- DS4.5 (tirage commun entre l'unité et l'obstacle) : étendu aux collisions entre unités (CO-08).
+- DS5.5 (grandes unités exclues de l'attaque sautée, comme sauteurs et comme cibles) : étendu à tout saut volontaire (GE-08) ; l'exclusion comme cible est maintenue (GE-09).
+- DS5.3 (l'attaquant prend la case de la cible repoussée) : maintenue (RP-09).
+- DS5.6 (coût proportionnel à la distance de Manhattan) : distance 3D pour les TU, et saut simple sans supplément (SA-22 à SA-24).
+- Recommandation E11 du LOT-2G (même vitesse pour toutes les masses) : écartée par SA-16.
+
+#### Encore ouvert
+
+- Géométrie : rapport case/étage ; dimensions des unités par type et par posture ; épaisseur des surfaces ; tolérance des contacts.
+- Sauts : masses et capacités de référence par type ; calibrage horizontal et portée en descente ; plage de gravité par type et très faible gravité ; valeur de `C_saut` ; coût en TU non entier.
+- Force et charge : capacité de portage en kg selon la Force ; cohérence avec N14 ; masses des corps et des objets.
+- Chutes : sens de « un étage » dans CH-01 ; seuil de 0,25 avant ou après `g/g0`, et cas des sauts volontaires au même niveau ; point d'application de `g/g0`.
+- Dégâts : `K_unités`, `K_obstacles` ; absorption d'énergie des planchers ; conversion de la résistance en énergie ; protections par zone et direction ; coefficients de santé et d'étourdissement ; pénalité d'étourdissement sur les Réactions.
+- Chaîne de calcul : place de `min(M/80, 3)` contre le décor ; surcharge dans les collisions ; interaction des plafonds 60, 70 et 80 avec les bonus, la gravité et la surcharge ; nature et normalisation du tirage de 50 à 150 % ; détail des deux arrondis ; limites numériques éventuelles ; double comptage de la gravité, de la vitesse et de la masse.
+- Vitesse après un choc qui interrompt le saut, et vitesse résiduelle après la traversée d'une surface.
+- Tirage commun entre deux unités (CO-08) et principe selon lequel le poids ne décide pas seul de l'unité la plus blessée (DS4.1) : à concilier.
+- Esquive : instant où la menace est « vue » ; `n` pour un impact à hauteur intermédiaire ; probabilité non entière ; algorithme des esquives en conflit.
+- Repoussement : retombée verticale de l'attaquant au-dessus de la cible (RP-06).
+- Événements : ordre FIFO des chutes et chronologie physique ; clé d'ordre stable ; emplacement des cadavres ; collisions imbriquées et multi-cibles ; nombre maximal d'événements en chaîne.
+- Décor : propriétés destructible ou indestructible, résistances initiales, unité des dégâts du terrain.
+- Marche et TU : coûts des cases, capital et renouvellement des TU, visibilité, sous la responsabilité de `MEC-0001`.
+- Primauté entre `MEC-0001` (N5 à N10) et `MEC-0002` pour les chutes.
+- Décisions du 9 novembre 2026 et correctif du propriétaire (LOT-2F) : reprises ici par leurs identifiants, sans inscription propre.
+
+Cette liste n'est pas exhaustive : tout ce que PE-01 à EN-10 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.
```

## 4. À confirmer avant une inscription

| # | Sujet | Pourquoi |
|---|---|---|
| 1 | Autorisation d'écrire le registre | CLAUDE.md §3 et §8 ; mandat LOT-2I v1.1 §2 : interdit dans ce lot |
| 2 | Preuve et date | La décision de `MEC-0002` repose sur une preuve déclarative (D2) et sur C2, qui n'est pas dans `main`. Faut-il archiver C2 et le mandat v1.1 dans `docs/mandates/`, comme les documents précédents ? |
| 3 | Les huit principes marqués « à confirmer » | A3, A4, A8, A12, A18, A24, A25, A27 (consolidation, §12) |
| 3 bis | Copie des arbitrages | Le mandat v1.1 (§1) demande une copie approuvée des 29 propositions et des réponses 1A à 6A, si Claude Code n'y a pas accès ; elle n'a pas été fournie |
| 4 | Identifiants PE, GE, SA, CH, CO, ES, RP, EN | Proposés par le LOT-2I ; à confirmer, car un identifiant du registre est permanent |
| 5 | Identifiant `MEC-0002` | Nommé par C2 et par le mandat v1.1 ; permanent une fois inscrit |
| 6 | Décisions du 9 novembre et correctif | Reprises par leurs identifiants dans `MEC-0002`, sans inscription propre : ce choix est à confirmer |
| 7 | Rebase du diff | Le diff vaut pour le registre au commit `74faa29` ; à régénérer si le registre change |
| 8 | Fichiers cités par la fiche | La fiche cite les documents du LOT-2I, qui ne seront sur `main` qu'après une fusion autorisée de ce lot |

## 5. Ce qui n'est pas modifié

- `docs/gameplay/GAMEPLAY-DECISIONS.md` : inchangé (SHA-256 identique à `main`).
- Aucun autre registre (`docs/decisions/`, `docs/references/`), ni `CLAUDE.md`, ni le harnais, ni `src/` ou `tests/`.
- `docs/mandates/` : ni archive du mandat v1.1, ni modification de l'index (non autorisées).
- Les livrables des LOT-2F, LOT-2G et LOT-2H restent tels quels.
