# Revue indépendante de la consolidation MEC-0001 v0.4.2 (Q1 à Q5 et B3)

- **Objet :** `D/revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2.md`, 911 lignes. SHA-256 recalculé : `a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808`. Il est identique à l'empreinte annoncée par le propriétaire (message 37 du journal, 2026-11-20T15:41:03.718Z).
- **Relecteur :** agent distinct de l'auteur de la v0.4.2. J'ai travaillé en lecture seule. Je ne m'accorde pas la validation finale : elle revient au propriétaire.
- **Date :** 20 novembre 2026.
- **Bases :**
  - `origin/main` = `818c646c7d33b819d8b69b81679749be6e77eff9` ;
  - registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, SHA-256 `9117d20c…d39e` ;
  - clone OXCE au commit `441cae1b071d249d40a223858cb6bd07fd5d791b`.
- **Mandat :** message 37 du propriétaire dans le journal. Les vérifications 1 à 11 et le livrable qui m'ont été transmis sont identiques à ce message.
- **Notations :**
  - `D` = `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad` ;
  - « v042:N » : ligne N de la v0.4.2 ; « v041:N » : ligne N de la v0.4.1 ;
  - « RV41 l.N » : ligne du rapport de revue de la v0.4.1 ;
  - « P1 l.N » à « P6 l.N » : ligne d'une copie ; `R:N` : ligne du registre sur `main` ; `D:N` : ligne de la v0.2 ;
  - « message n » : n-ième message du propriétaire dans l'extraction mécanique du journal (O-1, O-4, et ma propre réextraction, qui leur est identique).

## 1. Verdict : conforme sous réserves

**Ce qui est vérifié (exécuté et réussi) :**
- **Intégrité.** J'ai recalculé 22 empreintes de fichiers et 7 empreintes du dépôt. Toutes sont identiques à celles du §15 de la v0.4.2. En fin de revue, aucune pièce n'a changé.
- **Six arbitrages.** Les textes validés et les statuts sont identiques à P6. Les renvois de lignes sont exacts. Le texte n'ajoute aucune pénalité, aucun multiplicateur et aucun arrondi d'énergie.
- **I-1.** J'ai vérifié la chronologie dans le journal : messages 31, 34 et 35, et remise de la v0.4 à 13:05:12.403Z. Les libellés des options B n'apparaissent dans aucun message antérieur au message 35. Les huit libellés et la validation sont exacts. La compilation est signalée comme telle, et l'omission de la partie « Mission » est identifiée.
- **Copies.** P1 (message 1), P2, P3, P5 et P6 sont identiques aux messages 30, 24 à 28, 32 à 34, 35 et 36. P1, message 2, reproduit exactement le début du message 31.
- **Calculs.** Je retrouve tous les résultats chiffrés en arithmétique exacte, y compris T47 et T48.
- **Portée.** Mon `diff` est identique au patch fourni. Ses 28 blocs tombent tous dans des sections déclarées au §20.
- **Matrice.** Les 73 rattachements de la matrice sont tous cités par leur scénario. Les dix rattachements visés par M-03 sont traités.
- **Citations.** Sur 226 citations, 198 sont retrouvées dans les sources primaires et 23 dans la v0.4.1 ou dans RV41. Les 5 autres renvoient au texte même de la v0.4.2. Les 66 renvois qui associent une citation à une ligne précise sont exacts.

**Ce qui empêche le verdict « conforme » :** huit anomalies mineures, AN-01 à AN-08 (§2.3). Trois méritent d'être signalées en tête :
- une correction est déclarée faite alors qu'elle ne l'est pas : AN-01 (M-01, T04) ;
- le §0.1 désigne les messages de façon ambiguë, alors que c'est précisément l'objet d'I-1 : AN-02 ;
- l'état de départ du scénario T47 (b) est incompatible avec Z1 et G3 : AN-03.

S'y ajoutent les réserves structurelles. Les pièces sont des copies, non authentifiées et non archivées. Les formulations de Q4 sont des résumés. Les textes des options de Q5.1, de Q5.2, de B3 et des six arbitrages manquent.

**Aucune anomalie bloquante ni importante. Je n'ai trouvé aucune règle de gameplay nouvelle sans source, et aucune contradiction de gameplay n'est établie (§3).**

## 2. Anomalies

Pour chaque anomalie, j'indique sa nature, en distinguant l'**erreur réelle**, la **préférence de rédaction** et la **décision volontairement reportée**, ainsi que l'état du constat (§10).

### 2.1 Bloquantes

Aucune.

### 2.2 Importantes

Aucune.

### 2.3 Mineures

**AN-01 — M-01 : le marqueur ⟨B3-03⟩ manque toujours dans T04, alors que le §20.2 le déclare ajouté.**
- **Endroit :**
  - §13, T04 (v042:577) ;
  - §20.2, ligne M-01 (v042:876) : « marqueur ajouté : 1 274 mm, 1 341,6 mm, profil dans la case (§3.6) ; rapport 0,5 (§9.1) ; T04 », statut « corrigé » ;
  - §17, contrôle 6 (v042:793).
- **Preuve :**
  - la ligne T04 de la v0.4.2 est identique, caractère pour caractère, à v041:485, celle que RV41 avait relevée (RV41 l.67, « T04, l.485 ») ;
  - un `grep` du marqueur sur cette ligne renvoie 0 ;
  - les quatre autres endroits sont corrigés (v042:245, 246, 248 et 420) ;
  - le contrôle 6 du §17 vérifie seulement que chaque anomalie a une ligne au §20. Il ne vérifie pas que la correction est appliquée.
- **Gravité :** mineure sur le fond, puisque le marqueur figure aux lignes Q1.9 du §3.1 (v042:172) et du §12 (v042:507). Elle est aggravée par une déclaration inexacte dans le journal des corrections.
- **Nature :** erreur réelle.
- **Correction proposée :** ajouter ⟨B3-03⟩ à T04, comme le demandait P6 l.130 (« Compléter les cinq marqueurs manquants »). À défaut, corriger la ligne M-01 du §20.2 et son statut.
- **État :** exécuté et échoué.

