# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.3

**Date :** 20 novembre 2026
**Nature :** projet de consolidation documentaire complète, préparé sous le mandat de la v0.4.3 (copie P7). Il corrige les anomalies AN-01 à AN-08 et traite les observations OB-01 à OB-08 de la revue indépendante de la v0.4.2, sans modifier les décisions. Non revu, non inscrit.
**Statut :**
- MEC-0001 et MEC-0002 restent **reportées** dans leur ensemble ;
- aucun gameplay, aucune implémentation, aucune inscription n'est autorisé ;
- aucun test n'a été exécuté.

**Base :**
- `main` = `818c646c7d33b819d8b69b81679749be6e77eff9` ;
- registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, SHA-256 `9117d20c45aa95abbc218ce5cdcc2a095106eb86c64a342be76d8521ef14d39e`.

**Succède à :** la v0.4.2 (SHA-256 `a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808`), revue de façon indépendante : verdict « conforme sous réserves » (pièce 13 bis, RV42).

**Lignée :** v0.3 (`85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256`) → v0.4 (`02d8da8d9595e98e256186d59edb3ce75c49d7a0bf1be8ea889f8e2f63dd2a52`) → v0.4.1 (`bd4cf4fa5f94aa005c6e27bf81eb6cc6aba6e7365c8eccaddaf847320a699e3f`) → v0.4.2 → v0.4.3. Corrections : W-01 à W-14 dans la v0.4 (§18) ; provenance de Q1.1 à Q1.4 dans la v0.4.1 (§19) ; six arbitrages, I-1 et M-01 à M-18 dans la v0.4.2 (§2 bis et §20) ; AN-01 à AN-08 et OB-01 à OB-08 dans la v0.4.3 (§21). Les décisions validées sont conservées ; la v0.4.3 n'en modifie aucune.

**Copies de travail citées** (dossier `…/scratchpad/revue-v03/`, empreintes au §15) :
- **P1** : propositions et validations de Q1 à Q3 ;
- **P2** : déclarations Q4.6 et Q4.7, Q5.1 et Q5.2, addenda Q5 et B3, rectificatif B3 ;
- **P3** : consignes pour la v0.3, mandat de revue de la v0.3, mandat de la v0.4 ;
- **P4** : rapport de revue de la v0.3 ;
- **P5** : options B de Q1.1 à Q1.4 (message I du propriétaire), qui complètent la copie P1 ;
- **P6** : mandat de la v0.4.2, avec les six arbitrages du propriétaire (message J) ;
- **RV41** : rapport de la revue indépendante de la v0.4.1 (pièce 13, fichier original du relecteur) ;
- **P7** : mandat de la v0.4.3 (message K) ;
- **RV42** : rapport de la revue indépendante de la v0.4.2 (pièce 13 bis, fichier original du relecteur).

Références : `D:NN` pour une ligne de la v0.2 ; `R:NN` pour une ligne du registre sur `main` ; `P1 l.NN` pour une ligne d'une copie ; `JS-NN` pour un message du propriétaire, désigné par son numéro dans l'extraction du journal de session (tableau du §0).

## 0. Provenance : niveaux de preuve

| Code | Sens | Vaut décision ? |
|---|---|---|
| **[INS]** | inscrit au registre sur `main` | oui |
| **[TR]** | proposition avec ses options, et validation, transmises **ensemble, dans un même message** du propriétaire : Q1.5 à Q3.14 (JS-30, 2026-11-19T20:36:22Z ; copie P1, intertitre « Message 1 ») | oui |
| **[TR-M]** | proposition avec ses options, et validation, transmises **en plusieurs messages** du propriétaire, qui forment ensemble le dossier : Q1.1 à Q1.4 (§0.1). Même catégorie que [TR], « proposition et validation transmises » (P3 l.116) ; mais aucun des messages ne contient à lui seul la proposition complète | oui |
| [TR-A] | **code retiré dans la v0.4.1.** Il désignait, dans la v0.4, l'option retenue et la validation citée, sans les options écartées (copie P1, intertitre « Message 2 » : JS-31). Q1.1 à Q1.4, classées [TR] dans la v0.4.1, relèvent de [TR-M] depuis la v0.4.2 | sans objet (§0.1) |
| **[CIT]** | validation citée au §12 de la v0.2 ; identifiant et option attestés, formulation résumée par l'orchestrateur | oui pour l'option ; formulation à vérifier |
| **[DÉC]** | déclaration du propriétaire, sans le texte de la proposition d'origine | oui |
| **[CONF]** | confirmation expresse du propriétaire, reçue avec le mandat de la v0.4 le 20 novembre 2026 (P3, message H) | oui |
| **[VAL]** | arbitrage validé expressément par le propriétaire dans le mandat de la v0.4.2, le 20 novembre 2026 (copie P6, message J) : texte de la décision validée et statut transmis ; textes des options non transmis | oui, dans les limites du statut indiqué (par exemple « principe validé ; modalités ouvertes ») |
| **[DÉD]** | conséquence arithmétique ou logique de règles sourcées, à vérifier | non |
| **[PNV]** | proposé, non validé : aucune décision explicite trouvée | **non** |
| **[OUV]** | point ouvert, déclaré comme tel | **non** |

- **Marqueur ⟨B3-03⟩** : provenance à confirmer par archivage. B3-03 l'exige pour les valeurs de Q1 « jusqu'à l'archivage de leur validation originale » (P2 l.169).
- **Statut des pièces :** toutes sont des copies transmises par le propriétaire. **Aucune n'est une pièce originale authentifiée de façon indépendante, et aucune n'est archivée dans le dépôt**, sauf mention contraire au §15. « La transmission complète des propositions ne vaut pas authentification indépendante de la conversation d'origine. » (P6 l.123)
- **Portée de [TR] et [TR-M]** (OB-05) : ces codes qualifient la transmission des pièces dans la session de travail, non l'échange d'origine. JS-30 regroupe lui-même cinq validations (P1 l.67, 111, 165, 213 et 293), que le message A situe entre 14 h 26 et 14 h 47 UTC (P2 l.12-14) : c'est une déclaration, non une preuve.

**Identifiants des messages** (AN-02). Un message du propriétaire est désigné par `JS-NN`, son numéro dans l'extraction mécanique du journal de session (O-7, 38 messages ; ses 36 premiers sont identiques à O-4, ses 35 premiers à O-1). Les intertitres des copies (« Message 1 », « Message A »…) restent ceux des copies.

| Identifiant | Horodatage (UTC) | Contenu | Copie |
|---|---|---|---|
| JS-22 | 2026-11-19T16:25:44.422Z | mandat de revue indépendante Q1–Q4 | non copié (pièce 14) |
| JS-23 | 2026-11-19T16:39:53.607Z | envoi de la consolidation v0.2, en pièce jointe | non copié ; la pièce jointe est la pièce 5 |
| JS-24 à JS-28 | 2026-11-19, de 19:56:49.488Z à 20:13:09.653Z | messages A à E | P2, intégraux |
| JS-29 | 2026-11-19T20:35:55.895Z | mandat en sept points de vérification de la provenance de Q1.5 à Q3.14 | non copié (pièce 14 bis) |
| JS-30 | 2026-11-19T20:36:22.283Z | propositions et validations de Q1.5 à Q3.14 | P1, intertitre « Message 1 », intégral |
| JS-31 | 2026-11-19T20:54:21.612Z | titres et options A de Q1.1 à Q1.4, validation, puis partie « Mission : » | P1, intertitre « Message 2 », sans la partie « Mission » |
| JS-32 à JS-34 | 2026-11-19T20:59:24.681Z ; 2026-11-19T21:08:57.339Z ; 2026-11-20T12:53:14.601Z | messages F, G et H | P3, intégraux |
| JS-35 | 2026-11-20T13:41:45.327Z | message I : options B de Q1.1 à Q1.4 | P5, intégral |
| JS-36 | 2026-11-20T14:44:23.468Z | message J : mandat de la v0.4.2 et six arbitrages | P6, intégral |
| JS-37 | 2026-11-20T15:41:03.718Z | autorisation de la revue indépendante de la v0.4.2 | non copié (pièce 14 ter) |
| JS-38 | 2026-11-20T16:12:04.779Z | message K : mandat de la v0.4.3 | P7, intégral |

### 0.1 Q1.1 à Q1.4 : un dossier composé de deux messages

**Les deux messages, dans l'ordre réel** (identifiants et horodatages du tableau du §0) :

| Ordre | Message | Horodatage | Contenu | Copie |
|---|---|---|---|---|
| 1 | **JS-31**, qui commence par « Pour Bastion MEC-0001, voici les quatre dernières propositions et validations originales manquantes : Q1.1 à Q1.4. » | 2026-11-19T20:54:21.612Z | titre et option A de Q1.1 à Q1.4 ; validation ; puis une partie « Mission : » (six consignes et des restrictions). **Aucune option B** | copie P1, intertitre « Message 2 » (l.297-310) : tout le message, **sauf** la partie « Mission », non reproduite (M-16) |
| 2 | **JS-35** (message I) | 2026-11-20T13:41:45.327Z | options B de Q1.1 à Q1.4, puis consignes de travail | copie P5, l.9-35 : message intégral |

**Avant les deux :** JS-29 (2026-11-19T20:35:55.895Z), mandat de vérification de la provenance de Q1.5 à Q3.14, écrivait : « Q1.1 à Q1.4 ne sont pas encore joints. Conserve explicitement leur provenance comme non vérifiée et identifie les règles de la consolidation qui en dépendent. » Les propositions de Q1.5 à Q3.14 ont suivi dans JS-30.

**Entre les deux :**
- le mandat de la v0.4 (JS-34, message H, 2026-11-20T12:53:14.601Z) écrivait : « Les pièces comprennent, pour chacune de ces décisions, les deux options A et B, puis la validation explicite de l'option A. » (P3 l.108). À cette heure, le dossier ne contenait pas les options B ;
- la v0.4, remise à 2026-11-20T13:05:12.403Z, demandait de les joindre ;
- JS-35 (message I) indique : « les options B de Q1.1 à Q1.4 ont déjà été transmises au propriétaire dans la conversation d'origine. Elles sont absentes de ta copie P1. » (P5 l.11). Le journal montre qu'elles manquaient déjà à JS-31 : la copie P1 n'est pas en cause, puisqu'elle reproduit fidèlement la partie du message qu'elle reprend.

**Les huit options et la validation**, reproduites des copies :

| Décision (titre, P1) | Option A (JS-31 ; P1) | Option B (JS-35 ; P5) |
|---|---|---|
| Q1.1 — Largeur des cases | « Largeur uniforme par carte, configurable et paire en millimètres. » (l.301) | « Une largeur différente selon le niveau tactique. Chaque étage possède son échelle. » (l.14) |
| Q1.2 — Dimensions physiques des unités | « Dimensions configurables par type d'unité et posture. Le volume peut dépasser sa case ; les collisions restent obligatoires. » (l.303) | « Dimensions obligatoirement contenues dans la case. Plus restrictif, notamment pour les unités couchées ou de grande taille. » (l.15) |
| Q1.3 — Épaisseur physique des murs | « Épaisseur configurable par type de mur ; les murs possèdent un volume physique défini. » (l.305) | « Épaisseur nulle. Les murs sont représentés uniquement par des surfaces séparant les cases. » (l.16) |
| Q1.4 — Hauteur de référence des niveaux | « Altitude configurable pour chaque niveau ; les étages pouvaient initialement être séparés par des hauteurs différentes. » (l.307) | « Espacement vertical constant. Tous les niveaux sont séparés par la même hauteur. » (l.17) |

Validation, dans JS-31 (P1 l.308-309) : « Pour Bastion MEC-0001, lot Q1 Géométrie, je valide Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A. Poursuis le lot Q1 en regroupant les paramètres numériques restants, avec comparaison vérifiée d'OpenXcomCE et de Kowlting, sans implémentation. »

Ce tableau, comme celui de P5 (l.39-48), est une **compilation** de Claude Code. Ce n'est pas un message original : aucun message ne contient à lui seul les huit options et la validation.

