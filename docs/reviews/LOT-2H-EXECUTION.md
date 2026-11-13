# LOT-2H — Rapport d'exécution : préparation de l'inscription des principes DS1 à DS5

| | |
|---|---|
| Mandat | `BASTION-MANDAT-LOT-2H-PREPARATION-INSCRIPTION-v1.0.md` (SHA-256 `5dff21c4…f6e9`), copié depuis `orchestration/mandats`, commit `24ca756`. |
| Autorisation | Propriétaire, 13 novembre 2026 : exécution du mandat, branche locale depuis `main`, proposition documentaire sans modification du registre ; « Aucun push, aucune PR ni fusion sans autorisation distincte. Arrête-toi après les contrôles et la revue indépendante. » |
| Branche | `docs/lot-2h-preparation-inscription-mec-0001`, créée depuis `origin/main` = `72908389ea99f7267f7f723c57b488f640bfe441`, après `git fetch origin main`. |
| Publication | **Aucune** : commit local seulement, sans push ni PR. |

## 1. Résumé

- Les 25 principes acceptés de la consolidation DS1 à DS5 (DS1.1 à DS5.7) sont transcrits dans un texte proposé pour la fiche `MEC-0001`, avec le diff exact du registre (`LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md`).
- Chaque principe a une source, les règles antérieures touchées, son statut au registre et un statut de traçabilité (`LOT-2H-TRACABILITE-ECARTS.md`). Les huit contrôles de contradiction du mandat (§3 B) sont faits.
- 15 sujets restent à arbitrer avant une inscription exhaustive ou une implémentation (proposition, §5). Aucun des 13 points bloquants du LOT-2F n'est entièrement résolu.
- **Le registre n'est pas modifié** ; `MEC-0001` reste « reportée ».

## 2. Sources lues

