# LOT-0B — Rapport de clôture

**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-0B-CLOTURE-v1.0.md` (SHA-256 `86b878ea…627d`) · **Exécutant :** Claude Code · **Date :** 8 nov. 2026
**Branche :** `chore/lot-0b-harnais` · **Base :** `main`

## 1. Corrections effectuées

| # | Fichier | Changement | Commit |
|---|---|---|---|
| NC-1 | `docs/gameplay/GAMEPLAY-DECISIONS.md` | Gabarit `G-NNN` remplacé par une fiche `MEC-NNNN` avec les champs du §3.1 de la v0.2 : système, description, classe (`OXCE-REFERENCE`, `MODIFICATION-PROPOSEE`, `MODIFICATION-VALIDEE`, `A-VERIFIER`), référence et preuves, changement demandé, décision du propriétaire (preuve, date), périmètre autorisé et éléments exclus, tests de référence et de modification, état d'implémentation séparé. **Aucune fiche créée** : registre vide. | `daf3406` |
| NC-2 | `CLAUDE.md` | Ajouts : rôles « relecteur indépendant » et « contrôles automatiques » ; une idée de conversation n'est pas une décision ; interdiction de modifier l'équilibrage sans accord ; interdiction d'affirmer une fidélité à OXCE sans référence vérifiable et tests. Toutes les règles existantes sont conservées. | `daf3406` |
| NC-3 | `scripts/harness/stop-report-check.sh` | Le rappel demande d'indiquer dans le rapport les contrôles non exécutés. Simple message, sans nouveau mécanisme. Tests inchangés (la décision du hook est la même). | `daf3406` |

**Précision sur NC-2.** La première règle « Gameplay » de `CLAUDE.md` renvoyait à un statut « Validée » qui n'existe plus dans le nouveau registre. Elle est reformulée à l'identique sur le fond : il faut une fiche portant une décision du propriétaire « acceptée », explicite et datée, et `MODIFICATION-VALIDEE` n'autorise que son périmètre.

**Archivage** (commit `ebda48e`) : copies à l'identique dans `docs/mandates/`, SHA-256 vérifiés après copie :

| Document | SHA-256 | Attendu par le mandat |
|---|---|---|
| `BASTION-HARNAIS-LOT-0A-v0.2.md` | `d81a1c2e77414fef25d7c7ef29b8f13820e82b09028c33dbba25bf919030b001` | identique |
| `BASTION-LOT-0B-RETOUR-ORCHESTRATEUR.md` | `98ad142f4814d00c063fde78f9786be90b8bbbeff1a3a9c095550ae807973223` | identique |
| `BASTION-MANDAT-LOT-0B-CLOTURE-v1.0.md` | `86b878eabaf0d6fb6db621596cacf58d70f8a52f47b6d1e7e58ded437f54627d` | (non fourni) |

Le mot « PROPOSÉ » reste dans la spécification. `docs/mandates/README.md` indique séparément sa validation du 8 novembre 2026.

## 2. Contrôles locaux

SDK .NET 10.0.114 local (bac à sable), commit `ebda48e`.

| Commande | Résultat | Code |
|---|---|---|
| `dotnet restore` | projets à jour | 0 |
| `dotnet build --no-restore --configuration Release` | 0 avertissement, 0 erreur | 0 |
| `dotnet format --verify-no-changes --no-restore` | aucune sortie | 0 |
| `dotnet test --no-build --configuration Release` | `Passed: 2, Failed: 0, Total: 2` | 0 |
| `bash scripts/harness/test-hooks.sh` | `48 tests, 0 échec(s)`, dont « un seul rappel (stop_hook_active) » | 0 |

**Hook `Stop` sans boucle, en conditions réelles** (copie jetable du dépôt, branche avec un commit sans rapport, session `claude -p` non interactive, modèle Haiku) :

1. Premier arrêt → code **2**, message : « … rédigez son rapport avant de terminer, en y indiquant les contrôles non exécutés. Si vous attendez une réponse du propriétaire, dites-le et arrêtez-vous. »
2. Claude lance 2 commandes `git` en lecture seule et n'écrit pas de rapport.
3. Second arrêt → code **0**. Fin : `success`, 4 tours, 0,004 $. Aucun fichier modifié.

**Vérifications de périmètre** (§5.4 du mandat) :

- Fichiers modifiés par ce mandat (`5ed8960..ebda48e`) : 7 fichiers, tous autorisés (`CLAUDE.md`, registre gameplay, hook `Stop`, 3 documents archivés, index).
- Aucun fichier C# modifié. `src/` ne contient qu'une classe vide (`SimulationAssembly`).
- `git log -p --all` passé au filtre des motifs de secrets (jetons GitHub, clés, `password=`…) : aucune correspondance.
- `git ls-remote origin` avant publication : vide (aucune branche, aucun commit distant).

## 3. Graphe Git

```
*   26e6ad7 Merge branch 'main' into chore/lot-0b-harnais   ← chore/lot-0b-harnais
|\
| * fdbff5d chore: initialisation du dépôt                    ← main
* ebda48e docs(lot-0b): archivage de la spécification v0.2, du retour et du mandat de clôture
* daf3406 fix(lot-0b): corrections NC-1 à NC-3 du harnais
* 5ed8960 docs(lot-0b): réponse au retour n° 1 de l'orchestrateur
* 6d26e9d fix(harnais): contrôle Stop effectif sans branche main
* 46629b4 docs(lot-0b): rapport d'exécution final
* 9039493 fix(lot-0b): corrections issues de la revue indépendante, activation des hooks
* 7532b04 chore(lot-0b): harnais de développement minimal, sans gameplay
```

- `main` = `fdbff5d` : commit sans parent, arbre vide (`4b825dc6…`), **0 fichier**.
- `26e6ad7` : fusion de `main` **dans** la branche du lot (`--allow-unrelated-histories`, sans rebase). Elle ne modifie aucun fichier.
- Les 7 commits antérieurs sont intacts (tous ancêtres de `26e6ad7`, mêmes identifiants) : **aucune réécriture**.
- `git diff --name-only main...chore/lot-0b-harnais` : 27 fichiers, soit exactement les fichiers suivis du lot.
- Ce rapport est ajouté par le commit qui suit `26e6ad7`.

## 4. Publication et CI

_Rédigé avant le premier push avec la mention « CI distante non exécutée à ce stade ». Complété une seule fois après la première CI._

**Publication :**

| Commande | Résultat | Code |
|---|---|---|
| `git push -u origin main` | `* [new branch] main -> main` | 0 |
| `git push -u origin chore/lot-0b-harnais` | `* [new branch] chore/lot-0b-harnais -> chore/lot-0b-harnais` | 0 |

- Aucun `--force`.
- Branches distantes après push (API GitHub) : `main` = `fdbff5d`, `chore/lot-0b-harnais` = `f88c022`. Aucune n'est protégée.
- **PR : [mengpo1/bastion#1](https://github.com/mengpo1/bastion/pull/1)**, `draft: true`, `merged: false`, base `main` (`fdbff5d`), tête `f88c022`, 28 fichiers, 9 commits.

**Première CI** (workflow `CI`, `.github/workflows/ci.yml`) :

| Exécution | Événement | Commit testé | Statut | Étapes en échec |
|---|---|---|---|---|
| [n° 1 — 42472439100](https://github.com/mengpo1/bastion/actions/runs/42472439100) | `push` | `f88c022` | **success** | aucune |
| [n° 2 — 42472482525](https://github.com/mengpo1/bastion/actions/runs/42472482525) | `pull_request` | `062bb8c`, fusion temporaire de `f88c022` dans `fdbff5d` créée par GitHub | **success** | aucune |

Relevé dans les journaux des deux exécutions :

- Runner `ubuntu-24.04` (image 20261101.360.1) ; `actions/checkout@v7` (SHA `3d3c42e5…`) ; `actions/setup-dotnet@v6` (SHA `0f4a354d…`) ; jeton GitHub limité à `contents: read`.
- **SDK utilisé en CI : 10.0.403**, déjà présent sur le runner et retenu via `global.json` (canal 10.0). Il diffère du 10.0.114 local, comme prévu dans `LOT-0B-RETOUR-1.md` §5.
- Restauration OK ; compilation **0 avertissement, 0 erreur** (aucune alerte NuGet) ; format sans écart ; tests .NET **2/2** ; tests des hooks **48/48**.

**NC-4 satisfait :** preuve d'exécution de la CI disponible (exécutions n° 1 et n° 2).

## 5. Arbitrages du mandat appliqués

- .NET 10 conservé provisoirement (`global.json` : `10.0.100`, `latestFeature`). **Compatibilité Godot non affirmée** (non testée).
- `Bastion.slnx` et `chore/lot-0b-harnais` conservés.
- Limites acceptées provisoirement : faux positif sur une commande citant `rm -rf` ; dépendance Godot déclarée mais inutilisée non détectée.
- `TreatWarningsAsErrors` conservé, alertes NuGet comprises. Si la CI échoue sur un avis de sécurité, ce sera rapporté, pas masqué.
- Aucune mécanique marquée validée. `docs/decisions/TECHNICAL-DECISIONS.md` n'est **pas modifié** : ce mandat n'autorise pas son édition. Les arbitrages ci-dessus y restent donc à transcrire.

## 6. Limites, vérifications reportées, anomalies

**Limites acceptées :**

- Hooks fondés sur des motifs de texte, contournables, qui ne prouvent pas l'absence de gameplay.
- Hook `Stop` : **non qualifié** (lot 0C).
- Comportement de « ask » non documenté en `bypassPermissions`, `dontAsk` et `claude -p`.

**Vérifications reportées :**

- Projet Godot et lancement headless (H-Q10) : Godot absent de l'environnement.
- Qualification H-Q01 à H-Q10 : lot 0C.
- Hooks `SessionStart`, `PostToolUse` et `SubagentStop` ; analyse statique, contrôle des secrets et validation du registre en CI : différés.
- **Protection de `main` sur GitHub : étape distincte, à confirmer par le propriétaire.** Non mise en place.

**Anomalies :**

- Le push de `main` a affiché `fatal: expected 'acknowledgments', received 'packfile'`, puis `push negotiation failed; proceeding anyway with push`. Le push a abouti (code 0, branche visible avec le bon identifiant). Message attribué à la négociation via le proxy du bac à sable ; sans effet constaté.
- `docs/decisions/TECHNICAL-DECISIONS.md` ne reflète pas encore les arbitrages de la section 5.

## 7. Déclaration

**Aucun gameplay implémenté ; aucune fusion dans main.**

Arrêt à l'issue du lot 0B.
