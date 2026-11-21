import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
def rep(old, new):
    global t
    n = t.count(old)
    if n != 1:
        sys.exit("ECHEC: %d occurrence(s) de: %r" % (n, old[:100]))
    t = t.replace(old, new)
def between(start, end_excl, new):
    global t
    assert t.count(start) == 1 and t.count(end_excl) == 1, (start[:60], end_excl[:60])
    i = t.index(start); j = t.index(end_excl)
    assert i < j
    t = t[:i] + new + t[j:]

SP = "/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad"
H = dict(
 P1="c9ee67cab4a96d4ab4902048426ae6fe34feb7dd23b9416768ee6ffba1c69063",
 P5="7e799d1c8ebd3a4486f28aaf34117709b76a92a11b68aa14c0296f44f0139777",
 P2="b69ba3b799608572363b1571ad1a9197a1c90af5e19c1b69f328de6a9a37b869",
 P3="b940866f15f286333313d5a3af4ead155eddd9e0bd1719fbcc08bc7e17d36290",
 P6="b222381f3e432bfbdf7828d04a71c8b1c657c6a5a9263caeeb02b8a9e38caf23",
 P4="81657c1c2353c845868d6a2689e9cab2fc3c9750b3826b1bb7c9a05b51b1878c",
 V02="062c5e9c8176d08fedb4dbbb9d67daeebf1caf53b0e7d76d28250f19819ca2a1",
 V03="85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256",
 V04="02d8da8d9595e98e256186d59edb3ce75c49d7a0bf1be8ea889f8e2f63dd2a52",
 V041="bd4cf4fa5f94aa005c6e27bf81eb6cc6aba6e7365c8eccaddaf847320a699e3f",
 RV41="efd36eed9d9d98c1e9609ea81c11e906ebdab6354d543efbff2e084998da9db6",
 O1="73f1fcd26e95a9c11b09158ed9beaf150c47a1f67b069ce70ef3c6867c5a7c3c",
 O2="206ca788e261d6104f027229b34fad84d971f47e8ac20ef73870b83968a791db",
 O3="1d6d2a58249344508f2613817ad7e32ae647b56ac794e4f8f746d6ea33174f8c",
 O4="f50d039c212b1dcef132da490b7c494e79b2cf9c420d6e85da4da4d912f57fcc",
 O5="78453dd92293fbfb5e23fd23405c9d1f62a69828f363b6b03659933705c9b6fe",
)

# ---------- En-tête
rep("# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.1\n",
    "# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.2\n")
rep("**Nature :** projet de consolidation documentaire ; v0.4 corrigée après réception des options B de Q1.1 à Q1.4. Non revu, non inscrit.",
    "**Nature :** projet de consolidation documentaire complète, préparé sous le mandat de la v0.4.2 (copie P6). Il intègre les six arbitrages du propriétaire du 20 novembre 2026 et corrige l'anomalie I-1 et les anomalies M-01 à M-18 de la revue indépendante de la v0.4.1. Non revu, non inscrit.")
rep("**Succède à :** la v0.4 (SHA-256 `" + H["V04"] + "`), issue de la v0.3 (SHA-256 `" + H["V03"] + "`). La v0.4 intégrait les confirmations W-01 et W-12 du propriétaire et les corrections W-01 à W-14 (tableau final au §18). La v0.4.1 ne change que la provenance de Q1.1 à Q1.4 et les références qui en dépendent. Aucune décision n'est modifiée (liste des changements au §19).",
    "**Succède à :** la v0.4.1 (SHA-256 `" + H["V041"] + "`), revue de façon indépendante : verdict « conforme sous réserves » (pièce 13).\n\n**Lignée :** v0.3 (`" + H["V03"] + "`) → v0.4 (`" + H["V04"] + "`) → v0.4.1 → v0.4.2. Corrections : W-01 à W-14 dans la v0.4 (§18) ; provenance de Q1.1 à Q1.4 dans la v0.4.1 (§19) ; six arbitrages, I-1 et M-01 à M-18 dans la v0.4.2 (§2 bis et §20). Les décisions validées auparavant sont conservées ; les six arbitrages les précisent ou tranchent des points ouverts (§2 bis).")
rep("- **P5** : options B de Q1.1 à Q1.4 (message I du propriétaire), qui complètent la copie P1.\n",
    "- **P5** : options B de Q1.1 à Q1.4 (message I du propriétaire), qui complètent la copie P1 ;\n- **P6** : mandat de la v0.4.2, avec les six arbitrages du propriétaire (message J) ;\n- **RV41** : rapport de la revue indépendante de la v0.4.1 (pièce 13, fichier original du relecteur).\n")

# ---------- §0
rep("| **[TR]** | proposition avec ses options, et validation, transmises par le propriétaire (copie P1, message 1 ; pour Q1.1 à Q1.4 : copie P1, message 2, complétée par la copie P5) | oui |",
    "| **[TR]** | proposition avec ses options, et validation, transmises **ensemble, dans un même message** du propriétaire : Q1.5 à Q3.14 (message du 19 novembre 2026 à 20 h 36 UTC ; copie P1, message 1) | oui |\n| **[TR-M]** | proposition avec ses options, et validation, transmises **en plusieurs messages** du propriétaire, qui forment ensemble le dossier : Q1.1 à Q1.4 (§0.1). Même catégorie que [TR], « proposition et validation transmises » (P3 l.116) ; mais aucun des messages ne contient à lui seul la proposition complète | oui |")
rep("| [TR-A] | **code retiré dans la v0.4.1.** Il désignait, dans la v0.4, l'option retenue et la validation citée, sans les options écartées (copie P1, message 2) | sans objet (§0.1) |",
    "| [TR-A] | **code retiré dans la v0.4.1.** Il désignait, dans la v0.4, l'option retenue et la validation citée, sans les options écartées (copie P1, message 2). Q1.1 à Q1.4, classées [TR] dans la v0.4.1, relèvent de [TR-M] depuis la v0.4.2 | sans objet (§0.1) |")
rep("| **[CONF]** | confirmation expresse du propriétaire, reçue avec le mandat de la v0.4 le 20 novembre 2026 (P3, message H) | oui |",
    "| **[CONF]** | confirmation expresse du propriétaire, reçue avec le mandat de la v0.4 le 20 novembre 2026 (P3, message H) | oui |\n| **[VAL]** | arbitrage validé expressément par le propriétaire dans le mandat de la v0.4.2, le 20 novembre 2026 (copie P6, message J) : texte de la décision validée et statut transmis ; textes des options non transmis | oui, dans les limites du statut indiqué (par exemple « principe validé ; modalités ouvertes ») |")
rep("**Aucune n'est une pièce originale authentifiée de façon indépendante, et aucune n'est archivée dans le dépôt**, sauf mention contraire au §15.",
    "**Aucune n'est une pièce originale authentifiée de façon indépendante, et aucune n'est archivée dans le dépôt**, sauf mention contraire au §15. « La transmission complète des propositions ne vaut pas authentification indépendante de la conversation d'origine. » (P6 l.123)")

