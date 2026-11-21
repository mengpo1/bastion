import sys
src, dst = sys.argv[1], sys.argv[2]
CIT = "269 passages : 254 retrouvés dans les sources primaires, à la casse de l'initiale près, sans la mention (recommandé) des propositions et à l'espacement près autour de × (écarts déjà admis par la revue de la v0.4.1, §4.3) ; 15 ne figurent que dans le document ou ses versions antérieures (renvois internes des journaux de corrections, §19 à §21, et phrases finales) ; aucun introuvable"
t = open(src, encoding="utf-8").read()
def rep(old, new):
    global t
    n = t.count(old)
    if n != 1: sys.exit("ECHEC: %d occurrence(s) de: %r" % (n, old[:100]))
    t = t.replace(old, new)
def between(start, end_excl, new):
    global t
    assert t.count(start) == 1 and t.count(end_excl) == 1, (start[:60], end_excl[:60])
    i = t.index(start); j = t.index(end_excl); assert i < j
    t = t[:i] + new + t[j:]
SP = "/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad"
H = dict(P1="c9ee67cab4a96d4ab4902048426ae6fe34feb7dd23b9416768ee6ffba1c69063", P5="7e799d1c8ebd3a4486f28aaf34117709b76a92a11b68aa14c0296f44f0139777",
 P2="b69ba3b799608572363b1571ad1a9197a1c90af5e19c1b69f328de6a9a37b869", P3="b940866f15f286333313d5a3af4ead155eddd9e0bd1719fbcc08bc7e17d36290",
 P6="b222381f3e432bfbdf7828d04a71c8b1c657c6a5a9263caeeb02b8a9e38caf23", P7="c1b86a538feb15851cfc8d180c8c655e0c12efa0efa20a82ca3fc86bb4c5c119",
 P4="81657c1c2353c845868d6a2689e9cab2fc3c9750b3826b1bb7c9a05b51b1878c", V02="062c5e9c8176d08fedb4dbbb9d67daeebf1caf53b0e7d76d28250f19819ca2a1",
 V03="85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256", V04="02d8da8d9595e98e256186d59edb3ce75c49d7a0bf1be8ea889f8e2f63dd2a52",
 V041="bd4cf4fa5f94aa005c6e27bf81eb6cc6aba6e7365c8eccaddaf847320a699e3f", V042="a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808",
 RV41="efd36eed9d9d98c1e9609ea81c11e906ebdab6354d543efbff2e084998da9db6", RV42="1476a060e449fda7816ccc74c060d3465096cb1e56a0ae134b5f699145a6eb69",
 O1="73f1fcd26e95a9c11b09158ed9beaf150c47a1f67b069ce70ef3c6867c5a7c3c", O2="206ca788e261d6104f027229b34fad84d971f47e8ac20ef73870b83968a791db",
 O3="1d6d2a58249344508f2613817ad7e32ae647b56ac794e4f8f746d6ea33174f8c", O4="f50d039c212b1dcef132da490b7c494e79b2cf9c420d6e85da4da4d912f57fcc",
 O5="78453dd92293fbfb5e23fd23405c9d1f62a69828f363b6b03659933705c9b6fe", O6="4decc4c83282d9bce4b466e989c33f16fb7a50ea8bc214541381b4a1ca9a3686",
 O7="8bd912bca00b933c1119f190c5000a30728eeefe48c36ed96d30439ae09f624c")
