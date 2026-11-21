# Rapport de revue indépendante de la v0.3, et observations complémentaires

Partie 1 : copie, par Claude Code, du rapport rendu par le relecteur indépendant (agent distinct de celui qui a préparé la v0.3), sans correction. Partie 2 : extrait des observations complémentaires ajoutées par Claude Code en transmettant ce rapport au propriétaire. Ni l'une ni l'autre n'est archivée dans le dépôt.

---

## Partie 1 — Rapport du relecteur

# Revue indépendante de la v0.3 de la consolidation MEC-0001 (Q1 à Q5 et B3)

Revue faite en lecture seule. Je n'ai rien modifié, dans le dépôt comme dans les documents relus.

## 1. Verdict : conforme sous réserves

**Ce qui est conforme :**
- Les 29 décisions Q1–Q3 sont restituées fidèlement en substance, par rapport aux copies transmises.
- Les 21 décisions Q4 sont fidèles aux résumés de la v0.2, qui sont leur seule source.
- Q5.1 et Q5.2 sont fidèles.
- Tous les renvois `R:NN` (registre sur `main`) et `D:NN` (lignes de la v0.2) que j'ai contrôlés sont exacts.
- Les empreintes des documents sont conformes.
- J'ai recalculé en arithmétique exacte toutes les valeurs du §5 et des scénarios T01 à T36 : elles sont justes.
- Les neuf formulations PNV sont bien isolées. Aucune n'est utilisée dans un scénario « Sp » ni dans le §9 comme une règle acceptée, sous une réserve (W-09).

**Ce qui empêche le verdict « conforme » :**
- **Une ambiguïté tranchée sans le propriétaire.** La hauteur d'étage a été retirée des valeurs configurables de B3-02 (W-01). Cela bloque l'inscription de GE-02.
- **Une clause de provenance omise.** La mention « provenance non vérifiée » que B3 impose sur les valeurs de Q1 a disparu (W-02).
- **Une explication de test fausse** dans T21 (W-03).
- **Des textes incomplets :** les modifications prévues dans MEC-0002 (W-04) et la liste des pièces à archiver (W-05).
- **Une couverture de tests réduite sans le dire** (W-06).

Enfin, le message C, §E, subordonne un verdict « pleinement conforme » à la vérification des preuves de validation. Je ne peux pas la faire sur des copies.

**Synthèse des neuf contrôles prioritaires :**

| # | Résultat |
|---|---|
| 1 | Les 29 décisions sont présentes et fidèles en substance. Écarts de rédaction en W-07 et W-08. Pour Q1.1 à Q1.4, la preuve est plus faible que ce qu'annonce le code [TR] (W-05). |
| 2 | Chronologie exacte : GE-02 inscrit (principes acceptés le 14 novembre), puis Q1.4 et Q1.8 vers 14 h 26–14 h 29 UTC le 19 novembre, puis Q4.1. L'écart réel entre Q1.4 et GE-02 est bien signalé. En revanche, la lecture « hauteur non configurable » n'est pas établie (W-01). |
| 3 | Q4 : conforme aux résumés, avec la bonne réserve RD-2. Q5.1 et Q5.2 : fidèles, sauf l'omission de « admissible » (W-08). B3 : écarts W-01, W-02 et W-12. |
| 4 | Correct, sauf W-09 (a) et (b). |
| 5 | Cohérent, avec deux lacunes (W-14). |
| 6 | Toutes les formules et tous les résultats sont exacts. Une explication est fausse (W-03), des choix non sourcés figurent dans des attendus (W-10), la couverture est incomplète (W-06). |
| 7 | GE-02 : W-01, W-02 et W-04. GE-03 : W-04 et W-08 (h). Ligne « Géométrie » (R:336) : W-04. |
| 8 | Les corrections C-01 à C-31 sont présentes dans le texte, sauf C-19 (partielle, W-04) et C-30 (contestée, W-01). Numéros d'origine à revoir (W-11). §15 incomplet (W-05). |
| 9 | Voir ci-dessous. |