**AN-02 — §0.1 : les mots « message 1 » et « message 2 » désignent des messages différents d'une phrase à l'autre.**
- **Endroit :** §0 (v042:34) et §0.1 (v042:54, 64, 71 et 90).
- **Preuve :**
  - au §0 (v042:34), « copie P1, message 1 » désigne le message du 19 novembre à 20:36:22Z (message 30). C'est la numérotation de P1 (P1 l.7 et l.297) ;
  - au §0.1, la ligne « Ordre 1 » (v042:54) est le message de 20:54:21Z, c'est-à-dire « copie P1, message 2 » ;
  - l'en-tête du tableau (v042:64) appelle pourtant ce même message « message 1 », et le message I « message 2 » ;
  - v042:71 écrit « Validation, dans le message 1 (P1 l.308-309) » : il s'agit du message de 20:54, alors que P1 le nomme « Message 2 » ;
  - v042:90, en une seule phrase, emploie « P1 (message 1) » pour le message de 20:36, puis « la partie « Mission » du message 1 ci-dessus » pour celui de 20:54.
- **Gravité :** mineure. Les horodatages permettent de lever l'ambiguïté. Mais elle touche le premier point demandé pour I-1 : « Identifier séparément les deux messages » (P6 l.115).
- **Nature :** erreur réelle (ambiguïté).
- **Correction proposée :** désigner les messages par leur numéro dans le journal et leur horodatage, par exemple « message 31, 19 novembre, 20:54:21Z » et « message 35 (message I), 20 novembre, 13:41:45Z ». Réserver « P1, message 1 / 2 » aux intertitres de la copie.
- **État :** inspecté seulement.

**AN-03 — T47 (b) : l'état de départ est incompatible avec Z1 et G3.**
- **Endroit :** §13, T47 (v042:621) : « trois pas orthogonaux prévus en terrain normal […] (b) valeurs fictives : 5 TU et 98 d'énergie avant ce pas ».
- **Preuve :** calcul exact (`calculs_independants.py`).
  - Avant le deuxième pas, l'unité a 5 TU. Elle en avait donc 9 à la sélection de l'ordre (5 + 4).
  - Trois pas normaux coûtent 12 TU et 6 d'énergie. La destination était donc hors de la zone atteignable et n'était pas sélectionnable : Z1 (R:90, annotation G3) et G3 (R:141), comme le montre T44.
  - Plus généralement, si l'ordre de trois pas a pu être sélectionné, l'unité a au moins 8 TU et 4 d'énergie avant le deuxième pas. Un deuxième pas à 6 TU et 3 d'énergie est donc toujours payable dans ce cadre.
  - Le résultat attendu de (b) est juste au regard de la règle testée (Q3.4, G3, M-05=A). Mais la situation décrite ne peut pas naître d'un ordre sélectionné, et le scénario ne la présente pas comme un état injecté, à la différence de T23 et T37 (« candidats injectés », « sélection abstraite »).
