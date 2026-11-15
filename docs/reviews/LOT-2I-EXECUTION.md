# LOT-2I — Rapport d'exécution : consolidation de `MEC-0002` et diff proposé du registre

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2I-v1.1.md`, `orchestration/mandats`, commit `58d3ebc`, SHA-256 `6ac95b0d…6ef6`. Non archivé (non autorisé). |
| Autorisation | Propriétaire, 14 novembre 2026 : exécution documentaire du mandat v1.1 ; branche locale `docs/lot-2i-consolidation-mec-0002` depuis `origin/main` ; archivage du mandat et modification de `docs/mandates/README.md` **non autorisés** ; aucun push, aucune PR, aucune fusion, aucune modification du registre protégé, aucune implémentation. |
| Branche | `docs/lot-2i-consolidation-mec-0002`, créée depuis `origin/main` = `74faa2974da7a4645725b4271eb66ae2a512e98a`, après `git fetch origin main`. |
| Publication | D'abord un commit local seulement (`8b84f0c`). Puis autorisée par le propriétaire le 14 novembre 2026 (« Je valide », précisé en « Publier en PR brouillon ») : branche poussée et PR en brouillon vers `main`, **sans fusion**. |
| Implémentation | **Aucune autorisation d'implémentation** n'existe ni ne découle de ce lot. |

> **Correctif v1.2** : les §1 à §8 décrivent l'exécution v1.1 (commit `cca1690`) et sont conservés tels quels, comme historique ; leurs comptes (64 / 33 / 8, 28 ambiguïtés, 26 critères) sont dépassés. L'état après le correctif v1.2, ses contrôles et sa revue figurent au §9.

## 1. Bilan

- **Consolidation** (`LOT-2I-CONSOLIDATION-MEC-0002.md`) :
  - 105 règles identifiées : les 103 règles de C2, plus 2 règles de DS1 à DS5 que C2 ne redit pas mais ne modifie pas (GE-09, RP-09) ;
  - 64 validées en conception, 33 avec un paramètre ouvert, 8 à confirmer avant inscription ;
  - les interactions avec `MEC-0001` sont décrites ;
  - les 8 contradictions demandées par le mandat sont analysées, et 12 autres constats ajoutés ;
  - 28 ambiguïtés sont à trancher avant une implémentation déterministe, dont 8 avant même l'inscription ;
  - les limites de traçabilité sont consignées.
- **Matrice** (`LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`) :
  - pour chacune des 105 règles : source, date, formulation ancienne, priorité, conflit et statut ;
  - le tableau des écarts de C2 est vérifié ligne à ligne (3 descriptions inexactes de l'historique, et 6 écarts qu'il ne mentionne pas) ;
  - 26 critères de tests futurs : 8 spécifiables, 16 partiels, 2 bloqués ;
  - l'effet sur la matrice du LOT-2F est décrit.
- **Diff proposé** (`LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md`) :
  - `MEC-0001` est annotée, sans changement de statut ;
  - une nouvelle fiche `MEC-0002` est proposée, « reportée », avec les 105 principes, dont 8 marqués « à confirmer avant inscription définitive » ;
  - le diff exact s'applique au registre de `main` ; **il n'est pas appliqué**.
- **Constats principaux** :
  - le tirage commun aux deux unités d'une collision (CO-08), combiné au facteur de masse déterministe (CO-03), fixe l'ordre des blessures avant l'armure ; à puissances égales, la plus légère est toujours la plus blessée. Cela contredit DS4.1, selon une lecture à confirmer (consolidation, §11.1, point 8 ; A8) ;
  - l'unité qui tombe d'un étage sans surcharge sur une unité n'est plus exemptée de dégâts, changement que C2 ne signale pas (§11.2, X12 ; A25).

## 2. Sources lues

| Source | Emplacement | Empreinte |
|---|---|---|
| `CLAUDE.md` | `main` | `74faa29` |
| Mandat LOT-2I v1.1 | `orchestration/mandats`, commit `58d3ebc` | SHA-256 `6ac95b0d…6ef6` |
| Mandat LOT-2I v1.0 (historique) | `orchestration/mandats`, commit `9f24ce8` | SHA-256 `9a14d831…cbfa` |
| Consolidation provisoire C2 | `orchestration/mandats`, commit `d028c52` | SHA-256 `8e7c652b…dd83` ; objet Git `2cd7e97a…` |
| Déclaration D2 du propriétaire | conversation, 14 novembre 2026 | texte cité dans la consolidation, en-tête |
| Registre | `main` | objet Git `a72df450…` (identique à celui cité par C2) ; SHA-256 `c2a3a55e…3968` |
| LOT-2F, LOT-2G, LOT-2H (spécification, matrice, arbitrages, impacts, proposition, traçabilité, exécution) ; consolidation DS1 à DS5 | `main` | `74faa29` |

## 3. Fichiers produits (locaux)

| Fichier | Nature |
|---|---|
| `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` | spécification consolidée, états, sources, contradictions, ambiguïtés |
| `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` | provenance, écarts, tests futurs |
| `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md` | texte et diff proposés, non appliqués |
| `docs/reviews/LOT-2I-EXECUTION.md` | ce rapport |

Aucun autre fichier n'est créé ni modifié. En particulier, rien dans `docs/mandates/`.

## 4. Contrôles

Exécutés le 14 novembre 2026, après intégration de la revue, sur les fichiers indexés, avant le commit.

- **Base** : `git fetch origin main orchestration/mandats` ; `git rev-parse HEAD origin/main` donne `74faa29…` pour les deux ; `git merge-base --is-ancestor origin/main HEAD` : code 0.
- **Périmètre** : `git diff --cached --name-status origin/main` liste exactement les 4 fichiers du §3, tous dans `docs/reviews/`.
- **Fichiers protégés** : `git diff --cached --quiet origin/main -- docs/gameplay docs/decisions docs/references docs/mandates CLAUDE.md .claude scripts .github src tests` : code 0. Même résultat sur l'arbre de travail pour le registre, dont le SHA-256 reste `c2a3a55e…3968`.
- **Source C2** : SHA-256 `8e7c652b…dd83` sur `orchestration/mandats`, inchangé depuis la lecture.
- **Espaces** : `git diff --cached --check origin/main` : aucune sortie, code 0 ; `grep -nE ' +$'` sur les 4 fichiers : aucune ligne, code 1.
- **Diff proposé** :
  - le bloc extrait du document passe `git apply --check` sur le registre, code 0 ;
  - `patch -o` sur une copie hors dépôt : code 0, résultat identique au registre proposé (`cmp` : code 0) ;
  - le texte rendu de la fiche (§2 du document) est identique au bloc que le diff insère.
- **Harnais, simulé sur le registre proposé** : le champ « Décision du propriétaire » de `MEC-0001` et celui de `MEC-0002` commencent par « reportée ». `scripts/harness/check-simulation-trace.sh` refuserait donc toute déclaration de code pour l'une ou l'autre.
- **Cohérence** (scripts) :
  - les mêmes 105 identifiants dans la consolidation, la matrice et la fiche ;
  - aucun identifiant cité sans être défini ;
  - statuts identiques entre la matrice et la consolidation ;
  - texte de chaque règle de la fiche identique à la consolidation (seules les abréviations « C2 », « D2 » et « G » y sont écrites en toutes lettres) ;
  - ambiguïtés A1 à A28 définies, et aucune autre citée ;
  - chaque règle citée du LOT-2F (J, K, D, I, P, H, E) et du registre (S, Z, N) existe ;
  - chaque test du LOT-2F cité existe.
- **Tableaux** : nombre de colonnes cohérent ; aucune barre verticale non échappée dans du code.
- **Valeurs illustratives** : aucune dans la fiche proposée (recherche de 3,24, `M_ref = 80`, 0,236, « optionnel »).
- **Harnais** : `bash scripts/harness/test-hooks.sh` : 75 tests, 0 échec, code 0.
- **.NET** : non lancé, car `dotnet` est absent de l'environnement et le lot ne touche ni au code ni aux tests.
- Aucun identifiant de modèle dans les fichiers du lot.

## 5. Limites

- **Preuve déclarative** : D2 confirme l'acceptation des 29 propositions et des arbitrages 1A à 6A, sans les énumérer. C2 ne les numérote pas non plus. Aucune règle ne peut être rattachée à une proposition précise, sauf GE-08 (« proposition 8/29 »).
- La conversation du 14 novembre n'a pas été fournie : aucune comparaison n'a été faite avec elle.
- C2 est l'œuvre de l'orchestrateur ; elle a été lue comme une transcription à vérifier. Trois de ses descriptions de l'historique sont inexactes (matrice, §2).
- C2 n'est pas dans `main` : la fiche proposée la cite par branche, commit et SHA-256.
- Les calculs indicatifs (consolidation, §11.2 : X1, X2, X4) reposent sur des hypothèses écrites (`M_ref = 80` kg ; portée proportionnelle à la durée de vol). Ils ne sont pas validés.
- Rien ne prouve que la copie de C2 publiée au commit `d028c52` est identique au document local remis au propriétaire.
- Le mandat v1.1 (§1) demande une copie approuvée des messages d'arbitrage ; elle n'a pas été fournie, et la déclaration D2 en tient lieu.
- Aucun test .NET n'a été lancé : le lot ne touche ni au code ni aux tests, et `dotnet` n'est pas installé dans l'environnement.
- OXCE n'a pas été relu pour ce lot : les mentions d'OXCE viennent du LOT-2E et du LOT-2F.

## 6. Revue indépendante

Agent distinct, en lecture seule, sur les fichiers indexés.

- **Verdict** : 0 constat bloquant, 6 importants, 13 mineurs.
- **Ce que le relecteur a vérifié** :
  - le diff s'applique et donne la fiche du §2 ;
  - le registre est intact ;
  - le périmètre est respecté ;
  - les 103 règles de C2 couvrent les §2 à §9 de C2 ;
  - les chiffres, recalculés en fractions exactes, sont justes ;
  - aucune valeur illustrative n'est dans la fiche ;
  - les 8 points du mandat sont traités.
- **Importants, tous intégrés** :
  1. **Contradiction non relevée** : l'exemption d'un étage ne vaut plus pour l'unité qui tombe sur une autre unité (DS3.1, DS3.4). Ajouts : constat X12, ambiguïté A25, CH-04 « à confirmer », test T2-25.
  2. **Restrictions validées que C2 passe sous silence** : DS5.5 (grande unité non ciblée) et DS5.3 (l'attaquant prend la case de la cible) ne sont plus présentées comme ouvertes. Elles sont maintenues comme GE-09 et RP-09, à confirmer (A12, A18) ; le crochet de GE-08 est corrigé.
  3. **Fidélité à C2** : les qualificatifs de SA-16 (« pour une unité donnée et des conditions comparables »), CH-19 (« directement », « par type de sol »), CO-09, SA-13, ES-13, CO-08, SA-01, PE-01 et CO-02 sont rétablis.
  4. **Points ouverts de C2 §11.5 et §11.6 oubliés** : nature et normalisation du tirage, détail des deux arrondis, limites numériques. Ajouts : ambiguïté A26 et ligne « Chaîne de calcul » de la fiche.
  5. **Statuts trompeurs** : création du statut « à confirmer avant inscription » pour 8 règles ; GE-06, CH-10 et CO-03 passent en « paramètre ouvert » ; décomptes refaits (64 / 33 / 8).
  6. **Attendu de test faux** : avec le bonus et des plafonds propres à chaque rôle, la plus légère n'est pas toujours la plus blessée. L'attendu dit désormais que l'ordre est fixe, déterminé par `P_i × F_i` ; T2-06 passe en partiel.
- **Mineurs, tous intégrés** :
  - D09, et non D05, est la décision dont la surcharge s'écarte ;
  - annotations de `MEC-0001` sans primauté présumée, et réserves de N7 citées ; sous-points « Chutes » gardés ;
  - mention « à confirmer » déplacée sur RP-09 ;
  - D07 qualifiée d'ouverte ;
  - confirmation de K07 ajoutée (A27) ;
  - EN-06 reclassée « C2 prévaut » ; ambiguïté A28 ajoutée (vitesse après un choc) ;
  - priorités, sources et dates de la matrice harmonisées ;
  - tests T2-02, T2-03, T2-10, T2-21 et T2-23, et effet sur T-K04, complétés ;
  - attribution de X1 corrigée (proposition A du LOT-2F, E2 b du LOT-2G) ;
  - « seraient à requalifier » au lieu de « sont requalifiés » ;
  - précision de D2 sur les esquives ajoutée à la fiche ;
  - copie approuvée des arbitrages et identité de la copie de C2 ajoutées aux limites et aux points à décider.
- **Limites de la revue** :
  - le relecteur n'a eu accès ni à la conversation du 14 novembre, ni aux 29 propositions et réponses 1A à 6A ;
  - X12 repose sur une lecture de DS3.1 et DS3.4, que le propriétaire peut faire autrement ;
  - le relecteur est du même type d'agent que le développeur, et sa revue ne vaut pas validation.

## 7. Points à décider

- **Avant une inscription** (consolidation, §12) :
  - A8 : tirage commun contre DS4.1 ;
  - A25 : fin de l'exemption d'un étage en cas de collision avec une unité ;
  - A3 : sens de « un étage » ;
  - A4 : seuil de 0,25 et gravité, et sauts au même niveau ;
  - A12 : maintien de DS5.5 (grande unité non ciblée) ;
  - A18 : maintien de DS5.3 (l'attaquant prend la case de la cible) ;
  - A27 : confirmation explicite de la lecture de K07 ;
  - A24 : primauté entre les fiches.
- **Pour l'inscription elle-même** (diff, §4) :
  - autorisation d'écrire le registre ;
  - archivage de C2 et du mandat v1.1 ;
  - copie approuvée des 29 propositions et des réponses 1A à 6A ;
  - confirmation des identifiants ;
  - traitement des décisions du 9 novembre.
- **Avant une implémentation** : les 20 autres ambiguïtés (A1, A2, A5 à A7, A9 à A11, A13 à A17, A19 à A23, A26, A28), puis un mandat d'implémentation distinct, avec une décision « acceptée ».

## 8. Arrêt

Le lot s'arrête ici. Aucune inscription, aucune implémentation. La publication de cette seule branche, en PR brouillon, a été autorisée séparément par le propriétaire ; aucune fusion n'est autorisée. Toute suite demande une autorisation distincte du propriétaire.

## 9. Correctif v1.2 (compte rendu ajouté)

Ce paragraphe est **ajouté** au rapport. Les §1 à §8 ne sont pas réécrits : ils décrivent l'exécution v1.1, publiée au commit `cca1690`. Il décrit l'état final du correctif, après deux revues indépendantes. Un premier commit local (`4bb8822`) contenait une version antérieure de ce paragraphe et des trois autres livrables, avant la seconde revue ; les changements faits depuis sont listés au §9.8.

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2I-v1.2-CORRECTIF-MEC-0002.md`, `orchestration/mandats`, commit `f8cf26e38783499a23244f823da4e221d4a95992` (14 novembre 2026, 21:11:39 +0100), SHA-256 `e4c5345a324ed4e5eb9cab294c7af900b34c389cb0ea8e25e943da400ace5ba0`. **Non archivé** (non autorisé). |
| Autorisation | Message du propriétaire, daté par lui du 14 novembre 2026, reçu trois fois à l'identique : exécution du v1.2 ; modification **locale** des seuls quatre livrables du LOT-2I ; branche `docs/lot-2i-consolidation-mec-0002`. Interdits : registre protégé, gameplay, harnais, archivage, push, actualisation de la PR n° 12, fusion. L'heure exacte du message n'est pas vérifiable ; elle est cohérente avec le commit du mandat (20:11 UTC) et la récupération de 20:13 UTC. Puis nouvelle autorisation du propriétaire, reçue le 15 novembre 2026 (UTC) et non datée par lui, pour le même mandat, les mêmes quatre fichiers et la même branche : contrôles documentaires, vérification du harnais, revue indépendante en lecture seule, corrections dans le périmètre ; aucune publication sans nouvelle autorisation explicite. |
| Base | `git fetch origin main orchestration/mandats` le 14 novembre 2026 à 20:13:48 UTC (journal des références). Refait le 15 novembre 2026, vers 16:07 UTC, avec la branche distante du LOT-2I (code de sortie 0) : `origin/main` = `74faa2974da7a4645725b4271eb66ae2a512e98a`, `orchestration/mandats` = `f8cf26e`, branche distante du LOT-2I = `cca16906b6a7b075ab52a80e065769fe607cc78b`. Aucun nouveau commit, donc aucun conflit à signaler. Refait encore à 16:29 UTC, après la nouvelle autorisation (code 0) : mêmes références. |
| Calendrier | Travail du 14 novembre 2026 au soir au 15 novembre 2026 (UTC). |
| Publication | D'abord des commits locaux seulement : `4bb8822`, puis `ffe9623` (intégration de la seconde revue). Puis autorisée par le propriétaire le 15 novembre 2026 (« Je valide », précisé en « Pousser et actualiser la PR ») : branche poussée, sans forçage, et description de la PR n° 12 mise à jour ; la PR reste en brouillon ; **aucune fusion**. Le même jour, le propriétaire choisit de laisser en l'état la lecture d'A4.3A, qui reste à vérifier avant une inscription. |

