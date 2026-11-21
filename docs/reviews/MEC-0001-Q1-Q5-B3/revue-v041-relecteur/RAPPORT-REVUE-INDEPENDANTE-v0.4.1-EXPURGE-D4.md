# Revue indépendante de la consolidation MEC-0001 v0.4.1 (Q1 à Q5 et B3)

- **Objet :** `D/revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md`, 730 lignes. SHA-256 recalculé : `bd4cf4fa5f94aa005c6e27bf81eb6cc6aba6e7365c8eccaddaf847320a699e3f`. Il est identique à l'empreinte déclarée.
- **Relecteur :** agent distinct de l'auteur. J'ai travaillé en lecture seule. Je ne m'accorde pas la validation finale, qui revient au propriétaire.
- **Date :** 20 novembre 2026.
- **Bases :**
  - `origin/main` = `818c646c7d33b819d8b69b81679749be6e77eff9` ;
  - clone OXCE au commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, qui est le commit figé de `docs/references/OXCE-BASELINE.md` (l.13).
- **Notations :**
  - `D` = `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad` ;
  - « v0.4.1 l.N » : ligne du document revu ; « P1 l.N » à « P5 l.N » : ligne d'une copie ; `R:N` : ligne du registre sur `main` ; `D:N` : ligne de la v0.2 ;
  - « journal » : messages du propriétaire extraits mécaniquement du journal de session (fichier `MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md`, que j'ai réextrait moi-même à l'identique).

## 1. Verdict : conforme sous réserves

**Ce qui est vérifié :**
- **Intégrité.** Les douze empreintes déclarées et les sept fichiers du dépôt, recalculés, sont identiques.
- **Portée de la v0.4.1.** Mon propre `diff` de la v0.4 à la v0.4.1 est identique au patch fourni. Ses 16 blocs sont tous couverts par V-01 à V-12, et je n'ai trouvé aucun changement non déclaré. La correction de RD-1 (« 7 à 11 ») est exacte.
- **Copies.** P1, P2, P3 et P5 sont identiques aux messages du propriétaire du journal. P1, message 2, ne reprend que le début du message reçu.
- **Calculs.** Tous les résultats chiffrés sont retrouvés en arithmétique exacte.
- **W-01 à W-14.** Ils sont corrigés en substance.
- **PNV.** Les neuf ont le bon statut, et aucune n'intervient dans un scénario « Sp ».
- **Rapport à OXCE.** Le §11 n'affirme aucune fidélité.
- **Reclassement de Q1.1 à Q1.4 en [TR].** Il est conforme au mandat. La condition de P3 l.116 est remplie au sens où le propriétaire a lui-même décrit les pièces (P3 l.108) : options A et B, puis validation. Les options citées sont exactes.

**Ce qui empêche le verdict « conforme » :**
- **Une anomalie importante, purement documentaire (I-1).** Les limites du §0.1 sont justes mais incomplètes. Elles ne disent pas que le message reçu le 19 novembre ne contenait aucune option B. Et le code [TR] couvre désormais deux qualités de preuve, sans distinction visible au §3.1 ni au §12.
- **Dix-huit anomalies mineures.** Elles comprennent deux lectures [DÉD] trop affirmatives (M-04 et M-05), qui frôlent la décision implicite sans la constituer.
- **Des réserves structurelles, qui subsistent même après correction.** Les pièces sont des copies, non authentifiées et non archivées. Les formulations de Q4 sont des résumés. Les options d'origine de Q5.1, Q5.2 et B3 manquent. Or le message C, §E (P2 l.114), subordonne un verdict « pleinement conforme » à la vérification des preuves de validation.

**Aucune anomalie bloquante.** Je n'ai trouvé aucune nouvelle règle de gameplay introduite sans source.

## 2. Anomalies

Pour chaque anomalie, j'indique si sa correction est **documentaire** ou si elle demande un **arbitrage** du propriétaire.

### 2.1 Bloquant

Aucune.

### 2.2 Important

**I-1 — Reclassement de Q1.1 à Q1.4 : limites du §0.1 incomplètes ; [TR] non qualifié au §3.1 et au §12.**

- **Endroit :** §0.1 (v0.4.1 l.42-58) ; §0 (l.30) ; §3.1 (l.104-107) ; §12 (l.413-416).
- **Preuve :**
  1. **Le message reçu ne contenait aucune option B.** Le message 31 du journal (2026-11-19T20:54:21.612Z) commence exactement par P1 l.299-310 : le script `compare_copies.py` répond « P1 msg2 = préfixe du message 31 : True ». La suite du message ne contient que « Mission : 1. Réévaluer la réserve bloquante… ». Les options B n'ont donc pas été omises par la copie : elles manquaient au message tel que reçu dans la session.
     - P3 l.108 (« Les pièces comprennent, pour chacune de ces décisions, les deux options A et B ») ne correspondait donc pas au dossier, le 20 novembre à 12:53Z.
     - P5 l.11 (« Elles sont absentes de ta copie P1 ») peut se lire comme le constat d'une copie défectueuse.
     - La v0.4.1 n'en dit rien. Elle écrit seulement : « la proposition est transmise en deux messages » (l.54).
  2. **Le nombre d'options repose sur une déclaration.** Qu'il n'existe que deux options, A et B, ne repose que sur les déclarations du propriétaire (P3 l.108 ; P5 l.11-19). Q1.5 à Q1.9 en avaient trois (P1 l.13-53). Le §0.1 constate que « chacune des quatre décisions a maintenant deux options » (l.48), sans préciser que ce nombre est déclaré, non attesté.
  3. **[TR] recouvre deux qualités de preuve.** Pour Q1.5 à Q3.14, [TR] désigne une copie de propositions complètes : descriptions, mention « (recommandé) », message 30 du journal. Pour Q1.1 à Q1.4, il désigne une restitution en deux temps :
     - les libellés A ne portent ni guillemets ni mention « recommandé », et celui de Q1.4 est au passé (P1 l.307) ;
     - les libellés B sont arrivés le 20 novembre à 13:41:45Z, après que la v0.4 eut demandé de les joindre (v0.4 l.46 : « Pour lever ce point : joindre les libellés des options B. »).

     La distinction n'apparaît que dans la définition du §0 (l.30) et au §0.1. Au §12, la colonne « Réserves » de Q1.2 et de Q1.3 porte « — ».