**Distinction demandée au contrôle 9 :**
- **Contradictions réelles :**
  - Q1.4 contre GE-02. Elle est historique, résolue par Q4.1 et correctement signalée.
  - La tension interne à B3-02, qui n'est pas tranchée (W-01).
- **Anomalies documentaires :** tout le reste.
- **Paramètres reportés :** ils sont correctement déclarés [OUV]. Trois seulement sont tranchés en douce :
  - la hauteur d'étage (W-01) ;
  - le sens du départage par identifiant de connexion (T33) ;
  - l'inclusion des bornes des seuils de ressaut (T04).

## 2. Anomalies

Abréviations utilisées ci-dessous :
- **P1** : `PIECES-Q1-Q3-TRANSMISES.md` ;
- **P2** : `PIECES-Q4-Q5-B3-DECLARATIONS.md` ;
- « l. » : numéro de ligne du fichier concerné.

### Bloquant

**W-01 — Hauteur d'étage retirée de B3-02 (correction C-30).** Bloquant pour l'inscription de GE-02 et pour la « règle applicable » du §3.2.
- **Nature :** anomalie de fidélité sur un point décisionnel. Elle révèle une tension réelle entre des sources du propriétaire.
- **Ce que dit la v0.3 :**
  - §3.2, l.107 : « Elle ne figure donc pas parmi les valeurs configurables de B3-02 (correction C-30) » ;
  - §3.1, l.88 : « valeurs initiales configurables, sauf la hauteur d'étage » ;
  - §9, ligne GE-02 (l.280) : « case de 1 500 mm et mur de 100 mm en valeurs initiales. La hauteur de 3 m reste fixe ».
- **Ce que disent les sources :**
  - B3-02 (P2, l.143-151) range « hauteur entre sols de référence de deux étages consécutifs : 3 000 mm » parmi les « valeurs initiales prévues ». Il ajoute : « Ces valeurs ne sont pas des constantes universelles. Le moteur doit pouvoir utiliser d'autres configurations admissibles. » Puis : « La hauteur d'étage de 3 000 mm demeure la règle explicitement validée par Q4.1. »
  - Le paragraphe de portée de Q1.5 à Q1.9 (P1, l.55) : « Les autres … cartes pourront utiliser des paramètres différents. »
  - Le mot « fixes » de GE-02 (R:203) traduit A3A, « qui fixe en mètres la seule hauteur d'étage ». Le constat X13 de `LOT-2I-CONSOLIDATION-MEC-0002.md` le confirme : « Seule la hauteur d'étage reçoit une valeur métrique ».
  - SA-19 (R:231) raisonne en « quart d'étage, soit 0,75 m avec 3 m par étage ».
  - Q4.1 n'est connue que par un résumé (RD-2).
- **Mécanisme :** deux lectures sont possibles :
  - (a) 3 000 mm est une constante ;
  - (b) l'écart est uniforme entre étages consécutifs (c'est la rectification de Q1.4), mais reste une valeur initiale configurable.

  La v0.3 retient la lecture (a). Elle décrit B3-02 de façon inexacte et en retire un élément sous le nom de « correction », sans décision du propriétaire. Or CLAUDE.md §1 dit : en cas d'ambiguïté, s'arrêter et demander.
- **Correction minimale :**
  - reproduire B3-02 tel quel aux §3.1, §3.2 et §9 ;
  - requalifier C-30 en question ouverte ;
  - ajouter au §14 la question : « la hauteur de 3 000 mm est-elle une constante, ou une valeur initiale configurable, uniforme entre étages consécutifs ? » ;
  - en attendant, n'énoncer que ce qui est commun aux deux lectures : 3 000 mm uniformes entre les sols de référence de deux étages tactiques consécutifs, distincts des dénivelés locaux ;
  - ne pas inscrire GE-02 avant la réponse du propriétaire.

### Importants