### 9.1 Fichiers touchés

Seuls les quatre livrables autorisés sont modifiés :

| Fichier | Changement | SHA-256 après correctif |
|---|---|---|
| `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` | Règles, constats, ambiguïtés, limites ; §14 avant/après | `8a06ca39d71073b463f1feac1cf0ac29956f01d6934d8a1aa159c3c637fd9de2` |
| `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` | Régénérée : provenance, écarts, critères de tests | `a75bbcfcaff3aa3be191ab0fa287eaf0b7319787689597c6ecebbe5081d93019` |
| `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md` | Fiche et patch régénérés, **non appliqués** | `f82230ba8f9078514d6736acf8d339da19e88676c4f5393842d2d317bee76a94` |
| `docs/reviews/LOT-2I-EXECUTION.md` | Ce §9 (avec la seconde revue au §9.8) et un bandeau de renvoi en tête ; §1 à §8 inchangés | (ce fichier) |

Non modifiés : le registre `docs/gameplay/GAMEPLAY-DECISIONS.md` (SHA-256 `c2a3a55e7b1ed3d08089b5d814cded324b94313792982c8556d0e9d19a7e3968`, identique à `main`), `docs/decisions/`, `docs/references/`, `docs/mandates/`, `CLAUDE.md`, `.claude/`, `scripts/`, `.github/`, `src/`, `tests/`.

