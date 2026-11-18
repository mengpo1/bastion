# BASTION — MEC-0001 — Consolidation documentaire v1.4.1

**Date :** 17 novembre 2026  
**Nature :** candidate documentaire v1.4 corrigée après sa vérification interne : deux réserves rédactionnelles mineures (G1-06 et G4-03). Aucun nouvel arbitrage ni réglage de gameplay.  
**Périmètre :** marche ordinaire, calcul des chemins, ressources associées, interruptions et interfaces avec MEC-0002.  
**Statut :** décisions **ARB-A à ARB-E et G1 à G4 validées en conversation** par le propriétaire ; **non inscrites** comme telles au registre GitHub ; **MEC-0001 non validée globalement**.  
**Autorisation :** ce document n’autorise ni écriture dans le dépôt, ni modification de gameplay, ni commit, ni push, ni fusion. Aucun test n’a été exécuté pour cette consolidation.  
**Relation aux versions antérieures :** reprend la v1.4 après correction des anomalies V-01 à V-07 de la revue v1.3, puis corrige deux réserves mineures relevées sur la v1.4. La v1.0 historique n’est pas reconstituée. La v1.4 a été contrôlée par Claude Code en lecture seule, **sans relecteur distinct** ; la présente v1.4.1 n’a pas été relue indépendamment.

## 1. Sources et hiérarchie

### 1.1 Sources officielles du dépôt Bastion

- `CLAUDE.md` : règles permanentes, simplicité avant tout, interdiction de modifier le gameplay et les registres sans mandat et autorisation appropriés.
- `docs/gameplay/GAMEPLAY-DECISIONS.md`, fiches `MEC-0001` et `MEC-0002` sur `main`, consultées le 17 novembre 2026.
- `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md` : matrice **historique**, avec résultats à requalifier.
- `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` et `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` : interfaces et remplacement d’anciennes règles relatives aux sauts, chutes et impacts.
- `docs/reviews/LOT-2J-INSCRIPTION-DOCUMENTAIRE.md` : inscription documentaire partielle, sans autorisation d’implémentation.
- `docs/references/OXCE-BASELINE.md` : OXCE 8.7.1, commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, référence **de comportement** et non source de données à copier.

Le registre officiel est consultable à : https://github.com/mengpo1/bastion/blob/main/docs/gameplay/GAMEPLAY-DECISIONS.md

### 1.2 Provenance des décisions complémentaires

**Arbitrages du 17 novembre 2026 :**

1. Après la proposition d’ARB-B et ARB-E, le propriétaire a indiqué « parfait. je valide les deux » : validation de **ARB-B et ARB-E**.
2. Après la présentation récapitulative des cinq arbitrages, il a indiqué « Je valide tout le reste » : validation de **ARB-A, ARB-C et ARB-D**, en sus de B et E.
3. Il avait expressément précisé que les UT de *kowlting* et les TU de Bastion n’étaient **pas équivalentes**, et que les tirs de réaction manqués ou blessants sans neutraliser **interrompaient** la marche.
4. Pour **G1**, à la question « solution A, trajectoire directe, ou B, trajet par un passage ouvert ? », il a répondu **« B »**.
5. Pour **G2**, à la question « réveil différé A, ou déplacement automatique sur une case voisine libre B ? », il a répondu **« B »**. Puis, si aucune case voisine n’est libre, à « réveil sur place A, ou réveil différé B ? », il a répondu **« A »**.
6. Pour **G3**, à « marche TU uniquement A, ou marche TU et énergie B ? », il a répondu **« B »**.
7. Pour **G4**, à « priorité TU A ou priorité énergie B ? », il a répondu **« A »**.
8. Après le tableau récapitulant G1 à G4, il a confirmé **« Je valide »**.

**Pièces textuelles supplémentaires issues des échanges du 17 novembre, absentes de la revue interne v1.3 :**

- Après le premier choix G2 (**« B »**), la réponse présentée indiquait explicitement : **« Il est automatiquement déplacé vers une case voisine libre et accessible. »** et **« Ce repositionnement est distinct d’un déplacement volontaire et ne constitue pas un pas de marche ordinaire. »**
- Dans la question G2 suivante, l’option **A** était rédigée : **« Réveil sur place : le personnage reprend conscience mais reste au sol, sans pouvoir se relever tant que sa case est occupée. »** Le propriétaire a répondu **« A »**.
- La récapitulation postérieure disait : **« Ce repositionnement ne constitue pas un déplacement volontaire et ne consomme pas de TU de marche. »** Puis le récapitulatif des quatre arbitrages a été approuvé par **« Je valide »**.
- Avant le choix G4 (**« A »**), le propriétaire avait reçu la règle commune aux options : **« Dans les deux cas, les égalités restantes sont départagées de manière déterministe. »** La réponse après son choix précisait le départage stable et reproductible ; le récapitulatif a été validé ensuite.

Ces extraits distinguent une **preuve de validation conversationnelle** d’une citation du registre. Ils répondent au doute V-02 du relecteur. Les règles encore ouvertes ci-dessous ne sont pas validées implicitement. Les conséquences de posture restent séparées : **« au sol »** est le comportement validé, mais sa correspondance technique précise avec les postures `GE-03` reste à formaliser.

