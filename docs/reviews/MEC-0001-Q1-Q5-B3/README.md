# MEC-0001 — Dossier documentaire Q1 à Q5 et B3

**Nature :** archive documentaire du dossier de consolidation MEC-0001 (Q1 à Q5 et B3), de la v0.2 à la v0.4.3 et à son erratum. **Archiver n'est pas inscrire** : aucune décision n'est inscrite au registre, et rien n'autorise une implémentation.

**Statut :** MEC-0001 et MEC-0002 restent **reportées**. Le registre `docs/gameplay/GAMEPLAY-DECISIONS.md` n'est pas modifié.

**Version de référence :** la consolidation **v0.4.3** et la même version **avec l'erratum AR-01/AR-02**. Par décision du propriétaire (JS-41, pièce P8), l'erratum est conservé en l'état, accompagné du rapport de contrôle qui signale les réserves AE-01 et AE-02 ; aucun second erratum n'est demandé. Il se lit avec ce rapport (RV43e). Conformément à la décision D4 et aux décisions du propriétaire sur le plan d'archivage (JS-42, 20 novembre 2026 ; validation JS-43, 21 novembre 2026), ces deux versions sont archivées sous forme de **copies expurgées** du code d'OXCE (§2) ; leurs originaux restent hors du dépôt, inchangés.

**Organisation :** les sous-dossiers reprennent ceux de l'espace de travail d'origine (`revue-v03/`, `verif-v04/`…), et les fichiers y gardent leur nom d'origine, sauf les copies expurgées, suffixées `-EXPURGE-D4`. Les chemins relatifs cités par la v0.4.3 (§15) restent donc valables à partir de ce dossier, sauf pour les fichiers expurgés, dont le tableau du §2 donne la correspondance. Seule la v0.2 est placée dans `pieces-jointes/`. Les autres fichiers sont copiés octet pour octet.

## 1. Notice de provenance

| Provenance | Sens | Pièces |
|---|---|---|
| original `.md` | fichier joint par le propriétaire, copié octet pour octet | v0.2 |
| transcription | message du propriétaire extrait mécaniquement du journal de la session de travail et reproduit intégralement, sauf omission déclarée ; identité avec la conversation d'origine **non vérifiée** | P1, P2, P3, P5, P6, P7, P8 ; O-7 |
| copie partielle | copie dont certaines sections sont résumées, comme elle le déclare | P4 |
| rédigé par Claude Code | consolidations et scripts de l'auteur | v0.3 à v0.4.3, erratum ; groupe B |
| rapport original d'un relecteur | rapport d'un agent distinct de l'auteur, en lecture seule | RV41, RV42, RV43, RV43e ; groupe C |
| copie expurgée D4 | copie d'un des fichiers ci-dessus dont les extraits de code d'OXCE sont remplacés par un marqueur (§2) | 11 fichiers |

Les messages du propriétaire sont désignés par leur identifiant `JS-NN`, numéro du message dans l'extraction mécanique du journal (tableau du §0 de la v0.4.3 ; O-7 pour JS-1 à JS-38, P8 pour JS-39 à JS-41 ; JS-42 et JS-43 sont reproduits dans le rapport d'exécution `docs/reviews/MEC-0001-ARCHIVAGE-Q1-Q5-B3-2026-11-21.md`).

## 2. Copies expurgées (décision D4)

**Règle appliquée :**
- **retiré :** tout extrait de code d'OXCE (commit `441cae1b`) : instruction, expression, appel avec arguments, signature, indexation, commentaire du code ;
- **conservé :** les noms de fichiers et de chemins, les numéros de ligne, les noms de fonctions, de classes, de variables ou de clés pris isolément, ainsi que les descriptions de comportement.

Chaque extrait retiré est remplacé par le marqueur « [code OXCE retiré — D4] », sur la même ligne : le nombre et l'ordre des lignes sont inchangés, donc les renvois de ligne restent valables. Une vérification par script (`archivage-prep/d4/verifier_expurgation.py`, hors dépôt) a établi, ligne par ligne, que chaque copie s'obtient de son original en remplaçant uniquement des extraits de la liste retirée, et qu'aucun reste de code d'OXCE ne subsiste dans les fichiers de ce dossier.