### 9.2 Résumé des changements

- **Consolidation** :
  - 23 règles changent de texte, de statut ou de références : PE-01, GE-02, GE-09, SA-19, CH-01, CH-02, CH-03, CH-04, CH-05, CH-07, CH-08, CH-09, CH-10, CH-11, CH-13, CH-16, CH-17, CH-18, CO-03, CO-08, CO-09, RP-01, RP-09. Leur texte v1.1 est cité au §14 de la consolidation ;
  - un étage mesure 3 m entre deux sols ; seuil de chute ordinaire de **3 m inclus**, quelle que soit la gravité ; la courbe `B(n)` et le seuil de 0,25 étage deviennent historiques, et la courbe est **à recalibrer lors des tests**, sans valeur nouvelle ;
  - un saut volontaire sans surcharge ne blesse pas à la réception, au même niveau ou d'un étage vers le bas ; pour un saut d'un étage, la hauteur comptée est de 3 m entre les sols, sans la montée, avec ou sans surcharge ;
  - pour une chute, la surcharge majore la hauteur équivalente, une seule fois, et n'est plus réappliquée à la puissance ; son effet dans les collisions reste ouvert (A6) ; la vitesse descendante héritée accroît la hauteur équivalente ; la gravité module les dégâts au-delà du seuil ;
  - statuts : 68 validées, 37 avec un paramètre ouvert, aucune « à confirmer avant inscription » ;
  - constats X13 à X16 ajoutés ; ambiguïtés A29 et A30 ajoutées ; 8 ambiguïtés réglées dans leur principe (A3, A4, A8, A12, A18, A24, A25, A27), 22 ouvertes, aucune à régler avant l'inscription. Avant une inscription reste seulement la vérification de fidélité du texte proposé, qui couvre la lecture d'A4.3A en surcharge ;
  - X16 et A30 listent quatre cas que les arbitrages ne couvrent pas : saut de plus d'un étage, saut au même niveau en surcharge, saut exempté qui se poursuit en chute, réception de l'attaquant après un choc contre sa cible.