S = [("S-1", "vérification de la v0.4 remise (texte extrait du journal)", "verif-v04/extract.py", "385f24c9af8d5f26347301b7f8a63ed2f53219289451500ce63033ac047a59e1"),
 ("S-2", "comparaison de P5 au message I (journal)", "verif-v04/last_user.py", "bad862ae1a031213affc23e22f20aebad3175f7f6d5410d432e9d94b5bc0b0d6"),
 ("S-3", "production de la v0.4.1 à partir de la v0.4", "verif-v04/make_v041.py", "145a738bf97c28008f8204da9840e1232eb3f0b66c072c2a98e5ea6a01c6a9f2"),
 ("S-4", "libellés de Q1.1 à Q1.4 (v0.4.1)", "verif-v04/check_labels.py", "a1a7e4c70e9a5f0fc04d4621e5c5a650dda69e2c8e1d91215d1b138e442ee5db"),
 ("S-5", "calculs des scénarios (depuis la v0.4.1)", "verif-v04/calculs.py", "0c8708c61c78f7738b300b8d096c58e66bb55bae8ff38d7a17b06e15e31278ed"),
 ("S-6", "production de la v0.4.2 à partir de la v0.4.1", "verif-v042/make_v042.py", "0a6c9f8d4ef5265794ebaf781dbef81115b39bef3720cb9d2ce1d6f882867a21"),
 ("S-7", "libellés de Q1.1 à Q1.4 et textes des six arbitrages", "verif-v042/check_textes.py", "b1f732a05d59b828256235ac8921a25d76f5d974006dbc6ef7fb137b38cb7e35"),
 ("S-8", "rattachements de la matrice ; PNV dans les scénarios « Sp »", "verif-v042/check_matrice.py", "4660e1e9a5b396097d3ccf6302b0548c7b6df689ff19ab739ea01039245aa8bf"),
 ("S-9", "calculs de T47, T48 et T21 (v0.4.2)", "verif-v042/calculs_v042.py", "7869bab86eeba16c4f185bb6b1a4c8ba2b706bd1f688cf96844ffabca4ffca02"),
 ("S-10", "application des corrections AN et OB (v0.4.3)", "verif-v043/check_v043.py", "4cbfe87f481479f135190f6893058c691ddd88d438159ff0fd489b22992146da"),
 ("S-11", "contrôle de toutes les citations (v0.4.3)", "verif-v043/citations_v043.py", "ceb93d77f4befbfe51cc732a1c28b24a0f865491900c09591cc355875ad2eb19"),
 ("S-12", "calculs de T47 (a) et (b) et des arrondis de T48 (v0.4.3)", "verif-v043/calculs_v043.py", "bc668debbd11788a16587a503a97b78fdaf0301042591f8c1d2fd0624a25d229")]

# ---------- En-tête
rep("# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.2\n", "# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.3\n")
rep("**Nature :** projet de consolidation documentaire complète, préparé sous le mandat de la v0.4.2 (copie P6). Il intègre les six arbitrages du propriétaire du 20 novembre 2026 et corrige l'anomalie I-1 et les anomalies M-01 à M-18 de la revue indépendante de la v0.4.1. Non revu, non inscrit.",
    "**Nature :** projet de consolidation documentaire complète, préparé sous le mandat de la v0.4.3 (copie P7). Il corrige les anomalies AN-01 à AN-08 et traite les observations OB-01 à OB-08 de la revue indépendante de la v0.4.2, sans modifier les décisions. Non revu, non inscrit.")
rep("**Succède à :** la v0.4.1 (SHA-256 `" + H["V041"] + "`), revue de façon indépendante : verdict « conforme sous réserves » (pièce 13).",
    "**Succède à :** la v0.4.2 (SHA-256 `" + H["V042"] + "`), revue de façon indépendante : verdict « conforme sous réserves » (pièce 13 bis, RV42).")
rep("→ v0.4.1 → v0.4.2. Corrections : W-01 à W-14 dans la v0.4 (§18) ; provenance de Q1.1 à Q1.4 dans la v0.4.1 (§19) ; six arbitrages, I-1 et M-01 à M-18 dans la v0.4.2 (§2 bis et §20). Les décisions validées auparavant sont conservées ; les six arbitrages les précisent ou tranchent des points ouverts (§2 bis).",
    "→ v0.4.1 (`" + H["V041"] + "`) → v0.4.2 → v0.4.3. Corrections : W-01 à W-14 dans la v0.4 (§18) ; provenance de Q1.1 à Q1.4 dans la v0.4.1 (§19) ; six arbitrages, I-1 et M-01 à M-18 dans la v0.4.2 (§2 bis et §20) ; AN-01 à AN-08 et OB-01 à OB-08 dans la v0.4.3 (§21). Les décisions validées sont conservées ; la v0.4.3 n'en modifie aucune.")
rep("- **RV41** : rapport de la revue indépendante de la v0.4.1 (pièce 13, fichier original du relecteur).\n",
    "- **RV41** : rapport de la revue indépendante de la v0.4.1 (pièce 13, fichier original du relecteur) ;\n- **P7** : mandat de la v0.4.3 (message K) ;\n- **RV42** : rapport de la revue indépendante de la v0.4.2 (pièce 13 bis, fichier original du relecteur).\n")