- **Correction documentaire proposée :**
  - ajouter au §0.1, parmi les limites :
    - (a) que P1, message 2, reproduit fidèlement le message reçu, et que celui-ci ne contenait pas les options B ;
    - (b) que l'existence de deux options seulement est déclarée par le propriétaire (P3 l.108, P5) ;
  - porter au §12, pour Q1.1 à Q1.4, la réserve « proposition restituée en deux messages (§0.1) ».
- **Arbitrage :** aucun n'est nécessaire, puisque P3 l.116 a fixé la catégorie. Si le propriétaire veut réserver [TR] aux propositions transmises en une seule fois, c'est à lui de le dire.

### 2.3 Mineur

**M-01 — W-02 : marqueur ⟨B3-03⟩ absent sur plusieurs valeurs tirées de Q1.**
- **Endroit :** §3.6, l.177 (1 274 mm), l.178 (1 341,6 mm) et l.180 (profil dans la case) ; §9.1, l.337 (rapport 0,5) ; T04, l.485 (seuils de Q1.9).
- **Preuve :**
  - un `grep` montre que le marqueur figure aux l.175, 176 et 179, mais pas aux lignes citées ;
  - B3-03 vise précisément le profil humain (P2 l.157-169) ;
  - le rectificatif, §3, écrit : « Sous réserve de leur confirmation, […] un rapport case/étage de 0,5 » (P2 l.239).
- **Correction documentaire :** ajouter ⟨B3-03⟩ à ces cinq endroits.

**M-02 — W-03 : la bonne explication ne figure pas dans T21.**
- **Endroit :** §13, T21 (l.503). L'explication n'est qu'au §18, l.686.
- **Preuve :** P3 l.124-126 demande de « Corriger l'explication du plafond de TU ». La phrase fausse a bien disparu, et les résultats 15, 17, 12 et 13 sont exacts (calcul exact). Mais T21 n'explique plus pourquoi il utilise un maximum fictif de 20.
- **Correction documentaire :** ajouter à T21 : « avec le profil Q4.6, min(solde + 60, 60) = 60 pour tout solde ≥ 0 ; ce profil ne distingue pas ARB-D d'une remise au maximum, d'où le maximum fictif de 20 ».

**M-03 — W-11 (b) : le même défaut subsiste pour d'autres rattachements du §12.**
- **Endroit :** §12, l.416, 420, 428, 429, 431, 433, 435 et 447.
- **Preuve :** le script `matrice_scenarios.py` relève dix rattachements où le scénario ne cite pas la décision dans ses sources :
  - Q1.4 et Q1.8 → T27 ;
  - Q3.1 → T01 et T02 ;
  - Q3.2 → T02 ;
  - Q3.4 → T44 ;
  - Q3.6 → T22 ;
  - Q3.8 → T18 ;
  - Q4.6 → T01 et T21.

  Certains rattachements se défendent :
  - T01, T02 et T18 dépendent de ces décisions par le préambule du §13 (l.474-478 : « barème du §5 », « profil Q4.6 ») ;
  - T27 teste la règle qui a supplanté Q1.4 et le cadre configurable de Q1.8.

  D'autres non :
  - T44 teste Z1 sans qu'aucun pas ne commence, alors que Q3.4 porte sur l'interruption avant chaque pas ;
  - T22 teste l'admissibilité par l'énergie, non le plafond ni la récupération (Q3.6) ;
  - T21 écarte expressément le profil de Q4.6.
- **Correction documentaire :** citer ces décisions dans les sources des scénarios concernés, ou écrire « aucun scénario dédié ».

**M-04 — « La surcharge ne réduit pas l'énergie » [DÉD] : énoncé plus affirmatif que ses sources.**
- **Endroit :** §5, l.259.
- **Preuve :**
  - ARB-D (R:124) applique la réduction au total de TU plafonné, puis écrit : « L'énergie est récupérée séparément » ;
  - Q3.14 (P1 l.259) ne vise que les TU ;
  - Q3.6 (P1 l.149) : la récupération d'énergie a sa propre règle, « Les valeurs seront fixées séparément » ;
  - le registre laisse ouvertes la « récupération et [le] plafond d'énergie » (R:141), et R:169 tient pour non décidé « tout paramètre non explicitement accepté » ;
  - OXCE ne réduit pas l'énergie selon la charge (`BattleUnit.cpp:2733-2742`, lu au commit figé). C'est cohérent, mais ce n'est pas une décision de Bastion.

  La conséquence certaine est plus étroite : la réduction prévue par ARB-D et Q3.14 ne porte que sur les TU.
- **Correction documentaire :** « ARB-D et Q3.14 n'appliquent la réduction de surcharge qu'aux TU ; aucun effet de la surcharge sur l'énergie n'est décidé [OUV] ».
- **Arbitrage :** il ne serait nécessaire que si le propriétaire veut faire de « aucun effet sur l'énergie » une règle.

**M-05 — Lecture de « non exécutable » dans Q4.21, marquée [DÉD].**
- **Endroit :** §6, l.299, et points ouverts, l.301.
- **Preuve :**
  - D:115 écrit « (coût réel supérieur, occupation ou obstacle inattendu) », sans dire à quoi le coût est supérieur ;
  - R:166 laisse le cas ouvert, « notamment en cas d'augmentation imprévue du coût » ;
  - deux lectures sont possibles : supérieur aux ressources restantes, ou supérieur au coût prévu ;
  - la v0.4.1 retient la première comme une déduction, alors qu'elle interprète un résumé [CIT] (RD-2). Elle ne crée pas de règle, puisque le cas d'un coût plus élevé mais payable reste [OUV]. Mais elle pourrait vider Q4.21 d'une partie de son sens.
- **Correction documentaire :** remplacer [DÉD] par « lecture non vérifiable (RD-2) ».
- **Arbitrage :** demander au propriétaire si Q4.21 arrête la marche sur tout coût réel supérieur au coût prévu.