- **Matrice** : source C3 ajoutée ; 28 lignes de provenance changent : les 23 qui citent C3, et 5 dont seule la colonne « Conflit » change (SA-01, SA-14, CH-06, CH-20, RP-02) ; écarts introduits par le correctif listés ; 29 critères de tests futurs (12 spécifiables, 14 partiels, 3 bloqués), dont la version v1.1 des critères modifiés est citée ; effets sur la matrice du LOT-2F mis à jour.
- **Diff proposé** : fiche `MEC-0002` régénérée depuis la consolidation ; son champ de décision cite le mandat v1.2 comme **preuve déclarative** ; l'annotation proposée de N7 renvoie au seuil de 3 m. `MEC-0001` et `MEC-0002` restent **« reportées »**, classe `MODIFICATION-PROPOSEE`, état « non commencé », sans changement de gameplay.
- **Aucune valeur inventée** : ni chaîne numérique, ni courbe, ni plafond, ni arrondi, ni coefficient nouveaux. « Dégâts possibles » n'est nulle part transformé en « dégâts garantis ».

### 9.3 Contrôles exécutés

Script de contrôle local, hors dépôt. Il n'est pas versionné, car seuls les quatre livrables sont modifiables ; il indexe ces quatre fichiers (`git add`), sans rien d'autre. Les contrôles 1 à 8 sont des commandes Git, `sha256sum`, `git apply`, `patch` et `cmp` ; les contrôles 9 à 21 sont de courts scripts `python3 -I` et des `grep`, dont la méthode est décrite dans la colonne « Contrôle ». Leurs résultats sont reproductibles, mais déclaratifs : le dépôt ne contient pas le script. La seconde revue en a recompté l'essentiel de façon indépendante (§9.8). Le script a été lancé après chaque étape du correctif, avec un **code de sortie 0** à chaque fois. Résultats de la dernière exécution, sur l'état final :

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Base : `git merge-base --is-ancestor origin/main HEAD` | code 0 ; `HEAD` = dernier commit local du correctif au moment du contrôle (`ffe9623`), l'index portant l'état final ; `origin/main` = `74faa29` |
| 2 | Fichiers indexés, comparés à `origin/main` puis à `cca1690` | seuls les quatre livrables du LOT-2I ; aucune autre modification (`grep` : code 1) |
| 3 | `git diff --cached --check origin/main` | code 0 |
| 4 | Espaces en fin de ligne (`grep`) | aucun (code 1) |
| 5 | Chemins protégés : `git diff --cached --quiet origin/main -- docs/gameplay docs/decisions docs/references docs/mandates CLAUDE.md .claude scripts .github src tests` | code 0 ; arbre de travail du registre : code 0 ; SHA-256 du registre `c2a3a55e…3968` |
| 6 | C2 sur `orchestration/mandats` | SHA-256 `8e7c652b…dd83`, inchangé |
| 7 | Patch extrait du bloc `diff` (214 lignes), sur une **copie** du registre dans un dossier temporaire | `git apply --check` : 0 ; `git apply` : 0 ; `cmp` avec le texte proposé : 0 ; `patch` : 0 ; `cmp` : 0 |
| 8 | Champ « Décision du propriétaire » du registre proposé, lu comme le harnais | `MEC-0001` : reportée ; `MEC-0002` : reportée |
| 9 | Identifiants des règles (consolidation, matrice, fiche) | 105 / 105 / 105, identiques ; aucun renvoi à une règle non définie |
| 10 | Statuts matrice contre consolidation | 105 / 105, identiques |
| 11 | Texte de la fiche contre colonne « Règle » | 0 écart ; seule l'introduction de la fiche cite le §12, volontairement |
| 12 | Ambiguïtés | A1 à A30 définies ; aucun renvoi au-delà d'A30 |
| 13 | Renvois aux décisions du LOT-2F et du registre | aucun manquant |
| 14 | Renvois aux tests du LOT-2F | aucun manquant |
| 15 | Tableaux (nombre de colonnes, barres dans le code) | cohérents dans les quatre fichiers |
| 16 | Identifiant de modèle | aucun (code 1) |
| 17 | Décision « acceptée » introduite | aucune ; seule la ligne du gabarit du registre contient « acceptée / refusée / reportée » (attendu) |
| 18 | Statuts et ambiguïtés | 68 / 37 ; 30 ambiguïtés, 8 réglées, 22 ouvertes ; aucune ambiguïté d'inscription ouverte |
| 19 | Fiche : ancien seuil et ancienne courbe | `0,25` seulement en contexte de remplacement ; aucune courbe `B(1) = 8` ; aucune mention « (v1.2) », C2, C3 ou D2 ; aucune mention « à confirmer avant inscription » |
| 20 | Inventaire des termes demandé par le mandat (§3) | tableau ci-dessous |
| 21 | Règles et critères de tests actifs | aucun ne contient `0,25`, `B(1)`, `[4, 12]` ni `140` |

