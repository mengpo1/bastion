# LOT-2H — Proposition d'inscription des principes DS1 à DS5 dans `MEC-0001`

> **PROPOSITION DOCUMENTAIRE — NON INSCRITE.** Rien de ce document n'est écrit dans `docs/gameplay/GAMEPLAY-DECISIONS.md`. Une inscription exigera une autorisation distincte du propriétaire et un mandat d'écriture du registre.

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2H-PREPARATION-INSCRIPTION-v1.0.md`, publié sur `orchestration/mandats` (commit `24ca7569bd3a25cc2b0f3807a0afc92b403ebcd7`). Archivé octet pour octet dans `docs/mandates/`, SHA-256 `5dff21c4e0040d81ea2bb14a7142ffcc87a077d287de967978349dc130d7f6e9`. |
| Autorisation | Propriétaire, 13 novembre 2026 : « Je t'autorise à exécuter le mandat LOT-2H de Bastion. […] Prépare la proposition documentaire d'inscription au registre, sans modifier le registre lui-même. Aucun push, aucune PR ni fusion sans autorisation distincte. Arrête-toi après les contrôles et la revue indépendante. » |
| Source des décisions | `BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`, consolidation du 13 novembre 2026, publiée sur `orchestration/mandats` (commit `197d8b953540b178143b7c365335e19ec33e9c40`, inchangée au commit `24ca7569bd3a25cc2b0f3807a0afc92b403ebcd7`). Archivée octet pour octet, SHA-256 `dee88998c561247a5941fe2d04854a95b74e863d31b837b86f3de1acad9f335f`. |
| Registre lu | `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` = `72908389ea99f7267f7f723c57b488f640bfe441`, SHA-256 `c2a3a55e7b1ed3d08089b5d814cded324b94313792982c8556d0e9d19a7e3968`. Lu, **non modifié**. Inchangé sur `main` après la fusion de la PR n° 10 (commit `b14dc49`, même SHA-256). |
| Branche | `docs/lot-2h-preparation-inscription-mec-0001`, créée depuis `origin/main` après `git fetch origin main`. Locale : ni push ni PR. |
| Compagnons | `docs/reviews/LOT-2H-TRACABILITE-ECARTS.md` (traçabilité et écarts) ; `docs/reviews/LOT-2H-EXECUTION.md` (contrôles, limites, revue). |

## 0. Lecture rapide

**Ce que vous avez validé** (consolidation, « ACCEPTÉ — principe ») : 25 principes, notés DS1.1 à DS5.7 (§2).
- DS1 : géométrie en proportions, unités en pavés, sol de départ ignoré pendant le saut ; la cible effective reste une cible de collision (l'esquive et l'exclusion des grandes unités restent possibles).
- DS2 : une unité plus lourde saute moins haut et moins loin ; portée en Manhattan ; références du 9 novembre rattachées à une masse de référence ; plage de gravité.
- DS3 : pas de dégâts pour l'unité qui tombe d'un seul étage sans surcharge ; seuil de surcharge de N14 ; aucune exemption au-delà d'un étage ; l'unité percutée peut être blessée dès un étage ; deux arrondis au plus proche.
- DS4 : dans une collision entre unités, le rapport de masse tend à protéger la plus lourde, sans décider seul ; puissance contre un obstacle proportionnelle au carré de la vitesse normale ; poids total et plafond de 70 ; type « impact » ; même tirage pour l'unité et l'obstacle.
- DS5 : monde figé ; arrêt au premier choc ; cible repoussée après une collision non esquivée ; grandes unités exclues ; coût complet à l'engagement ; esquive avec les TU restantes vers huit voisines.

**Ce qui reste à arbitrer** : 15 sujets, regroupés au §5. Aucune valeur numérique n'est fixée par ce document.

**Ce qu'une future écriture changerait au registre** (diff exact au §4) :
1. le bandeau de la fiche, qui mentionnerait DS1.1 à DS5.7, DS5.3 sous réserve ;
2. les champs « Fonctionnement de référence et preuves », « Changement demandé », « Décision du propriétaire » (le mot « reportée » reste en tête), « Éléments exclus » et « Tests de référence » ;
3. une annotation de N7 ;
4. une nouvelle sous-section listant DS1.1 à DS5.7 ;
5. la liste « Encore ouvert » : cinq lignes précisées, deux ajoutées ;
6. la phrase finale sur ce que la fiche ne couvre pas.

**Ce qui n'est pas modifié** : voir §6. En particulier, `MEC-0001` reste « reportée », de classe `MODIFICATION-PROPOSEE`, à l'état « non commencé », et aucun gameplay n'est autorisé.

**Points d'attention avant toute inscription** (détail au §5) :
- les décisions du 9 novembre (LOT-2F) et le correctif E14, E18, E23 **ne sont pas au registre**, alors que DS1 à DS5 s'y réfèrent ;
- la fiche s'intitule « Déplacement élémentaire à pied », alors que DS1 à DS5 portent sur des sauts, des chutes et des collisions ;
- DS5.3 (cible repoussée) doit être confirmée face à K07 (« cible immobile ») ;
- la consolidation est datée du 13 novembre ; la confirmation de son contenu par le propriétaire reste à consigner au moment de l'inscription.

## 1. Conventions

- **Statuts** repris de la consolidation et du mandat :
  - **accepté en conversation** (« ACCEPTÉ — principe » de la consolidation) ;
  - **à définir** ;
  - **conflit/écart** (dont les points « à vérifier »).
- **Identifiants** : DS*n*.*m* = section *n* (DS1 à DS5) et item *m* de la consolidation. Ce sont des identifiants proposés pour le registre, à confirmer lors de l'inscription.
- **Règles antérieures** : S, Z et N sont au registre. P, J, K, D, I et E viennent du LOT-2F (`docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`) et **ne sont pas au registre**.
- **LOT-2G** : ses documents ont été lus sur la branche `docs/lot-2g-mec-0001-arbitrages` (PR n° 10, tête `2a14a501376a84a1bb2f41f5d135db56e15ee10e`), fusionnée depuis dans `main` le 14 novembre 2026. Ses recommandations ne valent que si la consolidation les reprend.
- Les citations des principes suivent le texte de la consolidation, en phrases simplifiées sans changement de sens. Le texte source fait foi.

## 2. Texte proposé : nouvelle sous-section de la fiche

À insérer dans la fiche `MEC-0001`, entre la décision N14 et la rubrique « Encore ouvert ». **Non inscrit.**

#### Principes acceptés après le LOT-2G (DS1 à DS5), consolidés le 13 novembre 2026

Ils n'autorisent, seuls, aucun gameplay. Source : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`, transcription des réponses du propriétaire, consolidée le 13 novembre 2026. Les numéros DS*n*.*m* reprennent ses sections et ses items. Seuls les éléments qu'elle marque « ACCEPTÉ — principe » sont repris ici ; ses éléments « à définir » figurent sous « Encore ouvert ». Les propositions du LOT-2G qui n'y sont pas reprises restent non validées.