**W-02 — Clause de provenance de B3 omise.**
- **Ce qu'exigent les sources :**
  - B3-03 (P2, l.169) : « Ces valeurs Q1 doivent conserver une mention de provenance non vérifiée jusqu'à l'archivage de leur validation originale » ;
  - B3-02 (l.143) : « Sous réserve de confirmation documentaire des décisions Q1 » ;
  - rectificatif, §3 (l.237 et 239) : « provenance non vérifiée » jusqu'à l'obtention des messages d'origine, puis « Sous réserve de leur confirmation ».
- **Ce que fait la v0.3 :**
  - aucune occurrence de « non vérifiée » ni de « sous réserve » (`grep`, code 1) ;
  - la ligne prévue pour R:336 (l.290) affirme « les valeurs initiales sont sourcées (Q1) » ;
  - le rapport case/étage de 0,5 (§3.6) est donné sans réserve.
- **Mécanisme :** la transmission des copies peut satisfaire la condition du rectificatif (« obtention »), mais pas celle de B3-03 (« archivage »). La v0.3 lève donc la réserve d'elle-même. RD-1 ne la remplace pas : il vise l'inscription, pas la mention portée sur les valeurs.
- **Correction :** porter la mention « provenance à confirmer par archivage (B3-03) » sur les valeurs Q1 aux §3.1, §3.6, §9 (GE-02, GE-03, R:336) et §12. À défaut, faire constater par le propriétaire que la transmission lève la réserve.

**W-03 — T21 : remarque fausse.**
- **Ce que dit la v0.3 (l.411) :** « Avec le profil Q4.6 (60 récupérées sur 60), le plafond n'est jamais exercé ».
- **Calcul :** pour un solde de 0, 1, 10, 59 et 60, solde + 60 vaut 60, 61, 70, 119 et 120. Le minimum avec 60 donne toujours 60.
- **Mécanisme :** le plafond d'ARB-D joue dès que le solde est positif. Les TU disponibles valent toujours 60 avant surcharge. La phrase dit l'inverse, et pourrait faire écrire un test sans plafond. Les quatre résultats de T21 (15, 17, 12 et 13) sont exacts.
- **Correction :** « le plafond s'applique dès que le solde est positif : les TU disponibles valent toujours 60 avant surcharge, ce qui ne distingue pas ARB-D d'une remise au maximum ; d'où le maximum fictif de 20 ».

**W-04 — Modifications de MEC-0002 incomplètes (C-19 annoncée, non faite).**
- **Ce qu'annonce le journal :** C-19 (l.504) dit « points ouverts de GE-02, GE-03 et R:336 actualisés, §9 ».
- **Ce que fait réellement le §9 :**
  - rien sur la mention « Ouvert : largeur de case, volumes, rapport case/étage » de GE-02 (R:203) ;
  - rien sur la mention « Ouvert : dimensions par type et posture » de GE-03 (R:204) ;
  - seule la ligne R:336 est actualisée.
- **Ce qui manque dans la nouvelle ligne R:336 :**
  - le rectificatif, §1 (l.221) : « La précision et les arrondis des trajectoires, vitesses, hauteurs équivalentes et autres calculs physiques restent à qualifier » ;
  - le rectificatif, §4 : dimensions minimales, tolérances, conventions d'arrondi.

  La v0.3 les déclare bien [OUV] aux §3.1 et §14, mais pas dans le texte destiné à R:336.
- **Conséquence :** inscrite telle quelle, GE-02 donnerait « case de 1 500 mm » tout en gardant « Ouvert : largeur de case ». Or le rectificatif, §3, demande que GE-02 et GE-03 soient « annotées pour rendre explicite cette évolution ».
- **Correction :** rédiger au §9 le nouveau texte des mentions « Ouvert » de GE-02 et GE-03, et compléter la ligne R:336.