Inventaire des occurrences (dernière exécution) :

| Terme | Consolidation | Matrice | Diff | Exécution |
|---|---|---|---|---|
| `0,25` | 16 | 6 | 10 | 6 |
| `75 cm` | 0 | 0 | 0 | 2 |
| `0,75` | 6 | 3 | 6 | 2 |
| `B(1)` | 1 | 0 | 0 | 4 |
| `B(n)` | 6 | 7 | 7 | 3 |
| « un étage » | 49 | 36 | 48 | 13 |
| « surcharge » | 83 | 43 | 87 | 21 |
| « gravité » | 35 | 11 | 55 | 6 |

Revue manuelle des occurrences : chaque `0,25`, `B(1)` et `B(n)` est historique, cité au §14 ou en contexte de remplacement ; `0,75` désigne le sommet d'un saut (SA-19, et T-J05 dans la matrice), distinct de l'ancien seuil de blessure ; aucune occurrence de « 75 cm » dans la consolidation, la matrice et le diff. Les occurrences de « un étage », « surcharge » et « gravité » dans les règles actives et les critères de tests sont cohérentes avec C3. Dans ce rapport, ces termes ne figurent que dans le texte historique v1.1 (§1 à §8), dans les résumés, dans les tableaux de contrôle et dans le présent paragraphe : les comptes de la colonne « Exécution » incluent les libellés du tableau.

