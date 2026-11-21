# Bastion — Inscription documentaire MEC-0001 / MEC-0002 : Q1 à Q5, B3 et six arbitrages

**Date d'exécution :** 21 novembre 2026
**Nature :** inscription documentaire au registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, par application exclusive du diff v4 préparé et relu hors du dépôt. **MEC-0001 et MEC-0002 restent « reportée » ; aucune implémentation n'est autorisée.**
**Mandat :** « BASTION — Mandat d'inscription documentaire MEC-0001 / MEC-0002 », reçu le 2026-11-21T16:52:29.515Z (horodatage du journal de session), statut « préparé pour autorisation d'exécution ». Il porte les décisions D-01 et D-02 du propriétaire, du 21 novembre 2026. Texte intégral en annexe A.
**Autorisation :** réponse du propriétaire, le 2026-11-21T16:55:19.533Z, « Autoriser, diff v4 tel quel (Recommandé) », à la question qui demandait l'autorisation d'exécuter le mandat (annexe B).
**Base :** `main` au commit `7c5e325f0771abcb9f5c5636bd695cc0959cb3d3`, après `git fetch origin main`.
**Branche :** `claude/inscription-mec-0001-mec-0002-q1-q5-b3`, créée à partir de `origin/main`.
**Opération :** un commit documentaire unique, un push de cette seule branche, puis une PR en brouillon vers `main`. **Aucune fusion n'est autorisée.**

## 1. Résumé

Le registre reçoit :
- dans `MEC-0001`, un nouveau bloc « Sous-décisions de conception acceptées les 19 et 20 novembre 2026 (Q1 à Q5, B3, M-04, M-05, R-5 à R-8) », avec la provenance et le niveau de preuve de chaque décision ;
- des annotations de S2, S8, S10, S11, N4, N14, ARB-C, ARB-D, ARB-E, G1, G2, G3, G4 et du bloc du 17 novembre 2026 ;
- l'actualisation des champs de fiche et de la liste « Encore ouvert » ;
- dans `MEC-0002`, des annotations de GE-02 (clause « proportions » modifiée par B3), GE-03 (précisée), GE-07, CH-14, ES-09, ES-10 et EN-06, avec l'actualisation de l'en-tête, des champs, des conventions, de DS1.1 et de « Encore ouvert ».

Le texte historique est conservé. Les 21 lignes annotées ne sont complétées qu'en fin de ligne. Dans 9 lignes d'en-têtes, de champs ou de listes (R:51, R:58, R:59, R:60, R:62, R:175, R:182, R:184, R:325), du texte est inséré dans la ligne, et la conjonction « et » d'une énumération prolongée devient une virgule (R:59, R:62). Seules les listes « Encore ouvert » sont réécrites, pour distinguer ce qui est décidé de ce qui reste ouvert. Aucun paramètre volontairement ouvert n'est tranché. Les neuf formulations PNV, les scénarios et les comparaisons avec OXCE ne sont pas inscrits. Aucun code, aucune donnée ni aucun asset d'OXCE n'est ajouté (D4).

Conformément aux décisions du propriétaire :
- **D-01 :** la réserve de traçabilité de Q1 à Q3 ne bloque plus l'inscription. Le registre ne déclare pas la provenance vérifiée : il garde la mention « provenance non vérifiée » des valeurs de Q1 et expose les limites de preuve ;
- **D-02 :** les décisions Q4 sont inscrites à partir des résumés, au niveau [CIT], présentées comme des résumés et non comme des citations littérales ; Q4.6 et Q4.7 restent des valeurs initiales de test.

## 2. Fichiers

| Fichier | Opération | Empreinte SHA-256 après |
|---|---|---|
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | modifié par le diff v4 : 350 → 442 lignes ; 137 insertions, 45 suppressions de lignes au sens de Git | `9054c825cecfd61c82689c984a4a7f1057f77c756d8227cab2bf2f707236c68e` |
| `docs/reviews/MEC-0001-MEC-0002-INSCRIPTION-Q1-Q5-B3-2026-11-21.md` | ajouté : le présent rapport | — |

Aucun autre fichier n'est touché : mandats, harnais, code et tests sont inchangés.

## 3. Préparation et relecture du diff (avant ce mandat)

Le diff a été préparé hors du dépôt, par remplacements à ancre unique sur une copie du registre de `main`, à partir du dossier archivé `docs/reviews/MEC-0001-Q1-Q5-B3/` (consolidation v0.4.3 avec erratum, pièces P1, P2, P3, P5, P6 et v0.2).

Un agent distinct de l'auteur l'a relu, en lecture seule :
- **relecture de la v1** : « conforme sous réserves », 14 constats (RI-01 à RI-14), aucun bloquant ;
- **première contre-vérification, sur la v2** : « corrections conformes sous réserves », 4 constats nouveaux (RI-15 à RI-18) ;
- **deuxième contre-vérification, sur la v3** : « corrections conformes », 2 observations (RI-19, RI-20) ;
- **vérification finale, sur la v4** : « conforme », sans constat nouveau.

Chaque constat a été vérifié contre les pièces avant d'être corrigé ; les corrections ne portent que sur la fidélité aux sources et sur les points ouverts. La matrice de traçabilité et la liste des éléments non inscrits sont reproduites en annexes C et D.

Ces fichiers de préparation sont restés dans l'espace de travail éphémère de la session ; ils ne sont **pas archivés** dans le dépôt :

| Fichier | SHA-256 |
|---|---|
| diff v4 (`PROPOSITION-GAMEPLAY-DECISIONS.diff`) | `8f78ef25201fed272a7ec95c2c1dc83431a3a943511627aa0f1a1b90480a160f` |
| registre proposé v4 (`registre-propose.md`) | `9054c825cecfd61c82689c984a4a7f1057f77c756d8227cab2bf2f707236c68e` |
| rapport de relecture (v1) | `f1002dffcfad079f77ea774482ac2ba27f0aa46b027c38e3594c49b5592e9ee7` |
| contre-vérification de la v2 | `d9e69de55f5258e96d3cb2a6c4dd7aea91c24a61273d956fa5aa68a14928fa9f` |
| contre-vérification de la v3 | `0a7c7e5fed441316722a134c678fc9da7886469cf84bdab0c80f11d58a41c64c` |
| vérification finale de la v4 | `2d24f59261b72732a2626467be2ef79464b97f7b973d9929ec7f38de317d8d03` |