rep("`P1 l.NN` pour une ligne d'une copie.", "`P1 l.NN` pour une ligne d'une copie ; `JS-NN` pour un message du propriétaire, désigné par son numéro dans l'extraction du journal de session (tableau du §0).")

# ---------- §0
rep("Q1.5 à Q3.14 (message du 19 novembre 2026 à 20 h 36 UTC ; copie P1, message 1) | oui |",
    "Q1.5 à Q3.14 (JS-30, 2026-11-19T20:36:22Z ; copie P1, intertitre « Message 1 ») | oui |")
rep("sans les options écartées (copie P1, message 2). Q1.1 à Q1.4,", "sans les options écartées (copie P1, intertitre « Message 2 » : JS-31). Q1.1 à Q1.4,")
rep("\n### 0.1 Q1.1 à Q1.4 : un dossier composé de deux messages\n", """- **Portée de [TR] et [TR-M]** (OB-05) : ces codes qualifient la transmission des pièces dans la session de travail, non l'échange d'origine. JS-30 regroupe lui-même cinq validations (P1 l.67, 111, 165, 213 et 293), que le message A situe entre 14 h 26 et 14 h 47 UTC (P2 l.12-14) : c'est une déclaration, non une preuve.

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
""")
rep("(horodatages UTC du journal de session, relevés par les extractions O-1 et O-4) :", "(identifiants et horodatages du tableau du §0) :")
rep("| 1 | message du propriétaire commençant par « Pour Bastion MEC-0001,", "| 1 | **JS-31**, qui commence par « Pour Bastion MEC-0001,")
rep("| copie P1, message 2 (l.297-310) : tout le message,", "| copie P1, intertitre « Message 2 » (l.297-310) : tout le message,")
rep("| 2 | message I du propriétaire | 2026-11-20T13:41:45.327Z |", "| 2 | **JS-35** (message I) | 2026-11-20T13:41:45.327Z |")
rep("**Entre les deux :**\n", "**Avant les deux :** JS-29 (2026-11-19T20:35:55.895Z), mandat de vérification de la provenance de Q1.5 à Q3.14, écrivait : « Q1.1 à Q1.4 ne sont pas encore joints. Conserve explicitement leur provenance comme non vérifiée et identifie les règles de la consolidation qui en dépendent. » Les propositions de Q1.5 à Q3.14 ont suivi dans JS-30.\n\n**Entre les deux :**\n")
rep("- le mandat de la v0.4 (message H, 2026-11-20T12:53:14.601Z) écrivait", "- le mandat de la v0.4 (JS-34, message H, 2026-11-20T12:53:14.601Z) écrivait")
rep("- le message I indique :", "- JS-35 (message I) indique :")
rep("Le journal montre qu'elles manquaient déjà au message reçu le 19 novembre :", "Le journal montre qu'elles manquaient déjà à JS-31 :")
rep("| Décision (titre, P1) | Option A (message 1 ; P1) | Option B (message 2 ; P5) |", "| Décision (titre, P1) | Option A (JS-31 ; P1) | Option B (JS-35 ; P5) |")
rep("Validation, dans le message 1 (P1 l.308-309) :", "Validation, dans JS-31 (P1 l.308-309) :")
rep("**Autres copies** (contrôle 7 du §17) : les messages copiés dans P1 (message 1), P2, P3, P5 et P6 le sont intégralement. La seule omission relevée est la partie « Mission » du message 1 ci-dessus.",
    "**Autres copies** (contrôle 7 du §17) : JS-24 à JS-28 (P2), JS-30 (P1), JS-32 à JS-34 (P3), JS-35 (P5), JS-36 (P6) et JS-38 (P7) sont copiés intégralement. La seule omission relevée est la partie « Mission » de JS-31 (P1).")

# ---------- §2 bis, §3.5
rep("R-7=A et R-8=A, qui sont des clarifications ;", "R-7=A (« clarification validée ») et R-8=A (« articulation validée ») ;")
rep("la formulation « toutes les données géométriques » ne vaut donc pas règle ;", "la formulation de D:30, « Unités physiques de géométrie : mm entiers », ne vaut donc pas règle pour les données calculées ;")