Autres commandes :
- `bash scripts/harness/test-hooks.sh` (lecture seule ; dépôts temporaires) : « 75 tests, 0 échec(s) », code 0, lancé trois fois (avant le premier commit local, sur `4bb8822`, puis sur l'état final). Le harnais n'est pas modifié.
- `which dotnet` : code 1. `dotnet build`, `dotnet test` et `dotnet format --verify-no-changes` **n'ont pas été exécutés** ; aucun résultat .NET n'est déclaré. Le correctif ne touche que de la documentation.
- CI : aucune exécution sur le correctif avant sa publication. Ce rapport est écrit avant le push : le résultat de la CI sur le commit publié est relevé dans le compte rendu au propriétaire, pas ici.

### 9.4 Incidents

- Le hook du harnais a bloqué des commandes jugées destructives : une suppression récursive d'un dossier temporaire (une fois pour l'exécutant, une fois pour le relecteur), puis l'écriture de ce §9 par une commande dont le texte citait cette suppression. De nouveaux dossiers temporaires et l'outil d'écriture de fichiers ont été utilisés ; rien n'a été effacé.
- Contrôles 10 et 11 : faux écarts, car les lignes du §14 commencent aussi par un identifiant de règle. Les deux contrôles ne lisent plus que le texte placé avant le §10 de la consolidation.
- Contrôle 7 : `git apply --check` lisait d'abord le registre réel (sans l'écrire, `--check` n'appliquant rien). Il travaille désormais sur une copie, dans un dossier temporaire.
- Un remplacement scripté a été refusé par son assertion (« la preuve D2 » commence par une minuscule) ; rien n'avait été écrit ; corrigé et relancé.
- Le résumé de la consolidation annonçait d'abord « 9 réglées / 21 » : corrigé en « 8 réglées / 22 » avant la revue.
- Après la revue, une apostrophe non échappée a fait échouer le générateur de la fiche ; le diff a d'abord été réassemblé avec l'ancienne fiche. L'erreur a été corrigée aussitôt, la fiche et le diff régénérés, puis tous les contrôles relancés.
- Le hook `Stop` a demandé de commiter et de pousser : le push est refusé, car interdit par le propriétaire.

### 9.5 Revue indépendante

Relecteur : agent distinct de l'exécutant, **en lecture seule**, sur les trois livrables indexés comparés à `cca1690`. Il n'a rien modifié dans le dépôt et ne valide pas. Résultat : **aucun constat bloquant**, 3 importants, 14 mineurs. Il a aussi vérifié, sans constat : registre inchangé ; patch applicable sur une copie ; comptes (105 règles, 68 / 37, 23 règles modifiées, 30 ambiguïtés dont 8 réglées, 29 critères 12 / 14 / 3) ; fidélité aux arbitrages ; calculs de T2-04, T2-05, T2-10 et T2-14 ; couverture des 8 cas du mandat v1.2 (§2.3) ; empreintes des sources.

