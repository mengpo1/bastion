# LOT-2I — Diff proposé du registre : `MEC-0001` annotée et nouvelle fiche `MEC-0002`

> **PROPOSITION DOCUMENTAIRE — NON APPLIQUÉE. Version corrigée par le correctif v1.2 (14 novembre 2026).** Rien de ce document n'est écrit dans `docs/gameplay/GAMEPLAY-DECISIONS.md`. Une inscription exigera une autorisation distincte du propriétaire et un mandat d'écriture du registre. **Aucune implémentation n'est autorisée**, même après une inscription : les deux fiches resteraient « reportées ».

| | |
|---|---|
| Base | Registre sur `origin/main` = `74faa2974da7a4645725b4271eb66ae2a512e98a` ; objet Git `a72df450…`, SHA-256 `c2a3a55e7b1ed3d08089b5d814cded324b94313792982c8556d0e9d19a7e3968`. Lu, **non modifié**. |
| Contenu | Les règles de `MEC-0002` reprennent mot pour mot la colonne « Règle » de `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md`, générées depuis ce fichier. Seules différences : les abréviations propres au LOT-2I (« C2 », « D2 », « G ») y sont écrites en toutes lettres ; la mention « (v1.2) » y est omise ; les renvois aux §11 et §12 de la consolidation sont retirés, et « (§12, A*n*) » devient « (A*n*) ». Les libellés des arbitrages v1.2 (A3A, D1C, etc.) et les renvois A*n* sont expliqués dans l'introduction des principes. |
| Correctif v1.2 | Fiche et diff régénérés après intégration des arbitrages C3 dans la consolidation (§14 de celle-ci). Le diff v1.1 reste lisible dans l'historique Git (commit `cca1690`). Changements : voir « Changements du correctif v1.2 » ci-dessous. |
| Remplace | La proposition du LOT-2H (`docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md`), qui mettait DS1 à DS5 dans `MEC-0001`. Elle n'a pas été appliquée ; ses principes deviennent des sources de `MEC-0002`. |

## 0. Lecture rapide

**Ce qu'une écriture future changerait au registre** (diff exact au §3) :
1. la phrase d'introduction : « Deux fiches sont enregistrées » ;
2. `MEC-0001` :
   - son bandeau renvoie les sauts, chutes, collisions, esquives et repoussements à `MEC-0002` ;
   - le champ « Éléments exclus » les exclut ;
   - N7 reçoit une annotation, sans réécriture ;
   - une annotation sous N10 dit que N5 à N10 sont précisées par `MEC-0002` ;
   - la ligne « Chutes » de « Encore ouvert » garde ses quatre sous-points et en reçoit un cinquième : ils sont précisés ou tranchés en partie par `MEC-0002` (seuil : CH-09), qui liste ceux qui restent ouverts ;
3. une nouvelle fiche `MEC-0002 — Sauts, chutes et collisions`, avec :
   - les champs du gabarit ;
   - **« Décision du propriétaire : reportée »** ;
   - les 105 principes PE-01 à EN-10 ;
   - les décisions antérieures remplacées ou modifiées ;
   - sa liste « Encore ouvert ».

**Ce qui n'est pas modifié** : la classe (`MODIFICATION-PROPOSEE`), l'état (« non commencé ») et le périmètre (« aucun changement de gameplay ») de `MEC-0001` ; le texte de S1 à S12, Z1 et N1 à N14 ; les champs « Décision du propriétaire » de `MEC-0001`.

**Aucun principe ne porte plus la mention « à confirmer avant inscription définitive »** : les huit principes qui la portaient en v1.1 (PE-01, GE-09, CH-01, CH-04, CH-09, CO-08, RP-01, RP-09) sont réglés dans leur principe par les arbitrages v1.2. Cela n'autorise **ni l'inscription, ni l'implémentation** : `MEC-0001` et `MEC-0002` restent « reportées », classe `MODIFICATION-PROPOSEE`. Avant une inscription reste la vérification de fidélité du texte proposé (§4, point 3), qui couvre notamment la lecture d'A4.3A pour un saut d'un étage en surcharge.

Les ouvertures restantes figurent dans la liste « Encore ouvert » de la fiche.

**Changements du correctif v1.2** dans le texte proposé :
- `MEC-0002` : 23 principes changent de texte, de statut ou de références (consolidation, §14) : seuil de chute de 3 m inclus, quelle que soit la gravité ; courbe `B(n)` historique et courbe à recalibrer ; surcharge d'une chute sur la hauteur équivalente, son effet dans les collisions restant ouvert ; vitesse héritée ; gravité au-delà du seuil ; sauts au même niveau et d'un étage, sans surcharge, exemptés à la réception, et saut d'un étage compté sur 3 m entre les sols, avec ou sans surcharge ; collision calculée à part ; tirage commun confirmé ; hauteur d'étage de 3 m ;
- champ « Décision du propriétaire » de `MEC-0002` : cite les arbitrages du 14 novembre 2026 transcrits dans le mandat v1.2, comme preuve déclarative ;
- listes « Décisions antérieures remplacées ou modifiées » et « Encore ouvert » de `MEC-0002` : mises à jour ;
- `MEC-0001` : l'annotation de N7 renvoie au seuil de 3 m, et non plus au seuil de 0,25 étage ; l'annotation sous N10 dit que `MEC-0002` fait autorité ; le cinquième sous-point « Chutes » de « Encore ouvert » cite le seuil de 3 m (CH-09).

## 1. Modifications de `MEC-0001`

| # | Emplacement | Aujourd'hui | Proposition |
|---|---|---|---|
| 1 | Introduction du registre | « Une seule fiche est enregistrée : `MEC-0001` » | « Deux fiches sont enregistrées : `MEC-0001` et `MEC-0002` », proposées et incomplètes |
| 2 | Bandeau de `MEC-0001` | Sous-décisions S1 à S12, Z1, N1 à N14 | Ajoute : « Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`. » |
| 3 | Éléments exclus | Ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | Ajoute les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002` |
| 4 | N7 | « Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] » | Texte gardé ; annotation : précisée par `MEC-0002`, qui fait autorité ; pas de dégâts de chute ordinaires jusqu'à 3 m inclus (CH-09) ; renvoi à CH-01 et CH-03. *(v1.1 : renvoi au seuil de 0,25 étage, « avec leurs réserves ».)* |
| 5 | Sous N10 | — | Annotation : N5 à N10 précisées par `MEC-0002`, qui fait autorité ; texte conservé comme historique. Primauté confirmée par le propriétaire (A24, v1.2) |
| 6 | Encore ouvert : chutes | Quatre sous-points sur les chutes, dont « hauteur de chute sans dégâts » | Les quatre sous-points sont gardés ; un cinquième dit qu'ils sont précisés ou tranchés en partie par `MEC-0002`, qui fait autorité (seuil sans dégâts : 3 m inclus, CH-09), et renvoie à sa liste des points ouverts. *(v1.1 : « principes et points encore ouverts : voir `MEC-0002` ».)* |

## 2. Texte proposé de la fiche `MEC-0002`

À ajouter à la fin du registre, après `MEC-0001`. **Non inscrit.**

### MEC-0002 — Sauts, chutes et collisions

**Fiche de conception incomplète. Des principes de conception sont acceptés (PE-01 à EN-10, du 14 novembre 2026, sauf GE-09 et RP-09, du 13 novembre 2026, dont le maintien a été confirmé le 14 novembre 2026), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**

| Champ | Valeur |
|---|---|
| Système | Combat tactique : sauts simples et attaques sautées, chutes volontaires et involontaires, trajectoire balistique, collisions, réception, esquives réactives, repoussements, destruction sous impact et chaîne d'événements associée. |
| Description | Une unité peut sauter vers une case admissible, tomber, heurter des unités ou le décor, esquiver une unité qui tombe ou être repoussée. Règles partielles ci-dessous. |
| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** ; aucun calcul de dégâts de chute n'y a été identifié (`docs/reviews/LOT-2E-VERTICALITE-OXCE.md`, C8). Les règles ci-dessous sont des adaptations de Bastion, sans reprise de code, de données ni d'assets (D4). Spécification : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Arbitrage : `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. Principes DS1 à DS5 : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`. Consolidation : `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` et `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`. |
| Changement demandé | Fixer les sauts, chutes et collisions de Bastion à partir des principes PE-01 à EN-10 ci-dessous. Les points encore ouverts sont listés plus bas. |
| Décision du propriétaire | reportée — inscription partielle des principes de conception. Principes acceptés le 14 novembre 2026 : 29 propositions et arbitrages complémentaires 1A à 6A, consolidés dans `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` (branche `orchestration/mandats`, commit `d028c52f500ed8daeca917adbcb9a9e1eb3ff8bd`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`). Preuve : déclaration du propriétaire du 14 novembre 2026 (preuve déclarative), qui précise que les esquives sont des tentatives automatiques dont la réussite dépend d'un tirage et des Réactions. Le même jour, arbitrages complémentaires du propriétaire sur la hauteur d'étage (3 m), le seuil de chute sans dégâts (3 m inclus), la surcharge, la gravité et la vitesse héritée, et confirmation des huit points laissés à confirmer par le LOT-2I ; ils sont transcrits par l'orchestrateur dans `docs/mandates/BASTION-MANDAT-LOT-2I-v1.2-CORRECTIF-MEC-0002.md` (branche `orchestration/mandats`, commit `f8cf26e38783499a23244f823da4e221d4a95992`, SHA-256 `e4c5345a324ed4e5eb9cab294c7af900b34c389cb0ea8e25e943da400ace5ba0`), preuve déclarative, et prévalent sur la consolidation là où ils la modifient. GE-09 et RP-09 reprennent DS5.5 et DS5.3 (13 novembre 2026), que la consolidation ne modifie pas ; leur maintien a été confirmé le 14 novembre 2026. Ces principes reprennent ou modifient les décisions du 9 novembre 2026 et le correctif du propriétaire (identifiants du LOT-2F), ainsi que les principes DS1 à DS5 du 13 novembre 2026. |
| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
| Éléments exclus | Tous les points listés sous « Encore ouvert » ; escaliers, échelles et ascenseurs ; règles générales du brouillard ; renouvellement des TU ; stabilité structurelle des bâtiments ; toute autre mécanique (tir, explosion, destruction de cadavre, vol, apesanteur). |
| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` §3). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
| Tests de modification | Critères futurs seulement. Aucun test écrit ni exécuté. |
| État d'implémentation | non commencé |