# ---------- §5, §6, §9.2
rep("  - la clause inscrite d'ARB-D « La surcharge ne majore pas le prix des pas » (R:124) n'est pas modifiée.",
    "- **Rappel du registre**, qui ne vient pas de P6 (OB-01) : la clause d'ARB-D « La surcharge ne majore pas le prix des pas » [INS] (R:124) n'est pas modifiée par M-04=B.\n- **Point d'articulation** [OUV] (OB-06) : N14 retient le « principe d'OXCE, sans seuil d'immobilisation supplémentaire » et « aucune immobilisation liée à la charge » (R:104-105). Or OXCE ne réduit pas la récupération d'énergie selon la charge : `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`, commit `441cae1b`) ne tient compte que des blessures mortelles au torse. L'articulation de N14 et d'ARB-D avec M-04=B, décision postérieure du propriétaire, reste à traiter avec les modalités de M-04=B.")
rep("(R:166) est tranché sur ce point.", "(R:166) est donc tranché sur ce point [DÉD] : c'est une conséquence de M-05=A, que P6 n'énonce pas (OB-02).")
rep("ARB-D (Q3.14, Q4.6 ; M-04=B), ARB-E", "ARB-D (Q3.14, Q4.6 ; M-04=B), N14 (M-04=B : point d'articulation, §5), ARB-E")

# ---------- §10
rep("| R:166 : trajet devenu non payable | Q4.21, Q3.4 ; M-05=A (coût plus élevé mais encore payable) | — |",
    "| R:166 : trajet devenu non payable | Q4.21, Q3.4 ; M-05=A (coût plus élevé mais encore payable) | repli d'une diagonale sur le passage Y (§6) |")
rep("| G3, « Ouvert » (R:141) | Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.6, Q3.11, Q4.6 ; M-05=A | — |",
    "| G3, « Ouvert » (R:141) | Q3.7 à Q3.9, Q3.13 ; Q3.12 ; Q3.6, Q3.11, Q4.6 ; M-05=A | coûts de chaque connexion (Q3.10=B) |")

# ---------- §12, §13
rep("| T03, T04, T15, T26, T42, T43, T46 (conditionnels) | — |", "| T04, T15, T26 (conditionnels) | — |")
rep("| ARB-A, G1, Q3.4 | Pa (géométrie, PNV-6) |", "| ARB-A, G1, Q3.4 | Pa (géométrie laissée ouverte par G1 : R:134) |")
rep("| Q1.9 | Pa (bornes [OUV] ; au-delà : PNV-5) |", "| Q1.9 | Pa (bornes [OUV] ; au-delà : PNV-5) ⟨B3-03⟩ |")
rep("| Q1.1 à Q1.7, Q2.5, Q2.6 | Pa (1 274 mm : PNV-3 ; « dans sa case » : PNV-4) ⟨B3-03⟩ |",
    "| Q1.1 à Q1.3, Q1.5 à Q1.7, Q2.5, Q2.6 | Pa (1 274 mm : PNV-3 ; « le profil ne dépasse pas sa case » : PNV-4) ⟨B3-03⟩ |")
rep("| S7, G1 | Pa (sous-segments) |", "| S7, G1 | Pa (sous-segments, laissés ouverts par G1 : R:134) |")
rep("Pa (géométrie et praticabilité du trajet ; **pas** PNV-7)", "Pa (géométrie et trajectoire, laissées ouvertes par G1 : R:134 ; **pas** PNV-7)")
rep("| ARB-B, G1 | Pa (géométrie) |", "| ARB-B, G1 | Pa (géométrie laissée ouverte par G1 : R:134) |")
rep("(a) profil Q4.6 ; (b) valeurs fictives : 5 TU et 98 d'énergie avant ce pas | (a) le deuxième pas est exécuté et débité à son coût réel ; l'ordre continue, sans recalcul du trajet ; il reste 46 TU et 93 d'énergie après le troisième pas. (b) arrêt avant le deuxième pas, sans débit de ce pas ; il reste 5 TU et 98 d'énergie | M-05=A, Q3.4, Q4.21, G3, Q3.8 | Sp (coût réel simulé) |",
    "(a) profil Q4.6 ; (b) valeurs fictives : 12 TU et 100 d'énergie à la sélection, de sorte que le trajet connu (12 TU et 6 d'énergie) est sélectionnable (Z1, G3) | (a) le deuxième pas est exécuté et débité à son coût réel ; l'ordre continue, sans recalcul du trajet ; il reste 46 TU et 93 d'énergie après le troisième pas. (b) après le premier pas, il reste 8 TU et 98 d'énergie ; le deuxième pas, à 6 TU et 3 d'énergie, reste payable : il est exécuté, il reste 2 TU et 95 d'énergie ; le troisième pas (4 TU) n'est plus payable : arrêt avant ce pas, sans débit ; il reste 2 TU et 95 d'énergie | M-05=A, Q3.4, Q4.21, G3, Z1, Q3.8 | Sp (coût réel simulé) |")