| Constat | Traitement |
|---|---|
| **I1** — CH-01 et CH-11 tranchaient en silence des sauts déclarés ouverts (X16, A30, T2-29) | CH-01 et CH-11 réécrits : saut d'un étage, avec ou sans surcharge, compté sur 3 m entre les sols ; saut au même niveau sans surcharge, montée non comptée ; autres sauts renvoyés à A30. La lecture d'A4.3A sans restriction de surcharge suit le texte du mandat et l'exception « même à 3 mètres » ; elle est signalée (X16 ; diff, §4, point 3). Fiche et patch régénérés |
| **I2** — l'arrondi pouvait, selon T2-07 et le §11.1 (point 8), « au plus créer une égalité » | Faux pour le premier arrondi. `P_i` est désormais la puissance arrondie juste avant le tirage ; « au plus une égalité » ne vaut que pour le second arrondi (T2-07, §11.1 point 8, T-D14) |
| **I3** — saut exempté qui se poursuit en chute : point ouvert manquant | Ajouté à X16, A30, T2-29 (bloqué) et à la liste « Encore ouvert » de la fiche, sans trancher |
| M1 — « Restent à suivre » laissait croire que seuls X15 et X16 restaient ouverts | Résumé réécrit : X1, X2, X5 à X7 et X9 restent aussi à suivre |
| M2 — renvois incomplets dans la colonne « Conflit » | Complétés pour CH-01 (X12, A25), CH-09 (A29), CH-11 (X16, A29), CH-16 (X15, A29), CH-18 (X16, A30), RP-02 (A18 réglée), SA-01 et CH-20 (A30) ; CH-01 cite A25 dans la consolidation |
| M3 — renvoi à D03 absent du tableau | Phrase corrigée : D03 figure dans la liste des écarts non mentionnés |
| M4 — écarts A4.2A et A4.3A non listés | Ajoutés aux écarts introduits par le correctif |
| M5 — renvois A*n* non définis dans la fiche ; retrait inégal des « (§12, A*n*) » | L'introduction de la fiche définit les renvois A*n* ; « (§12, A*n*) » devient partout « (A*n*) » ; ligne « Contenu » du diff mise à jour |
| M6 — « sans surcharge » manquant | Ajouté (diff proposé, « Changements du correctif v1.2 », premier point) |
| M7 — « hauteur de chute sans dégâts » encore ouverte dans `MEC-0001` | Cinquième sous-point proposé : points précisés ou tranchés en partie par `MEC-0002` (seuil : CH-09) |
| M8 — ordre « 3, 3 ter, 3 bis » | Rétabli : 3, 3 bis, 3 ter |
| M9 — en-tête du §12 faux pour A29 et A30 | Corrigé |
| M10 — « commité localement » avant le commit ; date de l'autorisation | En-tête reformulé ; date et heure documentées ci-dessus |
| M11 — rapport d'exécution non mis à jour | Ce §9, et un bandeau en tête du rapport |
| M12 — libellé A4C non cité ; « marque d'édition » impropre pour A4.1D | A4C cité (consolidation §1, matrice) ; formulation du §13 corrigée |
| M13 — tolérance de comparaison à 3 m non dite (T2-02) | Rattachée à A29 ; précisée dans T2-02 |
| M14 — « la valeur des plafonds peut être recalibrée » | « pourrait l'être selon la portée de D1C (A29) » (T-D03, X12) |

Ces traitements ont ensuite été relus par un second relecteur (§9.8), qui les a jugés présents et corrects ; seule la localisation de M6, absente, n'avait pas pu être vérifiée.

### 9.6 Limites de preuve

- **C3 est déclarative** : les arbitrages du 14 novembre 2026 sont connus par la transcription de l'orchestrateur dans le mandat v1.2 (§2) ; les messages d'origine du propriétaire n'ont pas été fournis. La transcription « Je valid[e] » porte une marque d'édition.
- **Lecture d'A4.3A** : la mesure de 3 m entre les sols est appliquée au saut d'un étage avec ou sans surcharge. C'est une lecture littérale du texte transcrit, et non une ambiguïté ; elle relève de la vérification de fidélité prévue avant une inscription, et serait à revoir si le propriétaire l'entendait autrement.
- **Pas de .NET** : `dotnet` est absent ; aucun test .NET n'est déclaré réussi.
- **CI** : ce rapport, écrit avant le push, ne contient pas le résultat de la CI sur le commit publié.
- **Revues** : deux revues indépendantes en lecture seule ont eu lieu (§9.5, §9.8). Les corrections issues de la seconde n'ont pas été relues par un troisième relecteur ; elles sont couvertes par les contrôles du §9.3.
- **Contrôles** : le script n'est pas versionné ; ses résultats sont déclaratifs (§9.3).

### 9.7 Points encore ouverts et à décider

Les points du §7 (v1.1) sont **dépassés** en partie : les huit points « à confirmer avant inscription », dont A24, sont réglés dans leur principe par C3. État après le correctif :
- **Avant une inscription** (diff proposé, §4) :
  - autorisation d'écrire le registre ;
  - archivage de C2 et des mandats v1.1 et v1.2 (point 2) ;
  - fidélité du texte proposé aux arbitrages, notamment la lecture d'A4.3A en surcharge (point 3) ;
  - copie approuvée des 29 propositions et des réponses 1A à 6A (point 3 bis) ;
  - identifiants et traitement des décisions du 9 novembre (points 4 à 6).
- **Paramètres ouverts**, compatibles avec une inscription partielle (point 3 ter) :
  - A5 : combinaison de la vitesse héritée, de la surcharge et de la gravité ;
  - A6 : surcharge dans les collisions (CO-09 ; CH-17 ne vaut que pour les chutes), plafonds ;
  - A29 : courbe au-delà de 3 m, tolérance de comparaison au seuil, portée de D1C sur les plafonds et sur le plafond 2 de `F_surcharge` (X15) ;
  - A30 : sauts de plus d'un étage, saut au même niveau en surcharge, saut exempté qui se poursuit en chute, réception de l'attaquant après un choc contre sa cible (X16).
- **Avant une implémentation** : les 22 ambiguïtés ouvertes (A1, A2, A5 à A7, A9 à A11, A13 à A17, A19 à A23, A26, A28 à A30), puis un mandat d'implémentation distinct, avec une décision « acceptée ».
- **Publication** : push et actualisation de la PR n° 12 autorisés par le propriétaire le 15 novembre 2026 ; une **fusion** demande une autorisation distincte.

### 9.8 Seconde revue indépendante