**M-06 — Observation sur l'option B de Q1.4 : code [DÉD] impropre, comparaison à préciser.**
- **Endroit :** §0.1, l.58.
- **Preuve :**
  - [DÉD] est défini comme une « conséquence arithmétique ou logique de règles sourcées » (l.35). Or il s'agit ici d'une comparaison de textes ;
  - l'option B (« Espacement vertical constant. Tous les niveaux sont séparés par la même hauteur », P5 l.17) ne fixe ni la valeur ni l'interdiction de la configurer par carte. W-01 ajoute l'une et l'autre (P3 l.88).

  Le fond de l'observation est exact, et la v0.4.1 dit bien qu'elle ne vaut pas décision.
- **Correction documentaire :** la qualifier d'« observation documentaire, sans valeur de décision » et préciser : « principe commun : un espacement constant ; W-01 ajoute la valeur de 3 000 mm et l'interdiction de la configurer par carte ».

**M-07 — Une PNV placée dans la colonne « Précisée ou modifiée par ».**
- **Endroit :** §2, l.91 : « G1 | … | priorité « X puis Y » : PNV-7 ».
- **Preuve :** une PNV ne précise aucune règle (§0, l.36), mais la ligne peut se lire comme si PNV-7 précisait G1.
- **Correction documentaire :** écrire « — (priorité « X puis Y » non décidée : PNV-7) ».

**M-08 — PNV-4 : « tout le volume » est cité entre guillemets, mais ne figure pas dans la source.**
- **Endroit :** §3.5, l.166.
- **Preuve :** le script `citations.py` a contrôlé 147 citations. Celle-ci est la seule qui ne renvoie à aucun texte source. D:34 écrit « valide pour son volume horizontal », et la colonne « Formulation (v0.2) » paraphrase en « sous tout le volume horizontal ».
- **Correction documentaire :** citer D:34 mot pour mot.

**M-09 — T24 : « jamais deux unités conscientes sur une même case » ne tient pas compte de l'exception de G2.**
- **Endroit :** §13, T24 (l.506) ; §18, ligne W-14 (l.707).
- **Preuve :**
  - G2 : « Ce chevauchement de deux unités conscientes est une exception transitoire à S10 » (R:137 ; voir aussi R:80) ;
  - addendum Q5 : « L'exception transitoire au réveil prévue par G2 reste inchangée » (P2 l.92) ;
  - le §4 (l.212) le dit correctement, mais pas T24.
- **Correction documentaire :** ajouter « hors de l'exception transitoire de G2, absente du scénario ».

**M-10 — Q4.15 : citation attribuée au mauvais message.**
- **Endroit :** §4, l.209.
- **Preuve :**
  - le message B (P2 l.38) dit « Q5.2 ne crée donc aucune exception supplémentaire à S10 » : il parle de Q5.2 ;
  - la phrase sur Q4.15 est la « Rectification demandée » de l'addendum, au §B (P2 l.95).
- **Correction documentaire :** citer P2 l.95.

**M-11 — Q4.6 : « Ces chiffres sont identiques à ceux de l'option A de Q3.11 ».**
- **Endroit :** §5, l.245.
- **Preuve :** l'option A de Q3.11 (P1 l.201) ne contient que « Maximum 100 ; récupération 20 par tour », pour l'énergie. Les 60 / 60 TU n'y figurent pas.
- **Correction documentaire :** « Les valeurs d'énergie (100 et 20) sont identiques à celles de l'option A de Q3.11, écartée. »

**M-12 — RD-2 : « seules les valeurs de Q4.6 et Q4.7 sont confirmées ».**
- **Endroit :** §14, l.573.
- **Preuve :** le contenu de Q4.1 est confirmé par W-01 (P3 l.88). Le §12, l.442, marque d'ailleurs Q4.1 « [CIT] + [CONF] ».
- **Correction documentaire :** ajouter « et le contenu de Q4.1, par la confirmation W-01 ».

**M-13 — Statuts incohérents entre T45, d'une part, et T02 et T22, d'autre part.**
- **Endroit :** §13 : T45 (l.527) est classé « Pa (géométrie, PNV-6) » ; T02 (l.483) et T22 (l.504) sont classés « Sp ».
- **Preuve :**
  - les trois scénarios posent la même hypothèse : un passage « praticable » ;
  - T45 est une diagonale à plat. Les phases de PNV-6 (montée, descente) ne s'y appliquent pas, et le contrôle du volume de la diagonale est [INS] (l.168) ;
  - l'écart est hérité de la v1.4.1 : G1-02 et P0-09 y sont « partiels », P0-03 y est « spécifiable ».
- **Correction documentaire :** harmoniser les statuts, ou justifier l'écart. Par exemple : T45 « Sp sous hypothèse de praticabilité ; test intégré de la géométrie : Pa ».

**M-14 — Sort des cas de la v1.4.1 : trois imprécisions.**
- **Endroit :** §13, l.550, l.561 et l.567.
- **Preuve :** les 37 cas des tableaux du §5 de la v1.4.1 sont tous couverts (script `cas_v141.py`). Mais :
  - **P0-05 et P0-06.** Le résultat de P0-05 (v1.4.1 l.150 : sans surcharge, 7 + 15 plafonné à 20, résultat **20**) n'est un résultat attendu ni de T21 ni de T20. Celui de P0-06 (20 × 0,75 = 15, v1.4.1 l.151) correspond à T21 (a), et non à T20 ;
  - **G1-01.** Il est dit « repris », alors que la v1.4.1 écrit « fermés par terrain/murs » (l.169) et que T41 se limite aux « murs pleins ». C'est une adaptation ;
  - **§5.5 de la v1.4.1.** Les anciens tests du LOT-2F qu'il mentionne (T-M01 à T-M11, T-J, T-K, T-D) ne sont pas mentionnés, alors que la v0.4.1 écrit « Aucun cas exclu ».
- **Correction documentaire :**
  - « P0-05 → T21 (valeur intermédiaire), P0-06 → T21 (a) ; le résultat isolé de P0-05 n'est pas conservé » ;
  - « G1-01 : adapté (murs pleins seulement) » ;
  - « §5.5 : anciens tests du LOT-2F, non repris, renvoyés à la v1.4.1 ».