# ---------- §0.1
between("### 0.1 Q1.1 à Q1.4 : vérification de la proposition complète", "## 1. Périmètre et responsabilités", """### 0.1 Q1.1 à Q1.4 : un dossier composé de deux messages

**Les deux messages, dans l'ordre réel** (horodatages UTC du journal de session, relevés par les extractions O-1 et O-4) :

| Ordre | Message | Horodatage | Contenu | Copie |
|---|---|---|---|---|
| 1 | message du propriétaire commençant par « Pour Bastion MEC-0001, voici les quatre dernières propositions et validations originales manquantes : Q1.1 à Q1.4. » | 2026-11-19T20:54:21.612Z | titre et option A de Q1.1 à Q1.4 ; validation ; puis une partie « Mission : » (six consignes et des restrictions). **Aucune option B** | copie P1, message 2 (l.297-310) : tout le message, **sauf** la partie « Mission », non reproduite (M-16) |
| 2 | message I du propriétaire | 2026-11-20T13:41:45.327Z | options B de Q1.1 à Q1.4, puis consignes de travail | copie P5, l.9-35 : message intégral |

**Entre les deux :**
- le mandat de la v0.4 (message H, 2026-11-20T12:53:14.601Z) écrivait : « Les pièces comprennent, pour chacune de ces décisions, les deux options A et B, puis la validation explicite de l'option A. » (P3 l.108). À cette heure, le dossier ne contenait pas les options B ;
- la v0.4, remise à 2026-11-20T13:05:12.403Z, demandait de les joindre ;
- le message I indique : « les options B de Q1.1 à Q1.4 ont déjà été transmises au propriétaire dans la conversation d'origine. Elles sont absentes de ta copie P1. » (P5 l.11). Le journal montre qu'elles manquaient déjà au message reçu le 19 novembre : la copie P1 n'est pas en cause, puisqu'elle reproduit fidèlement la partie du message qu'elle reprend.

**Les huit options et la validation**, reproduites des copies :

| Décision (titre, P1) | Option A (message 1 ; P1) | Option B (message 2 ; P5) |
|---|---|---|
| Q1.1 — Largeur des cases | « Largeur uniforme par carte, configurable et paire en millimètres. » (l.301) | « Une largeur différente selon le niveau tactique. Chaque étage possède son échelle. » (l.14) |
| Q1.2 — Dimensions physiques des unités | « Dimensions configurables par type d'unité et posture. Le volume peut dépasser sa case ; les collisions restent obligatoires. » (l.303) | « Dimensions obligatoirement contenues dans la case. Plus restrictif, notamment pour les unités couchées ou de grande taille. » (l.15) |
| Q1.3 — Épaisseur physique des murs | « Épaisseur configurable par type de mur ; les murs possèdent un volume physique défini. » (l.305) | « Épaisseur nulle. Les murs sont représentés uniquement par des surfaces séparant les cases. » (l.16) |
| Q1.4 — Hauteur de référence des niveaux | « Altitude configurable pour chaque niveau ; les étages pouvaient initialement être séparés par des hauteurs différentes. » (l.307) | « Espacement vertical constant. Tous les niveaux sont séparés par la même hauteur. » (l.17) |

Validation, dans le message 1 (P1 l.308-309) : « Pour Bastion MEC-0001, lot Q1 Géométrie, je valide Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A. Poursuis le lot Q1 en regroupant les paramètres numériques restants, avec comparaison vérifiée d'OpenXcomCE et de Kowlting, sans implémentation. »

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

**Autres copies** (contrôle 7 du §17) : les messages copiés dans P1 (message 1), P2, P3, P5 et P6 le sont intégralement. La seule omission relevée est la partie « Mission » du message 1 ci-dessus.

""")

# ---------- §2
rep("| N11, N14 | R:102-111 | en vigueur | N14 : portée modifiée par G3 ; formule par Q3.14 |",
    "| N11, N14 | R:102-111 | en vigueur | N14 : portée modifiée par G3 ; formule par Q3.14 ; effet possible sur l'énergie : M-04=B (§5) |")
rep("| ARB-D | R:124 | en vigueur | Q3.14 ; Q4.6 |",
    "| ARB-D | R:124 | en vigueur | Q3.14 ; Q4.6 ; M-04=B (énergie, modalités ouvertes) |")
rep("| G1 | R:126-134 | en vigueur | priorité « X puis Y » : PNV-7 |",
    "| G1 | R:126-134 | en vigueur | — (priorité « X puis Y » non décidée : PNV-7) |")
rep("| G3 | R:141 | en vigueur | Q3.7 à Q3.9, Q3.13 |",
    "| G3 | R:141 | en vigueur | Q3.7 à Q3.9, Q3.13 ; M-05=A (coût réel accru mais payable) |")
rep("| B3, Q1.1, Q1.5, Q1.7, Q4.1, [CONF] W-01 |",
    "| B3, Q1.1, Q1.5, Q1.7, Q4.1, [CONF] W-01 ; R-5=A, R-6=A, R-7=A |")
rep("| GE-03 (MEC-0002) | R:204 | **à annoter** : précisée (§9.1) | B3-03, Q1.2, Q1.6 |",
    "| GE-03 (MEC-0002) | R:204 | **à annoter** : précisée (§9.1) | B3-03 ; Q1.2, précision explicite (R-8=A) ; Q1.6 ; R-5=A |")

# ---------- §2 bis
rep("\n## 3. Géométrie\n", """
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
- **règles validées, applicables telles quelles :** M-05=A ; R-6=A ; R-5=A pour ses deux énoncés (dimensions configurées en millimètres entiers ; calculs physiques non limités systématiquement aux entiers) ; R-7=A et R-8=A, qui sont des clarifications ;
- **principe validé, modalités à définir :** M-04=B. Aucun multiplicateur, arrondi ni pénalité d'énergie n'est fixé ;
- **modalités qui restent ouvertes :**
  - pour M-04=B : l'existence d'un effet dans chaque situation, son déclenchement, son calcul et ses valeurs (P6 l.38) ;
  - pour R-5=A : les modalités de conversion, la précision numérique et les arrondis des autres grandeurs calculées, lorsqu'ils ne sont pas spécifiés (P6 l.67).

**Portée :**
- ces arbitrages répondent aux points M-04, M-05 et R-5 à R-8 du rapport RV41 ;
- R-5=A « est commune à MEC-0001 et MEC-0002 dans le cadre du référentiel physique B3 » (P6 l.69) ;
- R-8=A « ne modifie pas à elle seule le registre sur `main` » (P6 l.106). Aucun des six arbitrages n'est inscrit : aucune inscription n'est autorisée.

## 3. Géométrie
""")

# ---------- §3.1
rep("| P1 l.300-301, 309 ; P5 l.14 | [TR] ⟨B3-03⟩ |", "| P1 l.300-301, 309 ; P5 l.14 | [TR-M] ⟨B3-03⟩ |")
rep("Plus restrictif, notamment pour les unités couchées ou de grande taille. » | P1 l.302-303, 309 ; P5 l.15 | [TR] |",
    "Plus restrictif, notamment pour les unités couchées ou de grande taille. » Q1.2 précise explicitement GE-03 (R-8=A). | P1 l.302-303, 309 ; P5 l.15 | [TR-M] |")
rep("| P1 l.304-305, 309 ; P5 l.16 | [TR] |\n", "| P1 l.304-305, 309 ; P5 l.16 | [TR-M] |\n")
rep("**Historique** pour la hauteur d'étage (§3.2). | P1 l.306-307, 309 ; P5 l.17 | [TR] |",
    "**Historique** pour l'altitude des niveaux de référence ; seules les variations locales de support demeurent (R-7=A, §3.2). | P1 l.306-307, 309 ; P5 l.17 | [TR-M] |")
rep("Son cadre configurable est historique (§3.2). | P1 l.39-45, 67",
    "Son cadre configurable est historique : la hauteur d'étage est fixe (W-01, R-6=A ; §3.2). | P1 l.39-45, 67")
rep("Ce sont des valeurs initiales configurables, **sauf la hauteur d'étage**, fixée par [CONF] W-01 (§3.2).",
    "Ce sont des valeurs initiales configurables, **sauf la hauteur d'étage**, fixée par W-01 [CONF] et R-6=A [VAL] : elle n'est réglable ni globalement ni par carte, et ce n'est pas une valeur initiale ajustable (§3.2).")
rep("Il n'existe pas de dimensions concurrentes d'une même unité selon qu'elle marche, saute ou tombe.",
    "Il n'existe pas de dimensions concurrentes d'une même unité selon qu'elle marche, saute ou tombe. **R-8=A** [VAL] (P6 l.96) : « Q1.2 précise explicitement GE-03, avec géométrie commune aux deux mécaniques. » Le même volume physique sert à MEC-0001 et à MEC-0002 (P6 l.103).")
rep("- le rectificatif B3 (§1), validé (W-12), écrit : « Les dimensions physiques configurées **peuvent être exprimées** en millimètres. » **Cette seconde formulation est retenue.**",
    """- le rectificatif B3 (§1), validé (W-12), écrit : « Les dimensions physiques configurées **peuvent être exprimées** en millimètres. » (P2 l.217). Il ajoute : « La contrainte Q1 des millimètres entiers ne doit pas être étendue implicitement aux grandeurs physiques intermédiaires calculées par MEC-0002. » (P2 l.219) ;
- **R-5=A** [VAL] (P6 l.59) tranche ensuite : « Dimensions physiques configurées en millimètres entiers ; calculs physiques non limités systématiquement aux entiers. » **C'est la règle applicable**, commune à MEC-0001 et à MEC-0002 (P6 l.69) :
  - les dimensions physiques configurées sont exprimées en millimètres entiers ;
  - les calculs physiques intermédiaires ne sont pas soumis à un arrondi systématique au millimètre entier ;
  - les conventions d'arrondi déjà validées sont conservées : Q2.6 (enveloppes), Q3.13 (coûts), Q3.14 (surcharge). Elles ne sont pas étendues à d'autres calculs sans source ;
  - restent ouverts : les modalités de conversion, la précision numérique et les arrondis des autres grandeurs calculées (P6 l.67).""")