## 4. Exécution et contrôles

Toutes les commandes ont été exécutées dans `/home/user/bastion`, sauf mention contraire.

| Étape | Commande | Résultat |
|---|---|---|
| 1. Base | `git fetch origin main` ; `git rev-parse origin/main` | code 0 ; `7c5e325f0771abcb9f5c5636bd695cc0959cb3d3`, inchangé depuis la préparation |
| 2. Registre de base | `git show origin/main:docs/gameplay/GAMEPLAY-DECISIONS.md \| sha256sum` | `9117d20c45aa95abbc218ce5cdcc2a095106eb86c64a342be76d8521ef14d39e`, base exacte du diff v4 |
| 3. Empreintes | `sha256sum` du diff et du registre proposé | `8f78ef25…` et `9054c825…`, conformes au mandat |
| 4. Branche | `git branch --list …` ; `git ls-remote --heads origin …` ; puis `git switch -c claude/inscription-mec-0001-mec-0002-q1-q5-b3 origin/main` | absente en local et sur le dépôt distant ; création, code 0 ; `HEAD` = `7c5e325f…` |
| 5. Application | `git apply --check <diff v4>` ; `git apply <diff v4>` | codes 0 et 0 |
| 6. Identité | `sha256sum docs/gameplay/GAMEPLAY-DECISIONS.md` ; `cmp` avec le registre proposé | `9054c825…` ; `cmp` code 0 : identique octet pour octet |
| 7. Périmètre | `git status --porcelain` ; `git diff --name-only origin/main` ; `git diff origin/main --check` | un seul fichier modifié ; `--check` code 0 |
| 7. Statuts | `grep -cF` sur `main` et sur la branche | lignes « Décision du propriétaire » des deux fiches : toujours « reportée — … » ; `Classe` `MODIFICATION-PROPOSEE` : 2 et 2 ; « État d'implémentation \| non commencé » : 3 et 3, gabarit de fiche compris ; « Aucun changement de gameplay » : 2 et 2 ; « sans décision globale « acceptée » » : 1 et 1 |
| 7. PNV | `git diff -U0 origin/main` filtré sur « PNV » | cinq mentions ajoutées, toutes d'exclusion ou de non-validation (« formulations proposées et non validées », « formulation non validée PNV-7 ») |
| 7. Identifiants | puces ajoutées ou modifiées | décisions Q1 à Q5, B3, M-04, M-05, R-5, R-8 (R-6 et R-7 dans « Hauteur d'étage » et Q1.4), et règles existantes annotées ; aucun autre identifiant nouveau |
| Harnais | `bash scripts/harness/test-hooks.sh` | « 75 tests, 0 échec(s) », code 0 |
| .NET | `command -v dotnet` | absent du conteneur : `dotnet build`, `dotnet test` et `dotnet format` n'ont pas été exécutés localement ; ils le sont par la CI (§7) |
| Traçabilité de la simulation | lecture de `.github/workflows/ci.yml` et de `scripts/harness/check-simulation-trace.sh` | aucun fichier de `src/Bastion.Simulation/` modifié : aucune déclaration requise |

## 5. Contrôle indépendant du changement appliqué

**Contrôleur :** agent distinct de l'auteur, en lecture seule ; l'auteur l'a lancé séparément de l'agent qui avait relu la préparation. Écriture limitée à son dossier de travail. **Livrable :** `CONTROLE-INSCRIPTION.md`, SHA-256 `a270aa7460e90fb62c09c9b11916fd0b49e7f478d1f38a2ec707e8749fa4d233`, resté dans l'espace de travail éphémère et non archivé. **Verdict :** « conforme sous réserves », sans constat bloquant. Le contrôleur ne valide ni le commit ni la fusion.

Vérifié par commandes exécutées :
1. **Registre identique au v4.** Le diff v4, appliqué à une copie du registre de base (`git apply --check`, puis `git apply`, codes 0), donne un fichier identique octet pour octet au registre de l'arbre de travail et au registre proposé (`cmp`, codes 0 ; `9054c825…`). Le diff du clone ne diffère du diff v4 que par la ligne `index` et le contexte des en-têtes `@@`.
2. **Périmètre.** Seuls diffèrent de la base le registre, modifié, et ce rapport, nouveau. Rien n'est modifié dans les mandats, le harnais, `docs/decisions/`, `docs/references/`, le code ou les tests. `git diff --check` : code 0.
3. **Aucun ajout de gameplay.** Décomptes identiques des statuts « reportée », des classes et des états d'implémentation ; aucune décision hors de Q1 à Q5, B3, M-04, M-05 et R-5 à R-8 ; les cinq mentions des PNV sont des exclusions ; aucun texte historique perdu.
4. **D-01 et D-02.** Le registre ne déclare nulle part la provenance vérifiée ou authentifiée ; les 21 décisions Q4 portent l'étiquette [CIT] et sont présentées comme des résumés ; Q4.6 et Q4.7 restent des valeurs de test.
5. **Rapport.** Empreintes, comptages, commandes, fichiers et statuts exacts ; annexes A et B identiques au journal de session, caractère pour caractère ; aucun identifiant de modèle d'IA ni code d'OXCE ; `test-hooks.sh` relancé : « 75 tests, 0 échec(s) », code 0.

Inspecté seulement par le contrôleur : le `git fetch`, établi par ses traces (`FETCH_HEAD`, journal des références) ; la portée de M-05 sur l'ancien point R:166. Non vérifié par le contrôleur : l'absence de la branche sur le dépôt distant (il n'avait pas d'accès réseau ; l'auteur l'a vérifiée par `git ls-remote`, §4), la CI et .NET.

Constats et suites données, avant le commit :

| Constat | Gravité | Suite |
|---|---|---|
| CI-01 — le rapport disait que chaque ligne de `main` reste le début de la ligne proposée ; c'est faux pour 9 lignes, où du texte est inséré | à corriger | corrigé (§1 et annexe C.2) |
| CI-02 — le §8, point 1, jugeait « réalisé » l'archivage visé par B3-03, en omettant « validation originale » | à corriger | reformulé, avec les trois conditions citées exactement |
| CI-03 — « attestés » surestimait la preuve des Q4 | observation | reformulé (§6) |
| CI-04 — « les pièces sont des transcriptions » généralisait | observation | précisé (§6) |
| CI-05 — le registre ne consigne pas D-01 et D-02 | observation | voulu par le propriétaire (annexe B) ; §6 et §8, point 12 |
| CI-06 — conventions de MEC-0002 omises au §1 ; le décompte « non commencé » inclut le gabarit | observation | corrigé (§1, §4) |

Ces corrections ne portent que sur le présent rapport ; le registre n'est pas modifié. Le même contrôleur les a contre-vérifiées (`CONTROLE-CORRECTIONS-RAPPORT.md`, SHA-256 `35e4bd00f13127e7ce10a58fe3331d16d1a0a112732fb70799cdfa30ba4a0c30`, non archivé) : verdict « conforme », avec trois observations de formulation (CI-07 à CI-09), intégrées ensuite. Écart déclaré par le contrôleur : une commande Git en lecture seule hors de la liste autorisée (`git merge-base --is-ancestor`), dont il n'a pas utilisé le résultat.

## 6. Limites de preuve

- **Authenticité des sources :** les pièces P1, P2, P3, P5 et P6 sont des transcriptions de la session de travail ; la v0.2 est un fichier joint par le propriétaire, reconstruction documentaire de l'orchestrateur ; la v0.4.3 est rédigée par Claude Code. L'identité des transcriptions avec la conversation de conception d'origine n'est pas vérifiée, et aucune pièce n'est authentifiée de façon indépendante (D-01). Le registre ne déclare pas la provenance vérifiée.
- **Q4 :** formulations résumées par l'orchestrateur (D-02). L'identifiant et l'option validés sont cités par la v0.2, elle-même reconstruction non authentifiée ; les valeurs de Q4.6 et Q4.7 sont confirmées par une déclaration du propriétaire, et le contenu de Q4.1 par sa confirmation W-01 et par R-6.
- **D-01 et D-02 ne figurent pas dans le registre.** Le paragraphe de provenance du nouveau bloc (ligne 162) dit qu'« Aucune pièce ne déclare expressément la réserve levée » ; ce texte reste exact, D-01 portant sur le caractère bloquant de la réserve, et non sur la provenance. Le propriétaire a choisi d'appliquer le diff v4 tel quel ; D-01 et D-02 sont consignées ici (annexe A).
- **Préparation non archivée :** les fichiers du §3 ne sont pas dans le dépôt. Le diff v4 est vérifiable par le commit lui-même, dont le résultat a l'empreinte `9054c825…`.
- **Tests .NET :** non exécutés localement (§4).
- **Options d'origine** de Q5.1, Q5.2, B3 et des six arbitrages : non transmises.

## 7. CI

La CI se déclenche au push et à l'ouverture de la PR, après le commit qui contient ce rapport : son état réel n'y figure donc pas. Il est vérifié sur la PR et communiqué au propriétaire tel qu'il est.

## 8. Points à décider par le propriétaire

La numérotation reprend celle de la préparation ; les renvois de l'annexe C y renvoient.

0. *Réserve de traçabilité de Q1 à Q3* : **tranché par D-01** (ne bloque plus l'inscription ; limites de preuve maintenues).
1. **Mention « provenance non vérifiée » des valeurs de Q1** (Q1.1, Q1.5, Q1.6, Q1.7, Q1.9) : conservée. B3-03 la lie à l'archivage de « leur validation originale », W-02 à « l'archivage des validations », et le rectificatif de B3 à « l'obtention des messages d'origine ». Sont archivées des transcriptions non authentifiées des validations ; les messages d'origine ne sont pas obtenus. Sa levée relève d'une décision distincte.
2. *Inscription de Q4 sur la base de résumés* : **tranché par D-02**.
3. **Date et référence de l'inscription :** les annotations portent « Annotation ajoutée lors de l'inscription des décisions des 19 et 20 novembre 2026 », sans date ni renvoi au présent rapport. Un renvoi pourra être ajouté par un mandat distinct.
4. **R:166 :** le cas « augmentation imprévue du coût » est classé tranché, comme conséquence de M-05, que la pièce n'énonce pas en ces termes ; le repli d'une diagonale reste ouvert.
5. **Annotations de S2, S8, S11 et N4**, hors de la liste du §9.2 de la v0.4.3 : appliquées avec le diff v4.
6. **Renvoi à OXCE de l'ancien point « coûts » (R:152)** : supprimé avec la réécriture du point.
7. **CH-08** : non annotée (« inchangée » selon la v0.4.3).
8. *Base* : vérifiée, inchangée (§4).
9. **Rapport case/étage** : chiffré à 0,5 avec les valeurs initiales, sous réserve, et laissé ouvert hors de ces valeurs.
10. **Critère « terrain » du réveil** : laissé ouvert.
11. *Annotation d'archivage du bloc du 17 novembre 2026* : appliquée avec le diff v4, dont l'autorisation la couvre.
12. **Mention de D-01 et de D-02 dans le registre** : non faite (§6) ; possible par un mandat distinct.

## 9. Statut des mécaniques

MEC-0001 et MEC-0002 restent **reportées** dans leur ensemble : leurs lignes « Décision du propriétaire » commencent toujours par « reportée », leurs classes restent `MODIFICATION-PROPOSEE` et leur état d'implémentation « non commencé ». Aucun gameplay ni aucune implémentation n'est autorisé. La fusion de la PR fera l'objet d'une autorisation distincte.

## Annexe A — Mandat, tel que reçu (2026-11-21T16:52:29.515Z)

Texte extrait du journal de la session de travail, reproduit sans correction.

````text
BASTION — Mandat d'inscription documentaire MEC-0001 / MEC-0002
Statut : préparé pour autorisation d'exécution.
Objet : inscrire les décisions validées Q1 à Q5, B3 et les six arbitrages complémentaires dans le registre officiel de Bastion.
1. Base de travail
Dépôt : `mengpo1/bastion`
Fichier à modifier exclusivement :
`docs/gameplay/GAMEPLAY-DECISIONS.md`
Diff validé comme base :
`inscription-prep/PROPOSITION-GAMEPLAY-DECISIONS.diff`
SHA-256 :
`8f78ef25201fed272a7ec95c2c1dc83431a3a943511627aa0f1a1b90480a160f`
Registre proposé :
`inscription-prep/registre-propose.md`
SHA-256 :
`9054c825cecfd61c82689c984a4a7f1057f77c756d8227cab2bf2f707236c68e`
Ces fichiers se trouvent dans le scratchpad de la session précédente. Ne pas les reconstruire approximativement s'ils sont indisponibles.
2. Décisions complémentaires du propriétaire
Le propriétaire a validé explicitement le 21 novembre 2026 :
D-01 — Q1 à Q3
La réserve de traçabilité précédemment qualifiée de bloquante ne bloque plus l'inscription documentaire.
La provenance et l'authenticité des échanges d'origine restent des limites de preuve. Ne pas les déclarer vérifiées.
D-02 — Q4
Les décisions Q4 peuvent être inscrites à partir des résumés disponibles.
Indiquer explicitement leur provenance et leur niveau de preuve. Ne pas les présenter comme des citations littérales de sources originales indisponibles.
Les valeurs initiales de test restent identifiées comme telles.
Ces deux décisions autorisent le traitement documentaire des sources concernées. Elles n'autorisent aucune implémentation.
3. Exécution prévue
Après autorisation explicite du présent mandat :

1. Exécuter `git fetch origin main`.
2. Vérifier que le registre correspond exactement à la base du diff v4.
3. Vérifier les empreintes du diff et du registre proposé.
4. Créer une nouvelle branche dédiée depuis `origin/main` : `claude/inscription-mec-0001-mec-0002-q1-q5-b3`, sous réserve qu'elle n'existe pas déjà.
5. Appliquer exclusivement le diff v4.
6. Vérifier que le résultat est identique au registre proposé.
7. Contrôler l'absence de décisions supplémentaires, de PNV inscrites et de modifications de gameplay.
8. Faire réaliser un contrôle indépendant ciblé du changement effectivement appliqué.
9. Rédiger un rapport d'exécution dans `docs/reviews/`, conformément à `CLAUDE.md`.
10. Après contrôles satisfaisants, créer un commit documentaire unique, pousser uniquement la branche autorisée et ouvrir une PR en brouillon vers `main`.

Si la base a changé ou si le diff ne s'applique plus exactement, arrêter sans adapter les décisions.
Ne pas ajouter de corrections éditoriales ou techniques au diff v4 sans autorisation.
4. Périmètre strict

* Conserver le texte historique des décisions.
* Ne modifier que le registre et ajouter le rapport d'exécution requis.
* Ne pas modifier les mandats, le harnais, le code ou les tests du jeu.
* Ne pas ajouter de code, données ou assets d'OXCE.
* Ne pas résoudre les paramètres encore ouverts.
* Ne pas créer de règle par déduction.
* Ne pas fusionner la PR.

MEC-0001 et MEC-0002 doivent conserver leur statut « reportée ».
Aucune implémentation n'est autorisée.
5. Livrable final
Remettre :

* le numéro et le lien de la PR ;
* la branche et le SHA du commit ;
* le diff réellement publié ;
* le résultat du contrôle indépendant ;
* l'état réel de la CI ;
* le chemin du rapport d'exécution ;
* la confirmation que les deux mécaniques restent reportées.

La fusion fera l'objet d'une autorisation distincte.
````

## Annexe B — Autorisation (2026-11-21T16:55:19.533Z)

Réponse du propriétaire à la question posée par Claude Code après les vérifications préalables, telle qu'enregistrée par l'outil de question de la session, sans correction.

````text
Your questions have been answered: "Le mandat d'inscription MEC-0001/MEC-0002 est marqué « préparé pour autorisation d'exécution ». Les vérifications préalables sont conformes : main inchangé (7c5e325f), registre = base du diff v4, empreintes exactes, branche inexistante. Remarque : le diff v4 ne mentionne pas vos décisions D-01 et D-02 du 21 novembre. Son paragraphe de provenance (P:162) reste littéralement exact (« Aucune pièce ne déclare expressément la réserve levée »), mais n'indique pas que la réserve ne bloque plus l'inscription. Autorisez-vous l'exécution (branche, application du diff, contrôle indépendant, rapport, commit unique, push de la seule branche autorisée, PR en brouillon) ?"="Autoriser, diff v4 tel quel (Recommandé)". You can now continue with these answers in mind.
````

## Annexe C — Matrice : décision → source → ligne actuelle → modification

Reprise de la matrice de la préparation. « R:NN » : ligne du registre sur `main` avant l'inscription ; « P:NN » : ligne du registre après l'inscription. P1 `revue-v03/PIECES-Q1-Q3-TRANSMISES.md` ; P2 `revue-v03/PIECES-Q4-Q5-B3-DECLARATIONS.md` ; P3 `revue-v03/PIECES-MANDATS-ET-CONFIRMATIONS.md` ; P5 `revue-v03/PIECE-Q1.1-Q1.4-OPTIONS-B.md` ; P6 `revue-v03/PIECE-MANDAT-v0.4.2-ARBITRAGES.md` ; v0.2 `pieces-jointes/4f625a0d-BASTION-MEC-0001-CONSOLIDATION-Q1-Q4-REVUE.md` ; v0.4.3e `revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.3-erratum-AR01-AR02-EXPURGE-D4.md`, tous sous `docs/reviews/MEC-0001-Q1-Q5-B3/`. Les numéros de ligne de la matrice ont été établis sur la v1 et restent valables : les corrections ultérieures n'ont modifié que le contenu de lignes existantes. La ligne de la réserve de traçabilité de Q1 à Q3 ajoute aussi, depuis la v4, W-02 (P3 l.121) et le message F (P3 l.10).

**Nature du texte inscrit :**
- **CIT. DIR.** : citation directe de la pièce, entre guillemets ;
- **VAL. EXPL.** : validation explicite, citée par sa source ;
- **RÉSUMÉ** : reformulation, par l'orchestrateur ([CIT]) ou par moi, que la pièce soutient ;
- **DÉD.** : déduction, signalée comme telle.

Les niveaux de preuve [TR], [TR-M], [CIT], [DÉC], [CONF] et [VAL] sont ceux de la v0.4.3e (§0), repris dans le bloc (P:153-158).

### C.1 Décisions inscrites dans le nouveau bloc

| Décision | Nature du texte inscrit | Source exacte | Preuve | Ligne actuelle | Modification |
|---|---|---|---|---|---|
| Q1.1 | CIT. DIR. de l'option A | option A : P1 l.301 ; validation : P1 l.309 (VAL. EXPL., « Ma validation originale était ») ; option B : P5 l.14 | [TR-M] ; provenance non vérifiée | aucune (nouveau) | P:165 ; annotations de G1 (R:134) et de GE-02 (R:203) |
| Q1.2 | CIT. DIR. | P1 l.303, 309 ; P5 l.15 ; R-8 : P6 l.96 | [TR-M] | aucune | P:166 ; annotation de GE-03 (R:204) |
| Q1.3 | CIT. DIR. | P1 l.305, 309 ; P5 l.16 | [TR-M] | aucune | P:167 ; annotation de G1 |
| Q1.4 | CIT. DIR., marquée historique | P1 l.307, 309 ; P5 l.17 ; R-7 : P6 l.85 | [TR-M] | aucune | P:168 ; annotation de GE-02 |
| Q1.5 | RÉSUMÉ de la valeur validée (1 500 mm) | proposition : P1 l.15 ; validation : P1 l.67 (« Q1.5 largeur de case=1500 mm ») | [TR] ; provenance non vérifiée | aucune | P:170 ; annotations de GE-02 et de G1 |
| Q1.6 | CIT. DIR. | P1 l.23 et 25 ; validation : P1 l.67 (« Q1.6 profil humain=A ») | [TR] ; provenance non vérifiée | aucune | P:171 ; annotation de GE-03 |
| Q1.7 | RÉSUMÉ de la valeur (100 mm) | P1 l.33 ; P1 l.67 (« Q1.7 mur standard=100 ») | [TR] ; provenance non vérifiée | aucune | P:172 ; annotation de GE-02 |
| Q1.8 | RÉSUMÉ (3 000 mm) ; cadre configurable marqué historique | P1 l.41, 67 | [TR] | aucune | P:173 ; P:177 |
| Q1.9 | CIT. DIR. | P1 l.49, 67 | [TR] ; provenance non vérifiée | aucune | P:174 |
| Portée de Q1.5 à Q1.9 | CIT. DIR. | P1 l.55 | [TR] | aucune | P:176 |
| Hauteur d'étage (Q4.1, W-01, R-6, R-7) | RÉSUMÉ de la règle ; CIT. DIR. de W-01 et de R-6 | Q4.1 : v0.2 l.86, validation l.181 ; W-01 : P3 l.88 ; R-6 : P6 l.73 ; R-7 : P6 l.85 et l.91 (conséquence) | [CIT] + [CONF] + [VAL] | GE-02 (R:203), « Décisions antérieures remplacées » (R:325), « Encore ouvert » (R:336) | P:177 ; annotations de GE-02 et de DS1.1 ; P:428 |
| Q2.1 à Q2.4 | CIT. DIR. | P1 l.73, 79, 85, 91 ; validation P1 l.111 | [TR] | N4 (R:94), ARB-C (R:123), R:153 | P:188-192 ; annotations de N4 et d'ARB-C ; P:244 |
| Q2.5 | CIT. DIR. | P1 l.99, 111 | [TR] | R:151 ; G1 (R:134) | P:178 ; P:242 ; annotation de G1 |
| Q2.6 | CIT. DIR. ; B3-04 en RÉSUMÉ | P1 l.105, 111 ; B3-04 : P2 l.171-181 | [TR] ; [DÉC] | CO-01 inchangée | P:179 |
| Q3.1 | CIT. DIR. | P1 l.117, 165 | [TR] | S2 (R:72), R:152, G3 (R:141) | P:208 ; annotations de S2 et de G3 ; P:243 |
| Q3.2 | CIT. DIR. | P1 l.123, 165 | [TR] | S2, G3 | P:209 ; annotations |
| Q3.3 | CIT. DIR. | P1 l.131, 165 | [TR] | ARB-C, G3 | P:193 ; annotations |
| Q3.4 | CIT. DIR. | P1 l.137, 165 | [TR] | S8 (R:78), R:166, R:167 | P:221 ; annotation de S8 ; P:258-259 |
| Q3.5 | CIT. DIR. | P1 l.143, 165 | [TR] | EN-06 (R:310) | P:224 ; annotation d'EN-06 |
| Q3.6 | CIT. DIR. | P1 l.149, 165 | [TR] | G3, R:163 | P:213 ; annotation de G3 ; P:254 |
| Portée de Q3.1 à Q3.6 | CIT. DIR. | P1 l.153-161, 165 | [TR] | ES-09 (R:286) | P:212 ; annotation d'ES-09 |
| Q3.7 à Q3.9 | CIT. DIR. (Q3.8 citée sans la fin « avec arrondi entier à définir », que Q3.13 tranche) | P1 l.173, 181, 187 ; validation P1 l.213 | [TR] | G3, R:152 | P:210 ; annotations de S2, G1, G3 |
| Q3.10 (option B) | CIT. DIR. | P1 l.197, 213 | [TR] | ARB-C, G3 | P:193 |
| Q3.11 (option B) | CIT. DIR. | P1 l.203, 213 | [TR] | G3, R:163 | P:213 |
| Q3.12 | CIT. DIR. | P1 l.207, 213 | [TR] | S2, G1, G3, R:152 | P:194 ; annotations |
| Q3.13 | CIT. DIR. | P1 l.225-233, 293 | [TR] | S2, G3 | P:211 ; annotations |
| Q3.14 | CIT. DIR. | P1 l.251-259, 293 | [TR] | ARB-D (R:124), N14 (R:109), R:160 | P:216 ; annotations ; P:251 |
| Q4.1 | voir « Hauteur d'étage » | v0.2 l.86 ; l.181 | [CIT] + [CONF] + [VAL] | GE-02 | P:177 |
| Q4.2 | RÉSUMÉ [CIT] | v0.2 l.87 ; l.181 | [CIT] | GE-05 inchangée | P:183 |
| Q4.3 | RÉSUMÉ [CIT] | v0.2 l.88 ; l.183 | [CIT] | EN-03 inchangée | P:225 |
| Q4.4 | RÉSUMÉ [CIT] | v0.2 l.89 ; l.183 | [CIT] | EN-06 (R:310), R:345 | P:226 ; annotation d'EN-06 ; P:437 |
| Q4.5 | RÉSUMÉ [CIT] | v0.2 l.93 ; l.185 | [CIT] | GE-07 (R:208), CH-14 (R:255), ARB-D, N14, R:338 | P:217 ; annotations ; P:430 |
| Q4.6 | RÉSUMÉ [CIT] ; valeurs : VAL. EXPL. [DÉC], citée | v0.2 l.94 ; l.185 ; P2 l.18 | [CIT] + [DÉC] | ARB-D, R:161, R:163 | P:214 ; annotations ; P:252, P:254 |
| Q4.7 | RÉSUMÉ [CIT] ; valeurs [DÉC], citées | v0.2 l.95 ; l.185 ; P2 l.18 | [CIT] + [DÉC] | ARB-C, R:151 | P:195 ; P:242 |
| Q4.8 à Q4.12, Q4.15 | RÉSUMÉ [CIT] | v0.2 l.96, 97, 101, 102, 103, 106 ; l.185, 187, 189 | [CIT] | ARB-C, R:153 | P:196-202 ; P:244 |
| Q4.13 | RÉSUMÉ [CIT] | v0.2 l.104 ; l.189 | [CIT] | ARB-E (R:125) | P:228 ; annotation d'ARB-E |
| Q4.14 | RÉSUMÉ [CIT] | v0.2 l.105 ; l.189 | [CIT] | EN-03, EN-08 inchangées | P:229 |
| Q4.16 | RÉSUMÉ [CIT], sans la règle « X d'abord » | v0.2 l.110 ; l.191 | [CIT] | G4 (R:142-147), R:162 | P:235 ; annotation de G4 ; P:253 |
| Q4.17 | RÉSUMÉ [CIT] | v0.2 l.111 ; l.191 | [CIT] | R:163 | P:236 ; P:254 |
| Q4.18 | RÉSUMÉ [CIT] | v0.2 l.112 ; l.191 | [CIT] | GE-03, G2 (R:140) | P:237 ; annotations ; P:255 |
| Q4.19 | RÉSUMÉ [CIT] | v0.2 l.113 ; l.191 | [CIT] | G2 (R:135-140) | P:238 ; annotation de G2 ; P:255 |
| Q4.20 | RÉSUMÉ [CIT] | v0.2 l.114 ; l.191 | [CIT] | S11 (R:81), R:163 | P:230 ; annotation de S11 ; P:254 |
| Q4.21 | RÉSUMÉ [CIT] ; portée du coût par M-05 | v0.2 l.115 ; l.191 | [CIT] | S8, R:166 | P:223 ; annotation de S8 ; P:258 |
| Q5.1 | CIT. DIR. de l'addendum | P2 l.28-32 (message B) ; l.70-82 (addendum Q5, §A) | [DÉC] | ARB-E | P:227 ; annotation d'ARB-E |
| Q5.2 | CIT. DIR. ; rectification relative à Q4.15 en RÉSUMÉ | P2 l.34-38 ; l.83-95 | [DÉC] | S10 (R:80) | P:203 ; annotation de S10 |
| B3 | RÉSUMÉ de B3-01, B3-04 et B3-05 ; CIT. DIR. de B3-01 et du rectificatif §1 | P2 l.124-201 (B3-01 l.129-135) ; rectificatif l.207-257 (§1 l.217-219) ; validation du rectificatif : P3 l.101 | [DÉC] ; rectificatif [CONF] | GE-02, GE-03 (R:203-204) | P:180 ; annotations de GE-02 et de GE-03 ; champs de MEC-0002 |
| B3-03 (réserve de provenance) | CIT. DIR. | P2 l.169 ; rectificatif §3 : P2 l.237 | [DÉC] ; [CONF] | aucune | P:162 |
| Réserve de traçabilité de Q1 à Q3 | CIT. DIR. ; RÉSUMÉ du constat « aucune pièce ne la déclare levée » | P2 l.17 (message A), l.46 (message B), l.111 (addendum Q5, §D) ; partie « Mission » de JS-31 : `verif-v043/messages-extraction-3.md`, message 31 ; message F : P3 l.9 et l.14 | [DÉC] | aucune | P:162 |
| M-04=B | CIT. DIR. de la décision et du statut ; conséquences en RÉSUMÉ | P6 l.32, 35-40, 42 | [VAL] | ARB-D, N14, R:160 | P:218 ; annotations ; P:251 |
| M-05=A | CIT. DIR. ; conséquences en RÉSUMÉ | P6 l.45, 48-55, 56 | [VAL] | G3, S8, R:166 | P:222 ; annotations ; P:258 |
| R-5=A | CIT. DIR. ; conséquences en RÉSUMÉ | P6 l.59, 62-67, 69, 70 | [VAL] | GE-02, GE-03, R:151, R:336 | P:181 ; annotations ; P:242, P:428 |
| R-6=A | CIT. DIR. | P6 l.73, 82 | [VAL] | GE-02 | P:177 ; annotation de GE-02 |
| R-7=A | CIT. DIR. | P6 l.85, 91, 93 | [VAL] | GE-02 | P:168, P:177 ; annotation de GE-02 |
| R-8=A | CIT. DIR. | P6 l.96, 103, 106, 107 | [VAL] | GE-03 | P:166, P:182 ; annotation de GE-03 |

### C.2 Règles existantes annotées ou actualisées

Les annotations conservent le texte historique : la ligne de `main` reste le début de la ligne annotée. Dans les en-têtes et les champs de fiche (R:51, R:58-60, R:62, R:175, R:182, R:184) et dans DS1.1 (R:325), du texte est inséré dans la ligne ; seule la conjonction « et » d'une énumération prolongée y devient une virgule (R:59, R:62).

| Règle ou ligne | Ligne actuelle | Décisions sources | Modification |
|---|---|---|---|
| En-tête de MEC-0001 | R:51 | toutes | ajout de « Q1 à Q5, B3, M-04, M-05 et R-5 à R-8 les 19 et 20 novembre 2026 » |
| Références | R:58 | — | ajout du dossier `docs/reviews/MEC-0001-Q1-Q5-B3/` |
| Changement demandé | R:59 | — | liste des sous-décisions complétée |
| Décision du propriétaire | R:60 | toutes | phrase de provenance renvoyant au nouveau bloc ; la décision globale reste « reportée » |
| Éléments exclus | R:62 | — | liste complétée ; PNV-1 à PNV-9 exclues |
| S2 | R:72 | Q3.1, Q3.2, Q3.9, Q3.12, Q3.13 | annotation « précisée » |
| S8 | R:78 | Q3.4, Q4.21, M-05 | annotation « précisée » |
| S10 | R:80 | Q5.2, Q4.15 | seconde annotation : aucune exception supplémentaire |
| S11 | R:81 | Q4.20 | annotation « précisée » |
| N4 | R:94 | Q2.1 à Q2.4 | annotation « précisée » |
| N14 | R:109 | Q3.14, Q4.5, M-04 | annotation ; articulation avec le principe d'OXCE déclarée ouverte |
| Bloc du 17 novembre 2026 | R:115 | — (archivage, commit `1ecc608`) | annotation : les deux documents sont archivés depuis, aux mêmes empreintes ; empreintes vérifiées sur `main` |
| ARB-C | R:123 | Q2.1-Q2.4, Q3.3, Q3.10, Q3.12, Q4.7-Q4.12, Q4.15, Q5.2 | annotation « précisée » |
| ARB-D | R:124 | Q3.14, Q4.5, Q4.6, M-04 | annotation ; clause « La surcharge ne majore pas le prix des pas » maintenue |
| ARB-E | R:125 | Q5.1, Q4.13 | annotation « précisée » |
| G1, « Ouvert » | R:134 | Q1.1-Q1.3, Q1.5-Q1.7, Q2.5, Q3.9, Q3.12, Q3.13 | annotation « en partie précisé » ; PNV-7 déclarée non décidée |
| G2, « Ouvert » | R:140 | Q4.18, Q4.19 | annotation « en partie tranché » |
| G3 | R:141 | Q3, Q4.6, M-05 | annotation « en partie tranché » ; esquives toujours sans énergie |
| G4 | R:147 | Q4.16 | annotation |
| « Encore ouvert » : géométrie | R:151 | Q1, Q2.5, Q2.6, B3, R-5, R-6, Q4.7 | réécrit : décidé, puis ouvert |
| « Encore ouvert » : coûts | R:152 | Q3 | réécrit ; renvoi à OXCE retiré avec le point devenu sans objet (§8, point 6) |
| « Encore ouvert » : escaliers | R:153 | Q2, Q4.8-Q4.12, Q4.15, Q5.2 | réécrit |
| « Encore ouvert » : chutes | R:154-159 | — | inchangé |
| « Encore ouvert » : surcharge | R:160 | Q3.14, Q4.5, M-04 | réécrit |
| « Encore ouvert » : capital de TU | R:161 | Q4.6 | réécrit |
| « Encore ouvert » : chemin | R:162 | Q4.16 | réécrit |
| « Encore ouvert » : orientation, énergie, interruptions | R:163 | Q4.17, Q3.6-Q3.9, Q3.11, Q4.6, Q5.1, Q4.13, Q4.14, Q4.20 | réécrit ; « autres interruptions » conservées ouvertes |
| « Encore ouvert » : postures et réveil | nouveau (P:255) | Q4.18, Q4.19 | ajouté |
| « Encore ouvert » : visibilité, interface | R:164-165 | — | inchangés |
| « Encore ouvert » : trajet non payable | R:166 | Q3.4, Q4.21, M-05 | réécrit (§8, point 4) |
| « Encore ouvert » : LOT-2B | R:167 | Q3.4, Q3.13, Q5.1 | complété ; « paiement de chaque pas » conservé parmi les propositions non arbitrées |
| Non-exhaustivité | R:169 | — | complétée |
| En-tête de MEC-0002 | R:175 | B3, R-5 à R-8 | complété |
| Références de MEC-0002 | R:182 | — | dossier ajouté |
| Décision de MEC-0002 | R:184 | B3, rectificatif, R-5 à R-8 | phrase ajoutée ; la décision globale reste « reportée » |
| Conventions de MEC-0002 | R:193 | — | sens de Q*n*.*m*, B3, M-04, M-05, R-5 à R-8 |
| GE-02 | R:203 | B3, rectificatif, Q1.1, Q1.5, Q1.7, Q4.1, W-01, R-5, R-6, R-7 | annotation : clause « proportions » **modifiée** |
| GE-03 | R:204 | B3-03, Q1.2, R-8, Q1.6, R-5, Q4.18 | annotation : **précisée** |
| GE-07 | R:208 | Q4.5, Q3.14 | annotation |
| CH-14 | R:255 | Q4.5 | annotation |
| ES-09 | R:286 | Q3.1, Q3.7, Q3.8, Q3.13, S2, G3, portée de Q3.1-Q3.6 | annotation : coût de marche en TU, sans énergie |
| ES-10 | R:287 | G3 | annotation : débit en TU seulement |
| EN-06 | R:310 | Q4.4, Q3.5 | annotation : clé d'ordre tranchée |
| DS1.1 (décisions remplacées) | R:325 | B3, R-5 | complété |
| « Encore ouvert » : géométrie | R:336 | B3, R-5, R-6, Q4.1, Q1, rectificatif §3 | réécrit |
| « Encore ouvert » : force et charge | R:338 | Q4.5 | réécrit |
| « Encore ouvert » : événements | R:345 | Q4.4 | réécrit |
| Non-exhaustivité | R:350 | — | complétée |

### C.3 Règles examinées, non annotées

| Règle | Ligne | Lien avec les décisions | Raison |
|---|---|---|---|
| CH-08 | R:249 | rectificatif §1, R-6 | inchangée selon la v0.4.3e (§9.1) : 3 m = 3 000 mm ; la contrainte d'entiers n'est pas étendue aux calculs. Hors de la liste du mandat. Voir le §8, point 7 |
| GE-04, GE-05, CO-01 | R:205-206, R:265 | B3-03, B3-04, Q4.2 | B3-04 les déclare inchangées |
| EN-03, EN-08 | R:307, R:312 | Q4.3, Q4.14 | compatibles ; renvoi par `MEC-0002` dans Q4.3, Q4.9, Q4.14 |
| ARB-A, ARB-B, Z1, S9 | R:121-122, R:90, R:79 | G1, G2, Q4.19, Q4.21, Q3.4 | aucune précision nouvelle au-delà de G1, de G2 et des annotations de S8 et de S10 |
| ES-08, ES-11, ES-12, RP-03, RP-05 | — | Q4.19 | inchangées : l'admissibilité d'une case portant un corps reste du ressort de `MEC-0002` |


## Annexe D — Décisions et éléments non inscrits

| Élément | Source | Raison |
|---|---|---|
| PNV-1 à PNV-9 (repère, conversion « vers demi-entiers », liste fermée de huit orientations, support uniforme et centre de case, refus au-delà des seuils de ressaut, phases d'un pas, priorité « X puis Y », ordre de réveils simultanés, position exacte des rencontres) | v0.2 l.29-40 ; v0.4.3e §3.5 | proposées, non validées (RD-4) ; consigne du mandat. Seules les parties tranchées ailleurs sont inscrites, par leur propre source : millimètres entiers des dimensions configurées (R-5), largeur paire (Q1.1), enveloppes paires (Q2.6) |
| Règle « X d'abord » du résumé de Q4.16 | v0.2 l.110 | renvoi sans objet : aucune règle de ce nom dans les pièces de Q1 (PNV-7). Le bloc le dit (P:235) |
| Scénarios T01 à T48 | v0.4.3e §13 | ce ne sont pas des règles ; aucun n'est exécuté |
| Conséquences [DÉD] : barème dérivé (par exemple 9 TU et 5 d'énergie en diagonale difficile), largeur intérieure de 1 400 mm, enveloppes de 850 et 1 274 mm, étendue de 1 341,6 mm, profil contenu dans la case, coût de la case d'arrivée pour Q3.1, orientation à 45°, « deux unités conscientes ne peuvent occuper la même case », nécessité d'un calcul exact pour Q3.14, réserve des cycles gratuits | v0.4.3e §3.6, §4, §5, §7 | déductions, qui ne valent pas décision. Seuls restent : le rapport case/étage de 0,5 avec les valeurs initiales, sous réserve de leur confirmation, parce que le rectificatif validé l'énonce lui-même (P2 l.239) ; la conclusion « le rapport n'est plus un paramètre distinct » (v0.4.3e §9.1, [DÉD]) n'est pas inscrite, et le rapport reste ouvert hors des valeurs initiales ; la fermeture partielle de R:166, conséquence de M-05 (§8, point 4) |
| Comparaisons avec OXCE, dont le « point d'articulation » de la récupération d'énergie | v0.4.3e §5 et §11 | analyses, et non décisions ; AE-01 juge l'explication de la récupération d'énergie incomplète ; décision D4 |
| Options écartées : Q3.10=A (profil chiffré des connexions), Q3.11=A (100 et 20), toutes les options B et C | P1 | non retenues. La coïncidence entre Q3.11=A et les valeurs d'énergie de Q4.6 n'est pas inscrite |
| Exemple chiffré de Q3.14 (30 kg, 40 kg, 45 TU) | P1 l.277-289 | exemple déclaré fictif |
| Remarque « Cohérent avec GE-02 et CH-08 » du résumé de Q4.1 ; renvois de vérification des messages de validation | v0.2 l.86, l.181-191 | commentaires, et non contenu de décision |
| Textes de méthode et de mandat (« Mission », consignes, conditions de clôture du message C, §E) | P1, P2, P3, P6 | consignes de travail, et non décisions de gameplay |
| Réserves documentaires RD-1 à RD-10, AE-01, AE-02, OC-01 à OC-07 | v0.4.3e §14 ; notice §3 | elles restent dans le dossier ; le bloc en donne l'essentiel (transcriptions non authentifiées, résumés de Q4, options absentes, provenance non vérifiée des valeurs de Q1) et renvoie à la notice |
| Recommandation de méthode arithmétique (rationnels, entiers) | v0.4.3e §5 | [OUV], non arbitrée |