#### Principes de conception acceptés le 14 novembre 2026

Ils n'autorisent, seuls, aucun gameplay. Les identifiants PE, GE, SA, CH, CO, ES, RP et EN ont été proposés par le LOT-2I. Entre crochets, la décision antérieure reprise, précisée ou modifiée. S, Z et N renvoient à `MEC-0001` (R : registre). Les autres identifiants (J, K, D, I, P, E) renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` (M : décision du 9 novembre 2026 ; P : correctif du propriétaire). DS*n*.*m* renvoie à la consolidation DS1 à DS5 du 13 novembre 2026. A3A, A4.1D, A4.2A, A4.3A, A8A, D1C, D2A, D3A, D4A et « exception de surcharge » désignent les arbitrages complémentaires du 14 novembre 2026, et A12, A18, A24, A25, A27 les points du LOT-2I confirmés le même jour (mandat LOT-2I v1.2, §2). Un renvoi A*n* seul (A5, A6, A7, A15, A17, A19, A26, A29, A30, etc.) désigne l'ambiguïté du même numéro, au §12 de `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` : A12, A18, A24, A25 et A27 y sont réglées, les autres restent ouvertes ; D1C à D4A n'ont aucun lien avec les décisions D01 à D13. « Ouvert » nomme le paramètre qui reste à fixer.

- **Périmètre**
  - **PE-01** — `MEC-0001` garde la marche ordinaire : cheminement, coûts de terrain, diagonales, visibilité du trajet, TU du déplacement ordinaire. Elle conserve S1 à S12, Z1 et N1 à N14, avec une annotation historique de N7, sous réserve d'autorisation d'inscription. Pour les sauts, les chutes et les collisions, `MEC-0002` fait autorité ; N5 à N10 restent dans `MEC-0001` comme historique. [Rattachement de la fiche (LOT-2H, §5 ligne 12) ; primauté confirmée : A24.]
  - **PE-02** — `MEC-0002` couvre le saut simple, l'attaque sautée, les chutes volontaires et involontaires, la trajectoire, les contacts et collisions, la réception, l'esquive réactive, le repoussement, l'impact des corps, la destruction sous impact et la chaîne d'événements associée.
  - **PE-03** — Hors de `MEC-0002` : escaliers, échelles, ascenseurs, règles générales du brouillard, renouvellement global des TU, stabilité structurelle des bâtiments.
  - **PE-04** — Décrire une règle physique utilisable ailleurs n'autorise pas d'autres mécaniques (tir, explosion, destruction de cadavre, vol, apesanteur, etc.).