rep("Un arrondi préalable au millimètre donnerait 852, qui ne contient pas le volume |",
    "Un arrondi préalable au millimètre le plus proche, ou inférieur, donnerait 852, qui ne contient pas le volume ; un arrondi supérieur donnerait 853, puis 854 |")

# ---------- §14
rep("La copie P1 ne reproduit pas la partie « Mission » du message du 19 novembre 2026 à 20 h 54 UTC (M-16) ; c'est la seule omission relevée dans les copies P1, P2, P3, P5 et P6 (§17, contrôle 7).",
    "La copie P1 ne reproduit pas la partie « Mission » de JS-31 (2026-11-19T20:54:21Z ; M-16) ; c'est la seule omission relevée dans les copies P1, P2, P3, P5, P6 et P7 (§17, contrôle 7).")
rep("- **RD-7 — Revue.** La v0.4.1 a été revue de façon indépendante (pièce 13 : « conforme sous réserves »). La v0.4.2 ne l'est pas encore. Aucun test n'a été exécuté.",
    "- **RD-7 — Revue.** La v0.4.1 et la v0.4.2 ont été revues de façon indépendante (pièces 13 et 13 bis : « conforme sous réserves » chacune). La v0.4.3 ne l'est pas encore : le contrôle indépendant de son diff relève d'une autorisation distincte (P7). Aucun test n'a été exécuté.")
rep("R-10 (limites de cette revue) et R-11 (statut) demeurent.",
    "R-10 (limites de cette revue) et R-11 (statut) demeurent.\n- **RD-9 — Journal de session.** C'est un fichier local qui s'allonge à chaque échange, sans empreinte stable. L'attribution de ses entrées « user » au propriétaire repose sur l'outil de session. Les rapports RV41 et RV42 ne sont authentifiés que par leur empreinte (RV42, §5).\n- **RD-10 — Pleine conformité.** Le message C, §E, subordonne un verdict « pleinement conforme » au « traitement documenté des anomalies, vérification des preuves de validation et nouvelle appréciation indépendante » (P2 l.114). La vérification des preuves suppose l'archivage (RD-1).")
rep("  - **RF-01 :** profils de connexions, y compris la reprise d'un transfert,", "  - **RF-01 :** profils de connexions, y compris les coûts de chaque connexion (Q3.10=B), la reprise d'un transfert,")
rep("- **Surcharge :** modalités d'un effet sur l'énergie (M-04=B) : existence selon la situation, déclenchement, calcul, valeurs ; autres pénalités ;",
    "- **Surcharge :** modalités d'un effet sur l'énergie (M-04=B) : existence selon la situation, déclenchement, calcul, valeurs ; articulation de ces modalités avec N14 et ARB-D (OB-06, §5) ; autres pénalités ;")