**M-15 — §11, ARB-D : « Concordance d'ordre et de troncature » mérite une nuance.**
- **Endroit :** §11, l.404.
- **Preuve :**
  - `BattleUnit.cpp:2714-2720` contient bien [code OXCE retiré — D4], c'est-à-dire [code OXCE retiré — D4] (l.1612-1615), puis [code OXCE retiré — D4] et [code OXCE retiré — D4]. L'ordre et la troncature concordent ;
  - mais OXCE tronque un produit en nombres flottants, alors que Bastion exige le plancher de la valeur exacte (§5, l.262) ;
  - une émulation en float32 (`float32_oxce.py`), et non une exécution d'OXCE, donne 454 triplets différents pour des Force, poids et TU de 1 à 120. Exemple : Force 1, poids 41, 41 TU donnent 0 en float32 et 1 en valeur exacte.

  Le §11 n'affirme d'ailleurs aucune fidélité (l.392).
- **Correction documentaire :** ajouter « troncature d'un produit flottant dans OXCE ; résultats non garantis identiques au plancher exact de Q3.14 ».

**M-16 — Copie P1, message 2 : reproduction partielle non déclarée.**
- **Endroit :** P1 l.3 et l.297-310 ; §15, pièce 1 (v0.4.1 l.611).
- **Preuve :**
  - P1 l.3 écrit : « Le texte est reproduit tel que reçu » ;
  - le message 31 se poursuit pourtant par une partie « Mission : » (six points de consignes), qui n'est pas reproduite. Elle ne contient ni proposition ni validation.
- **Correction documentaire :** au §15, pièce 1 : « message 2 : partie propositions et validation ; consignes de mission non reproduites ». La copie P1 elle-même n'est pas à modifier en silence.

**M-17 — §15 : outils de comparaison non inventoriés, et choix de ne pas modifier P1 non dit.**
- **Endroit :** §0.1, l.51 ; §15.
- **Preuve :**
  - le §0.1 s'appuie sur une comparaison avec le « message reçu dans la session ». Ni l'extraction du journal (`MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md`, `73f1fcd2…`) ni son script (`extract_user_msgs.py`, `206ca788…`) ne sont inventoriés ;
  - le point 1 du message I (P5 l.22) demandait de « compléter la copie de provenance ». L'auteur a ajouté P5, sans modifier P1 (empreinte inchangée, `c9ee67…`). Ce choix est bon, mais il n'est pas énoncé.
- **Correction documentaire :** inscrire ces deux fichiers au §15 comme outils de vérification ; écrire « P1 non modifiée ; complétée par P5 ».

**M-18 — Renvoi approximatif.**
- **Endroit :** §18, ligne W-08 (g) (l.693) : « P2 l.215 environ ».
- **Preuve :** la phrase « peuvent être exprimées en millimètres » figure en P2 l.217.
- **Correction documentaire :** « P2 l.217 ».

## 3. Contrôle des corrections W-01 à W-14

Source des anomalies : section 2 de P4. Consignes : P3, message H. Les numéros de ligne renvoient à la v0.4.1.

| Anomalie | Constat dans la v0.4.1 | État |
|---|---|---|
| **W-01** hauteur d'étage | §3.2, l.129-143 : chronologie en cinq étapes, identique à P3 l.93-97. La règle applicable (l.137) reprend W-01 (P3 l.88) et la consigne n° 2 (P3 l.15). B3-02 est cité sans modification (l.141). Q1.4 et Q1.8 restent dans l'historique (l.139-140 ; §12 l.416, 420). Voir aussi §3.1 l.114, §9.1 l.334, T27 et C-30 | **Corrigée** (sur [CONF]) ; réserve R-6 |
| **W-02** provenance des valeurs de Q1 | marqueur défini au §0 (l.39) ; présent aux §3.1, §3.6 (l.175, 176, 179), §9.1 (l.334, 343, 351), §12 et dans T26 | **Corrigée**, reliquat M-01 |
| **W-03** T21 | la phrase fausse a disparu (aucune occurrence de « jamais exercé ») ; les résultats 15, 17, 12 et 13 sont exacts | **Corrigée** ; explication absente de T21 (M-02) |
| **W-04** MEC-0002 | §9.1, l.330-361 : annotations et mentions « Ouvert » de GE-02 et de GE-03 ; ligne R:336 complète, y compris les points des §1 et §4 du rectificatif ; GE-05, CO-01 et règles de dégâts inchangées | **Corrigée** |
| **W-05** (a) copies P1 et P2 | §15, pièces 1 et 2, empreintes vérifiées | **Corrigé** |
| W-05 (b) Q1.1 à Q1.4 | le relecteur de la v0.3 proposait de les classer en « restitution ». Le propriétaire a écarté cette proposition (P3 l.105-118). Le reclassement en [TR] est fait au §0.1 | **Fait, conforme à P3 l.116** ; limites incomplètes (I-1) |
| W-05 (c) message A entier | P2, message A, est identique au message 24 du journal | **Corrigé** |
| W-05 (d) mandat et rapport de revue | P3, message G, et P4 sont inventoriés | **Corrigé** |
| **W-06** cas de test | T37 à T43 ; dépendance de G1-05 corrigée (T43, l.525 ; C-14, l.659) ; 37 cas sur 37 couverts | **Corrigée**, reliquat M-14 |
| **W-07** Q3.11 | l.244 : citation exacte de P1 l.203 ; lien avec Q4.6 à la l.245 | **Corrigée** |
| **W-08** (a) Q1.6 | l.109 | Corrigé |
| W-08 (b) Q3.2 | l.227 | Corrigé |
| W-08 (c) Q3.10 | l.191 | Corrigé |
| W-08 (d) Q3.5 | l.272 | Corrigé |
| W-08 (e) Q3.1 | l.226, marqué [DÉD] | Corrigé |
| W-08 (f) Q5.1 | l.289, « destination tactique admissible » | Corrigé |
| W-08 (g) millimètres | l.120 et l.334, « peuvent être exprimées » | Corrigé (renvoi : M-18) |
| W-08 (h) GE-02 et GE-03 | l.334, « modifiée » ; l.343, Q1.2 attribuée explicitement | Corrigé |
| W-08 (i) ARB-A et G1 | l.154-156, règle limitée à la diagonale | Corrigé |
| W-08 (j) Q4.7 | l.193 | Corrigé |
| W-08 (k) Q4.19 | l.321, « trois points » | Corrigé |
| W-08 (l) arithmétique | l.260-263, trois niveaux | Corrigé |
| W-08 (m) paragraphe de portée | l.228, citation exacte de P1 l.157 et 161 | Corrigé |
| **W-09** (a) PNV-2 | l.164 et l.360 : sourcée seulement par Q1.1 et Q2.6 ; non étendue à MEC-0002 | **Corrigé** ; réserve R-5 |
| W-09 (b) §3.6 et PNV-4 | l.180 | Corrigé |
| W-09 PNV-3, PNV-6, PNV-7 | l.165, 168 et 169 | Corrigé |
| **W-10** (a) T33 | l.515, sens ouvert | Corrigé |
| W-10 (b) T04 | l.485, bornes ouvertes | Corrigé |
| W-10 (c) T36 | l.518, Pa | Corrigé |
| W-10 (d) T30 | l.512, condition physique explicite | Corrigé |
| W-10 (e) T18 | l.500, option B retirée | Corrigé |
| **W-11** (a) renvois aux PNV | l.468 : T03, T04, T15, T26, T42, T43, T45 et T46 ; T25 retiré | Corrigé |
| W-11 (b) « aucun scénario dédié » | l.425, 430, 432 et 437 ; Q2.1 à Q2.3 rattachées à T40, qui les cite | **Corrigé pour les décisions citées** ; même défaut ailleurs (M-03) |
| W-11 (c) origines du journal | §16 : messages B et C distingués de R-Q5-1 à R-Q5-5 ; C-08 renvoie au point 5 du message B, exact (P2 l.48-50) | Corrigé ; les R-Q5-n et les numéros d'anomalie de la revue Q1–Q4 sont **non vérifiés** (pièces absentes) |
| W-11 (d) emplacement / case | l.590, sous « Occupation des connexions » | Corrigé |
| **W-12** rectificatif B3 | l.466 : pièce « proposition » (P2 l.209) et [CONF] séparée (P3 l.100-104) ; voir aussi l.34 et l.120 ; pas d'autorisation de modifier le dépôt | **Corrigée** |
| **W-13** (a) G4 et Q4.16 | l.402 : écart pour G4 seul ; l.403 : Q4.16 « non comparé » (LOT-2A §2, ligne 14 : « Départage des égalités : NV ») | Corrigé |
| W-13 (b) ARB-D | l.404 : `BattleUnit.cpp:2714-2720`, vérifié dans le code | **Corrigé** ; nuance M-15 |
| **W-14** (a) lectures [DÉD] | l.211-213 : conséquence tirée sur S10 | Corrigé ; formulation de T24 (M-09) ; attribution (M-10) |
| W-14 (b) transit partagé | l.217, [OUV] | Corrigé |