| Original (hors dépôt) | SHA-256 de l'original | Copie archivée | SHA-256 de la copie | Extraits retirés | Statut |
|---|---|---|---|---|---|
| `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2.md` | `a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808` | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2-EXPURGE-D4.md` | `05ef9e8345df86cc8890cc6b582db2fde4325a2479ac44acf50afb9a415f7e90` | 2 | document : lignes et numérotation identiques à l'original |
| `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3.md` | `cd1c808b10dbcf39f96e557f9d6ef994b232bdcacc44e696122edd4dbee76602` | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3-EXPURGE-D4.md` | `375eae2205a15af826f0c1dab270024c0ba4ef55cb918069352298977333b9a1` | 2 | document : lignes et numérotation identiques à l'original |
| `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3-erratum-AR01-AR02.md` | `16bfac9d1b5995b5eb2f4ba418639f9e24ffe56435b5fbf279ab3ff80d196c51` | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3-erratum-AR01-AR02-EXPURGE-D4.md` | `cd3cd9af9a9484bf8077539f8576e7dff7949136f4fc71b642b50eeed15f5ce9` | 3 | document : lignes et numérotation identiques à l'original |
| `revue-v041-relecteur/RAPPORT-REVUE-INDEPENDANTE-v0.4.1.md` | `efd36eed9d9d98c1e9609ea81c11e906ebdab6354d543efbff2e084998da9db6` | `revue-v041-relecteur/RAPPORT-REVUE-INDEPENDANTE-v0.4.1-EXPURGE-D4.md` | `8a9cec4779eba06c28e49876480fa3358758c6428f4437a073237ea8446150d2` | 4 | document : lignes et numérotation identiques à l'original |
| `revue-v043-relecteur/RAPPORT-CONTROLE-INDEPENDANT-v0.4.3.md` | `427e0736235ad1eb5340cfb028eb19c24c315b030399e899fb41421a5ca902c2` | `revue-v043-relecteur/RAPPORT-CONTROLE-INDEPENDANT-v0.4.3-EXPURGE-D4.md` | `55f0526e39e5cc4733cfababef2fced0347b828235d2e053fc1a1087cc19270d` | 2 | document : lignes et numérotation identiques à l'original |
| `revue-v043e-relecteur/RAPPORT-CONTROLE-ERRATUM-v0.4.3.md` | `6c28e343c592211669cad05d1b86fa9959b114c55f60c20d966872f8ab64dd05` | `revue-v043e-relecteur/RAPPORT-CONTROLE-ERRATUM-v0.4.3-EXPURGE-D4.md` | `d1afac5645bbb132651bffe6df4716bbc047b356e05c4e867776ce10dac97ac2` | 16 | document : lignes et numérotation identiques à l'original |
| `verif-v042/make_v042.py` | `0a6c9f8d4ef5265794ebaf781dbef81115b39bef3720cb9d2ce1d6f882867a21` | `verif-v042/make_v042-EXPURGE-D4.py` | `1e6e8f5c0ba1d098b2d9182236e7b777dcbb80173bc9f89aab1feff64990ec27` | 2 | **fonctionnel sur la chaîne expurgée, vérifié** : appliqué à la v0.4.1, il reproduit octet pour octet la v0.4.2 expurgée ; il ne reproduit plus la v0.4.2 originale |
| `verif-v043e/make_erratum.py` | `11f1054a50dd252900e0c8376f1d2ddcbe39671338b8e6def486b8964ae2d783` | `verif-v043e/make_erratum-EXPURGE-D4.py` | `070da61bd8a46122f9c9fbb83b7eef3114644317c1754b392e2049878aebbb2a` | 1 | **fonctionnel sur la chaîne expurgée, vérifié** : appliqué à la v0.4.3 expurgée, il reproduit octet pour octet l'erratum expurgé ; il ne reproduit plus l'erratum original |
| `revue-v041-relecteur/float32_oxce.py` | `589e7c0e3701d4f8a853e4c57872d02ed2e39b3ab8960fba60841753f77b9aec` | `revue-v041-relecteur/float32_oxce-EXPURGE-D4.py` | `61f86c6f5be57c973a8d76ebd27ae7017b8e86996a313bd38ac8c23dcd9a6379` | 1 | **fonctionnel, vérifié** : seul un commentaire a changé ; sa sortie est identique à celle de l'original |
| `revue-v043e-relecteur/citations_oxce.py` | `34ea55e1e948ab60caab2efe8d811e6779dfbafe50b800d64d8d4ce1fd41ea19` | `revue-v043e-relecteur/citations_oxce-EXPURGE-D4.py` | `0f893c36bf51a7a4b8a874d0188a3ca83ff514f90c6eed7a300713d314e8418a` | 27 | **non fonctionnel, vérifié** : les lignes de code comparées ont été retirées ; relancé sur le clone d'OXCE, il se termine par le code 1 (17 contrôles en échec, 7 réussis). Conservé pour la liste des contrôles qu'il décrit |
| `revue-v043e-relecteur/sortie-citations-oxce.txt` | `c01928086bd47ad5b7a7f4f576b0ef67fb019cecc88bf05e761cc4ad664c00c2` | `revue-v043e-relecteur/sortie-citations-oxce-EXPURGE-D4.txt` | `b706c2c8b8e40399d3c4505d270a9413a5ddcaf9f89ba5181f276be51e3ad094` | 4 | sortie de la version originale, expurgée de la même façon |

**Conséquences :**
- les empreintes citées **à l'intérieur** des documents (par exemple au §15 de la v0.4.3, dans l'en-tête de l'erratum ou dans les rapports) désignent les **originaux**, non les copies expurgées ;
- les extraits retirés ne peuvent être relus qu'au commit `441cae1b` d'OXCE, à partir des renvois `fichier:ligne`, qui sont conservés ;
- les originaux restent dans l'espace de travail de la session, qui est **éphémère** : leur conservation hors du dépôt n'est pas assurée par cet archivage.

## 3. Réserves à conserver

Ces réserves sont **documentaires**. Aucune ne vaut décision de gameplay.

- **AE-01** : l'explication de la récupération énergétique d'OXCE dans l'erratum est incomplète. Elle doit être lue avec le rapport indépendant, qui précise le rôle des bonus du soldat (`revue-v043e-relecteur/RAPPORT-CONTROLE-ERRATUM-v0.4.3-EXPURGE-D4.md`).
- **AE-02** : la comparaison section par section du contrôle 11 n'est pas étayée par un script conservé. Elle doit être considérée comme une vérification documentaire par relecture.
- **Authentification des sources :** aucune pièce n'est authentifiée de façon indépendante. Les transcriptions sont fidèles au journal de la session de travail, ce que les relecteurs ont vérifié, mais la conversation de conception d'origine est inaccessible. Le journal lui-même n'est pas archivé : il s'allonge à chaque échange et n'a pas d'empreinte stable. Les rapports des relecteurs ne sont authentifiés que par leur empreinte.
- **Formulations de Q4 :** ce sont des résumés de l'orchestrateur (RD-2 de la v0.4.3). Seuls sont confirmés les valeurs de Q4.6 et Q4.7 et le contenu de Q4.1.
- **Neuf formulations PNV :** proposées, non validées (§3.5 de la v0.4.3). Elles ne valent pas règle.
- **Paramètres volontairement ouverts :** ceux du §14 de la v0.4.3, dont les modalités de M-04=B et de R-5=A. Ils ne sont pas tranchés.
- **Autres limites déclarées :** textes des options absents pour Q5.1, Q5.2, B3 et les six arbitrages (RD-3) ; Q1.1 à Q1.4 transmises en deux messages, l'existence des options B dans la conversation d'origine reposant sur la déclaration du propriétaire (RD-5) ; P1 sans la partie « Mission » de JS-31 ; P4 partielle.
- **Expurgation D4 :** voir le §2. Elle ne modifie aucune décision, aucune valeur ni aucun scénario.
- **Reproductibilité des scripts :** les scripts référencent les chemins de l'espace de travail d'origine. `make_v041.py` (S-3) ne reproduit pas exactement la v0.4.1 : une ligne du §17 y a été corrigée à la main après sa génération, sans que le script soit mis à jour. Les deux scripts de production expurgés ne reproduisent que les versions expurgées ; `citations_oxce-EXPURGE-D4.py` n'est pas fonctionnel.

## 4. Inventaire

Chemins relatifs à `docs/reviews/MEC-0001-Q1-Q5-B3/`. Empreintes SHA-256 des fichiers archivés.

### 4.1 Groupe A — consolidations, pièces, rapports

| N° | Fichier | Contenu | Provenance | Statut | Renvoi (v0.4.3, §15) | SHA-256 |
|---|---|---|---|---|---|---|
| A-01 | `pieces-jointes/4f625a0d-BASTION-MEC-0001-CONSOLIDATION-Q1-Q4-REVUE.md` | Consolidation Q1–Q4 v0.2 (validations de Q4, l.181-191) | original `.md` joint par le propriétaire (JS-23) | historique ; source des validations [CIT] de Q4 | pièce 5 | `062c5e9c8176d08fedb4dbbb9d67daeebf1caf53b0e7d76d28250f19819ca2a1` |
| A-02 | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.3.md` | Consolidation v0.3 | rédigée par Claude Code | historique ; revue : pièce 4 (P4) | pièce 6 | `85c18f375a6d84f6cd6ef48eba870a55a94308ac8b37373be2b06d1e5b21f256` |
| A-03 | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.md` | Consolidation v0.4 | rédigée par Claude Code ; identique au texte remis le 2026-11-20T13:05:12Z | historique | pièce 12 | `02d8da8d9595e98e256186d59edb3ce75c49d7a0bf1be8ea889f8e2f63dd2a52` |
| A-04 | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md` | Consolidation v0.4.1 | rédigée par Claude Code | historique ; revue : RV41 | pièce 12 bis | `bd4cf4fa5f94aa005c6e27bf81eb6cc6aba6e7365c8eccaddaf847320a699e3f` |
| A-05 | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.2-EXPURGE-D4.md` | Consolidation v0.4.2 | rédigée par Claude Code | copie **expurgée D4** de l'original (§2) ; historique ; revue : RV42 | pièce 12 ter | `05ef9e8345df86cc8890cc6b582db2fde4325a2479ac44acf50afb9a415f7e90` |
| A-06 | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3-EXPURGE-D4.md` | **Consolidation v0.4.3 initiale** | rédigée par Claude Code | copie **expurgée D4** de l'original (§2) ; **référence**, original inchangé hors du dépôt ; contrôle : RV43 | pièce 12 quater | `375eae2205a15af826f0c1dab270024c0ba4ef55cb918069352298977333b9a1` |
| A-07 | `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3-erratum-AR01-AR02-EXPURGE-D4.md` | **Consolidation v0.4.3 avec erratum AR-01/AR-02** | rédigée par Claude Code | copie **expurgée D4** de l'original (§2) ; **référence**, original inchangé hors du dépôt, conservée en l'état par décision du propriétaire (JS-41) ; contrôle : RV43e ; réserves AE-01 et AE-02 | — | `cd3cd9af9a9484bf8077539f8576e7dff7949136f4fc71b642b50eeed15f5ce9` |
| A-08 | `revue-v03/PIECES-Q1-Q3-TRANSMISES.md` | P1 : propositions et validations de Q1 à Q3 | transcription des messages JS-30 (intégral) et JS-31 (**sans sa partie « Mission »**) | pièce justificative | pièce 1 | `c9ee67cab4a96d4ab4902048426ae6fe34feb7dd23b9416768ee6ffba1c69063` |
| A-09 | `revue-v03/PIECE-Q1.1-Q1.4-OPTIONS-B.md` | P5 : options B de Q1.1 à Q1.4 | transcription de JS-35 (intégral), suivie d'une compilation (l.39-48) | pièce justificative | pièce 1 bis | `7e799d1c8ebd3a4486f28aaf34117709b76a92a11b68aa14c0296f44f0139777` |
| A-10 | `revue-v03/PIECES-Q4-Q5-B3-DECLARATIONS.md` | P2 : messages A à E (Q4.6, Q4.7, Q5.1, Q5.2, addenda Q5 et B3, rectificatif B3) | transcription de JS-24 à JS-28 (intégraux) | pièce justificative | pièce 2 | `b69ba3b799608572363b1571ad1a9197a1c90af5e19c1b69f328de6a9a37b869` |
| A-11 | `revue-v03/PIECES-MANDATS-ET-CONFIRMATIONS.md` | P3 : messages F, G et H (dont les confirmations W-01 et W-12) | transcription de JS-32 à JS-34 (intégraux) | pièce justificative ; mandats | pièce 3 | `b940866f15f286333313d5a3af4ead155eddd9e0bd1719fbcc08bc7e17d36290` |
| A-12 | `revue-v03/PIECE-MANDAT-v0.4.2-ARBITRAGES.md` | P6 : mandat de la v0.4.2 et **six arbitrages** (M-04, M-05, R-5 à R-8) | transcription de JS-36 (intégral) | pièce justificative ; mandat | pièce 3 bis | `b222381f3e432bfbdf7828d04a71c8b1c657c6a5a9263caeeb02b8a9e38caf23` |
| A-13 | `revue-v03/PIECE-MANDAT-v0.4.3-CORRECTIONS.md` | P7 : mandat de la v0.4.3 | transcription de JS-38 (intégral) | mandat | pièce 3 ter | `c1b86a538feb15851cfc8d180c8c655e0c12efa0efa20a82ca3fc86bb4c5c119` |
| A-14 | `revue-v03/PIECES-MANDATS-CONTROLE-ERRATUM-ARCHIVAGE.md` | P8 : mandat de contrôle de la v0.4.3 ; mandat d'erratum ; mandat de préparation de l'archivage (décision de conserver l'erratum en l'état) | transcription de JS-39, JS-40 et JS-41 (intégraux) | **nouvelle pièce** ; mandats et décision | — | `1cab7b97bc57bdadad8295d9c634d05df657c50dc3ce25254ba4679d96c1b7a3` |
| A-15 | `revue-v03/RAPPORT-REVUE-INDEPENDANTE-v0.3.md` | P4 : rapport de revue de la v0.3 (W-01 à W-14) | **copie partielle** : sections 3 et 6 résumées ; extrait d'observations de Claude Code | rapport de revue | pièce 4 | `81657c1c2353c845868d6a2689e9cab2fc3c9750b3826b1bb7c9a05b51b1878c` |
| A-16 | `verif-v043/messages-extraction-3.md` | O-7 : messages du propriétaire JS-1 à JS-38 | extraction mécanique du journal de session (script O-2) | référence des identifiants JS-NN | O-7 | `8bd912bca00b933c1119f190c5000a30728eeefe48c36ed96d30439ae09f624c` |
| A-17 | `revue-v041-relecteur/RAPPORT-REVUE-INDEPENDANTE-v0.4.1-EXPURGE-D4.md` | RV41 : revue de la v0.4.1 | rapport original d'un relecteur indépendant (agent distinct) | copie **expurgée D4** de l'original (§2) ; « conforme sous réserves » | pièce 13 | `8a9cec4779eba06c28e49876480fa3358758c6428f4437a073237ea8446150d2` |
| A-18 | `revue-v042-relecteur/RAPPORT-REVUE-INDEPENDANTE-v0.4.2.md` | RV42 : revue de la v0.4.2 | rapport original d'un relecteur indépendant (agent distinct) | « conforme sous réserves » | pièce 13 bis | `1476a060e449fda7816ccc74c060d3465096cb1e56a0ae134b5f699145a6eb69` |
| A-19 | `revue-v043-relecteur/RAPPORT-CONTROLE-INDEPENDANT-v0.4.3-EXPURGE-D4.md` | RV43 : contrôle de la v0.4.3 | rapport original d'un relecteur indépendant (agent distinct) | copie **expurgée D4** de l'original (§2) ; « conforme sous réserves » (AR-01, AR-02) | — | `55f0526e39e5cc4733cfababef2fced0347b828235d2e053fc1a1087cc19270d` |
| A-20 | `revue-v043e-relecteur/RAPPORT-CONTROLE-ERRATUM-v0.4.3-EXPURGE-D4.md` | RV43e : contrôle de l'erratum AR-01/AR-02 | rapport original d'un relecteur indépendant (agent distinct) | copie **expurgée D4** de l'original (§2) ; « conforme sous réserves » (**AE-01, AE-02**) | — | `d1afac5645bbb132651bffe6df4716bbc047b356e05c4e867776ce10dac97ac2` |