- **Gravité :** mineure. Aucune règle n'est créée, et (a) est exact : il reste 46 TU et 93 d'énergie.
- **Nature :** erreur réelle (cohérence du scénario).
- **Correction proposée (documentaire, au choix de l'auteur) :**
  - soit qualifier (b) d'« état injecté (contrôle abstrait avant le pas), non atteignable par un ordre sélectionné sous Z1 et G3 » ;
  - soit rendre l'état atteignable, par exemple : « 12 TU et 100 d'énergie à la sélection ; le deuxième pas (6 TU et 3 d'énergie) est exécuté, il reste 2 TU ; arrêt avant le troisième pas (4 TU), sans débit ; il reste 2 TU et 95 d'énergie ». J'ai vérifié ce calcul ; il n'utilise que M-05=A, Q3.4, G3 et Z1.
- **État :** exécuté et échoué. Le calcul de cohérence a tourné ; la condition attendue n'est pas remplie.

**AN-04 — Trois expressions entre guillemets ne figurent pas dans le texte cité. C'est le défaut de M-08, ailleurs.**
- **Endroit et preuve :**
  - (a) §3.5, PNV-2, colonne « Statut » (v042:232) : « la formulation « toutes les données géométriques » ne vaut donc pas règle ». D:30 ne contient pas cette expression. Il écrit « Unités physiques de géométrie : mm entiers » et « Les données géométriques et tous leurs arrondis doivent être contrôlés ». L'expression vient de la paraphrase de la colonne 2. Le défaut est **nouveau dans la v0.4.2** ;
  - (b) §20.2, ligne M-15 (v042:890) : « « concordance de troncature » d'ARB-D ». La v0.4.1 (v041:404) et RV41 (l.186) écrivent « Concordance d'ordre et de troncature » ;
  - (c) §13, statut de T26 (v042:600) : « « dans sa case » : PNV-4 ». T26 écrit « le profil ne dépasse pas sa case ». Le défaut est hérité (v041:508).
- **Méthode :** `citations.py` a contrôlé 226 citations. Ces trois-là sont les seules qui ne renvoient ni à une source ni au texte même du document.
- **Gravité :** mineure, sans effet sur le fond.
- **Nature :** erreur réelle (citation inexacte).
- **Correction proposée :**
  - (a) retirer les guillemets ou citer D:30 mot pour mot ;
  - (b) citer « Concordance d'ordre et de troncature » ;
  - (c) écrire « le profil ne dépasse pas sa case » : PNV-4.
- **État :** exécuté et échoué.

**AN-05 — §18, ligne W-11 (a) : T45 figure encore parmi les scénarios qui dépendent d'une PNV.**
- **Endroit :** v042:827 : « dépendances des PNV corrigées (T03, T04, T15, T26, T42, T43, T45, T46) ».
- **Preuve :** la correction de M-13 retire cette dépendance :
  - §13, T45 (v042:619) ;
  - §12, ligne PNV, où T45 a disparu (v042:560) ;
  - §17, contrôle 9 (v042:796) ;
  - §20.2, ligne M-13 (v042:888) : « dépendance à PNV-6 retirée ».

  Le §18 a été actualisé pour huit lignes (V-20), mais pas pour W-11 (a).
- **Gravité :** mineure.
- **Nature :** erreur réelle (incohérence interne).
- **Correction proposée :** ajouter « T45 retiré en v0.4.2 (M-13) ».
- **État :** inspecté seulement.

**AN-06 — Dépendances aux PNV : le raisonnement de M-13 n'est pas appliqué à T03, et T42, T43 et T46 sont rattachés aux PNV sans qu'aucune PNV soit nommée.**
- **Endroit :**
  - §13 : T03 « Pa (géométrie, PNV-6) » (v042:576) ; T42 « Pa (sous-segments) » (v042:616) ; T43 « Pa (géométrie et praticabilité du trajet ; **pas** PNV-7) » (v042:617) ; T46 « Pa (géométrie) » (v042:620) ;
  - §12, ligne PNV (v042:560) ; §17, contrôle 9 (v042:796).
- **Preuve :**
  - selon la correction de M-13, les phases de PNV-6 ne s'appliquent pas à une diagonale à plat, et le contrôle du volume de la diagonale est [INS]. Le §3.5 le dit (v042:236 : « contrôle du volume : [INS] pour la diagonale ») ;
  - T03 est aussi une diagonale à plat. Sa dépendance relève de la géométrie laissée ouverte par G1 (R:134 : dimensions, tolérance, trajectoire), donc de [OUV], et non d'une PNV ;
  - T42, T43 et T46 ne nomment aucune PNV, mais la ligne PNV du §12 les donne pour « conditionnels ».
- **Gravité :** mineure, sans effet sur les statuts : tous restent « Pa ».
- **Nature :** erreur réelle d'étiquetage, **héritée de la v0.4.1**, non introduite par la v0.4.2.
- **Correction proposée :**
  - rattacher ces dépendances à [OUV] (G1, « Ouvert »), ou nommer la PNV en cause et la justifier ;
  - actualiser en conséquence le §12 (v042:560) et le §17, contrôle 9.
- **État :** inspecté seulement.

**AN-07 — §10 : la colonne « Ce qui reste ouvert » porte « — » pour R:166 et pour G3, alors que d'autres sections gardent des points ouverts de même nature.**
- **Endroit :** v042:465 (R:166) et v042:469 (G3).
- **Preuve :**
  - **R:166** vise un « Trajet devenu non payable ou non réalisable en cours de route, à cause d'un coût réel, d'une occupation ou d'un obstacle jusque-là inconnus ». Or le §6 (v042:384) et le §14 (v042:690, « Imprévus : repli d'une diagonale sur le passage Y ») maintiennent un point ouvert de cette famille ;
  - **G3** : sa mention « Ouvert » (R:141) comprend les « coûts en énergie des diagonales et des passages ». Or la ligne R:152 du §10 (v042:459) laisse ouverts les « coûts de chaque connexion » (Q3.10=B) ;
  - dans la v0.4.1, chaque colonne portait un seul point, le coût plus élevé mais encore payable, que M-05=A tranche. La v0.4.2 l'a remplacé par « — », sans reporter les autres points.
- **Gravité :** mineure.
- **Nature :** erreur réelle (incomplétude), en partie héritée.
- **Correction proposée :** R:166 : « repli d'une diagonale sur le passage Y (§6) » ; G3 : « coûts de chaque connexion (Q3.10=B) ».
- **État :** inspecté seulement.

**AN-08 — Traçabilité du §17 : scripts absents de l'inventaire, résultat brut du contrôle 7 réinterprété sans le dire, message 29 décrit de façon réductrice.**
- **Endroit :** §17 (v042:782-798) ; §15, « Outils de vérification » (v042:732-742) ; §17, contrôle 7 (v042:794).
- **Preuve :**
  1. **Scripts.** Le §17 ne nomme aucun script. Les scripts qui l'outillent sont dans `D/verif-v042/` et `D/verif-v04/` mais ne figurent pas au §15 : `check_textes.py` (`b1f732a5…`), `check_matrice.py` (`4660e1e9…`), `calculs_v042.py` (`7869bab8…`), `verif-v04/calculs.py` et `make_v042.py` (`0a6c9f8d…`). C'est le principe de M-17, appliqué aux outils de la v0.4.2. Je les ai relancés : code 0, avec les résultats annoncés.
  2. **Contrôle 7.** La sortie brute de O-5 classe le message 22 « PARTIEL dans PIECES-MANDATS-ET-CONFIRMATIONS.md : 47/2592 car. ». La concordance est fortuite : les 47 caractères sont le titre « BASTION — Mandat de revue indépendante MEC-0001 », que P3 l.31 reprend pour la v0.3. Le §17 écrit « non copié ». C'est exact sur le fond, mais l'interprétation n'est pas dite.
  3. **Message 29.** Le §17 décrit le message 29 (2026-11-19T20:35:55.895Z) comme « annonce d'un envoi ». C'est en réalité un mandat en sept points, qui écrit : « Q1.1 à Q1.4 ne sont pas encore joints. Conserve explicitement leur provenance comme non vérifiée ». Il éclaire la chronologie d'I-1, mais ne figure pas à l'inventaire, dont la pièce 14 ne couvre que le message 22.
- **Gravité :** mineure, sans effet sur le fond.
- **Nature :** erreur réelle de traçabilité.
- **Correction proposée :**
  - inscrire les scripts au §15, avec leur empreinte ;
  - dire que la concordance de 47 caractères est fortuite ;
  - décrire le message 29 exactement, et le citer si l'on veut au §0.1.
- **État :** exécuté et réussi pour les scripts (relancés) ; inspecté seulement pour les descriptions.

### 2.4 Préférences de rédaction et observations (ce ne sont pas des erreurs)

- **OB-01 — §5, M-04=B, sixième point (v042:333).** « La clause inscrite d'ARB-D « La surcharge ne majore pas le prix des pas » (R:124) n'est pas modifiée. »
  - Ce point est présenté sous « Application (P6 l.35-40) », mais il ne figure pas dans P6 : c'est un rappel de [INS] R:124.
  - Il est juste sur le fond. Depuis G3, le « prix » d'un pas comprend les TU et l'énergie : les modalités futures de M-04=B ne pourront donc pas prendre la forme d'un surcoût des pas sans modification explicite d'ARB-D.
  - Je propose d'indiquer sa source propre (« [INS] R:124 »).
- **OB-02 — §6 (v042:382).** « Le point du registre […] (R:166) est tranché sur ce point. » C'est une conséquence documentaire exacte de M-05=A, mais P6 ne le dit pas. Je propose de la marquer [DÉD].
- **OB-03 — T48 (b) (v042:622).** « Un arrondi préalable au millimètre donnerait 852 » n'est vrai que pour un arrondi au plus proche ou vers le bas. Un arrondi vers le haut donne 853, puis 854. Je propose de préciser « au millimètre le plus proche ». Le résultat attendu de 854 mm est exact.
- **OB-04 — §2 bis (v042:147).** « R-7=A et R-8=A, qui sont des clarifications » : le statut de R-8=A est « articulation validée » (P6 l.107). Le tableau du §2 bis le cite d'ailleurs correctement.
- **OB-05 — §0 : [TR] et [TR-M] qualifient la transmission dans la session, et non l'échange d'origine.**
  - Le message 30 (P1, message 1) regroupe lui-même cinq validations (P1 l.67, 111, 165, 213 et 293).
  - Le message A les situe entre 14 h 26 et 14 h 47 UTC (P2 l.12-14). C'est une déclaration, non une preuve.
  - Le §0 et la pièce 16 le laissent entendre, sans le dire. Une phrase suffirait.
- **OB-06 — M-04=B et N14.**
  - Le §2 rattache M-04=B à N14 (v042:117). Le §9.2 ne prévoit l'annotation de M-04=B que sous ARB-D (v042:450).
  - N14 (R:103-111) renvoie au « principe d'OXCE ». Or OXCE ne réduit pas l'énergie selon la charge : `prepareEnergy`, `src/Savegame/BattleUnit.cpp:2733-2742`, lu au commit `441cae1b`.
  - Ce n'est pas une contradiction : N14 n'exclut pas un effet sur l'énergie, M-04=B est une décision postérieure du propriétaire, et le §11 n'affirme aucune fidélité. C'est un point d'articulation à traiter avec les modalités de M-04=B et lors d'une future annotation de N14.
- **OB-07 — T26 (v042:600).** Ses sources « Q1.1 à Q1.7 » incluent Q1.4, qui est historique, alors que la matrice rattache Q1.4 à « aucun ». La source est citée en trop ; c'est sans conséquence.
- **OB-08 — Écart dans la commande de la présente revue, et non dans la v0.4.2.** Le tableau des pièces qui m'a été remis donne pour P2 l'empreinte `b69ba3b7…a869`. Le fichier, comme la v0.4.2 (v042:712), donne `…37b869`.

### 2.5 Décisions volontairement reportées (ce ne sont pas des défauts)

- Modalités de M-04=B : existence de l'effet selon la situation, déclenchement, calcul, valeurs (P6 l.38, l.42).
- Modalités techniques de R-5=A : conversion, précision numérique, arrondis des autres grandeurs calculées (P6 l.67, l.70).
- Les neuf PNV, conservées comme non validées (P6 l.183-184).
- Les points [OUV] du §14 (P6 §6).
- Le statut de MEC-0001 et de MEC-0002, qui restent reportées, et toute inscription (P6 l.198-209).

## 3. Contradictions de gameplay

**Aucune contradiction n'est établie** entre la v0.4.2 et Q1 à Q5, B3, GE-02, GE-03, GE-05, CO-01, ARB-D, ARB-E, G1 à G4 et S10. Les constats ci-dessous ont été inspectés seulement.

- **M-05=A, Q4.21, G3 et Z1.**
  - Le « coût réel supérieur » de Q4.21 (D:115) se lit désormais « supérieur aux ressources » (v042:373). M-05=A et P6 l.50 le fondent.
  - L'ordre continue sans recalcul (D:115 ; P6 l.53). Une unité peut donc s'arrêter plus loin, sur un pas devenu non payable. C'est cohérent avec S5 et Z1 : « Une interruption imprévue reste possible » (R:75, R:90).
- **M-04=B et ARB-D.** Le texte d'ARB-D est conservé : « L'énergie est récupérée séparément » et « La surcharge ne majore pas le prix des pas » (R:124). **Points d'articulation à traiter lors de la définition des modalités**, qui ne sont pas des contradictions :
  - la clause sur le prix des pas (OB-01) ;
  - « aucune immobilisation liée à la charge » (N14 et annotation G3, R:105) ;
  - le « principe d'OXCE » de N14 (OB-06).
- **R-6=A, R-7=A, GE-02 et B3-02.** La hauteur de 3 000 mm est fixe, sans réglage global ni par carte. La phrase de B3-02 sur les « constantes universelles » ne s'applique pas à cette hauteur (v042:209), en vertu de W-01, de P3 l.90 et de R-6=A. T27 exclut aussi tout réglage « de l'altitude de référence ». C'est une lecture de R-7=A (« seules les variations locales de support demeurent ») : elle est défendable, et je ne propose aucun arbitrage.
- **R-8=A et B3-03.** R-8=A apporte la « précision explicite » qu'exigeait P2 l.42 pour GE-03. GE-04, GE-05 et CO-01 sont inchangées (v042:443).

## 4. Corrections strictement indispensables

Toutes sont **documentaires** et n'exigent **aucun nouvel arbitrage** :
1. **AN-01 :** ajouter ⟨B3-03⟩ à T04, ou rendre exacte la ligne M-01 du §20.2.
2. **AN-02 :** désigner sans ambiguïté les messages du §0.1, par leur numéro et leur horodatage.
3. **AN-03 :** qualifier T47 (b) d'état injecté, ou le reformuler pour le rendre atteignable sous Z1 et G3.
4. **AN-04 (a) et (b) :** retirer ou corriger les deux guillemets inexacts de v042:232 et v042:890.
5. **AN-05 :** actualiser la ligne W-11 (a) du §18 (T45).
6. **AN-07 :** compléter les cellules « — » de R:166 et de G3 au §10.

**Recommandées, non indispensables :** AN-04 (c), AN-06, AN-08 et OB-01 à OB-07.

## 5. Réserves documentaires et paramètres encore ouverts

**Réserves documentaires :** RD-1 à RD-8 de la v0.4.2 (v042:668-676) sont exactes. J'ajoute ou je précise :
- **Authentification.** Aucune pièce n'est authentifiée de façon indépendante.
  - P1 à P6 sont des copies. J'ai vérifié leur fidélité au journal de session, pas à la conversation de conception, qui reste inaccessible.
  - Le journal est un fichier local sans empreinte stable (v042:742). L'attribution de ses entrées « user » au propriétaire repose sur l'outil de session.
  - RV41 est authentifié par son empreinte seulement.
- **Q1.1 à Q1.4.** La présence des options B dans la conversation d'origine, et l'existence de deux options seulement, reposent sur les déclarations du propriétaire (P5 l.11 ; P3 l.108). [TR] et [TR-M] qualifient la transmission, non l'échange d'origine (OB-05).
- **Q4.** Les formulations sont des résumés de l'orchestrateur (RD-2). PNV-7 et PNV-8 en dépendent.
- **Options absentes.** Pour Q5.1, Q5.2, B3 et les six arbitrages, aucun texte d'option n'est transmis (RD-3).
- **P4.** Sa fidélité au rapport d'origine de la revue de la v0.3 n'est pas vérifiable.
- **Message C, §E (P2 l.114).** Un verdict « pleinement conforme » reste subordonné à la vérification des preuves de validation, ce qui suppose l'archivage.

**Paramètres encore ouverts :** la liste du §14 (v042:678-698) couvre les neuf points de P6 §6 (l.173-181) :
- modalités énergétiques de la surcharge ;
- déclenchement du débit d'un pas engagé ;
- support pendant les phases du pas ;
- cycles gratuits et terminaison de la recherche ;
- critères du réveil ;
- orientation et volume balayé ;
- tolérances et précision ;
- connexions et transferts ;
- surveillance.

Il faut y ajouter le repli d'une diagonale sur le passage Y et les coûts de chaque connexion, que le §10 omet (AN-07).

## 6. Aptitude du dossier à l'archivage documentaire

- **Les pièces** P1, P2, P3, P5 et P6, O-1, O-4 et les scripts sont **aptes à être archivées en l'état**. Leur fidélité aux messages du journal est vérifiée, et la seule omission, la partie « Mission » du message 31, est déclarée (v042:54, 674, 710). Les archiver est justement ce que demande RD-1.
- **La consolidation v0.4.2** est **apte à l'archivage sous réserve** d'une version corrective limitée aux six corrections indispensables du §4. Ces corrections sont purement documentaires : elles ne demandent aucun arbitrage, et un contrôle ciblé du diff paraît suffire. Ce choix revient au propriétaire.
- **Archiver n'est pas inscrire.** MEC-0001 et MEC-0002 restent reportées. Toute inscription exige un mandat distinct qui couvre les deux fiches (P2 l.255 ; v042:409).

## 7. Contrôle point par point des vérifications 1 à 11

| # | Vérification | Constat | État |
|---|---|---|---|
| 1 | Six arbitrages, sans extension implicite | Textes et statuts identiques à P6 l.32, 45, 59, 73, 85, 96 et l.42, 56, 70, 82, 93, 107 (script de l'auteur relancé, et lecture). Plages l.30-42, 43-56, 57-70, 71-82, 83-93, 94-107 exactes. Conséquences reprises de P6 aux sections déclarées (`sections_arbitrages.py`). Aucune extension de fond ; attributions à préciser (OB-01, OB-02, OB-04) | exécuté et réussi (textes) ; inspecté seulement (extensions) |
| 2 | I-1 : chronologie, messages et compilation, statuts | Message 31 (19 nov., 20:54:21.612Z) : options A et validation, sans aucune option B ; message 34 (20 nov., 12:53:14.601Z) ; v0.4 remise à 13:05:12.403Z ; message 35 (13:41:45.327Z) : options B. Compilation signalée (v042:73). [TR], [TR-M] et [VAL] justifiés par P3 l.116, P6 l.119 et P6 l.28-29. Désignations ambiguës (AN-02) ; [TR] porte sur la transmission (OB-05) | exécuté et réussi (chronologie, textes) ; inspecté seulement (désignations) |
| 3 | M-01 à M-18 contre RV41 | Tableau du §8 : 17 corrections effectives, 1 partielle (M-01) | exécuté et échoué (M-01) ; les autres, voir §8 |
| 4 | Cohérence avec Q1 à Q5, B3, GE-02, GE-03, GE-05, CO-01, ARB-D, ARB-E, G1 à G4, S10 | Aucune contradiction ; renvois `R:N` exacts (registre relu) ; points d'articulation au §3 | inspecté seulement |
| 5 | M-04=B ne définit aucune pénalité énergétique | Les 17 occurrences de M-04 et les mentions de la surcharge liées à l'énergie ont été relues : aucun multiplicateur, arrondi, seuil ni pénalité. T20 et T21 ne portent que sur les TU. La matrice indique « aucun scénario spécifiable » | exécuté et réussi (`grep`) ; inspecté seulement |
| 6 | M-05=A : contrôle avant le pas, ressources disponibles, interruptions prioritaires | Contrôle avant chaque pas des TU et de l'énergie (G3, Q3.4) ; débit au coût réel ; interruption si le pas n'est plus payable ou devient inadmissible ; aucun débit d'un pas non commencé ; pas de recalcul (v042:375-382). Les événements physiques prioritaires (Q4.3, Q5.1) gardent leur place dans le tableau des états du pas (v042:351-356). T47 (b) incohérent (AN-03) | exécuté et réussi (T47 (a)) ; exécuté et échoué (T47 (b)) |
| 7 | Calculs, en particulier T47 et T48 | `calculs_independants.py` : TOUS_OK = True. Barème, coïncidences du §11, T01, T02, T05 (énumération exhaustive), T11a, T18 à T23, T26, T37, T39, T44, T45, T47 (a) 46/93, T47 (b) 5/98, T48 (b) 1 205/√2 = 852,0637 → 854 (encadrement exact par les carrés), §3.6 (1 400, 850, 1 274, 1 341,6 à 26,6°, 0,5), float32 de 1/41 × 41 = 0,99999994 | exécuté et réussi ; cohérence de T47 (b) : échoué (AN-03) |
| 8 | Neuf PNV, points ouverts, absence de règle non sourcée | Les neuf PNV sont conservées ; PNV-2 est actualisée par R-5=A (P6 l.66) ; PNV-4 cite D:34 mot pour mot. Aucune PNV dans un scénario « Sp » (script). Les neuf points de P6 §6 sont présents au §14. Aucune règle nouvelle trouvée. Écarts : AN-04 (a), AN-06, AN-07 | exécuté et réussi (script) ; inspecté seulement (le reste) |
| 9 | Matrice, rattachements, citations, empreintes, inventaire | 73 rattachements cités ; 226 citations (3 inexactes : AN-04) ; 66 renvois citation → ligne exacts ; empreintes identiques au §15 ; scripts du §17 non inventoriés (AN-08) | exécuté et réussi ; exécuté et échoué (AN-04) |
| 10 | Modifications proposées pour MEC-0002, non inscrites | Le §9 les présente comme des propositions, sans inscription autorisée (v042:409). Le registre sur `main` est inchangé (`9117d20c…`) ; R:203, R:204 et R:336 gardent leur texte historique. Les annotations de GE-02, de GE-03 et de R:336 sont conformes à B3, au rectificatif et à R-5 à R-8. GE-04, GE-05 et CO-01 sont inchangées | exécuté et réussi (registre) ; inspecté seulement (textes) |
| 11 | Fidélité aux copies, limites d'authentification | Copies fidèles au journal (§1) ; le document cite les copies exactement (citations, renvois) ; limites déclarées (v042:46, 81-86, RD-1, RD-6, v042:800-804) ; limites complémentaires au §5 | exécuté et réussi ; authenticité d'origine : non vérifié |

## 8. Tableau I-1 et M-01 à M-18

« Constat d'origine » résume RV41 ; la ligne du rapport est indiquée. « État » : état de la correction dans la v0.4.2, puis état de mon constat.

| N° | Constat d'origine (RV41) | Dans la v0.4.2 | État |
|---|---|---|---|
| I-1 | l.43-62 : limites du §0.1 incomplètes (aucune option B dans le message reçu ; nombre d'options déclaré ; [TR] recouvrant deux qualités de preuve) | §0.1 réécrit (v042:48-90) ; [TR-M] (v042:35) ; réserve du §12 (v042:499-502) ; RD-5. Les trois points sont traités | **corrigé**, désignations ambiguës (AN-02) ; exécuté et réussi |
| M-01 | l.66-72 : ⟨B3-03⟩ absent à cinq endroits (l.177, 178, 180, 337, 485) | ajouté à v042:245, 246, 248 et 420 ; **absent de T04** (v042:577) | **partiel** (AN-01) ; exécuté et échoué |
| M-02 | l.74-77 : T21 n'explique pas le maximum fictif de 20 | explication dans T21 (v042:595) ; min(s + 60, 60) = 60 pour s de 0 à 60, recalculé | corrigé ; exécuté et réussi |
| M-03 | l.79-98 : dix rattachements non cités | critère énoncé (v042:495) ; les dix traités ; 73 rattachements, tous cités | corrigé ; exécuté et réussi |
| M-04 | l.100-111 : [DÉD] « la surcharge ne réduit pas l'énergie » | retiré ; M-04=B intégré (v042:327-333) | corrigé par arbitrage ; inspecté seulement |
| M-05 | l.113-121 : lecture [DÉD] de Q4.21 | remplacée par M-05=A (v042:373-382) ; T47 | corrigé par arbitrage ; T47 (b) : AN-03 ; exécuté |
| M-06 | l.123-130 : [DÉD] impropre pour l'observation sur l'option B de Q1.4 | « observation documentaire, sans valeur de décision » ; apports de W-01 et de R-6=A (v042:88) | corrigé ; inspecté seulement |
| M-07 | l.132-135 : PNV-7 dans « Précisée ou modifiée par » | « — (priorité « X puis Y » non décidée : PNV-7) » (v042:123) | corrigé ; inspecté seulement |
| M-08 | l.137-140 : « tout le volume » absent de D:34 | D:34 cité mot pour mot (v042:234) | corrigé ; même défaut ailleurs (AN-04) ; exécuté et réussi |
| M-09 | l.142-148 : T24 sans l'exception de G2 | exception rappelée (v042:598, 280, 833) | corrigé ; inspecté seulement |
| M-10 | l.150-155 : citation de Q4.15 attribuée au message B | attribuée à P2 l.95 ; message B (P2 l.38) cité pour Q5.2 (v042:277) | corrigé ; exécuté et réussi (renvoi vérifié) |
| M-11 | l.157-160 : « Ces chiffres sont identiques… » | limité à l'énergie, 100 et 20 ; TU non concernées (v042:313) | corrigé ; exécuté et réussi (P1 l.201) |
| M-12 | l.162-165 : RD-2 omet Q4.1 | contenu de Q4.1 confirmé par W-01 et R-6=A (v042:670) | corrigé ; inspecté seulement |
| M-13 | l.167-173 : T45 incohérent avec T02 et T22 | T45 « Sp (passage supposé praticable…) ; test intégré : Pa » (v042:619) | corrigé ; reliquats AN-05 et AN-06 ; inspecté seulement |
| M-14 | l.175-184 : P0-05, P0-06, G1-01 et §5.5 de la v1.4.1 | v042:634, 644-645 et 663 ; v1.4.1 l.150, 151, 169 et §5.5 (l.196-204) relus ; 37 cas sur 37 couverts | corrigé ; exécuté et réussi |
| M-15 | l.186-194 : « Concordance d'ordre et de troncature » sans nuance | calcul flottant d'OXCE distingué du plancher exact ; code relu (`BattleUnit.cpp:2714-2720`, `setValueMax` l.1612-1615) ; émulation refaite (v042:488) | corrigé ; citation du §20.2 inexacte (AN-04 b) ; exécuté et réussi |
| M-16 | l.196-201 : P1 « reproduit tel que reçu », partie « Mission » omise | omission déclarée (v042:54, 674, 710) ; P1 non modifiée | corrigé ; exécuté et réussi (journal) |
| M-17 | l.203-208 : outils non inventoriés ; choix de ne pas modifier P1 non dit | O-1 à O-6 inventoriés ; « P1 n'est pas modifiée ; elle est complétée par la pièce 1 bis » (v042:710, 732-742) | corrigé ; scripts du §17 non inventoriés (AN-08) ; exécuté et réussi (empreintes) |
| M-18 | l.210-213 : « P2 l.215 environ » | « P2 l.217 » (v042:819) ; la ligne contient « peuvent être exprimées en millimètres » | corrigé ; exécuté et réussi |

## 9. Commandes exécutées et codes de sortie

Scripts et sorties dans `D/revue-v042-relecteur/`. Python a toujours été lancé avec `python3 -I`. Git n'a servi qu'en lecture : `rev-parse`, `show` et `log`.

| # | Commande | Code | Résultat |
|---|---|---|---|
| 1 | `ls -la` sur les dossiers de revue | 0 | inventaire des fichiers |
| 2 | `sha256sum` sur 22 fichiers (pièces, scripts O-2 et O-5, extractions, scripts de l'auteur) | 0 | identiques aux déclarations ; écart du seul tableau de commande pour P2 (OB-08) |
| 3 | `python3 -I verif-v04/extract_user_msgs.py <journal> messages-reextraits.md` | 0 | 37 messages ; le 37e est le présent mandat |
| 4 | `compare_extractions.py` | 0 | O-1 = mes 35 premiers messages, O-4 = mes 36 premiers, reconstruits octet pour octet |
| 5 | `awk` sur les messages 2, 22, 23, 29, 31 et 37 | code non relevé ; sortie observée | textes lus |
| 6 | `fidelite_copies.py` (dans les deux sens) | 0 | messages 24 à 28, 30 et 32 à 36 copiés intégralement ; message 31 : préfixe de 1 067 sur 2 023 caractères ; messages 22 (concordance fortuite de 47 caractères), 23 et 29 non copiés ; chaque bloc copié est une sous-chaîne de son message |
| 7 | `python3 -I verif-v042/omissions.py` (O-5, script de l'auteur) | 0 | message 22 classé « PARTIEL 47/2592 », de façon fortuite (AN-08) |
| 8 | `remise_v04.py` (horodatage 2026-11-20T13:05:12.403Z) | 0 | message de l'auteur contenant la v0.4 à l'identique |
| 9 | `git -C bastion rev-parse origin/main` ; `git show origin/main:<7 fichiers> \| sha256sum` ; `git log --oneline -8` ; `git log -1 1ecc608` | 0 (rev-parse, log) ; empreintes observées | `818c646c…` ; pièces 7 à 11 identiques ; `1ecc608` du 2026-11-18 |
| 10 | `git show origin/main:` registre, v1.4.1, LOT-2A et rapport d'inscription, vers des fichiers locaux | 0 | `registre.md`, `v141.md`, `lot2a.md`, `inscription.md` |
| 11 | `git -C oxce rev-parse HEAD` ; `git show HEAD:src/Savegame/BattleUnit.cpp` (l.1605-1620 et 2700-2745) | 0 ; 0 | `441cae1b…` ; l.2714, 2717 et 2720 conformes au §11 |
| 12 | `calculs_independants.py` | 0 | TOUS_OK = True ; incohérence de T47 (b) relevée (AN-03) |
| 13 | `diff -u v0.4.1 v0.4.2 > mon-diff.patch` ; `cmp` avec le patch fourni (en-têtes exclus) | 1 (attendu) ; 0 | patch identique ; 28 blocs |
| 14 | `grep` des lignes retirées et ajoutées ; `blocs_diff.py` | 0 | chaque bloc tombe dans une section déclarée au §20 |
| 15 | `citations.py` (trois passes : sources primaires ; avec v0.4.1 et RV41) | 0 | 226 citations ; 198 retrouvées dans les sources primaires, 23 dans v0.4.1 ou RV41, 5 renvoient au texte même ; 3 inexactes (AN-04) |
| 16 | `renvois_lignes.py` ; `renvois_lignes2.py` | 0 ; 0 | 23 + 43 renvois concordants, 0 écart |
| 17 | `matrice.py` | 0 | 73 rattachements, tous cités (Q1.4 : « aucun ») ; aucune PNV dans un « Sp » |
| 18 | `python3 -I verif-v042/check_textes.py …` ; `check_matrice.py` ; `calculs_v042.py` ; `verif-v04/calculs.py`, puis `cmp` avec `calculs-v04.txt` | 0 ; 0 ; 0 ; 0 ; 0 | résultats annoncés au §17 reproduits |
| 19 | `sha256sum verif-v04/diff-v0.4-v0.4.1.patch` | 0 | `1d6d2a58…`, identique à O-3 |
| 20 | `grep` du marqueur ⟨B3-03⟩ aux cinq endroits de M-01 | sortie observée | T04 sans marqueur (AN-01) |
| 21 | `git -C bastion show --stat 1ecc608` | 0 | ajoute la v1.4.1, le mandat v1.0 et le rapport d'archivage |
| 22 | `grep` des 37 identifiants de cas de la v1.4.1 dans le §13 | sortie observée | 37 sur 37 présents |
| 23 | `options_b.py` | 0 | options B présentes seulement dans le message 35 ; options A seulement dans le message 31 ; huit libellés exacts aux §0.1 et §3.1 |
| 24 | `sections_arbitrages.py` | 0 | chaque arbitrage figure dans toutes les sections déclarées |
| 25 | `grep` de M-04 et des mentions de la surcharge liées à l'énergie | sortie observée | aucune pénalité définie |
| 26 | décompte des statuts des 49 scénarios ; `sha256sum` final des pièces | sortie observée | 29 Sp, 17 Pa, 1 Ou, 2 mixtes (T11a, T48) ; pièces inchangées |
| 27 | `sed -i` sur mon propre `citations.py` | 0 | sans effet, à cause d'un échappement |
| 28 | `python3 -I -` pour corriger mon `citations.py` | 1 (AssertionError) | aucune écriture ; script réécrit ensuite dans mon dossier |

## 10. Classement des constats

**Exécuté et réussi :**
- empreintes des pièces, du dépôt et des outils ; pièces inchangées en fin de revue ;
- réextraction du journal, et identité avec O-1 et O-4 ;
- fidélité de P1 (message 1), P2, P3, P5 et P6 ; P1, message 2, préfixe exact du message 31 ;
- horodatages des messages 22 à 36 et de la remise de la v0.4 ;
- absence d'option B avant le message 35 ; huit libellés et validation ;
- textes et statuts des six arbitrages ;
- identité du diff avec le patch ; correspondance des 28 blocs avec le §20 ;
- 198 + 23 citations ; 66 renvois de lignes ;
- 73 rattachements de la matrice ; absence de PNV dans les scénarios « Sp » ;
- tous les calculs, T47 (a) et T48 compris ;
- couverture des 37 cas de la v1.4.1 ;
- code OXCE aux lignes citées ; émulation float32 ;
- scripts de l'auteur (codes 0) ;
- registre inchangé sur `main`.

**Exécuté et échoué** (le contrôle a tourné, et la condition attendue n'est pas remplie) :
- marqueur ⟨B3-03⟩ de T04 (AN-01) ;
- cohérence de T47 (b) avec Z1 et G3 (AN-03) ;
- trois citations inexactes (AN-04).

**Inspecté seulement :**
- désignation des messages au §0.1 (AN-02) ;
- §18, ligne W-11 (a) (AN-05) ;
- étiquettes PNV de T03, T42, T43 et T46 (AN-06) ;
- cellules « — » du §10 (AN-07) ;
- descriptions du §17 (AN-08) ;
- absence d'extension implicite des arbitrages ;
- cohérence de gameplay (§3) ;
- textes proposés pour MEC-0002 ;
- corrections M-04 à M-07, M-09, M-12 et M-13.

**Non vérifié :**
- authenticité des messages du propriétaire et de la conversation de conception ;
- présence des options B dans cette conversation, et nombre d'options d'origine ;
- textes des options de Q5.1, Q5.2, B3 et des six arbitrages ;
- fidélité de P4 au rapport d'origine ;
- origine des 23 citations qui ne se retrouvent que dans la v0.4.1 ou dans RV41, au-delà de ces deux textes ;
- comportement d'OXCE à l'exécution : le code a été lu, ni compilé ni exécuté ;
- exécution des scénarios comme tests ;
- rapports de Claude Code du 19 novembre (pièce 15).

## 11. Écarts au périmètre et fichiers produits

**Écarts :** aucun.
- Je n'ai écrit que dans `D/revue-v042-relecteur/`.
- Deux commandes ont été lancées depuis un autre répertoire, sans y rien écrire : le `diff` depuis `D/revue-v03/`, avec une sortie redirigée vers mon dossier, et les scripts de l'auteur depuis mon dossier, avec leurs chemins passés en argument.
- Git n'a servi qu'à `rev-parse`, `show` et `log`, sur le dépôt comme sur le clone OXCE. Je n'ai fait aucun accès réseau.
- Le journal n'a servi qu'à deux choses : les entrées du propriétaire, et le message de l'auteur daté 13:05:12.403Z, pour l'horodatage de remise de la v0.4.

**Fichiers produits**, tous dans `D/revue-v042-relecteur/` :
- le présent rapport ;
- scripts : `compare_extractions.py`, `fidelite_copies.py`, `remise_v04.py`, `calculs_independants.py`, `citations.py`, `matrice.py`, `options_b.py`, `renvois_lignes.py`, `renvois_lignes2.py`, `sections_arbitrages.py`, `blocs_diff.py` ;
- extraits et sorties : `messages-reextraits.md`, `registre.md`, `v141.md`, `lot2a.md`, `inscription.md`, `mon-diff.patch`, `a.tmp`, `b.tmp`, `statuts.txt`, `sortie-calculs-v04-auteur.txt`.

Je ne prends aucune décision de gameplay et ne crée aucun arbitrage. Les corrections proposées sont documentaires, et la décision revient au propriétaire. MEC-0001 et MEC-0002 restent reportées.