**W-05 — Liste des pièces à archiver (§15) incomplète ; classement de Q1.1 à Q1.4.**
- (a) Les deux copies de travail ne sont pas listées : P1 (SHA-256 `c9ee67…`) et P2 (`b69ba3…`). Ce sont pourtant les seules formes disponibles des textes [TR] et [DÉC].
- (b) L'item 1 (l.460) parle du « texte des options retenues ». Or le message 2 (P1, l.299-310) est une restitution postérieure :
  - les options sont reformulées au passé (« les étages pouvaient initialement être séparés ») ;
  - la validation est citée (« Ma validation originale était : « … » »).

  Ce n'est donc pas la proposition d'origine que suppose le code [TR] du §0. RD-5 ne signale que l'absence des options écartées.
- (c) L'item 9 ne cite du message A que la phrase sur Q4.6 et Q4.7. Le message porte aussi les repères horaires et la consigne « Ne transforme pas ces informations en preuve indépendante » (P2, l.12-17).
- (d) Le mandat et le rapport de la présente revue manquent dans la partie D.
- **Correction :** ajouter (a) et (d) ; archiver le message A en entier ; requalifier Q1.1 à Q1.4 en « restitution par le propriétaire de l'option retenue, avec citation de la validation d'origine » (§0, §3.1, §12, RD-5, §15).
- L'item 8 est vérifié : la v1.4.1 est sur `main` (commit `1ecc608`), avec la même empreinte `b7874c48…` que celle que cite R:115.