**Vérification** (Claude Code, comparaison de textes ; ce n'est pas une revue indépendante) :
- les huit libellés et la validation cités ici et au §3.1 sont identiques aux copies, et les copies aux messages du journal (contrôles 1 et 7 du §17) ;
- pour chaque décision, les deux options sont distinctes et s'excluent ; la validation retient A pour les quatre.

**Classement : [TR-M]** (§0). La condition du mandat de la v0.4 est remplie par les deux messages réunis : « Reclasser ces quatre décisions dans la catégorie « proposition et validation transmises », sous réserve que les textes complets soient effectivement joints au dossier de travail. » (P3 l.116). Les décisions ne changent pas : Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A.

**Limites :**
- la présence des options B dans la conversation d'origine repose sur la déclaration du propriétaire (P5 l.11). Je ne peux pas la vérifier : je n'ai pas accès à cette conversation ;
- l'existence de **deux options seulement** repose aussi sur ses déclarations (P3 l.108 ; P5 l.11-19). Les propositions de Q1.5 à Q1.9 en avaient trois, A, B et C (P1 l.11-53) ;
- pour Q1.1 à Q1.4, les pièces ne donnent que le titre et le libellé des options. Les propositions de Q1.5 à Q1.9 décrivent chaque option et signalent l'option recommandée (P1 l.11-53). On ne peut donc pas savoir si la proposition d'origine de Q1.1 à Q1.4 contenait davantage ;
- le libellé de l'option A de Q1.4 est au passé (« les étages pouvaient initialement être séparés… ») : c'est la formulation du message, citée telle quelle. Il a pu être rédigé après Q4.1 ; ce n'est pas vérifiable. La portée de Q1.4 n'en dépend pas : elle est fixée par R-7=A (§3.2) ;
- P1 et P5 sont des copies, ni authentifiées de façon indépendante ni archivées (RD-1, RD-6).

**Observation documentaire, sans valeur de décision** (M-06) : l'option B de Q1.4, écartée, et la règle actuelle ont un principe commun, un espacement vertical constant. W-01 et R-6=A y ajoutent la valeur de 3 000 mm et l'exclusion de tout réglage, global ou par carte. La règle applicable découle de GE-02, de Q4.1, de W-01 et de R-6=A, non de cette option (§3.2).

**Autres copies** (contrôle 7 du §17) : JS-24 à JS-28 (P2), JS-30 (P1), JS-32 à JS-34 (P3), JS-35 (P5), JS-36 (P6) et JS-38 (P7) sont copiés intégralement. La seule omission relevée est la partie « Mission » de JS-31 (P1).

## 1. Périmètre et responsabilités

- **MEC-0001** : marche ordinaire, cheminement, coûts en TU et en énergie, visibilité du trajet, portes et connexions spéciales [INS] (PE-01, R:196) ; B3-05 [DÉC].
- **MEC-0002** : sauts, chutes, contacts, collisions, esquives, repoussements, impacts [INS] (PE-01, PE-02, R:196-197). Les escaliers, échelles et ascenseurs sont hors de MEC-0002 [INS] (PE-03, R:198).
- Une perte de support transfère immédiatement la situation à MEC-0002 : Q4.3 [CIT].
- B3 n'autorise aucune nouvelle mécanique et ne modifie pas les règles de dégâts [DÉC].

## 2. Décisions inscrites et état actuel

| Règle | Ligne | État | Précisée ou modifiée par |
|---|---|---|---|
| S1 | R:71 | en vigueur | — |
| S2 | R:72 | en vigueur | Q3.1, Q3.13 ; Q3.12 (pas de surcoût universel de mur) |
| S3 | R:73 | en vigueur | — |
| S4 | R:74 | restreinte | ARB-A, G1 |
| S5 | R:75 | **historique** | supplantée par Z1 pour la sélection normale |
| S6, S7 | R:76-77 | en vigueur | S7 appliquée au trajet physique (G1) |
| S8, S9 | R:78-79 | en vigueur | Q3.4, Q4.21 |
| S10 | R:80 | en vigueur | exceptions ARB-B et G2 ; **aucune exception supplémentaire** créée par Q5.2 [DÉC] |
| S11 | R:81 | en vigueur | Q4.20 |
| S12 | R:82 | en vigueur | — |
| Z1 | R:90 | portée étendue | G3 (énergie) |
| N1 à N3 | R:91-93 | en vigueur | — |
| N4 | R:94 | en vigueur | ARB-C ; Q2.1 à Q2.4 |
| N5 à N10 | R:95-101 | historiques pour les chutes | MEC-0002 fait autorité |
| N11, N14 | R:102-111 | en vigueur | N14 : portée modifiée par G3 ; formule par Q3.14 ; effet possible sur l'énergie : M-04=B (§5) |
| ARB-A | R:121 | en vigueur | G1 |
| ARB-B | R:122 | en vigueur | Q4.19 |
| ARB-C | R:123 | en vigueur | Q2.1 à Q2.4, Q3.3, Q3.10, Q3.12, Q4.7 à Q4.15, Q5.2 |
| ARB-D | R:124 | en vigueur | Q3.14 ; Q4.6 ; M-04=B (énergie, modalités ouvertes) |
| ARB-E | R:125 | en vigueur | Q4.13 (transferts) ; Q5.1 |
| G1 | R:126-134 | en vigueur | — (priorité « X puis Y » non décidée : PNV-7) |
| G2 | R:135-140 | en vigueur | Q4.19 |
| G3 | R:141 | en vigueur | Q3.7 à Q3.9, Q3.13 ; M-05=A (coût réel accru mais payable) |
| G4 | R:142-147 | en vigueur | Q4.16 |
| GE-02 (MEC-0002) | R:203 | **à annoter** : une clause est modifiée par B3 (§9.1) | B3, Q1.1, Q1.5, Q1.7, Q4.1, [CONF] W-01 ; R-5=A, R-6=A, R-7=A |
| GE-03 (MEC-0002) | R:204 | **à annoter** : précisée (§9.1) | B3-03 ; Q1.2, précision explicite (R-8=A) ; Q1.6 ; R-5=A |

## 2 bis. Arbitrages du propriétaire du 20 novembre 2026

**Source :** mandat de la v0.4.2 (message J, 2026-11-20T14:44:23.468Z ; copie P6, §2, l.28-107). **Preuve :** [VAL] (§0).
- Les textes validés sont cités tels quels.
- Les textes des options d'origine (A, B…) ne sont pas transmis (RD-3).
- Dans P6, chaque arbitrage est suivi de « Conséquences ». La v0.4.2 les applique, aux sections indiquées.

| Arbitrage | Texte validé | Statut (P6) | Source | Appliqué en |
|---|---|---|---|---|
| **M-04=B** — surcharge et énergie | « La surcharge peut également réduire l'énergie ; modalités à définir. » | « principe validé ; modalités ouvertes » | P6 l.30-42 | §2, §5, §9.2, §10, §12, §14 |
| **M-05=A** — augmentation imprévue du coût d'un pas | « Si le coût augmente mais reste payable et que le passage est admissible, le pas est exécuté. » | « règle validée » | P6 l.43-56 | §2, §6, §9.2, §10, §12, §13 (T47), §14 |
| **R-5=A** — dimensions géométriques et précision numérique | « Dimensions physiques configurées en millimètres entiers ; calculs physiques non limités systématiquement aux entiers. » | « règle validée ; modalités techniques restantes ouvertes » | P6 l.57-70 | §2, §3.1, §3.5 (PNV-2), §9.1, §12, §13 (T48), §14 |
| **R-6=A** — hauteur des étages | « 3 000 mm fixes, sans réglage global ni par carte. » | « règle validée » | P6 l.71-82 | §2, §3.1, §3.2, §9.1, §12, §13 (T27) |
| **R-7=A** — portée résiduelle de Q1.4 | « Q1.4 reste historique pour l'altitude des niveaux de référence ; seules les variations locales de support demeurent. » | « clarification validée » | P6 l.83-93 | §2, §3.1, §3.2, §9.1, §12, §13 (T27) |
| **R-8=A** — articulation de Q1.2 et de GE-03 | « Q1.2 précise explicitement GE-03, avec géométrie commune aux deux mécaniques. » | « articulation validée » | P6 l.94-107 | §2, §3.1, §3.4, §9.1, §12 |

**Règle approuvée ou modalité à définir :**
- **règles validées, applicables telles quelles :** M-05=A ; R-6=A ; R-5=A pour ses deux énoncés (dimensions configurées en millimètres entiers ; calculs physiques non limités systématiquement aux entiers) ; R-7=A (« clarification validée ») et R-8=A (« articulation validée ») ;
- **principe validé, modalités à définir :** M-04=B. Aucun multiplicateur, arrondi ni pénalité d'énergie n'est fixé ;
- **modalités qui restent ouvertes :**
  - pour M-04=B : l'existence d'un effet dans chaque situation, son déclenchement, son calcul et ses valeurs (P6 l.38) ;
  - pour R-5=A : les modalités de conversion, la précision numérique et les arrondis des autres grandeurs calculées, lorsqu'ils ne sont pas spécifiés (P6 l.67).

**Portée :**
- ces arbitrages répondent aux points M-04, M-05 et R-5 à R-8 du rapport RV41 ;
- R-5=A « est commune à MEC-0001 et MEC-0002 dans le cadre du référentiel physique B3 » (P6 l.69) ;
- R-8=A « ne modifie pas à elle seule le registre sur `main` » (P6 l.106). Aucun des six arbitrages n'est inscrit : aucune inscription n'est autorisée.

## 3. Géométrie

### 3.1 Décisions Q1

| Décision | Texte validé | Source | Preuve |
|---|---|---|---|
| Q1.1=A | « Largeur uniforme par carte, configurable et paire en millimètres. » Option B, écartée : « Une largeur différente selon le niveau tactique. Chaque étage possède son échelle. » | P1 l.300-301, 309 ; P5 l.14 | [TR-M] ⟨B3-03⟩ |
| Q1.2=A | « Dimensions configurables par type d'unité et posture. Le volume peut dépasser sa case ; les collisions restent obligatoires. » Option B, écartée : « Dimensions obligatoirement contenues dans la case. Plus restrictif, notamment pour les unités couchées ou de grande taille. » Q1.2 précise explicitement GE-03 (R-8=A). | P1 l.302-303, 309 ; P5 l.15 | [TR-M] |
| Q1.3=A | « Épaisseur configurable par type de mur ; les murs possèdent un volume physique défini. » Option B, écartée : « Épaisseur nulle. Les murs sont représentés uniquement par des surfaces séparant les cases. » | P1 l.304-305, 309 ; P5 l.16 | [TR-M] |
| Q1.4=A | « Altitude configurable pour chaque niveau ; les étages pouvaient initialement être séparés par des hauteurs différentes. » Option B, écartée : « Espacement vertical constant. Tous les niveaux sont séparés par la même hauteur. » **Historique** pour l'altitude des niveaux de référence ; seules les variations locales de support demeurent (R-7=A, §3.2). | P1 l.306-307, 309 ; P5 l.17 | [TR-M] |
| Q1.5 | 1 500 mm (option B : « compromis initial pour les personnages et les obstacles »). | P1 l.11-17, 67 | [TR] ⟨B3-03⟩ |
| Q1.6=A | « debout 600 × 600 × 1 800 ; agenouillé 600 × 600 × 1 200 ; couché 1 200 × 600 × 500, orienté selon le corps ». Largeur × profondeur × hauteur, en millimètres ; « Ce sont des volumes de collision proposés, pas des dimensions anatomiques exactes. » | P1 l.19-29, 67 | [TR] ⟨B3-03⟩ |
| Q1.7 | 100 mm (option A : « mur standard relativement fin »). | P1 l.31-37, 67 | [TR] ⟨B3-03⟩ |
| Q1.8=A | 3 000 mm, « hauteur de référence initiale entre étages ». Son cadre configurable est historique : la hauteur d'étage est fixe (W-01, R-6=A ; §3.2). | P1 l.39-45, 67 | [TR] |
| Q1.9=A | « Montée 200 mm, descente 300 mm » : seuils initiaux des ressauts pour un humain debout. | P1 l.47-53, 67 | [TR] ⟨B3-03⟩ |

**Portée de Q1.5 à Q1.9** [TR] (P1 l.55) : « Ces choix fixent uniquement les valeurs initiales de référence. Les autres types d'unités, postures, murs et cartes pourront utiliser des paramètres différents. » Ce sont des valeurs initiales configurables, **sauf la hauteur d'étage**, fixée par W-01 [CONF] et R-6=A [VAL] : elle n'est réglable ni globalement ni par carte, et ce n'est pas une valeur initiale ajustable (§3.2).

**Référentiel commun B3** [DÉC] (P2, message D, B3-01) : MEC-0001 et MEC-0002 utilisent le même référentiel physique, à savoir les coordonnées, les dimensions des cases, les niveaux, les surfaces, les volumes de collision, les postures et les orientations. Il n'existe pas de dimensions concurrentes d'une même unité selon qu'elle marche, saute ou tombe. **R-8=A** [VAL] (P6 l.96) : « Q1.2 précise explicitement GE-03, avec géométrie commune aux deux mécaniques. » Le même volume physique sert à MEC-0001 et à MEC-0002 (P6 l.103).

**Unités de mesure :**
- B3-01 écrivait « Les distances et dimensions physiques sont exprimées en millimètres. » ;
- le rectificatif B3 (§1), validé (W-12), écrit : « Les dimensions physiques configurées **peuvent être exprimées** en millimètres. » (P2 l.217). Il ajoute : « La contrainte Q1 des millimètres entiers ne doit pas être étendue implicitement aux grandeurs physiques intermédiaires calculées par MEC-0002. » (P2 l.219) ;
- **R-5=A** [VAL] (P6 l.59) tranche ensuite : « Dimensions physiques configurées en millimètres entiers ; calculs physiques non limités systématiquement aux entiers. » **C'est la règle applicable**, commune à MEC-0001 et à MEC-0002 (P6 l.69) :
  - les dimensions physiques configurées sont exprimées en millimètres entiers ;
  - les calculs physiques intermédiaires ne sont pas soumis à un arrondi systématique au millimètre entier ;
  - les conventions d'arrondi déjà validées sont conservées : Q2.6 (enveloppes), Q3.13 (coûts), Q3.14 (surcharge). Elles ne sont pas étendues à d'autres calculs sans source ;
  - restent ouverts : les modalités de conversion, la précision numérique et les arrondis des autres grandeurs calculées (P6 l.67).

**Configurations admissibles** (rectificatif, §4) :
- les dimensions configurées sont des millimètres entiers : R-5=A [VAL] ;
- la parité de la largeur des cases est sourcée par Q1.1 [TR-M] ⟨B3-03⟩ ;
- les dimensions minimales, les tolérances, les modalités de conversion et les conventions d'arrondi géométriques autres que celle de Q2.6 restent [OUV] ;
- le rectificatif ne crée aucune contrainte.

**Valeurs sans source vérifiable :** voir les PNV du §3.5.

### 3.2 Hauteur des étages : chronologie et règle applicable

1. **GE-02** [INS] (R:203) : « Hauteur d'étage : **3 m** fixes entre deux sols d'étages consécutifs », précisée par l'arbitrage A3A, « qui fixe en mètres la seule hauteur d'étage ». Elle est reprise par CH-08 (R:249). CH-01 et CH-03 assimilent un étage à 3 m (R:242, R:244).
2. **Q1.4=A** [TR-M] : altitude configurable pour chaque niveau, avec des hauteurs d'étage possiblement différentes. *Écart avec GE-02 à cette date.* L'option B, écartée, prévoyait un « espacement vertical constant » (P5 l.17) ; la règle applicable ne repose pas sur elle (observation du §0.1).
3. **Q1.8=A** [TR] : 3 000 mm comme hauteur de référence initiale, dans le cadre configurable de Q1.5 à Q1.9 (P1 l.55).
4. **Q4.1=A** [CIT] (D:86) : « 3 m fixes entre sols de référence des étages tactiques consécutifs, avec possibilité de dénivelés locaux ». Q4.1 rectifie Q1.4.
5. **Confirmation W-01** [CONF] (P3 l.88) : « La hauteur entre les sols de référence de deux étages tactiques consécutifs est fixée à 3 000 mm, non configurable par carte. Les dénivelés locaux restent possibles. » Elle reprend la consigne n° 2 pour la v0.3 (P3 l.15) : « La hauteur entre sols de référence reste fixée à 3 000 mm. »
6. **R-6=A** [VAL] (P6 l.73) : « 3 000 mm fixes, sans réglage global ni par carte. » Il précise W-01 : la hauteur « n'est configurable ni globalement ni individuellement par carte » (P6 l.77).

**Règle applicable** (GE-02, précisée par Q4.1, confirmée par W-01, puis par R-6=A) : 3 000 mm fixes entre les sols de référence de deux étages tactiques consécutifs, réglables ni globalement ni par carte. Ce n'est pas une valeur initiale ajustable. Les dénivelés locaux des supports restent possibles.

**Historique conservé :**
- Q1.4 et le cadre configurable de Q1.8 restent dans l'historique et ne sont pas effacés.
- **R-7=A** [VAL] (P6 l.85) : « Q1.4 reste historique pour l'altitude des niveaux de référence ; seules les variations locales de support demeurent. » Q1.4 ne confère donc plus aucune faculté de configurer l'altitude de référence d'un étage (P6 l.89). Aucune autre exception à la hauteur fixe de 3 000 mm n'est créée (P6 l.91).
- **B3-02, tel qu'écrit** (P2 l.143-151), range « hauteur entre sols de référence de deux étages consécutifs : 3 000 mm » parmi les « valeurs initiales prévues », puis précise : « Ces valeurs ne sont pas des constantes universelles. » La pièce n'est pas modifiée. En vertu de W-01 et de R-6=A, cette phrase **ne s'applique pas à la hauteur d'étage**. B3-02 ajoute d'ailleurs : « La hauteur d'étage de 3 000 mm demeure la règle explicitement validée par Q4.1 », et le rectificatif (§2) : « B3 conserve cette hauteur et n'introduit aucune nouvelle valeur ».

**Restent ouverts** [OUV] : les bornes des dénivelés locaux ; le rattachement d'une case à un étage.

### 3.3 Murs et enveloppes

- **Q2.5=A** [TR] (P1 l.97-101, 111) : « Mur centré sur la frontière commune. Son épaisseur se répartit de part et d'autre ; un mur de 100 mm occupe 50 mm dans chaque case. »
- **Q2.6=A** [TR] (P1 l.103-107, 111) : « L'enveloppe calculée est agrandie au plus petit nombre pair de millimètres qui la contient intégralement. »
- **B3-04** [DÉC] : les enveloppes de calcul ne remplacent pas, sans justification, les volumes réels qu'exige CO-01 (R:265).

### 3.4 Contacts et collisions

- **Q4.2=A** [CIT] (D:87) : un contact de surfaces est détectable. Le contact seul ne bloque pas la marche, contrairement au chevauchement intérieur, qui est interdit. Impacts et dégâts restent sous MEC-0002.
- **Pour le pas diagonal seulement** — ARB-A et G1 [INS] (R:121, R:126-133) : le volume emprunte un passage sans traverser une autre unité consciente ni un obstacle, et un corps reste traversable (ARB-B).
- **Pour tous les volumes** — Q1.2 [TR-M], précision explicite de GE-03 (R-8=A) : « les collisions restent obligatoires ».
- **Méthode de contrôle du volume balayé pour les pas non diagonaux :** non décidée (PNV-6).
- **GE-05** est inchangée ; sa tolérance numérique reste [OUV].

### 3.5 Formulations sans source suffisante (PNV)

| N° | Formulation (v0.2) | Sources trouvées | Statut |
|---|---|---|---|
| PNV-1 | Repère : x vers l'est, y vers le sud, z vers le haut ; origine au nord-ouest ; indices à partir de zéro ; centres de case en (i + 0,5) × L (D:29) | N3 et GE-01 [INS] donnent seulement des positions (x, y, z) ; Q1.1, une largeur uniforme par carte | positions (x, y, z) : [INS] ; le reste : **[PNV]** |
| PNV-2 | Toutes les données géométriques en millimètres entiers ; conversion des valeurs externes « vers demi-entiers », la moitié arrondie en s'éloignant de zéro (D:30) | Q1.1 (largeur **paire** en mm, donc entière) ; Q2.6 (enveloppes en nombre **pair** de mm). Le rectificatif (§1) parle de « la contrainte Q1 des millimètres entiers » (P2 l.219). **R-5=A** (P6 l.59) | **dimensions configurées** en millimètres entiers : **tranché**, [VAL] R-5=A, pour MEC-0001 et MEC-0002 ; largeur paire : [TR-M] ; enveloppes paires : [TR] ; **données calculées** : non limitées systématiquement aux entiers (R-5=A), hors arrondis validés ; la formulation de D:30, « Unités physiques de géométrie : mm entiers », ne vaut donc pas règle pour les données calculées ; **conversion** des valeurs externes « vers demi-entiers » : **[PNV]** ; précision et arrondis des autres grandeurs calculées : [OUV] |
| PNV-3 | Orientations sur huit directions (D:32) | S1 [INS] (huit directions de déplacement) et Q4.17 [CIT] (orientation vers le pas engagé) : une unité qui marche en diagonale est orientée à 45° [DÉD]. Q1.6 dit « orienté selon le corps » | orientation à 45° lors d'un pas diagonal : [DÉD] ; liste fermée de huit orientations, et orientation d'une unité couchée : **[PNV]** |
| PNV-4 | D:34 : « Support : pieds de l'unité sur un support physiquement uniforme et valide pour son volume horizontal ; unité stable au centre de case à l'arrivée. » | Q2.1 (« positions stables »), Q2.2 (« supports horizontaux », « positions stables horizontales »), Q4.19 (« avec support ») | positions stables horizontales : [TR] ; support « physiquement uniforme » et « valide pour son volume horizontal » ; unité « au centre de case » : **[PNV]** |
| PNV-5 | Au-delà des seuils de Q1.9, marche refusée, sans chute ni saut automatique (D:35) | ARB-C [INS] : la marche ne change pas de niveau implicitement ; sauts et chutes relèvent de MEC-0002 (PE-01, PE-02) | absence de changement de niveau implicite : [INS] ; refus au-delà du seuil et absence de chute automatique : **[PNV]** ; inclusion des bornes : [OUV] |
| PNV-6 | Phases d'un pas (montée verticale puis translation ; descente horizontale puis abaissement) ; volume balayé de chaque pas vérifié (D:36) | G1 [INS] pour la diagonale ; base partielle pour les autres pas : Q1.2 (« collisions restent obligatoires ») et Q4.2 (chevauchement intérieur interdit) | phases : **[PNV]** ; contrôle du volume : [INS] pour la diagonale ; méthode pour les autres pas : **[PNV]** |
| PNV-7 | Diagonale : priorité au passage X, puis Y (D:37) | G1 [INS] dit « l'un des passages orthogonaux praticables », sans priorité. Q4.16 [CIT] renvoie à une « règle X d'abord Q1 » : **renvoi sans objet**, car aucune règle « X puis Y » ne figure dans les pièces Q1 | **[PNV]** jusqu'au texte d'origine de Q4.16 |
| PNV-8 | Réveil simultané : ordre par identifiant croissant ; voisins N, NE, E, SE, S, SW, W, NW ; sans nouvelle tentative en boucle (D:39) | Q4.19 [CIT] : ordre des voisins, pas de nouvelle recherche automatique. Q3.5 [TR] ne vise que les « événements simultanés **sur le trajet** » | ordre des voisins et absence de nouvelle recherche : [CIT] ; ordre de traitement de réveils simultanés : **[PNV]** ; attribution à Q1 retirée |
| PNV-9 | Représenter l'ordre du trajet physique et la position exacte des rencontres (D:40) | Q4.3 [CIT] (perte de support), Q5.1 [DÉC] (tir de réaction), Q3.4 [TR] et S8 [INS] (obstacle inconnu), Q3.5 [TR] (ordre des événements du trajet) | cas énumérés : sourcés ; exigence générale : **[PNV]** |

### 3.6 Conséquences [DÉD]

- **Largeur intérieure entre deux murs standards :** 1 500 − 2 × 50 = **1 400 mm** (Q1.5, Q1.7, Q2.5) ⟨B3-03⟩.
- **Enveloppe d'une unité debout à 45° :** 848,5 → **850 mm** (Q1.6, Q2.6 ; orientation : PNV-3, partie [DÉD]) ⟨B3-03⟩.
- **Enveloppe d'une unité couchée à 45° :** 1 272,8 → **1 274 mm** ; dépend de **PNV-3** (orientation d'une unité couchée) ⟨B3-03⟩.
- **Rotation du profil couché :** étendue horizontale maximale de **1 341,6 mm** (vers 26,6°), inférieure à 1 400 mm ⟨B3-03⟩. Le volume balayé reste [OUV].
- **Rapport case / étage initial :** 1 500 / 3 000 = **0,5** ⟨B3-03⟩.
- **Le profil humain initial ne dépasse pas sa case horizontalement** (600, 1 200 et 1 274 mm, pour 1 500 mm) **si l'unité est placée au centre de sa case**, ce qui dépend de **PNV-4** ⟨B3-03⟩. D'autres types d'unités peuvent dépasser leur case (Q1.2).

## 4. Connexions, passages et portes