## 4. Provenance

### 4.1 Reclassement de Q1.1 à Q1.4 de [TR-A] en [TR]

- **La condition de P3 l.116 est remplie, au sens que le propriétaire lui donne.** L.116 subordonne le reclassement à la jonction des « textes complets ». L.108 décrit ces pièces : « les deux options A et B, puis la validation explicite de l'option A ». Le dossier contient désormais exactement cela :
  - les options A en P1 l.300-307 ;
  - les options B en P5 l.14-17 ;
  - la validation en P1 l.309.

  Le message I demande de reclasser « si la vérification est satisfaisante » (P5 l.24). **Le reclassement est justifié au regard du mandat.**
- **Les options citées sont exactes.** Le script `libelles_q1.py` retrouve les huit libellés à l'identique au §3.1 (l.104-107) et dans la reconstitution de P5 (l.45-48). La validation de P1 l.309 est exacte. Pour chaque décision, les deux options sont distinctes et s'excluent. La validation retient A pour les quatre.
- **Les limites du §0.1 sont justes :**
  - la transmission en deux messages ;
  - l'affirmation du propriétaire, invérifiable, selon laquelle les options B figuraient dans la conversation d'origine ;
  - le statut de copies ;
  - la forme réduite des pièces (titre et libellé seulement, alors que Q1.5 à Q1.9 ont des descriptions et une option recommandée) ;
  - le libellé au passé de Q1.4, présenté sans spéculation abusive.
- **Elles sont incomplètes** sur trois points (I-1) :
  - l'absence d'option B dans le message reçu le 19 novembre ;
  - le caractère seulement déclaré du nombre d'options ;
  - l'absence de qualification visible de [TR] au §12.
- **La remarque sur le libellé au passé de l'option A de Q1.4 (l.57) est exacte.** Elle est prudente (« ce n'est pas vérifiable »), et elle a raison de dire que la portée de Q1.4 pour la hauteur d'étage n'en dépend pas. Elle laisse implicite ce qui reste de Q1.4 hors de la hauteur d'étage : voir R-7.

### 4.2 Fidélité des copies

Comparaison mécanique (`compare_copies.py`, code 0), après réextraction du journal (`extract_user_msgs.py`, code 0, sortie identique au fichier fourni : SHA-256 `73f1fcd2…`).

| Copie | Message du journal | Horodatage (UTC) | Résultat |
|---|---|---|---|
| P1, message 1 | 30 | 2026-11-19T20:36:22.283Z | identique (12 962 caractères) |
| P1, message 2 | 31 | 2026-11-19T20:54:21.612Z | identique au début du message (1 066 caractères sur 2 023). La partie « Mission » n'est pas reproduite (M-16). **Le message ne contient aucune option B** |
| P2, messages A à E | 24 à 28 | 2026-11-19, de 19:56:49Z à 20:13:09Z | identiques |
| P3, messages F, G et H | 32, 33 et 34 | 2026-11-19T20:59:24Z, 2026-11-19T21:08:57Z, 2026-11-20T12:53:14Z | identiques |
| P5, message I | 35 | 2026-11-20T13:41:45.327Z | identique (1 864 caractères) |
| P5, reconstitution (l.39-48) | — | — | conforme à P1 et à P5 l.14-17 ; aucun texte ajouté |
| P4 (rapport de la revue de la v0.3) | ce n'est pas un message du propriétaire | — | **non vérifié** : hors des sources admises |
| v0.4 (pièce 12) | message de l'auteur | 2026-11-20T13:05:12.403Z | le fichier reproduit à l'identique le texte remis (70 717 caractères). Le message ajoutait ensuite un post-scriptum, non repris |