Entre crochets, le lien avec une décision antérieure. Les identifiants P, J, K, D, I et E renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Ces décisions du 9 novembre 2026, et le correctif du propriétaire (E14, E18, E23), ne sont pas encore inscrits dans cette fiche.

- **DS1 — Géométrie**
  - **DS1.1** — Les calculs géométriques emploient des proportions entre largeur de case, hauteur d'étage et taille des unités, sans échelle imposée en mètres.
  - **DS1.2** — Les unités sont des volumes rectangulaires (pavés). Les collisions portent sur le volume, pas seulement sur le centre de l'unité. [Reprend P07.]
  - **DS1.3** — Le sol de la case de départ est ignoré pendant le saut de l'unité qui quitte cette case. Les autres obstacles restent soumis au calcul normal des collisions. [Exception à P07 (tout sol qui coupe le volume bloque), limitée au sol de départ ; elle ne s'étend à aucun autre sol.]
  - **DS1.4** — Les unités qui constituent la cible effective d'un saut offensif restent des cibles de collision, notamment un ennemi actuellement visible. [Reprend E14.]
- **DS2 — Sauts, charge et gravité**
  - **DS2.1** — À conditions comparables, une unité plus lourde saute moins haut et moins loin. [Écarte la proposition du LOT-2G d'une vitesse de départ égale pour toutes les masses (E11). La loi n'est pas choisie.]
  - **DS2.2** — La portée horizontale se mesure selon Manhattan : une diagonale (1, 1) compte pour deux cases. [Reprend P05.]
  - **DS2.3** — Les références du 9 novembre (à 1 g, sommet à un quart d'étage ; portée de deux cases pour une descente d'un étage) valent pour une masse de référence, encore à fixer. [Précise P04 et P05.]
  - **DS2.4** — Le saut offensif n'existe que dans une plage de gravité, encore à fixer ; il est indisponible en apesanteur et hors de cette plage. [Précise P01.]