### 1.3 Règles officielles à respecter

- `S1` : huit directions ; `S2` : coût diagonal = `⌊1,5 × coût d’arrivée⌋`, sous la réserve historique concernant d’éventuels coûts de murs ; `S3`, `S4` et `N2` : règle permissive des diagonales.
- `S6–S9` : destinations et chemins sur information visible/explorée ; mémoire de terrain ; découverte d’obstacles cachés ; `S10` : occupation bloquante telle qu’écrite historiquement ; `S11–S12` : révélation puis disparition sans marqueur permanent de position.
- `Z1` **dans le registre actuel** : « Afficher la zone atteignable selon les TU et les informations connues ; interdire la sélection d’une destination hors de cette zone. » `S5` est supplantée pour la sélection normale ; **une interruption imprévue reste possible (`S8`, `S11`)**. **G3 ajoute postérieurement l’énergie à Z1 : cette évolution doit être annotée au registre.**
- `N3–N4` : niveaux et transitions. `N11–N14` : surcharge sans surcoût de TU par pas ni état d’immobilisation supplémentaire lié **à la charge**. **N14 inscrit encore** : « l’unité est empêchée d’avancer seulement lorsque ses TU restantes ne permettent pas de payer le pas suivant ». **G3 y ajoute postérieurement un second motif de non-exécution : énergie insuffisante**, sans rétablir l’immobilisation liée à la charge. Cette modification de portée doit être indiquée au registre.
- `MEC-0002/GE-02–GE-03` : hauteur d’étage **3 m**, volumes configurables par type/posture, largeur de case encore ouverte ; `PE-01–PE-03` : marche ordinaire dans MEC-0001, sauts/chutes/impacts/esquives/repoussements dans MEC-0002.
- `MEC-0002/ES-09–ES-10` : pour l’esquive, **le registre ne prévoit que le débit de TU**, y compris pendant le tour adverse. G3 ne crée pas de coût d’énergie pour l’esquive ; une telle extension exigerait une décision distincte.
- `MEC-0002/RP-04` et `EN-08` : les corps conservent leur masse et leur volume pour les impacts et chutes.

## 2. Décisions ARB-A à ARB-E — conservées

| ID | Décision validée | Précision de traçabilité |
|---|---|---|
| **ARB-A** | Une diagonale autorisée par les passages peut néanmoins être inexécutable si le volume ne peut passer sans collision. | Restriction physique supplémentaire à `S4/N2`, à documenter explicitement, sans la présenter comme un texte déjà inscrit. Précisée par **G1**. **Écart avec OXCE** sur la possibilité qu’une unité voisine empêche physiquement la diagonale (lecture du code : LOT-2A, ligne 44). |
| **ARB-B** | Pendant la **marche ordinaire**, les corps morts ou inconscients sont traversables ; leur case est une destination possible. | Exception nouvelle à la portée historique de `S10`. Le simple chevauchement lié à la marche n’est pas un impact MEC-0002 ; masse/volume conservés pour MEC-0002. Précisée par **G2** pour le réveil. |
| **ARB-C** | Les portes demandent une ouverture explicite ; escaliers et échelles empruntent des connexions définies ; les ascenseurs ont des états/connexions définis. Pas de changement de niveau implicite par la **marche ordinaire**. | Les coûts et états particuliers restent ouverts. Cette ouverture explicite des portes est un écart au fonctionnement d’OXCE lu dans son code. |
| **ARB-D** | Les TU disponibles après récupération sont calculées à partir du solde restant + récupération, **plafonnés aux TU maximales**, puis réduits par la surcharge sur **ce total plafonné** ; récupération d’énergie distincte. | La surcharge ne majore pas directement le prix des pas. Force→kg, quantités et arrondis encore ouverts. |
| **ARB-E** | Un **tir de réaction effectivement réalisé** contre une unité qui marche interrompt son ordre, même manqué, non blessant ou non incapacitant. Le pas déjà effectué reste payé ; un pivot sans tir ne suffit pas à interrompre au titre d’ARB-E. | Les conditions du système Overwatch et les coûts des réactions restent hors de cette fiche. Ne pas convertir les UT de *kowlting* en TU de Bastion. |

## 3. Arbitrages G1 à G4 — **nouveaux, validés**

### G1 — Trajet diagonal par un passage orthogonal praticable

**Décision validée :** la géométrie du déplacement diagonal ne suit pas obligatoirement la droite entre centres de cases. Elle passe par **un des passages orthogonaux praticables** autour du coin (solution B), de manière à permettre un trajet physiquement réalisable.