- **Géométrie, masse et posture**
  - **GE-01** — Positions `(x, y, z)`, plusieurs niveaux. [N3 (R).]
  - **GE-02** — Largeur de case et volumes des unités en proportions, sans mètres fixés. Hauteur d'étage : **3 m** fixes entre deux sols d'étages consécutifs, à distinguer de la montée d'un saut. [DS1.1 ; **précisée** par A3A, qui fixe en mètres la seule hauteur d'étage.] Ouvert : largeur de case, volumes, rapport case/étage.
  - **GE-03** — Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. [DS1.2 ; postures : nouveau.] Ouvert : dimensions par type et posture.
  - **GE-04** — Pendant le vol, posture et orientation du volume sont conservées : pas de rotation des pavés, pas de changement de posture. [nouveau.]
  - **GE-05** — Un contact de surfaces suffit à détecter la rencontre. Sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés, sans créer d'énergie ni dédoubler un impact. [D11 ; contacts : nouveau.] Ouvert : tolérance numérique.
  - **GE-06** — La masse physique totale `M` comprend le corps, l'armure, l'équipement et l'inventaire, en kg. [E23 (P).] Ouvert : masses par type et par objet.
  - **GE-07** — La charge portée, pour la surcharge, comprend l'armure, l'équipement et l'inventaire, en kg ; elle est distincte de `M`. La Force se traduit en capacité de portage en kg, selon un modèle à définir. [N10, N14 (R) ; E20 (LOT-2F).] Ouvert : modèle Force → capacité.
  - **GE-08** — Les unités de plusieurs cases peuvent subir des chutes involontaires et des collisions. Leurs sauts volontaires sont provisoirement indisponibles (« proposition 8/29 »). [étend DS5.5, qui excluait l'attaque sautée faite par ces unités et contre elles.]
  - **GE-09** — Une unité de plusieurs cases n'est pas choisie comme cible d'une attaque sautée. **Maintenue de DS5.5** : la consolidation du 14 novembre ne la redit pas, mais ne la modifie pas ; maintien confirmé par le propriétaire. [DS5.5 ; maintien confirmé : A12.]

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
  - **SA-19** — Référence à 1 g, pour l'unité de référence : sommet à un quart d'étage, soit **0,75 m** avec 3 m par étage ; portée de 2 cases de Manhattan **au même niveau**, pour franchir un trou d'une case ; portée pour un étage de descente **supérieure à 2 cases**, valeur à calculer. Ce sommet de saut n'est pas un seuil de blessure (CH-09). [P04 (M) inchangée ; **remplace** P05 (M) et la portée de DS2.3 ; 0,75 m selon A3A.] Ouvert : valeur de la portée en descente.
  - **SA-20** — À capacités égales, un saut au même niveau a une durée de vol et une portée inférieures à un saut avec un étage de descente. [conséquence de SA-16 à SA-19.]
  - **SA-21** — Portée horizontale `|Δx| + |Δy|`, plafond entier arrondi vers le bas. Aucune portée minimale garantie quand le calcul donne moins d'une case. [P05 (M) ; DS2.2 ; tranche la conversion de E2.]
  - **SA-22** — Distance pour les TU : `d_3D = |Δx| + |Δy| + |Δz|`, distincte de la portée horizontale. [précise DS5.6 (« distance de Manhattan »).]
  - **SA-23** — `TU_simple = d_3D × C_saut`. [nouveau.] Ouvert : `C_saut` ; coût non entier.
  - **SA-24** — `TU_attaque = d_3D × C_saut + max(1, ⌊0,20 × TU_max⌋)`. [J09 (M) ; DS5.6.] Ouvert : `C_saut` ; coût non entier.
  - **SA-25** — `C_saut` est propre aux sauts, indépendant de la marche ; sa valeur est explicitement reportée à l'équilibrage. [E13 (LOT-2F).] Ouvert : valeur.
  - **SA-26** — Coût payé en entier à l'engagement, même si le saut est interrompu ou si la cible esquive ; aucun remboursement. Une chute passive qui suit la destination choisie ne coûte pas de TU en plus. [J09 (M) ; DS5.6.]
  - **SA-27** — Une action sans TU suffisantes est interdite. Destination, coût et trajectoire sont prévisualisés dans les limites des informations connues. [J10, I02 (M).]

- **Chutes et réception**
  - **CH-01** — Un saut volontaire (simple ou offensif), sans surcharge, n'inflige pas de dégâts de réception au sol : au **même niveau**, même si la trajectoire monte puis redescend ; d'**un étage** vers le bas. Pour un saut d'un étage vers le bas, avec ou sans surcharge, la hauteur comptée est l'écart entre le sol de départ et le sol d'arrivée (3 m), sans ajouter la montée au sommet ; en surcharge, cette hauteur est majorée, et des dégâts sont possibles (CH-02, CH-18). Un choc contre une unité est une collision, calculée à part (CH-04). [précise DS3.1 (« volontaire ») ; N7 (R) ; A3A, A4.2A, A4.3A, exception de surcharge : « un étage » défini, saut au même niveau ajouté ; collision calculée à part : A25.]
  - **CH-02** — En surcharge, un saut volontaire d'un étage peut produire des dégâts. [DS3.1, DS3.2 ; confirmé par l'exception de surcharge : dégâts possibles même à 3 m.]
  - **CH-03** — Une chute **involontaire**, prévue ou subie par surprise, suit le seuil de CH-09 : sans surcharge, sans vitesse descendante héritée et sans collision, une chute de 3 m au plus, soit un étage, n'inflige pas de dégâts de chute ; au-delà, des dégâts sont possibles. [**remplace** D01 (M), repris par la consolidation du 14 novembre 2026 (blessure possible dès un étage, même sans surcharge) : A4.1D, D3A ; rejoint DS3.1 pour une chute ordinaire d'un étage.]
  - **CH-04** — Une réception sur une unité est une collision, distincte d'une réception au sol : ses dégâts sont calculés à part, et les deux unités peuvent être blessées, même si la réception de l'unité qui tombe est exemptée (CH-01). Le bonus offensif ne vaut que pour l'attaque sautée. [DS3.4 ; K01, K02, D08 (M) ; **restreint** DS3.1 : l'exemption ne protège pas des dégâts de collision ; confirmé : A25.]
  - **CH-05** — Si la cible esquive, l'attaquant finit son saut au sol : ce saut reste **volontaire**, sa réception est comptée entre le sol de départ et le sol d'arrivée, et l'exemption d'un étage sans surcharge s'applique (CH-01). L'esquive ne transforme pas cette réception en chute involontaire. [E18 (P) ; DS3.1 ; mesure entre les sols : A4.3A.]
  - **CH-06** — Si un obstacle interrompt la trajectoire puis provoque une nouvelle chute, cette chute est **involontaire** ; collision et chute sont comptées séparément. [D13 (M).]
  - **CH-07** — Au-delà du seuil de 3 m, la puissance d'une chute au sol dépend de la hauteur équivalente et de la gravité (CH-10), selon une courbe **à recalibrer lors des tests** ; aucune valeur n'est fixée. [**remplace**, comme barème, la courbe `B(n)` de D03 et D04 (M), reprise par la consolidation du 14 novembre 2026 : D1C ; cette courbe reste historique, sans décalage d'un étage.] Ouvert : courbe et valeurs (A29).
  - **CH-08** — Hauteurs en mètres, fractions comprises, avec 3 m entre deux sols d'étages consécutifs. Trois grandeurs sont distinctes : l'écart entre le sol de départ et le sol d'arrivée ; la trajectoire, avec la montée et le sommet d'un saut ; la hauteur équivalente utilisée pour les dégâts (CH-09 à CH-11, CH-16). Pour une chute, la hauteur parcourue est la hauteur réelle ; pour un saut volontaire, la hauteur comptée suit CH-01 et CH-11. [nouveau ; tranche le comptage de E12 pour les dégâts ; A3A, A4.3A ; l'interpolation linéaire entre les points `B(n)` de la consolidation du 14 novembre 2026 devient historique avec eux.] Ouvert : sauts non couverts par CH-01 (A30).
  - **CH-09** — Seuil des dégâts de chute ordinaires : **3 m inclus** de hauteur équivalente, quelle que soit la gravité positive. Une chute ordinaire de 3 m au plus, sans surcharge ni vitesse descendante héritée, n'inflige aucun dégât de chute ; une collision distincte reste possible (CH-04). Au-delà de 3 m, des dégâts sont possibles, sans être garantis (CH-07). [**remplace** le seuil de 0,25 étage de la consolidation du 14 novembre 2026 et son interpolation : A4.1D, D1C, D3A ; précise N7 (R) ; tranche « moins d'un étage » (DS3).]
  - **CH-10** — En gravité positive, la gravité module les dégâts **au-delà** du seuil de 3 m, sans modifier ce seuil. Le facteur `g/g0`, avec `g0 = 1 g`, reste la référence ; son point d'application et l'absence de double comptage avec la hauteur équivalente (CH-11) sont à vérifier. La précision décimale est gardée jusqu'aux arrondis prévus. [**modifie** D03, qui ne dépendait pas de la gravité ; la gravité ne déplace pas le seuil : D3A.] Ouvert : point d'application, double comptage (A5).
  - **CH-11** — Une vitesse verticale descendante **héritée**, par exemple après la traversée d'un support, accroît la hauteur équivalente, donc les dégâts possibles : `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 3 m porte sur `H_eq`. Pour un saut volontaire d'un étage vers le bas, avec ou sans surcharge, et pour un saut au même niveau sans surcharge, la montée et le sommet ne sont pas ajoutés (CH-01). Pour une autre vitesse initiale montante, la montée, le sommet et la descente sont résolus physiquement, avec la vitesse réelle à l'impact ; l'application de cette règle aux sauts volontaires que CH-01 ne couvre pas (plus d'un étage, même niveau en surcharge), et à un saut exempté qui se poursuit en chute, reste ouverte (A30). [nouveau ; vitesse héritée confirmée : D4A ; le seuil de 0,25 de la consolidation du 14 novembre 2026 est remplacé par celui de 3 m ; montée non comptée : A4.2A, A4.3A.] Ouvert : combinaison avec la surcharge et la gravité (A5) ; tolérance de la comparaison au seuil (A29) ; sauts non couverts par CH-01, saut exempté suivi d'une chute, réception de l'attaquant après un choc (A30).
  - **CH-12** — Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse verticale ; la vitesse horizontale compte contre les surfaces qui lui sont normales. [D11 (M).]
  - **CH-13** — Plafond de puissance de base 70 pour une chute au sol, limite précédemment validée. La surcharge n'agit plus sur la puissance après ce plafond : elle majore la hauteur équivalente (CH-16, CH-17). Les plafonds 60 (unité qui tombe), 80 (cible percutée) et 70 (obstacle) restent pour leurs domaines. Leur interaction avec la courbe à recalibrer, la hauteur majorée et les arrondis reste à vérifier. [D05 (M) ; déroge à D09 (M), qui plaçait les facteurs de poids après le tirage ; la surcharge passe sur la hauteur équivalente : D2A.] Ouvert : interaction avec la courbe, la hauteur majorée et les arrondis ; portée de D1C sur les plafonds (A6, A29).
  - **CH-14** — Capacité de portage en kg selon la Force ; seuil de surcharge commun à N14. [DS3.2 ; N14 (R).] Ouvert : modèle Force → kg.
  - **CH-15** — Dépassement relatif `S = max(0, charge / capacité − 1)`, avec une capacité strictement positive. [nouveau.]
  - **CH-16** — Coefficient `F_surcharge = min(2, 1 + 0,5 × S)`, inchangé. Il majore la hauteur équivalente de chute. [nouveau ; tranche E24 pour le poids au sol ; appliqué à la hauteur équivalente, et non plus à la puissance : D2A.] Ouvert : combinaison avec la vitesse héritée et la gravité (A5) ; portée de D1C sur le plafond 2 (A29).
  - **CH-17** — Pour une chute, ce coefficient n'est appliqué qu'une fois, à la hauteur équivalente : il n'est pas réappliqué à la puissance. La puissance obtenue sert aux blessures et à l'étourdissement ; l'armure applique ensuite ses protections. [N9, N10 (R) ; **remplace**, pour une chute, l'aggravation de la puissance par la surcharge (la consolidation du 14 novembre 2026) : D2A ; collisions : CO-09, A6.]
  - **CH-18** — La surcharge ne supprime pas le seuil de 3 m : elle majore la hauteur équivalente qui lui est comparée. En surcharge, une chute ou un saut d'un étage peut donc blesser, même à 3 m. [nouveau ; le seuil de 0,25 de la consolidation du 14 novembre 2026 est remplacé par celui de 3 m ; exception de surcharge.]
  - **CH-19** — La nature du sol ne modifie pas directement les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol. [D02 (M).]
  - **CH-20** — L'impact peut endommager ou détruire le support ; s'il cède, la chute continue. Chaque impact successif est résolu à part, et les dommages corporels peuvent s'additionner. [D12, D13 (M).]
  - **CH-21** — Traverser une surface destructible absorbe de l'énergie et ralentit le corps ; la gravité peut ensuite le réaccélérer. [nouveau.] Ouvert : formule de perte d'énergie.

- **Collisions et dégâts**
  - **CO-01** — Détection des contacts sur les volumes réels au moment du contact, y compris après un déplacement d'esquive ou une perte de support. [DS1.2.]
  - **CO-02** — Puissance de base `P = K × v_n²`, où `v_n` est la composante normale de la vitesse relative au contact (entre deux unités, ou contre une surface fixe). Deux coefficients distincts et configurables : `K_unités` et `K_obstacles`. [étend DS4.2 aux collisions entre unités ; D10 (M).] Ouvert : `K_unités`, `K_obstacles`.
  - **CO-03** — Entre unités, facteur appliqué aux dégâts reçus par chacune : `F_i = clamp(√(M_autre/M_i), 0,75 ; 1,5)`, masses strictement positives. [DS4.1 ; K08 (M) ; formule E6 du LOT-2G non reprise ; interaction avec le tirage commun réglée : A8A.]
  - **CO-04** — Contre le décor : référence du LOT-2F `min(M/80, 3)` pour le facteur de masse, et plafond de 70. Le point d'insertion de ce facteur dans la nouvelle chaîne reste à revoir. [D10, D05 (M).] Ouvert : point d'insertion (A7).
  - **CO-05** — Type de dégâts « impact » propre à Bastion : zones corporelles exposées et protections d'armure liées à la direction du choc, sans recopier de code ni de données d'OXCE. [DS4.4 ; D07 (LOT-2F, ouverte : E7).] Ouvert : protections par zone.
  - **CO-06** — Blessures et étourdissement sont des effets séparés ; une armure peut protéger plus la santé que l'étourdissement ; on peut être étourdi sans perdre de santé. [K02 (M).] Ouvert : coefficients santé / étourdissement.
  - **CO-07** — Chaque type d'unité a une sensibilité à l'étourdissement ; 0 vaut immunité aux étourdissements d'impact. Une unité consciente mais étourdie peut encore tenter une esquive, avec des Réactions réduites. [nouveau.] Ouvert : pénalité sur les Réactions.
  - **CO-08** — Tirage d'intensité de 50 à 150 %, **une fois par événement de collision**, partagé par les deux unités d'une collision entre unités, ou par l'unité et l'obstacle. Résistances et effets s'appliquent ensuite à chacun. Des collisions réellement distinctes, même rapprochées, ont des tirages distincts. Conséquence assumée : entre deux unités, ce tirage commun ne peut pas, à lui seul, inverser le rapport de leurs puissances avant protections ; leurs protections individuelles s'appliquent ensuite. [D06 (M) ; **étend** DS4.5 aux collisions entre unités ; confirmé, avec son écart à DS4.1 : A8A.] Ouvert : nature et normalisation du tirage (A26).
  - **CO-09** — Ordre : puissance initiale (pour une chute, calculée sur la hauteur équivalente déjà majorée par la surcharge, CH-16) ; facteur de gravité s'il s'applique, au-delà du seuil (CH-10) ; plafond de base ; bonus d'attaque applicable ; arrondi au plus proche, moitié vers le haut ; tirage ; facteur de masse s'il s'applique ; second arrondi ; puis effets et protections séparés pour la santé et l'étourdissement. Pour une chute, la surcharge n'est plus un bonus appliqué à la puissance (CH-17) ; son application éventuelle aux collisions reste ouverte (A6). Surcharge, gravité et masse ne sont comptées qu'une fois chacune ; les termes D09 et D10, et la combinaison de la vitesse héritée, de la surcharge et de la gravité, restent à réconcilier. [DS3.5 ; D10 (M) ; déroge à D09 (M) : la surcharge, facteur lié au poids, précède le tirage ; surcharge sur la hauteur équivalente et gravité au-delà du seuil : D2A, D3A.] Ouvert : réconciliation (A5 à A7) ; détail des deux arrondis et du tirage (A26).
  - **CO-10** — Bonus × 1,25 uniquement sur les dégâts infligés à la cible d'une attaque sautée, après le plafond et avant le tirage ; jamais pour l'attaquant. Une cible alliée ou neutre cachée le reçoit aussi. [J08, J11, J12, D08 (M).]
  - **CO-11** — Contacts simultanés d'un même choc : les surfaces peuvent être endommagées, sans dupliquer la puissance corporelle. Contre plusieurs unités distinctes : un calcul par cible, regroupé au besoin dans un même événement. [nouveau.] Ouvert : détails d'implémentation.

- **Esquives réactives**
  - **ES-01** — Le moteur déclenche la tentative tout seul, sans le joueur ; la réussite n'est pas automatique : elle dépend d'un tirage et des Réactions. [K03, K05 (M) ; DS5.7 ; précision du propriétaire du 14 novembre 2026.]
  - **ES-02** — Conditions : menace vue **juste avant l'impact**, TU suffisantes, case admissible. Une unité qui découvre la menace pendant la chute peut tenter l'esquive. [K03 (M) ; DS5.7.] Ouvert : instant exact (A15).
  - **ES-03** — Bonus de + 10 points si l'unité menacée voyait la menace **dès le départ** du saut ou dès le début d'une chute involontaire ; sinon 0. Même logique pour les corps qui tombent, selon ce que perçoit la cible. [nouveau.]
  - **ES-04** — Bonus de + 5 points par étage, `n = |z_départ − z_arrivée|`, pour une menace qui descend. [K05 (M).] Ouvert : `n` pour un impact à hauteur intermédiaire.
  - **ES-05** — `P = clamp(R_effectif + B_visibilité + 5n, 0, 100)` %, où `R_effectif` est la valeur des Réactions après une éventuelle pénalité d'étourdissement. [K05 (M) ; DS5.7.] Ouvert : pénalité d'étourdissement.
  - **ES-06** — Tirage entier uniforme `t` dans {1, …, 100} ; réussite si `t ≤ P`. [nouveau ; LOT-2G (E12 e) non repris.] Ouvert : `P` non entier.
  - **ES-07** — Une unité inconsciente ou morte n'esquive pas ; les corps qui tombent peuvent, eux, être esquivés. [nouveau.]
  - **ES-08** — Déplacement vers l'une des 8 cases voisines du même niveau, diagonales comprises, avec un support valide ; pas de saut dans le vide en esquivant. [DS5.7.]
  - **ES-09** — Coût habituel de la marche vers la case choisie (terrain, facteur diagonal), payé avec les TU restantes, même pendant le tour adverse. [DS5.7 ; S2 (R).] Ouvert : coûts de terrain (`MEC-0001`).
  - **ES-10** — Esquive réussie et effectivement faite : TU débitées. Échec du tirage ou déplacement impossible : aucun débit. [K06, K07 (M).]
  - **ES-11** — Choix aléatoire uniforme parmi les destinations admissibles. Une information cachée ne permet pas de choisir une case. La découverte d'un obstacle bloque et révèle la tentative, sans débit de TU. [K04 (M) ; tranche E22 (loi uniforme).]
  - **ES-12** — Pas d'échange simultané de cases ni de volumes qui se traversent ; destination libre au début de la résolution. Esquives en conflit : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager au hasard les combinaisons équivalentes. [nouveau.] Ouvert : algorithme (A17).
  - **ES-13** — Plusieurs menaces visibles et simultanées sur une même unité dans un même événement : une seule tentative ; la case doit éviter toutes les menaces **connues** ; `n` vient de la menace visible qui tombe du plus d'étages. Les menaces cachées ne comptent pas dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée. [nouveau.]
  - **ES-14** — Dangers successifs : nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte suit le moteur séquentiel. [nouveau.]

- **Repoussement et retombées**
  - **RP-01** — Esquive réussie : déplacement volontaire, pas de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un repoussement **après** l'impact. [**tranche** le point « à vérifier » K07 (M) / DS5.3 ; confirmé : A27.]
  - **RP-02** — Cible touchée : repoussement en priorité dans la direction de l'impact, sinon vers les directions voisines les plus proches, égalités tirées au hasard. Une case au-dessus du vide est admissible pour un repoussement forcé et entraîne une chute involontaire. [précise DS5.3.]
  - **RP-03** — Une case occupée par une autre unité n'est pas admissible : pas de repoussement en chaîne. [S10 (R).]
  - **RP-04** — Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort garde sa masse et son volume. [tranche « cible hors de combat » (DS5).]
  - **RP-05** — Si la cible ne peut pas être repoussée, l'attaquant cherche une case adjacente (8 voisines) pour retomber, en priorité du côté d'où il vient, puis par proximité de direction ; pas de recherche au-delà. [précise DS5.4 (rayon : cases adjacentes).]
  - **RP-06** — Impossibilité entièrement connue avant l'engagement : l'attaque sautée est refusée, sans révéler de données cachées. Impossibilité révélée en vol : l'attaquant s'arrête au contact, puis retombe verticalement depuis sa dernière position libre, sans pénétrer la cible. [nouveau.] Ouvert : issue de la retombée (A19).
  - **RP-07** — Une collision accidentelle, un cadavre ou un corps inconscient peut repousser ; aucune intention n'est requise, et aucun bonus offensif n'est créé. [nouveau.]
  - **RP-08** — Plusieurs impacts vraiment simultanés : la direction du repoussement combine intensités et directions ; cela n'introduit pas d'attaques volontaires simultanées. [nouveau.]
  - **RP-09** — Après le repoussement de la cible, l'attaquant prend la case initiale de la cible. **Maintenue de DS5.3** : la consolidation du 14 novembre ne la redit pas, mais la suppose (RP-05) ; maintien confirmé par le propriétaire. [DS5.3 ; maintien confirmé : A18.]

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
- D01 (chute blessante possible dès un étage) : remplacée ; une chute ordinaire de 3 m au plus ne blesse pas (CH-03, CH-09).
- D03 et D04 (courbe `B(n)` selon le nombre d'étages, sans gravité) : la courbe n'est plus un barème ; elle reste historique, sans décalage d'un étage ; au-delà de 3 m, la puissance est à recalibrer lors des tests (CH-07) et modulée par la gravité (CH-10).
- D09 (facteurs de poids après le tirage) : pour une chute, la surcharge, facteur lié au poids, majore la hauteur équivalente, donc avant le tirage (CH-13, CH-16, CO-09) ; son effet dans les collisions reste ouvert.
- D12 (résistance du terrain d'OXCE, sans cumul) : modifiée par EN-01 (résistance cumulative).
- DS1.1 (proportions, sans échelle en mètres) : la hauteur d'étage est fixée à 3 m (GE-02).
- DS3.1 (exemption d'un étage sans surcharge) : précisée ; une chute ordinaire de 3 m au plus ne blesse pas (CH-03, CH-09) ; un saut volontaire sans surcharge ne blesse pas à la réception, au même niveau ou d'un étage vers le bas (CH-01) ; l'exemption ne protège pas des dégâts d'une collision avec une unité, calculés à part (CH-04).
- DS4.5 (tirage commun entre l'unité et l'obstacle) : étendu aux collisions entre unités (CO-08) ; l'écart avec DS4.1 est assumé.
- Seuil de 0,25 étage, interpolation jusqu'à la base 8 et multiplicateur de surcharge appliqué à la puissance d'une chute, proposés par la consolidation du 14 novembre 2026 : remplacés le même jour par le seuil de 3 m (CH-09) et par la majoration de la hauteur équivalente (CH-16, CH-17).
- DS5.5 (grandes unités exclues de l'attaque sautée, comme sauteurs et comme cibles) : étendu à tout saut volontaire (GE-08) ; l'exclusion comme cible est maintenue (GE-09).
- DS5.3 (l'attaquant prend la case de la cible repoussée) : maintenue (RP-09).
- DS5.6 (coût proportionnel à la distance de Manhattan) : distance 3D pour les TU, et saut simple sans supplément (SA-22 à SA-24).
- Recommandation E11 du LOT-2G (même vitesse pour toutes les masses) : écartée par SA-16.

#### Encore ouvert

- Géométrie : largeur de case et rapport case/étage (la hauteur d'étage est fixée à 3 m) ; dimensions des unités par type et par posture ; épaisseur des surfaces ; tolérance des contacts.
- Sauts : masses et capacités de référence par type ; calibrage horizontal et portée en descente ; plage de gravité par type et très faible gravité ; valeur de `C_saut` ; coût en TU non entier.
- Force et charge : capacité de portage en kg selon la Force ; cohérence avec N14 ; masses des corps et des objets.
- Chutes : courbe de puissance au-delà de 3 m, à recalibrer lors des tests, et portée de ce recalibrage sur les plafonds de puissance et sur le plafond 2 de `F_surcharge` ; tolérance numérique de la comparaison au seuil quand la hauteur équivalente est calculée ; combinaison de la vitesse héritée, de la surcharge et de la gravité (ordre, point d'application de `g/g0`, absence de double comptage) ; hauteur comptée pour un saut volontaire de plus d'un étage et pour un saut au même niveau en surcharge ; suite d'un saut exempté qui se poursuit en chute, si le support de réception cède ou si la destination est sans support ; réception de l'attaquant après un choc contre sa cible : réception exemptée, ou chute consécutive distincte avec vitesse résiduelle.
- Dégâts : `K_unités`, `K_obstacles` ; absorption d'énergie des planchers ; conversion de la résistance en énergie ; protections par zone et direction ; coefficients de santé et d'étourdissement ; pénalité d'étourdissement sur les Réactions.
- Chaîne de calcul : place de `min(M/80, 3)` contre le décor ; surcharge dans les collisions ; interaction des plafonds 60, 70 et 80 avec les bonus, la gravité et la hauteur majorée par la surcharge ; nature et normalisation du tirage de 50 à 150 % ; détail des deux arrondis ; limites numériques éventuelles ; double comptage de la gravité, de la vitesse et de la masse.
- Vitesse après un choc qui interrompt le saut, et vitesse résiduelle après la traversée d'une surface.
- Esquive : instant où la menace est « vue » ; `n` pour un impact à hauteur intermédiaire ; probabilité non entière ; algorithme des esquives en conflit.
- Repoussement : retombée verticale de l'attaquant au-dessus de la cible (RP-06).
- Événements : ordre FIFO des chutes et chronologie physique ; clé d'ordre stable ; emplacement des cadavres ; collisions imbriquées et multi-cibles ; nombre maximal d'événements en chaîne.
- Décor : propriétés destructible ou indestructible, résistances initiales, unité des dégâts du terrain.
- Marche et TU : coûts des cases, capital et renouvellement des TU, visibilité, sous la responsabilité de `MEC-0001`.
- Décisions du 9 novembre 2026 et correctif du propriétaire (LOT-2F) : reprises ici par leurs identifiants, sans inscription propre.

Cette liste n'est pas exhaustive : tout ce que PE-01 à EN-10 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.

## 3. Diff exact proposé

Diff unifié (contexte d'une ligne) du registre de `main` vers le texte proposé. **Il n'est pas appliqué.** Les lignes de contexte vides y sont sans espace initial ; `git apply` et `patch` les acceptent (contrôles dans `LOT-2I-EXECUTION.md` ; §9 pour le correctif v1.2).

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
+- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] Précisée par `MEC-0002`, qui fait autorité pour les sauts et les chutes : pas de dégâts de chute ordinaires jusqu'à 3 m inclus de hauteur équivalente (CH-09) ; voir aussi CH-01 (saut volontaire) et CH-03 (chute involontaire). *(Annotation ajoutée lors de l'inscription de `MEC-0002`.)*
 - **N8** — Les caractéristiques individuelles et les équipements peuvent modifier les conséquences d'une chute. [À vérifier.]
@@ -100,2 +100,3 @@
 - **N10** — Le poids de l'inventaire (armes, munitions, matériel) contribue aussi à l'effet de la charge lors d'une chute. [Effet sur les chutes : à vérifier. Vérifié : dans OXCE, le poids porté est le poids de l'armure plus celui des objets de l'inventaire (`src/Savegame/BattleUnit.cpp:4852-4861`).]
+  *(Annotation ajoutée lors de l'inscription de `MEC-0002` : pour les sauts, les chutes et leurs conséquences, N5 à N10 sont précisées par `MEC-0002`, qui fait autorité ; leur texte est conservé ici comme historique.)*
 - **N11** — Le poids total porté affecte aussi le déplacement normal. [Vérifié : dans OXCE, l'effet est indirect, par la réduction des TU, qui touche toutes les actions ; voir N12 à N14.]
@@ -120,3 +121,4 @@
   - hauteur de chute sans dégâts ;
-  - effet précis des caractéristiques, équipements, armure et charge.
+  - effet précis des caractéristiques, équipements, armure et charge ;
+  - ces points sont précisés ou tranchés en partie par `MEC-0002`, qui fait autorité (seuil sans dégâts : 3 m inclus, CH-09) ; les points qui restent ouverts y sont listés.
 - Surcharge : transposition exacte du principe d'OXCE (formule, arrondi, ordre avec les autres pénalités) ; présentation de l'indicateur « encombré ».
@@ -133 +135,180 @@
 L'hypothèse provisoire du LOT-2B « toutes les unités sont connues » n'est pas retenue : S6 à S9 introduisent les cases explorées et le terrain mémorisé, S11 et S12 les unités cachées.
+
+### MEC-0002 — Sauts, chutes et collisions
+
+**Fiche de conception incomplète. Des principes de conception sont acceptés (PE-01 à EN-10, du 14 novembre 2026, sauf GE-09 et RP-09, du 13 novembre 2026, dont le maintien a été confirmé le 14 novembre 2026), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**
+
+| Champ | Valeur |
+|---|---|
+| Système | Combat tactique : sauts simples et attaques sautées, chutes volontaires et involontaires, trajectoire balistique, collisions, réception, esquives réactives, repoussements, destruction sous impact et chaîne d'événements associée. |
+| Description | Une unité peut sauter vers une case admissible, tomber, heurter des unités ou le décor, esquiver une unité qui tombe ou être repoussée. Règles partielles ci-dessous. |
+| Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
+| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** ; aucun calcul de dégâts de chute n'y a été identifié (`docs/reviews/LOT-2E-VERTICALITE-OXCE.md`, C8). Les règles ci-dessous sont des adaptations de Bastion, sans reprise de code, de données ni d'assets (D4). Spécification : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Arbitrage : `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. Principes DS1 à DS5 : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`. Consolidation : `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` et `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`. |
+| Changement demandé | Fixer les sauts, chutes et collisions de Bastion à partir des principes PE-01 à EN-10 ci-dessous. Les points encore ouverts sont listés plus bas. |
+| Décision du propriétaire | reportée — inscription partielle des principes de conception. Principes acceptés le 14 novembre 2026 : 29 propositions et arbitrages complémentaires 1A à 6A, consolidés dans `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` (branche `orchestration/mandats`, commit `d028c52f500ed8daeca917adbcb9a9e1eb3ff8bd`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`). Preuve : déclaration du propriétaire du 14 novembre 2026 (preuve déclarative), qui précise que les esquives sont des tentatives automatiques dont la réussite dépend d'un tirage et des Réactions. Le même jour, arbitrages complémentaires du propriétaire sur la hauteur d'étage (3 m), le seuil de chute sans dégâts (3 m inclus), la surcharge, la gravité et la vitesse héritée, et confirmation des huit points laissés à confirmer par le LOT-2I ; ils sont transcrits par l'orchestrateur dans `docs/mandates/BASTION-MANDAT-LOT-2I-v1.2-CORRECTIF-MEC-0002.md` (branche `orchestration/mandats`, commit `f8cf26e38783499a23244f823da4e221d4a95992`, SHA-256 `e4c5345a324ed4e5eb9cab294c7af900b34c389cb0ea8e25e943da400ace5ba0`), preuve déclarative, et prévalent sur la consolidation là où ils la modifient. GE-09 et RP-09 reprennent DS5.5 et DS5.3 (13 novembre 2026), que la consolidation ne modifie pas ; leur maintien a été confirmé le 14 novembre 2026. Ces principes reprennent ou modifient les décisions du 9 novembre 2026 et le correctif du propriétaire (identifiants du LOT-2F), ainsi que les principes DS1 à DS5 du 13 novembre 2026. |
+| Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
+| Éléments exclus | Tous les points listés sous « Encore ouvert » ; escaliers, échelles et ascenseurs ; règles générales du brouillard ; renouvellement des TU ; stabilité structurelle des bâtiments ; toute autre mécanique (tir, explosion, destruction de cadavre, vol, apesanteur). |
+| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` §3). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
+| Tests de modification | Critères futurs seulement. Aucun test écrit ni exécuté. |
+| État d'implémentation | non commencé |
+
+#### Principes de conception acceptés le 14 novembre 2026
+
+Ils n'autorisent, seuls, aucun gameplay. Les identifiants PE, GE, SA, CH, CO, ES, RP et EN ont été proposés par le LOT-2I. Entre crochets, la décision antérieure reprise, précisée ou modifiée. S, Z et N renvoient à `MEC-0001` (R : registre). Les autres identifiants (J, K, D, I, P, E) renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` (M : décision du 9 novembre 2026 ; P : correctif du propriétaire). DS*n*.*m* renvoie à la consolidation DS1 à DS5 du 13 novembre 2026. A3A, A4.1D, A4.2A, A4.3A, A8A, D1C, D2A, D3A, D4A et « exception de surcharge » désignent les arbitrages complémentaires du 14 novembre 2026, et A12, A18, A24, A25, A27 les points du LOT-2I confirmés le même jour (mandat LOT-2I v1.2, §2). Un renvoi A*n* seul (A5, A6, A7, A15, A17, A19, A26, A29, A30, etc.) désigne l'ambiguïté du même numéro, au §12 de `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` : A12, A18, A24, A25 et A27 y sont réglées, les autres restent ouvertes ; D1C à D4A n'ont aucun lien avec les décisions D01 à D13. « Ouvert » nomme le paramètre qui reste à fixer.
+
+- **Périmètre**
+  - **PE-01** — `MEC-0001` garde la marche ordinaire : cheminement, coûts de terrain, diagonales, visibilité du trajet, TU du déplacement ordinaire. Elle conserve S1 à S12, Z1 et N1 à N14, avec une annotation historique de N7, sous réserve d'autorisation d'inscription. Pour les sauts, les chutes et les collisions, `MEC-0002` fait autorité ; N5 à N10 restent dans `MEC-0001` comme historique. [Rattachement de la fiche (LOT-2H, §5 ligne 12) ; primauté confirmée : A24.]
+  - **PE-02** — `MEC-0002` couvre le saut simple, l'attaque sautée, les chutes volontaires et involontaires, la trajectoire, les contacts et collisions, la réception, l'esquive réactive, le repoussement, l'impact des corps, la destruction sous impact et la chaîne d'événements associée.
+  - **PE-03** — Hors de `MEC-0002` : escaliers, échelles, ascenseurs, règles générales du brouillard, renouvellement global des TU, stabilité structurelle des bâtiments.
+  - **PE-04** — Décrire une règle physique utilisable ailleurs n'autorise pas d'autres mécaniques (tir, explosion, destruction de cadavre, vol, apesanteur, etc.).
+
+- **Géométrie, masse et posture**
+  - **GE-01** — Positions `(x, y, z)`, plusieurs niveaux. [N3 (R).]
+  - **GE-02** — Largeur de case et volumes des unités en proportions, sans mètres fixés. Hauteur d'étage : **3 m** fixes entre deux sols d'étages consécutifs, à distinguer de la montée d'un saut. [DS1.1 ; **précisée** par A3A, qui fixe en mètres la seule hauteur d'étage.] Ouvert : largeur de case, volumes, rapport case/étage.
+  - **GE-03** — Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. [DS1.2 ; postures : nouveau.] Ouvert : dimensions par type et posture.
+  - **GE-04** — Pendant le vol, posture et orientation du volume sont conservées : pas de rotation des pavés, pas de changement de posture. [nouveau.]
+  - **GE-05** — Un contact de surfaces suffit à détecter la rencontre. Sans composante de vitesse dirigée vers la surface, pas de dégât d'impact normal. Les contacts simultanés sont agrégés, sans créer d'énergie ni dédoubler un impact. [D11 ; contacts : nouveau.] Ouvert : tolérance numérique.
+  - **GE-06** — La masse physique totale `M` comprend le corps, l'armure, l'équipement et l'inventaire, en kg. [E23 (P).] Ouvert : masses par type et par objet.
+  - **GE-07** — La charge portée, pour la surcharge, comprend l'armure, l'équipement et l'inventaire, en kg ; elle est distincte de `M`. La Force se traduit en capacité de portage en kg, selon un modèle à définir. [N10, N14 (R) ; E20 (LOT-2F).] Ouvert : modèle Force → capacité.
+  - **GE-08** — Les unités de plusieurs cases peuvent subir des chutes involontaires et des collisions. Leurs sauts volontaires sont provisoirement indisponibles (« proposition 8/29 »). [étend DS5.5, qui excluait l'attaque sautée faite par ces unités et contre elles.]
+  - **GE-09** — Une unité de plusieurs cases n'est pas choisie comme cible d'une attaque sautée. **Maintenue de DS5.5** : la consolidation du 14 novembre ne la redit pas, mais ne la modifie pas ; maintien confirmé par le propriétaire. [DS5.5 ; maintien confirmé : A12.]
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
+  - **SA-19** — Référence à 1 g, pour l'unité de référence : sommet à un quart d'étage, soit **0,75 m** avec 3 m par étage ; portée de 2 cases de Manhattan **au même niveau**, pour franchir un trou d'une case ; portée pour un étage de descente **supérieure à 2 cases**, valeur à calculer. Ce sommet de saut n'est pas un seuil de blessure (CH-09). [P04 (M) inchangée ; **remplace** P05 (M) et la portée de DS2.3 ; 0,75 m selon A3A.] Ouvert : valeur de la portée en descente.
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
+  - **CH-01** — Un saut volontaire (simple ou offensif), sans surcharge, n'inflige pas de dégâts de réception au sol : au **même niveau**, même si la trajectoire monte puis redescend ; d'**un étage** vers le bas. Pour un saut d'un étage vers le bas, avec ou sans surcharge, la hauteur comptée est l'écart entre le sol de départ et le sol d'arrivée (3 m), sans ajouter la montée au sommet ; en surcharge, cette hauteur est majorée, et des dégâts sont possibles (CH-02, CH-18). Un choc contre une unité est une collision, calculée à part (CH-04). [précise DS3.1 (« volontaire ») ; N7 (R) ; A3A, A4.2A, A4.3A, exception de surcharge : « un étage » défini, saut au même niveau ajouté ; collision calculée à part : A25.]
+  - **CH-02** — En surcharge, un saut volontaire d'un étage peut produire des dégâts. [DS3.1, DS3.2 ; confirmé par l'exception de surcharge : dégâts possibles même à 3 m.]
+  - **CH-03** — Une chute **involontaire**, prévue ou subie par surprise, suit le seuil de CH-09 : sans surcharge, sans vitesse descendante héritée et sans collision, une chute de 3 m au plus, soit un étage, n'inflige pas de dégâts de chute ; au-delà, des dégâts sont possibles. [**remplace** D01 (M), repris par la consolidation du 14 novembre 2026 (blessure possible dès un étage, même sans surcharge) : A4.1D, D3A ; rejoint DS3.1 pour une chute ordinaire d'un étage.]
+  - **CH-04** — Une réception sur une unité est une collision, distincte d'une réception au sol : ses dégâts sont calculés à part, et les deux unités peuvent être blessées, même si la réception de l'unité qui tombe est exemptée (CH-01). Le bonus offensif ne vaut que pour l'attaque sautée. [DS3.4 ; K01, K02, D08 (M) ; **restreint** DS3.1 : l'exemption ne protège pas des dégâts de collision ; confirmé : A25.]
+  - **CH-05** — Si la cible esquive, l'attaquant finit son saut au sol : ce saut reste **volontaire**, sa réception est comptée entre le sol de départ et le sol d'arrivée, et l'exemption d'un étage sans surcharge s'applique (CH-01). L'esquive ne transforme pas cette réception en chute involontaire. [E18 (P) ; DS3.1 ; mesure entre les sols : A4.3A.]
+  - **CH-06** — Si un obstacle interrompt la trajectoire puis provoque une nouvelle chute, cette chute est **involontaire** ; collision et chute sont comptées séparément. [D13 (M).]
+  - **CH-07** — Au-delà du seuil de 3 m, la puissance d'une chute au sol dépend de la hauteur équivalente et de la gravité (CH-10), selon une courbe **à recalibrer lors des tests** ; aucune valeur n'est fixée. [**remplace**, comme barème, la courbe `B(n)` de D03 et D04 (M), reprise par la consolidation du 14 novembre 2026 : D1C ; cette courbe reste historique, sans décalage d'un étage.] Ouvert : courbe et valeurs (A29).
+  - **CH-08** — Hauteurs en mètres, fractions comprises, avec 3 m entre deux sols d'étages consécutifs. Trois grandeurs sont distinctes : l'écart entre le sol de départ et le sol d'arrivée ; la trajectoire, avec la montée et le sommet d'un saut ; la hauteur équivalente utilisée pour les dégâts (CH-09 à CH-11, CH-16). Pour une chute, la hauteur parcourue est la hauteur réelle ; pour un saut volontaire, la hauteur comptée suit CH-01 et CH-11. [nouveau ; tranche le comptage de E12 pour les dégâts ; A3A, A4.3A ; l'interpolation linéaire entre les points `B(n)` de la consolidation du 14 novembre 2026 devient historique avec eux.] Ouvert : sauts non couverts par CH-01 (A30).
+  - **CH-09** — Seuil des dégâts de chute ordinaires : **3 m inclus** de hauteur équivalente, quelle que soit la gravité positive. Une chute ordinaire de 3 m au plus, sans surcharge ni vitesse descendante héritée, n'inflige aucun dégât de chute ; une collision distincte reste possible (CH-04). Au-delà de 3 m, des dégâts sont possibles, sans être garantis (CH-07). [**remplace** le seuil de 0,25 étage de la consolidation du 14 novembre 2026 et son interpolation : A4.1D, D1C, D3A ; précise N7 (R) ; tranche « moins d'un étage » (DS3).]
+  - **CH-10** — En gravité positive, la gravité module les dégâts **au-delà** du seuil de 3 m, sans modifier ce seuil. Le facteur `g/g0`, avec `g0 = 1 g`, reste la référence ; son point d'application et l'absence de double comptage avec la hauteur équivalente (CH-11) sont à vérifier. La précision décimale est gardée jusqu'aux arrondis prévus. [**modifie** D03, qui ne dépendait pas de la gravité ; la gravité ne déplace pas le seuil : D3A.] Ouvert : point d'application, double comptage (A5).
+  - **CH-11** — Une vitesse verticale descendante **héritée**, par exemple après la traversée d'un support, accroît la hauteur équivalente, donc les dégâts possibles : `H_eq = H_parcourue + v0²/(2g)`, pour `g > 0`. Le seuil de 3 m porte sur `H_eq`. Pour un saut volontaire d'un étage vers le bas, avec ou sans surcharge, et pour un saut au même niveau sans surcharge, la montée et le sommet ne sont pas ajoutés (CH-01). Pour une autre vitesse initiale montante, la montée, le sommet et la descente sont résolus physiquement, avec la vitesse réelle à l'impact ; l'application de cette règle aux sauts volontaires que CH-01 ne couvre pas (plus d'un étage, même niveau en surcharge), et à un saut exempté qui se poursuit en chute, reste ouverte (A30). [nouveau ; vitesse héritée confirmée : D4A ; le seuil de 0,25 de la consolidation du 14 novembre 2026 est remplacé par celui de 3 m ; montée non comptée : A4.2A, A4.3A.] Ouvert : combinaison avec la surcharge et la gravité (A5) ; tolérance de la comparaison au seuil (A29) ; sauts non couverts par CH-01, saut exempté suivi d'une chute, réception de l'attaquant après un choc (A30).
+  - **CH-12** — Sur un sol horizontal, les dégâts de réception n'utilisent que la vitesse verticale ; la vitesse horizontale compte contre les surfaces qui lui sont normales. [D11 (M).]
+  - **CH-13** — Plafond de puissance de base 70 pour une chute au sol, limite précédemment validée. La surcharge n'agit plus sur la puissance après ce plafond : elle majore la hauteur équivalente (CH-16, CH-17). Les plafonds 60 (unité qui tombe), 80 (cible percutée) et 70 (obstacle) restent pour leurs domaines. Leur interaction avec la courbe à recalibrer, la hauteur majorée et les arrondis reste à vérifier. [D05 (M) ; déroge à D09 (M), qui plaçait les facteurs de poids après le tirage ; la surcharge passe sur la hauteur équivalente : D2A.] Ouvert : interaction avec la courbe, la hauteur majorée et les arrondis ; portée de D1C sur les plafonds (A6, A29).
+  - **CH-14** — Capacité de portage en kg selon la Force ; seuil de surcharge commun à N14. [DS3.2 ; N14 (R).] Ouvert : modèle Force → kg.
+  - **CH-15** — Dépassement relatif `S = max(0, charge / capacité − 1)`, avec une capacité strictement positive. [nouveau.]
+  - **CH-16** — Coefficient `F_surcharge = min(2, 1 + 0,5 × S)`, inchangé. Il majore la hauteur équivalente de chute. [nouveau ; tranche E24 pour le poids au sol ; appliqué à la hauteur équivalente, et non plus à la puissance : D2A.] Ouvert : combinaison avec la vitesse héritée et la gravité (A5) ; portée de D1C sur le plafond 2 (A29).
+  - **CH-17** — Pour une chute, ce coefficient n'est appliqué qu'une fois, à la hauteur équivalente : il n'est pas réappliqué à la puissance. La puissance obtenue sert aux blessures et à l'étourdissement ; l'armure applique ensuite ses protections. [N9, N10 (R) ; **remplace**, pour une chute, l'aggravation de la puissance par la surcharge (la consolidation du 14 novembre 2026) : D2A ; collisions : CO-09, A6.]
+  - **CH-18** — La surcharge ne supprime pas le seuil de 3 m : elle majore la hauteur équivalente qui lui est comparée. En surcharge, une chute ou un saut d'un étage peut donc blesser, même à 3 m. [nouveau ; le seuil de 0,25 de la consolidation du 14 novembre 2026 est remplacé par celui de 3 m ; exception de surcharge.]
+  - **CH-19** — La nature du sol ne modifie pas directement les dégâts de chute reçus : pas de coefficient d'amortissement par type de sol. [D02 (M).]
+  - **CH-20** — L'impact peut endommager ou détruire le support ; s'il cède, la chute continue. Chaque impact successif est résolu à part, et les dommages corporels peuvent s'additionner. [D12, D13 (M).]
+  - **CH-21** — Traverser une surface destructible absorbe de l'énergie et ralentit le corps ; la gravité peut ensuite le réaccélérer. [nouveau.] Ouvert : formule de perte d'énergie.
+
+- **Collisions et dégâts**
+  - **CO-01** — Détection des contacts sur les volumes réels au moment du contact, y compris après un déplacement d'esquive ou une perte de support. [DS1.2.]
+  - **CO-02** — Puissance de base `P = K × v_n²`, où `v_n` est la composante normale de la vitesse relative au contact (entre deux unités, ou contre une surface fixe). Deux coefficients distincts et configurables : `K_unités` et `K_obstacles`. [étend DS4.2 aux collisions entre unités ; D10 (M).] Ouvert : `K_unités`, `K_obstacles`.
+  - **CO-03** — Entre unités, facteur appliqué aux dégâts reçus par chacune : `F_i = clamp(√(M_autre/M_i), 0,75 ; 1,5)`, masses strictement positives. [DS4.1 ; K08 (M) ; formule E6 du LOT-2G non reprise ; interaction avec le tirage commun réglée : A8A.]
+  - **CO-04** — Contre le décor : référence du LOT-2F `min(M/80, 3)` pour le facteur de masse, et plafond de 70. Le point d'insertion de ce facteur dans la nouvelle chaîne reste à revoir. [D10, D05 (M).] Ouvert : point d'insertion (A7).
+  - **CO-05** — Type de dégâts « impact » propre à Bastion : zones corporelles exposées et protections d'armure liées à la direction du choc, sans recopier de code ni de données d'OXCE. [DS4.4 ; D07 (LOT-2F, ouverte : E7).] Ouvert : protections par zone.
+  - **CO-06** — Blessures et étourdissement sont des effets séparés ; une armure peut protéger plus la santé que l'étourdissement ; on peut être étourdi sans perdre de santé. [K02 (M).] Ouvert : coefficients santé / étourdissement.
+  - **CO-07** — Chaque type d'unité a une sensibilité à l'étourdissement ; 0 vaut immunité aux étourdissements d'impact. Une unité consciente mais étourdie peut encore tenter une esquive, avec des Réactions réduites. [nouveau.] Ouvert : pénalité sur les Réactions.
+  - **CO-08** — Tirage d'intensité de 50 à 150 %, **une fois par événement de collision**, partagé par les deux unités d'une collision entre unités, ou par l'unité et l'obstacle. Résistances et effets s'appliquent ensuite à chacun. Des collisions réellement distinctes, même rapprochées, ont des tirages distincts. Conséquence assumée : entre deux unités, ce tirage commun ne peut pas, à lui seul, inverser le rapport de leurs puissances avant protections ; leurs protections individuelles s'appliquent ensuite. [D06 (M) ; **étend** DS4.5 aux collisions entre unités ; confirmé, avec son écart à DS4.1 : A8A.] Ouvert : nature et normalisation du tirage (A26).
+  - **CO-09** — Ordre : puissance initiale (pour une chute, calculée sur la hauteur équivalente déjà majorée par la surcharge, CH-16) ; facteur de gravité s'il s'applique, au-delà du seuil (CH-10) ; plafond de base ; bonus d'attaque applicable ; arrondi au plus proche, moitié vers le haut ; tirage ; facteur de masse s'il s'applique ; second arrondi ; puis effets et protections séparés pour la santé et l'étourdissement. Pour une chute, la surcharge n'est plus un bonus appliqué à la puissance (CH-17) ; son application éventuelle aux collisions reste ouverte (A6). Surcharge, gravité et masse ne sont comptées qu'une fois chacune ; les termes D09 et D10, et la combinaison de la vitesse héritée, de la surcharge et de la gravité, restent à réconcilier. [DS3.5 ; D10 (M) ; déroge à D09 (M) : la surcharge, facteur lié au poids, précède le tirage ; surcharge sur la hauteur équivalente et gravité au-delà du seuil : D2A, D3A.] Ouvert : réconciliation (A5 à A7) ; détail des deux arrondis et du tirage (A26).
+  - **CO-10** — Bonus × 1,25 uniquement sur les dégâts infligés à la cible d'une attaque sautée, après le plafond et avant le tirage ; jamais pour l'attaquant. Une cible alliée ou neutre cachée le reçoit aussi. [J08, J11, J12, D08 (M).]
+  - **CO-11** — Contacts simultanés d'un même choc : les surfaces peuvent être endommagées, sans dupliquer la puissance corporelle. Contre plusieurs unités distinctes : un calcul par cible, regroupé au besoin dans un même événement. [nouveau.] Ouvert : détails d'implémentation.
+
+- **Esquives réactives**
+  - **ES-01** — Le moteur déclenche la tentative tout seul, sans le joueur ; la réussite n'est pas automatique : elle dépend d'un tirage et des Réactions. [K03, K05 (M) ; DS5.7 ; précision du propriétaire du 14 novembre 2026.]
+  - **ES-02** — Conditions : menace vue **juste avant l'impact**, TU suffisantes, case admissible. Une unité qui découvre la menace pendant la chute peut tenter l'esquive. [K03 (M) ; DS5.7.] Ouvert : instant exact (A15).
+  - **ES-03** — Bonus de + 10 points si l'unité menacée voyait la menace **dès le départ** du saut ou dès le début d'une chute involontaire ; sinon 0. Même logique pour les corps qui tombent, selon ce que perçoit la cible. [nouveau.]
+  - **ES-04** — Bonus de + 5 points par étage, `n = |z_départ − z_arrivée|`, pour une menace qui descend. [K05 (M).] Ouvert : `n` pour un impact à hauteur intermédiaire.
+  - **ES-05** — `P = clamp(R_effectif + B_visibilité + 5n, 0, 100)` %, où `R_effectif` est la valeur des Réactions après une éventuelle pénalité d'étourdissement. [K05 (M) ; DS5.7.] Ouvert : pénalité d'étourdissement.
+  - **ES-06** — Tirage entier uniforme `t` dans {1, …, 100} ; réussite si `t ≤ P`. [nouveau ; LOT-2G (E12 e) non repris.] Ouvert : `P` non entier.
+  - **ES-07** — Une unité inconsciente ou morte n'esquive pas ; les corps qui tombent peuvent, eux, être esquivés. [nouveau.]
+  - **ES-08** — Déplacement vers l'une des 8 cases voisines du même niveau, diagonales comprises, avec un support valide ; pas de saut dans le vide en esquivant. [DS5.7.]
+  - **ES-09** — Coût habituel de la marche vers la case choisie (terrain, facteur diagonal), payé avec les TU restantes, même pendant le tour adverse. [DS5.7 ; S2 (R).] Ouvert : coûts de terrain (`MEC-0001`).
+  - **ES-10** — Esquive réussie et effectivement faite : TU débitées. Échec du tirage ou déplacement impossible : aucun débit. [K06, K07 (M).]
+  - **ES-11** — Choix aléatoire uniforme parmi les destinations admissibles. Une information cachée ne permet pas de choisir une case. La découverte d'un obstacle bloque et révèle la tentative, sans débit de TU. [K04 (M) ; tranche E22 (loi uniforme).]
+  - **ES-12** — Pas d'échange simultané de cases ni de volumes qui se traversent ; destination libre au début de la résolution. Esquives en conflit : tirer d'abord les réussites individuelles, chercher la combinaison de déplacements compatibles qui maximise leur nombre, départager au hasard les combinaisons équivalentes. [nouveau.] Ouvert : algorithme (A17).
+  - **ES-13** — Plusieurs menaces visibles et simultanées sur une même unité dans un même événement : une seule tentative ; la case doit éviter toutes les menaces **connues** ; `n` vient de la menace visible qui tombe du plus d'étages. Les menaces cachées ne comptent pas dans le choix ; une esquive peut malgré tout éviter ou rencontrer une menace cachée. [nouveau.]
+  - **ES-14** — Dangers successifs : nouvelle tentative permise tant que TU et destination restent disponibles ; une menace distincte suit le moteur séquentiel. [nouveau.]
+
+- **Repoussement et retombées**
+  - **RP-01** — Esquive réussie : déplacement volontaire, pas de repoussement. Esquive échouée : aucun déplacement d'esquive, mais la collision peut provoquer un repoussement **après** l'impact. [**tranche** le point « à vérifier » K07 (M) / DS5.3 ; confirmé : A27.]
+  - **RP-02** — Cible touchée : repoussement en priorité dans la direction de l'impact, sinon vers les directions voisines les plus proches, égalités tirées au hasard. Une case au-dessus du vide est admissible pour un repoussement forcé et entraîne une chute involontaire. [précise DS5.3.]
+  - **RP-03** — Une case occupée par une autre unité n'est pas admissible : pas de repoussement en chaîne. [S10 (R).]
+  - **RP-04** — Une cible mise hors de combat par le choc peut encore être repoussée ; un corps inconscient ou mort garde sa masse et son volume. [tranche « cible hors de combat » (DS5).]
+  - **RP-05** — Si la cible ne peut pas être repoussée, l'attaquant cherche une case adjacente (8 voisines) pour retomber, en priorité du côté d'où il vient, puis par proximité de direction ; pas de recherche au-delà. [précise DS5.4 (rayon : cases adjacentes).]
+  - **RP-06** — Impossibilité entièrement connue avant l'engagement : l'attaque sautée est refusée, sans révéler de données cachées. Impossibilité révélée en vol : l'attaquant s'arrête au contact, puis retombe verticalement depuis sa dernière position libre, sans pénétrer la cible. [nouveau.] Ouvert : issue de la retombée (A19).
+  - **RP-07** — Une collision accidentelle, un cadavre ou un corps inconscient peut repousser ; aucune intention n'est requise, et aucun bonus offensif n'est créé. [nouveau.]
+  - **RP-08** — Plusieurs impacts vraiment simultanés : la direction du repoussement combine intensités et directions ; cela n'introduit pas d'attaques volontaires simultanées. [nouveau.]
+  - **RP-09** — Après le repoussement de la cible, l'attaquant prend la case initiale de la cible. **Maintenue de DS5.3** : la consolidation du 14 novembre ne la redit pas, mais la suppose (RP-05) ; maintien confirmé par le propriétaire. [DS5.3 ; maintien confirmé : A18.]
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
+- D01 (chute blessante possible dès un étage) : remplacée ; une chute ordinaire de 3 m au plus ne blesse pas (CH-03, CH-09).
+- D03 et D04 (courbe `B(n)` selon le nombre d'étages, sans gravité) : la courbe n'est plus un barème ; elle reste historique, sans décalage d'un étage ; au-delà de 3 m, la puissance est à recalibrer lors des tests (CH-07) et modulée par la gravité (CH-10).
+- D09 (facteurs de poids après le tirage) : pour une chute, la surcharge, facteur lié au poids, majore la hauteur équivalente, donc avant le tirage (CH-13, CH-16, CO-09) ; son effet dans les collisions reste ouvert.
+- D12 (résistance du terrain d'OXCE, sans cumul) : modifiée par EN-01 (résistance cumulative).
+- DS1.1 (proportions, sans échelle en mètres) : la hauteur d'étage est fixée à 3 m (GE-02).
+- DS3.1 (exemption d'un étage sans surcharge) : précisée ; une chute ordinaire de 3 m au plus ne blesse pas (CH-03, CH-09) ; un saut volontaire sans surcharge ne blesse pas à la réception, au même niveau ou d'un étage vers le bas (CH-01) ; l'exemption ne protège pas des dégâts d'une collision avec une unité, calculés à part (CH-04).
+- DS4.5 (tirage commun entre l'unité et l'obstacle) : étendu aux collisions entre unités (CO-08) ; l'écart avec DS4.1 est assumé.
+- Seuil de 0,25 étage, interpolation jusqu'à la base 8 et multiplicateur de surcharge appliqué à la puissance d'une chute, proposés par la consolidation du 14 novembre 2026 : remplacés le même jour par le seuil de 3 m (CH-09) et par la majoration de la hauteur équivalente (CH-16, CH-17).
+- DS5.5 (grandes unités exclues de l'attaque sautée, comme sauteurs et comme cibles) : étendu à tout saut volontaire (GE-08) ; l'exclusion comme cible est maintenue (GE-09).
+- DS5.3 (l'attaquant prend la case de la cible repoussée) : maintenue (RP-09).
+- DS5.6 (coût proportionnel à la distance de Manhattan) : distance 3D pour les TU, et saut simple sans supplément (SA-22 à SA-24).
+- Recommandation E11 du LOT-2G (même vitesse pour toutes les masses) : écartée par SA-16.
+
+#### Encore ouvert
+
+- Géométrie : largeur de case et rapport case/étage (la hauteur d'étage est fixée à 3 m) ; dimensions des unités par type et par posture ; épaisseur des surfaces ; tolérance des contacts.
+- Sauts : masses et capacités de référence par type ; calibrage horizontal et portée en descente ; plage de gravité par type et très faible gravité ; valeur de `C_saut` ; coût en TU non entier.
+- Force et charge : capacité de portage en kg selon la Force ; cohérence avec N14 ; masses des corps et des objets.
+- Chutes : courbe de puissance au-delà de 3 m, à recalibrer lors des tests, et portée de ce recalibrage sur les plafonds de puissance et sur le plafond 2 de `F_surcharge` ; tolérance numérique de la comparaison au seuil quand la hauteur équivalente est calculée ; combinaison de la vitesse héritée, de la surcharge et de la gravité (ordre, point d'application de `g/g0`, absence de double comptage) ; hauteur comptée pour un saut volontaire de plus d'un étage et pour un saut au même niveau en surcharge ; suite d'un saut exempté qui se poursuit en chute, si le support de réception cède ou si la destination est sans support ; réception de l'attaquant après un choc contre sa cible : réception exemptée, ou chute consécutive distincte avec vitesse résiduelle.
+- Dégâts : `K_unités`, `K_obstacles` ; absorption d'énergie des planchers ; conversion de la résistance en énergie ; protections par zone et direction ; coefficients de santé et d'étourdissement ; pénalité d'étourdissement sur les Réactions.
+- Chaîne de calcul : place de `min(M/80, 3)` contre le décor ; surcharge dans les collisions ; interaction des plafonds 60, 70 et 80 avec les bonus, la gravité et la hauteur majorée par la surcharge ; nature et normalisation du tirage de 50 à 150 % ; détail des deux arrondis ; limites numériques éventuelles ; double comptage de la gravité, de la vitesse et de la masse.
+- Vitesse après un choc qui interrompt le saut, et vitesse résiduelle après la traversée d'une surface.
+- Esquive : instant où la menace est « vue » ; `n` pour un impact à hauteur intermédiaire ; probabilité non entière ; algorithme des esquives en conflit.
+- Repoussement : retombée verticale de l'attaquant au-dessus de la cible (RP-06).
+- Événements : ordre FIFO des chutes et chronologie physique ; clé d'ordre stable ; emplacement des cadavres ; collisions imbriquées et multi-cibles ; nombre maximal d'événements en chaîne.
+- Décor : propriétés destructible ou indestructible, résistances initiales, unité des dégâts du terrain.
+- Marche et TU : coûts des cases, capital et renouvellement des TU, visibilité, sous la responsabilité de `MEC-0001`.
+- Décisions du 9 novembre 2026 et correctif du propriétaire (LOT-2F) : reprises ici par leurs identifiants, sans inscription propre.
+
+Cette liste n'est pas exhaustive : tout ce que PE-01 à EN-10 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.
```

## 4. À confirmer avant une inscription

| # | Sujet | Pourquoi |
|---|---|---|
| 1 | Autorisation d'écrire le registre | CLAUDE.md §3 et §8 ; mandats LOT-2I v1.1 §2 et v1.2 §0 : interdit dans ce lot |
| 2 | Preuve et date | La décision de `MEC-0002` repose sur des preuves déclaratives (D2 ; C3, transcription de l'orchestrateur dans le mandat v1.2) et sur C2, qui ne sont pas dans `main`. Faut-il archiver C2 et les mandats v1.1 et v1.2 dans `docs/mandates/`, comme les documents précédents ? Le correctif v1.2 n'autorise aucun archivage. |
| 3 | Les huit principes marqués « à confirmer » en v1.1 | **Réglés dans leur principe** par le correctif v1.2 (A3A, A4.1D à A4.3A, exception de surcharge, A8A ; « oui » à A12, A18, A24, A25, A27). Reste à vérifier, avant inscription, que le texte proposé leur est fidèle, notamment la lecture d'A4.3A, appliquée au saut d'un étage avec ou sans surcharge (consolidation, §11.2, X16) |
| 3 bis | Copie des arbitrages | Le mandat v1.1 (§1) demande une copie approuvée des 29 propositions et des réponses 1A à 6A, si Claude Code n'y a pas accès ; elle n'a pas été fournie |
| 3 ter | Paramètres encore ouverts | Courbe au-delà de 3 m, tolérance de comparaison au seuil et portée du recalibrage sur les plafonds et sur le plafond 2 de `F_surcharge` (A29) ; combinaison de la vitesse héritée, de la surcharge et de la gravité (A5) ; surcharge dans les collisions (A6) ; sauts non couverts, suite d'un saut exempté qui se poursuit en chute et réception de l'attaquant après un choc (A30). Ils peuvent rester ouverts dans une inscription partielle |
| 4 | Identifiants PE, GE, SA, CH, CO, ES, RP, EN | Proposés par le LOT-2I ; à confirmer, car un identifiant du registre est permanent |
| 5 | Identifiant `MEC-0002` | Nommé par C2 et par le mandat v1.1 ; permanent une fois inscrit |
| 6 | Décisions du 9 novembre et correctif | Reprises par leurs identifiants dans `MEC-0002`, sans inscription propre : ce choix est à confirmer |
| 7 | Rebase du diff | Le diff vaut pour le registre au commit `74faa29` ; à régénérer si le registre change |
| 8 | Fichiers cités par la fiche | La fiche cite les documents du LOT-2I, qui ne seront sur `main` qu'après une fusion autorisée de ce lot |

## 5. Ce qui n'est pas modifié

- `docs/gameplay/GAMEPLAY-DECISIONS.md` : inchangé (SHA-256 identique à `main`).
- Aucun autre registre (`docs/decisions/`, `docs/references/`), ni `CLAUDE.md`, ni le harnais, ni `src/` ou `tests/`.
- `docs/mandates/` : ni archive des mandats v1.1 et v1.2, ni modification de l'index (non autorisées).
- Les livrables des LOT-2F, LOT-2G et LOT-2H restent tels quels.