### 4.2 Groupe B — scripts de Claude Code et résultat conservé

Ces scripts sont des preuves, non des outils du projet ; la CI ne les exécute pas. Les autres résultats ont été affichés sans être conservés ; ils sont reproductibles en relançant les scripts dans l'espace de travail d'origine.

| N° | Fichier | Rôle | SHA-256 |
|---|---|---|---|
| B-01 | `verif-v04/extract.py` | S-1 | `385f24c9af8d5f26347301b7f8a63ed2f53219289451500ce63033ac047a59e1` |
| B-02 | `verif-v04/last_user.py` | S-2 | `bad862ae1a031213affc23e22f20aebad3175f7f6d5410d432e9d94b5bc0b0d6` |
| B-03 | `verif-v04/make_v041.py` | S-3 | `145a738bf97c28008f8204da9840e1232eb3f0b66c072c2a98e5ea6a01c6a9f2` |
| B-04 | `verif-v04/check_labels.py` | S-4 | `a1a7e4c70e9a5f0fc04d4621e5c5a650dda69e2c8e1d91215d1b138e442ee5db` |
| B-05 | `verif-v04/calculs.py` | S-5 | `0c8708c61c78f7738b300b8d096c58e66bb55bae8ff38d7a17b06e15e31278ed` |
| B-06 | `verif-v04/extract_user_msgs.py` | O-2 | `206ca788e261d6104f027229b34fad84d971f47e8ac20ef73870b83968a791db` |
| B-07 | `verif-v042/make_v042-EXPURGE-D4.py` | S-6 — copie expurgée D4 (§2) | `1e6e8f5c0ba1d098b2d9182236e7b777dcbb80173bc9f89aab1feff64990ec27` |
| B-08 | `verif-v042/check_textes.py` | S-7 | `b1f732a05d59b828256235ac8921a25d76f5d974006dbc6ef7fb137b38cb7e35` |
| B-09 | `verif-v042/check_matrice.py` | S-8 | `4660e1e9a5b396097d3ccf6302b0548c7b6df689ff19ab739ea01039245aa8bf` |
| B-10 | `verif-v042/calculs_v042.py` | S-9 | `7869bab86eeba16c4f185bb6b1a4c8ba2b706bd1f688cf96844ffabca4ffca02` |
| B-11 | `verif-v042/omissions.py` | O-5 | `78453dd92293fbfb5e23fd23405c9d1f62a69828f363b6b03659933705c9b6fe` |
| B-12 | `verif-v042/calculs-v04.txt` | sortie de S-5 | `abfc0e2b9a7462dc31649126157f5d3248e09b0d4a2f304a552a7566f7552c97` |
| B-13 | `verif-v043/check_v043.py` | S-10 | `4cbfe87f481479f135190f6893058c691ddd88d438159ff0fd489b22992146da` |
| B-14 | `verif-v043/citations_v043.py` | S-11 | `ceb93d77f4befbfe51cc732a1c28b24a0f865491900c09591cc355875ad2eb19` |
| B-15 | `verif-v043/calculs_v043.py` | S-12 | `bc668debbd11788a16587a503a97b78fdaf0301042591f8c1d2fd0624a25d229` |
| B-16 | `verif-v043/make_v043.py` | S-13 | `d877a7f2f1bd8ea1a692c6b9133592dcaaf71550aca56778c9a1d3d8622ad8c7` |
| B-17 | `verif-v043e/make_erratum-EXPURGE-D4.py` | production de l'erratum — copie expurgée D4 (§2) | `070da61bd8a46122f9c9fbb83b7eef3114644317c1754b392e2049878aebbb2a` |