1. La condition de terrain de `N2` reste le premier contrôle : au moins un des deux passages orthogonaux doit être ouvert.
2. Le volume de l’unité doit pouvoir emprunter un passage sans traverser celui d’**une autre unité consciente** ou d’un obstacle. **Exception ARB-B :** un corps mort ou inconscient est traversable pendant la marche ordinaire, même si son volume subsiste pour les impacts et chutes de `MEC-0002`.
3. Une unité voisine **n’interdit pas automatiquement** la diagonale au test `S4`, mais peut rendre **physiquement impraticable** le passage disponible. C’est la restriction physique acceptée par ARB-A puis précisée avec G1 ; ne pas prétendre que l’ancienne portée de S4/N2 reste intégralement inchangée.
4. Le chemin physique utilisé doit respecter `S7` : ne pas exploiter de terrain jamais exploré pour fabriquer un passage prétendument connu. L’application exacte aux sous-segments et aux contacts de murs reste à formaliser.
5. Le déplacement constitue **un seul pas diagonal** : une seule facturation du coût de TU de `S2`, et un coût d’énergie de pas diagonal à définir selon G3. Il ne devient pas deux actions de marche orthogonales.
6. Si aucun passage physique ne convient, la diagonale est refusée.

**À définir sans changer ces décisions :** dimensions des volumes, largeur des cases, épaisseur des murs et tolérance géométrique, courbe/sous-segments concrets de la trajectoire, prise en compte des événements détectés pendant la traversée, coût éventuel des murs. Les tests doivent couvrir un passage ouvert avec unité voisine bloquante et un passage ouvert réellement praticable.

### G2 — Réveil sur une case occupée

**Décision validée :** lorsqu’une unité inconsciente reprend conscience alors que sa case est occupée par une autre unité :

1. Si une case **voisine libre et accessible** existe, l’unité réveillée y est **automatiquement repositionnée**.
2. Ce repositionnement n’est pas un déplacement volontaire et **ne coûte pas de TU de marche**. Aucun autre coût n’est fixé ici.
3. Si **aucune** case voisine n’est disponible, l’unité **reprend conscience sur place** et reste **au sol** ; elle **ne peut pas se relever tant que sa case reste occupée**.
4. Le chevauchement temporaire de deux unités conscientes dans ce cas est une **exception transitoire** à la règle ordinaire d’occupation `S10`. La récupération de conscience n’est pas différée faute de place.
5. `ARB-B` demeure : un corps inconscient reste traversable pendant la marche ordinaire jusqu’au réveil ; le corps mort reste traversable.

**À définir :** choix entre plusieurs cases voisines libres (ordre stable ou autre règle), définition précise d’« accessible » dans cette situation (terrain, niveau, visibilité, support, volumes), **une case contenant déjà un corps compte-t-elle comme « libre » pour le repositionnement G2 ?**, collisions et interactions pendant la coexistence temporaire, éventuels événements consécutifs, coûts d’autres actions de posture ; interprétation technique de l’état « au sol » avec les postures `GE-03` sans ajouter de relèvement implicite. **Hors de cette décision :** admissibilité des cases portant un corps aux esquives (`ES-08/11/12`), repoussements (`RP-03/05`) et sauts (règles pertinentes de `MEC-0002`, **sans attribuer à SA-05 une règle d’occupation**).

### G3 — La marche consomme TU **et** énergie

**Décision validée :**

1. Chaque pas de **marche ordinaire** a un coût en **TU et en énergie**.
2. Le pas n’est réalisable que si **les deux ressources** sont suffisantes pour les coûts de ce pas.
3. La zone atteignable `Z1` doit donc être calculée avec les TU disponibles, l’énergie disponible et l’information connue. Une destination qui ne peut être atteinte avec les deux ressources n’est pas sélectionnable.
4. Les coûts sont **propres à Bastion** : ni conversion depuis les UT de *kowlting*, ni reprise automatique des chiffres d’OXCE.
5. Pour les esquives de `MEC-0002`, **le registre `ES-09/10` ne prévoit que le débit de TU**. G3 ne leur ajoute aucun coût d’énergie. `G3` **modifie la portée de Z1 et de la clause « seulement lorsque ses TU restantes… » de N14** : le caractère payable d’un pas dépend désormais des deux ressources, sans ajouter une immobilisation spécifique à la surcharge.

**À définir :** barèmes de terrain, coûts énergétiques des diagonales et des passages, éventuels arrondis, interaction avec les coûts de murs, récupération et plafond d’énergie, traitement exact d’une hausse imprévue du coût pendant un ordre.

### G4 — Chemin de coût TU minimal, puis énergie minimale

**Décision validée :** parmi les **chemins admissibles** avec les ressources disponibles et les informations accessibles au camp :

1. Choisir celui qui **dépense le moins de TU**.
2. En cas d’égalité de TU, choisir celui qui **dépense le moins d’énergie**.
3. S’il reste une égalité, appliquer un **départage déterministe**, identique pour un même état et une même destination.

La sélection de destination respecte `Z1` et la contrainte double de `G3` : **un chemin moins cher en TU mais irréalisable en énergie n’est pas admissible**. Ne pas remplacer la priorité lexicographique par un mélange pondéré des deux ressources. Le chemin est calculé à partir de l’état connu (`S6–S9`) et non à partir de la vérité cachée.

**À définir :** clé de départage exacte lorsque TU et énergie sont à égalité, et détails d’algorithme, à choisir pour leur simplicité et leur déterminisme sans modifier le résultat fonctionnel. **Écart avec OXCE** : la référence étudiée ne garantit pas la minimisation sur tous les détours (LOT-2A, ligne 55). Aucun identifiant `V41` n’est établi ; ne pas l’utiliser.

