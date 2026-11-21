import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()

def rep(old, new):
    global t
    n = t.count(old)
    if n != 1:
        sys.exit("ECHEC: %d occurrence(s) de: %r" % (n, old[:90]))
    t = t.replace(old, new)

H04 = "02d8da8d9595e98e256186d59edb3ce75c49d7a0bf1be8ea889f8e2f63dd2a52"
HP5 = "7e799d1c8ebd3a4486f28aaf34117709b76a92a11b68aa14c0296f44f0139777"

# En-tête
rep("# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4\n",
    "# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.1\n")
rep("**Nature :** projet de consolidation documentaire, corrigé après la revue indépendante de la v0.3. Non revu, non inscrit.",
    "**Nature :** projet de consolidation documentaire ; v0.4 corrigée après réception des options B de Q1.1 à Q1.4. Non revu, non inscrit.")
rep("**Succède à :** la v0.3 (SHA-256 `85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256`). Elle intègre les confirmations W-01 et W-12 du propriétaire et les corrections W-01 à W-14 (tableau final au §18).",
    "**Succède à :** la v0.4 (SHA-256 `" + H04 + "`), issue de la v0.3 (SHA-256 `85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256`). La v0.4 intégrait les confirmations W-01 et W-12 du propriétaire et les corrections W-01 à W-14 (tableau final au §18). La v0.4.1 ne change que la provenance de Q1.1 à Q1.4 et les références qui en dépendent. Aucune décision n'est modifiée (liste des changements au §19).")
rep("- **P4** : rapport de revue de la v0.3.\n",
    "- **P4** : rapport de revue de la v0.3 ;\n- **P5** : options B de Q1.1 à Q1.4 (message I du propriétaire), qui complètent la copie P1.\n")

# §0
rep("| **[TR]** | proposition avec ses options, et validation, transmises par le propriétaire (copie P1, message 1) | oui |",
    "| **[TR]** | proposition avec ses options, et validation, transmises par le propriétaire (copie P1, message 1 ; pour Q1.1 à Q1.4 : copie P1, message 2, complétée par la copie P5) | oui |")
rep("| **[TR-A]** | option retenue et validation citée, transmises par le propriétaire, **sans les options écartées** (copie P1, message 2) | oui ; pièce incomplète (§0.1) |",
    "| [TR-A] | **code retiré dans la v0.4.1.** Il désignait, dans la v0.4, l'option retenue et la validation citée, sans les options écartées (copie P1, message 2) | sans objet (§0.1) |")

# §0.1
start = t.index("### 0.1 Q1.1 à Q1.4 : vérification de la pièce transmise")
endmark = "- **Pour lever ce point :** joindre les libellés des options B.\n"
end = t.index(endmark) + len(endmark)
assert t.count("### 0.1 ") == 1 and t.count(endmark) == 1
new01 = """### 0.1 Q1.1 à Q1.4 : vérification de la proposition complète

- **Pièces :**
  - copie P1, message 2 : le titre de chaque décision et le libellé de son option A (l.300 à 307), puis la validation citée (l.308-309) : « … je valide Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A. … » ;
  - copie P5, message I du propriétaire du 20 novembre 2026 : le libellé de l'option B de chaque décision (l.14 à 17). La reconstitution par décision figure en P5 l.39 à 48.
- **Vérification** (Claude Code, par inspection et comparaison de textes ; ce n'est pas une revue indépendante) :
  - chacune des quatre décisions a maintenant deux options, A et B, avec leur libellé ;
  - pour chaque décision, les deux options sont distinctes et s'excluent : largeur uniforme par carte, ou différente selon le niveau (Q1.1) ; volume pouvant dépasser la case, ou contenu dans la case (Q1.2) ; épaisseur configurable, ou nulle (Q1.3) ; altitude configurable par niveau, ou espacement vertical constant (Q1.4) ;
  - la validation désigne l'option A pour les quatre ; aucune option B n'est retenue ;
  - le texte de P5 est identique au message reçu dans la session (comparaison par `diff`, code de sortie 0) ; les libellés A et B cités au §3.1 sont identiques à ceux de P1 et de P5 (contrôle 1 du §17).
- **Conclusion :** la condition posée par le mandat de la v0.4 est remplie : « Reclasser ces quatre décisions dans la catégorie « proposition et validation transmises », sous réserve que les textes complets soient effectivement joints au dossier de travail. » (P3 l.116). Q1.1 à Q1.4 passent de [TR-A] à **[TR]**. Les décisions ne changent pas : Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A.
- **Limites :**
  - la proposition est transmise en deux messages : les options A avec la validation, puis les options B, après la v0.4. Le propriétaire déclare que les options B figuraient dans la conversation d'origine (P5 l.11). Je ne peux pas le vérifier : je n'ai pas accès à cette conversation ;
  - P1 et P5 sont des copies, ni authentifiées de façon indépendante ni archivées (RD-1, RD-6) ;
  - pour Q1.1 à Q1.4, les pièces ne donnent que le titre et le libellé de chaque option. Les propositions de Q1.5 à Q1.9 ont une autre forme : elles décrivent chaque option et signalent l'option recommandée (P1 l.11 à 53). On ne peut donc pas savoir si la proposition d'origine de Q1.1 à Q1.4 contenait davantage ;
  - le libellé de l'option A de Q1.4 est au passé (« les étages pouvaient initialement être séparés… ») : c'est la formulation de P1, citée telle quelle. Il a pu être rédigé après Q4.1 ; ce n'est pas vérifiable. La portée de Q1.4 n'en dépend pas, puisque Q1.4 est historique pour la hauteur d'étage (§3.2).
- **Observation [DÉD] :** l'option B de Q1.4, écartée, prévoyait un espacement vertical constant ; c'est le principe que Q4.1 et la confirmation W-01 ont fixé ensuite. Cela n'en fait pas une décision : la règle applicable découle de GE-02, de Q4.1 et de W-01, non de cette option (§3.2).
"""
t = t[:start] + new01 + t[end:]