### 4.3 Niveaux de preuve

| Décisions | Code | Pièces et lignes contrôlées | Avis |
|---|---|---|---|
| S1 à S12, Z1, N1 à N14, ARB-A à ARB-E, G1 à G4, PE, GE, CH, ES, EN, CO | [INS] | R:71-147, R:196-198, R:203-208, R:242-265, R:286-287, R:310, R:336 | justifié ; tous les numéros de ligne cités sont exacts |
| Q1.1 à Q1.4 | [TR] | P1 l.300-309 ; P5 l.14-17 | justifié par le mandat ; I-1 |
| Q1.5 à Q3.14 | [TR] | P1 l.11-293 (message 30) | justifié ; lignes exactes. Les citations ne diffèrent de la source que par la majuscule initiale, l'espacement autour de « × » et le retrait de la mention « (recommandé) » |
| Q4.1 à Q4.21 | [CIT] | validations : v0.2 l.181-191 ; résumés : D:86-115 | justifié ; Q4.1 est aussi [CONF] (M-12) |
| valeurs de Q4.6 et Q4.7 | [DÉC] | P2 l.18 | justifié |
| Q5.1 et Q5.2 | [DÉC] | P2 l.28-38 et l.70-95 | justifié ; attribution à corriger (M-10) |
| B3 | [DÉC] | P2 l.121-201 ; validation en P2 l.125 | justifié |
| Rectificatif B3 | « proposition » et [CONF] | P2 l.209 ; P3 l.100-104 | justifié |
| Confirmation W-01 | [CONF] | P3 l.86-99 | justifié |
| ⟨B3-03⟩ | marqueur | P2 l.169 ; rectificatif, P2 l.237 | justifié ; reliquat M-01 |

### 4.4 Dates et horodatages

| Date citée | Vérification |
|---|---|
| 20 novembre 2026 : [CONF] (l.34), message I (l.46, l.612), rectificatif validé (l.334), remise de la v0.4 (l.623) | **vérifiées** par le journal : 12:53:14Z, 13:41:45Z, 12:53:14Z et 13:05:12Z |
| 19 novembre 2026 : addendum B3 validé (l.334) ; mandat de la revue Q1–Q4 (l.633) | **vérifiées** : P2 l.125 ; message 22 du journal, 16:25:44Z |
| 17 novembre, rapport d'inscription (l.401, l.619) | **vérifiée** : « Date : 17 novembre 2026 (UTC) » ; commit `b20d5aca` du 17 novembre |
| 18 novembre, rapport d'archivage (l.622) | **vérifiée** : « Date d'exécution : 18 novembre 2026 » ; commit `1ecc608`, 2026-11-18 03:55 +0100 ; fusion par la PR n° 15 |
| 19 novembre, rapports de Claude Code (l.634) | **non vérifiée** : ce sont des messages de l'auteur, hors des sources admises |

Je n'ai trouvé **aucune date inventée**. La v0.4.1 ne reprend pas les repères horaires du message A (P2 l.12-14).

## 5. PNV et scénarios

### 5.1 Les neuf formulations PNV (§3.5)

| PNV | Formulation d'origine | Statut dans la v0.4.1 | Avis |
|---|---|---|---|
| PNV-1 | D:29 | positions : [INS] (N3, GE-01 : R:93, R:202) ; le reste : [PNV] | exact |
| PNV-2 | D:30 | largeur et enveloppes : [TR] (Q1.1, Q2.6) ; le reste, y compris la conversion : [PNV] ; non étendue à MEC-0002 | exact ; réserve R-5 |
| PNV-3 | D:32 | orientation à 45° lors d'un pas diagonal : [DÉD] (S1, Q4.17) ; liste fermée et orientation couchée : [PNV] | exact ; la déduction est valable |
| PNV-4 | D:34 | positions stables horizontales : [TR] (Q2.1, Q2.2, P1 l.73 et 79 ; Q4.19, D:113) ; le reste : [PNV] | exact ; citation à corriger (M-08) |
| PNV-5 | D:35 | absence de changement de niveau implicite : [INS] (R:123) ; refus et absence de chute : [PNV] ; bornes : [OUV] | exact |
| PNV-6 | D:36 | volume de la diagonale : [INS] (R:128) ; phases et méthode pour les autres pas : [PNV] | exact |
| PNV-7 | D:37 | [PNV] ; renvoi de Q4.16 (D:110) « sans objet » | exact : aucune règle « X puis Y » dans P1 ni dans P5 (`grep`, code 1) |
| PNV-8 | D:39 | ordre des voisins et absence de nouvelle recherche : [CIT] (D:113) ; ordre des réveils simultanés : [PNV] | exact ; Q3.5 vise bien les événements « sur le trajet » (P1 l.141) |
| PNV-9 | D:40 | cas énumérés : sourcés ; exigence générale : [PNV] | exact |

- **Une PNV est-elle employée comme règle ailleurs ?** Non, à une formulation près : la colonne « Précisée ou modifiée par » du §2 (M-07). Les dépendances à PNV-3 et à PNV-4 sont déclarées aux §3.6 (l.176-177, 180) et dans T26.
- **Une PNV intervient-elle dans un scénario « Sp » ?** Non. Je l'ai contrôlé deux fois :
  - mécaniquement, avec `matrice_scenarios.py` ;
  - par examen des scénarios « Sp » qui comportent une diagonale (T02, T05, T22) : leur coût ne dépend ni du passage emprunté (PNV-7) ni des phases (PNV-6).

### 5.2 Scénarios T01 à T46