## 4. Interfaces et conflits à faire vérifier

| Interface | Attendu confirmé | Ce qui reste ouvert |
|---|---|---|
| `S4/N2` ↔ `ARB-A/G1` | Admissibilité topologique distincte de la faisabilité physique ; chemin par un passage praticable ; coût d’un seul pas diagonal. | Dimensions, sous-segments, contacts, contrôle fin des cases visibles/explorées ; préciser textuellement la portée modifiée de S4/N2. |
| `S10` ↔ `ARB-B/G2` | Corps non bloquants pour marche ; réveil avec repositionnement, ou conscience retrouvée au sol si aucune case libre. | Sélection entre cases voisines ; case portant un corps pour G2 ; état/posture pendant chevauchement transitoire ; ES/RP/sauts distincts. |
| **`Z1` et `N14` ↔ `G3/G4`** | `Z1` doit ajouter **l’énergie** aux TU et à l’information connue ; `N14` reste sans blocage supplémentaire **lié à la charge**, mais un manque d’énergie empêche maintenant aussi le pas. Critère TU puis énergie. **Évolution de portée à inscrire explicitement.** | Montée imprévue des coûts, recalcul de trajet, égalité finale de chemin. |
| `N14/GE-07` ↔ `ARB-D` | Réduction de surcharge **après** solde + récupération + plafond, sur le total. | Force→kg, arrondis et récupération effective. |
| `MEC-0002/ES-09/10` ↔ `G3` | Le registre ne prévoit **que des TU** pour l’esquive ; le double coût est réservé à la marche ordinaire. | Interaction des critères d’accessibilité liés aux corps ; aucun coût énergie à ajouter sans nouvelle décision. |
| `ARB-E` ↔ Overwatch | Un tir réellement effectué interrompt l’ordre ; pas déjà exécuté payé. | Conditions et ordonnancement complet des réactions ; simulation d’événements dans les tests documentaires. |
| `S12` ↔ *kowlting* | Pas de marqueur persistant de dernière position ennemie dans Bastion. | Aucun transfert de cette règle depuis kowlting. |

## 5. Matrice de tests candidate mise à jour

**Statuts :** `spécifiable` = oracle déterminé par décisions acceptées et paramètres de scénario ; `partiel` = sous-ensemble testable, dépendance restante ; `ouvert` = pas d’oracle définitif. Les paramètres des scènes sont **fictifs**, et les résultats ne constituent pas des valeurs d’équilibrage.

### 5.1 Données fictives P0 — non équilibrées

- Unité témoin : **20 TU** et **12 énergie** au départ, à titre d’essai.
- Terrain normal : orthogonal **4 TU, 1 énergie** ; diagonal **6 TU, 3 énergie**.
- Terrain difficile : orthogonal **6 TU, 3 énergie** ; diagonal **9 TU, 5 énergie**.
- Pour une case de coût d’arrivée fictif **5 TU**, diagonal `⌊1,5×5⌋ = 7 TU` : test explicite de l’arrondi.
- **Fixture distincte G4 :** les couples de coûts **cumulés** des chemins A et B sont des données fictives **injectées dans la sélection d’itinéraire** ; ils ne prétendent ni provenir du barème P0 ci-dessus, ni démontrer qu’une carte intégrée peut produire ces chemins. L’intégration sur une carte concrète devra être qualifiée séparément.
- Ces coûts d’énergie sont des **tables de scénario**, pas une formule déduite des TU ; ils ne valident aucune reprise d’OXCE.
- **3 m** entre étages est une décision officielle de `MEC-0002/GE-02`, distincte des autres chiffres fictifs.

### 5.2 Cas de marche et visibilité