| Décision | Texte validé | Source | Preuve |
|---|---|---|---|
| Q2.1=A | « Connexions explicites entre positions stables. Chaque escalier relie des positions et niveaux définis ; le trajet physique doit rester praticable, sans modifier implicitement le niveau tactique. » | P1 l.71-75, 111 | [TR] |
| Q2.2=A | « Passages spéciaux entre supports horizontaux. Une rampe est un trajet de connexion défini ; ses extrémités sont des positions stables horizontales. Les collisions du trajet sont contrôlées. » | P1 l.77-81 | [TR] |
| Q2.3=A | « Action spécifique avec connexion définie. Accès réservé aux unités compatibles, points d'entrée et de sortie explicites et volume de passage contrôlé. Aucun déplacement vertical ordinaire implicite. » | P1 l.83-87 | [TR] |
| Q2.4=A | « Plateforme à états explicites. L'ascenseur possède un niveau courant et des connexions d'accès disponibles seulement lorsque les conditions de son état le permettent. » L'option de téléportation est écartée. | P1 l.89-93 | [TR] |
| Q3.3=A | « Coût défini par connexion. Escaliers, rampes, échelles et ascenseurs possèdent des coûts TU/énergie configurables. Aucun double débit automatique des segments géométriques. » | P1 l.129-133, 165 | [TR] |
| Q3.10=B | « Coûts obligatoirement définis par connexion. Aucun barème universel pour l'instant ; des valeurs de test seront définies pour chaque scénario. » Les chiffres de l'option A, écartée, ne sont pas repris. | P1 l.193-197, 213 | [TR] |
| Q3.12=A | « Aucun surcoût universel lié au mur. Un mur infranchissable bloque ; un passage ouvert est traité selon les coûts du terrain ou de sa connexion. L'ouverture d'une porte est une action distincte. » | P1 l.205-209, 213 | [TR] |
| Q4.7=A | Porte ordinaire : ouverture manuelle explicite, initialement 4 TU et 0 énergie ; pas de pas automatique ensuite ; les portes particulières ont des règles propres. Les valeurs sont des « valeurs initiales configurables de test, et non des constantes universelles ». | D:95 ; P2 l.18 | [CIT] ; valeurs [DÉC] |
| Q4.8=A | Connexion avec occupation physique et capacité ; admission, collision et sortie vérifiées ; coûts par connexion sans double débit des segments ; pas d'animation universelle requise ; aucun transfert par téléportation. | D:96 | [CIT] |
| Q4.9=A | Interruption du transfert : la position et l'état physique atteints sont conservés, sans arrivée complétée automatiquement ; perte de support : Q4.3 et MEC-0002. | D:97 | [CIT] |
| Q4.10=A | Transit interrompu mais soutenu : état suspendu, qui conserve la position, l'orientation et le lien avec la connexion ; reprise possible ; support perdu : MEC-0002. Cet état n'est pas une station tactique ordinaire. | D:101 | [CIT] |
| Q4.11=A | Coût intégral payé à l'engagement ; vérification avant le débit ; aucun remboursement en cas d'interruption ; pas de refacturation des segments d'un même transfert ; une action nouvelle a un coût nouveau. Le coût par pas de marche n'est pas modifié. | D:102 | [CIT] |
| Q4.12=A | Reprise du même transfert, dans le même sens, sans nouveau paiement, après vérification. Le retour vers l'entrée est une nouvelle action, avec son propre coût et sans remboursement. | D:103 | [CIT] |
| Q4.15=A | Chaque connexion définit sa capacité ; plusieurs utilisateurs possibles si la capacité et les volumes le permettent, sans chevauchement intérieur interdit, avec un accès et une sortie physiquement valides. | D:106 | [CIT] |

**Q5.2=A** [DÉC] (P2, message B l.34-38 ; addendum Q5, §B, l.83-95). Texte de l'addendum :
- « Une connexion peut avoir une capacité supérieure à une unité. Cette capacité ne supprime pas les règles d'occupation de S10. »
- « Chaque unité consciente occupe un emplacement tactique stable distinct lorsqu'elle est en position stable. »
- « Aucune superposition volontaire de deux unités conscientes sur un même emplacement stable n'est autorisée. »
- « Une plateforme comportant plusieurs emplacements peut accueillir plusieurs unités si la capacité et les volumes physiques le permettent. »
- « Une plateforme ne comportant qu'un emplacement tactique stable ne peut pas accueillir deux unités conscientes à cet emplacement. »
- « Le transit physique reste soumis aux contrôles de volume et d'occupation de Q4.8 et Q4.15. »
- « L'exception transitoire au réveil prévue par G2 reste inchangée. »
- **Q4.15 ne constitue pas une exception supplémentaire à S10** : c'est la « Rectification demandée » de l'addendum Q5, §B : « expliciter que Q4.15 ne constitue pas une exception supplémentaire à S10 » (P2 l.95). Le message B le dit de Q5.2 : « Q5.2 ne crée donc aucune exception supplémentaire à S10 » (P2 l.38).

**Lectures documentaires** [DÉD] :
- Q5.2 ne crée aucune exception, et S10 rend infranchissable « une case occupée par une autre unité », sauf ARB-B et G2. **Deux unités conscientes en position stable ne peuvent donc pas occuper la même case**, hors de l'exception transitoire au réveil prévue par G2 (R:137), que l'addendum maintient (P2 l.92). Rien n'autorise implicitement l'inverse.
- Le mot « volontaire » ne crée pas d'exception : seule l'exception transitoire de G2 est inscrite, et les situations propres à MEC-0002 relèvent de ses règles.

**Restent ouverts** [OUV] :
- la correspondance exacte entre « emplacement tactique stable » et « case » ;
- l'occupation pendant un transit partagé, au regard de S10 « pour la traversée » ;
- les profils complets des connexions : géométrie, support pendant le transit et en cas d'inconscience, accès, sortie, capacité, états d'ascenseur, coûts par instance ;
- le déclenchement de la reprise d'un transfert suspendu ;
- le réveil d'une unité restée dans une connexion ;
- le chemin et le coût d'un retour partiel (Q4.12).

## 5. Coûts, ressources et surcharge

**Décisions :**
- **Q3.1=A** [TR] (P1 l.115-119) : « Barème par type de terrain. Chaque terrain définit un coût d'entrée en TU et en énergie. Les règles existantes déterminent ensuite les coûts des pas diagonaux. » Il s'agit du coût d'entrée de la case d'arrivée, par cohérence avec S2 (R:72) [DÉD].
- **Q3.2=A** [TR] (P1 l.121-127) : « Multiplicateur configurable indépendant. L'énergie d'une diagonale possède son propre facteur. Le multiplicateur TU de S2 reste inchangé. »
- **Portée de Q3.1 à Q3.6** [TR] (P1 l.153-161) : « Ces six décisions ne fixeront pas encore les barèmes chiffrés de TU et d'énergie. Elles ne modifieront pas S2, G4, ARB-E ni les règles de MEC-0002 concernant les esquives, sauts et chutes. Les coûts des portes et des interactions distinctes resteront à distinguer des coûts de marche afin d'éviter toute facturation implicite. »
- **Q3.7=A** [TR] (P1 l.171-177) : « 4 TU et 2 énergie. Une diagonale coûte alors 6 TU, selon S2. »
- **Q3.8=A** [TR] (P1 l.179-183) : « normal = coût de base ; difficile = +50 % de TU et d'énergie ; très difficile = +100 %, avec arrondi entier à définir ». L'arrondi est défini par Q3.13.
- **Q3.9=A** [TR] (P1 l.185-191) : « Facteur initial 1,5 avec arrondi supérieur. Un coût énergétique de 3 devient 5 en diagonale. »
- **Q3.13=A** [TR] (P1 l.219-243, 293) : « Le coût de base est multiplié par le facteur de terrain, puis arrondi à l'entier supérieur pour chaque ressource. Ensuite, la diagonale applique ses propres règles : TU ×1,5 arrondi inférieur (S2) ; énergie ×1,5 arrondi supérieur (Q3.9). Chaque coût final est entier et calculé une seule fois avant le pas. »

**Barème initial** [DÉD], valeurs initiales configurables :

| Terrain | Orthogonal | Diagonal |
|---|---|---|
| Normal | 4 TU, 2 énergie | 6 TU, 3 énergie |
| Difficile (+50 %) | 6 TU, 3 énergie | 9 TU, 5 énergie |
| Très difficile (+100 %) | 8 TU, 4 énergie | 12 TU, 6 énergie |

**Ressources :**
- **Q3.6=A** [TR] (P1 l.147-151) : « L'énergie possède un maximum et une règle de récupération distincts de ceux des TU. Les valeurs seront fixées séparément. »
- **Q3.11=B** [TR] (P1 l.199-203) : « Valeurs à déterminer après calibration. La réserve et sa récupération restent configurables, sans valeurs définitives avant les essais de rythme de jeu. »
- **Q4.6=A** [CIT], valeurs [DÉC] (D:94 ; P2 l.18) : elle fixe ensuite les **valeurs initiales de test** : 60 TU maximales, 60 TU récupérées par tour, 100 d'énergie maximale, 20 d'énergie récupérée par tour. Ce sont des « valeurs initiales configurables de test, et non des constantes universelles ». Une valeur de test n'est pas une valeur définitive au sens de Q3.11 : il n'y a pas de contradiction. Les valeurs d'**énergie** (100 et 20) sont identiques à celles de l'option A de Q3.11, écartée (« Maximum 100 ; récupération 20 par tour », P1 l.201). Les valeurs de TU (60 et 60) ne sont pas concernées par cette correspondance.

**Surcharge :**
- **ARB-D** [INS] (R:124) : TU disponibles = min(solde + TU récupérées, TU maximales), puis réduction due à la surcharge sur ce total plafonné ; énergie récupérée séparément.
- **Q3.14=A** [TR] (P1 l.245-289, 293) : « La capacité de portage est une donnée exprimée en kg, déterminée par la Force selon une conversion configurable. Le facteur de surcharge est `min(1, capacité / charge)`, avec facteur 1 lorsque la charge est nulle. Ce facteur s'applique au total de TU déjà récupérées et plafonnées, conformément à ARB-D. Le résultat est arrondi à l'entier inférieur. »

```text
F = 1                         si charge = 0
F = min(1, capacité / charge) si charge > 0
TU_après = ⌊ min(TU_restantes + TU_récupérées, TU_max) × F ⌋
```

- **Q4.5=A** [CIT] (D:93) : conversion Force → kg configurable par type, unique pour les deux mécaniques, capacités positives. Les valeurs restent ouvertes. La mention « aucune formule Force × 10 universelle » ne vient que du résumé.
- **Charge portée** [INS] (GE-07, R:208) : armure, équipement, inventaire, distincte de la masse totale (GE-06).
- **Surcharge et énergie — M-04=B** [VAL] (P6 l.32) : « La surcharge peut également réduire l'énergie ; modalités à définir. » Statut : « principe validé ; modalités ouvertes » (P6 l.42). Application (P6 l.35-40) :
  - aucune affirmation générale selon laquelle la surcharge ne réduirait pas l'énergie ne subsiste. La v0.4.1 en contenait une, marquée [DÉD] ; elle est retirée ;
  - la réduction des TU (ARB-D, Q3.14) est inchangée ;
  - la récupération séparée de l'énergie (ARB-D : « L'énergie est récupérée séparément ») est inchangée ;
  - des effets de la surcharge sur l'énergie sont possibles. Leur existence dans chaque situation, leur déclenchement, leur calcul et leurs valeurs ne sont pas spécifiés [OUV] ;
  - la formule de surcharge des TU ne s'applique pas automatiquement à l'énergie. Aucun multiplicateur, arrondi ni pénalité d'énergie n'est fixé ;
- **Rappel du registre**, qui ne vient pas de P6 (OB-01) : la clause d'ARB-D « La surcharge ne majore pas le prix des pas » [INS] (R:124) n'est pas modifiée par M-04=B.
- **Point d'articulation** [OUV] (OB-06) : N14 retient le « principe d'OXCE, sans seuil d'immobilisation supplémentaire » et « aucune immobilisation liée à la charge » (R:104-105). Or OXCE ne réduit pas la récupération d'énergie selon la charge : `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`, commit `441cae1b`) ne tient compte que des blessures mortelles au torse. L'articulation de N14 et d'ARB-D avec M-04=B, décision postérieure du propriétaire, reste à traiter avec les modalités de M-04=B.
- **Arithmétique**, en trois niveaux :
  - **exigence validée** — Q3.14 : arrondir vers le bas la valeur du produit ;
  - **nécessité technique démontrée** [DÉD] — un calcul flottant naïf de ⌊22 × (15/22)⌋ donne 14 au lieu de 15 ; un calcul exact est donc nécessaire pour appliquer Q3.14 fidèlement ;
  - **recommandation non arbitrée** [OUV] — la méthode : nombres rationnels, ou entiers et division entière.

**Restent ouverts** [OUV] : modalités d'un effet de la surcharge sur l'énergie (M-04=B) ; autres pénalités de TU et leur ordre ; table Force → kg ; indicateur « encombré ».

## 6. Exécution d'un pas et événements

**Décisions :**
- **G3** [INS] (R:141) : chaque pas coûte des TU et de l'énergie, et n'est exécuté que si les deux suffisent.
- **Q3.4=A** [TR] (P1 l.135-139) : « Vérifier avant chaque pas et interrompre si nécessaire. Le pas non commencé n'est pas débité. Les pas déjà accomplis conservent leurs coûts. Les découvertes actualisent la connaissance conformément à S8–S11. »
- **Q3.5=A** [TR] (P1 l.141-145), « Événements simultanés **sur le trajet** » : « Les règles déjà décidées ont priorité. En cas d'égalité restante, les événements sont départagés par leur identifiant unique croissant. Leur applicabilité est réévaluée après chaque résolution. »
- **Q4.4=A** [CIT] (D:89) : les chutes nées d'un même événement suivent un ordre stable, en file par identifiant croissant ; les chutes secondaires s'ajoutent en fin de file, avec revalidation selon EN-07 ; Q3.5 ne renverse pas ces priorités.

**États d'un pas** (distinction demandée par l'addendum Q5, §A) :

| État | Règle | Source |
|---|---|---|
| Non commencé | aucun débit | Q3.4 [TR] ; Q4.3, Q4.21 [CIT] |
| Engagé | débité une seule fois ; débit conservé | Q4.3 [CIT] ; Q5.1 [DÉC] |
| Achevé | coût conservé, sans remboursement | Q3.4 [TR] ; ARB-E [INS] |
| Interrompu par un événement physique prioritaire | effet immédiat à la position physique courante ; relais à MEC-0002 ; pas engagé débité ; pas non commencé non facturé ; ni retour ni téléportation | Q4.3 [CIT] ; Q5.1 [DÉC] |

L'instant précis du passage de « non commencé » à « engagé » est [OUV]. Le support pendant les phases intermédiaires d'un pas est [OUV], lié à PNV-6.

**Q5.1=A** [DÉC] (P2, message B l.28-32 ; addendum Q5, §A, l.70-82) :
- « Un tir de réaction qui interrompt une marche ordinaire est résolu à la frontière du pas tactique engagé, une fois ce pas achevé. »
- « Le pas engagé est débité une seule fois. »
- « L'unité atteint la destination tactique admissible du pas avant la résolution du tir. »
- « Le tir effectivement effectué interrompt l'ordre, même s'il manque. »
- « Un simple pivot sans tir n'entraîne pas l'interruption prévue par ARB-E. »
- « La perte de support et les autres événements physiques prioritaires restent immédiatement applicables conformément à Q4.3 et MEC-0002. »
- « Les conditions de détection, de déclenchement et les coûts d'Overwatch demeurent hors de cet arbitrage. »

**Autres interruptions :**
- **Q4.13=A** [CIT] (D:104) : un tir de réaction effectivement tiré contre une unité en transfert interrompt aussi l'action, même sans toucher ; le coût et la position sont conservés ; le transfert n'est pas complété. Pendant la marche, la règle est celle de Q5.1.
- **Q4.14=A** [CIT] (D:105) : une incapacité interrompt l'action, puis le support est contrôlé ; l'unité reste en place si elle est soutenue, sinon elle chute sous MEC-0002. Il n'y a pas de chute automatique indépendante du support.
- **Q4.20=A** [CIT] (D:114) : une révélation seule, sans obstacle au trajet ni tir déclenché, n'interrompt pas la marche. Si elle bloque réellement le trajet, S8 à S11 s'appliquent.
- **Q4.21=A** [CIT] (D:115) : quand le pas suivant n'est plus exécutable (coût réel supérieur, occupation, obstacle inattendu), l'unité s'arrête sans débit de ce pas non commencé ; la connaissance et la zone atteignable sont mises à jour ; il n'y a ni recalcul ni reprise automatique. Pour le coût, la portée est fixée par **M-05=A** (ci-dessous) : le pas n'est non exécutable que s'il n'est plus payable (P6 l.50).

**Coût réel d'un pas — M-05=A** [VAL] (P6 l.45) : « Si le coût augmente mais reste payable et que le passage est admissible, le pas est exécuté. » Statut : « règle validée » (P6 l.56). Application (P6 l.48-55) :
- avant chaque pas, son coût réel en TU et en énergie est vérifié ;
- si les deux ressources suffisent et que le passage reste admissible, le pas est exécuté et débité à son coût réel ;
- si le pas n'est plus payable, ou s'il devient physiquement inadmissible, l'ordre est interrompu selon Q3.4 et Q4.21 ;
- aucun pas non commencé n'est débité ; le coût des pas déjà effectués est conservé ;
- aucun recalcul automatique du trajet n'est créé.

La simple augmentation du coût prévu ne suffit donc plus à interrompre l'ordre, lorsque le pas reste admissible et payable. Le point du registre « notamment en cas d'augmentation imprévue du coût » (R:166) est donc tranché sur ce point [DÉD] : c'est une conséquence de M-05=A, que P6 n'énonce pas (OB-02).

**Restent ouverts** [OUV] : le repli d'une diagonale sur le passage Y ; les conditions de la surveillance et des réactions.

## 7. Choix du chemin

- **G4** [INS] (R:142-147) : TU minimales, puis énergie minimale, puis départage déterministe, sur l'état connu.
- **Q4.16=A** [CIT] (D:110) : après les TU et l'énergie, départage lexicographique déterministe des suites de directions N, NE, E, SE, S, SW, W, NW ; connexions spéciales départagées par identifiant stable ; aucune information cachée.
  - Le **sens** du départage par identifiant de connexion n'est pas fixé [OUV].
  - La priorité « X d'abord » relève de PNV-7.
- **Réserve** [OUV] : sur un graphe fini à coûts positifs ou nuls, le coût minimal existe et un chemin sans répétition l'atteint ; parmi ces chemins, le minimum lexicographique existe. La réserve porte sur les cycles gratuits (0 TU et 0 énergie), la terminaison de la recherche et le départage, si l'on admet des chemins avec répétition. La méthode est à choisir, comme l'algorithme.