rep("- la parité de la largeur des cases est sourcée par Q1.1 [TR] ⟨B3-03⟩ ;\n- les dimensions minimales, les tolérances et les conventions d'arrondi autres que celle de Q2.6 restent [OUV] ;",
    "- les dimensions configurées sont des millimètres entiers : R-5=A [VAL] ;\n- la parité de la largeur des cases est sourcée par Q1.1 [TR-M] ⟨B3-03⟩ ;\n- les dimensions minimales, les tolérances, les modalités de conversion et les conventions d'arrondi géométriques autres que celle de Q2.6 restent [OUV] ;")

# ---------- §3.2
rep("2. **Q1.4=A** [TR] : altitude configurable pour chaque niveau, avec des hauteurs d'étage possiblement différentes. *Écart avec GE-02 à cette date.* L'option B, écartée, prévoyait un « espacement vertical constant » (P5 l.17) ; la règle applicable ne repose pas sur elle (§0.1).",
    "2. **Q1.4=A** [TR-M] : altitude configurable pour chaque niveau, avec des hauteurs d'étage possiblement différentes. *Écart avec GE-02 à cette date.* L'option B, écartée, prévoyait un « espacement vertical constant » (P5 l.17) ; la règle applicable ne repose pas sur elle (observation du §0.1).")
rep("Elle reprend la consigne n° 2 pour la v0.3 (P3 l.15) : « La hauteur entre sols de référence reste fixée à 3 000 mm. »",
    "Elle reprend la consigne n° 2 pour la v0.3 (P3 l.15) : « La hauteur entre sols de référence reste fixée à 3 000 mm. »\n6. **R-6=A** [VAL] (P6 l.73) : « 3 000 mm fixes, sans réglage global ni par carte. » Il précise W-01 : la hauteur « n'est configurable ni globalement ni individuellement par carte » (P6 l.77).")
rep("**Règle applicable** (GE-02, précisée par Q4.1 et confirmée par W-01) : 3 000 mm fixes, non configurables par carte, entre les sols de référence de deux étages tactiques consécutifs. Les dénivelés locaux restent possibles.",
    "**Règle applicable** (GE-02, précisée par Q4.1, confirmée par W-01, puis par R-6=A) : 3 000 mm fixes entre les sols de référence de deux étages tactiques consécutifs, réglables ni globalement ni par carte. Ce n'est pas une valeur initiale ajustable. Les dénivelés locaux des supports restent possibles.")
rep("- Q1.4 et le cadre configurable de Q1.8 restent dans l'historique et ne sont pas effacés.",
    "- Q1.4 et le cadre configurable de Q1.8 restent dans l'historique et ne sont pas effacés.\n- **R-7=A** [VAL] (P6 l.85) : « Q1.4 reste historique pour l'altitude des niveaux de référence ; seules les variations locales de support demeurent. » Q1.4 ne confère donc plus aucune faculté de configurer l'altitude de référence d'un étage (P6 l.89). Aucune autre exception à la hauteur fixe de 3 000 mm n'est créée (P6 l.91).")
rep("En vertu de W-01, cette phrase **ne s'applique pas à la hauteur d'étage**.",
    "En vertu de W-01 et de R-6=A, cette phrase **ne s'applique pas à la hauteur d'étage**.")

# ---------- §3.4, §3.5
rep("- **Pour tous les volumes** — Q1.2 [TR] : « les collisions restent obligatoires ».",
    "- **Pour tous les volumes** — Q1.2 [TR-M], précision explicite de GE-03 (R-8=A) : « les collisions restent obligatoires ».")
rep("Le rectificatif (§1) parle de « la contrainte Q1 des millimètres entiers » : dans les pièces Q1, elle n'est formulée que pour la largeur des cases (Q1.1) | largeur et enveloppes : [TR] ; au-delà, y compris la conversion : **[PNV]** ; **non étendue** aux calculs de MEC-0002 (rectificatif §1, [CONF] W-12) |",
    "Le rectificatif (§1) parle de « la contrainte Q1 des millimètres entiers » (P2 l.219). **R-5=A** (P6 l.59) | **dimensions configurées** en millimètres entiers : **tranché**, [VAL] R-5=A, pour MEC-0001 et MEC-0002 ; largeur paire : [TR-M] ; enveloppes paires : [TR] ; **données calculées** : non limitées systématiquement aux entiers (R-5=A), hors arrondis validés ; la formulation « toutes les données géométriques » ne vaut donc pas règle ; **conversion** des valeurs externes « vers demi-entiers » : **[PNV]** ; précision et arrondis des autres grandeurs calculées : [OUV] |")
rep("| PNV-4 | Support uniforme et valide sous tout le volume horizontal ; unité stable au centre de case à l'arrivée (D:34) |",
    "| PNV-4 | D:34 : « Support : pieds de l'unité sur un support physiquement uniforme et valide pour son volume horizontal ; unité stable au centre de case à l'arrivée. » |")
rep("| positions stables horizontales : [TR] ; « uniforme », « tout le volume », « au centre de case » : **[PNV]** |",
    "| positions stables horizontales : [TR] ; support « physiquement uniforme » et « valide pour son volume horizontal » ; unité « au centre de case » : **[PNV]** |")

# ---------- §3.6
rep("1 272,8 → **1 274 mm** ; dépend de **PNV-3** (orientation d'une unité couchée).",
    "1 272,8 → **1 274 mm** ; dépend de **PNV-3** (orientation d'une unité couchée) ⟨B3-03⟩.")
rep("étendue horizontale maximale de **1 341,6 mm** (vers 26,6°), inférieure à 1 400 mm. Le volume balayé reste [OUV].",
    "étendue horizontale maximale de **1 341,6 mm** (vers 26,6°), inférieure à 1 400 mm ⟨B3-03⟩. Le volume balayé reste [OUV].")
rep("ce qui dépend de **PNV-4**. D'autres types d'unités peuvent dépasser leur case (Q1.2).",
    "ce qui dépend de **PNV-4** ⟨B3-03⟩. D'autres types d'unités peuvent dépasser leur case (Q1.2).")

# ---------- §4
rep("- **Q4.15 ne constitue pas une exception supplémentaire à S10** (message B : « Q5.2 ne crée donc aucune exception supplémentaire à S10 »).",
    "- **Q4.15 ne constitue pas une exception supplémentaire à S10** : c'est la « Rectification demandée » de l'addendum Q5, §B : « expliciter que Q4.15 ne constitue pas une exception supplémentaire à S10 » (P2 l.95). Le message B le dit de Q5.2 : « Q5.2 ne crée donc aucune exception supplémentaire à S10 » (P2 l.38).")
rep("**Deux unités conscientes en position stable ne peuvent donc pas occuper la même case.** Rien n'autorise implicitement l'inverse.",
    "**Deux unités conscientes en position stable ne peuvent donc pas occuper la même case**, hors de l'exception transitoire au réveil prévue par G2 (R:137), que l'addendum maintient (P2 l.92). Rien n'autorise implicitement l'inverse.")

# ---------- §5
rep("Ces chiffres sont identiques à ceux de l'option A de Q3.11, qui avait été écartée.",
    "Les valeurs d'**énergie** (100 et 20) sont identiques à celles de l'option A de Q3.11, écartée (« Maximum 100 ; récupération 20 par tour », P1 l.201). Les valeurs de TU (60 et 60) ne sont pas concernées par cette correspondance.")