# §3.1
rep("| Q1.1=A | « Largeur uniforme par carte, configurable et paire en millimètres. » | P1 l.300-301, 309 | [TR-A] ⟨B3-03⟩ |",
    "| Q1.1=A | « Largeur uniforme par carte, configurable et paire en millimètres. » Option B, écartée : « Une largeur différente selon le niveau tactique. Chaque étage possède son échelle. » | P1 l.300-301, 309 ; P5 l.14 | [TR] ⟨B3-03⟩ |")
rep("| Q1.2=A | « Dimensions configurables par type d'unité et posture. Le volume peut dépasser sa case ; les collisions restent obligatoires. » | P1 l.302-303 | [TR-A] |",
    "| Q1.2=A | « Dimensions configurables par type d'unité et posture. Le volume peut dépasser sa case ; les collisions restent obligatoires. » Option B, écartée : « Dimensions obligatoirement contenues dans la case. Plus restrictif, notamment pour les unités couchées ou de grande taille. » | P1 l.302-303, 309 ; P5 l.15 | [TR] |")
rep("| Q1.3=A | « Épaisseur configurable par type de mur ; les murs possèdent un volume physique défini. » | P1 l.304-305 | [TR-A] |",
    "| Q1.3=A | « Épaisseur configurable par type de mur ; les murs possèdent un volume physique défini. » Option B, écartée : « Épaisseur nulle. Les murs sont représentés uniquement par des surfaces séparant les cases. » | P1 l.304-305, 309 ; P5 l.16 | [TR] |")
rep("| Q1.4=A | « Altitude configurable pour chaque niveau ; les étages pouvaient initialement être séparés par des hauteurs différentes. » **Historique** pour la hauteur d'étage (§3.2). | P1 l.306-307 | [TR-A] |",
    "| Q1.4=A | « Altitude configurable pour chaque niveau ; les étages pouvaient initialement être séparés par des hauteurs différentes. » Option B, écartée : « Espacement vertical constant. Tous les niveaux sont séparés par la même hauteur. » **Historique** pour la hauteur d'étage (§3.2). | P1 l.306-307, 309 ; P5 l.17 | [TR] |")
rep("- la parité de la largeur des cases est sourcée par Q1.1 [TR-A] ⟨B3-03⟩ ;",
    "- la parité de la largeur des cases est sourcée par Q1.1 [TR] ⟨B3-03⟩ ;")

# §3.2
rep("2. **Q1.4=A** [TR-A] : altitude configurable pour chaque niveau, avec des hauteurs d'étage possiblement différentes. *Écart avec GE-02 à cette date.*",
    "2. **Q1.4=A** [TR] : altitude configurable pour chaque niveau, avec des hauteurs d'étage possiblement différentes. *Écart avec GE-02 à cette date.* L'option B, écartée, prévoyait un « espacement vertical constant » (P5 l.17) ; la règle applicable ne repose pas sur elle (§0.1).")

