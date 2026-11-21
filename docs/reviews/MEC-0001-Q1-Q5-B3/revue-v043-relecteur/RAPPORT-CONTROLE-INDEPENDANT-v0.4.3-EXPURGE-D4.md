# Contrôle indépendant ciblé de la consolidation MEC-0001 v0.4.3 (Q1 à Q5 et B3)

- **Objet :** `D/revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3.md`, 1 008 lignes. SHA-256 recalculé : `cd1c808b10dbcf39f96e557f9d6ef994b232bdcacc44e696122edd4dbee76602`. Il est identique à l'empreinte annoncée.
- **Relecteur :** agent distinct de l'auteur de la v0.4.3. J'ai travaillé en lecture seule. Je ne m'accorde pas la validation finale : elle revient au propriétaire.
- **Date :** 20 novembre 2026.
- **Mandat :** message 39 du propriétaire dans le journal (2026-11-20T16:36:50.909Z), postérieur à O-7. Les vérifications 1 à 11 et le livrable qui m'ont été transmis sont identiques à ce message. Ses quatre empreintes concordent avec les fichiers.
- **Bases :**
  - `origin/main` = `818c646c7d33b819d8b69b81679749be6e77eff9` ;
  - registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, SHA-256 `9117d20c…d39e`, inchangé en fin de contrôle ;
  - clone OXCE au commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, commit figé de `docs/references/OXCE-BASELINE.md` (l.13).
- **Notations :**
  - `D` = `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad` ;
  - « v043:N » : ligne N de la v0.4.3 ; « v042:N » : ligne N de la v0.4.2 ;
  - « RV42 l.N » : ligne du rapport de revue de la v0.4.2 ; « P1 l.N » à « P7 l.N » : ligne d'une copie ;
  - `R:N` : ligne du registre sur `main` ; `D:N` : ligne de la v0.2 ;
  - `JS-N` : n-ième message du propriétaire dans l'extraction mécanique du journal (O-7, et ma réextraction, qui lui est identique sur ses 38 premiers messages) ;
  - « BU:N » : ligne de `src/Savegame/BattleUnit.cpp` au commit `441cae1b`.

## 1. Verdict : conforme sous réserves

**Ce que j'ai vérifié par mes propres contrôles (exécuté et réussi) :**
- **Les huit anomalies AN-01 à AN-08 sont effectivement corrigées** à l'endroit visé, et le texte fautif a disparu (§3).
- **OB-01 à OB-07 sont appliquées. Le rejet d'OB-08 est justifié** : l'erreur se trouvait dans la commande de revue de la v0.4.2, et non dans le document (§4).
- **Les six arbitrages sont conservés à l'identique.** Textes et statuts sont identiques à P6 l.32, 45, 59, 73, 85, 96 et l.42, 56, 70, 82, 93, 107. Chaque texte apparaît deux fois, comme dans la v0.4.2. Aucune extension n'a été trouvée (§5).
- **T47 (b)** est atteignable sous Z1 et G3, et ses débits sont exacts : 12 TU à la sélection ; 8 TU et 98 d'énergie, puis 2 TU et 95 d'énergie ; arrêt sans débit avant le troisième pas.
- **T48** : 1 205/√2 = 852,06…, d'où une enveloppe de 854 mm. Un arrondi préalable au plus proche ou inférieur donne 852 ; un arrondi supérieur donne 853, puis 854. Ces résultats sont établis en arithmétique exacte. T48 ne crée aucune convention d'arrondi.
- **Matrice et PNV.** Les 65 rattachements sont tous cités par leur scénario. Seuls T04, T15 et T26 dépendent d'une PNV, et aucune PNV ne figure dans un scénario « Sp ».
- **Points ouverts.** Aucun n'a disparu : « [OUV] » passe de 46 à 49 occurrences, « ouvert » de 52 à 59. Les neuf points de P6 §6 sont présents.
- **Copies et identifiants.** Les 13 horodatages JS sont exacts, et les correspondances JS ↔ intertitres aussi. P7 est la copie intégrale de JS-38.
- **Empreintes.** J'ai recalculé les 33 empreintes de fichiers du §15 et les 5 empreintes du dépôt : toutes sont exactes. Pour 32 fichiers, un script a vérifié que l'empreinte figure sur la ligne de son fichier. Pour la pièce 5, dont le nom est abrégé au §15 (v043:741), je l'ai vérifié par lecture. S-13 reproduit la v0.4.3 octet pour octet à partir de la v0.4.2.
- **Portée.** Mon diff est identique au patch fourni (23 blocs), et chaque bloc tombe dans une section déclarée au §21.

**Ce qui empêche le verdict « conforme » :** deux défauts mineurs du document, qui ne touchent aucune règle (§2.1) :
- **AR-01** : au §5, une affirmation générale sur OXCE est plus large que la référence de code qui l'appuie ;
- **AR-02** : au §17, tous les contrôles sont déclarés « exécutés, code de sortie 0 », alors que quatre d'entre eux sont, en tout ou en partie, des relectures.

S'y ajoutent sept observations rédactionnelles sans effet sur le fond (§2.2), et les réserves structurelles déjà connues (§2.3).

**Aucune anomalie bloquante ni importante. Aucune nouvelle règle implicite (§6). Aucune décision de gameplay modifiée.**

## 2. Anomalies restantes

### 2.1 Défauts du document