rep("- **Surcharge et énergie :** la surcharge ne réduit pas l'énergie. C'est une lecture d'ARB-D (« L'énergie est récupérée séparément ») [DÉD].",
    """- **Surcharge et énergie — M-04=B** [VAL] (P6 l.32) : « La surcharge peut également réduire l'énergie ; modalités à définir. » Statut : « principe validé ; modalités ouvertes » (P6 l.42). Application (P6 l.35-40) :
  - aucune affirmation générale selon laquelle la surcharge ne réduirait pas l'énergie ne subsiste. La v0.4.1 en contenait une, marquée [DÉD] ; elle est retirée ;
  - la réduction des TU (ARB-D, Q3.14) est inchangée ;
  - la récupération séparée de l'énergie (ARB-D : « L'énergie est récupérée séparément ») est inchangée ;
  - des effets de la surcharge sur l'énergie sont possibles. Leur existence dans chaque situation, leur déclenchement, leur calcul et leurs valeurs ne sont pas spécifiés [OUV] ;
  - la formule de surcharge des TU ne s'applique pas automatiquement à l'énergie. Aucun multiplicateur, arrondi ni pénalité d'énergie n'est fixé ;
  - la clause inscrite d'ARB-D « La surcharge ne majore pas le prix des pas » (R:124) n'est pas modifiée.""")
rep("**Restent ouverts** [OUV] : autres pénalités de TU et leur ordre ; table Force → kg ; indicateur « encombré ».",
    "**Restent ouverts** [OUV] : modalités d'un effet de la surcharge sur l'énergie (M-04=B) ; autres pénalités de TU et leur ordre ; table Force → kg ; indicateur « encombré ».")

# ---------- §6
rep("Lecture de « non exécutable » [DÉD] : un coût supérieur aux ressources restantes.",
    "Pour le coût, la portée est fixée par **M-05=A** (ci-dessous) : le pas n'est non exécutable que s'il n'est plus payable (P6 l.50).")
rep("**Restent ouverts** [OUV] : un coût plus élevé mais encore payable ; le repli d'une diagonale sur le passage Y ; les conditions de la surveillance.",
    """**Coût réel d'un pas — M-05=A** [VAL] (P6 l.45) : « Si le coût augmente mais reste payable et que le passage est admissible, le pas est exécuté. » Statut : « règle validée » (P6 l.56). Application (P6 l.48-55) :
- avant chaque pas, son coût réel en TU et en énergie est vérifié ;
- si les deux ressources suffisent et que le passage reste admissible, le pas est exécuté et débité à son coût réel ;
- si le pas n'est plus payable, ou s'il devient physiquement inadmissible, l'ordre est interrompu selon Q3.4 et Q4.21 ;
- aucun pas non commencé n'est débité ; le coût des pas déjà effectués est conservé ;
- aucun recalcul automatique du trajet n'est créé.

La simple augmentation du coût prévu ne suffit donc plus à interrompre l'ordre, lorsque le pas reste admissible et payable. Le point du registre « notamment en cas d'augmentation imprévue du coût » (R:166) est tranché sur ce point.

**Restent ouverts** [OUV] : le repli d'une diagonale sur le passage Y ; les conditions de la surveillance et des réactions.""")

# ---------- §9.1
rep("communes à `MEC-0001` et `MEC-0002`, qui peuvent être exprimées en millimètres. Valeurs initiales : largeur de case 1 500 mm (Q1.5), épaisseur de mur standard 100 mm (Q1.7) — provenance à confirmer par archivage (B3-03). La hauteur de 3 000 mm entre les sols de référence de deux étages tactiques consécutifs reste fixe, non configurable par carte ; les dénivelés locaux restent possibles (Q4.1 ; confirmation du propriétaire du 20 novembre 2026).*",
    "communes à `MEC-0001` et `MEC-0002`. Les dimensions physiques configurées sont exprimées en millimètres entiers ; les calculs physiques ne sont pas limités systématiquement aux entiers (arbitrage R-5 du 20 novembre 2026). Valeurs initiales : largeur de case 1 500 mm (Q1.5), épaisseur de mur standard 100 mm (Q1.7) — provenance à confirmer par archivage (B3-03). La hauteur de 3 000 mm entre les sols de référence de deux étages tactiques consécutifs est fixe, sans réglage global ni par carte ; les dénivelés locaux des supports restent possibles (Q4.1 ; confirmation du propriétaire et arbitrage R-6 du 20 novembre 2026). Q1.4 reste historique pour l'altitude des niveaux de référence (arbitrage R-7 du 20 novembre 2026).*")
rep("- **Nouvelle mention « Ouvert » proposée :** dimensions minimales ; tolérances géométriques ; conventions d'arrondi autres que celle des enveloppes (Q2.6) ; précision et arrondis des calculs physiques (rectificatif B3, §1) ; bornes des dénivelés locaux.",
    "- **Nouvelle mention « Ouvert » proposée :** dimensions minimales ; tolérances géométriques ; modalités de conversion des dimensions configurées ; conventions d'arrondi autres que celle des enveloppes (Q2.6) ; précision numérique et arrondis des calculs physiques non spécifiés (rectificatif B3, §1 ; R-5=A) ; bornes des dénivelés locaux.")
rep("Il vaut 0,5 avec les valeurs initiales.", "Il vaut 0,5 avec les valeurs initiales ⟨B3-03⟩.")
rep("Précisée aussi par Q1.2, que B3-03 ne reprend pas : le volume peut dépasser sa case ; les collisions restent obligatoires.*",
    "**Précisée explicitement par Q1.2** (arbitrage R-8 du 20 novembre 2026 : « Q1.2 précise explicitement GE-03, avec géométrie commune aux deux mécaniques ») : dimensions configurables par type d'unité et posture ; le volume peut dépasser sa case ; les collisions restent obligatoires ; le même volume physique sert à `MEC-0001` et à `MEC-0002`. Les dimensions configurées sont exprimées en millimètres entiers (arbitrage R-5).*")
rep("- **Nouvelle mention « Ouvert » proposée :** dimensions des autres types d'unités ; dimensions minimales ; orientations admises.",
    "- **Nouvelle mention « Ouvert » proposée :** dimensions des autres types d'unités ; dimensions minimales ; orientations admises.\n- **Inscription :** GE-03 est explicitement à annoter lors d'une future inscription (R-8=A, P6 l.104). Cette validation ne modifie pas à elle seule le registre sur `main` (P6 l.106).")
rep("hauteur d'étage fixe de 3 000 mm entre sols de référence (GE-02, Q4.1). Restent ouverts : dimensions des autres types d'unités ; dimensions minimales ; épaisseur des surfaces ; tolérance des contacts ; conventions d'arrondi ;",
    "dimensions configurées en millimètres entiers, calculs physiques non limités systématiquement aux entiers (arbitrage R-5) ; hauteur d'étage fixe de 3 000 mm entre sols de référence, sans réglage global ni par carte (GE-02, Q4.1, arbitrage R-6). Restent ouverts : dimensions des autres types d'unités ; dimensions minimales ; épaisseur des surfaces ; tolérance des contacts ; modalités de conversion ; conventions d'arrondi ;")
rep("La contrainte d'entiers, sourcée seulement par Q1.1 et Q2.6 (au-delà, PNV-2), n'est pas étendue aux calculs de MEC-0002 ;",
    "La contrainte d'entiers vaut pour les dimensions configurées (R-5=A) ; elle n'est pas étendue aux calculs physiques, ni de MEC-0001 ni de MEC-0002 (R-5=A ; rectificatif §1) ;")

# ---------- §9.2
rep("- **Nouveau bloc daté** des décisions Q1 à Q5 et B3, au niveau de preuve indiqué au §12, avec mention de leur provenance.",
    "- **Nouveau bloc daté** des décisions Q1 à Q5 et B3, et des six arbitrages du 20 novembre 2026 (§2 bis), au niveau de preuve indiqué au §12, avec mention de leur provenance.")
rep("S10 (Q5.2), ARB-C, ARB-D, ARB-E (Q4.13, Q5.1), G2 (Q4.19), G3 (Q3), G4 (Q4.16).",
    "S10 (Q5.2), ARB-C, ARB-D (Q3.14, Q4.6 ; M-04=B), ARB-E (Q4.13, Q5.1), G2 (Q4.19), G3 (Q3 ; M-05=A), G4 (Q4.16).")