- **DS3 — Chutes et arrondis**
  - **DS3.1** — Lors d'une chute d'un seul étage, l'unité qui tombe ne subit pas de dégâts si elle n'est pas ralentie par son poids. [Précise D01 pour l'unité qui tombe : la puissance de base de 8 pour un étage (D03) reste définie, mais aucun dégât n'est appliqué à cette unité sans surcharge. Vaut aussi pour la chute au sol de l'attaquant après une esquive (E18).]
  - **DS3.2** — Le critère qui dit si l'unité est « ralentie par son poids » (DS3.1) est le seuil de surcharge qui réduit ses TU (N14) ; aucun seuil autonome n'est ajouté.
  - **DS3.3** — Lors d'une chute de plusieurs étages, l'exemption de DS3.1 ne s'applique pas ; les dégâts précis restent à calculer.
  - **DS3.4** — Une unité sur laquelle tombe une autre unité peut subir des dégâts dès une chute d'un étage, indépendamment de l'exemption de l'unité qui tombe. [Une chute sur une unité n'est pas, pour autant, assimilée à une chute au sol.]
  - **DS3.5** — Les dégâts sont arrondis à l'entier le plus proche, la moitié vers le haut : une première fois après la base, le plafond et le bonus, avant le tirage aléatoire ; une seconde fois après le facteur de poids. Les conversions suivantes gardent leurs propres règles.
- **DS4 — Collisions, masses et type « impact »**
  - **DS4.1** — Quand une unité plus lourde tombe sur une plus légère, le rapport de masse tend à protéger la plus lourde et à aggraver les blessures de la plus légère. L'armure et les tirages aléatoires interviennent toujours ; le poids ne décide pas seul de l'unité la plus blessée. [Sens de l'effet seulement, distinct de l'effet aggravant du poids lors d'une chute au sol (N9, N10) ; la formule proposée au LOT-2G (E6) n'est pas validée.]
  - **DS4.2** — Contre un mur, un plafond ou un obstacle, la puissance de base est proportionnelle au carré de la vitesse normale au contact : à masse égale, doubler cette vitesse multiplie la puissance par quatre, avant plafond. [Précise D10 et D11.]
  - **DS4.3** — Le poids total de collision (corps, armure, équipement et inventaire) intervient ; le plafond de base de 70 pour les obstacles est conservé. [Reprend E23 et D05.]
  - **DS4.4** — Un type de dégâts « impact » propre à Bastion est créé. Son traitement s'inspire de celui d'OXCE (armure, puis santé et étourdissement) ; ses paramètres sont propres à Bastion, sans copie de données ni de code. [Lien avec D07, encore ouverte ; le champ d'application du type reste à définir.]
  - **DS4.5** — Quand une collision peut endommager une unité et un obstacle destructible, le même tirage aléatoire d'intensité sert aux deux ; protections, résistances et coefficients s'appliquent ensuite séparément. [Précise D12.]
- **DS5 — Ordre d'action, déplacement des corps et esquive**
  - **DS5.1** — Pendant la résolution d'un saut, le monde est figé, sauf les esquives automatiques et les chutes provoquées.
  - **DS5.2** — Le saut s'arrête au premier choc. Collisions, dégâts, déplacements et chutes consécutives se résolvent dans l'ordre chronologique. Aucun obstacle ni aucune unité cachés ne sont révélés avant d'être rencontrés. [Reprend I01, I03 et D13 ; étend l'arrêt à tout premier choc.]
  - **DS5.3** — Après un saut offensif et une collision non esquivée, la cible est repoussée sur une case voisine libre, et l'attaquant prend la case initiale de la cible. [À vérifier avant une inscription définitive : « cible immobile » en cas d'esquive échouée (K07) est lu comme « aucun déplacement d'esquive », la poussée venant après l'impact.]
  - **DS5.4** — Si aucune case voisine ne peut accueillir la cible, elle reste en place et l'attaquant retombe à proximité, sur un emplacement valide. Deux unités n'occupent jamais durablement une même case. [Respecte S10.]
  - **DS5.5** — À titre provisoire, les unités qui occupent plusieurs cases ne font pas de saut offensif et n'en sont pas la cible. Rien n'est décidé pour leur marche ni pour leurs chutes involontaires.
  - **DS5.6** — Le coût d'un saut offensif est un coût de déplacement proportionnel à la distance de Manhattan, plus le supplément `max(1, ⌊0,20 × TU_max⌋)`. Le tout est payé à l'engagement et n'est pas remboursé, même en cas d'interruption ou d'esquive. [Précise J09 et J10.]
  - **DS5.7** — Esquive automatique : la cible doit voir l'unité qui tombe ; elle utilise les TU qui lui restent, même pendant le tour adverse ; elle peut aller sur l'une des huit cases voisines au même niveau, diagonales comprises, si cette case est accessible et payable ; seules les informations de son camp sont utilisées ; ses TU ne sont débitées qu'en cas de réussite. La règle des Réactions, avec + 5 points de probabilité par étage et bornée de 0 à 100 %, est maintenue en principe. [Précise K03 à K07.]

## 3. Autres modifications proposées de la fiche

Extraits courts ; le texte exact figure dans le diff du §4.