## 8. Orientation, posture et réveil

- **Q4.17=A** [CIT] (D:111) : l'unité s'oriente vers le pas engagé, sans supplément de TU ni d'énergie ; le volume balayé par la rotation est contrôlé ; les rotations autonomes sont un autre sujet. La définition du volume balayé est [OUV].
- **Q4.18=A** [CIT] (D:112) : se coucher, s'agenouiller et se relever sont des actions distinctes, à coûts configurables et soumises à la validité physique ; la marche ne change jamais la posture automatiquement. Les seuils et la marche des autres postures sont [OUV].
- **G2** [INS] (R:135-140) et **Q4.19=A** [CIT] (D:113) :
  - au réveil sur une case occupée, l'unité va sur la première case voisine admissible dans l'ordre N, NE, E, SE, S, SW, W, NW, au même niveau, avec support, volume admissible et sans chevauchement intérieur avec une unité consciente ;
  - un corps inerte n'empêche pas ce repositionnement ;
  - à défaut, l'unité se réveille sur place, couchée, sans relèvement implicite ni nouvelle recherche automatique ;
  - le repositionnement ne coûte pas de TU de marche (G2).

  **Q4.19 tranche ainsi trois points** laissés ouverts par G2 (R:140) : le choix entre plusieurs voisines (par l'ordre), le statut d'une case portant un corps, et la posture « couché ».
- **Critères encore ouverts pour Q4.19** [OUV] : un mur ou une porte entre les deux cases ; une voisine en diagonale (N2, G1) ; l'état connu face à la vérité cachée ; l'orientation ; le dénivelé. L'ordre de traitement des réveils simultanés relève de PNV-8.

## 9. Modifications documentaires futures

Ces textes sont **proposés** pour un futur mandat d'inscription, qui devra couvrir explicitement MEC-0001 **et** MEC-0002 (rectificatif B3, §5). **Aucune inscription n'est autorisée.**

### 9.1 MEC-0002

**GE-02** (R:203)
- **Texte historique, conservé :** « Largeur de case et volumes des unités en proportions, sans mètres fixés. Hauteur d'étage : **3 m** fixes entre deux sols d'étages consécutifs, à distinguer de la montée d'un saut. [DS1.1 ; précisée par A3A…] Ouvert : largeur de case, volumes, rapport case/étage. »
- **Annotation proposée :**

  > *Annotation : texte historique conservé. La clause « largeur de case et volumes des unités en proportions, sans mètres fixés » est **modifiée** par B3 (addendum validé par le propriétaire le 19 novembre 2026 ; rectificatif validé le 20 novembre 2026) : la largeur de case et les volumes ont des valeurs métriques configurables, communes à `MEC-0001` et `MEC-0002`. Les dimensions physiques configurées sont exprimées en millimètres entiers ; les calculs physiques ne sont pas limités systématiquement aux entiers (arbitrage R-5 du 20 novembre 2026). Valeurs initiales : largeur de case 1 500 mm (Q1.5), épaisseur de mur standard 100 mm (Q1.7) — provenance à confirmer par archivage (B3-03). La hauteur de 3 000 mm entre les sols de référence de deux étages tactiques consécutifs est fixe, sans réglage global ni par carte ; les dénivelés locaux des supports restent possibles (Q4.1 ; confirmation du propriétaire et arbitrage R-6 du 20 novembre 2026). Q1.4 reste historique pour l'altitude des niveaux de référence (arbitrage R-7 du 20 novembre 2026).*

- **Nouvelle mention « Ouvert » proposée :** dimensions minimales ; tolérances géométriques ; modalités de conversion des dimensions configurées ; conventions d'arrondi autres que celle des enveloppes (Q2.6) ; précision numérique et arrondis des calculs physiques non spécifiés (rectificatif B3, §1 ; R-5=A) ; bornes des dénivelés locaux.
- *Le rapport case/étage n'est plus un paramètre distinct* [DÉD] : il découle de la largeur de case, configurable, et de la hauteur, fixe. Il vaut 0,5 avec les valeurs initiales ⟨B3-03⟩.

**GE-03** (R:204)
- **Texte historique, conservé :** « Chaque type d'unité a un volume de collision rectangulaire configurable en 3D. Les postures debout, agenouillé et couché modifient ce volume. […] Ouvert : dimensions par type et posture. »
- **Annotation proposée :**

  > *Annotation : texte historique conservé. **Précisée** par B3-03 : chaque type d'unité possède des dimensions physiques configurables, dépendant de sa posture ; les dimensions et orientations pertinentes sont communes aux deux mécaniques ; GE-04 reste applicable. Profil humain initial (Q1.6) : debout 600 × 600 × 1 800 mm, agenouillé 600 × 600 × 1 200 mm, couché 1 200 × 600 × 500 mm — provenance à confirmer par archivage (B3-03). **Précisée explicitement par Q1.2** (arbitrage R-8 du 20 novembre 2026 : « Q1.2 précise explicitement GE-03, avec géométrie commune aux deux mécaniques ») : dimensions configurables par type d'unité et posture ; le volume peut dépasser sa case ; les collisions restent obligatoires ; le même volume physique sert à `MEC-0001` et à `MEC-0002`. Les dimensions configurées sont exprimées en millimètres entiers (arbitrage R-5).*

- **Nouvelle mention « Ouvert » proposée :** dimensions des autres types d'unités ; dimensions minimales ; orientations admises.
- **Inscription :** GE-03 est explicitement à annoter lors d'une future inscription (R-8=A, P6 l.104). Cette validation ne modifie pas à elle seule le registre sur `main` (P6 l.106).

**« Encore ouvert », ligne Géométrie** (R:336)
- **Texte actuel :** « Géométrie : largeur de case et rapport case/étage (la hauteur d'étage est fixée à 3 m) ; dimensions des unités par type et par posture ; épaisseur des surfaces ; tolérance des contacts. »
- **Texte proposé :**

  > Géométrie : le principe de dimensions métriques configurables, communes à `MEC-0001` et `MEC-0002`, est décidé (B3) ; valeurs initiales de la largeur de case, de l'épaisseur des murs et du profil humain : Q1, provenance à confirmer par archivage ; dimensions configurées en millimètres entiers, calculs physiques non limités systématiquement aux entiers (arbitrage R-5) ; hauteur d'étage fixe de 3 000 mm entre sols de référence, sans réglage global ni par carte (GE-02, Q4.1, arbitrage R-6). Restent ouverts : dimensions des autres types d'unités ; dimensions minimales ; épaisseur des surfaces ; tolérance des contacts ; modalités de conversion ; conventions d'arrondi ; précision et arrondis des trajectoires, vitesses, hauteurs équivalentes et autres calculs physiques.

**Règles précisées, à annoter :**
- GE-07 et CH-14 (R:208, R:255) par Q4.5 [CIT] : conversion Force → kg configurable par type, commune aux deux fiches ; valeurs ouvertes ;
- EN-06 (R:310) par Q4.4 [CIT] : file par identifiant croissant ;
- ES-09 et ES-10 (R:286-287) : coûts de terrain fournis par Q3 [TR] ; aucune énergie ajoutée à l'esquive (G3 [INS]).

**Règles inchangées :**
- GE-04, GE-05, CO-01 et les règles de dégâts ;
- CH-08, compatible par conversion (3 m = 3 000 mm ; rectificatif §1). La contrainte d'entiers vaut pour les dimensions configurées (R-5=A) ; elle n'est pas étendue aux calculs physiques, ni de MEC-0001 ni de MEC-0002 (R-5=A ; rectificatif §1) ;
- ES-08, ES-11, ES-12, RP-03, RP-05 et les sauts : l'admissibilité d'une case portant un corps reste du ressort de MEC-0002.

### 9.2 MEC-0001

- **Nouveau bloc daté** des décisions Q1 à Q5 et B3, et des six arbitrages du 20 novembre 2026 (§2 bis), au niveau de preuve indiqué au §12, avec mention de leur provenance.
- **Annotations des règles inscrites qui sont précisées :** S10 (Q5.2), ARB-C, ARB-D (Q3.14, Q4.6 ; M-04=B), N14 (M-04=B : point d'articulation, §5), ARB-E (Q4.13, Q5.1), G2 (Q4.19), G3 (Q3 ; M-05=A), G4 (Q4.16).
- **Actualisation de la liste « Encore ouvert »** selon le §10.
- **R:115** dit encore que la v1.4.1 et le mandat d'inscription « ne sont pas archivés dans le dépôt ». Ils le sont depuis le commit `1ecc608` (PR n° 15) : la phrase est à actualiser.

## 10. Points ouverts du registre tranchés ou précisés

| Point du registre | Tranché ou précisé par | Ce qui reste ouvert |
|---|---|---|
| R:151 : géométrie, portes, taille des unités | Q1.1, Q1.3, Q1.5, Q1.7, Q2.5 ; Q1.2, Q1.6 ; Q4.7 ; R-5=A, R-8=A | définition d'un passage « bloqué » pour N2 ; trajectoire (PNV-6, PNV-7) ; tolérance |
| R:152 : coûts | Q3.1, Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.3, Q3.10 | coûts de chaque connexion ; autres terrains |
| R:153 : escaliers, échelles, ascenseurs | Q2.1 à Q2.4 | profils de connexions |
| R:160 : surcharge | Q3.14 ; Q4.5 ; M-04=B (principe d'un effet sur l'énergie) | table Force → kg ; autres pénalités ; indicateur « encombré » ; modalités de l'effet sur l'énergie |
| R:161 : capital et récupération | Q4.6 (valeurs initiales de test) | valeurs des autres types d'unités |
| R:162 : calcul de chemin | Q4.16 | algorithme ; cycles gratuits ; sens du départage par connexion |
| R:163 : orientation, énergie, interruptions | Q4.17 ; Q3.6, Q3.7 à Q3.9, Q3.11, Q4.6 ; Q4.20 ; Q5.1 | rotations autonomes ; surveillance |
| R:166 : trajet devenu non payable | Q4.21, Q3.4 ; M-05=A (coût plus élevé mais encore payable) | repli d'une diagonale sur le passage Y (§6) |
| R:167 : propositions du LOT-2B | précisées par Q3.4 et Q3.13 | instant exact du débit |
| G1, « Ouvert » (R:134) | Q1.2, Q1.5, Q1.6 ; Q1.1 ; Q1.3, Q1.7 ; Q3.9 | trajectoire, sous-segments, tolérance, événements |
| G2, « Ouvert » (R:140) | Q4.19 (trois points) ; Q4.18 | critères du §8 ; contacts pendant la coexistence |
| G3, « Ouvert » (R:141) | Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.6, Q3.11, Q4.6 ; M-05=A | coûts de chaque connexion (Q3.10=B) |
| G4, « Ouvert » (R:147) | Q4.16 | algorithme ; sens du départage par connexion |
| ARB-C à ARB-E, « Ouvert » (R:123-125) | Q2, Q3.3, Q3.10, Q4.7 ; Q3.14, Q4.5, Q4.6, M-04=B ; Q5.1, Q4.13 | détails d'interaction ; table Force → kg ; modalités de l'effet de la surcharge sur l'énergie ; surveillance |
| MEC-0002 | voir le §9.1 | — |

## 11. Rapport à OXCE

Ce tableau se limite aux comportements documentés par le LOT-2A (lecture du code, sans exécution) ou vérifiés dans le code au commit `441cae1b`. **Aucune fidélité n'est affirmée.**

| Décision | Rapport | Référence |
|---|---|---|
| Q3.7 à Q3.9, G3 | **Écart de principe** : OXCE fait coûter la marche 100 % des TU et 50 % en énergie, tronqué. Bastion a un barème propre et un multiplicateur indépendant. Les valeurs initiales coïncident avec ⌊TU/2⌋, sauf la diagonale difficile (5 contre 4) : c'est une coïncidence. | LOT-2A §2, ligne 6 |
| Q3.7 | Valeur coïncidente : OXCE prend une base de 4 TU quand le coût de la case est nul. | LOT-2A §2, ligne 5 |
| Q4.20 | **Écart** : OXCE arrête la marche quand un nouvel ennemi est repéré. | LOT-2A §2, ligne 16 |
| ARB-E, Q5.1 | Concordance de principe : OXCE arrête la marche sur un tir de réaction. La frontière du pas n'a pas été étudiée. | LOT-2A §2, ligne 16 |
| Q4.21 | Concordance de principe : OXCE arrête si le pas suivant devient impossible. | LOT-2A §2, ligne 16 |
| ARB-C, Q4.7 | **Écart établi** : OXCE ouvre les portes au passage. Cette lecture vient du rapport d'inscription du 17 novembre, pas du LOT-2A. | R:123 ; `src/Battlescape/UnitWalkBState.cpp:337-354` |
| G4 | **Écart établi**, par inférence : le chemin le moins coûteux n'est pas garanti. | R:142-147 ; LOT-2A §2, ligne 14 |
| Q4.16 | **Non comparé** : le LOT-2A classe le départage des égalités comme non vérifié. | LOT-2A §2, ligne 14 |
| ARB-D, Q3.14 | **Concordance d'ordre** : ajout au solde avec plafond au maximum (`setValueMax`, l.2714), puis rapport Force / poids appliqué au total, quand ce rapport est inférieur à 1 (l.2717-2720). **Différence de calcul** : OXCE calcule le rapport et le produit en nombres flottants ([code OXCE retiré — D4] puis [code OXCE retiré — D4]) et tronque ce résultat flottant ; Q3.14 exige le plancher de la valeur mathématique exacte. Les résultats ne sont pas garantis identiques : une émulation en simple précision de 1/41 × 41 donne 0,99999994, tronqué à 0, contre 1 en valeur exacte. C'est une émulation, non une exécution d'OXCE. Aucune équivalence numérique n'est affirmée. | R:111 ; `src/Savegame/BattleUnit.cpp:2714-2720`, vérifié au commit `441cae1b` |
| Autres décisions, dont les six arbitrages du §2 bis | non étudiées | — |

## 12. Matrice de traçabilité

Statuts : **V** en vigueur (validée, non inscrite) ; **I** inscrite ; **H** historique ; **N** non validée.

**Rattachement d'un scénario** (M-03) : un scénario n'est rattaché à une décision que s'il la cite dans ses sources et que son résultat attendu dépend d'elle. Sinon : « aucun scénario dédié ».

| ID | Formulation retenue (résumé) | Source exacte | Preuve | Statut | Registre concerné | Scénarios | Réserves |
|---|---|---|---|---|---|---|---|
| Q1.1 | largeur uniforme par carte, configurable, paire, en mm | P1 l.300-301, 309 ; P5 l.14 | [TR-M] | V | GE-02, R:151, G1 | T26 | ⟨B3-03⟩ ; proposition restituée en deux messages (§0.1) |
| Q1.2 | dimensions par type et posture ; dépassement de case ; collisions obligatoires | P1 l.302-303, 309 ; P5 l.15 | [TR-M] | V | GE-03 (précision explicite, R-8=A), G1 | T26 | proposition restituée en deux messages (§0.1) |
| Q1.3 | épaisseur par type de mur ; volume physique | P1 l.304-305, 309 ; P5 l.16 | [TR-M] | V | R:151 | T26 | proposition restituée en deux messages (§0.1) |
| Q1.4 | altitude configurable par niveau | P1 l.306-307, 309 ; P5 l.17 | [TR-M] | **H** (altitude des niveaux de référence ; R-7=A) | GE-02 | aucun (historique ; T27 vérifie la règle qui la supplante) | supplantée par Q4.1, W-01 et R-6=A ; portée résiduelle : R-7=A ; proposition restituée en deux messages ; libellé A au passé (§0.1) |
| Q1.5 | case de 1 500 mm | P1 l.11-17, 67 | [TR] | V, valeur initiale configurable | GE-02 | T26 | ⟨B3-03⟩ |
| Q1.6 | profil humain | P1 l.19-29, 67 | [TR] | V, valeur initiale configurable | GE-03 | T26 | ⟨B3-03⟩ |
| Q1.7 | mur standard de 100 mm | P1 l.31-37, 67 | [TR] | V, valeur initiale configurable | GE-02 | T26 | ⟨B3-03⟩ |
| Q1.8 | 3 000 mm | P1 l.39-45, 55, 67 | [TR] | valeur en vigueur, fixe (W-01, R-6=A) ; cadre configurable **H** | GE-02, CH-08 | T27 | — |
| Q1.9 | ressauts de 200 / 300 mm (humain debout) | P1 l.47-53, 67 | [TR] | V, valeur initiale configurable | — | T04 | ⟨B3-03⟩ ; bornes [OUV] |
| Q2.1 | escaliers : connexions explicites | P1 l.71-75, 111 | [TR] | V | N4, ARB-C | T40 | profils [OUV] |
| Q2.2 | rampes : passages entre supports horizontaux | P1 l.77-81, 111 | [TR] | V | N4, ARB-C | T40 | idem |
| Q2.3 | échelles : action spécifique | P1 l.83-87, 111 | [TR] | V | N4, ARB-C | T40 | idem |
| Q2.4 | ascenseurs : plateforme à états | P1 l.89-93, 111 | [TR] | V | N4, ARB-C | aucun dédié | idem |
| Q2.5 | mur centré | P1 l.97-101, 111 | [TR] | V | R:151 | T26 | — |
| Q2.6 | enveloppe paire supérieure | P1 l.103-107, 111 | [TR] | V | CO-01 (inchangée) | T26 | — |
| Q3.1 | barème par terrain, coût d'entrée | P1 l.115-119, 165 | [TR] | V | S2, R:152 | T02, T22 | case d'arrivée : [DÉD] |
| Q3.2 | multiplicateur d'énergie configurable et indépendant | P1 l.121-127, 165 | [TR] | V | S2 | T02 | — |
| Q3.3 | coût par connexion | P1 l.129-133, 165 | [TR] | V | ARB-C | aucun dédié | — |
| Q3.4 | vérifier avant chaque pas | P1 l.135-139, 165 | [TR] | V | S8, S9 | T08, T47 | — |
| Q3.5 | événements simultanés sur le trajet | P1 l.141-145, 165 | [TR] | V | EN-06 (MEC-0002) | aucun dédié | — |
| Q3.6 | réserve d'énergie plafonnée | P1 l.147-151, 165 | [TR] | V | G3 | aucun scénario dédié | valeurs : Q4.6 |
| Q3.7 | 4 TU et 2 d'énergie | P1 l.171-177, 213 | [TR] | V, valeur initiale configurable | G3 | T01 | — |
| Q3.8 | +50 % et +100 % | P1 l.179-183, 213 | [TR] | V, valeur initiale configurable | G3 | T02, T18 | — |
| Q3.9 | énergie de la diagonale × 1,5, arrondi supérieur | P1 l.185-191, 213 | [TR] | V, valeur initiale configurable | G3 | T02 | — |
| Q3.10 | pas de barème universel « pour l'instant » | P1 l.193-197, 213 | [TR] | V | ARB-C | aucun dédié | — |
| Q3.11 | valeurs à calibrer | P1 l.199-203, 213 | [TR] | V | G3 | — | valeurs de test : Q4.6 |
| Q3.12 | pas de surcoût universel de mur | P1 l.205-209, 213 | [TR] | V | S2, R:152 | T06 | — |
| Q3.13 | ordre des arrondis | P1 l.219-243, 293 | [TR] | V | S2 | T02, T18, T19 | — |
| Q3.14 | formule de surcharge | P1 l.245-289, 293 | [TR] | V | ARB-D, N14 | T20, T21 | table Force → kg [OUV] ; effet sur l'énergie : M-04=B, modalités [OUV] |
| Q4.1 | 3 m fixes entre sols de référence | v0.2 l.181 ; D:86 ; P3 l.88 ; P6 l.73 | [CIT] + [CONF] + [VAL] | V | GE-02, CH-08 | T27 | — |
| Q4.2 | contact non bloquant | v0.2 l.181 ; D:87 | [CIT] | V | GE-05 | T30 | tolérance [OUV] |
| Q4.3 | perte de support immédiate | v0.2 l.183 ; D:88 | [CIT] | V | EN-03 | T15 | support pendant le pas [OUV] |
| Q4.4 | file des chutes | v0.2 l.183 ; D:89 | [CIT] | V | EN-06, EN-07 | T16 | — |
| Q4.5 | Force → kg par type | v0.2 l.185 ; D:93 | [CIT] | V | GE-07, CH-14 | T31 | valeurs [OUV] |
| Q4.6 | 60 / 60 / 100 / 20 (valeurs de test) | v0.2 l.185 ; D:94 ; P2 l.18 | [CIT] + [DÉC] | V | ARB-D | T01 | T21 écarte ce profil (§13, T21) |
| Q4.7 | porte à 4 TU / 0 énergie (valeurs de test) | v0.2 l.185 ; D:95 ; P2 l.18 | [CIT] + [DÉC] | V | ARB-C | T06 | — |
| Q4.8 | occupation des connexions | v0.2 l.185 ; D:96 | [CIT] | V | ARB-C | T25 | — |
| Q4.9 | interruption du transfert | v0.2 l.185 ; D:97 | [CIT] | V | ARB-C | T11b | — |
| Q4.10 | état suspendu | v0.2 l.187 ; D:101 | [CIT] | V | ARB-C | T12 | reprise [OUV] |
| Q4.11 | paiement à l'engagement | v0.2 l.187 ; D:102 | [CIT] | V | ARB-C | T11b, T12 | — |
| Q4.12 | reprise et retour | v0.2 l.189 ; D:103 | [CIT] | V | ARB-C | T12, T13 | retour partiel [OUV] |
| Q4.13 | tir en transfert | v0.2 l.189 ; D:104 | [CIT] | V | ARB-E | T11b | — |
| Q4.14 | incapacité et support | v0.2 l.189 ; D:105 | [CIT] | V | EN-03, EN-08 | T11a (c), T14 | — |
| Q4.15 | capacité d'une connexion | v0.2 l.189 ; D:106 | [CIT] | V | S10 (sans exception) | T24, T25 | transit partagé [OUV] |
| Q4.16 | départage du chemin | v0.2 l.191 ; D:110 | [CIT] | V | G4 | T05, T33 | sens par connexion [OUV] ; PNV-7 |
| Q4.17 | orientation | v0.2 l.191 ; D:111 | [CIT] | V | « Encore ouvert » R:163 | T28 | volume balayé [OUV] |
| Q4.18 | postures | v0.2 l.191 ; D:112 | [CIT] | V | GE-03 | T29 | autres postures [OUV] |
| Q4.19 | réveil | v0.2 l.191 ; D:113 | [CIT] | V | G2, ARB-B | T10, T36 | critères [OUV] |
| Q4.20 | révélation | v0.2 l.191 ; D:114 | [CIT] | V | S8, S11 | T07 | — |
| Q4.21 | imprévu | v0.2 l.191 ; D:115 | [CIT] | V | S8, S9, G3 | T08, T47 | cas du coût précisé par M-05=A |
| Q5.1 | tir de réaction pendant un pas | P2 l.28-32, 70-82 | [DÉC] | V | ARB-E | T11a, T38, T39 | options d'origine absentes |
| Q5.2 | occupation d'une plateforme | P2 l.34-38, 83-95 | [DÉC] | V | S10 | T24 | emplacement / case [OUV] |
| B3 | géométrie commune | P2 l.121-201 | [DÉC] | V | GE-02, GE-03 | aucun scénario dédié | options d'origine absentes |
| Rectificatif B3 | unités, hauteur, ouverts, configurations, inscription | P2 l.207-257 ; validation P3 l.100-101 | pièce : « proposition » ; [CONF] W-12 | V | GE-02, GE-03, CH-08 | — | — |
| Confirmation W-01 | hauteur fixe, non configurable par carte | P3 l.88 ; consigne P3 l.15 | [CONF] | V | GE-02 | T27 | — |
| M-04=B | la surcharge peut aussi réduire l'énergie ; modalités à définir | P6 l.30-42 | [VAL] | V (principe) ; modalités **ouvertes** | ARB-D, N14 | aucun scénario spécifiable (modalités ouvertes) | options d'origine absentes |
| M-05=A | coût accru mais payable, passage admissible : pas exécuté à son coût réel | P6 l.43-56 | [VAL] | V | G3, Q3.4, Q4.21 ; R:166 | T47 | options d'origine absentes |
| R-5=A | dimensions configurées en mm entiers ; calculs non limités systématiquement aux entiers | P6 l.57-70 | [VAL] | V ; modalités techniques **ouvertes** | GE-02, GE-03, CH-08 ; PNV-2 | T48 | conversion et précision [OUV] ; options d'origine absentes |
| R-6=A | 3 000 mm fixes, ni réglage global ni par carte | P6 l.71-82 | [VAL] | V | GE-02, CH-08 | T27 | options d'origine absentes |
| R-7=A | Q1.4 historique pour l'altitude des niveaux de référence ; variations locales de support | P6 l.83-93 | [VAL] | V | GE-02 | T27 | options d'origine absentes |
| R-8=A | Q1.2 précise explicitement GE-03 ; géométrie commune | P6 l.94-107 | [VAL] | V | GE-03 | aucun scénario dédié | options d'origine absentes ; annotation de GE-03 à l'inscription |
| PNV-1 à PNV-9 | formulations sans source suffisante (PNV-2 en partie tranchée par R-5=A) | v0.2, D:29-40 | aucune | **N** | — | T04, T15, T26 (conditionnels) | — |

## 13. Scénarios de vérification (non exécutés)

Statut : **Sp** spécifiable ; **Pa** partiel, dépendance indiquée ; **Ou** ouvert. Les valeurs « fictives » sont des données de test.

Sauf mention contraire :
- profil initial de test : 60 TU et 100 d'énergie (Q4.6) ;
- barème du §5 ;
- terrain normal ;
- aucun mur ni unité.

| ID | Situation | Résultat attendu | Sources | Statut |
|---|---|---|---|---|
| T01 | un pas orthogonal | 4 TU et 2 d'énergie ; il reste 56 et 98 | Q3.7, G3, Q4.6 (profil 60 / 100) | Sp |
| T02 | une diagonale en terrain difficile, passage praticable | 9 TU et 5 d'énergie ; il reste 51 et 95 (la loi d'OXCE donnerait 4 d'énergie) | Q3.1, Q3.2, Q3.8, Q3.9, Q3.13, S2 | Sp |
| T03 | diagonale permise par N2 ; une unité consciente bloque le seul passage ouvert | refus, sans débit | ARB-A, G1, Q3.4 | Pa (géométrie laissée ouverte par G1 : R:134) |
| T04 | ressauts de +150 mm et −250 mm ; puis exactement +200 / −300 mm ; puis au-delà | +150 / −250 : admis si le volume et le support sont valides. Exactement aux seuils et au-delà : non spécifiable | Q1.9 | Pa (bornes [OUV] ; au-delà : PNV-5) ⟨B3-03⟩ |
| T05 | destination à deux cases à l'est et une au nord ; [NE, E] et [E, NE] coûtent chacun 10 TU et 5 d'énergie | [NE, E] | Q4.16, G4 | Sp (sur la formulation résumée de Q4.16) |
| T06 | porte ordinaire fermée | ouverture explicite à 4 TU et 0 énergie ; aucun pas automatique ; aucune ouverture pendant la marche | Q4.7, ARB-C, Q3.12 | Sp |
| T07 | ennemi caché révélé hors du trajet, sans tir | la marche continue | Q4.20 | Sp |
| T08 | obstacle inconnu devant le pas suivant | arrêt ; révélation ; pas suivant non débité ; pas de reprise automatique | Q3.4, Q4.21, S8, S9 | Sp |
| T09 | corps sur la case de destination | traversée et arrêt possibles ; pas d'impact dû au seul chevauchement | ARB-B | Sp |
| T10 | réveil sur une case occupée : (a) N libre ; (b) N occupée, NE libre ; (c) aucune voisine | (a) N ; (b) NE ; dans les deux cas, aucune TU de marche ; (c) couché sur place, sans se relever tant que la case est occupée | G2, Q4.19 | Pa (critères [OUV]) |
| T11a | trois pas orthogonaux ; un tir de réaction pendant le premier : (a) manqué ; (b) touche sans blesser, ou blesse sans incapacité ; (c) incapacité ou mort | (a) et (b) : premier pas achevé jusqu'à sa destination tactique admissible ; il reste 56 TU et 98 d'énergie ; ordre interrompu ; deuxième pas ni exécuté ni débité. (c) : interruption, puis contrôle du support | Q5.1, ARB-E, Q4.14 | (a), (b) : Sp (tir simulé) ; (c) : Pa |
| T11b | tir de réaction manqué pendant un transfert | action interrompue ; position atteinte et coût conservés ; pas d'arrivée complétée | Q4.13, Q4.9, Q4.11 | Pa (profil de connexion) |
| T12 | transfert payé puis interrompu, unité soutenue | état suspendu ; reprise dans le même sens non refacturée | Q4.10 à Q4.12 | Pa (profil de connexion) |
| T13 | retour vers l'entrée depuis un état suspendu | nouvelle action, nouveau coût | Q4.12 | Pa (chemin et coût du retour) |
| T14 | plateforme soutenant une unité devenue inconsciente | pas de chute automatique | Q4.14 | Sp |
| T15 | support détruit pendant un pas engagé | arrêt immédiat à la position physique courante ; relais à MEC-0002 ; pas engagé débité | Q4.3 | Pa (support pendant le pas, [OUV] et PNV-6) |
| T16 | trois chutes nées d'un même événement, puis une chute secondaire | file par identifiant croissant ; chute secondaire en fin de file ; revalidation selon EN-07 | Q4.4 | Sp |
| T17 | esquive de MEC-0002 | coût habituel de la marche en TU ; aucune énergie | ES-09, ES-10, G3 | Sp |
| T18 | base fictive de 3 TU et 1 d'énergie, terrain difficile | orthogonal : 5 TU et 2 d'énergie ; diagonal : 7 TU et 3 d'énergie (option A). L'option B, écartée, ne fixe pas son arrondi final : elle n'est pas un résultat attendu | Q3.8, Q3.13 | Sp |
| T19 | coût d'arrivée fictif de 5 TU, pas diagonal | 7 TU | S2, Q3.13 | Sp |
| T20 | surcharge, valeurs fictives : capacité 30 kg, charge 40 kg, total 60 ; charge nulle ; total 22, capacité 15, charge 22 | 45 ; 60 ; 15 (calcul exact ; un calcul flottant naïf donne 14) | Q3.14 | Sp |
| T21 | plafond d'ARB-D, valeurs fictives avec un maximum de 20 : (7, 15, facteur 0,75) ; (2, 15, sans surcharge) ; (4, 12, 0,75) ; (total 20, facteur 30/45). **Pourquoi un maximum fictif de 20** : avec le profil Q4.6, min(solde + 60, 60) = 60 pour tout solde positif ou nul ; le plafond serait toujours atteint, et ce profil ne distinguerait pas ARB-D d'une simple remise au maximum. Avec 20, les cas exercent un plafond atteint (7 + 15 = 22, ramené à 20), un plafond non atteint (2 + 15 = 17 ; 4 + 12 = 16), la réduction appliquée après le plafond, et l'arrondi inférieur (20 × 30/45 = 13,33…) | 15 ; 17 ; 12 ; 13 | ARB-D, Q3.14 | Sp |
| T22 | carte de 2 × 2 cases ; arrivée en terrain normal ; cases intermédiaires difficiles ; 20 TU et 2 d'énergie, puis 3 d'énergie | diagonale : 6 TU et 3 d'énergie ; détours : 10 TU et 5 d'énergie. Avec 2 d'énergie, destination hors zone ; avec 3, la diagonale seule est admissible | G3, Z1, Q3.1 (coût d'entrée de la case d'arrivée) | Sp (passages praticables) |
| T23 | candidats injectés A (17 TU, 11 d'énergie) et B (18 TU, 2 d'énergie) ; budget 20 / 12, puis 20 / 10 | A, puis B | G4 | Sp (sélection abstraite) |
| T24 | plateforme à deux emplacements, capacité 2, deux unités conscientes ; plateforme à un emplacement, deuxième unité | admises ; deuxième unité refusée ; jamais deux unités conscientes sur une même case, hors de l'exception transitoire au réveil de G2, absente du scénario | Q5.2, Q4.15, S10 | Pa (correspondance emplacement / case [OUV]) |
| T25 | capacité d'une connexion déjà atteinte | admission refusée | Q4.15, Q4.8 | Sp |
| T26 | géométrie initiale | largeur intérieure de 1 400 mm ; enveloppe à 45° de 850 mm debout ; de 1 274 mm couché ; le profil ne dépasse pas sa case | Q1.1 à Q1.3, Q1.5 à Q1.7, Q2.5, Q2.6 | Pa (1 274 mm : PNV-3 ; « le profil ne dépasse pas sa case » : PNV-4) ⟨B3-03⟩ |
| T27 | deux étages tactiques consécutifs, sur deux cartes différentes | 3 000 mm entre sols de référence sur chacune ; aucun réglage global, par carte ni par niveau de cette hauteur ou de l'altitude de référence ; les dénivelés locaux des supports restent distincts et possibles | GE-02, Q1.8, Q4.1, W-01, R-6=A, R-7=A | Sp |
| T28 | pas après une orientation opposée | aucun supplément (4 TU et 2 d'énergie) | Q4.17 | Pa (volume balayé) |
| T29 | ordre de marche à une unité agenouillée | aucun changement automatique de posture | Q4.18 | Pa (marche des autres postures) |
| T30 | deux volumes tangents, **sans composante de vitesse dirigée vers la surface** | marche permise ; contact détecté ; aucun dégât d'impact normal | Q4.2, GE-05 | Sp |
| T31 | même unité, surcharge de MEC-0001 et seuil CH-14 | même capacité Force → kg | Q4.5, CH-14 | Pa (table [OUV]) |
| T32 | destination choisie dans la zone, sans imprévu | atteinte ; TU et énergie dépensées inférieures ou égales aux budgets | G3, Z1 | Sp |
| T33 | deux chemins de même coût ne différant que par la connexion | choix déterministe par identifiant stable ; le sens n'est pas fixé ; seul le déterminisme est vérifiable | Q4.16 | Pa (sens [OUV]) |
| T34 | cycle de connexions à 0 TU et 0 d'énergie | recherche qui se termine ; résultat déterministe | G4, Q4.16 | Ou (méthode) |
| T35 | ennemi repéré puis perdu de vue | aucun repère persistant | S12 | Sp (visibilité simulée) |
| T36 | réveil ; la seule voisine libre porte un corps | repositionnement sur cette case | Q4.19, ARB-B | Pa (critères [OUV], comme T10) |
| T37 | candidats injectés A (18 TU, 10 d'énergie) et B (18 TU, 9 d'énergie) ; budget 20 / 12 | B (second critère de G4) | G4, Q4.16 | Sp (sélection abstraite) |
| T38 | un surveillant déjà visible pivote sans tirer ; aucune révélation ni autre événement pendant le pas | la marche n'est pas interrompue | ARB-E, Q5.1 | Sp (pivot simulé) |
| T39 | plusieurs tirs de réaction contre la même unité pendant un pas | pas achevé, débité une seule fois (4 TU et 2 d'énergie) ; ordre interrompu | Q5.1, ARB-E | Sp pour la comptabilité ; ordre des réactions [OUV] |
| T40 | aucune connexion valide vers l'étage supérieur | aucune marche ordinaire n'atteint cet étage | ARB-C, Q2.1 à Q2.3 | Sp en principe (représentation des connexions [OUV]) |
| T41 | les deux passages orthogonaux fermés par des murs pleins | diagonale refusée | N2, S3 | Sp (murs pleins) |
| T42 | passage physiquement libre seulement par une case jamais explorée | ce passage n'est pas utilisé | S7, G1 | Pa (sous-segments, laissés ouverts par G1 : R:134) |
| T43 | un passage fermé, l'autre ouvert avec une unité consciente ; volumes fictifs étroits et trajectoire sans contact | diagonale exécutée en un seul pas (6 TU et 3 d'énergie) ; l'unité voisine n'est pas traitée comme un mur | S4, N2, G1, ARB-A | Pa (géométrie et trajectoire, laissées ouvertes par G1 : R:134 ; **pas** PNV-7) |
| T44 | destination à deux pas orthogonaux (8 TU et 4 d'énergie) avec 5 TU et 100 d'énergie | hors zone, sélection refusée, aucun pas ; il reste 5 TU et 100 d'énergie (l'ancienne règle S5 aurait fait un pas, laissant 1 TU) | Z1, G3 | Sp |
| T45 | un passage fermé par un mur, l'autre ouvert et praticable, sans unité | un seul pas diagonal (6 TU et 3 d'énergie) ; il reste 54 et 97 | G1, S2, Q3.13 | Sp (passage supposé praticable, comme T02 et T22) ; test intégré de la géométrie : Pa |
| T46 | un corps dans le seul passage ouvert | le corps ne rend pas ce passage impraticable ; diagonale possible au tarif d'un seul pas, si elle l'est sans le corps | ARB-B, G1 | Pa (géométrie laissée ouverte par G1 : R:134) |
| T47 | trois pas orthogonaux prévus en terrain normal ; avant le deuxième pas, son coût réel devient 6 TU et 3 d'énergie (terrain difficile ; coût réel simulé). (a) profil Q4.6 ; (b) valeurs fictives : 12 TU et 100 d'énergie à la sélection, de sorte que le trajet connu (12 TU et 6 d'énergie) est sélectionnable (Z1, G3) | (a) le deuxième pas est exécuté et débité à son coût réel ; l'ordre continue, sans recalcul du trajet ; il reste 46 TU et 93 d'énergie après le troisième pas. (b) après le premier pas, il reste 8 TU et 98 d'énergie ; le deuxième pas, à 6 TU et 3 d'énergie, reste payable : il est exécuté, il reste 2 TU et 95 d'énergie ; le troisième pas (4 TU) n'est plus payable : arrêt avant ce pas, sans débit ; il reste 2 TU et 95 d'énergie | M-05=A, Q3.4, Q4.21, G3, Z1, Q3.8 | Sp (coût réel simulé) |
| T48 | (a) dimensions configurées : largeur de case 1 500 mm, mur de 100 mm ; puis une dimension configurée de 600,5 mm. (b) volume fictif de 600 × 605 mm, orienté à 45° | (a) 1 500 et 100 mm sont conformes ; 600,5 mm ne l'est pas, et son traitement (refus ou conversion) n'est pas spécifié. (b) étendue horizontale de 1 205/√2 = 852,06… mm, non arrondie avant Q2.6 ; enveloppe de **854 mm**. Un arrondi préalable au millimètre le plus proche, ou inférieur, donnerait 852, qui ne contient pas le volume ; un arrondi supérieur donnerait 853, puis 854 | R-5=A, Q2.6 | (a) Pa (modalités de conversion [OUV]) ; (b) Sp |

**Sort des cas de la v1.4.1** (§5 de `docs/reviews/BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md`).

Les sept cas demandés :

| Cas | Sort | Dans la v0.4 |
|---|---|---|
| P0-10 | repris (sélection abstraite) | T37 |
| E-04 | repris | T38 |
| E-05 | repris ; débit adapté au barème Q3 | T39 |
| C-02 | repris | T40 |
| G1-01 | adapté : murs pleins seulement (la v1.4.1 vise des passages « fermés par terrain/murs », l.169) | T41 |
| G1-04 | repris | T42 |
| G1-05 | adapté ; dépendance corrigée : géométrie et praticabilité du trajet, non la priorité X puis Y | T43 |

Les autres cas :
- **Adaptés** au barème Q3, qui donne 2 d'énergie au pas orthogonal normal au lieu de 1 :
  - P0-01 → T01 ;
  - P0-02 → T44 ;
  - P0-03 → T22 ;
  - P0-04 → T02 ;
  - P0-05 → T21, comme valeur intermédiaire (7 + 15, plafonné à 20). Le résultat isolé de P0-05, 20 TU sans surcharge (v1.4.1 l.150), n'est pas conservé comme résultat attendu ;
  - P0-06 → T21, premier cas (20 × 0,75 = 15 ; v1.4.1 l.151) ;
  - P0-07, E-01, E-02 et E-03 → T11a ;
  - D-01 à D-04 → T21. D-04 vaut désormais 13, Q3.14 fixant l'arrondi.
- **Repris :**
  - P0-08 et G2-04 → T09 ;
  - P0-09 → T03 et T45 ;
  - G4-01 et G4-02 → T23 ;
  - G3-Z1 → T32 ;
  - S2-01 → T19 ;
  - S12-01 → T35 ;
  - C-01 → T06 ;
  - G1-02 → T45 ;
  - G1-03 → T03 ;
  - G1-06 → T46.
- **Remplacés :**
  - G4-03 → T05 et T33 ;
  - G2-01 à G2-03 → T10 (ordre de Q4.19).
- **Aucun cas des tableaux du §5 de la v1.4.1 n'est exclu.**
- **Anciens tests du LOT-2F** mentionnés au §5.5 de la v1.4.1 (T-M01 à T-M11, T-J, T-K, T-D) : non repris ici ; on se reporte à la v1.4.1, qui en fixe le sort.
- La matrice de la v1.4.1 reste un document historique.

## 14. Réserves et points ouverts

**Réserves documentaires :**
- **RD-1 — Archivage.** Aucune pièce du §15 n'est archivée dans le dépôt, sauf les numéros 7 à 11. C'est un préalable à toute inscription.
- **RD-2 — Formulations de Q4.** Ce sont des résumés de l'orchestrateur. Seuls sont confirmés les valeurs de Q4.6 et Q4.7 (P2 l.18) et le contenu de Q4.1 (confirmation W-01, P3 l.88 ; arbitrage R-6=A). Cela touche PNV-7 et PNV-8. Pour Q4.21, le cas du coût est désormais fixé par M-05=A.
- **RD-3 — Options d'origine absentes.** Pour Q5.1, Q5.2 et B3, et pour les six arbitrages du 20 novembre 2026 (§2 bis), seuls le choix et le texte validé sont transmis ; les textes des options ne le sont pas.
- **RD-4 — Neuf PNV**, qui ne valent pas règle.
- **RD-5 — Q1.1 à Q1.4.** Dossier composé de deux messages, classé [TR-M] (§0.1). La présence des options B dans la conversation d'origine, et l'existence de deux options seulement, reposent sur les déclarations du propriétaire. Restent aussi les réserves communes RD-1 et RD-6.
- **RD-6 — Copies.** Toutes les pièces sont des copies transmises, non authentifiées de façon indépendante. La copie P4 résume les sections 3 et 6 du rapport de revue. La copie P1 ne reproduit pas la partie « Mission » de JS-31 (2026-11-19T20:54:21Z ; M-16) ; c'est la seule omission relevée dans les copies P1, P2, P3, P5, P6 et P7 (§17, contrôle 7).
- **RD-7 — Revue.** La v0.4.1 et la v0.4.2 ont été revues de façon indépendante (pièces 13 et 13 bis : « conforme sous réserves » chacune). La v0.4.3 ne l'est pas encore : le contrôle indépendant de son diff relève d'une autorisation distincte (P7). Aucun test n'a été exécuté.
- **RD-8 — Réserves de la revue de la v0.4.1.** R-5 à R-8 sont tranchées par les arbitrages R-5=A à R-8=A. R-1 à R-4 restent couvertes par RD-1 à RD-6 ; R-9 (points ouverts) par la liste ci-dessous. R-10 (limites de cette revue) et R-11 (statut) demeurent.
- **RD-9 — Journal de session.** C'est un fichier local qui s'allonge à chaque échange, sans empreinte stable. L'attribution de ses entrées « user » au propriétaire repose sur l'outil de session. Les rapports RV41 et RV42 ne sont authentifiés que par leur empreinte (RV42, §5).
- **RD-10 — Pleine conformité.** Le message C, §E, subordonne un verdict « pleinement conforme » au « traitement documenté des anomalies, vérification des preuves de validation et nouvelle appréciation indépendante » (P2 l.114). La vérification des preuves suppose l'archivage (RD-1).

**Points ouverts** [OUV] :
- **Pas :** instant de l'engagement, c'est-à-dire déclenchement exact du débit d'un pas engagé ; support pendant les phases physiques du pas.
- **Chemin :** cycles gratuits, terminaison, départage ; sens du départage par identifiant de connexion ; algorithme.
- **Géométrie :**
  - bornes des dénivelés ; rattachement d'une case à un étage ;
  - inclusion des bornes de ressaut ; seuils et marche des autres postures ;
  - volume balayé par la rotation ; ensemble des orientations admises ;
  - modalités de conversion des dimensions configurées ; précision numérique et arrondis des grandeurs calculées non spécifiés, y compris dans MEC-0002 (R-5=A) ;
  - définition d'un passage « bloqué » pour N2 ; tolérance de GE-05 ;
  - dimensions minimales.
- **Occupation des connexions :** correspondance emplacement / case ; occupation pendant un transit partagé au regard de S10.
- **Réveil :** critères ouverts de Q4.19 ; ordre de traitement des réveils simultanés (PNV-8).
- **Imprévus :** repli d'une diagonale sur le passage Y. Le coût plus élevé mais encore payable est tranché par M-05=A.
- **Réserves RF reprises de la v0.2 :**
  - **RF-01 :** profils de connexions, y compris les coûts de chaque connexion (Q3.10=B), la reprise d'un transfert, le réveil dans une connexion et le retour partiel ;
  - **RF-02 :** postures et rotations autonomes ;
  - **RF-03 :** table Force → kg et données physiques des unités ;
  - **RF-04 :** cas limites des coûts ;
  - **RF-05 :** interfaces avec MEC-0002.
- **Surcharge :** modalités d'un effet sur l'énergie (M-04=B) : existence selon la situation, déclenchement, calcul, valeurs ; articulation de ces modalités avec N14 et ARB-D (OB-06, §5) ; autres pénalités ; indicateur « encombré ».
- **Autres :** conditions de surveillance (Overwatch) et de réaction.

**Hors périmètre :** équilibrage des autres unités, interface, animations, dégâts complets de chute et de collision, stabilité des bâtiments hors événements EN.

## 15. Inventaire des pièces justificatives

J'ai recalculé chaque empreinte pour la v0.4.3, avec `sha256sum` sur le fichier ou `git show origin/main:<chemin> | sha256sum`. Une pièce **n'est pas archivée** du seul fait qu'elle figure ici. Les numéros des versions précédentes sont conservés, pour que les renvois existants restent valables. Les messages sont désignés par leur identifiant JS-NN (tableau du §0).

**Pièces avec fichier et empreinte vérifiée :**

| N° | Pièce | Fichier | SHA-256 | Archivée dans le dépôt |
|---|---|---|---|---|
| 1 | Q1.1 à Q3.14. Intertitre « Message 1 » = JS-30 (2026-11-19T20:36:22Z), intégral : propositions et validations de Q1.5 à Q3.14. Intertitre « Message 2 » = JS-31 (2026-11-19T20:54:21Z) : options A et validation de Q1.1 à Q1.4 ; **partie « Mission » non reproduite** (M-16). La mention « reproduit tel que reçu » de P1 l.3 ne vaut donc pas pour la fin de JS-31. **P1 n'est pas modifiée ; elle est complétée par la pièce 1 bis** | copie P1, `PIECES-Q1-Q3-TRANSMISES.md` | `c9ee67cab4a96d4ab4902048426ae6fe34feb7dd23b9416768ee6ffba1c69063` | non |
| 1 bis | Options B de Q1.1 à Q1.4 : JS-35 (message I, 2026-11-20T13:41:45Z), intégral, et reconstitution par décision (compilation, l.39-48) | copie P5, `PIECE-Q1.1-Q1.4-OPTIONS-B.md` | `7e799d1c8ebd3a4486f28aaf34117709b76a92a11b68aa14c0296f44f0139777` | non |
| 2 | Messages A à E = JS-24 à JS-28 (2026-11-19, de 19:56:49Z à 20:13:09Z), intégraux : repères horaires de Q1 à Q3 et valeurs de Q4.6 et Q4.7 ; Q5.1 et Q5.2 ; addendum Q5 ; addendum B3 ; rectificatif B3 | copie P2, `PIECES-Q4-Q5-B3-DECLARATIONS.md` | `b69ba3b799608572363b1571ad1a9197a1c90af5e19c1b69f328de6a9a37b869` | non |
| 3 | Messages F, G et H = JS-32 à JS-34 (2026-11-19T20:59:24Z, 2026-11-19T21:08:57Z, 2026-11-20T12:53:14Z), intégraux : consignes pour la v0.3 ; mandat de revue de la v0.3 ; mandat de la v0.4, avec les confirmations **W-01** et **W-12** | copie P3, `PIECES-MANDATS-ET-CONFIRMATIONS.md` | `b940866f15f286333313d5a3af4ead155eddd9e0bd1719fbcc08bc7e17d36290` | non |
| 3 bis | Message J = JS-36 (2026-11-20T14:44:23Z), intégral : mandat de la v0.4.2, avec les **six arbitrages** (§2 bis) | copie P6, `PIECE-MANDAT-v0.4.2-ARBITRAGES.md` | `b222381f3e432bfbdf7828d04a71c8b1c657c6a5a9263caeeb02b8a9e38caf23` | non |
| 3 ter | Message K = JS-38 (2026-11-20T16:12:04Z), intégral : mandat de la v0.4.3 | copie P7, `PIECE-MANDAT-v0.4.3-CORRECTIONS.md` | `c1b86a538feb15851cfc8d180c8c655e0c12efa0efa20a82ca3fc86bb4c5c119` | non |
| 4 | Rapport de revue indépendante de la v0.3 (sections 1, 2, 4 et 5 entières ; 3 et 6 résumées) et observations complémentaires de Claude Code (extrait) | copie P4, `RAPPORT-REVUE-INDEPENDANTE-v0.3.md` | `81657c1c2353c845868d6a2689e9cab2fc3c9750b3826b1bb7c9a05b51b1878c` | non |
| 5 | Consolidation v0.2, dont les six messages de validation de Q4 (l.181 à 191) | pièce jointe `4f625a0d-…-Q1-Q4-REVUE.md` | `062c5e9c8176d08fedb4dbbb9d67daeebf1caf53b0e7d76d28250f19819ca2a1` | non |
| 6 | Consolidation v0.3 | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.3.md` | `85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256` | non |
| 7 | Registre | `main:docs/gameplay/GAMEPLAY-DECISIONS.md` | `9117d20c45aa95abbc218ce5cdcc2a095106eb86c64a342be76d8521ef14d39e` | oui |
| 8 | Rapport d'inscription ARB/G du 17 novembre | `main:docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md` | `ac4d72c6baa75412406bec427cd348f53de03b635a0d45c62e13c3b2e12d09f1` | oui |
| 9 | Consolidation v1.4.1 (citations d'ARB-A à ARB-E et de G1 à G4 ; cas de test du §5) | `main:docs/reviews/BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md` | `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc` | oui (commit `1ecc608`) |
| 10 | Mandat d'inscription v1.0 | `main:docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` | oui (commit `1ecc608`) |
| 11 | Rapport d'archivage du 18 novembre | `main:docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` | `7f457d789797f2fa7129ea1666ebfa66e6ad857534e8508d95419491252754c2` | oui |
| 12 | Consolidation v0.4, déposée telle que remise au propriétaire (2026-11-20T13:05:12Z) | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.md` | `02d8da8d9595e98e256186d59edb3ce75c49d7a0bf1be8ea889f8e2f63dd2a52` | non |
| 12 bis | Consolidation v0.4.1 | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md` | `bd4cf4fa5f94aa005c6e27bf81eb6cc6aba6e7365c8eccaddaf847320a699e3f` | non |
| 12 ter | Consolidation v0.4.2 | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2.md` | `a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808` | non |
| 13 | Rapport de la revue indépendante de la v0.4.1 (RV41), fichier original du relecteur : verdict « conforme sous réserves » ; I-1, M-01 à M-18, R-1 à R-11 | `RAPPORT-REVUE-INDEPENDANTE-v0.4.1.md` | `efd36eed9d9d98c1e9609ea81c11e906ebdab6354d543efbff2e084998da9db6` | non |
| 13 bis | Rapport de la revue indépendante de la v0.4.2 (RV42), fichier original du relecteur : verdict « conforme sous réserves » ; AN-01 à AN-08, OB-01 à OB-08 | `RAPPORT-REVUE-INDEPENDANTE-v0.4.2.md` | `1476a060e449fda7816ccc74c060d3465096cb1e56a0ae134b5f699145a6eb69` | non |

**Emplacements :**
- pièces 1 à 4, 6, 12, 12 bis et 12 ter : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-v03/` ;
- pièce 5 : `/root/.claude/uploads/7361641c-6eb6-5649-a764-279757212cf3/` ;
- pièce 13 : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-v041-relecteur/` ; pièce 13 bis : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-v042-relecteur/`.

**Outils de vérification** (M-17), dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/` :

| N° | Outil | Fichier | SHA-256 |
|---|---|---|---|
| O-1 | Extraction mécanique des messages du propriétaire : 35 messages, jusqu'à JS-35 ; aucune réponse de Claude Code | `revue-v03/MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md` | `73f1fcd26e95a9c11b09158ed9beaf150c47a1f67b069ce70ef3c6867c5a7c3c` |
| O-2 | Script d'extraction (O-1, O-4 et O-7) | `verif-v04/extract_user_msgs.py` | `206ca788e261d6104f027229b34fad84d971f47e8ac20ef73870b83968a791db` |
| O-3 | Diff de la v0.4 à la v0.4.1 | `verif-v04/diff-v0.4-v0.4.1.patch` | `1d6d2a58249344508f2613817ad7e32ae647b56ac794e4f8f746d6ea33174f8c` |
| O-4 | Même extraction, 36 messages, jusqu'à JS-36. Ses 35 premiers messages sont identiques à O-1 | `verif-v042/messages-extraction-2.md` | `f50d039c212b1dcef132da490b7c494e79b2cf9c420d6e85da4da4d912f57fcc` |
| O-5 | Script de recherche des omissions dans les copies (contrôle 7 du §17) | `verif-v042/omissions.py` | `78453dd92293fbfb5e23fd23405c9d1f62a69828f363b6b03659933705c9b6fe` |
| O-6 | Diff de la v0.4.1 à la v0.4.2 | `verif-v042/diff-v0.4.1-v0.4.2.patch` | `4decc4c83282d9bce4b466e989c33f16fb7a50ea8bc214541381b4a1ca9a3686` |
| O-7 | Même extraction, 38 messages, jusqu'à JS-38. Ses 36 premiers messages sont identiques à O-4 | `verif-v043/messages-extraction-3.md` | `8bd912bca00b933c1119f190c5000a30728eeefe48c36ed96d30439ae09f624c` |

La source de O-1, O-4 et O-7 est le journal de session, `/root/.claude/projects/-home-user/7361641c-6eb6-5649-a764-279757212cf3.jsonl`, sans empreinte stable (RD-9).

**Scripts de vérification et de production** (AN-08), dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/`, lancés avec `python3 -I` :

| N° | Rôle | Fichier | SHA-256 |
|---|---|---|---|
| S-1 | vérification de la v0.4 remise (texte extrait du journal) | `verif-v04/extract.py` | `385f24c9af8d5f26347301b7f8a63ed2f53219289451500ce63033ac047a59e1` |
| S-2 | comparaison de P5 au message I (journal) | `verif-v04/last_user.py` | `bad862ae1a031213affc23e22f20aebad3175f7f6d5410d432e9d94b5bc0b0d6` |
| S-3 | production de la v0.4.1 à partir de la v0.4 | `verif-v04/make_v041.py` | `145a738bf97c28008f8204da9840e1232eb3f0b66c072c2a98e5ea6a01c6a9f2` |
| S-4 | libellés de Q1.1 à Q1.4 (v0.4.1) | `verif-v04/check_labels.py` | `a1a7e4c70e9a5f0fc04d4621e5c5a650dda69e2c8e1d91215d1b138e442ee5db` |
| S-5 | calculs des scénarios (depuis la v0.4.1) | `verif-v04/calculs.py` | `0c8708c61c78f7738b300b8d096c58e66bb55bae8ff38d7a17b06e15e31278ed` |
| S-6 | production de la v0.4.2 à partir de la v0.4.1 | `verif-v042/make_v042.py` | `0a6c9f8d4ef5265794ebaf781dbef81115b39bef3720cb9d2ce1d6f882867a21` |
| S-7 | libellés de Q1.1 à Q1.4 et textes des six arbitrages | `verif-v042/check_textes.py` | `b1f732a05d59b828256235ac8921a25d76f5d974006dbc6ef7fb137b38cb7e35` |
| S-8 | rattachements de la matrice ; PNV dans les scénarios « Sp » | `verif-v042/check_matrice.py` | `4660e1e9a5b396097d3ccf6302b0548c7b6df689ff19ab739ea01039245aa8bf` |
| S-9 | calculs de T47, T48 et T21 (v0.4.2) | `verif-v042/calculs_v042.py` | `7869bab86eeba16c4f185bb6b1a4c8ba2b706bd1f688cf96844ffabca4ffca02` |
| S-10 | application des corrections AN et OB (v0.4.3) | `verif-v043/check_v043.py` | `4cbfe87f481479f135190f6893058c691ddd88d438159ff0fd489b22992146da` |
| S-11 | contrôle de toutes les citations (v0.4.3) | `verif-v043/citations_v043.py` | `ceb93d77f4befbfe51cc732a1c28b24a0f865491900c09591cc355875ad2eb19` |
| S-12 | calculs de T47 (a) et (b) et des arrondis de T48 (v0.4.3) | `verif-v043/calculs_v043.py` | `bc668debbd11788a16587a503a97b78fdaf0301042591f8c1d2fd0624a25d229` |

**Sans fichier, ou sans empreinte dans le présent texte :**

| N° | Pièce |
|---|---|
| 12 quater | Consolidation v0.4.3 (le présent texte) : fichier `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3.md`, dans `revue-v03/`. Un fichier ne pouvant contenir sa propre empreinte, celle-ci est donnée hors du fichier |
| O-8 | Diff de la v0.4.2 à la v0.4.3 : `verif-v043/diff-v0.4.2-v0.4.3.patch`. Son empreinte dépend du présent texte : elle est donnée hors du fichier |
| S-13 | Script de production de la v0.4.3 : `verif-v043/make_v043.py`. Il contient le texte des modifications, donc les empreintes citées ici : la sienne est donnée hors du fichier |
| 13 ter | Contrôle indépendant du diff de la v0.4.3 : à venir, sous autorisation distincte (P7) |
| 14 | JS-22 (2026-11-19T16:25:44Z), mandat de revue indépendante Q1–Q4 : non copié ; présent dans O-1, O-4 et O-7 |
| 14 bis | JS-29 (2026-11-19T20:35:55Z), mandat en sept points de vérification de la provenance de Q1.5 à Q3.14, qui écrit notamment « Q1.1 à Q1.4 ne sont pas encore joints » : non copié ; présent dans O-1, O-4 et O-7 |
| 14 ter | JS-37 (2026-11-20T15:41:03Z), autorisation de la revue indépendante de la v0.4.2 : non copié ; présent dans O-7 |
| 15 | Rapports de Claude Code du 19 novembre : revue indépendante Q1–Q4 ; mises à jour n° 1 et n° 2 ; remarques R-Q5-1 à R-Q5-5 sur l'addendum Q5 ; remarques sur l'addendum B3 et son rectificatif ; vérifications de provenance |
| 16 | Les messages d'origine du propriétaire et la conversation de conception : les pièces 1, 1 bis, 2, 3, 3 bis et 3 ter n'en sont que des copies ; O-1, O-4 et O-7 n'en sont que des extractions |

## 16. Journal des corrections de la v0.3 (C-01 à C-31), rectifié

**Désignations utilisées :**
- **message B** : vos points 1 à 6 sur Q5.1 et Q5.2 ;
- **message C** : l'addendum Q5, sections A à E ;
- **R-Q5-1 à R-Q5-5** : les remarques de Claude Code sur l'addendum Q5 :
  - R-Q5-1 : instant de l'engagement ;
  - R-Q5-2 : emplacement / case, et le mot « volontaire » ;
  - R-Q5-3 : la correction C4 ne peut pas réconcilier Q1 et GE-02 sans décision ;
  - R-Q5-4 : « coûts nuls » devient « cycles gratuits » ;
  - R-Q5-5 : corrections omises.

**Entrées inchangées :** C-01, C-05 à C-07, C-09 à C-13, C-15 à C-18, C-20 à C-29. Elles restent valables, et leur contenu est repris dans la v0.4, aux sections indiquées par la v0.3.

**Entrées rectifiées :**

| N° | Rectification |
|---|---|
| C-02 | origine : anomalie 2 ; message C, §A ; R-Q5-1 |
| C-03 | origine : anomalie 3 ; message C, §B ; R-Q5-2 ; complétée par W-14 (§4) |
| C-04 | origine : anomalie 4 ; R-Q5-3 ; B3 |
| C-08 | origine : anomalie 8 ; message B, **point 5** ; R-Q5-4 |
| C-14 | dépendance de G1-05 corrigée : géométrie et praticabilité du trajet (T43), **non** PNV-7 |
| C-19 | désormais faite : §9.1 (GE-02, GE-03, R:336) |
| C-30 | fondée sur la consigne n° 2 (P3 l.15) et sur la confirmation W-01 [CONF] (P3 l.88) ; la pièce B3-02 n'est pas modifiée (§3.2) |
| C-31 | origine : R-Q5-5 |

## 17. Vérification interne de la v0.4.3

Cette vérification est de Claude Code. Elle **n'est pas une revue indépendante**. Chaque contrôle a été exécuté avec `python3 -I` ou une commande du shell, avec le code de sortie 0. Les scripts sont inventoriés au §15 (S-1 à S-13). Les numéros 1 à 11 sont ceux de la v0.4.2, pour que les renvois restent valables ; les contrôles 12 et 13 sont nouveaux.

**Correspondance avec le §4 du mandat de la v0.4.3** (P7) : point 1 → contrôle 12 ; point 2 → contrôles 1, 2 et 13 ; point 3 → contrôle 5 ; point 4 → contrôles 2, 4 et 11 ; point 5 → contrôle 9 ; point 6 → contrôles 3 et 8 ; point 7 → contrôle 10.

| # | Contrôle | Méthode | Résultat |
|---|---|---|---|
| 1 | Citations de Q1.1 à Q1.4 | S-7 : recherche, dans le §0.1 et le §3.1, des huit libellés de P1 et de P5 et de la validation de P1 l.309 | identiques |
| 2 | Textes des six arbitrages | S-7 : recherche, dans le §2 bis, des six textes validés de P6 et de leurs statuts | identiques |
| 3 | Renvois de lignes nouveaux | lecture des lignes citées pour la première fois : JS-29, JS-37 et JS-38 dans O-7 ; P1 l.3, 67, 111, 165, 213 et 293 ; P2 l.12-14 et l.114 ; P3 l.31 ; P6 l.115 et l.130 ; D:30 ; R:104-105, R:134 et R:141 ; `BattleUnit.cpp:2733-2742` au commit `441cae1b` | concordants |
| 4 | Absence de décision nouvelle | relecture du diff O-8 bloc par bloc | aucune règle, valeur ni statut de décision modifié. Les ajouts sont des identifiants, des renvois, des réserves, des points [OUV], une conséquence marquée [DÉD] (OB-02) et un rappel [INS] (OB-01) |
| 5 | Calculs et scénarios | S-5, S-9 et S-12, en arithmétique exacte : barème, T01, T02, T05 (énumération exhaustive), T11a, T18 à T23, T26, T37, T39, T44, T45, T47 (a) et (b), T48 ; 1 341,6 mm | tous retrouvés. T47 (b) : trajet sélectionnable (12 TU pour 12 TU de coût connu) ; 8 TU, puis 2 TU ; arrêt sans débit ; il reste 2 TU et 95 d'énergie. T48 : 852,06… mm, enveloppe de 854 mm ; 852 mm par arrondi préalable au plus proche ou inférieur ; 853 puis 854 mm par arrondi supérieur |
| 6 | Exhaustivité | AN-01 à AN-08 et OB-01 à OB-08 ont chacun une ligne au §21 ; I-1, M-01 à M-18 et les six arbitrages au §20 ; W-01 à W-14 au §18 | complet |
| 7 | Copies | O-5 sur O-7 : chaque message du propriétaire est recherché en entier dans les copies | JS-24 à JS-28, JS-30, JS-32 à JS-36 et JS-38 intégraux ; JS-31 partiel, partie « Mission » omise ; JS-22, JS-23, JS-29 et JS-37 non copiés. Pour JS-22, la sortie brute indique « PARTIEL » sur 47 caractères : c'est une **concordance fortuite** avec le titre « BASTION — Mandat de revue indépendante MEC-0001 », que P3 l.31 reprend pour la v0.3 (AN-08) |
| 8 | Rattachement des scénarios | S-8 : chaque scénario de la colonne « Scénarios » du §12 cite-t-il la décision dans ses sources ? | aucun rattachement non cité |
| 9 | PNV | relecture du §3.5 et du §13 ; S-8 | neuf PNV conservées, PNV-2 actualisée par R-5=A. Dépendances à une PNV : T04, T15 et T26. T03, T42, T43 et T46 relèvent de la géométrie laissée ouverte par G1 (R:134). Aucune PNV dans un scénario « Sp » |
| 10 | Inventaire | empreintes recalculées | conformes au §15 |
| 11 | Portée de la v0.4.3 | diff de la v0.4.2 à la v0.4.3 (O-8), comparé section par section | aucun changement hors des sections du §21 ; §1, §3.3, §7, §8, §16 et §19 inchangés |
| 12 | Application des corrections | S-10 : pour chaque point AN et OB retenu, le texte corrigé est recherché à l'endroit visé, et le texte fautif doit avoir disparu. C'est la leçon d'AN-01 : on vérifie l'application de la correction, et non la seule présence d'une ligne au journal | toutes appliquées |
| 13 | Toutes les citations | S-11 : chaque passage entre « », guillemets imbriqués compris, est recherché dans les sources primaires (pièces, registre et documents de `main`, v0.2, extraction O-7, rapports RV41 et RV42), puis dans le document et ses versions antérieures | 269 passages : 254 retrouvés dans les sources primaires, à la casse de l'initiale près, sans la mention (recommandé) des propositions et à l'espacement près autour de × (écarts déjà admis par la revue de la v0.4.1, §4.3) ; 15 ne figurent que dans le document ou ses versions antérieures (renvois internes des journaux de corrections, §19 à §21, et phrases finales) ; aucun introuvable |

**Impossibilités de vérification :**
- authenticité des messages et de la conversation de conception ; présence des options B dans cette conversation ;
- textes des options des six arbitrages, de Q5.1, de Q5.2 et de B3 ;
- fidélité de P4 au rapport d'origine de la revue de la v0.3 ;
- comportement d'OXCE à l'exécution ; aucun scénario n'a été exécuté comme test ;
- contrôle indépendant du diff de la v0.4.3 : non fait, il relève d'une autorisation distincte (P7).

## 18. Tableau des corrections W-01 à W-14 (revue de la v0.3)

| Anomalie | Correction | Section | Preuve | Statut |
|---|---|---|---|---|
| W-01 | chronologie en cinq étapes (six depuis R-6=A, v0.4.2) ; règle applicable fondée sur la confirmation W-01 ; B3-02 reproduit sans modification ; sa phrase sur les « constantes universelles » déclarée sans effet pour la hauteur | §3.1, §3.2, §9.1, §16 (C-30) | P3 l.15, l.88 ; P2 l.143-151 ; R:203 ; D:86 ; P6 l.73 | corrigé (sur [CONF] ; précisé par R-6=A) |
| W-02 | marqueur ⟨B3-03⟩ sur les valeurs de Q1 ; distinction entre valeurs transmises et PNV | §0, §3.1, §3.6, §9.1, §12, T26 | P2 l.169 | corrigé |
| W-03 | T21 : remarque fausse retirée. Avec le profil Q4.6, min(solde + 60, 60) = 60 pour tout solde positif ou nul : le plafond est toujours atteint et ne distingue pas ARB-D d'une remise au maximum ; d'où les valeurs fictives | §13 (T21) | calcul vérifié | corrigé ; explication portée dans T21 en v0.4.2 (M-02) |
| W-04 | annotations et mentions « Ouvert » proposées pour GE-02 et GE-03 ; nouvelle ligne R:336 ; GE-05, CO-01 et règles de dégâts inchangées | §9.1 | R:203, R:204, R:336 ; rectificatif §1, §3, §4 | corrigé (textes proposés, non inscrits) |
| W-05 | inventaire complet avec empreintes vérifiées ; message A entier ; mandats, rapport et observations ; fichiers de la v0.4 et de la v0.4.1 ; revue de la v0.4.1 à venir. Reclassement de Q1.1 à Q1.4 en [TR] fait dans la v0.4.1, après réception des options B (copie P5). Dans la v0.4, il restait en attente | §0.1, §3.1, §12, §15 | P1 l.300-309 ; P5 l.14-17 ; P3 l.116 ; empreintes du §15 | corrigé (v0.4.1) ; provenance précisée en v0.4.2 : [TR-M] (I-1) |
| W-06 | P0-10, E-04, E-05, C-02, G1-01, G1-04 et G1-05 repris (T37 à T43) ; dépendance de G1-05 corrigée ; sort de tous les cas de la v1.4.1 | §13, §16 (C-14) | v1.4.1, §5 | corrigé |
| W-07 | formulation d'origine de Q3.11 reprise ; lien avec Q4.6 | §5 | P1 l.199-203 | corrigé |
| W-08 (a) à (e), (m) | citations d'origine pour Q1.6, Q3.2, Q3.10 et Q3.5 ; case d'arrivée marquée [DÉD] ; paragraphe de portée cité | §3.1, §4 à §6 | P1 l.19-29, 121-127, 193-197, 141-145, 115-119, 153-161 | corrigé |
| W-08 (f) | « destination tactique admissible » rétablie | §6 | P2 l.75 | corrigé |
| W-08 (g) | « peuvent être exprimées en millimètres », formulation du rectificatif | §3.1, §9.1 | P2 l.217 (rectificatif §1) | corrigé ; précisé par R-5=A (v0.4.2) |
| W-08 (h) | GE-02 : « modifiée », texte historique conservé ; GE-03 : la clause de Q1.2 lui est attribuée explicitement | §9.1 | B3-02, B3-03 | corrigé |
| W-08 (i) | règle d'ARB-A et G1 limitée au pas diagonal ; pour les autres pas : Q1.2 et Q4.2, méthode en PNV-6 | §3.4, §3.5 | R:121, R:126-133 | corrigé |
| W-08 (j) | Q4.7 : « valeurs initiales configurables de test, et non des constantes universelles » | §4 | P2 l.18 | corrigé |
| W-08 (k) | Q4.19 tranche trois points | §8, §10 | D:113 ; R:140 | corrigé |
| W-08 (l) | arithmétique en trois niveaux : exigence validée, nécessité démontrée, méthode non arbitrée | §5 | Q3.14 ; T20 | corrigé |
| W-09 | PNV-2 mise en cohérence (Q1.1, Q2.6 ; non étendue à MEC-0002), puis actualisée par R-5=A en v0.4.2 ; dépendance du §3.6 à PNV-4 déclarée ; PNV-3 et PNV-6 précisées ; PNV-7 : « renvoi sans objet » | §3.5, §3.6, §9.1 | P1 ; P2 l.219-221 | corrigé |
| W-10 | T04 : bornes ouvertes ; T18 : option B retirée ; T30 : condition physique explicite ; T33 : sens ouvert ; T36 : partiel | §13 | Q1.9 ; Q3.13 ; GE-05 ; D:110 ; Q4.19 | corrigé |
| W-11 (a) | dépendances des PNV corrigées (T03, T04, T15, T26, T42, T43, T45, T46). T45 retiré en v0.4.2 (M-13) ; T03, T42, T43 et T46 rattachés en v0.4.3 à la géométrie laissée ouverte par G1, R:134 (AN-06) : restent T04, T15 et T26 | §12, §13 | — | corrigé ; actualisé en v0.4.3 (AN-05, AN-06) |
| W-11 (b) | « aucun scénario dédié » pour Q2.4, Q3.3, Q3.5 et Q3.10 | §12 | — | corrigé ; étendu en v0.4.2 (M-03) |
| W-11 (c) | origines du journal rectifiées ; points de l'addendum (message C) distingués des remarques R-Q5-1 à R-Q5-5 | §16 | P2 ; inventaire n° 15 | corrigé |
| W-11 (d) | emplacement / case rangé sous « Occupation des connexions » | §14 | — | corrigé |
| W-12 | statut historique « proposition » conservé ; validation ultérieure [CONF] ajoutée séparément | §0, §12 | P2 l.209 ; P3 l.100-101 | corrigé (sans autorisation de modifier le dépôt) |
| W-13 | comparaisons limitées au documenté ; écart de G4 seul ; Q4.16 « non comparé » ; référence `BattleUnit.cpp:2714-2720` ajoutée pour ARB-D | §11 | LOT-2A §2, ligne 14 ; code au commit `441cae1b` | corrigé ; différence de calcul flottant précisée en v0.4.2 (M-15) |
| W-14 | lectures marquées [DÉD] ; pas d'exception à S10 ; jamais deux unités conscientes sur une même case stable, hors de l'exception transitoire de G2 ; emplacement / case et transit partagé maintenus ouverts | §4, §14, T24 | R:80 ; P2 l.34-38, 83-95 | corrigé, points ouverts maintenus |

## 19. Changements de la v0.4 à la v0.4.1

Origine : message I du propriétaire (copie P5). **Aucune décision n'est modifiée.** Aucune règle, valeur, PNV ni scénario n'est ajouté, retiré ou modifié sur le fond.

| N° | Endroit | Dans la v0.4 | Dans la v0.4.1 | Motif |
|---|---|---|---|---|
| V-01 | titre ; nature ; « Succède à » ; copies de travail | v0.4 ; copies P1 à P4 | v0.4.1 ; empreinte de la v0.4 ; copie P5 ajoutée | identification de la version |
| V-02 | §0 | codes [TR] et [TR-A] | [TR] couvre Q1.1 à Q1.4 (P1, message 2, et P5) ; [TR-A] retiré, sa définition gardée pour l'historique | point 3 du message I |
| V-03 | §0.1 | options B absentes ; [TR-A] maintenu | vérification de la proposition complète ; reclassement en [TR] ; limites ; observation [DÉD] sur l'option B de Q1.4 | points 2 et 3 |
| V-04 | §3.1 | Q1.1 à Q1.4 en [TR-A] ; sources P1 | [TR] ; sources P1 (validation l.309 comprise) et P5 ; texte des options B écartées ; parité de la largeur : [TR] | points 3 et 4 |
| V-05 | §3.2, étape 2 | Q1.4 [TR-A] | [TR] ; mention de l'option B écartée | point 3 (conséquence) |
| V-06 | §3.4 ; §3.5, PNV-2 | Q1.2 [TR-A] ; « [TR-A] et [TR] » | [TR] | point 3 (conséquence) ; le statut de PNV-2 ne change pas |
| V-07 | §12, lignes Q1.1 à Q1.4 | [TR-A] ; réserve « options B absentes » | [TR] ; sources P5 ; réserve retirée ; Q1.4 : libellé au passé signalé | points 3 et 4 |
| V-08 | §14 | RD-5 ouverte ; RD-1 : « sauf les numéros 9 à 12 » ; RD-7 : v0.4 | RD-5 levée ; RD-1 : « sauf les numéros 7 à 11 » ; RD-7 : v0.4 et v0.4.1 | point 4. RD-1 corrige une **erreur de renvoi de la v0.4**, relevée en refaisant l'inventaire : les pièces archivées sont les numéros 7 à 11 |
| V-09 | §15 | v0.4 sans fichier ; revue de la v0.4 à venir | pièces 1 bis (P5) et 12 (fichier de la v0.4) avec empreintes ; pièce 12 bis (v0.4.1, empreinte hors du fichier) ; revue de la v0.4.1 à venir | point 4 ; numéros 1 à 11 inchangés, pour que les renvois existants restent valables |
| V-10 | §17 | vérification de la v0.4 | vérification de la v0.4.1 : contrôles 1, 3, 4, 7 et 8 refaits ; contrôle 9 (diff) ajouté | — |
| V-11 | §18, ligne W-05 | reclassement en attente | corrigé (v0.4.1) | point 4 |
| V-12 | §19 ; phrase finale | — | ce tableau ; « La v0.4.1 n'est pas déclarée conforme » | — |

**Mentions conservées :** les mentions de la v0.4 qui désignent la version où un contenu est apparu (§13, colonne « Dans la v0.4 » ; §16 ; §18) restent telles quelles.

## 20. Corrections de la v0.4.1 à la v0.4.2

**Origine :** mandat de la v0.4.2 (copie P6) et rapport RV41 (pièce 13). Les constats sont ceux du rapport, résumés ; leur texte intégral est au §2 de la pièce 13.

### 20.1 Arbitrages intégrés

| N° | Arbitrage | Effet dans la v0.4.2 | Sections | Source | Statut |
|---|---|---|---|---|---|
| A-1 | M-04=B | affirmation [DÉD] « la surcharge ne réduit pas l'énergie » retirée ; principe d'un effet possible ; réduction des TU et récupération séparée inchangées ; modalités ouvertes | §2, §2 bis, §5, §9.2, §10, §12, §14 | P6 l.30-42 | intégré ; modalités ouvertes |
| A-2 | M-05=A | lecture [DÉD] de Q4.21 remplacée ; règle du coût réel ; point R:166 tranché pour le coût payable ; T47 | §2, §2 bis, §6, §9.2, §10, §12, §13, §14 | P6 l.43-56 | intégré |
| A-3 | R-5=A | unités de mesure ; PNV-2 ; annotations de GE-02, GE-03, R:336 et CH-08 ; T48 | §2, §2 bis, §3.1, §3.5, §9.1, §10, §12, §13, §14 | P6 l.57-70 | intégré ; modalités techniques ouvertes |
| A-4 | R-6=A | chronologie en six étapes ; règle applicable ; GE-02 et R:336 ; T27 | §2, §2 bis, §3.1, §3.2, §9.1, §12, §13, §18 | P6 l.71-82 | intégré |
| A-5 | R-7=A | portée résiduelle de Q1.4 ; T27 | §2, §2 bis, §3.1, §3.2, §9.1, §12, §13 | P6 l.83-93 | intégré |
| A-6 | R-8=A | Q1.2, précision explicite de GE-03 ; annotation de GE-03 ; inscription future | §2, §2 bis, §3.1, §3.4, §9.1, §10, §12 | P6 l.94-107 | intégré |

### 20.2 Anomalie I-1 et anomalies M-01 à M-18

| N° | Constat (RV41) | Correction | Emplacement | Source | Statut |
|---|---|---|---|---|---|
| I-1 | limites du §0.1 incomplètes : le message reçu le 19 novembre ne contenait pas les options B ; nombre de deux options seulement déclaré ; [TR] recouvrant deux qualités de preuve, sans distinction au §3.1 ni au §12 | §0.1 réécrit : deux messages identifiés et horodatés, dans l'ordre réel ; huit options et validation reproduites ; omission « Mission » identifiée ; compilation signalée ; code [TR-M] ; réserve au §12 ; RD-5 | §0, §0.1, §3.1, §3.2, §3.4, §3.5, §12, §14, §15 | RV41 §2.2 ; P6 l.108-124 ; O-1, O-4 | corrigé |
| M-01 | ⟨B3-03⟩ absent sur cinq valeurs tirées de Q1 | marqueur ajouté : 1 274 mm, 1 341,6 mm, profil dans la case (§3.6) ; rapport 0,5 (§9.1). *Rectifié en v0.4.3 : cette ligne annonçait aussi T04, qui n'avait pas été corrigé (AN-01) ; T04 l'est dans la v0.4.3* | §3.6, §9.1 ; §13 en v0.4.3 | RV41 M-01 ; P2 l.169, l.239 | corrigé en partie dans la v0.4.2 ; achevé dans la v0.4.3 |
| M-02 | T21 n'explique plus le maximum fictif de 20 | explication portée dans T21 | §13 (T21) | RV41 M-02 ; P3 l.124-126 | corrigé |
| M-03 | dix rattachements de la matrice non cités par leur scénario | critère de rattachement énoncé ; Q1.4 → aucun (historique) ; Q1.8 cité dans T27 ; Q3.1 → T02 et T22, qui le citent ; Q3.2 cité dans T02 ; Q3.4 → T08 et T47 ; Q3.6 → aucun ; Q3.8 cité dans T18 ; Q4.6 → T01, qui le cite, et T21 retiré. Même critère appliqué à B3 : T26 et T27 ne le citent pas, d'où « aucun scénario dédié » | §12, §13 | RV41 M-03 ; contrôle 8 du §17 | corrigé |
| M-04 | [DÉD] « la surcharge ne réduit pas l'énergie », plus affirmatif que ses sources | arbitrage M-04=B intégré (A-1) | §5 | RV41 M-04 ; P6 l.30-42 | corrigé par arbitrage |
| M-05 | lecture [DÉD] de « non exécutable » dans Q4.21 | arbitrage M-05=A intégré (A-2) | §6 | RV41 M-05 ; P6 l.43-56 | corrigé par arbitrage |
| M-06 | observation sur l'option B de Q1.4 : code [DÉD] impropre ; comparaison à préciser | qualifiée d'« observation documentaire, sans valeur de décision » ; principe commun et apports de W-01 et de R-6=A précisés | §0.1 | RV41 M-06 | corrigé |
| M-07 | PNV-7 placée dans la colonne « Précisée ou modifiée par » de G1 | « — (priorité « X puis Y » non décidée : PNV-7) » | §2 | RV41 M-07 | corrigé |
| M-08 | « tout le volume » cité entre guillemets, absent de D:34 | D:34 cité mot pour mot ; statut reformulé avec les seules expressions de la source | §3.5 (PNV-4) | RV41 M-08 ; D:34 | corrigé |
| M-09 | T24 : « jamais deux unités conscientes sur une même case », sans l'exception de G2 | exception transitoire de G2 rappelée dans T24, au §4 et au §18 (W-14) | §4, §13 (T24), §18 | RV41 M-09 ; R:137 ; P2 l.92 | corrigé |
| M-10 | citation sur Q4.15 attribuée au message B | attribuée à l'addendum Q5, §B (P2 l.95) ; phrase du message B citée pour Q5.2 (P2 l.38) | §4 | RV41 M-10 | corrigé |
| M-11 | « Ces chiffres sont identiques à ceux de l'option A de Q3.11 » | limité aux valeurs d'énergie 100 et 20 ; TU non concernées | §5 | RV41 M-11 ; P1 l.201 | corrigé |
| M-12 | RD-2 omettait la confirmation du contenu de Q4.1 | ajoutée (W-01 ; R-6=A) | §14 | RV41 M-12 ; P3 l.88 | corrigé |
| M-13 | statut de T45 incohérent avec T02 et T22 | T45 : « Sp (passage supposé praticable, comme T02 et T22) ; test intégré de la géométrie : Pa » ; dépendance à PNV-6 retirée | §12, §13, §17 | RV41 M-13 | corrigé |
| M-14 | sort de P0-05 et P0-06, de G1-01 et du §5.5 de la v1.4.1 imprécis | P0-05 → T21, valeur intermédiaire, résultat isolé non conservé ; P0-06 → T21, premier cas ; G1-01 « adapté » ; §5.5 : renvoi à la v1.4.1 | §13 | RV41 M-14 ; v1.4.1 l.150-151, l.169, §5.5 | corrigé |
| M-15 | « Concordance d'ordre et de troncature » d'ARB-D, sans nuance (citation rectifiée en v0.4.3, AN-04) | ordre concordant ; calcul flottant tronqué dans OXCE distingué du plancher exact de Q3.14 ; exemple émulé ; aucune équivalence affirmée | §11 | RV41 M-15 ; `BattleUnit.cpp:2714-2720` | corrigé |
| M-16 | P1 dit « reproduit tel que reçu », alors que la partie « Mission » est omise | omission déclarée au §0.1, au §15 (pièce 1) et en RD-6 ; P1 non modifiée | §0.1, §14, §15 | RV41 M-16 ; O-4, O-5 | corrigé |
| M-17 | outils de comparaison non inventoriés ; choix de ne pas modifier P1 non énoncé | outils O-1 à O-6 inventoriés ; « P1 n'est pas modifiée ; elle est complétée par la pièce 1 bis » | §15 | RV41 M-17 | corrigé |
| M-18 | renvoi « P2 l.215 environ » | « P2 l.217 » | §18 (W-08 g) | RV41 M-18 | corrigé |

### 20.3 Autres changements

| N° | Endroit | Changement | Motif |
|---|---|---|---|
| V-13 | titre ; nature ; « Succède à » ; copies | v0.4.2 ; lignée ; P6 et RV41 ajoutées | identification de la version |
| V-14 | §0 | [TR] limité aux propositions transmises en un message ; [TR-M] et [VAL] créés ; P6 l.123 citée | I-1, point 5 ; arbitrages |
| V-15 | §2 bis | rubrique distincte des six arbitrages | P6 l.167 |
| V-16 | §11 | « Autres décisions, dont les six arbitrages du §2 bis : non étudiées » | aucune comparaison faite |
| V-17 | §14 | RD-3 étendue aux arbitrages ; RD-7 actualisée ; RD-8 (réserves de RV41) ; points ouverts complétés selon P6, §6 | P6 l.169-183 |
| V-18 | §15 | pièces 3 bis, 12 bis (avec empreinte), 13, 12 ter, 13 bis ; outils O-1 à O-6 | M-17 ; I-1, point 6 |
| V-19 | §17 | vérification de la v0.4.2 et impossibilités de vérification | P6, §7 |
| V-20 | §18 | titre précisé ; lignes W-01, W-03, W-05, W-08 (g), W-09, W-11 (b), W-13 et W-14 actualisées | renvois aux corrections de la v0.4.2 |
| V-21 | §20 ; phrase finale | ce tableau ; « La v0.4.2 n'est pas déclarée conforme » | — |

Les §16 (journal C-01 à C-31) et §19 (changements de la v0.4 à la v0.4.1) restent tels quels : ils décrivent des versions antérieures.

## 21. Corrections de la v0.4.2 à la v0.4.3

**Origine :** mandat de la v0.4.3 (copie P7) et rapport RV42 (pièce 13 bis). Les constats sont ceux du rapport, résumés ; leur texte intégral est au §2 de la pièce 13 bis. **Aucune décision n'est modifiée.**

### 21.1 Anomalies AN-01 à AN-08

| N° | Constat (RV42) | Traitement dans la v0.4.3 | Emplacement | Source | Statut |
|---|---|---|---|---|---|
| AN-01 | ⟨B3-03⟩ annoncé ajouté à T04 au §20.2, mais absent | marqueur ajouté à T04 ; ligne M-01 du §20.2 rectifiée et signalée comme telle | §13 (T04), §20.2 | RV42 AN-01 ; P6 l.130 | corrigé (indispensable) |
| AN-02 | « message 1 » et « message 2 » désignent des messages différents au §0 et au §0.1 | identifiants stables JS-NN, horodatés, avec leurs copies (tableau du §0) ; §0.1, §14 (RD-6) et §15 réécrits avec ces identifiants ; « Message 1 » et « Message 2 » réservés aux intertitres de P1 | §0, §0.1, §14, §15 | RV42 AN-02 ; P6 l.115 | corrigé (indispensable) |
| AN-03 | T47 (b) part d'un état incompatible avec Z1 et G3 | T47 (b) : 12 TU et 100 d'énergie à la sélection ; le deuxième pas, plus coûteux mais payable, est exécuté (M-05=A) ; arrêt sans débit avant le troisième | §13 (T47) | RV42 AN-03 | corrigé (indispensable) |
| AN-04 | trois expressions entre guillemets absentes du texte cité | (a) PNV-2 : D:30 cité exactement ; (b) §20.2, M-15 : « Concordance d'ordre et de troncature » ; (c) T26 : « le profil ne dépasse pas sa case » | §3.5, §20.2, §13 | RV42 AN-04 ; D:30 | corrigé ((a) et (b) indispensables ; (c) recommandé) |
| AN-05 | §18, W-11 (a) : T45 encore parmi les scénarios qui dépendent d'une PNV | ligne actualisée (T45 retiré en v0.4.2) | §18 | RV42 AN-05 | corrigé (indispensable) |
| AN-06 | T03, T42, T43 et T46 rattachés aux PNV sans PNV nommée ni justifiée | dépendances rattachées à la géométrie laissée ouverte par G1 (R:134) ; ligne PNV du §12, contrôle 9 du §17 et ligne W-11 (a) du §18 actualisés ; statuts inchangés (Pa) | §12, §13, §17, §18 | RV42 AN-06 ; R:134 | corrigé (recommandé) |
| AN-07 | §10 : « — » pour R:166 et G3, malgré des points ouverts | R:166 : repli d'une diagonale sur le passage Y (§6) ; G3 : coûts de chaque connexion (Q3.10=B) ; RF-01 complété au §14 | §10, §14 | RV42 AN-07 ; R:141, R:166 | corrigé (indispensable) |
| AN-08 | scripts non inventoriés ; résultat brut du contrôle 7 réinterprété sans le dire ; JS-29 décrit comme une simple annonce | scripts S-1 à S-13 inventoriés, avec leur empreinte sauf S-13 ; concordance fortuite de JS-22 expliquée ; JS-29 décrit exactement, cité au §0.1 et inventorié (pièce 14 bis) | §0, §0.1, §15, §17 | RV42 AN-08 | corrigé (recommandé) |

### 21.2 Observations OB-01 à OB-08

| N° | Observation (RV42) | Traitement | Emplacement | Statut |
|---|---|---|---|---|
| OB-01 | rappel d'ARB-D présenté comme une conséquence de P6 | source propre indiquée : [INS] R:124, hors de P6 | §5 | retenu |
| OB-02 | « tranché sur ce point » (R:166) : P6 ne le dit pas | marqué [DÉD], conséquence de M-05=A | §6 | retenu |
| OB-03 | « arrondi préalable au millimètre » : vrai seulement au plus proche ou vers le bas | « au millimètre le plus proche, ou inférieur » ; cas de l'arrondi supérieur ajouté | §13 (T48), §17 | retenu |
| OB-04 | R-8=A présenté comme une « clarification » | statuts exacts de P6 cités pour R-7=A et R-8=A | §2 bis | retenu |
| OB-05 | [TR] et [TR-M] qualifient la transmission dans la session, non l'échange d'origine | phrase ajoutée au §0 | §0 | retenu |
| OB-06 | articulation de M-04=B avec N14 | point d'articulation [OUV] ajouté au §5 et au §14 ; N14 ajouté aux annotations du §9.2 | §5, §9.2, §14 | retenu |
| OB-07 | T26 cite Q1.4, historique | sources de T26 : « Q1.1 à Q1.3, Q1.5 à Q1.7, Q2.5, Q2.6 » | §13 (T26) | retenu |
| OB-08 | empreinte de P2 mal tronquée dans la commande de la revue de la v0.4.2 | **non retenu, sans objet** pour le document : l'erreur était dans la commande de revue, non dans la v0.4.2 ; l'empreinte complète de P2 est au §15 | — | non retenu |

### 21.3 Autres changements

| N° | Endroit | Changement | Motif |
|---|---|---|---|
| V-22 | titre ; nature ; « Succède à » ; lignée ; copies ; références | v0.4.3 ; P7 et RV42 ajoutés ; notation JS-NN | identification de la version |
| V-23 | §14 | RD-7 actualisée ; RD-9 (journal de session) et RD-10 (pleine conformité) ajoutées, d'après RV42, §5 | P7, §5 : réserves restantes |
| V-24 | §15 | pièces 3 ter (P7), 12 ter (v0.4.2, avec empreinte), 13 bis (RV42), 12 quater, 13 ter, 14 bis et 14 ter ; outils O-6 (avec empreinte), O-7 et O-8 ; scripts S-1 à S-13 | AN-08 ; P7, §5 |
| V-25 | §17 | vérification de la v0.4.3 ; contrôles 12 et 13 ajoutés ; numéros 1 à 11 conservés | P7, §4 |
| V-26 | §20.2 | lignes M-01 et M-15 rectifiées, et signalées comme telles | AN-01, AN-04 (b) |
| V-27 | §21 ; phrase finale | ce tableau ; « La v0.4.3 n'est pas déclarée conforme » | P7, §5 |

Les §16, §19 et §20.1 restent tels quels : ils décrivent des versions antérieures.

**La v0.4.3 n'est pas déclarée conforme** : il faut d'abord le contrôle indépendant de son diff, qui relève d'une autorisation distincte. MEC-0001 et MEC-0002 restent reportées.