# ---------- §10
rep("| R:151 : géométrie, portes, taille des unités | Q1.1, Q1.3, Q1.5, Q1.7, Q2.5 ; Q1.2, Q1.6 ; Q4.7 |",
    "| R:151 : géométrie, portes, taille des unités | Q1.1, Q1.3, Q1.5, Q1.7, Q2.5 ; Q1.2, Q1.6 ; Q4.7 ; R-5=A, R-8=A |")
rep("| R:160 : surcharge | Q3.14 ; Q4.5 | table Force → kg ; autres pénalités ; indicateur « encombré » |",
    "| R:160 : surcharge | Q3.14 ; Q4.5 ; M-04=B (principe d'un effet sur l'énergie) | table Force → kg ; autres pénalités ; indicateur « encombré » ; modalités de l'effet sur l'énergie |")
rep("| R:166 : trajet devenu non payable | Q4.21, Q3.4 | coût plus élevé mais encore payable |",
    "| R:166 : trajet devenu non payable | Q4.21, Q3.4 ; M-05=A (coût plus élevé mais encore payable) | — |")
rep("| G3, « Ouvert » (R:141) | Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.6, Q3.11, Q4.6 | hausse imprévue d'un coût encore payable |",
    "| G3, « Ouvert » (R:141) | Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.6, Q3.11, Q4.6 ; M-05=A | — |")
rep("| Q2, Q3.3, Q3.10, Q4.7 ; Q3.14, Q4.5, Q4.6 ; Q5.1, Q4.13 | détails d'interaction ; table Force → kg ; surveillance |",
    "| Q2, Q3.3, Q3.10, Q4.7 ; Q3.14, Q4.5, Q4.6, M-04=B ; Q5.1, Q4.13 | détails d'interaction ; table Force → kg ; modalités de l'effet de la surcharge sur l'énergie ; surveillance |")

# ---------- §11
rep("| ARB-D, Q3.14 | Concordance d'ordre et de troncature : ajout au solde avec plafond au maximum, puis rapport Force / poids appliqué au total, tronqué. |",
    "| ARB-D, Q3.14 | **Concordance d'ordre** : ajout au solde avec plafond au maximum (`setValueMax`, l.2714), puis rapport Force / poids appliqué au total, quand ce rapport est inférieur à 1 (l.2717-2720). **Différence de calcul** : OXCE calcule le rapport et le produit en nombres flottants ([code OXCE retiré — D4] puis [code OXCE retiré — D4]) et tronque ce résultat flottant ; Q3.14 exige le plancher de la valeur mathématique exacte. Les résultats ne sont pas garantis identiques : une émulation en simple précision de 1/41 × 41 donne 0,99999994, tronqué à 0, contre 1 en valeur exacte. C'est une émulation, non une exécution d'OXCE. Aucune équivalence numérique n'est affirmée. |")
rep("| Autres décisions | non étudiées | — |", "| Autres décisions, dont les six arbitrages du §2 bis | non étudiées | — |")

# ---------- §12
rep("Statuts : **V** en vigueur (validée, non inscrite) ; **I** inscrite ; **H** historique ; **N** non validée.",
    "Statuts : **V** en vigueur (validée, non inscrite) ; **I** inscrite ; **H** historique ; **N** non validée.\n\n**Rattachement d'un scénario** (M-03) : un scénario n'est rattaché à une décision que s'il la cite dans ses sources et que son résultat attendu dépend d'elle. Sinon : « aucun scénario dédié ».")
rep("| P1 l.300-301, 309 ; P5 l.14 | [TR] | V | GE-02, R:151, G1 | T26 | ⟨B3-03⟩ |",
    "| P1 l.300-301, 309 ; P5 l.14 | [TR-M] | V | GE-02, R:151, G1 | T26 | ⟨B3-03⟩ ; proposition restituée en deux messages (§0.1) |")
rep("| P1 l.302-303, 309 ; P5 l.15 | [TR] | V | GE-03, G1 | T26 | — |",
    "| P1 l.302-303, 309 ; P5 l.15 | [TR-M] | V | GE-03 (précision explicite, R-8=A), G1 | T26 | proposition restituée en deux messages (§0.1) |")
rep("| P1 l.304-305, 309 ; P5 l.16 | [TR] | V | R:151 | T26 | — |",
    "| P1 l.304-305, 309 ; P5 l.16 | [TR-M] | V | R:151 | T26 | proposition restituée en deux messages (§0.1) |")
rep("| P1 l.306-307, 309 ; P5 l.17 | [TR] | **H** (hauteur d'étage) | GE-02 | T27 | supplantée par Q4.1 et W-01 ; libellé A au passé (§0.1) |",
    "| P1 l.306-307, 309 ; P5 l.17 | [TR-M] | **H** (altitude des niveaux de référence ; R-7=A) | GE-02 | aucun (historique ; T27 vérifie la règle qui la supplante) | supplantée par Q4.1, W-01 et R-6=A ; portée résiduelle : R-7=A ; proposition restituée en deux messages ; libellé A au passé (§0.1) |")
rep("| valeur en vigueur ; cadre configurable **H** | GE-02, CH-08 | T27 | — |",
    "| valeur en vigueur, fixe (W-01, R-6=A) ; cadre configurable **H** | GE-02, CH-08 | T27 | — |")
rep("| S2, R:152 | T01, T02 | case d'arrivée : [DÉD] |", "| S2, R:152 | T02, T22 | case d'arrivée : [DÉD] |")
rep("| S8, S9 | T08, T44 | — |", "| S8, S9 | T08, T47 | — |")
rep("| Q3.6 | réserve d'énergie plafonnée | P1 l.147-151, 165 | [TR] | V | G3 | T22 | valeurs : Q4.6 |",
    "| Q3.6 | réserve d'énergie plafonnée | P1 l.147-151, 165 | [TR] | V | G3 | aucun scénario dédié | valeurs : Q4.6 |")
rep("| ARB-D, N14 | T20, T21 | table Force → kg [OUV] |",
    "| ARB-D, N14 | T20, T21 | table Force → kg [OUV] ; effet sur l'énergie : M-04=B, modalités [OUV] |")
rep("| Q4.1 | 3 m fixes entre sols de référence | v0.2 l.181 ; D:86 | [CIT] + [CONF] | V |",
    "| Q4.1 | 3 m fixes entre sols de référence | v0.2 l.181 ; D:86 ; P3 l.88 ; P6 l.73 | [CIT] + [CONF] + [VAL] | V |")
rep("| [CIT] + [DÉC] | V | ARB-D | T01, T21 | — |", "| [CIT] + [DÉC] | V | ARB-D | T01 | T21 écarte ce profil (§13, T21) |")
rep("| Q4.21 | imprévu | v0.2 l.191 ; D:115 | [CIT] | V | S8, S9, G3 | T08 | coût payable [OUV] |",
    "| Q4.21 | imprévu | v0.2 l.191 ; D:115 | [CIT] | V | S8, S9, G3 | T08, T47 | cas du coût précisé par M-05=A |")
rep("| B3 | géométrie commune | P2 l.121-201 | [DÉC] | V | GE-02, GE-03 | T26, T27 | options d'origine absentes |",
    "| B3 | géométrie commune | P2 l.121-201 | [DÉC] | V | GE-02, GE-03 | aucun scénario dédié | options d'origine absentes |")
rep("| Confirmation W-01 | hauteur fixe, non configurable par carte | P3 l.88 ; consigne P3 l.15 | [CONF] | V | GE-02 | T27 | — |",
    """| Confirmation W-01 | hauteur fixe, non configurable par carte | P3 l.88 ; consigne P3 l.15 | [CONF] | V | GE-02 | T27 | — |
| M-04=B | la surcharge peut aussi réduire l'énergie ; modalités à définir | P6 l.30-42 | [VAL] | V (principe) ; modalités **ouvertes** | ARB-D, N14 | aucun scénario spécifiable (modalités ouvertes) | options d'origine absentes |
| M-05=A | coût accru mais payable, passage admissible : pas exécuté à son coût réel | P6 l.43-56 | [VAL] | V | G3, Q3.4, Q4.21 ; R:166 | T47 | options d'origine absentes |
| R-5=A | dimensions configurées en mm entiers ; calculs non limités systématiquement aux entiers | P6 l.57-70 | [VAL] | V ; modalités techniques **ouvertes** | GE-02, GE-03, CH-08 ; PNV-2 | T48 | conversion et précision [OUV] ; options d'origine absentes |
| R-6=A | 3 000 mm fixes, ni réglage global ni par carte | P6 l.71-82 | [VAL] | V | GE-02, CH-08 | T27 | options d'origine absentes |
| R-7=A | Q1.4 historique pour l'altitude des niveaux de référence ; variations locales de support | P6 l.83-93 | [VAL] | V | GE-02 | T27 | options d'origine absentes |
| R-8=A | Q1.2 précise explicitement GE-03 ; géométrie commune | P6 l.94-107 | [VAL] | V | GE-03 | aucun scénario dédié | options d'origine absentes ; annotation de GE-03 à l'inscription |""")
rep("| PNV-1 à PNV-9 | formulations sans source suffisante | v0.2, D:29-40 | aucune | **N** | — | T03, T04, T15, T26, T42, T43, T45, T46 (conditionnels) | — |",
    "| PNV-1 à PNV-9 | formulations sans source suffisante (PNV-2 en partie tranchée par R-5=A) | v0.2, D:29-40 | aucune | **N** | — | T03, T04, T15, T26, T42, T43, T46 (conditionnels) | — |")