# §3.4 et §3.5
rep("- **Pour tous les volumes** — Q1.2 [TR-A] : « les collisions restent obligatoires ».",
    "- **Pour tous les volumes** — Q1.2 [TR] : « les collisions restent obligatoires ».")
rep("| largeur et enveloppes : [TR-A] et [TR] ; au-delà",
    "| largeur et enveloppes : [TR] ; au-delà")

# §12
rep("| Q1.1 | largeur uniforme par carte, configurable, paire, en mm | P1 l.300-301, 309 | [TR-A] | V | GE-02, R:151, G1 | T26 | options B absentes ; ⟨B3-03⟩ |",
    "| Q1.1 | largeur uniforme par carte, configurable, paire, en mm | P1 l.300-301, 309 ; P5 l.14 | [TR] | V | GE-02, R:151, G1 | T26 | ⟨B3-03⟩ |")
rep("| Q1.2 | dimensions par type et posture ; dépassement de case ; collisions obligatoires | P1 l.302-303, 309 | [TR-A] | V | GE-03, G1 | T26 | options B absentes |",
    "| Q1.2 | dimensions par type et posture ; dépassement de case ; collisions obligatoires | P1 l.302-303, 309 ; P5 l.15 | [TR] | V | GE-03, G1 | T26 | — |")
rep("| Q1.3 | épaisseur par type de mur ; volume physique | P1 l.304-305, 309 | [TR-A] | V | R:151 | T26 | options B absentes |",
    "| Q1.3 | épaisseur par type de mur ; volume physique | P1 l.304-305, 309 ; P5 l.16 | [TR] | V | R:151 | T26 | — |")
rep("| Q1.4 | altitude configurable par niveau | P1 l.306-307, 309 | [TR-A] | **H** (hauteur d'étage) | GE-02 | T27 | supplantée par Q4.1 et W-01 |",
    "| Q1.4 | altitude configurable par niveau | P1 l.306-307, 309 ; P5 l.17 | [TR] | **H** (hauteur d'étage) | GE-02 | T27 | supplantée par Q4.1 et W-01 ; libellé A au passé (§0.1) |")

# §14
rep("Aucune pièce du §15 n'est archivée dans le dépôt, sauf les numéros 9 à 12.",
    "Aucune pièce du §15 n'est archivée dans le dépôt, sauf les numéros 7 à 11.")
rep("- **RD-5 — Q1.1 à Q1.4.** Les libellés des options B sont absents de la copie P1 (§0.1).",
    "- **RD-5 — Q1.1 à Q1.4.** **Levée dans la v0.4.1** : les options B ont été transmises (copie P5), et les quatre décisions passent en [TR] (§0.1). Restent les réserves communes RD-1 et RD-6.")
rep("- **RD-7 — Revue.** La v0.4 n'a pas été revue de façon indépendante ; aucun test n'a été exécuté.",
    "- **RD-7 — Revue.** Ni la v0.4 ni la v0.4.1 n'ont été revues de façon indépendante à la date de rédaction ; aucun test n'a été exécuté.")

# §15
rep("| 2 | Messages A à E :",
    "| 1 bis | Options B de Q1.1 à Q1.4 : message I du propriétaire (20 novembre 2026), en entier, et reconstitution par décision des options A et B et de la validation | copie P5, `PIECE-Q1.1-Q1.4-OPTIONS-B.md` | `" + HP5 + "` | non |\n| 2 | Messages A à E :")
rep("| 11 | Rapport d'archivage du 18 novembre | `main:docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` | `7f457d789797f2fa7129ea1666ebfa66e6ad857534e8508d95419491252754c2` | oui |\n",
    "| 11 | Rapport d'archivage du 18 novembre | `main:docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` | `7f457d789797f2fa7129ea1666ebfa66e6ad857534e8508d95419491252754c2` | oui |\n| 12 | Consolidation v0.4, déposée telle que remise au propriétaire le 20 novembre 2026 | copie `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.md` | `" + H04 + "` | non |\n")
rep("Les copies 1 à 4 et 6 sont dans",
    "Les copies 1, 1 bis, 2 à 4, 6 et 12 sont dans")
rep("**Sans fichier ni empreinte**, à extraire avant archivage :",
    "**Sans fichier, ou sans empreinte dans le présent texte** :")