| N° | Endroit | Preuve | Gravité | Nature | Correction proposée | État |
|---|---|---|---|---|---|---|
| **AR-01** | §5, « Point d'articulation » (OB-06), v043:355 : « Or OXCE ne réduit pas la récupération d'énergie selon la charge : `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`, commit `441cae1b`) ne tient compte que des blessures mortelles au torse. » | **La référence est exacte** : BU:2733-2742 est bien `prepareEnergy`, qui ne retranche que l'effet de [code OXCE retiré — D4] (BU:2738). **Mais elle ne suffit pas à l'affirmation générale.** Le gain d'énergie que reçoit cette fonction est calculé ailleurs : [code OXCE retiré — D4] (BU:2946). Ce gain est configurable par armure, à partir de la clé `recovery` (`src/Mod/Armor.cpp:234`, avec des scripts de mod). Par défaut, il vaut `energyRegen` (`src/Mod/RuleStatBonus.cpp:537-544`), soit un tiers des TU initiales pour un soldat, ou la valeur de la règle de l'unité (`RuleStatBonus.cpp:144-155`), sans terme de poids. Dans tout `src/`, `getCarriedWeight` n'apparaît qu'à BU:2717 (TU), BU:3110, `InventoryState.cpp:656` et à sa définition. **L'affirmation est donc juste pour la configuration par défaut** (code lu, non exécuté), mais la ligne citée n'en apporte qu'une partie | mineure | défaut du document, **nouveau dans la v0.4.3**. La formulation reprend celle d'OB-06 (RV42 l.178), qui avait le même défaut. Ce n'est pas une affirmation de fidélité, et la règle n'en dépend pas | écrire « dans la configuration par défaut, OXCE ne réduit pas… », et ajouter : BU:2946 ; `RuleStatBonus.cpp:144-155` et `537-544` ; `Armor.cpp:234` (gain configurable) ; seule utilisation du poids dans la récupération : BU:2717 (TU). Ou bien restreindre la phrase à ce que montre BU:2733-2742 | exécuté et échoué (la référence ne couvre pas l'affirmation) ; le comportement par défaut a été inspecté seulement |
| **AR-02** | §17, phrase d'introduction (v043:833) : « Chaque contrôle a été exécuté avec `python3 -I` ou une commande du shell, avec le code de sortie 0. » | Les méthodes des contrôles 3 (« lecture des lignes citées », v043:841), 4 (« relecture du diff O-8 bloc par bloc », v043:842), 9 (« relecture du §3.5 et du §13 ; S-8 », v043:847) et 11 (« comparé section par section », v043:849) sont des relectures, en tout ou en partie. Un code de sortie 0 d'une commande de lecture n'établit pas la conclusion du contrôle. CLAUDE.md, §6 : « Sans sortie observable, pas de succès déclaré. » Leurs conclusions sont exactes : je les ai refaites (§7, points 3, 6, 9 et 11) | mineure | défaut du document (traçabilité), **hérité** de v042:784, et reformulé dans la v0.4.3 | séparer les contrôles exécutés par script (1, 2, 5, 7, 8, 10, 12 et 13) des relectures (3, 4, et en partie 9 et 11), par exemple : « Les contrôles 1, 2, 5, 7, 8, 10, 12 et 13 sont outillés (code 0) ; les contrôles 3, 4, 9 et 11 reposent en tout ou en partie sur une relecture. » | inspecté seulement. Les commandes réellement lancées par l'auteur : non vérifié |

### 2.2 Observations (ce ne sont pas des erreurs ; correction facultative)

| N° | Endroit | Constat | Proposition |
|---|---|---|---|
| OC-01 | §14, RD-9 (v043:699) | « Les rapports RV41 et RV42 ne sont authentifiés que par leur empreinte (RV42, §5). » RV42 §5 ne le dit que de RV41 (RV42 l.223). Le reste est un prolongement juste, mais il est attribué à RV42 | « (RV42, §5, pour RV41 ; même situation pour RV42) » |
| OC-02 | T43 (v043:639) ; §13, « Sort des cas », G1-05 (v043:658) ; §16, C-14 (v043:826) | T43 parle désormais de « géométrie et trajectoire, laissées ouvertes par G1 : R:134 ». Les deux autres lignes gardent « géométrie et praticabilité du trajet ». R:134 nomme bien la « trajectoire » ; le fond est le même. Le §16 est historique et reste inchangé, ce qui est voulu | harmoniser G1-05 du §13, ou le laisser tel quel |
| OC-03 | §10, ligne G3 (v043:491) | La cellule ne porte que « coûts de chaque connexion (Q3.10=B) », comme l'avait proposé RV42. Or la mention « Ouvert » de G3 (R:141) comprend aussi les « barèmes de terrain » et la « récupération et plafond d'énergie ». Les autres terrains restent ouverts : ligne R:152 du §10 (v043:481). Les valeurs définitives sont à calibrer : Q3.11=B, §5 (v043:333) et §12 (v043:546). **Aucun de ces points ne disparaît du document**, et P7 ne demandait que les deux points traités | ajouter, si l'on veut, « autres terrains ; valeurs définitives après calibration (Q3.11=B) » |
| OC-04 | T47 (v043:643) | Le nouveau cas (b) teste un pas renchéri mais payable (M-05=A), puis un pas suivant devenu non payable, qui garde son coût prévu. L'ancien cas (b) testait un pas renchéri qui devenait lui-même non payable, mais depuis un état inatteignable. Ce cas n'est plus exercé par un état sélectionnable. La règle est inchangée : l'arrêt sans débit reste testé par le troisième pas de T47 (b) et par T08 | facultatif : une variante (c), par exemple « 12 TU et 100 d'énergie ; le troisième pas passe à 6 TU et 3 d'énergie ; arrêt sans débit ; il reste 4 TU et 96 d'énergie » (calcul vérifié, `variante_t47.py`). La décision revient au propriétaire |
| OC-05 | §11, dernière ligne (v043:511) | « Autres décisions, dont les six arbitrages du §2 bis : non étudiées ». Or le §5 (v043:355) contient désormais un constat sur le code d'OXCE, lié à N14 et à M-04=B | ajouter un renvoi : « M-04=B et N14 : voir le point d'articulation du §5 ; aucune fidélité n'est affirmée » |
| OC-06 | §5 (v043:353) | Depuis le déplacement imposé par OB-01, la sous-liste « Application » finit par « n'est fixé ; » | remplacer le point-virgule final par un point (typographie) |
| OC-07 | §20.2, ligne I-1 (v043:929) | « le message reçu le 19 novembre » reprend les mots de RV41 (l.27 et l.280). C'est hors du §0.1, donc hors du périmètre d'AN-02, mais le 19 novembre compte plusieurs messages | ajouter « (JS-31) » |

### 2.3 Réserves structurelles déjà connues (ce ne sont pas des défauts du document)

- **Sources non authentifiées** (RD-1, RD-6, RD-9) :
  - P1 à P7 sont des copies. Leur fidélité au journal de session est vérifiée ; leur fidélité à la conversation d'origine ne peut pas l'être.
  - Le journal n'a pas d'empreinte stable.
  - RV41 et RV42 ne sont authentifiés que par leur empreinte.
- **Archivage non effectué** (RD-1). C'est un préalable à toute inscription. RD-10 subordonne un verdict « pleinement conforme » à la vérification des preuves (P2 l.114).
- **Paramètres volontairement ouverts** (§14) :
  - les modalités de M-04=B et de R-5=A ;
  - les neuf PNV ;
  - les points [OUV], dont les neuf de P6 §6.

  Je n'en exige pas la résolution.
- **Autres limites déclarées :**
  - textes des options absents pour Q5.1, Q5.2, B3 et les six arbitrages (RD-3) ;
  - formulations de Q4 résumées par l'orchestrateur (RD-2) ;
  - existence des options B et nombre d'options de Q1.1 à Q1.4 : déclarations du propriétaire (RD-5).
- **Empreinte de S-13** (`make_v043.py`) : je l'ai calculée, elle vaut `d877a7f2f1bd8ea1a692c6b9133592dcaaf71550aca56778c9a1d3d8622ad8c7`. Le §15 la dit « donnée hors du fichier », mais aucune valeur annoncée ne m'a été transmise. La comparaison n'est donc pas vérifiée. Le script lui-même est vérifié par son effet : il reproduit la v0.4.3 à l'identique.

## 3. Vérification explicite des huit anomalies AN

| AN | Constat de RV42 | Dans la v0.4.3 | Ma vérification | État |
|---|---|---|---|---|
| **AN-01** | ⟨B3-03⟩ annoncé à T04 au §20.2, mais absent | T04 porte ⟨B3-03⟩ (v043:599). La ligne M-01 du §20.2 est rectifiée et la rectification est signalée en italique ; emplacement : « §3.6, §9.1 ; §13 en v0.4.3 » ; statut : « corrigé en partie dans la v0.4.2 ; achevé dans la v0.4.3 » (v043:930) | Les cinq endroits de RV41 M-01 portent maintenant le marqueur : v043:266, 267, 269, 442 et 599. Q1.9 est bien ⟨B3-03⟩ (v043:193, 529). Le journal des corrections décrit exactement le changement : le diff ne touche que T04 et la ligne M-01. P6 l.130 a été relu | **corrigé** ; exécuté et réussi |
| **AN-02** | « message 1 / message 2 » ambigus au §0 et au §0.1 | identifiants JS-NN, avec horodatage et copie (tableau v043:53-65). Le §0.1 est réécrit (v043:69-111), ainsi que RD-6 (v043:696) et le §15 (v043:734-739). « Message 1 / 2 » est réservé aux intertitres | Les 13 horodatages sont identiques à ma réextraction. Les correspondances sont exactes : JS-24 à JS-28 = A à E ; JS-30 et JS-31 = P1 « Message 1 » et « Message 2 » ; JS-32 à JS-34 = F à H ; JS-35 = I ; JS-36 = J ; JS-38 = K. Toutes les occurrences de « message 1/2 » restantes sont rattachées à un intertitre de P1. Seuls deux endroits hors §0.1 en sont dépourvus : v043:896, dans le §19 historique (« P1, message 2 »), et v043:929 (OC-07). P6 l.115 a été relu | **corrigé** ; exécuté et réussi |
| **AN-03** | état de départ de T47 (b) incompatible avec Z1 et G3 | « 12 TU et 100 d'énergie à la sélection, de sorte que le trajet connu (12 TU et 6 d'énergie) est sélectionnable (Z1, G3) » ; Z1 ajouté aux sources (v043:643) | Sélection : 12 ≤ 12 TU et 6 ≤ 100 (R:90, R:141 : « une destination qui ne peut pas être atteinte avec les deux ressources n'est pas sélectionnable »). Premier pas : 8 TU et 98 d'énergie. Deuxième pas (6, 3) : payable, exécuté, il reste 2 TU et 95 d'énergie (M-05=A, P6 l.45 et 49). Troisième pas : 2 < 4 TU, arrêt sans débit (Q3.4, G3, P6 l.50-51) ; il reste 2 TU et 95 d'énergie. Les seules valeurs initiales qui donnent ce déroulement sont 12 et 13 TU. L'ancien cas partait de 9 TU, non sélectionnables. Le cas (a) est inchangé : 46 TU et 93 d'énergie | **corrigé** ; exécuté et réussi |
| **AN-04** | trois expressions entre guillemets absentes de la source | (a) « Unités physiques de géométrie : mm entiers » (v043:253) ; (b) « Concordance d'ordre et de troncature » (v043:944) ; (c) « le profil ne dépasse pas sa case » (v043:622) | (a) est littéralement dans D:30 ; (b) est littéralement dans v041:404 et RV41 l.186 ; (c) reprend littéralement le résultat de T26, sur la même ligne. Les trois expressions fautives ont disparu du document | **corrigé** ; exécuté et réussi |
| **AN-05** | T45 encore dans W-11 (a) | « T45 retiré en v0.4.2 (M-13) ; […] restent T04, T15 et T26 » (v043:881) | Cohérent avec le statut de T45 (v043:641, « Sp […] ; test intégré : Pa »), avec la ligne PNV du §12 (v043:582) et avec mon analyse des statuts | **corrigé** ; exécuté et réussi |
| **AN-06** | T03, T42, T43 et T46 rattachés aux PNV sans PNV justifiée | « géométrie laissée ouverte par G1 : R:134 » (v043:598, 642) ; « sous-segments, laissés ouverts par G1 : R:134 » (v043:638) ; « géométrie et trajectoire, laissées ouvertes par G1 : R:134 ; **pas** PNV-7 » (v043:639). Ligne PNV du §12 : « T04, T15, T26 » (v043:582) ; contrôle 9 (v043:847) | R:134 contient « dimensions des volumes, […] tolérance géométrique, trajectoire et sous-segments ». Les statuts restent « Pa ». Analyse mécanique du §13 : seuls T04 (PNV-5), T15 (PNV-6) et T26 (PNV-3, PNV-4) mentionnent une PNV de façon positive. Écart de vocabulaire : OC-02 | **corrigé** ; exécuté et réussi |
| **AN-07** | « — » pour R:166 et G3 au §10 | R:166 : « repli d'une diagonale sur le passage Y (§6) » (v043:487) ; G3 : « coûts de chaque connexion (Q3.10=B) » (v043:491) ; RF-01 complété (v043:716) | Les deux points sont bien ouverts : §6 (v043:406) et §14 (v043:714) pour le premier ; Q3.10=B (v043:280) pour le second. Ils relèvent de R:166 et de la mention « Ouvert » de R:141. Les cellules ne sont plus marquées comme entièrement résolues. Complétude de G3 : OC-03 | **corrigé** ; exécuté et réussi |
| **AN-08** | scripts non inventoriés ; « PARTIEL » réinterprété sans le dire ; JS-29 décrit de façon réductrice | S-1 à S-13 au §15 (v043:773-796) ; concordance fortuite expliquée (v043:845) ; JS-29 décrit et cité (v043:58, 76), et inventorié (pièce 14 bis, v043:799) | Les 12 empreintes de S-1 à S-12 sont exactes ; S-13 est vérifié par son effet (§2.3). J'ai relancé O-5 sur O-7 : JS-22 sort « PARTIEL […] 47/2592 car. ». Le titre de 47 caractères figure en P3 l.31 (« … MEC-0001 v0.3 »). JS-29 est bien un mandat en sept points ; la citation de v043:76 est littérale. Les scripts de `verif-v04/`, `verif-v042/` et `verif-v043/` sont tous inventoriés. Les fichiers de données de ces dossiers ne le sont pas, mais le document ne les cite pas | **corrigé** ; exécuté et réussi |

## 4. Observations OB-01 à OB-08

| OB | Traitement dans la v0.4.3 | Ma vérification | État |
|---|---|---|---|
| OB-01 | rappel d'ARB-D sorti de la liste « Application (P6 l.35-40) » ; source propre « [INS] (R:124) » (v043:354) | P6 l.35-40 ne contient pas la clause. R:124 contient « La surcharge ne majore pas le prix des pas ». Les six conséquences de P6 restent dans la liste (v043:349-353) | appliqué ; exécuté et réussi |
| OB-02 | « [DÉD] : c'est une conséquence de M-05=A, que P6 n'énonce pas » (v043:404) | exact : P6 l.43-56 ne mentionne pas R:166 | appliqué ; inspecté seulement |
| OB-03 | « au millimètre le plus proche, ou inférieur, donnerait 852 […] ; un arrondi supérieur donnerait 853, puis 854 » (v043:644) | calcul exact : 852 < e < 852,5 ; le plus proche donne 852, l'inférieur 852, le supérieur 853 puis 854 | appliqué ; exécuté et réussi |
| OB-04 | « R-7=A (« clarification validée ») et R-8=A (« articulation validée ») » (v043:168) | identique à P6 l.93 et l.107 | appliqué ; exécuté et réussi |
| OB-05 | phrase sur la portée de [TR] et [TR-M] (v043:49) | P1 l.67, 111, 165, 213 et 293 sont bien les cinq validations de JS-30. P2 l.12-14 donne « 14 h 26–14 h 29 », « 14 h 38 » et « 14 h 43–14 h 47 UTC ». La déclaration est qualifiée comme telle | appliqué ; exécuté et réussi |
| OB-06 | point d'articulation [OUV] au §5 (v043:355) et au §14 (v043:721) ; N14 au §9.2 (v043:472) | R:104 et R:105 sont cités littéralement. Aucune décision n'est prise : l'articulation « reste à traiter avec les modalités de M-04=B ». N14 était déjà rattaché à M-04=B au §2 (v043:138, inchangé). La référence OXCE est incomplète : AR-01 | appliqué ; réserve AR-01 |
| OB-07 | sources de T26 : « Q1.1 à Q1.3, Q1.5 à Q1.7, Q2.5, Q2.6 » (v043:622) | Q1.4 est retiré, et la matrice rattache Q1.4 à « aucun » (v043:524) : c'est cohérent | appliqué ; exécuté et réussi |
| **OB-08** | **non retenu, sans objet** : « l'erreur était dans la commande de revue, non dans la v0.4.2 ; l'empreinte complète de P2 est au §15 » (v043:993) | **Le rejet est justifié.** RV42 l.181 qualifiait déjà OB-08 d'« écart dans la commande de la présente revue, et non dans la v0.4.2 ». L'empreinte de P2 au §15 (v043:736) est exacte (`…a37b869`). La forme abrégée « …a869 » de l'ancienne commande n'est pas un suffixe de l'empreinte : « mal tronquée » est exact. La commande du présent contrôle donne l'empreinte complète et exacte. Le document n'avait rien à corriger | rejet justifié ; exécuté et réussi |

## 5. Conservation des six arbitrages

| Arbitrage | Texte validé (P6) | Statut (P6) | v0.4.3 | Modifications de la v0.4.3 qui le concernent | Verdict |
|---|---|---|---|---|---|
| M-04=B | l.32 | l.42 « principe validé ; modalités ouvertes » | v043:160, 348 | §5 : rappel d'ARB-D isolé (OB-01) et point d'articulation [OUV] (OB-06) ; §9.2 : N14 à annoter (point d'articulation) ; §14 : articulation ajoutée aux points ouverts. Aucun multiplicateur, arrondi ni pénalité | conservé |
| M-05=A | l.45 | l.56 « règle validée » | v043:161, 397 | §6 : [DÉD] (OB-02) ; §10 : point ouvert de R:166 ; T47 (b) rendu atteignable, et le comportement « renchéri mais payable, donc exécuté » est conservé | conservé |
| R-5=A | l.59 | l.70 « règle validée ; modalités techniques restantes ouvertes » | v043:162, 202 | §3.5 : seule la citation de D:30 change dans PNV-2 (AN-04 a) ; T48 : seule une phrase sur les arrondis préalables change (OB-03) | conservé |
| R-6=A | l.73 | l.82 « règle validée » | v043:163, 223 | aucune | conservé |
| R-7=A | l.85 | l.93 « clarification validée » | v043:164, 229 | §2 bis : statut cité (OB-04) | conservé |
| R-8=A | l.96 | l.107 « articulation validée » | v043:165, 197 | §2 bis : statut cité (OB-04) | conservé |

**Preuves :**
- `arbitrages.py` : texte et statut présents dans la ligne du §2 bis ; nombre d'occurrences de chaque texte identique dans la v0.4.2 et la v0.4.3 (2 et 2) ;
- liste de toutes les lignes du diff qui nomment un arbitrage, relue une à une ;
- S-7, relancé : TOUS_OK.

Les plages P6 l.30-42, 43-56, 57-70, 71-82, 83-93 et 94-107 du §2 bis sont exactes. Les sections où les conséquences de P6 sont appliquées (§3.1, §3.2, §3.4, §9.1, §11) sont inchangées.

**État :** exécuté et réussi pour les textes et les statuts ; inspecté seulement pour l'absence d'extension.

## 6. Absence de nouvelle règle implicite : confirmée

**Règles et registre :**
- Le registre sur `main` est inchangé (`9117d20c…`).
- Les sections qui portent les décisions sont inchangées : §1, §2, §3.1 à §3.4, §3.6, §4, §7, §8, §9.1 et §11 (`sections_diff.py`).
- Dans le §3.5, le §5 et le §6, seuls changent :
  - une citation (PNV-2) ;
  - un rappel [INS] (OB-01) ;
  - un point [OUV] (OB-06) ;
  - la qualification [DÉD] d'une conséquence déjà présente (OB-02).

**Scénarios.** Les modifications du §13 ne touchent que :
- des dépendances (T03, T42, T43 et T46 ; statuts « Pa » inchangés) ;
- un marqueur (T04) ;
- des sources (T26 et T47) ;
- l'état initial de T47 (b), dont le résultat découle de M-05=A, Q3.4, G3 et Z1 seuls ;
- une phrase de T48, qui décrit les effets d'un arrondi préalable sans en prescrire aucun.

**Points particuliers :**
- **T48** : 854 mm découle de Q2.6 seule (« qui la contient intégralement »), quel que soit l'arrondi préalable qui conserve le contenu. Aucune convention d'arrondi n'est créée ; R-5=A et P6 l.65 sont respectés.
- **OB-06** : aucune contradiction n'est déclarée et aucune modalité de M-04=B n'est fixée. La mention de N14 au §9.2 est une proposition d'annotation, qualifiée de « point d'articulation », dans une section qui n'autorise aucune inscription (v043:431).
- **AR-01** porte sur la précision d'une référence à OXCE, et non sur une règle de Bastion.

**État :** inspecté seulement. La relecture a été outillée par le diff, la carte des sections et la liste des lignes modifiées.

## 7. Contrôle point par point des vérifications 1 à 11

| # | Vérification | Constat | État |
|---|---|---|---|
| 1 | Correction effective d'AN-01 à AN-08 | les huit sont corrigées (§3) ; S-10 relancé (TOUS_OK), mais je ne m'y suis pas fié : chaque correction a été lue et rapprochée de sa source | exécuté et réussi |
| 2 | Traitement d'OB-01 à OB-08, rejet d'OB-08 | OB-01 à OB-07 sont appliquées ; le rejet d'OB-08 est justifié (§4) ; réserve AR-01 sur OB-06 | exécuté et réussi ; AR-01 : exécuté et échoué |
| 3 | Références et citations modifiées | `citations.py` : 0 citation introuvable. Toutes les citations des lignes ajoutées sont retrouvées dans la source qui leur est attribuée, ou renvoient au texte même du document, à la v0.4.1, à la v0.4.2 ou à RV42. Renvois relus : D:30 ; R:104, 105, 124, 134, 141 et 166 ; P1 l.3, 7, 67, 111, 165, 213, 293, 297, 308-309 ; P2 l.12-14, 114 (§E du message C) ; P3 l.31 ; P6 l.115, 123, 130 ; JS-29 ; v041:404 ; RV41 l.186 ; BU:2714-2720 et 2733-2742. Écarts : AR-01 et OC-01 | exécuté et réussi ; AR-01 : exécuté et échoué |
| 4 | Cohérence de T47 (b) : sélection, débits, arrêt | sélection admissible sous Z1 et G3 (12 ≤ 12, 6 ≤ 100) ; débits de 4 / 2, puis 6 / 3 au coût réel ; arrêt sans débit avant le troisième pas ; il reste 2 TU et 95 d'énergie (`calculs_independants.py`). Couverture : OC-04 | exécuté et réussi |
| 5 | T48 et conventions d'arrondi | e² = 1 205²/2 ; 852² < e² < 852,5² ; Q2.6 donne 854 ; 852 par arrondi au plus proche ou inférieur, qui ne contient pas le volume ; 853 puis 854 par arrondi supérieur. Aucune convention nouvelle. Non-régression : 1 400, 850 et 1 274 mm | exécuté et réussi |
| 6 | Matrice et dépendances aux PNV | `matrice.py` : 65 rattachements, tous cités (la mention de T27 dans la ligne Q1.4 est explicative). PNV : T04, T15 et T26, comme au §12 (v043:582) et au contrôle 9 ; aucune dans un « Sp ». S-8 relancé : 65 rattachements, 0 non cité | exécuté et réussi |
| 7 | Points ouverts qui ne doivent pas disparaître | `points_ouverts.py` : aucun segment ouvert retiré sans être repris (le seul segment retiré est une phrase de la lignée, sans point ouvert). « [OUV] » passe de 46 à 49 occurrences, « Ouvert » reste à 10, « [PNV] » à 11. Les neuf points de P6 l.173-181 sont présents au §14. Complétude de la ligne G3 : OC-03 | exécuté et réussi |
| 8 | Conservation des six arbitrages | §5 | exécuté et réussi (textes) ; inspecté seulement (extensions) |
| 9 | Pas de modification des autres décisions | §6 ; sections de décisions inchangées ; registre inchangé | exécuté et réussi (diff, registre) ; inspecté seulement (fond) |
| 10 | Empreintes, inventaire, fichiers de preuve | 33 empreintes de fichiers et 5 du dépôt exactes ; association empreinte–fichier contrôlée par script pour 32 fichiers, et par lecture pour la pièce 5 ; v0.4.3 (`cd1c808b…`) et O-8 (`d15f3054…`) identiques aux annonces. S-13 reproduit la v0.4.3 (`cmp` : 0). Mes 38 premiers messages sont identiques à O-7, mes 36 premiers à O-4, mes 35 premiers à O-1. P7 est la copie intégrale de JS-38 ; seule la partie « Mission » de JS-31 est omise. S-9 calcule encore l'ancien T47 (b), ce qui est sans conséquence puisque S-12 couvre le nouveau. Empreinte de S-13 non annoncée (§2.3). AR-02 | exécuté et réussi ; S-13 : comparaison non vérifiée |
| 11 | Pas de changement hors du périmètre annoncé | mon diff = le patch (`cmp` : 0) ; 23 blocs ; sections touchées : en-tête, §0, §0.1, §2 bis, §3.5, §5, §6, §9.2, §10, §12, §13, §14, §15, §17, §18, §20.2, phrase finale, §21. Chacune correspond à une entrée du §21 (AN, OB, V-22 à V-27). L'affirmation « §1, §3.3, §7, §8, §16 et §19 inchangés » du contrôle 11 est exacte | exécuté et réussi |

## 8. Aptitude de la v0.4.3 à l'archivage

- **La v0.4.3 est apte à l'archivage documentaire.**
  - Les huit anomalies indispensables ou recommandées de RV42 sont corrigées, et les six arbitrages conservés.
  - Le diff respecte strictement le périmètre annoncé.
  - AR-01 et AR-02 sont mineures. Elles ne touchent aucune règle, aucune valeur ni aucun scénario, et chacune se corrige en une phrase.
- **Il revient au propriétaire de choisir :**
  - soit de faire corriger AR-01 et AR-02 avant l'archivage, par un erratum limité à ces deux phrases, dont un contrôle par `diff` suffirait ;
  - soit d'archiver la v0.4.3 en l'état, avec le présent rapport, qui trace ces deux réserves.

  Les observations OC-01 à OC-07 sont facultatives.
- **Les réserves structurelles demeurent** (§2.3) : sources non authentifiées, options absentes, PNV et paramètres ouverts. Archiver les pièces est précisément ce que demande RD-1.
- **Archiver n'est pas inscrire.** MEC-0001 et MEC-0002 restent reportées. Toute inscription exige un mandat distinct qui couvre les deux fiches. L'archivage lui-même relève d'une autorisation distincte (P7 l.78 ; message 39).

## 9. Commandes exécutées et codes de sortie

Tous mes scripts et sorties sont dans `D/revue-v043-relecteur/`. Python a toujours été lancé avec `python3 -I`. Git n'a servi qu'à `rev-parse`, `show` et `ls-tree`.

| # | Commande | Code | Résultat |
|---|---|---|---|
| 1 | `sha256sum` sur les 15 documents du tableau de commande | 0 | 15 empreintes identiques aux annonces |
| 2 | `diff -u v0.4.2 v0.4.3 > mon-diff.patch` ; `cmp` avec le patch fourni, en-têtes exclus | 1 (attendu) ; 0 | patch identique ; 23 blocs |
| 3 | `git -C bastion rev-parse origin/main` ; `git show origin/main:<registre>` vers `registre.md` ; `git show … \| sha256sum` sur 5 documents | 0 ; 0 ; empreintes observées | `818c646c…` ; pièces 7 à 11 exactes ; OXCE-BASELINE `f1b1db1a…` |
| 4 | `sed` sur R:75 à R:167 | sortie observée | citations de R:104, 105, 124, 134, 141 et 166 exactes |
| 5 | `git -C oxce rev-parse HEAD` ; `git show HEAD:src/Savegame/BattleUnit.cpp` vers `BattleUnit.cpp.txt` ; `awk` sur les l.2705-2745 et 2880-2960 | 0 ; 0 ; sortie observée | `441cae1b…` ; BU:2714, 2717, 2720 et 2733-2742 conformes ; appel BU:2946 |
| 6 | `git show HEAD:src/Mod/Armor.cpp \| grep` ; `git show HEAD:src/Mod/RuleStatBonus.cpp` vers un fichier, puis `grep` et `awk` ; boucle `git ls-tree` + `git show \| grep getCarriedWeight` sur `src/` | sortie observée | gain d'énergie configurable (Armor.cpp:234) ; valeur par défaut sans poids ; poids utilisé seulement à BU:2717, BU:3110 et InventoryState.cpp:656 (AR-01) |
| 7 | `git show origin/main:docs/references/OXCE-BASELINE.md \| grep` | sortie observée | commit figé `441cae1b…` (l.13) |
| 8 | `awk` sur P6 (l.1-218) | sortie observée | arbitrages, consignes l.115, 123 et 130 |
| 9 | `python3 -I verif-v04/extract_user_msgs.py <journal> messages-reextraits.md` | 0 | 39 messages ; le 39e est le présent mandat |
| 10 | `compare_extractions.py` | 0 | O-7, O-4 et O-1 identiques à mes 38, 36 et 35 premiers messages |
| 11 | `sed` sur JS-22, 23, 29, 31 (« Mission ») et 37 | sortie observée | descriptions du §0 exactes ; citation de JS-29 littérale |
| 12 | `fidelite_copies.py` | 0 | JS-24 à 28, 30, 32 à 36 et 38 intégraux ; JS-31 : préfixe de 1 066 caractères sur 2 021 ; JS-22 : titre seul ; JS-23, 29 et 37 non copiés |
| 13 | `sed` sur P1, P2, P3, D:29-37, P2 l.100-116, v041:404, RV41 l.186 | sortie observée | renvois exacts |
| 14 | `git ls-tree -r --name-only origin/main docs` ; `git show` de 6 documents vers `main/` | 0 ; 0 (×6) | sources pour les citations |
| 15 | `citations.py` | 0 | 214 citations retrouvées dans les sources primaires et 51 dans les sources secondaires ; 0 introuvable ; citations nouvelles toutes rattachées |
| 16 | `grep` des désignations « message 1/2 » ; `grep` de « 19 novembre » dans RV41 | sortie observée | AN-02 ; OC-07 |
| 17 | `ls` des dossiers de vérification ; `sha256sum` et `cat` de O-5 | sortie observée | O-5 `78453dd9…` |
| 18 | `python3 -I verif-v042/omissions.py` (O-5) sur O-7 et sur les 6 copies | 0 | « PARTIEL 47/2592 » pour JS-22 ; « 1067/2023 » pour JS-31 ; JS-38 intégral |
| 19 | `cat` de S-10, S-11 et S-12 ; `grep` des ouvertures de fichier dans S-13 | sortie observée | aucune écriture, sauf dans la sortie de S-13 passée en argument |
| 20 | `sha256sum` de 33 fichiers, avec recherche de chaque empreinte dans la v0.4.3, puis contrôle de l'association empreinte–fichier | sortie observée ; bad=0 | 33 sur 33 présentes ; association contrôlée pour 32 (la pièce 5, au nom abrégé, contrôlée par lecture) |
| 21 | `python3 -I verif-v043/make_v043.py v0.4.2 → v043-reproduite.md` (S-13) ; `cmp` | 0 ; 0 | v0.4.3 reproduite à l'identique |
| 22 | S-10 ; S-11 ; S-12 ; S-7 ; S-8 ; S-9 ; S-5 (sortie vers mon dossier), puis `cmp` avec `verif-v042/calculs-v04.txt` | 0 ; 0 ; 0 ; 0 ; 0 ; 0 ; 0 ; 0 | résultats annoncés au §17 reproduits (269 / 254 / 15 / 0 ; 65 rattachements ; TOUS_OK) |
| 23 | `calculs_independants.py` | 0 | TOUS_OK = True (T47 a et b, domaine {12, 13}, T48, §3.6) |
| 24 | `matrice.py` | 0 | 65 rattachements cités ; PNV : T04, T15 et T26 |
| 25 | `points_ouverts.py` | 0 | aucun point ouvert perdu |
| 26 | `correspondance_js.py` | 0 | JS ↔ intertitres exacts |
| 27 | `arbitrages.py` | 0 | six textes et statuts conservés |
| 28 | `sections_diff.py` | 0 | carte des sections modifiées |
| 29 | `grep` de la complétude (calibration, terrains, praticabilité) et de la phrase du §17 | sortie observée | OC-02, OC-03 ; AR-02 (v043:833 et v042:784) |
| 30 | `grep` du verdict de RV41 ; `sed` sur P5 | sortie observée | « conforme sous réserves » (RV41 l.14) |
| 31 | `sed` sur le message 39 | sortie observée | mandat identique à celui qui m'a été transmis |
| 32 | `variante_t47.py` | 0 | variante d'OC-04 : il reste 4 TU et 96 d'énergie |
| 33 | `sha256sum` final des pièces ; `git show … \| sha256sum` du registre ; `git rev-parse` d'OXCE ; `find -newermt` hors de mon dossier ; `stat` | sortie observée | aucune pièce modifiée ; registre `9117d20c…` ; OXCE `441cae1b…` ; aucune écriture hors de mon dossier |

## 10. Classement des constats

**Exécuté et réussi :**
- empreintes : 15 de la commande, 33 du §15, 5 du dépôt, et celles du message 39 ;
- identité du diff avec le patch ;
- réextraction du journal, et identité avec O-7, O-4 et O-1 ;
- horodatages JS et correspondances JS ↔ intertitres ;
- fidélité des copies, P7 comprise ;
- AN-01 à AN-08 corrigées ; OB-01, OB-03 à OB-05 et OB-07 appliquées ; rejet d'OB-08 justifié ;
- calculs de T47 (a) et (b) et de T48, avec la non-régression du §3.6 ;
- 65 rattachements de la matrice ; dépendances aux PNV ;
- points ouverts conservés ;
- textes et statuts des six arbitrages ;
- carte des sections modifiées, toutes déclarées au §21 ;
- reproduction de la v0.4.3 par S-13 ;
- scripts S-5, S-7 à S-12 et O-5 relancés (code 0) ;
- registre inchangé.

**Exécuté et échoué** (le contrôle a tourné, et la condition attendue n'est pas remplie) :
- AR-01 : la référence BU:2733-2742 ne couvre pas, à elle seule, l'affirmation générale du §5.

**Inspecté seulement :**
- AR-02 ;
- OC-01 à OC-07 ;
- OB-02 et OB-06 sur le fond ;
- absence d'extension des arbitrages et de règle implicite (§6) ;
- comportement par défaut d'OXCE pour la récupération d'énergie (code lu).

**Non vérifié :**
- authenticité des messages du propriétaire et de la conversation de conception ;
- présence des options B dans cette conversation ;
- textes des options de Q5.1, de Q5.2, de B3 et des six arbitrages ;
- fidélité de P4 au rapport d'origine ;
- valeur annoncée « hors du fichier » de l'empreinte de S-13 ;
- commandes réellement lancées par l'auteur pour les contrôles 3, 4, 9 et 11 ;
- comportement d'OXCE à l'exécution, et possibilité, pour un script de mod, de faire dépendre la récupération d'énergie de la charge ;
- exécution des scénarios comme tests.

## 11. Écarts au périmètre et fichiers produits

**Écarts :** aucun.
- Je n'ai écrit que dans `D/revue-v043-relecteur/`. La date de modification du dossier parent (16:36:56Z) correspond à la création de ce dossier, avant mon premier accès. `find -newermt` ne relève aucune autre écriture, ni dans `D` ni dans le dépôt.
- Les scripts de l'auteur ont été lancés depuis mon dossier, avec leurs chemins en argument. S-13 n'a écrit que dans mon dossier (`v043-reproduite.md`). S-11 appelle `git show` en lecture.
- Git n'a servi qu'à `rev-parse`, `show` et `ls-tree`, sur le dépôt comme sur le clone OXCE. Je n'ai fait aucun accès réseau.
- Je n'ai lu dans le journal que les entrées du propriétaire, par l'extraction O-2. Je n'ai utilisé aucune réponse ni aucun raisonnement de l'auteur.

**Fichiers produits**, tous dans `D/revue-v043-relecteur/` :
- le présent rapport ;
- scripts : `compare_extractions.py`, `fidelite_copies.py`, `citations.py`, `calculs_independants.py`, `matrice.py`, `points_ouverts.py`, `correspondance_js.py`, `arbitrages.py`, `sections_diff.py`, `variante_t47.py` ;
- extraits et sorties : `messages-reextraits.md`, `registre.md`, `main/` (6 documents de `main`), `BattleUnit.cpp.txt`, `RuleStatBonus.cpp.txt`, `mon-diff.patch`, `a.tmp`, `b.tmp`, `sortie-citations.txt`, `sortie-S5.txt`, `v043-reproduite.md`.

Je ne prends aucune décision de gameplay et ne crée aucun arbitrage. Les corrections proposées sont documentaires et facultatives, sauf avis contraire du propriétaire, à qui revient la décision. MEC-0001 et MEC-0002 restent reportées.