# ---------- §15
srows = "\n".join(f"| {a} | {b} | `{c}` | `{d}` |" for a, b, c, d in S)
between("## 15. Inventaire des pièces justificatives", "## 16. Journal des corrections", f"""## 15. Inventaire des pièces justificatives

J'ai recalculé chaque empreinte pour la v0.4.3, avec `sha256sum` sur le fichier ou `git show origin/main:<chemin> | sha256sum`. Une pièce **n'est pas archivée** du seul fait qu'elle figure ici. Les numéros des versions précédentes sont conservés, pour que les renvois existants restent valables. Les messages sont désignés par leur identifiant JS-NN (tableau du §0).

**Pièces avec fichier et empreinte vérifiée :**

| N° | Pièce | Fichier | SHA-256 | Archivée dans le dépôt |
|---|---|---|---|---|
| 1 | Q1.1 à Q3.14. Intertitre « Message 1 » = JS-30 (2026-11-19T20:36:22Z), intégral : propositions et validations de Q1.5 à Q3.14. Intertitre « Message 2 » = JS-31 (2026-11-19T20:54:21Z) : options A et validation de Q1.1 à Q1.4 ; **partie « Mission » non reproduite** (M-16). La mention « reproduit tel que reçu » de P1 l.3 ne vaut donc pas pour la fin de JS-31. **P1 n'est pas modifiée ; elle est complétée par la pièce 1 bis** | copie P1, `PIECES-Q1-Q3-TRANSMISES.md` | `{H['P1']}` | non |
| 1 bis | Options B de Q1.1 à Q1.4 : JS-35 (message I, 2026-11-20T13:41:45Z), intégral, et reconstitution par décision (compilation, l.39-48) | copie P5, `PIECE-Q1.1-Q1.4-OPTIONS-B.md` | `{H['P5']}` | non |
| 2 | Messages A à E = JS-24 à JS-28 (2026-11-19, de 19:56:49Z à 20:13:09Z), intégraux : repères horaires de Q1 à Q3 et valeurs de Q4.6 et Q4.7 ; Q5.1 et Q5.2 ; addendum Q5 ; addendum B3 ; rectificatif B3 | copie P2, `PIECES-Q4-Q5-B3-DECLARATIONS.md` | `{H['P2']}` | non |
| 3 | Messages F, G et H = JS-32 à JS-34 (2026-11-19T20:59:24Z, 2026-11-19T21:08:57Z, 2026-11-20T12:53:14Z), intégraux : consignes pour la v0.3 ; mandat de revue de la v0.3 ; mandat de la v0.4, avec les confirmations **W-01** et **W-12** | copie P3, `PIECES-MANDATS-ET-CONFIRMATIONS.md` | `{H['P3']}` | non |
| 3 bis | Message J = JS-36 (2026-11-20T14:44:23Z), intégral : mandat de la v0.4.2, avec les **six arbitrages** (§2 bis) | copie P6, `PIECE-MANDAT-v0.4.2-ARBITRAGES.md` | `{H['P6']}` | non |
| 3 ter | Message K = JS-38 (2026-11-20T16:12:04Z), intégral : mandat de la v0.4.3 | copie P7, `PIECE-MANDAT-v0.4.3-CORRECTIONS.md` | `{H['P7']}` | non |
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
| 12 ter | Consolidation v0.4.2 | `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2.md` | `{H['V042']}` | non |
| 13 | Rapport de la revue indépendante de la v0.4.1 (RV41), fichier original du relecteur : verdict « conforme sous réserves » ; I-1, M-01 à M-18, R-1 à R-11 | `RAPPORT-REVUE-INDEPENDANTE-v0.4.1.md` | `{H['RV41']}` | non |
| 13 bis | Rapport de la revue indépendante de la v0.4.2 (RV42), fichier original du relecteur : verdict « conforme sous réserves » ; AN-01 à AN-08, OB-01 à OB-08 | `RAPPORT-REVUE-INDEPENDANTE-v0.4.2.md` | `{H['RV42']}` | non |

**Emplacements :**
- pièces 1 à 4, 6, 12, 12 bis et 12 ter : `{SP}/revue-v03/` ;
- pièce 5 : `/root/.claude/uploads/7361641c-6eb6-5649-a764-279757212cf3/` ;
- pièce 13 : `{SP}/revue-v041-relecteur/` ; pièce 13 bis : `{SP}/revue-v042-relecteur/`.

**Outils de vérification** (M-17), dans `{SP}/` :

| N° | Outil | Fichier | SHA-256 |
|---|---|---|---|
| O-1 | Extraction mécanique des messages du propriétaire : 35 messages, jusqu'à JS-35 ; aucune réponse de Claude Code | `revue-v03/MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md` | `{H['O1']}` |
| O-2 | Script d'extraction (O-1, O-4 et O-7) | `verif-v04/extract_user_msgs.py` | `{H['O2']}` |
| O-3 | Diff de la v0.4 à la v0.4.1 | `verif-v04/diff-v0.4-v0.4.1.patch` | `{H['O3']}` |
| O-4 | Même extraction, 36 messages, jusqu'à JS-36. Ses 35 premiers messages sont identiques à O-1 | `verif-v042/messages-extraction-2.md` | `{H['O4']}` |
| O-5 | Script de recherche des omissions dans les copies (contrôle 7 du §17) | `verif-v042/omissions.py` | `{H['O5']}` |
| O-6 | Diff de la v0.4.1 à la v0.4.2 | `verif-v042/diff-v0.4.1-v0.4.2.patch` | `{H['O6']}` |
| O-7 | Même extraction, 38 messages, jusqu'à JS-38. Ses 36 premiers messages sont identiques à O-4 | `verif-v043/messages-extraction-3.md` | `{H['O7']}` |

La source de O-1, O-4 et O-7 est le journal de session, `/root/.claude/projects/-home-user/7361641c-6eb6-5649-a764-279757212cf3.jsonl`, sans empreinte stable (RD-9).

**Scripts de vérification et de production** (AN-08), dans `{SP}/`, lancés avec `python3 -I` :

| N° | Rôle | Fichier | SHA-256 |
|---|---|---|---|
{srows}

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

""")

