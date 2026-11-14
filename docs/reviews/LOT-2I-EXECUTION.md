# LOT-2I — Rapport d'exécution : consolidation de `MEC-0002` et diff proposé du registre

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2I-v1.1.md`, `orchestration/mandats`, commit `58d3ebc`, SHA-256 `6ac95b0d…6ef6`. Non archivé (non autorisé). |
| Autorisation | Propriétaire, 14 novembre 2026 : exécution documentaire du mandat v1.1 ; branche locale `docs/lot-2i-consolidation-mec-0002` depuis `origin/main` ; archivage du mandat et modification de `docs/mandates/README.md` **non autorisés** ; aucun push, aucune PR, aucune fusion, aucune modification du registre protégé, aucune implémentation. |
| Branche | `docs/lot-2i-consolidation-mec-0002`, créée depuis `origin/main` = `74faa2974da7a4645725b4271eb66ae2a512e98a`, après `git fetch origin main`. |
| Publication | D'abord un commit local seulement (`8b84f0c`). Puis autorisée par le propriétaire le 14 novembre 2026 (« Je valide », précisé en « Publier en PR brouillon ») : branche poussée et PR en brouillon vers `main`, **sans fusion**. |
| Implémentation | **Aucune autorisation d'implémentation** n'existe ni ne découle de ce lot. |

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