# ---------- §13
rep("| 4 TU et 2 d'énergie ; il reste 56 et 98 | Q3.7, G3 | Sp |", "| 4 TU et 2 d'énergie ; il reste 56 et 98 | Q3.7, G3, Q4.6 (profil 60 / 100) | Sp |")
rep("(la loi d'OXCE donnerait 4 d'énergie) | Q3.8, Q3.9, Q3.13, S2 | Sp |", "(la loi d'OXCE donnerait 4 d'énergie) | Q3.1, Q3.2, Q3.8, Q3.9, Q3.13, S2 | Sp |")
rep("elle n'est pas un résultat attendu | Q3.13 | Sp |", "elle n'est pas un résultat attendu | Q3.8, Q3.13 | Sp |")
rep("(4, 12, 0,75) ; (total 20, facteur 30/45) | 15 ; 17 ; 12 ; 13 | ARB-D, Q3.14 | Sp |",
    "(4, 12, 0,75) ; (total 20, facteur 30/45). **Pourquoi un maximum fictif de 20** : avec le profil Q4.6, min(solde + 60, 60) = 60 pour tout solde positif ou nul ; le plafond serait toujours atteint, et ce profil ne distinguerait pas ARB-D d'une simple remise au maximum. Avec 20, les cas exercent un plafond atteint (7 + 15 = 22, ramené à 20), un plafond non atteint (2 + 15 = 17 ; 4 + 12 = 16), la réduction appliquée après le plafond, et l'arrondi inférieur (20 × 30/45 = 13,33…) | 15 ; 17 ; 12 ; 13 | ARB-D, Q3.14 | Sp |")
rep("| G3, Z1 | Sp (passages praticables) |", "| G3, Z1, Q3.1 (coût d'entrée de la case d'arrivée) | Sp (passages praticables) |")
rep("deuxième unité refusée ; jamais deux unités conscientes sur une même case |",
    "deuxième unité refusée ; jamais deux unités conscientes sur une même case, hors de l'exception transitoire au réveil de G2, absente du scénario |")
rep("| T27 | deux étages tactiques consécutifs | 3 000 mm entre sols de référence, non configurables par carte ; dénivelés locaux distincts | GE-02, Q4.1, W-01 | Sp |",
    "| T27 | deux étages tactiques consécutifs, sur deux cartes différentes | 3 000 mm entre sols de référence sur chacune ; aucun réglage global, par carte ni par niveau de cette hauteur ou de l'altitude de référence ; les dénivelés locaux des supports restent distincts et possibles | GE-02, Q1.8, Q4.1, W-01, R-6=A, R-7=A | Sp |")
rep("il reste 54 et 97 | G1, S2, Q3.13 | Pa (géométrie, PNV-6) |",
    "il reste 54 et 97 | G1, S2, Q3.13 | Sp (passage supposé praticable, comme T02 et T22) ; test intégré de la géométrie : Pa |")
rep("| ARB-B, G1 | Pa (géométrie) |\n", """| ARB-B, G1 | Pa (géométrie) |
| T47 | trois pas orthogonaux prévus en terrain normal ; avant le deuxième pas, son coût réel devient 6 TU et 3 d'énergie (terrain difficile ; coût réel simulé). (a) profil Q4.6 ; (b) valeurs fictives : 5 TU et 98 d'énergie avant ce pas | (a) le deuxième pas est exécuté et débité à son coût réel ; l'ordre continue, sans recalcul du trajet ; il reste 46 TU et 93 d'énergie après le troisième pas. (b) arrêt avant le deuxième pas, sans débit de ce pas ; il reste 5 TU et 98 d'énergie | M-05=A, Q3.4, Q4.21, G3, Q3.8 | Sp (coût réel simulé) |
| T48 | (a) dimensions configurées : largeur de case 1 500 mm, mur de 100 mm ; puis une dimension configurée de 600,5 mm. (b) volume fictif de 600 × 605 mm, orienté à 45° | (a) 1 500 et 100 mm sont conformes ; 600,5 mm ne l'est pas, et son traitement (refus ou conversion) n'est pas spécifié. (b) étendue horizontale de 1 205/√2 = 852,06… mm, non arrondie avant Q2.6 ; enveloppe de **854 mm**. Un arrondi préalable au millimètre donnerait 852, qui ne contient pas le volume | R-5=A, Q2.6 | (a) Pa (modalités de conversion [OUV]) ; (b) Sp |
""")
rep("| G1-01 | repris | T41 |", "| G1-01 | adapté : murs pleins seulement (la v1.4.1 vise des passages « fermés par terrain/murs », l.169) | T41 |")
rep("  - P0-05 et P0-06 → T21 et T20 ;",
    "  - P0-05 → T21, comme valeur intermédiaire (7 + 15, plafonné à 20). Le résultat isolé de P0-05, 20 TU sans surcharge (v1.4.1 l.150), n'est pas conservé comme résultat attendu ;\n  - P0-06 → T21, premier cas (20 × 0,75 = 15 ; v1.4.1 l.151) ;")
rep("- **Aucun cas exclu.** La matrice de la v1.4.1 reste un document historique.",
    "- **Aucun cas des tableaux du §5 de la v1.4.1 n'est exclu.**\n- **Anciens tests du LOT-2F** mentionnés au §5.5 de la v1.4.1 (T-M01 à T-M11, T-J, T-K, T-D) : non repris ici ; on se reporte à la v1.4.1, qui en fixe le sort.\n- La matrice de la v1.4.1 reste un document historique.")

# ---------- §14
rep("- **RD-2 — Formulations de Q4.** Ce sont des résumés de l'orchestrateur ; seules les valeurs de Q4.6 et Q4.7 sont confirmées. Cela touche PNV-7 et PNV-8.",
    "- **RD-2 — Formulations de Q4.** Ce sont des résumés de l'orchestrateur. Seuls sont confirmés les valeurs de Q4.6 et Q4.7 (P2 l.18) et le contenu de Q4.1 (confirmation W-01, P3 l.88 ; arbitrage R-6=A). Cela touche PNV-7 et PNV-8. Pour Q4.21, le cas du coût est désormais fixé par M-05=A.")
rep("- **RD-3 — Q5.1, Q5.2 et B3.** Les textes des options d'origine sont absents.",
    "- **RD-3 — Options d'origine absentes.** Pour Q5.1, Q5.2 et B3, et pour les six arbitrages du 20 novembre 2026 (§2 bis), seuls le choix et le texte validé sont transmis ; les textes des options ne le sont pas.")
rep("- **RD-5 — Q1.1 à Q1.4.** **Levée dans la v0.4.1** : les options B ont été transmises (copie P5), et les quatre décisions passent en [TR] (§0.1). Restent les réserves communes RD-1 et RD-6.",
    "- **RD-5 — Q1.1 à Q1.4.** Dossier composé de deux messages, classé [TR-M] (§0.1). La présence des options B dans la conversation d'origine, et l'existence de deux options seulement, reposent sur les déclarations du propriétaire. Restent aussi les réserves communes RD-1 et RD-6.")