| ID | Scène | Résultat attendu | Statut |
|---|---|---|---|
| **P0-01** | Deux pas normaux orthogonaux, trajet unique ; 20 TU/12 énergie. | **12 TU et 10 énergie** restantes (2×4 TU et 2×1 énergie). | Spécifiable avec les paramètres fictifs G3. |
| **P0-02** | Destination distante de 2 pas normaux orthogonaux, chemin unique : coût **8 TU et 2 énergie** ; budget **5 TU et 12 énergie**. | Destination **hors zone Z1 par manque de TU**, sélection impossible ; aucun pas exécuté ; solde **5 TU et 12 énergie**. Distingue Z1 de la marche partielle historique S5. | Spécifiable. |
| **P0-03** | Carte fictive **2×2**, extérieur infranchissable ; départ et arrivée en coins opposés, arrivée sur terrain normal ; les **deux cases orthogonales intermédiaires sont en terrain difficile**, sans mur, sans unité, passages physiquement praticables. Diagonale directe : **6 TU / 3 énergie** ; chaque détour orthogonal en deux pas : **6+4=10 TU / 3+1=4 énergie**. Budget initial **20 TU / 2 énergie**. | Aucun trajet admissible par l’énergie : les trois trajets de longueur un ou deux pas exigent au moins **3 énergie** ; les éventuels trajets plus longs n’améliorent pas ce minimum dans cette carte à coûts d’énergie strictement positifs. Destination **hors zone Z1** ; aucun pas. **Variante témoin**, même carte avec **20 TU / 3 énergie** : la diagonale devient admissible et la destination sélectionnable. | Spécifiable avec les paramètres et la géométrie fictifs annoncés ; un test intégré de contacts reste conditionnel au moteur physique. |
| **P0-04** | Deux pas difficiles diagonaux sur chemin unique ; 20 TU/12 énergie. | **2 TU et 2 énergie** restantes (2×9 TU, 2×5 énergie). | Spécifiable pour ce scénario. |
| **P0-05** | Solde 7 TU, récupération 15 TU, maximum 20 TU, sans surcharge. | **20 TU** après plafond. Ce test **seul** ne distingue pas tous les modèles. | Spécifiable pour le calcul. |
| **P0-06** | Total plafonné 20 TU ; rapport de surcharge fictif 0,75. | **15 TU** après réduction ; pas de TU facturée en plus pour la marche. | Spécifiable sous facteur fictif ; arrondi exact. |
| **P0-07** | Destination à **3 pas normaux sur chemin unique**, 20 TU/12 énergie ; tir de réaction simulé **après le premier pas**. | Arrêt sur la 1re case ; **16 TU et 11 énergie** restantes ; 2e pas non exécuté ; le 1er pas **payé**. | Spécifiable sous événement de réaction simulé ; Overwatch complet hors périmètre. |
| **P0-08** | Corps mort/inconscient sur destination. | Marche et arrêt possibles, sans événement d’impact du seul fait du chevauchement. | Spécifiable pour la marche ARB-B. |
| **P0-09** | Diagonale avec un seul passage ouvert. Variante a : passage physiquement libre et connu. Variante b : le volume heurte une unité/obstacle. | a : un seul pas diagonal exécuté, tarif `S2` ; b : refus physique sans traversée. | Partiel tant que dimensions et trajectoire exacte ne sont pas fixées. |
| **P0-10** | **Test isolé du choix G4** : deux itinéraires candidats de même destination, fournis par la **fixture G4 distincte** : A = **18 TU / 10 énergie**, B = **18 TU / 9 énergie** ; budget **20 TU / 12 énergie**. Les coûts totaux sont des données injectées, pas des trajets établis dans la grille P0. | Sélectionner **B**, car les TU sont égales et **9 < 10** en énergie. | Spécifiable pour la sélection parmi itinéraires fournis ; **partiel** pour l’intégration de la recherche sur grille tant qu’une carte conforme n’est pas construite. |
| **G4-01** | **Fixture distincte G4 (sélection isolée)** : chemins candidats A = **17 TU / 11 énergie**, B = **18 TU / 2 énergie** ; budget **20 TU / 12 énergie**. Ces coûts cumulés ne sont **pas** produits par la table P0 §5.1. | Choisir **A** (priorité TU), malgré sa plus forte dépense d’énergie. | Spécifiable pour l’arbitrage entre candidats fournis ; intégration grille à qualifier. |
| **G4-02** | Même **fixture G4 distincte** que G4-01 : A = **17 TU / 11 énergie**, B = **18 TU / 2 énergie** ; budget **20 TU / 10 énergie**. | A est **inadmissible par énergie** ; choisir **B**. | Spécifiable pour l’arbitrage entre candidats fournis ; intégration grille à qualifier. |
| **G4-03** | **Fixture distincte G4 — sélection abstraite** : deux candidats différents, de mêmes coûts cumulés en TU et en énergie, injectés avec les mêmes données et dans le même ordre à chaque essai. Aucun calcul de chemin sur grille n’est effectué. | **Même candidat sélectionné à chaque essai** ; son identité exacte reste indéterminée tant que la clé finale de départage n’est pas définie. Le test d’intégration sur une vraie carte reste à construire. | Spécifiable pour la propriété de déterminisme ; partiel pour la clé exacte et l’intégration sur grille. |
| **G3-Z1** | Destination affichée dans la zone, aucun événement imprévu, coût connu, chemin admissible. | Destination atteinte ; **TU et énergie dépensées ≤ budgets** initiaux. | Spécifiable sous les règles et paramètres complets du scénario. |
| **S2-01** | Coût d’arrivée fictif 5 TU, pas diagonal. | **7 TU**, non 7,5 ni 8. | Spécifiable. |
| **S12-01** | Ennemi repéré, puis perdu de vue. | **Aucun marqueur persistant** de dernière position. | Spécifiable avec visibilité simulée. |
| **C-01** | Porte fermée pendant une marche ordinaire. | Pas d’ouverture automatique. | Spécifiable en principe ; coût de l’ouverture ouvert. |
| **C-02** | Pas de connexion valide vers l’étage supérieur. | Pas de marche implicite permettant d’atteindre l’étage. | Spécifiable en principe ; détails de connexion ouverts. |

### 5.3 Scénarios de géométrie et d’occupation