**W-06 — Cas de test pertinents non repris.**
- **Ce que dit la v0.3 (§13, l.428) :** « Ses cas encore pertinents sont repris ici. Son contre-exemple G1-05 dépend de PNV-7. »
- **Pourquoi c'est faux pour G1-05 :** ce cas de la v1.4.1 a « un passage fermé, l'autre ouvert ». La priorité X puis Y (PNV-7) y est donc sans objet. G1-05 dépend de la géométrie (PNV-6), comme T03. Or la v1.4.1, §5.5, juge G1-03 et G1-05 « nécessaires ensemble » pour distinguer le contrôle topologique (S4, N2) du contrôle physique (G1, R:129).
- **Autres cas de la v1.4.1 absents de T01 à T36 :**
  - P0-10 : le second critère de G4 (à TU égales, moins d'énergie) n'est jamais testé ;
  - E-04 : un pivot sans tir n'interrompt pas la marche (ARB-E, Q5.1) ;
  - E-05 : plusieurs réactions, un seul débit (Q5.1) ;
  - C-02 : aucun changement de niveau implicite (ARB-C, Q2.1 à Q2.3) ;
  - G1-01 : deux passages fermés (N2) ;
  - G1-04 : terrain jamais exploré (S7).
- **Correction :** reprendre ces cas (G1-05 en statut Pa, pour la géométrie) ou retirer l'affirmation et les lister comme non repris. Corriger la dépendance de G1-05, ici et dans C-14.

### Mineurs

**W-07 — Q3.11 durcie.**
- La v0.3 (§5, l.200) écrit « sans valeur fixée à ce stade ».
- La pièce (P1, l.201-203) dit : option B « Valeurs à déterminer après calibration », « sans valeurs définitives avant les essais de rythme de jeu ».
- La rédaction de la v0.3 crée une contradiction apparente avec les valeurs de test de Q4.6. Le texte d'origine n'en crée pas : une valeur de test n'est pas une valeur définitive.
- **Correction :** reprendre la formule d'origine.

**W-08 — Autres écarts de rédaction dans des énoncés codés.** Les points (f) à (i) changent la portée de l'énoncé.
- (a) Q1.6 : « volumes de collision proposés, pas des dimensions anatomiques exactes » (P1, l.23) devient « pas des dimensions anatomiques ».
- (b) Q3.2 : « configurable » est omis.
- (c) Q3.10 : « pour l'instant » est omis.
- (d) Q3.5 (§6) : « sur le trajet » est omis, alors que PNV-8 en tire argument.
- (e) Q3.1 : « celui de la case d'arrivée (S2) » est inséré dans l'énoncé [TR]. C'est une lecture, cohérente avec R:152, à marquer [DÉD].
- (f) Q5.1 : « la destination tactique admissible du pas » (P2, l.75) devient « la destination du pas ».
- (g) B3, §3.1 : la v0.3 écrit « s'expriment en millimètres ». B3-01 dit « sont exprimées » et le rectificatif, §1, « peuvent être exprimées ». La v0.3 garde la forme normative tout en disant intégrer le rectificatif.
- (h) §9, ligne GE-02 : la v0.3 écrit « remplacée » là où B3-02 dit « modifiée » ; or le registre conserve le texte historique et l'annote. La ligne GE-03 ajoute « le volume peut dépasser sa case » (Q1.2), qui ne figure pas dans B3-03.
- (i) §3.4 : « ARB-A et G1 [INS] : le volume ne traverse ni… » généralise une règle qui ne vise que le pas diagonal (R:121, R:128). C'est en contradiction avec PNV-6 (l.132).
- (j) Q4.7 : la v0.3 écrit « (initiales, configurables) ». Le message A dit « valeurs initiales configurables de test, et non des constantes universelles ».
- (k) §8 : « tranche ainsi deux points », alors que Q4.19 en tranche trois : ordre des voisines, case portant un corps, posture « couché ». Le §10 le dit d'ailleurs.
- (l) §5, l.217 : « qui devra se faire en arithmétique exacte » est une prescription glissée dans une liste de points ouverts. À marquer [DÉD] : Q3.14 arrondit la valeur exacte, 22 × 15/22 = 15, alors qu'un calcul flottant naïf donne 14,999… puis 14.
- (m) Le paragraphe « Portée de cette validation » de Q3.1 à Q3.6 (P1, l.153-161) n'est cité qu'au §15. Il dit que ces décisions ne modifient ni S2, ni G4, ni ARB-E, ni les règles de MEC-0002 sur les esquives, sauts et chutes, et que les coûts des portes restent distincts.

**W-09 — Formulations PNV.**
- (a) **PNV-2.** La v0.3 classe en [PNV] « toutes les données géométriques en millimètres entiers ». Mais le rectificatif, §1, parle de « La contrainte Q1 des millimètres entiers », que le §9 reprend à la ligne CH-08 (« les entiers de Q1 »). Les pièces Q1 ne l'énoncent que pour la largeur des cases (paire, Q1.1) et pour les enveloppes (paires, Q2.6) ; `grep` ne trouve « entier » dans aucune pièce Q1. Le §9 renvoie donc à une contrainte que le §3.5 tient pour non sourcée. À soumettre au propriétaire.
- (b) **§3.6, dernière puce.** « ne dépasse jamais sa case » suppose que l'unité est placée dans sa case. C'est PNV-4 (« au centre de case »), et la dépendance n'est pas déclarée.
- **Classements trop prudents, sans anomalie de fidélité :**
  - PNV-3 : une orientation à 45° pour une unité debout qui marche en diagonale se déduit de S1 et de Q4.17. Seule l'enveloppe du profil couché, dans T26, dépend de PNV-3.
  - PNV-6 : le contrôle du volume pour tous les pas a une base partielle dans Q1.2 (« les collisions restent obligatoires ») et Q4.2 (« chevauchement intérieur interdit »).
  - PNV-7 : « renvoi circulaire » est inexact ; c'est plutôt un renvoi sans objet, car aucune règle X puis Y ne figure dans P1.
- PNV-1, PNV-4, PNV-5, PNV-8 et PNV-9 sont correctement classées.

**W-10 — Scénarios : choix non sourcés dans des attendus.**
- (a) **T33** retient « l'identifiant stable le plus petit ». Q4.16 (D:110) dit seulement « départagées par identifiant stable », sans sens. « Croissant » n'est décidé que pour les événements (Q3.5) et les chutes (Q4.4).
- (b) **T04** admet +200 mm et −300 mm, ce qui suppose des seuils inclusifs. Q1.9 ne le dit pas, contrairement à CH-09 (« 3 m inclus »).
- (c) **T36** est en statut Sp, alors que les critères ouverts qui font passer T10 en Pa s'y appliquent aussi.
- (d) **T30** annonce « pas de dégât ». GE-05 ne l'assure que « sans composante de vitesse dirigée vers la surface ».
- (e) **T18** : « l'option B donnerait 6 TU » suppose un arrondi final des TU vers le bas, que l'option B ne fixe pas. Avec un arrondi vers le haut, on obtient 7.

**W-11 — Traçabilité interne.**
- (a) Dans la matrice du §12, la ligne PNV renvoie à « T25, T26 et T04 ». Or T25 ne dépend d'aucune PNV. Les scénarios conditionnels sont T03 (PNV-6), T04 (PNV-5), T26 (PNV-3) et T15.
- (b) Q2.1 à Q2.4, Q3.3, Q3.5 et Q3.10 sont rattachées à des scénarios qui ne les citent pas dans leurs sources. Écrire plutôt « aucun scénario dédié ».
- (c) Journal : C-08 est attribuée à « addendum Q5 (point 4) » et C-31 à « (point 5) ». Dans le message B, le point 4 est la provenance, le point 5 les coûts nuls (c'est C-08) et le point 6 le statut. De plus, « addendum Q5.1–Q5.2 » désigne ailleurs dans la v0.3 le message C, dont la numérotation ne correspond pas. À vérifier : une autre pièce, que je n'ai pas, est peut-être visée.
- (d) Le §14 range la relation « emplacement / case » sous « Réveil » ; elle relève de l'occupation des connexions.

**W-12 — Statut du rectificatif B3.**
- Le message E porte « Statut : proposition de rectification documentaire », sans ligne de validation. L'addendum, lui, porte « Validation : propriétaire ».
- La v0.3 le code pourtant [DÉC] et s'en sert aux §3.1, §3.2 (correction C-30) et §9 (ligne CH-08).
- **Correction :** indiquer ce statut aux §0 et §15, et faire confirmer le rectificatif lors de l'archivage.

**W-13 — Rapport à OXCE (§11).**
- (a) La ligne « G4, Q4.16, Écart établi » étend l'écart à Q4.16. Or le LOT-2A, §2 ligne 14, classe le départage des égalités « NV » : l'écart ne vaut que pour G4.
- (b) La « concordance d'ordre » d'ARB-D et Q3.14 n'est appuyée que sur R:111, qui ne parle pas du plafond. Je l'ai vérifiée dans le code : `src/Savegame/BattleUnit.cpp:2714-2720` ajoute les TU au solde en plafonnant au maximum, puis applique au total le rapport Force / poids porté et tronque. La concordance est exacte ; il faut ajouter cette référence.
- Les autres lignes du §11 sont conformes : LOT-2A §2 lignes 5, 6, 14 et 16, R:123, `Pathfinding.cpp:573-577` et `Armor.h:140-156`.

**W-14 — Q5.2, S10 et correspondance « emplacement / case ».**
- **Ce qui est cohérent :** aucune exception n'est ajoutée à S10 ; la relation est déclarée [OUV] ; T24 est en statut Pa.
- (a) Les notes des l.175 et 176 sont des lectures sans code, à marquer [DÉD]. Leur conséquence n'est pas tirée : puisque Q5.2 ne crée aucune exception à S10, deux emplacements occupés en même temps ne peuvent pas se trouver dans une même case.
- (b) Le transit à plusieurs utilisateurs (Q4.15) face à S10 « pour la traversée » n'est pas déclaré ouvert.

## 3. Matrice de traçabilité

(Matrice détaillée par décision ; voir le message d'origine du relecteur. Résumé : Q1.1 à Q1.4 classées « RV » ; Q1.5 à Q3.14 « PV » ; Q4.1 à Q4.21 « VC » (Q4.1, Q4.6 et Q4.7 « VC + DÉ ») ; Q5.1, Q5.2 et B3 « DÉ ». Fidélité : fidèle, sauf les écarts référencés W-01, W-02, W-03, W-07, W-08, W-10, W-12.)

## 4. Règles insuffisamment justifiées

1. La hauteur d'étage comme constante non configurable (§3.1, §3.2, §9) : W-01.
2. « les valeurs initiales sont sourcées (Q1) », dans la ligne prévue pour R:336 : W-02.
3. « devra se faire en arithmétique exacte » (§5) : W-08 (l).
4. « S10 s'applique telle qu'inscrite » ; la portée du mot « volontaire » ; la règle de l'ARB-A et de G1 étendue à tous les pas (§3.4).
5. Le sens du départage par identifiant de connexion (T33) et l'inclusion des bornes de ressaut (T04).
6. La clause de Q1.2 ajoutée à GE-03, au-delà du texte de B3-03 ; et la forme normative « s'expriment en millimètres ».

## 5. Corrections

Strictement nécessaires avant archivage et inscription : W-01 ; W-02 ; W-03 ; W-04 ; W-05 ; W-06 ; W-07 et W-08 (f) à (i) ; W-09 (a) et (b) ; W-10 (a) et (b) ; W-11 (a) et (c) ; W-12. Souhaitables : W-08 (a) à (e) et (j) à (m) ; reclassement des PNV trop prudentes (W-09) ; W-10 (c) à (e) ; W-11 (b) et (d) ; W-13 et W-14.

## 6. Limites (extrait)

- Copies non vérifiables : tout jugement « fidèle » porte sur les copies P1 et P2.
- Options d'origine de Q4.1 à Q4.21, Q5.1, Q5.2 et B3 absentes.
- Pièces des revues précédentes absentes.
- OXCE : code lu, ni compilé ni exécuté.
- Hors objet : R:115 dit encore que la v1.4.1 n'est pas archivée, alors qu'elle l'est depuis le commit `1ecc608`.

*Note de copie : les sections 3 (matrice détaillée) et 6 (commandes) du rapport d'origine sont résumées ci-dessus ; les sections 1, 2, 4 et 5 sont reproduites intégralement pour leur contenu décisionnel.*

---

## Partie 2 — Observations complémentaires de Claude Code (extrait de la transmission au propriétaire)

- **Réserve sur W-01.** Le relecteur classe W-01 « bloquant », au motif que la v0.3 aurait tranché seule. La consigne n° 2 du propriétaire pour la v0.3 (message F) disait pourtant : « La hauteur entre sols de référence reste fixée à 3 000 mm ». Elle n'avait pas été transmise au relecteur. Restait fondé : la v0.3 ne cite pas cette consigne, et le texte de B3-02 range cette hauteur parmi des valeurs qui « ne sont pas des constantes universelles ». Classement proposé : anomalie importante de traçabilité, à lever par une confirmation du propriétaire.
- **Ajout à W-05.** Inscrire aussi à l'inventaire le message de consignes pour la v0.3 (message F).
- **Vérifications faites par Claude Code**, non indépendantes : absence de « non vérifiée » et de « sous réserve » dans la v0.3 ; phrase de B3-03 présente ; statut « proposition » du rectificatif B3, sans ligne de validation ; min(solde + 60, 60) = 60 pour un solde de 0, 1, 10, 59 et 60 ; lignes 120, 273, 411, 423 et 428 de la v0.3 ; G1-05 de la v1.4.1 (« un passage fermé, l'autre ouvert ») ; R:115 non actualisé.
- **Omission reconnue.** Ni la consigne sur la hauteur d'étage ni la liste des remarques de Claude Code sur l'addendum Q5 n'avaient été remises au relecteur, d'où l'ambiguïté relevée en W-11 (c).
- **Deux confirmations demandées au propriétaire :** portée de la phrase de B3-02 sur la hauteur d'étage ; validation du rectificatif B3.