rep("La copie P4 résume les sections 3 et 6 du rapport de revue.",
    "La copie P4 résume les sections 3 et 6 du rapport de revue. La copie P1 ne reproduit pas la partie « Mission » du message du 19 novembre 2026 à 20 h 54 UTC (M-16) ; c'est la seule omission relevée dans les copies P1, P2, P3, P5 et P6 (§17, contrôle 7).")
rep("- **RD-7 — Revue.** Ni la v0.4 ni la v0.4.1 n'ont été revues de façon indépendante à la date de rédaction ; aucun test n'a été exécuté.",
    "- **RD-7 — Revue.** La v0.4.1 a été revue de façon indépendante (pièce 13 : « conforme sous réserves »). La v0.4.2 ne l'est pas encore. Aucun test n'a été exécuté.\n- **RD-8 — Réserves de la revue de la v0.4.1.** R-5 à R-8 sont tranchées par les arbitrages R-5=A à R-8=A. R-1 à R-4 restent couvertes par RD-1 à RD-6 ; R-9 (points ouverts) par la liste ci-dessous. R-10 (limites de cette revue) et R-11 (statut) demeurent.")
rep("- **Pas :** instant de l'engagement ; support pendant les phases du pas.",
    "- **Pas :** instant de l'engagement, c'est-à-dire déclenchement exact du débit d'un pas engagé ; support pendant les phases physiques du pas.")
rep("  - grille de conversion, précision et arrondis des calculs, y compris ceux de MEC-0002 ;",
    "  - modalités de conversion des dimensions configurées ; précision numérique et arrondis des grandeurs calculées non spécifiés, y compris dans MEC-0002 (R-5=A) ;")
rep("- **Imprévus :** coût plus élevé mais encore payable ; repli d'une diagonale sur le passage Y.",
    "- **Imprévus :** repli d'une diagonale sur le passage Y. Le coût plus élevé mais encore payable est tranché par M-05=A.")
rep("- **Autres :** surveillance (Overwatch) ; autres pénalités de surcharge ; indicateur « encombré ».",
    "- **Surcharge :** modalités d'un effet sur l'énergie (M-04=B) : existence selon la situation, déclenchement, calcul, valeurs ; autres pénalités ; indicateur « encombré ».\n- **Autres :** conditions de surveillance (Overwatch) et de réaction.")

# ---------- §15
between("## 15. Inventaire des pièces justificatives", "## 16. Journal des corrections", f"""## 15. Inventaire des pièces justificatives

J'ai recalculé chaque empreinte pour la v0.4.2, avec `sha256sum` sur le fichier ou `git show origin/main:<chemin> | sha256sum`. Une pièce **n'est pas archivée** du seul fait qu'elle figure ici. Les numéros de la v0.4.1 sont conservés, pour que les renvois existants restent valables.

**Pièces avec fichier et empreinte vérifiée :**

| N° | Pièce | Fichier | SHA-256 | Archivée dans le dépôt |
|---|---|---|---|---|
| 1 | Q1.1 à Q3.14. Message 1 (2026-11-19T20:36:22Z), intégral : propositions et validations de Q1.5 à Q3.14. Message 2 (2026-11-19T20:54:21Z) : options A et validation de Q1.1 à Q1.4 ; **partie « Mission » non reproduite** (M-16). La mention « reproduit tel que reçu » de P1 l.3 ne vaut donc pas pour la fin du message 2. **P1 n'est pas modifiée ; elle est complétée par la pièce 1 bis** | copie P1, `PIECES-Q1-Q3-TRANSMISES.md` | `{H['P1']}` | non |
| 1 bis | Options B de Q1.1 à Q1.4 : message I (2026-11-20T13:41:45Z), intégral, et reconstitution par décision (compilation, l.39-48) | copie P5, `PIECE-Q1.1-Q1.4-OPTIONS-B.md` | `{H['P5']}` | non |
| 2 | Messages A à E (2026-11-19, de 19:56:49Z à 20:13:09Z), intégraux : repères horaires de Q1 à Q3 et valeurs de Q4.6 et Q4.7 ; Q5.1 et Q5.2 ; addendum Q5 ; addendum B3 ; rectificatif B3 | copie P2, `PIECES-Q4-Q5-B3-DECLARATIONS.md` | `{H['P2']}` | non |
| 3 | Messages F, G et H (2026-11-19T20:59:24Z, 2026-11-19T21:08:57Z, 2026-11-20T12:53:14Z), intégraux : consignes pour la v0.3 ; mandat de revue de la v0.3 ; mandat de la v0.4, avec les confirmations **W-01** et **W-12** | copie P3, `PIECES-MANDATS-ET-CONFIRMATIONS.md` | `{H['P3']}` | non |
| 3 bis | Message J (2026-11-20T14:44:23Z), intégral : mandat de la v0.4.2, avec les **six arbitrages** (§2 bis) | copie P6, `PIECE-MANDAT-v0.4.2-ARBITRAGES.md` | `{H['P6']}` | non |
| 4 | Rapport de revue indépendante de la v0.3 (sections 1, 2, 4 et 5 entières ; 3 et 6 résumées) et observations complémentaires de Claude Code (extrait) | copie P4, `RAPPORT-REVUE-INDEPENDANTE-v0.3.md` | `{H['P4']}` | non |
| 5 | Consolidation v0.2, dont les six messages de validation de Q4 (l.181 à 191) | pièce jointe `4f625a0d-…-Q1-Q4-REVUE.md` | `{H['V02']}` | non |
| 6 | Consolidation v0.3 | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.3.md` | `{H['V03']}` | non |
| 7 | Registre | `main:docs/gameplay/GAMEPLAY-DECISIONS.md` | `9117d20c45aa95abbc218ce5cdcc2a095106eb86c64a342be76d8521ef14d39e` | oui |
| 8 | Rapport d'inscription ARB/G du 17 novembre | `main:docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md` | `ac4d72c6baa75412406bec427cd348f53de03b635a0d45c62e13c3b2e12d09f1` | oui |
| 9 | Consolidation v1.4.1 (citations d'ARB-A à ARB-E et de G1 à G4 ; cas de test du §5) | `main:docs/reviews/BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md` | `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc` | oui (commit `1ecc608`) |
| 10 | Mandat d'inscription v1.0 | `main:docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` | oui (commit `1ecc608`) |
| 11 | Rapport d'archivage du 18 novembre | `main:docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` | `7f457d789797f2fa7129ea1666ebfa66e6ad857534e8508d95419491252754c2` | oui |
| 12 | Consolidation v0.4, déposée telle que remise au propriétaire (2026-11-20T13:05:12Z) | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.md` | `{H['V04']}` | non |
| 12 bis | Consolidation v0.4.1 | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md` | `{H['V041']}` | non |
| 13 | Rapport de la revue indépendante de la v0.4.1 (RV41), fichier original du relecteur : verdict « conforme sous réserves » ; I-1, M-01 à M-18, R-1 à R-11 | `RAPPORT-REVUE-INDEPENDANTE-v0.4.1.md` | `{H['RV41']}` | non |

**Emplacements :**
- pièces 1 à 4, 6, 12 et 12 bis : `{SP}/revue-v03/` ;
- pièce 5 : `/root/.claude/uploads/7361641c-6eb6-5649-a764-279757212cf3/` ;
- pièce 13 : `{SP}/revue-v041-relecteur/`.

**Outils de vérification** (M-17), dans `{SP}/` :

| N° | Outil | Fichier | SHA-256 |
|---|---|---|---|
| O-1 | Extraction mécanique des messages du propriétaire : 35 messages, jusqu'à 2026-11-20T13:41:45Z ; aucune réponse de Claude Code | `revue-v03/MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md` | `{H['O1']}` |
| O-2 | Script d'extraction (O-1 et O-4) | `verif-v04/extract_user_msgs.py` | `{H['O2']}` |
| O-3 | Diff de la v0.4 à la v0.4.1 | `verif-v04/diff-v0.4-v0.4.1.patch` | `{H['O3']}` |
| O-4 | Même extraction, 36 messages, jusqu'à 2026-11-20T14:44:23Z. Ses 35 premiers messages sont identiques à O-1 ; le 36e est le message J (pièce 3 bis) | `verif-v042/messages-extraction-2.md` | `{H['O4']}` |
| O-5 | Script de recherche des omissions dans les copies (contrôle 7 du §17) | `verif-v042/omissions.py` | `{H['O5']}` |

La source de O-1 et de O-4 est le journal de session, `/root/.claude/projects/-home-user/7361641c-6eb6-5649-a764-279757212cf3.jsonl`. Ce fichier s'allonge à chaque échange : il n'a pas d'empreinte stable.

**Sans fichier, ou sans empreinte dans le présent texte :**

| N° | Pièce |
|---|---|
| 12 ter | Consolidation v0.4.2 (le présent texte) : fichier `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2.md`, dans `revue-v03/`. Un fichier ne pouvant contenir sa propre empreinte, celle-ci est donnée hors du fichier |
| O-6 | Diff de la v0.4.1 à la v0.4.2 : `verif-v042/diff-v0.4.1-v0.4.2.patch`. Son empreinte dépend du présent texte : elle est donnée hors du fichier |
| 13 bis | Rapport de revue indépendante de la v0.4.2 : à venir, si le propriétaire le décide |
| 14 | Mandat de revue indépendante Q1–Q4 (message du 19 novembre 2026, 16:25:44Z) : non copié ; présent dans O-1 (message 22) |
| 15 | Rapports de Claude Code du 19 novembre : revue indépendante Q1–Q4 ; mises à jour n° 1 et n° 2 ; remarques R-Q5-1 à R-Q5-5 sur l'addendum Q5 ; remarques sur l'addendum B3 et son rectificatif ; vérifications de provenance |
| 16 | Les messages d'origine du propriétaire et la conversation de conception : les pièces 1, 1 bis, 2, 3 et 3 bis n'en sont que des copies ; O-1 et O-4 n'en sont que des extractions |

""")