| ID | Scène | Résultat attendu | Statut |
|---|---|---|---|
| **G1-01** | Deux passages orthogonaux fermés par terrain/murs. | Diagonale refusée. | Spécifiable en principe N2. |
| **G1-02** | Un passage orthogonal ouvert, réellement praticable par le volume ; terrain connu. | Un pas diagonal, **pas deux pas orthogonaux** ; débit une seule fois. | Partiel : géométrie et coût énergétique précis à paramétrer. |
| **G1-03** | Un seul passage orthogonal ouvert, contenant **une unité consciente** dont le volume bloque réellement la trajectoire ; autre passage fermé. | Diagonale refusée **par collision physique**, et non parce que S4 classerait automatiquement l’unité comme un mur. | Partiel : géométrie à définir pour construire le cas. |
| **G1-05 — contre-exemple S4** | **Même topologie que G1-03** : un passage fermé, l’autre ouvert, avec **une unité consciente dans le passage ouvert**, mais des volumes fictifs suffisamment étroits et une trajectoire effectivement **sans contact**. | **Diagonale permise, exécutée au tarif S2** et au coût énergétique fictif du pas : l’unité voisine n’est **pas** considérée comme un mur. Rejette une implémentation qui bloque toute diagonale en présence d’une unité voisine. | Partiel : fixture géométrique et coût d’énergie à fixer pour le test intégré. |
| **G1-06 — corps** | Même topologie de passage ouvert que G1-02 : le passage est **physiquement praticable pour l’unité qui marche en l’absence du corps** ; on place ensuite un **corps mort ou inconscient** sur le passage, sans autre obstruction. | **Le corps ne rend pas ce passage impraticable pour la marche ordinaire** ; une diagonale réalisable sans ce corps reste réalisable avec lui, au tarif d’un seul pas, sans choc MEC-0002 dû au seul chevauchement. Son volume demeure pertinent pour MEC-0002. | **Spécifiable pour la règle** (corps non bloquant) ; **partiel pour le test intégré** tant que géométrie et trajectoire exactes ne sont pas fixées. |
| **G1-04** | Passage physiquement libre au prix d’un détour par une case jamais explorée. | Pas d’exploitation de terrain jamais exploré par calcul de trajet (S7). | Partiel : sous-segments à préciser. |
| **G2-01** | Inconscient se réveille alors que sa case est occupée par **une unité consciente** ; **une seule case voisine** libre et accessible, **sans corps**. | Réveil + repositionnement sur cette case ; **aucune TU de marche** dépensée pour le repositionnement (validation conversationnelle reproduite au §1.2). | Spécifiable dans ce scénario. |
| **G2-02** | Inconscient se réveille sur une case occupée par une unité consciente ; **aucune case voisine disponible** ; cases portant un corps exclues de la fixture pour ne pas préjuger leur statut. | Il devient **conscient**, reste **au sol sur place**, ne se relève pas tant que la case est occupée (validation conversationnelle reproduite au §1.2). **Correspondance technique au sol/GE-03 encore ouverte.** | Spécifiable pour le comportement approuvé ; partiel pour la posture et les contacts techniques. |
| **G2-03** | Plusieurs cases voisines **sans unité consciente ni corps** et accessibles. | Repositionnement sur **une** de ces cases ; choix précis non fixé. Le statut d’une case portant un corps est un **autre cas encore ouvert**. | Partiel. |
| **G2-04** | Corps mort ou inconscient au sol et unité marchant sur sa case. | Passage et arrêt possibles ; ne pas créer automatiquement un choc MEC-0002 par le seul chevauchement de marche. | Spécifiable pour la marche. |

### 5.4 Réactions et ressources

| ID | Scène | Résultat attendu | Statut |
|---|---|---|---|
| **E-01** | Tir de réaction réellement effectué après un pas ; tir manqué. | Marche interrompue ; **pas déjà effectué débité, sans remboursement**. | Spécifiable avec tir simulé. |
| **E-02** | Tir effectué, touche sans blessures ou blesse sans incapacité. | Marche interrompue ; **pas déjà effectué débité, sans remboursement**. | Spécifiable avec tir simulé. |
| **E-03** | Tir effectué, incapacité ou mort. | Marche interrompue ; effets de santé/inconscience traités par système concerné. | Partiel. |
| **E-04** | **Surveillant déjà visible** du camp qui marche ; il pivote **sans tirer** ; aucune révélation ni autre événement pendant le pas. | L’ordre de marche **n’est pas interrompu** du seul fait du pivot ; pas de tir déclenché. | Spécifiable avec pivot simulé ; règles d’orientation encore ouvertes. |
| **E-05** | Plusieurs réactions contre la même unité pendant un pas. | Une seule dépense du pas exécuté, aucune répétition artificielle du débit. | Spécifiable pour la comptabilité ; ordre des réactions ouvert. |
| **D-01** | `s=7, r=15, max=20, k=0,75` (facteur fictif). | `min(7+15,20)×0,75 =` **15 TU**. | Spécifiable. |
| **D-02** | `s=2, r=15, max=20`, sans surcharge. | **17 TU**, pas 20. | Spécifiable. |
| **D-03** | `s=4, r=12, max=20, k=0,75`. | `min(4+12,20)×0,75 =` **12 TU** ; distingue la réduction du seul incrément. | Spécifiable. |
| **D-04** | Total plafonné 20 TU, facteur de charge fictif `30/45`. | **13,333… avant arrondi** ; valeur entière non décidée. | Partiel (arrondi ouvert). |