### 4.3 Groupe C — scripts et sorties des relecteurs

Mêmes réserves que le groupe B.

| N° | Fichier | Rôle | SHA-256 |
|---|---|---|---|
| C-01 | `revue-v041-relecteur/calculs_relecteur.py` | script ou sortie d'un relecteur (v041) | `8db2a926d6c14cfa25bf606bb9a482ba4b78ad68dcd650b9c72fd618fd71af26` |
| C-02 | `revue-v041-relecteur/cas_v141.py` | script ou sortie d'un relecteur (v041) | `1c5e85440ef6c2f8370a617e08a4e3d34c955ccbe1284a3392eeda9d30e3904c` |
| C-03 | `revue-v041-relecteur/citations.py` | script ou sortie d'un relecteur (v041) | `7a93c8af7bb1a137b18a9c03200e793369ebc242aff842acee326702d1bfcc20` |
| C-04 | `revue-v041-relecteur/compare_copies.py` | script ou sortie d'un relecteur (v041) | `68e244e2d51ad015c7dd023ab5021fa7cda67e37a979231b6a1ffcc8bb71c6cf` |
| C-05 | `revue-v041-relecteur/float32_oxce-EXPURGE-D4.py` | script ou sortie d'un relecteur (v041) — copie expurgée D4 (§2) | `61f86c6f5be57c973a8d76ebd27ae7017b8e86996a313bd38ac8c23dcd9a6379` |
| C-06 | `revue-v041-relecteur/libelles_q1.py` | script ou sortie d'un relecteur (v041) | `5f74fa4d8631bd23af367eda1fd34ef1dafa640f64f96de3a7392e632e3a188a` |
| C-07 | `revue-v041-relecteur/matrice_scenarios.py` | script ou sortie d'un relecteur (v041) | `ea7e58967def424518b535baa5e91617e2d9c402425df34ab57ea31ebe93a2c5` |
| C-08 | `revue-v041-relecteur/v04_vs_journal.py` | script ou sortie d'un relecteur (v041) | `7ee18d08b3bb1cf9b58638c2cccd75518b542307362ff94ae7a6e082742afccd` |
| C-09 | `revue-v042-relecteur/blocs_diff.py` | script ou sortie d'un relecteur (v042) | `d105100d928fcf05922b61f2dca46aad8216cfda452495fad01dde61f2dafcda` |
| C-10 | `revue-v042-relecteur/calculs_independants.py` | script ou sortie d'un relecteur (v042) | `367d02963df3f45903e073dc4575673644d568627f82b01e68db588bc119c259` |
| C-11 | `revue-v042-relecteur/citations.py` | script ou sortie d'un relecteur (v042) | `6c6c7b3f63dc30ab4d05385c6e7fcf1729ab0ed354476cf360a2ca3d97cd6f7e` |
| C-12 | `revue-v042-relecteur/compare_extractions.py` | script ou sortie d'un relecteur (v042) | `5dd786c2ee41b45a7bb0df7611ff8f82be78c0e54e76d6b5c5641d751a2b6e5e` |
| C-13 | `revue-v042-relecteur/fidelite_copies.py` | script ou sortie d'un relecteur (v042) | `48dc6d8f6bd979410c290a6c6b07853092bff6549e7348721ab868956c07035e` |
| C-14 | `revue-v042-relecteur/matrice.py` | script ou sortie d'un relecteur (v042) | `561269361f7030c561a8d5e146b3bd93ee687c877c64cb8ef38e9923145217cf` |
| C-15 | `revue-v042-relecteur/options_b.py` | script ou sortie d'un relecteur (v042) | `417d877d751d767262fc3e933dd7aae630a658586df4d2c58e850a9724f22f33` |
| C-16 | `revue-v042-relecteur/remise_v04.py` | script ou sortie d'un relecteur (v042) | `de6343e74cec60f98d79fc16b498bdbdb5fd1d0f1155e580d4a4674e19b3d834` |
| C-17 | `revue-v042-relecteur/renvois_lignes.py` | script ou sortie d'un relecteur (v042) | `d234c0a5bf4a0f93216b9ebecd393ba77d8373109409668ba4b12e6af83e4da8` |
| C-18 | `revue-v042-relecteur/renvois_lignes2.py` | script ou sortie d'un relecteur (v042) | `744458f3c269f3ec4f85f8dbd19f49cb50a0b4582ca9b6b69ef417d491f50eb4` |
| C-19 | `revue-v042-relecteur/sections_arbitrages.py` | script ou sortie d'un relecteur (v042) | `199cea6a7c8bbb1670c931dc75ac598c364debda95d31c5cabfeb1130b3e303f` |
| C-20 | `revue-v042-relecteur/statuts.txt` | script ou sortie d'un relecteur (v042) | `0600aabdba1444b3d0742871c2b2323d8f52a22f5ec01bcc45811aada3cc3e05` |
| C-21 | `revue-v043-relecteur/arbitrages.py` | script ou sortie d'un relecteur (v043) | `c7da5e1ffc8c7e7e205c284be57816e4954483579ea263ccca17f2c8cc5f2049` |
| C-22 | `revue-v043-relecteur/calculs_independants.py` | script ou sortie d'un relecteur (v043) | `109fd28ba71019d40fccb45f23643cdbb51ec9a0812486ae84f84b1ec042ef09` |
| C-23 | `revue-v043-relecteur/citations.py` | script ou sortie d'un relecteur (v043) | `fd58c2d54e3ed707c54c0dcde0fbec266eedc867f657e9821ad8b81e68324cc5` |
| C-24 | `revue-v043-relecteur/compare_extractions.py` | script ou sortie d'un relecteur (v043) | `e41e4446c07a6ce3d2bdd8bfeef806cbdce5f934502aae2c5954fc364c0ebc2c` |
| C-25 | `revue-v043-relecteur/correspondance_js.py` | script ou sortie d'un relecteur (v043) | `541e6358398ce96b9873c949cdfe553a18bcd2bc9ce77851100e8cf24464f5f1` |
| C-26 | `revue-v043-relecteur/fidelite_copies.py` | script ou sortie d'un relecteur (v043) | `a5e51f23b3d0a36240832145761a8f5e3d71e0243c526082760ffd7a11168933` |
| C-27 | `revue-v043-relecteur/matrice.py` | script ou sortie d'un relecteur (v043) | `a6b2f55ff39dadab0ddd1376472da4d9cd7d70ae0f7c42ff5f86c958af8ee3f6` |
| C-28 | `revue-v043-relecteur/points_ouverts.py` | script ou sortie d'un relecteur (v043) | `9b64a4fd3e032681faf7c03c4a07707b998cf3d23b92fd2d633cfbe4d69dda8e` |
| C-29 | `revue-v043-relecteur/sections_diff.py` | script ou sortie d'un relecteur (v043) | `dc2f62dd6935613e4763e8c015a30ffd55e9ead9205b0461830cf497a9548285` |
| C-30 | `revue-v043-relecteur/sortie-citations.txt` | script ou sortie d'un relecteur (v043) | `f0a2e1fb5207d085ff8fe6063492185e0834c23aa867260e4940a0ddf76246cb` |
| C-31 | `revue-v043-relecteur/variante_t47.py` | script ou sortie d'un relecteur (v043) | `572ec6dbf9b591f6486e4b98dc85bdfb7226f63fe55304deaa09b3e336a54e88` |
| C-32 | `revue-v043e-relecteur/citations_oxce-EXPURGE-D4.py` | script ou sortie d'un relecteur (v043e) — copie expurgée D4 (§2) | `0f893c36bf51a7a4b8a874d0188a3ca83ff514f90c6eed7a300713d314e8418a` |
| C-33 | `revue-v043e-relecteur/perimetre.py` | script ou sortie d'un relecteur (v043e) | `a7cc0241f331ebf520f535a6f926dc2da95993a509e130fc03e6d605e8bd2032` |
| C-34 | `revue-v043e-relecteur/sortie-citations-oxce-EXPURGE-D4.txt` | script ou sortie d'un relecteur (v043e) — copie expurgée D4 (§2) | `b706c2c8b8e40399d3c4505d270a9413a5ddcaf9f89ba5181f276be51e3ad094` |
| C-35 | `revue-v043e-relecteur/sortie-perimetre.txt` | script ou sortie d'un relecteur (v043e) | `3e396732510a45f364731ca7dd2e3aa0a2f9246471d0293bca83ec2643c46a9c` |
| C-36 | `revue-v043e-relecteur/sorties-scripts-auteur.txt` | script ou sortie d'un relecteur (v043e) | `c58e8a0862e93baf6e72c9c7e3b97b8e0680abe92c54dc196b21bab8b15ca694` |