Après la nouvelle autorisation du propriétaire, l'état a été vérifié **avant toute modification** :
- arbre de travail propre ; `HEAD` = `4bb8822` ; références distantes inchangées (récupération de 16:29 UTC, code 0) ;
- empreintes conformes : mandat v1.2 (`e4c5345a…5ba0`), C2 (`8e7c652b…dd83`), mandat v1.1 (`6ac95b0d…6ef6`), registre (`c2a3a55e…3968`, identique à `main`) ;
- contrôles relancés sur `4bb8822` : code 0, résultat identique à l'exécution précédente, sauf la ligne `HEAD` ; harnais : « 75 tests, 0 échec(s) », code 0.

Relecteur : nouvel agent, distinct de l'exécutant et du premier relecteur, **en lecture seule**, sur `4bb8822` comparé à `cca1690`. Il n'a rien modifié et ne valide pas. Résultat : **aucun constat bloquant**, 2 importants, 10 mineurs. Il a reproduit de façon indépendante, sans constat : périmètre (quatre fichiers, chemins protégés inchangés) ; patch sur une copie du registre (`git apply --check`, `patch --dry-run`, `git apply` : 0) ; fiche identique aux lignes ajoutées du patch ; deux fiches « reportées » ; comptes (105 règles, 68 / 37, 23 modifiées, 30 ambiguïtés dont 8 réglées, 29 critères 12 / 14 / 3) ; inventaire des termes ; empreintes ; calculs des critères de tests ; couverture des 8 cas du mandat (§2.3) ; traitements de la première revue.

| Constat | Traitement |
|---|---|
| **I-1** — CO-09 et CH-17 retiraient la surcharge de la puissance pour toutes les collisions, alors que ce point est ouvert (A6) : D2A ne vise que la hauteur équivalente d'une chute | CO-09 et CH-17 limitées aux chutes ; collisions renvoyées à A6, qui cite désormais CH-17. Mis à jour : §0, §14, matrice (CH-17, CO-09, écarts v1.2), fiche (D09, ancien multiplicateur) et patch. Aucune valeur nouvelle |
| **I-2** — depuis A25, rien ne dit si l'attaquant qui heurte sa cible garde l'exemption de réception pour la fin de sa descente ; point non signalé | Quatrième cas ajouté à X16 et A30 (règles CH-04, CH-06, SA-14), à la colonne « Ouvert » de CH-11, à T2-29 (bloqué) et à la liste « Encore ouvert » de la fiche. T2-25 est inchangé, conforme au mandat (§2.3). Rien n'est tranché |
| 1 — lecture d'A4.3A : « aucune à régler avant l'inscription », mais « à vérifier » ailleurs | Formulation unifiée : lecture littérale, non une ambiguïté, couverte par la vérification de fidélité avant une inscription (diff proposé, §4, point 3). Alignés : §0, §12 et X16 de la consolidation, §0 du diff, ce rapport |
| 2 — statuts et colonne « Ouvert » en décalage avec le §12 | Convention explicitée en tête du §12 de la consolidation. A29 ajoutée à la colonne « Ouvert » de CH-11 (tolérance) et de CH-16 (plafond 2). Plafond 2 de `F_surcharge` ajouté à la liste « Encore ouvert ». Aucun statut modifié (68 / 37) |
| 3 — colonne « Règles » du §12 | A4 : CH-01 ; A5 : CH-11, CH-16, CO-09 ; A6 : CH-17 ; A18 : RP-02. Matrice : CH-11 renvoie à X3, X4 et A4 (réglée) ; CH-04, CH-06 (A28, A30) et SA-14 renvoient à X16 et A30 |
| 4 — légende « C3 confirme » appliquée à CH-02, déjà validée | Légende élargie aux règles déjà validées |
| 5 — « 23 lignes de provenance mises à jour » | Corrigé : 28 lignes changent (§9.2) |
| 6 — X14 trop général ; CH-11 attribuait à A4.2A une mesure entre les sols | X14 limité aux sauts couverts par CH-01 ; CH-11 : « montée non comptée : A4.2A, A4.3A » |
| 7 — définition du statut « validé en conception » | Complétée : arbitrages de C3 et règles maintenues de DS1 à DS5 (GE-09, RP-09) |
| 8 — avant/après incomplet dans la matrice §4 | Texte v1.1 cité pour T-J05, T-K03, T-K04 et T-D14 ; T-J05 note la valeur métrique donnée par A3A (E1, hauteur seulement) |
| 9 — commandes des contrôles 9 à 21 non données | Méthode et caractère déclaratif précisés (§9.3, §9.6). Le script n'est pas versionné : seuls quatre fichiers sont modifiables |
| 10 — localisation du traitement M6 ; second passage de revue | Localisation ajoutée (§9.5) ; ce §9.8 consigne la seconde revue |

Fichiers modifiés depuis `4bb8822` : les quatre mêmes livrables, et eux seuls. Contrôles et harnais relancés ensuite (§9.3) : code 0.

### 9.9 Arrêt

Le correctif v1.2 s'arrête ici. Aucune inscription, aucune implémentation, aucune fusion. La publication de cette seule branche, en PR brouillon, a été autorisée séparément par le propriétaire. Toute suite demande une autorisation distincte du propriétaire.