| # | Emplacement | Aujourd'hui | Proposition |
|---|---|---|---|
| 1 | Bandeau de la fiche | Sous-décisions S1 à S12, Z1, N1 à N14 | Ajoute « ainsi que des principes DS1.1 à DS5.7 pour les sauts offensifs, les chutes, les collisions et l'esquive (DS5.3 sous réserve) » ; garde « la mécanique n'est pas acceptée dans son ensemble » |
| 2 | Fonctionnement de référence et preuves | Rapports LOT-2A à LOT-2D | Ajoute les rapports LOT-2E, LOT-2F et LOT-2G, tous présents sur `main` depuis la fusion de la PR n° 10 |
| 3 | Changement demandé | À partir de S1 à S12, Z1 et N1 à N14 | Ajoute DS1.1 à DS5.7 |
| 4 | Décision du propriétaire | « reportée » ; preuves du 8 novembre | **« reportée » reste en tête.** Ajoute les principes DS1.1 à DS5.7 (DS5.3 sous réserve), leur date (13 novembre 2026) et leur preuve (consolidation, commits, SHA-256) |
| 5 | Éléments exclus | Ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | Ajoute DS1.1 à DS5.7 |
| 6 | Tests de référence | LOT-2B §4, à adapter | Ajoute la matrice du LOT-2F, à recalculer selon DS1 à DS5 |
| 7 | N7 | « Pas de dégâts pour les petites chutes ; seuil exact à décider » | Garde le texte et ajoute une annotation : précisée par DS3.1 à DS3.4. N7 n'est ni effacée ni réécrite |
| 8 | Encore ouvert : géométrie | Taille des unités | Ajoute l'exclusion provisoire des grandes unités pour le saut (DS5.5) |
| 9 | Encore ouvert : chutes | Hauteur de chute sans dégâts | Principe fixé pour un étage (DS3.1 à DS3.3) ; renvoi au nouveau point |
| 10 | Encore ouvert : surcharge | Transposition d'OXCE | Ajoute le seuil tiré de N14 pour DS3.2 |
| 11 | Encore ouvert : interruptions | Interruptions non encore spécifiées | Ajoute le monde figé pendant un saut offensif (DS5.1) |
| 12 | Encore ouvert : TU | Capital et renouvellement | Ajoute la contrainte de DS5.7 (TU gardées pendant le tour adverse) |
| 13 | Encore ouvert : nouveaux points | — | Ajoute « Sauts offensifs, chutes, collisions et esquive » (les « à définir » de la consolidation) et les décisions du LOT-2F non inscrites |
| 14 | Phrase finale | Ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | Ajoute DS1.1 à DS5.7 |

## 4. Diff exact proposé

Diff unifié (contexte d'une ligne) du registre de `main` vers le texte proposé. **Il n'est pas appliqué.** Les lignes de contexte vides apparaissent sans espace initial ; `git apply` et `patch` les acceptent (contrôle consigné dans `LOT-2H-EXECUTION.md`).

```diff
diff --git a/docs/gameplay/GAMEPLAY-DECISIONS.md b/docs/gameplay/GAMEPLAY-DECISIONS.md
--- a/docs/gameplay/GAMEPLAY-DECISIONS.md
+++ b/docs/gameplay/GAMEPLAY-DECISIONS.md
@@ -50,3 +50,3 @@

-**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**
+**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14), ainsi que des principes DS1.1 à DS5.7 pour les sauts offensifs, les chutes, les collisions et l'esquive (DS5.3 sous réserve), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé.**

@@ -57,8 +57,8 @@
 | Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
-| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. Actualisation : `docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`. Surcharge, même commit, lecture du code : `src/Savegame/BattleUnit.cpp:2709-2726` et `:4852-4861`, `src/Battlescape/UnitWalkBState.cpp:295-323`. |
-| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12, Z1 et N1 à N14 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
-| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception acceptées le 8 novembre 2026 : S1 à S12 (LOT-2C), puis Z1 et N1 à N14 (LOT-2D ; N12 et N13 fusionnées dans N14). Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par les mandats `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`) et `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md` (commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`), branche `orchestration/mandats`, confirmées par les autorisations d'exécution de ces lots données par le propriétaire le 8 novembre 2026. |
+| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. Actualisation : `docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`. Surcharge, même commit, lecture du code : `src/Savegame/BattleUnit.cpp:2709-2726` et `:4852-4861`, `src/Battlescape/UnitWalkBState.cpp:295-323`. Verticalité et chutes dans OXCE : `docs/reviews/LOT-2E-VERTICALITE-OXCE.md`. Spécification des sauts, chutes et collisions : `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Dossier d'arbitrage : `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`. |
+| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12, Z1, N1 à N14 et DS1.1 à DS5.7 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
+| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception acceptées le 8 novembre 2026 : S1 à S12 (LOT-2C), puis Z1 et N1 à N14 (LOT-2D ; N12 et N13 fusionnées dans N14). Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par les mandats `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`) et `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md` (commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`), branche `orchestration/mandats`, confirmées par les autorisations d'exécution de ces lots données par le propriétaire le 8 novembre 2026. Principes DS1.1 à DS5.7 acceptés dans la conversation, DS5.3 sous la réserve indiquée, consolidés le 13 novembre 2026. Preuve : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` (branche `orchestration/mandats`, commit `197d8b953540b178143b7c365335e19ec33e9c40`, inchangée au commit `24ca7569bd3a25cc2b0f3807a0afc92b403ebcd7`, SHA-256 `dee88998c561247a5941fe2d04854a95b74e863d31b837b86f3de1acad9f335f`), désignée comme transcription de référence par le mandat LOT-2H, que le propriétaire a autorisé le 13 novembre 2026. |
 | Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
-| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas. |
-| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
+| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1, N1 à N14 et DS1.1 à DS5.7 ne couvrent pas. |
+| Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter ; sauts, chutes et collisions : `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md`, à recalculer selon DS1 à DS5). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
 | Tests de modification | Critères futurs seulement, un par écart retenu. Aucun test écrit ni exécuté. |
@@ -96,3 +96,3 @@
 - **N6** — Dégâts de chute croissants avec la hauteur. [À vérifier.]
-- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.]
+- **N7** — Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] Précisée pour l'unité qui tombe par DS3.1 à DS3.3 : une chute d'un seul étage ne la blesse pas si elle n'est pas en surcharge ; une chute de plusieurs étages n'est pas exemptée. L'unité sur laquelle elle tombe peut être blessée dès un étage (DS3.4). *(Annotation ajoutée lors de l'inscription des principes DS1 à DS5.)*
 - **N8** — Les caractéristiques individuelles et les équipements peuvent modifier les conséquences d'une chute. [À vérifier.]
@@ -111,5 +111,42 @@

+#### Principes acceptés après le LOT-2G (DS1 à DS5), consolidés le 13 novembre 2026
+
+Ils n'autorisent, seuls, aucun gameplay. Source : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`, transcription des réponses du propriétaire, consolidée le 13 novembre 2026. Les numéros DS*n*.*m* reprennent ses sections et ses items. Seuls les éléments qu'elle marque « ACCEPTÉ — principe » sont repris ici ; ses éléments « à définir » figurent sous « Encore ouvert ». Les propositions du LOT-2G qui n'y sont pas reprises restent non validées.
+
+Entre crochets, le lien avec une décision antérieure. Les identifiants P, J, K, D, I et E renvoient à `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md`. Ces décisions du 9 novembre 2026, et le correctif du propriétaire (E14, E18, E23), ne sont pas encore inscrits dans cette fiche.
+
+- **DS1 — Géométrie**
+  - **DS1.1** — Les calculs géométriques emploient des proportions entre largeur de case, hauteur d'étage et taille des unités, sans échelle imposée en mètres.
+  - **DS1.2** — Les unités sont des volumes rectangulaires (pavés). Les collisions portent sur le volume, pas seulement sur le centre de l'unité. [Reprend P07.]
+  - **DS1.3** — Le sol de la case de départ est ignoré pendant le saut de l'unité qui quitte cette case. Les autres obstacles restent soumis au calcul normal des collisions. [Exception à P07 (tout sol qui coupe le volume bloque), limitée au sol de départ ; elle ne s'étend à aucun autre sol.]
+  - **DS1.4** — Les unités qui constituent la cible effective d'un saut offensif restent des cibles de collision, notamment un ennemi actuellement visible. [Reprend E14.]
+- **DS2 — Sauts, charge et gravité**
+  - **DS2.1** — À conditions comparables, une unité plus lourde saute moins haut et moins loin. [Écarte la proposition du LOT-2G d'une vitesse de départ égale pour toutes les masses (E11). La loi n'est pas choisie.]
+  - **DS2.2** — La portée horizontale se mesure selon Manhattan : une diagonale (1, 1) compte pour deux cases. [Reprend P05.]
+  - **DS2.3** — Les références du 9 novembre (à 1 g, sommet à un quart d'étage ; portée de deux cases pour une descente d'un étage) valent pour une masse de référence, encore à fixer. [Précise P04 et P05.]
+  - **DS2.4** — Le saut offensif n'existe que dans une plage de gravité, encore à fixer ; il est indisponible en apesanteur et hors de cette plage. [Précise P01.]
+- **DS3 — Chutes et arrondis**
+  - **DS3.1** — Lors d'une chute d'un seul étage, l'unité qui tombe ne subit pas de dégâts si elle n'est pas ralentie par son poids. [Précise D01 pour l'unité qui tombe : la puissance de base de 8 pour un étage (D03) reste définie, mais aucun dégât n'est appliqué à cette unité sans surcharge. Vaut aussi pour la chute au sol de l'attaquant après une esquive (E18).]
+  - **DS3.2** — Le critère qui dit si l'unité est « ralentie par son poids » (DS3.1) est le seuil de surcharge qui réduit ses TU (N14) ; aucun seuil autonome n'est ajouté.
+  - **DS3.3** — Lors d'une chute de plusieurs étages, l'exemption de DS3.1 ne s'applique pas ; les dégâts précis restent à calculer.
+  - **DS3.4** — Une unité sur laquelle tombe une autre unité peut subir des dégâts dès une chute d'un étage, indépendamment de l'exemption de l'unité qui tombe. [Une chute sur une unité n'est pas, pour autant, assimilée à une chute au sol.]
+  - **DS3.5** — Les dégâts sont arrondis à l'entier le plus proche, la moitié vers le haut : une première fois après la base, le plafond et le bonus, avant le tirage aléatoire ; une seconde fois après le facteur de poids. Les conversions suivantes gardent leurs propres règles.
+- **DS4 — Collisions, masses et type « impact »**
+  - **DS4.1** — Quand une unité plus lourde tombe sur une plus légère, le rapport de masse tend à protéger la plus lourde et à aggraver les blessures de la plus légère. L'armure et les tirages aléatoires interviennent toujours ; le poids ne décide pas seul de l'unité la plus blessée. [Sens de l'effet seulement, distinct de l'effet aggravant du poids lors d'une chute au sol (N9, N10) ; la formule proposée au LOT-2G (E6) n'est pas validée.]
+  - **DS4.2** — Contre un mur, un plafond ou un obstacle, la puissance de base est proportionnelle au carré de la vitesse normale au contact : à masse égale, doubler cette vitesse multiplie la puissance par quatre, avant plafond. [Précise D10 et D11.]
+  - **DS4.3** — Le poids total de collision (corps, armure, équipement et inventaire) intervient ; le plafond de base de 70 pour les obstacles est conservé. [Reprend E23 et D05.]
+  - **DS4.4** — Un type de dégâts « impact » propre à Bastion est créé. Son traitement s'inspire de celui d'OXCE (armure, puis santé et étourdissement) ; ses paramètres sont propres à Bastion, sans copie de données ni de code. [Lien avec D07, encore ouverte ; le champ d'application du type reste à définir.]
+  - **DS4.5** — Quand une collision peut endommager une unité et un obstacle destructible, le même tirage aléatoire d'intensité sert aux deux ; protections, résistances et coefficients s'appliquent ensuite séparément. [Précise D12.]
+- **DS5 — Ordre d'action, déplacement des corps et esquive**
+  - **DS5.1** — Pendant la résolution d'un saut, le monde est figé, sauf les esquives automatiques et les chutes provoquées.
+  - **DS5.2** — Le saut s'arrête au premier choc. Collisions, dégâts, déplacements et chutes consécutives se résolvent dans l'ordre chronologique. Aucun obstacle ni aucune unité cachés ne sont révélés avant d'être rencontrés. [Reprend I01, I03 et D13 ; étend l'arrêt à tout premier choc.]
+  - **DS5.3** — Après un saut offensif et une collision non esquivée, la cible est repoussée sur une case voisine libre, et l'attaquant prend la case initiale de la cible. [À vérifier avant une inscription définitive : « cible immobile » en cas d'esquive échouée (K07) est lu comme « aucun déplacement d'esquive », la poussée venant après l'impact.]
+  - **DS5.4** — Si aucune case voisine ne peut accueillir la cible, elle reste en place et l'attaquant retombe à proximité, sur un emplacement valide. Deux unités n'occupent jamais durablement une même case. [Respecte S10.]
+  - **DS5.5** — À titre provisoire, les unités qui occupent plusieurs cases ne font pas de saut offensif et n'en sont pas la cible. Rien n'est décidé pour leur marche ni pour leurs chutes involontaires.
+  - **DS5.6** — Le coût d'un saut offensif est un coût de déplacement proportionnel à la distance de Manhattan, plus le supplément `max(1, ⌊0,20 × TU_max⌋)`. Le tout est payé à l'engagement et n'est pas remboursé, même en cas d'interruption ou d'esquive. [Précise J09 et J10.]
+  - **DS5.7** — Esquive automatique : la cible doit voir l'unité qui tombe ; elle utilise les TU qui lui restent, même pendant le tour adverse ; elle peut aller sur l'une des huit cases voisines au même niveau, diagonales comprises, si cette case est accessible et payable ; seules les informations de son camp sont utilisées ; ses TU ne sont débitées qu'en cas de réussite. La règle des Réactions, avec + 5 points de probabilité par étage et bornée de 0 à 100 %, est maintenue en principe. [Précise K03 à K07.]
+
 #### Encore ouvert