## 5. Pièces non archivées

| Pièce | SHA-256 | Raison |
|---|---|---|
| les 11 originaux des copies expurgées | voir le §2 | contiennent des extraits de code d'OXCE : exclus par D4 ; conservés hors du dépôt, dans l'espace de travail éphémère |
| O-1, extraction de JS-1 à JS-35 (`revue-v03/MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md`) | `73f1fcd26e95a9c11b09158ed9beaf150c47a1f67b069ce70ef3c6867c5a7c3c` | préfixe exact de O-7, vérifié par script |
| O-4, extraction de JS-1 à JS-36 (`verif-v042/messages-extraction-2.md`) | `f50d039c212b1dcef132da490b7c494e79b2cf9c420d6e85da4da4d912f57fcc` | préfixe exact de O-7, vérifié par script |
| extraction de JS-1 à JS-40 (`verif-v043e/messages-extraction-4.md`), fournie au relecteur de l'erratum | `9ef7d01f16c351b929c7ee411285cf78539703bc352d7a774c7a830e3740c019` | contenu inclus dans O-7 et P8, vérifié par script |
| O-3, diff de la v0.4 à la v0.4.1 | `1d6d2a58249344508f2613817ad7e32ae647b56ac794e4f8f746d6ea33174f8c` | décision du propriétaire : les diffs reproductibles ne sont pas archivés |
| O-6, diff de la v0.4.1 à la v0.4.2 | `4decc4c83282d9bce4b466e989c33f16fb7a50ea8bc214541381b4a1ca9a3686` | idem ; un diff entre versions expurgées différerait de celui-ci par les marqueurs |
| O-8, diff de la v0.4.2 à la v0.4.3 | `d15f305467744f5e874daea772cb544faf16e813aad3b71bdbc29e0b78485787` | idem |
| diff de l'erratum | `645915da758001dc701a0ab42e23e32b028f09f51b8a1a3e080ff9a7665c4d3d` | idem |
| copies de travail des relecteurs (registre, v1.4.1, LOT-2A, rapport ARB-G, OXCE-BASELINE, mandat d'inscription, rapport d'archivage) | — | doublons de fichiers déjà présents sur `main` |
| copies du code source d'OXCE faites par un relecteur (`BattleUnit.cpp.txt`, `RuleStatBonus.cpp.txt`) | — | exclues : décision D4 |
| réextractions du journal, reproductions de la v0.4.3 et de l'erratum, diffs et fichiers temporaires des relecteurs, sorties en double | — | redondants |
| journal de session | — | fichier local, sans empreinte stable ; il contient aussi les réponses et raisonnements de l'auteur |

## 6. Pièces citées mais indisponibles

- la conversation de conception d'origine et les messages d'origine du propriétaire, dont les transcriptions ne sont que des copies ;
- les textes complets des propositions de Q4, et ceux des options de Q5.1, de Q5.2, de B3 et des six arbitrages ;
- les sections 3 et 6 du rapport d'origine de la revue de la v0.3 (P4 les résume) ;
- les rapports de Claude Code du 19 novembre 2026 (pièce 15 de la v0.4.3) : ils n'existent que dans le journal de session.

## 7. Pièces déjà présentes dans le dépôt

Les pièces 7 à 11 de la v0.4.3 sont déjà archivées sur `main` et ne sont pas copiées : le registre, le rapport d'inscription ARB/G du 17 novembre, la consolidation v1.4.1, le mandat d'inscription v1.0 et le rapport d'archivage du 18 novembre.

## 8. Vérifier l'intégrité

Depuis la racine du dépôt, pour un fichier : `sha256sum docs/reviews/MEC-0001-Q1-Q5-B3/<chemin>`, à comparer à l'empreinte du §4.