**Calculs** (`calculs_relecteur.py`, arithmétique exacte avec `Fraction`, code 0, « TOUS_OK = True ») :
- barème du §5 ; T01, T02 (y compris 4 d'énergie selon la loi d'OXCE) ;
- T05 : énumération des chemins de 1 à 4 pas ; seuls [NE, E] et [E, NE] sont ex aequo à 10 TU et 5 d'énergie ; [NE, E] est retenu ;
- T11a, T18 (l'option B donnerait 27/4, sans arrondi fixé), T19 ;
- T20 (22 × 15/22 = 15 en valeur exacte, 14,999999999999998 en flottant) ;
- T21 (15, 17, 12 et 13 ; 40/3 avant arrondi) ; W-03 (min(s + 60, 60) = 60 pour s de 0 à 60) ;
- T22 (2 d'énergie : aucun chemin ; 3 d'énergie : la diagonale seule ; tout chemin commence par un pas coûtant au moins 3 d'énergie) ;
- T23, T37, T39, T43, T44, T45 ;
- T26 et §3.6, avec des encadrements exacts par les carrés :
  - largeur intérieure : 1 400 mm ;
  - 600√2 dans ]848, 850], donc 850 mm ;
  - 1 800/√2 dans ]1 272, 1 274], donc 1 274 mm ;
  - étendue maximale du profil couché : √(1 200² + 600²) = 1 341,64 mm, vers 26,57°, inférieure à 1 400 mm ;
  - rapport case / étage : 1/2 ;
- §11 : les coûts initiaux coïncident avec ⌊TU/2⌋, sauf la diagonale difficile (5 contre 4).

Le script de l'auteur (`verif-v04/calculs.py`), que j'ai lu puis exécuté, donne les mêmes valeurs (code 0).

**Statuts :**
Les 47 lignes de T01 à T46 (T11 est scindé en T11a et T11b) se répartissent ainsi :
- 27 sont « Sp », parfois sous condition : T01, T02, T05 à T09, T14, T16 à T23, T25, T27, T30, T32, T35, T37 à T41 et T44. Les qualifications « Sp (formulation résumée) », « Sp en principe » et « Sp pour la comptabilité » sont explicites ;
- 18 sont « Pa » : T03, T04, T10, T11b, T12, T13, T15, T24, T26, T28, T29, T31, T33, T36, T42, T43, T45 et T46 ;
- T34 est « Ou » ;
- T11a est mixte : (a) et (b) sont « Sp », (c) est « Pa ».

Les dépendances déclarées sont justes, à une incohérence près (M-13). Les rattachements à la matrice sont à reprendre (M-03).

**Cas de la v1.4.1 :**
- 37 sur 37 couverts ;
- les sept cas du mandat (P0-10, E-04, E-05, C-02, G1-01, G1-04 et G1-05) sont repris dans T37 à T43, avec les bons résultats ;
- trois imprécisions de sort (M-14).

## 6. Réserves restantes (même si toutes les anomalies sont corrigées)

- **R-1 — Authenticité et archivage.** Toutes les pièces P1 à P5 sont des copies, non authentifiées de façon indépendante et non archivées (RD-1, RD-6). La réserve ⟨B3-03⟩ demeure jusqu'à l'archivage des validations d'origine de Q1.
- **R-2 — Q1.1 à Q1.4.** La proposition est restituée en deux messages, et la conversation d'origine est inaccessible. L'existence des options B dans cette conversation, et celle de deux options seulement, reposent sur la déclaration du propriétaire.
- **R-3 — Q4.** Les formulations sont des résumés de l'orchestrateur (RD-2). C'est de là que dépendent PNV-7, PNV-8 et la lecture de Q4.21 (M-05).
- **R-4 — Q5.1, Q5.2 et B3.** Les textes des options d'origine sont absents (RD-3).
- **R-5 — PNV-2.** Le rectificatif B3, validé par W-12, parle de « La contrainte Q1 des millimètres entiers » (P2 l.219). Les pièces Q1 ne la formulent que pour la largeur des cases. Que cette phrase étende ou non la contrainte à toutes les données géométriques n'est pas tranché. **Point à soumettre au propriétaire**, comme le demandait déjà P4.
- **R-6 — Portée de W-01.** W-01 dit « non configurable par carte » (P3 l.88). La v0.4.1 en conclut que la phrase de B3-02 sur les « constantes universelles » ne s'applique pas à la hauteur d'étage (l.141). Cette conclusion est fondée sur P3 l.90 (« Corriger les formulations contradictoires de B3-02 »). Mais W-01 ne dit pas expressément si la hauteur peut être configurée à un autre niveau que la carte, par exemple globalement.
- **R-7 — Q1.4 hors hauteur d'étage.** Q1.4 n'est historique « que » pour la hauteur d'étage (§12, l.416). Ce qui en subsiste ailleurs, par exemple pour l'altitude du premier niveau, n'est pas dit. Le rattachement d'une case à un étage reste [OUV].
- **R-8 — GE-03 et Q1.2.** L'annotation de GE-03 proposée au §9.1 ajoute Q1.2, que B3-03 ne reprend pas. Le propriétaire a demandé cette attribution explicite (P3 l.163). Mais il avait aussi demandé de ne pas considérer que Q1 modifie automatiquement GE-03 (P2 l.42). **À confirmer lors du futur mandat d'inscription.**
- **R-9 — Points ouverts déclarés.** Ils sont nombreux et correctement marqués [OUV] (§14). Ils ne sont pas des défauts, mais ils limitent le nombre de scénarios « Sp ».
- **R-10 — Limites de ma revue.**
  - La fidélité de P4 au rapport d'origine n'est pas vérifiée.
  - Le code d'OXCE a été lu, ni compilé ni exécuté. L'émulation en float32 n'est pas une exécution.
  - Aucun scénario n'a été exécuté comme test.
- **R-11 — Statut.** MEC-0001 et MEC-0002 restent reportées. Aucune inscription n'est autorisée.

## 7. Vérifications effectuées

### 7.1 Commandes et codes de sortie

Scripts et sorties dans `D/revue-v041-relecteur/`. Python a toujours été lancé avec `python3 -I`.