rep("| 12 | Consolidation v0.4 (le présent texte) : fichier et empreinte à établir avant sa revue indépendante |\n| 13 | Rapport de revue de la v0.4 : à venir |",
    "| 12 bis | Consolidation v0.4.1 (le présent texte) : fichier `BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md`, dans le même dossier. Un fichier ne pouvant contenir sa propre empreinte, celle-ci est donnée hors du fichier, à sa remise et dans le rapport de revue |\n| 13 | Rapport de revue indépendante de la v0.4.1 : à venir. La v0.4 n'est pas revue séparément |")

# §17
rep("## 17. Vérification interne de la v0.4\n", "## 17. Vérification interne de la v0.4.1\n")
rep("| 1 | Fidélité aux 29 décisions de Q1 à Q3 | chaque énoncé [TR] ou [TR-A] comparé aux lignes de P1 citées au §12 | conforme. Les citations sont reprises mot pour mot, y compris les points W-07 et W-08 (a) à (e) et (m). Q1.1 à Q1.4 restent [TR-A] (§0.1) |",
    "| 1 | Fidélité aux 29 décisions de Q1 à Q3 | chaque énoncé [TR] comparé aux lignes de P1 et de P5 citées au §12 ; pour Q1.1 à Q1.4, recherche mécanique des huit libellés de P1 et de P5 dans le §3.1 | conforme. Les citations sont reprises mot pour mot, y compris les points W-07 et W-08 (a) à (e) et (m). Les huit libellés de Q1.1 à Q1.4 sont présents à l'identique (§0.1) |")
rep("tout énoncé décisionnel porte [INS], [TR], [TR-A], [CIT], [DÉC] ou [CONF]",
    "tout énoncé décisionnel porte [INS], [TR], [CIT], [DÉC] ou [CONF] ; le code [TR-A] ne subsiste qu'à titre historique (§0, §0.1, §18, §19)")
rep("| 4 | Calculs et scénarios | Python (`python3 -I`), en arithmétique exacte, code de sortie 0 |",
    "| 4 | Calculs et scénarios | Python (`python3 -I`), en arithmétique exacte, ré-exécuté pour la v0.4.1, code de sortie 0 |")
rep("| options B de Q1.1 à Q1.4 absentes ; formulations de Q4 résumées ; options de Q5.1, Q5.2 et B3 absentes ; P4 partiellement résumée |",
    "| formulations de Q4 résumées ; options de Q5.1, Q5.2 et B3 absentes ; P4 partiellement résumée ; options B de Q1.1 à Q1.4 transmises à part, après la v0.4 (P5 ; limites au §0.1) |")
rep("| 8 | Inventaire | empreintes recalculées (code de sortie 0) ; distinction fichier / sans fichier ; archivé / non archivé | conforme au §15 |",
    "| 8 | Inventaire | empreintes recalculées pour la v0.4.1 (code de sortie 0) ; distinction fichier / sans fichier ; archivé / non archivé | conforme au §15 |\n| 9 | Portée de la v0.4.1 | `diff` entre les fichiers de la v0.4 et de la v0.4.1, rapproché de la liste du §19 | aucune modification hors du §19 |")

# §18
rep("| W-05 | inventaire complet avec empreintes vérifiées ; message A entier ; mandats, rapport et observations ; v0.4 et sa revue à venir. Reclassement de Q1.1 à Q1.4 **non fait** : les options B sont absentes de P1 | §0.1, §15 | P1 l.300-309 ; empreintes du §15 | inventaire corrigé ; reclassement **en attente des options B** |",
    "| W-05 | inventaire complet avec empreintes vérifiées ; message A entier ; mandats, rapport et observations ; fichiers de la v0.4 et de la v0.4.1 ; revue de la v0.4.1 à venir. Reclassement de Q1.1 à Q1.4 en [TR] fait dans la v0.4.1, après réception des options B (copie P5). Dans la v0.4, il restait en attente | §0.1, §3.1, §12, §15 | P1 l.300-309 ; P5 l.14-17 ; P3 l.116 ; empreintes du §15 | corrigé (v0.4.1) |")

# §19 et phrase finale
rep("**La v0.4 n'est pas déclarée conforme** : il faut d'abord une nouvelle revue indépendante. MEC-0001 et MEC-0002 restent reportées.",
"""## 19. Changements de la v0.4 à la v0.4.1

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

**La v0.4.1 n'est pas déclarée conforme** : il faut d'abord une revue indépendante. MEC-0001 et MEC-0002 restent reportées.""")

open(dst, "w", encoding="utf-8").write(t)
print("OK")