# ---------- §17
between("## 17. Vérification interne de la v0.4.2", "## 18. ", f"""## 17. Vérification interne de la v0.4.3

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
| 13 | Toutes les citations | S-11 : chaque passage entre « », guillemets imbriqués compris, est recherché dans les sources primaires (pièces, registre et documents de `main`, v0.2, extraction O-7, rapports RV41 et RV42), puis dans le document et ses versions antérieures | {CIT} |

**Impossibilités de vérification :**
- authenticité des messages et de la conversation de conception ; présence des options B dans cette conversation ;
- textes des options des six arbitrages, de Q5.1, de Q5.2 et de B3 ;
- fidélité de P4 au rapport d'origine de la revue de la v0.3 ;
- comportement d'OXCE à l'exécution ; aucun scénario n'a été exécuté comme test ;
- contrôle indépendant du diff de la v0.4.3 : non fait, il relève d'une autorisation distincte (P7).

""")

# ---------- §18, §20
rep("| W-11 (a) | dépendances des PNV corrigées (T03, T04, T15, T26, T42, T43, T45, T46) | §12 | — | corrigé |",
    "| W-11 (a) | dépendances des PNV corrigées (T03, T04, T15, T26, T42, T43, T45, T46). T45 retiré en v0.4.2 (M-13) ; T03, T42, T43 et T46 rattachés en v0.4.3 à la géométrie laissée ouverte par G1, R:134 (AN-06) : restent T04, T15 et T26 | §12, §13 | — | corrigé ; actualisé en v0.4.3 (AN-05, AN-06) |")
rep("| M-01 | ⟨B3-03⟩ absent sur cinq valeurs tirées de Q1 | marqueur ajouté : 1 274 mm, 1 341,6 mm, profil dans la case (§3.6) ; rapport 0,5 (§9.1) ; T04 | §3.6, §9.1, §13 | RV41 M-01 ; P2 l.169, l.239 | corrigé |",
    "| M-01 | ⟨B3-03⟩ absent sur cinq valeurs tirées de Q1 | marqueur ajouté : 1 274 mm, 1 341,6 mm, profil dans la case (§3.6) ; rapport 0,5 (§9.1). *Rectifié en v0.4.3 : cette ligne annonçait aussi T04, qui n'avait pas été corrigé (AN-01) ; T04 l'est dans la v0.4.3* | §3.6, §9.1 ; §13 en v0.4.3 | RV41 M-01 ; P2 l.169, l.239 | corrigé en partie dans la v0.4.2 ; achevé dans la v0.4.3 |")
rep("| M-15 | « concordance de troncature » d'ARB-D, sans nuance |", "| M-15 | « Concordance d'ordre et de troncature » d'ARB-D, sans nuance (citation rectifiée en v0.4.3, AN-04) |")

# ---------- §21 et phrase finale
rep("**La v0.4.2 n'est pas déclarée conforme** : il faut d'abord une revue indépendante. MEC-0001 et MEC-0002 restent reportées.",
"""## 21. Corrections de la v0.4.2 à la v0.4.3

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

**La v0.4.3 n'est pas déclarée conforme** : il faut d'abord le contrôle indépendant de son diff, qui relève d'une autorisation distincte. MEC-0001 et MEC-0002 restent reportées.""")

open(dst, "w", encoding="utf-8").write(t)
print("OK")