| # | Commande | Code | Résultat |
|---|---|---|---|
| 1 | `sha256sum` sur les douze pièces du mandat | 0 | douze empreintes identiques aux déclarations |
| 2 | `git -C bastion show origin/main:<chemin> \| sha256sum`, pour sept fichiers ; `git rev-parse origin/main` | 0 | `818c646c…` ; registre `9117d20c…`, et pièces 8 à 11 du §15 identiques ; `git log` : `1ecc608` (18 novembre), PR n° 15 |
| 3 | `python3 -I extract_user_msgs.py <journal> messages-reextraits.md` ; `sha256sum` ; `diff` | 0 ; 0 ; 0 | 35 messages ; fichier identique (`73f1fcd2…`) |
| 4 | `compare_copies.py` | 0 | P1, P2, P3 et P5 fidèles (§4.2) |
| 5 | `diff -u v0.4 v0.4.1 > mon-diff.patch`, puis `cmp` avec le patch fourni (en-têtes exclus) | 1 (attendu : il y a des différences) ; `cmp` : 0 | patch identique ; 16 blocs, tous couverts par V-01 à V-12 |
| 6 | `grep` de `TR-A`, de « v0.4 » et de RD-1 dans les v0.3, v0.4 et v0.4.1 | 0 | [TR-A] seulement aux l.31, 52, 672 et 716-721 ; « 9 à 12 » était faux dans la v0.4 ; « 7 à 11 » est exact |
| 7 | `v04_vs_journal.py` | 0 | fichier v0.4 = texte remis (13:05:12Z), sans le post-scriptum |
| 8 | `libelles_q1.py` | 0 | huit libellés présents à l'identique ; validation exacte |
| 9 | `citations.py` (147 citations « … ») | 0 | 138 retrouvées dans les sources, 8 renvoient au texte même de la v0.4 ou de la v0.4.1, **1 introuvable** (M-08) |
| 10 | `matrice_scenarios.py` | 0 | **10 rattachements non cités** (M-03) ; aucune PNV dans un scénario « Sp » |
| 11 | `cas_v141.py` | 0 | 37 cas sur 37 couverts ; §5.5 non mentionné (M-14) |
| 12 | `calculs_relecteur.py` | 0 | tous les calculs retrouvés |
| 13 | `python3 -I verif-v04/calculs.py` (script de l'auteur, lu avant exécution) | 0 | mêmes valeurs |
| 14 | `git -C oxce rev-parse HEAD` ; `git show HEAD:src/Savegame/BattleUnit.cpp` (l.1612-1615, 2700-2760) ; `git show HEAD:src/Battlescape/UnitWalkBState.cpp` (l.330-358) | 0 | commit `441cae1b…` ; renvois du §11 exacts |
| 15 | `float32_oxce.py` (émulation, non-exécution d'OXCE) | 0 | 454 divergences entre float32 et valeur exacte pour des valeurs de 1 à 120 (M-15) |
| 16 | `grep` du marqueur ⟨B3-03⟩ sur les valeurs tirées de Q1 | 0 | absent aux l.177, 178, 180, 337 et 485 (M-01) |

**Écart de procédure, signalé par transparence.** Sur le clone OXCE, j'ai aussi lancé `git status --porcelain` (sortie vide), `git grep` et `git describe`. Ces commandes ne figurent pas dans la liste autorisée.
- `.git/index` n'a pas été modifié : sa date de modification est restée le 2026-11-17 à 15:37:31Z.
- La date de modification du répertoire `.git` est en revanche passée au 2026-11-20 à 14:01:59Z. C'est ce que laisse un fichier de verrou temporaire, que `git status` crée puis supprime.
- Aucun contenu n'a été modifié.

Sur le dépôt Bastion, je n'ai utilisé que `show`, `log` et `rev-parse`.

### 7.2 Classement des constats

**Exécuté et réussi :**
- empreintes des pièces et du dépôt ;
- réextraction du journal ;
- fidélité de P1, P2, P3 et P5 ;
- identité entre le diff et le patch fourni, et correspondance avec le §19 ;
- correction de RD-1 ;
- conformité du fichier v0.4 au texte remis ;
- huit libellés de Q1.1 à Q1.4 ;
- 138 citations ;
- tous les calculs des scénarios et du §3.6 ;
- couverture des 37 cas de la v1.4.1 ;
- absence de PNV dans les scénarios « Sp » ;
- commit OXCE ;
- script de l'auteur (code 0).

**Exécuté et échoué** (le contrôle a tourné et la condition attendue n'est pas remplie) :
- une citation sans source (M-08) ;
- dix rattachements de la matrice non cités par leur scénario (M-03) ;
- cinq valeurs de Q1 sans marqueur ⟨B3-03⟩ (M-01) ;
- résultat isolé de P0-05 non conservé (M-14).

**Inspecté seulement :**
- substance des corrections W-01 à W-14 ;
- statuts et sources des neuf PNV ;
- qualification [DÉD] (M-04, M-05, M-06) ;
- textes proposés au §9 ;
- numéros de ligne du registre, du LOT-2A et de la v0.2 ;
- lignes du code d'OXCE (lues, non compilées) ;
- dates des rapports du dépôt ;
- renvois internes des §0 à §19.

**Non vérifié :**
- authenticité des messages d'origine du propriétaire et de la conversation de conception ;
- présence des options B dans cette conversation ;
- fidélité de P4 au rapport d'origine ;
- origines R-Q5-1 à R-Q5-5 et numéros d'anomalie de la revue Q1–Q4, au §16 ;
- rapports de Claude Code du 19 novembre (pièce 15) ;
- comportement d'OXCE à l'exécution ;
- exécution des scénarios comme tests ;
- exécutions que l'auteur déclare au §17, hormis le script `calculs.py`, que j'ai relancé.

### 7.3 Fichiers produits (tous dans `D/revue-v041-relecteur/`)

- `RAPPORT-REVUE-INDEPENDANTE-v0.4.1.md` : le présent rapport ;
- scripts : `compare_copies.py`, `v04_vs_journal.py`, `libelles_q1.py`, `citations.py`, `matrice_scenarios.py`, `cas_v141.py`, `calculs_relecteur.py`, `float32_oxce.py` ;
- extraits et sorties : `messages-reextraits.md`, `diff-messages.txt`, `mon-diff.patch`, `a.tmp`, `b.tmp`, `registre.md`, `v141.md`, `lot2a.md`, `sortie-calculs-auteur.txt`.

Aucun autre fichier n'a été créé, modifié ni supprimé. Aucune décision de gameplay n'est prise ici : les points R-5 à R-8, M-04 et M-05 relèvent du propriétaire.