| Source | Emplacement | Empreinte ou commit |
|---|---|---|
| `CLAUDE.md` | `main` | `7290838` |
| Mandat LOT-2H | `orchestration/mandats` | commit `24ca756`, SHA-256 `5dff21c4…f6e9` |
| Consolidation DS1 à DS5 | `orchestration/mandats` | commit `197d8b9` (inchangée au commit `24ca756`), SHA-256 `dee88998…f335f` |
| Registre `docs/gameplay/GAMEPLAY-DECISIONS.md` | `main` | SHA-256 `c2a3a55e7b1ed3d08089b5d814cded324b94313792982c8556d0e9d19a7e3968` ; lu, non modifié |
| Spécification et matrice du LOT-2F | `main` | `7290838` |
| Dossier et impacts du LOT-2G | branche `docs/lot-2g-mec-0001-arbitrages` (PR n° 10, non fusionnée) | tête `2a14a501376a84a1bb2f41f5d135db56e15ee10e` ; lue sans fusion |
| `docs/references/OXCE-BASELINE.md` | `main` | consulté pour la décision D4 (aucune reprise de code, de données ni d'assets), citée par la traçabilité. Aucune affirmation nouvelle sur OXCE : la traçabilité rappelle seulement deux comportements déjà lus au commit `441cae1` (LOT-2E C7 ; `src/Mod/RuleDamageType.cpp:37` et `:139-142`, cités par le LOT-2G) |

## 3. Fichiers du lot

| Fichier | Nature |
|---|---|
| `docs/mandates/BASTION-MANDAT-LOT-2H-PREPARATION-INSCRIPTION-v1.0.md` | copie exacte du mandat |
| `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` | copie exacte de la consolidation |
| `docs/mandates/README.md` | deux lignes d'index ajoutées en fin de tableau ; aucune ligne existante modifiée |
| `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md` | texte et diff proposés, « PROPOSITION DOCUMENTAIRE — NON INSCRITE » |
| `docs/reviews/LOT-2H-TRACABILITE-ECARTS.md` | matrice de traçabilité, contrôles B1 à B8, effet sur les 13 points |
| `docs/reviews/LOT-2H-EXECUTION.md` | ce rapport |

## 4. Contrôles

Exécutés le 13 novembre 2026, après intégration de la revue, sur les fichiers indexés, avant le commit.

- **Base** : `git fetch origin main orchestration/mandats` ; `git rev-parse HEAD origin/main` donne `72908389…` pour les deux ; `git merge-base --is-ancestor origin/main HEAD` : code 0.
- **Périmètre** : `git diff --cached --name-status origin/main` liste exactement les 6 fichiers du mandat (§4). `git diff --cached --numstat` sur l'index : 2 lignes ajoutées, 0 supprimée.
- **Archives** :
  - `cmp` avec `git show origin/orchestration/mandats:docs/mandates/<fichier>` : code 0 pour les deux ;
  - empreintes Git identiques ;
  - SHA-256 `5dff21c4e0040d81ea2bb14a7142ffcc87a077d287de967978349dc130d7f6e9` (mandat) et `dee88998c561247a5941fe2d04854a95b74e863d31b837b86f3de1acad9f335f` (consolidation) ;
  - la consolidation est identique aux commits `197d8b9` et `24ca756` (`git diff --quiet` : code 0).
- **Espaces** :
  - `git diff --cached --check origin/main` : code 2. Il signale seulement les 10 lignes d'origine des deux archives qui finissent par des espaces (5 par fichier), conservées telles quelles ;
  - hors archives : aucune sortie, code 0 ;
  - `grep -nE ' +$'` sur les trois rapports et l'index : aucune ligne, code 1.
- **Fichiers protégés** : `git diff --cached --quiet origin/main -- docs/gameplay docs/decisions docs/references CLAUDE.md .claude scripts .github src tests`, plus la spécification et la matrice du LOT-2F : code 0. SHA-256 du registre : `c2a3a55e…3968`, identique à `main`.
- **Diff proposé** :
  - bloc extrait de la proposition (§4) : `git apply --check` sur le registre de `main`, code 0 ;
  - `patch -o` sur une copie hors dépôt : code 0, résultat identique au registre proposé (SHA-256 `f818ce52…24e`) ;
  - le texte rendu au §2 de la proposition est identique au bloc que le diff insère ;
  - dans le registre proposé, le champ « Décision du propriétaire » commence toujours par « reportée ». La logique de `scripts/harness/check-simulation-trace.sh` continuerait donc de refuser toute déclaration de code pour `MEC-0001`.
- **Aucune formule optionnelle du LOT-2G** dans les lignes ajoutées au registre : recherche de `R(γ`, `β`, `2/7`, `f_sol`, `3,2`, `v_ref`, `c_s`, « sols franchis », `n = 0`, `B(n)`, `0,236` et `ρ`, sans résultat (code 1).
- **Complétude** :
  - 25 principes dans la source (4 + 4 + 5 + 5 + 7), tous présents dans le texte proposé et dans la matrice (25 lignes) ;
  - 5 groupes « à définir », 5 écarts ;
  - les 8 contrôles B1 à B8 et les 8 sujets du mandat §3 C sont couverts (proposition, §5 : 15 lignes).
- **Renvois** : chaque règle P, J, K, D, I, H, M et chaque point E cités existent dans la spécification du LOT-2F ; chaque S, Z et N cité existe au registre. Seules exceptions apparentes : P14 (proposition du LOT-2B citée dans le texte même du registre) et N12 à N14 (écrites « N12 à N14 » au registre).
- **Tableaux** : nombre de colonnes cohérent dans les trois rapports et l'index.
- **Harnais** : `bash scripts/harness/test-hooks.sh` : 75 tests, 0 échec, code 0.
- **Aucun fichier sous `src/`** : contrôle de traçabilité de la simulation sans objet.
- **.NET** : non lancé, car `dotnet` est absent de l'environnement et le lot ne touche ni au code ni aux tests.
- Aucun identifiant de modèle dans les fichiers du lot.

## 5. Limites

- La consolidation est une transcription des réponses du propriétaire. La conversation elle-même n'a pas été fournie : aucune comparaison avec elle n'a été faite. Le texte proposé suit la consolidation, qui fait foi.
- Les décisions du 9 novembre (LOT-2F) et le correctif E14, E18, E23 ne sont pas au registre. Le texte proposé y renvoie sans les inscrire.
- Le diff proposé vaut pour le registre de `main` au commit `7290838`. Il serait à régénérer si le registre changeait.
- Les chemins du LOT-2G cités dans le texte proposé n'existeront sur `main` qu'après la fusion de la PR n° 10.
- **Index des mandats** : la PR n° 10 ajoute aussi des lignes à la fin du tableau de `docs/mandates/README.md`, et une ligne de légende. Fusionner les deux branches demandera de garder les deux ajouts : conflit simple, mais à résoudre à la main. La ligne de légende « copie de branche » de la PR n° 10 n'existe pas sur `main` : les deux nouvelles lignes décrivent donc leur provenance en entier.
- Aucun test .NET n'a été lancé : le lot ne touche ni au code ni aux tests, et `dotnet` n'est pas installé dans l'environnement.

## 6. Revue indépendante

Agent distinct, en lecture seule, sur les fichiers indexés.

- **Verdict** : 0 constat bloquant, 2 importants, 12 mineurs. Le relecteur a vérifié :
  - le registre n'est pas modifié ;
  - le diff s'applique (`git apply --check`, `patch`) et le texte du §2 lui est identique ;
  - aucune formule optionnelle du LOT-2G n'est dans le texte proposé pour le registre ;
  - « reportée », la classe, l'état et le périmètre sont inchangés ;
  - les 25 principes ont été comparés un par un à la consolidation.
- **Importants, intégrés** :
  1. dans la traçabilité, des propositions du LOT-2G étaient présentées en bloc comme « reprises » alors que la consolidation n'en garde que le principe. Le tableau du §4 qualifie désormais chaque reprise (« en principe seulement », « en partie », « pour le saut offensif seulement »), et la liste « non reprises » est complétée. B4 ne présume plus que l'esquive et les chutes comptent les étages de la même façon ;
  2. la liste des calculs et attendus du LOT-2G qui supposent une vitesse de départ indépendante de la masse est complétée (T-J09, T-J10, T-D09, T-D10, tableau de requalification de T-J02, T-J03 et T-J11, contact latéral) et alignée avec la matrice ; T-G04 en est retiré, car il ne dépend pas de cette vitesse.
- **Mineurs, intégrés** :
  - texte proposé :
    - DS3.3 garde « les dégâts précis restent à calculer » ;
    - DS4.4 dit qu'un type « impact » est créé, sans fixer son champ d'application ;
    - DS3.2, DS3.4, DS4.3 et DS1.3 sont resserrés sur la source ;
  - réserve sur DS5.3 ajoutée au bandeau et au champ « Décision du propriétaire » ;
  - liste « Encore ouvert » complétée : moins d'un étage au sol, unités de la constante, algorithme géométrique, interruptions (DS5.1) ;
  - lecture rapide sans surestimation (cible, effet des masses) ;
  - ligne 14 du §5 corrigée : N7 est inscrite [À vérifier], l'annotation n'est qu'une proposition ;
  - classement des propositions du LOT-2G corrigé : DS5.3 correspond à l'alternative C de E9 ; DS5.4 rejoint E9 h ;
  - affirmations sur OXCE précisées : méthode 2 non par défaut ; LOT-2E C7 ; commit figé cité ;
  - commits de la consolidation harmonisés (`197d8b9`, inchangée au `24ca756`) ;
  - matrice complétée : N7 pour DS3.3 et DS3.4, interruptions pour DS5.1, P02 dans B2, description de la source F ;
  - E5 classé « partiellement tranché ».
- **Limites de la revue** :
  - le relecteur n'a eu accès ni à la conversation du propriétaire ni au texte de l'autorisation ;
  - il n'a relu dans OXCE que `RuleDamageType.cpp` ;
  - il est du même type d'agent que le développeur, et sa revue ne vaut pas validation.

## 7. Arrêt

Le lot s'arrête ici. Aucune inscription au registre, aucune implémentation, aucune publication. Une publication de la branche demanderait une autorisation distincte, limitée à cette branche.