**Débit dans les scènes E-01 et E-02 :** **« pas exécuté = débité, sans remboursement ; pas suivant non exécuté = non débité au seul titre de ce pas »**. Aucune autre règle de paiement d’action non commencée n’est décidée ici.

### 5.5 Mise à jour des anciens tests LOT-2F

- **T-M01 à T-M04** : principes conservés, réserves géométriques et coûts à actualiser ; **T-M02** (arrondis `S2`) reste un oracle valide.
- **T-M05** : **ne plus** affirmer « toujours permis » au niveau physique ; séparer condition `S4/N2` de la praticabilité `ARB-A/G1`. Les cas **G1-03 (collision réelle)** et **G1-05 (unité voisine, pas de collision)** sont nécessaires ensemble pour distinguer les deux contrôles.
- **T-M06 à T-M08** : principes conservés ; **Z1** inclut désormais l’énergie en plus des TU (`G3`).
- **T-M09** : distinguer unité occupant la case (**bloquante**) et corps mort/inconscient (**non bloquant pour la marche**) ; `ARB-B/G2`.
- **T-M10** : révélation d’une unité cachée conservée ; suite de déplacement après découverte sans tir encore ouverte.
- **T-M11** : historique/incomplet ; le remplacer comme vérification d’ARB-D par **D-01 à D-04**.
- **T-J, T-K, T-D** : tests historiquement mêlés à MEC-0001 ; pour sauts, chutes, esquives et impacts, se référer à MEC-0002 et à `LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` (§4). Ne pas réutiliser les attendus historiques devenus faux.

## 6. Points **encore ouverts** après les neuf arbitrages

**Ces points ne sont pas des décisions implicites, même si les principes G1 à G4 sont validés.**

### 6.1 Dimensions et contacts

- Dimensions physiques des cases et des volumes selon les unités et postures ; murs et épaisseurs ; définition d’un « passage ouvert » pour les volumes ; contacts/tolérance ; trajectoire géométrique concrète correspondant à G1 ; sous-segments et perception pendant ce pas.
- Choix de la case de repositionnement G2 lorsque plusieurs cases sont disponibles ; contraintes précises de support, perception, occupation et géométrie ; gestion des contacts transitoires au sol.

### 6.2 Coûts et ressources

- Barèmes TU/énergie des terrains et diagonales ; coût de rotation et d’interaction ; éventuels coûts de murs et de transitions verticales.
- TU maximales, énergie maximale et récupérations ; Force→capacité en kg ; facteurs, arrondis et pénalités supplémentaires de surcharge.
- Départage final exact entre chemins ex aequo (G4 impose seulement **déterminisme**) ; algorithme concret sous contraintes duales.

### 6.3 Interactions avec les autres mécaniques

- Application des règles de corps aux esquives, repoussements et sauts de MEC-0002 (`ES-08/11/12`, `RP-03/05` et autres règles pertinentes de saut) ; **SA-05 concerne la visibilité, pas l’occupation**. Aucun transfert automatique de `ARB-B`. Pour G2, préciser si une case portant un corps est « libre » pour le repositionnement.
- Définition et coûts complets de l’Overwatch ; interruption éventuelle lors d’une **simple découverte sans tir** ; réaction à un obstacle/cout imprévu pendant une marche ; choix entre arrêt et recalcul de trajet.
- Séquence détaillée des portes, ascenseurs, échelles et escaliers ; états des ascenseurs ; cas d’une cage sans support ; interactions avec MEC-0002.

### 6.4 Gouvernance

- Préparer ultérieurement un **mandat distinct** pour inscrire les décisions dans `docs/gameplay/GAMEPLAY-DECISIONS.md` avec textes, sources, dates et preuve ; expliciter les **quatre interfaces historiques** : **S4/N2** (contrôle physique G1), **S10** (exception corps ARB-B/G2), **Z1** (zone à double ressource G3) et **N14** (le manque d’énergie devient une cause d’arrêt du pas, sans immobilisation de surcharge). Mettre à jour « Encore ouvert » en conséquence.
- Dans ce **mandat distinct seulement**, apposer le bandeau historique à `LOT-2F-MATRICE-TESTS-MEC-0001.md` et actualiser `docs/references/OXCE-BASELINE.md` qui décrit encore MEC-0001 comme seule fiche. Ni ces fichiers ni les registres ne sont modifiés par la présente consolidation.
- Ne pas transformer une revue documentaire conforme en validation globale de MEC-0001 ni en autorisation de code.

## 7. Bilan de vérification interne de la v1.4 et suites

Le relecteur doit, **en lecture seule**, vérifier en priorité :