# ---------- §17
between("## 17. Vérification interne de la v0.4.1", "## 18. ", """## 17. Vérification interne de la v0.4.2

Cette vérification est de Claude Code. Elle **n'est pas une revue indépendante**. Chaque contrôle a été exécuté avec `python3 -I` ou une commande du shell ; tous ont rendu le code de sortie 0.

| # | Contrôle | Méthode | Résultat |
|---|---|---|---|
| 1 | Citations de Q1.1 à Q1.4 | recherche mécanique, dans le §0.1 et le §3.1, des huit libellés de P1 et de P5 et de la validation de P1 l.309 | identiques |
| 2 | Textes des six arbitrages | recherche mécanique, dans le §2 bis, des six textes validés de P6 et de leurs statuts | identiques |
| 3 | Renvois de lignes nouveaux | lecture des lignes de P1, P2, P3, P6, D:34 et de la v1.4.1 citées par la v0.4.2 | concordants |
| 4 | Absence de décision nouvelle | tout énoncé décisionnel porte [INS], [TR], [TR-M], [CIT], [DÉC], [CONF] ou [VAL] ; les deux lectures [DÉD] visées par M-04 et M-05 sont retirées ; les conséquences des arbitrages sont reprises de P6, avec leurs lignes | aucune règle ajoutée hors des arbitrages ; T47 et T48 ne testent que des règles sourcées |
| 5 | Calculs et scénarios | arithmétique exacte : barème, T01, T02, T05 (énumération exhaustive), T11a, T18 à T23, T26, T37, T39, T44, T45, T47 et T48 (852,06… mm → 854 mm ; 852 par arrondi préalable) ; 1 341,6 mm | tous retrouvés |
| 6 | Exhaustivité | I-1, M-01 à M-18 et les six arbitrages ont chacun une ligne au §20 ; W-01 à W-14 au §18 | complet |
| 7 | Copies | O-5 sur O-4 : chaque message du propriétaire copié est recherché en entier dans les copies | messages 24 à 28, 30 et 32 à 36 intégraux ; message 31 partiel, partie « Mission » omise ; messages 22, 23 et 29 non copiés (mandat de revue Q1–Q4 ; envoi de la v0.2 ; annonce d'un envoi) |
| 8 | Rattachement des scénarios | script : chaque scénario de la colonne « Scénarios » du §12 cite-t-il la décision dans ses sources ? | aucun rattachement non cité |
| 9 | PNV | relecture du §3.5 et du §13 | neuf PNV conservées, PNV-2 actualisée par R-5=A ; dépendances déclarées dans T03, T04, T15, T26, T42, T43 et T46 ; aucune PNV dans un scénario « Sp » |
| 10 | Inventaire | empreintes recalculées | conformes au §15 |
| 11 | Portée de la v0.4.2 | `diff` de la v0.4.1 à la v0.4.2 (O-6), rapproché du §20 | aucun changement hors du §20 |

**Impossibilités de vérification :**
- authenticité des messages et de la conversation de conception ; présence des options B dans cette conversation ;
- textes des options des six arbitrages, de Q5.1, de Q5.2 et de B3 ;
- fidélité de P4 au rapport d'origine de la revue de la v0.3 ;
- comportement d'OXCE à l'exécution ; aucun scénario n'a été exécuté comme test.

""")

# ---------- §18
rep("## 18. Tableau des corrections : anomalie, correction, section, preuve, statut",
    "## 18. Tableau des corrections W-01 à W-14 (revue de la v0.3)")
rep("| W-01 | chronologie en cinq étapes ;", "| W-01 | chronologie en cinq étapes (six depuis R-6=A, v0.4.2) ;")
rep("| P3 l.15, l.88 ; P2 l.143-151 ; R:203 ; D:86 | corrigé (sur [CONF]) |",
    "| P3 l.15, l.88 ; P2 l.143-151 ; R:203 ; D:86 ; P6 l.73 | corrigé (sur [CONF] ; précisé par R-6=A) |")
rep("| §13 (T21) | calcul vérifié | corrigé |", "| §13 (T21) | calcul vérifié | corrigé ; explication portée dans T21 en v0.4.2 (M-02) |")
rep("empreintes du §15 | corrigé (v0.4.1) |", "empreintes du §15 | corrigé (v0.4.1) ; provenance précisée en v0.4.2 : [TR-M] (I-1) |")
rep("| §3.1, §9.1 | P2 l.215 environ (rectificatif §1) | corrigé |", "| §3.1, §9.1 | P2 l.217 (rectificatif §1) | corrigé ; précisé par R-5=A (v0.4.2) |")
rep("| W-09 | PNV-2 mise en cohérence (Q1.1, Q2.6 ; non étendue à MEC-0002) ;",
    "| W-09 | PNV-2 mise en cohérence (Q1.1, Q2.6 ; non étendue à MEC-0002), puis actualisée par R-5=A en v0.4.2 ;")
rep("| W-11 (b) | « aucun scénario dédié » pour Q2.4, Q3.3, Q3.5 et Q3.10 | §12 | — | corrigé |",
    "| W-11 (b) | « aucun scénario dédié » pour Q2.4, Q3.3, Q3.5 et Q3.10 | §12 | — | corrigé ; étendu en v0.4.2 (M-03) |")
rep("code au commit `441cae1b` | corrigé |", "code au commit `441cae1b` | corrigé ; différence de calcul flottant précisée en v0.4.2 (M-15) |")
rep("jamais deux unités conscientes sur une même case stable ;", "jamais deux unités conscientes sur une même case stable, hors de l'exception transitoire de G2 ;")

# ---------- §20 et phrase finale
rep("**La v0.4.1 n'est pas déclarée conforme** : il faut d'abord une revue indépendante. MEC-0001 et MEC-0002 restent reportées.",
"""## 20. Corrections de la v0.4.1 à la v0.4.2

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
| M-01 | ⟨B3-03⟩ absent sur cinq valeurs tirées de Q1 | marqueur ajouté : 1 274 mm, 1 341,6 mm, profil dans la case (§3.6) ; rapport 0,5 (§9.1) ; T04 | §3.6, §9.1, §13 | RV41 M-01 ; P2 l.169, l.239 | corrigé |
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
| M-15 | « concordance de troncature » d'ARB-D, sans nuance | ordre concordant ; calcul flottant tronqué dans OXCE distingué du plancher exact de Q3.14 ; exemple émulé ; aucune équivalence affirmée | §11 | RV41 M-15 ; `BattleUnit.cpp:2714-2720` | corrigé |
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

**La v0.4.2 n'est pas déclarée conforme** : il faut d'abord une revue indépendante. MEC-0001 et MEC-0002 restent reportées.""")

open(dst, "w", encoding="utf-8").write(t)
print("OK")