-- Géométrie précise des murs et des angles, dont ce qu'est un passage orthogonal « bloqué » pour N2 ; portes ; taille des unités.
+- Géométrie précise des murs et des angles, dont ce qu'est un passage orthogonal « bloqué » pour N2 ; portes ; taille des unités (pour le saut offensif, les unités de plusieurs cases sont exclues à titre provisoire : DS5.5).
 - Modèle et valeurs des coûts : terrain, murs éventuels, changements de niveau. S2 suppose un coût d'entrée par case d'arrivée : le modèle B (N1) peut obliger à la revoir, notamment pour un coût éventuel des murs (dans OXCE, ce coût s'ajoute après le facteur 1,5 : LOT-2A §2 lignes 4 et 5).
@@ -119,8 +156,8 @@
   - formule et valeurs des dégâts ;
-  - hauteur de chute sans dégâts ;
+  - hauteur de chute sans dégâts : principe fixé pour une chute d'un seul étage par DS3.1 à DS3.3 ; le reste figure sous « Sauts offensifs, chutes, collisions et esquive » ;
   - effet précis des caractéristiques, équipements, armure et charge.
-- Surcharge : transposition exacte du principe d'OXCE (formule, arrondi, ordre avec les autres pénalités) ; présentation de l'indicateur « encombré ».
-- Capital initial et renouvellement des TU.
+- Surcharge : transposition exacte du principe d'OXCE (formule, arrondi, ordre avec les autres pénalités) ; présentation de l'indicateur « encombré » ; seuil tiré de N14 pour l'exemption de DS3.2.
+- Capital initial et renouvellement des TU (DS5.7 suppose qu'une unité garde des TU pendant le tour adverse).
 - Calcul de chemin garantissant le coût minimal ; départage déterministe des chemins de même coût.
-- Orientation et rotation ; énergie ; interruptions non encore spécifiées.
+- Orientation et rotation ; énergie ; interruptions non encore spécifiées (pendant un saut offensif, le monde est figé, sauf les esquives et les chutes provoquées : DS5.1).
 - Conditions détaillées de visibilité ; règles de brouillard de guerre hors du déplacement.
@@ -129,4 +166,12 @@
 - Autres propositions du LOT-2B non arbitrées, notamment : ordre impossible sans TU dépensée (P14), paiement de chaque pas avant de le faire, marche seule ; classe définitive de la fiche.
+- Sauts offensifs, chutes, collisions et esquive (DS1 à DS5) :
+  - géométrie : rapport entre largeur de case et hauteur d'étage ; dimensions des unités ; représentation et épaisseur des surfaces ; contact tangent, contacts simultanés, précision numérique ; règles de fin de chute ; algorithme géométrique (repère, point de départ de l'arc, calcul du premier contact), dont les détails proposés au LOT-2G restent des propositions ;
+  - sauts : masse ou charge de référence ; loi qui réduit la hauteur et la portée selon le poids (quantité de mouvement, énergie ou autre : non choisie) ; rôle de la masse corporelle, du poids total et de la surcharge ; bornes de la plage de gravité et valeurs extrêmes ; règles numériques de la portée ;
+  - chutes : seuil binaire tiré de N14 ; lien entre la charge portée de N14 et le poids total de collision (E23) ; dégâts de l'unité qui tombe en surcharge ou de plus d'un étage ; chute de moins d'un étage, au sol ou sur une unité ; mode de comptage des étages franchis ; paramètres des facteurs de poids ;
+  - collisions : constante de conversion entre vitesse et puissance, et ses unités ; champ d'application du type « impact » (chute au sol, collision entre unités, obstacle) ; coefficients et résistances de ce type ; côté d'armure selon le contact ; loi de l'effet relatif des deux masses ; protection et amortissement ; dégâts au sol et effet des caractéristiques ; collision avec plusieurs unités ou objets ;
+  - placement : choix de la case où la cible est repoussée, notamment entre plusieurs cases possibles ; zone et recherche du lieu où retombe l'attaquant ; absence d'emplacement valide ; cible hors de combat ; effets secondaires d'une poussée ;
+  - TU et esquive : TU par case de saut ; règle numérique finale de la probabilité d'esquive ; loi du choix de la case d'esquive ; destination inconnue ou occupée en cours d'action ; articulation de DS5.3 avec K07.
+- Décisions du 9 novembre 2026 et correctif du propriétaire (LOT-2F) : non inscrits dans cette fiche. Leur inscription demande un mandat distinct et la confirmation de leur contenu (E16 du LOT-2F).

-Cette liste n'est pas exhaustive : tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.
+Cette liste n'est pas exhaustive : tout ce que S1 à S12, Z1, N1 à N14 et DS1.1 à DS5.7 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.

```

## 5. À arbitrer avant inscription exhaustive ou implémentation

Ce document ne demande aucun choix pendant le lot : ces sujets sont regroupés pour une conversation ultérieure.

| # | Sujet | Ce qui est acquis | Ce qui reste à choisir | Avant |
|---|---|---|---|---|
| 1 | Loi masse, hauteur et portée | Plus lourd = moins haut et moins loin (DS2.1) ; références rattachées à une masse (DS2.3) | Masse ou charge de référence ; loi (quantité de mouvement, énergie ou autre) ; masse corporelle, poids total ou surcharge | Implémentation ; recalcul des tests de saut |
| 2 | Surcharge et exemption d'un étage | Seuil de N14 (DS3.2) | Traduction de N14 en seuil binaire ; lien entre charge portée (N14) et poids total (E23) ; dégâts en surcharge et au-delà d'un étage | Implémentation |
| 3 | Comptage des étages | Exemption pour un seul étage (DS3.1) ; + 5 points par étage (DS5.7) | Mode de comptage des étages franchis (non confirmé), et s'il est le même pour les dégâts et pour l'esquive ; chute de moins d'un étage, au sol ou sur une unité | Implémentation |
| 4 | Dimensions et gravités | Proportions, pavés (DS1.1, DS1.2) ; plage de gravité (DS2.4) | Rapport case/étage ; tailles d'unités ; surfaces et contacts ; bornes de gravité | Implémentation |
| 5 | Facteurs de dégâts | Deux arrondis (DS3.5) ; sens de l'effet des masses (DS4.1) ; carré de la vitesse (DS4.2) | Constante vitesse/puissance ; loi des masses ; tirages communs ou séparés entre deux unités ; base d'une collision entre unités ; amortissement | Implémentation |
| 6 | Collision sans case libre | Cible repoussée, sinon attaquant à proximité (DS5.3, DS5.4) | Choix de la case de repousse ; zone et recherche du lieu de repli ; aucun lieu valide ; cible hors de combat ; effets d'une poussée | Implémentation |
| 7 | Articulation avec K07 | Cible repoussée après l'impact (DS5.3) | Confirmer la lecture « immobile = sans déplacement d'esquive » | **Inscription définitive** |
| 8 | Tarif du saut | Proportionnel à Manhattan, payé en entier (DS5.6) | TU par case | Implémentation |
| 9 | Probabilité d'esquive | Réactions + 5 points par étage, bornée (DS5.7) | Règle numérique finale ; tirage ; loi du choix de la case ; moment où « voit » est évalué | Implémentation |
| 10 | Armure et terrain | Type « impact » (DS4.4) ; tirage commun unité/obstacle (DS4.5) | Champ d'application du type ; côté d'armure ; résistances et conversions ; facteur vers le terrain | Implémentation |
| 11 | Décisions du 9 novembre et correctif | Transcrites au LOT-2F ; DS1 à DS5 s'y réfèrent | Confirmer leur contenu (E16 du LOT-2F) et les inscrire par un mandat distinct | **Inscription** |
| 12 | Rattachement à `MEC-0001` | Le mandat LOT-2H vise `MEC-0001` | Garder sauts, chutes et collisions dans une fiche titrée « à pied », ou ouvrir une fiche distincte | **Inscription** |
| 13 | Preuve et date | Consolidation datée du 13 novembre, désignée par le mandat LOT-2H | Confirmer explicitement son contenu lors de l'autorisation d'inscription (CLAUDE.md §3 : décision explicite et datée) | **Inscription** |
| 14 | Statut de N7 et de H01 | N7 inscrite [À vérifier] ; annotation proposée, sans réécriture (§3) | Accepter l'annotation ; requalifier H01 (« N7 contredite ») et E21 du LOT-2F | **Inscription** |
| 15 | Dépendances encore ouvertes au registre | — | Renouvellement des TU (DS5.7) ; visibilité (DS5.7) ; coûts du terrain (pas d'esquive) | Implémentation |

## 6. Ce qui n'est pas modifié

- `docs/gameplay/GAMEPLAY-DECISIONS.md` : inchangé (SHA-256 identique à `main`).
- Statut de `MEC-0001` : décision « reportée », classe `MODIFICATION-PROPOSEE`, état « non commencé », périmètre « aucun changement de gameplay ».
- Sous-décisions S1 à S12, Z1, N1 à N14 : aucune réécrite. N7 recevrait seulement une annotation, si le propriétaire l'accepte.
- Livrables du LOT-2F et du LOT-2G (ce dernier fusionné dans `main` par la PR n° 10).
- Aucun code, aucun test, aucun fichier du harnais ni de `docs/decisions/` ou `docs/references/`.