1. **Exactitude des neuf décisions** et de la chaîne de validation du propriétaire (ARB-A à ARB-E ; G1 à G4).
2. **Topologie/physique :** G1 protège-t-il la distinction `S4/N2` vs collision réelle, sans refuser toute diagonale avec un seul mur ? Contrôler G1-03 **ET** le contre-exemple G1-05, ainsi que G1-06 (corps), sans prétendre que la géométrie physique est déjà fixée.
3. **Corps/réveil :** G2-01 à G2-04 respectent-ils les **citations explicites du §1.2**, `ARB-B`, `S10`, `GE-03` et la frontière MEC-0002 ? L’état « au sol » est acquis ; la correspondance technique exacte à GE-03 et la case portant un corps restent ouvertes.
4. **Double ressource :** la **modification de portée de Z1 et N14** par G3 est-elle mentionnée partout ; les chemins respectent-ils TU et énergie simultanément ; `ES-09/10` ne reçoivent-ils pas de coût d’énergie nouveau ?
5. **Minimisation :** `G4` priorise-t-il TU puis énergie **parmi les chemins admissibles**, et une égalité finale reste-t-elle reproductible sans présumer sa clé ? Séparer la **sélection abstraite** de candidats fournis et la **qualification d’un vrai calcul sur grille**, encore à construire.
6. **Débit et réactions :** pas déjà réalisé facturé une fois même en cas de tir manqué ; simulations séparées de l’implémentation Overwatch.
7. **Surcharge :** réduction après plafond sur total, et contre-exemples D-02/D-03 suffisants pour déceler les modèles concurrents.
8. **Historique/présent :** l’ancien LOT-2F n’est pas présenté comme oracle actuel ; valeurs fictives P0 ne deviennent pas des réglages validés.
9. **Périmètre :** aucun emprunt automatique des UT de *kowlting* aux TU de Bastion ; aucune extension de MEC-0001 aux sauts, chutes, impacts et esquives.
10. **Statut :** pas de modification des registres, du code ou de l’équilibrage sans autorisation expresse.

**Livrable attendu d’une éventuelle revue :** examiner **uniquement V-01 à V-07**, et relever une contradiction supplémentaire seulement si elle est vérifiable et importante ; preuves exactes, correctif minimal, points nécessitant réellement une nouvelle décision. Ne pas recommencer une revue générale de tous les arbitrages sans nouveau motif. Une revue ne valide pas le gameplay à la place du propriétaire.

---

## 8. Tableau de traitement des constats de la revue v1.3

| ID | Traitement dans v1.4 | Limite assumée |
|---|---|---|
| **V-01** | G1-05 ajouté : unité voisine **sans contact**, diagonale permise ; G1-03 devient explicitement l’opposé **avec contact**. G1-06 traite le corps. | Volumes et géométrie réels encore ouverts. |
| **V-02** | §1.2 : extraits des options et réponses du 17 novembre, y compris coût nul en TU de marche, réveil au sol et déterminisme G4. | Mise en correspondance technique avec les postures `GE-03` ouverte. |
| **V-03** | `Z1` et `N14` déclarés explicitement comme règles historiques dont la portée évolue avec `G3`. | Inscription dans le registre réservée à un autre mandat. |
| **V-04** | P0-02 : énergie renseignée ; P0-03 : fixture 2×2 et témoin ; G4-01/02 et P0-10 : fixture isolée, sans fausse revendication de réalisabilité sous la table P0. | Des cartes de tests intégrés du chemin restent à construire ; ce n’est pas un test d’intégration déjà qualifié. |
| **V-05** | E-04 : surveillant visible, aucune révélation, aucun événement parasite. | Pivot/orientation à définir globalement. |
| **V-06** | G1 : exception des corps ; G1-06 ; G2 : case portant un corps déclarée ouverte pour le repositionnement. | Les interactions de MEC-0002 ne sont pas modifiées. |
| **V-07** | SA-05 corrigée ; ES-09/10 sans suraffirmation ; rappel complet de Z1 ; écarts à OXCE pour G1 et G4. | Lecture du code de référence sans exécution ni preuve de fidélité. |

**Clôture documentaire de cette version :** la vérification interne de la v1.4 a jugé **V-01 à V-07 corrigées** et identifié deux réserves mineures, corrigées ici dans **G1-06** et **G4-03** ; la phrase P0-03 précise le domaine des trois itinéraires les plus courts sans changer ses résultats. ARB-A à ARB-E et G1 à G4 restent **validées en conversation**, sans inscription au registre. **Les paramètres physiques et d’équilibrage restent ouverts.** Le présent document n’est pas une fiche approuvée de MEC-0001 et n’autorise aucune implémentation.


## 9. Errata de la vérification de la v1.4 (aucun nouveau choix du propriétaire)

- **Réserve 1 — G1-06 :** statut désormais scindé entre règle ARB-B spécifiable et test géométrique intégré partiel ; la scène pose explicitement que le passage serait physiquement praticable en l’absence du corps.
- **Réserve 2 — G4-03 :** test décrit comme une **sélection abstraite de deux candidats injectés**, avec sortie reproductible ; aucune recherche réelle sur grille n’est prétendue testée.
- **Clarification de comptage — P0-03 :** « trois trajets » désigne seulement les itinéraires de un ou deux pas, non une énumération exhaustive des marches plus longues. Les calculs et résultats de sélection restent identiques.

**Statut de la v1.4.1 :** correction éditoriale non relue indépendamment, sans nouvelle décision. La prochaine étape envisagée est un **mandat distinct et explicitement autorisé d’inscription documentaire** au registre Bastion, sans implémentation.
