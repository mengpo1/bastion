# LOT-0B — Rapport d'exécution

**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-0B-v1.0.md` · **Exécutant :** Claude Code · **Date :** 8 nov. 2026
**Branche locale :** `chore/lot-0b-harnais` · **Push :** non effectué (non autorisé)

## 1. Résumé

- Dépôt trouvé **vide** (aucun commit, aucun fichier ; dépôt distant `github.com/mengpo1/bastion` vide aussi). Rien n'a donc été écrasé, déplacé ni supprimé.
- Créés : règles permanentes (`CLAUDE.md`), registres vides de toute décision de gameplay, solution C# minimale (1 bibliothèque + 1 projet de tests, 2 tests fumée techniques), 2 hooks Claude Code avec 28 tests, une CI GitHub Actions.
- Exécution dans un **bac à sable cloud** (Ubuntu 24.04), pas sur la machine du propriétaire : les versions vérifiées sont celles de ce bac à sable.
- **Non fait, avec raison :** projet Godot et lancement headless (Godot absent, téléchargement bloqué) ; exécution de la CI distante (aucun push autorisé).

## 2. Fichiers créés

Aucun fichier préexistant : tous les fichiers sont nouveaux.

| Fichier | Rôle |
|---|---|
| `README.md` | Présentation, structure, commandes |
| `CLAUDE.md` | Règles permanentes de Claude Code |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | Registre gameplay — aucune décision |
| `docs/decisions/TECHNICAL-DECISIONS.md` | Registre technique — 2 décisions issues du mandat, 6 choix provisoires « Proposée » |
| `docs/references/OXCE-BASELINE.md` | Référence OXCE — « version/commit à figer » |
| `docs/mandates/BASTION-MANDAT-LOT-0B-v1.0.md` | Copie à l'identique du mandat (SHA-256 identique à l'original) |
| `docs/mandates/README.md` | Index ; référence la spécification v0.2 (absente du dépôt) |
| `docs/reviews/LOT-0B-EXECUTION.md` | Ce rapport |
| `.gitignore`, `.gitattributes` | Exclusions .NET/Godot/IDE ; fins de ligne LF pour `*.sh` |
| `global.json`, `Directory.Build.props`, `Bastion.slnx` | SDK, cible `net10.0`, solution |
| `src/Bastion.Simulation/` (csproj + `SimulationAssembly.cs`) | Bibliothèque de simulation vide de logique (repère technique) |
| `tests/Bastion.Simulation.Tests/` (csproj + `SmokeTests.cs`) | 2 tests fumée : nom de l'assembly ; aucune référence à Godot |
| `scripts/harness/pre-tool-use.sh` | Hook PreToolUse |
| `scripts/harness/stop-report-check.sh` | Hook Stop |
| `scripts/harness/test-hooks.sh` | 28 tests des hooks (effets et limites) |
| `scripts/harness/README.md` | Fonctionnement et limites des hooks |
| `.claude/settings.json` | Branchement des 2 hooks |
| `.github/workflows/ci.yml` | CI : restauration, compilation, format, tests .NET, tests des hooks |

Commits locaux : voir section 8.

## 3. Versions et décisions techniques

### Versions relevées (bac à sable)

| Outil | Version | Commentaire |
|---|---|---|
| Git | 2.43.0 | préinstallé |
| Claude Code | 2.1.319 | préinstallé |
| .NET SDK | 10.0.114 (runtime 10.0.14) | **absent au départ.** Paquets officiels Ubuntu `dotnet-sdk-10.0` téléchargés (`apt-get download`) et **extraits dans un dossier temporaire du bac à sable** (`dpkg -x`), sans installation système. Seul effet global : `apt-get update` (index des paquets). Les serveurs Microsoft (`dot.net`, `builds.dotnet.microsoft.com`) sont refusés par le réseau du bac à sable. |
| Godot .NET | **absent** | `github.com/godotengine/godot/releases` refusé (403) par le réseau du bac à sable. Non installé, pas de contournement. |
| bash / sed / grep / jq | 5.2.21 / GNU / GNU / présent | les hooks n'utilisent pas jq |
| `actions/checkout`, `actions/setup-dotnet` | v7 (7.0.1), v6 (6.1.0) | étiquettes lues avec `git ls-remote` le 8 nov. 2026 |

### Décisions

Toutes dans `docs/decisions/TECHNICAL-DECISIONS.md`. Seules T-001 (simulation indépendante de Godot) et T-002 (Godot .NET / C#, version à figer) sont marquées « Validée », avec pour source le mandat LOT-0B. Les choix du lot (T-101 à T-106) sont **« Proposée »**.

### Incertitudes

- **Compatibilité `net10.0` ↔ Godot .NET non vérifiée** (Godot indisponible). Si la version de Godot retenue l'exige, passer à `net8.0` : une ligne dans `Directory.Build.props` et une dans `global.json`. Attention : .NET 8 arrive en fin de support le 10 nov. 2026.
- Versions de la machine du propriétaire inconnues.
- Spécification `BASTION-HARNAIS-LOT-0A-v0.2.md` **non fournie** : impossible de vérifier les noms de projets ou la liste des hooks qu'elle prévoit.

## 4. Vérifications

Commandes lancées depuis la racine du dépôt, avec le SDK local dans le `PATH`.

| # | Commande | Résultat | Code |
|---|---|---|---|
| 1 | `git status` (avant travaux) | `On branch claude/new-session-mgfohp — No commits yet — nothing to commit` | 0 |
| 2 | `git ls-remote origin` | aucune référence (dépôt distant vide) | 0 |
| 3 | `dotnet --info` | SDK 10.0.114, runtime 10.0.14, ubuntu.24.04-x64 | 0 |
| 4 | `dotnet restore` | 2 projets restaurés | 0 |
| 5 | `dotnet build --no-restore --configuration Release` | `Build succeeded. 0 Warning(s) 0 Error(s)` | 0 |
| 6 | `dotnet format --verify-no-changes --no-restore` | aucune sortie | 0 |
| 7 | `dotnet test --no-build --configuration Release` | `Passed! - Failed: 0, Passed: 2, Skipped: 0, Total: 2` | 0 |
| 8 | `bash scripts/harness/test-hooks.sh` | `28 tests, 0 échec(s)` | 0 |
| 9 | CI doit échouer — copie du dépôt avec un test faux, puis `dotnet test` | `Failed! - Failed: 1, Passed: 1` | 1 |
| 10 | CI doit échouer — copie avec une erreur de compilation, puis `dotnet build` | 2 erreurs `CS` | 1 |
| 11 | CI doit échouer — copie avec un espace en trop, puis `dotnet format --verify-no-changes` | `error WHITESPACE` | 2 |
| 12 | Tests des hooks contre un hook PreToolUse neutralisé (copie) | `28 tests, 15 échec(s)` : les tests détectent un hook inopérant | 1 |
| 13 | Sortie « ask » passée à `jq` | JSON valide | 0 |
| 14 | Entrées produites par `JSON.stringify` (format de Claude Code) : guillemets échappés, retours à la ligne, chemins Windows, contenu piégé | décisions attendues (détail section 5) | — |
| 15 | Lecture du YAML de CI (`yaml.safe_load`) | 7 étapes, YAML valide | 0 |
| 16 | Projet Godot headless | **non réalisé** : Godot absent | — |
| 17 | CI distante | **workflow préparé, CI non exécutée** (aucun push) | — |
| 18 | Revue indépendante | voir section 7 | — |

## 5. Hooks : tests et limites

Sortie complète de `bash scripts/harness/test-hooks.sh` (code de sortie 0) :

```
== PreToolUse : effets ==
OK     [autorise] écriture d'un fichier source
OK     [autorise] commande ordinaire (dotnet test)
OK     [autorise] lecture d'un fichier protégé (cat CLAUDE.md)
OK     [autorise] commit sur une branche de travail
OK     [demande] Edit du registre de gameplay
OK     [demande] Write de .claude/settings.json
OK     [demande] Write d'un registre, chemin Windows
OK     [demande] NotebookEdit dans docs/mandates/
OK     [demande] redirection shell vers un registre
OK     [demande] git push
OK     [demande] git merge
OK     [bloque] rm -rf
OK     [bloque] rm -fr sur une 2e ligne
OK     [bloque] git reset --hard
OK     [bloque] git clean -fd
OK     [bloque] git push --force
OK     [bloque] git branch -D
OK     [bloque] commit sur main
== PreToolUse : limites connues (non détectées) ==
OK     [autorise] LIMITE rm --recursive
OK     [autorise] LIMITE écriture via python
OK     [autorise] LIMITE code de gameplay dans src/
OK     [autorise] LIMITE commit sur main après checkout dans la même commande
OK     [demande] LIMITE faux positif : message de commit citant git push
== Stop : effets et limites ==
OK     [autorise] dépôt propre sur main
OK     [bloque] branche modifiée sans rapport
OK     [autorise] LIMITE un seul rappel (stop_hook_active)
OK     [autorise] branche modifiée avec rapport dans docs/reviews/
OK     [bloque] modification non commitée sur main sans rapport
== 28 tests, 0 échec(s) ==
```

Essais complémentaires avec des entrées produites par `JSON.stringify` :

| Entrée | Code obtenu |
|---|---|
| `echo "a\"b" && rm -rf /tmp/x` | 2 (bloqué) |
| `ls` puis, à la ligne, `rm -Rf build` | 2 (bloqué) |
| `git push origin HEAD` | 0 + « ask » |
| `grep -n "command" x.json` | 0 (autorisé) |
| Edit de `C:\Users\p\bastion\docs\gameplay\GAMEPLAY-DECISIONS.md` | « ask », chemin normalisé en `C:/Users/…` |
| Write de `src/a.cs` dont le contenu contient `"file_path":"CLAUDE.md" rm -rf /` | 0 (autorisé : seul le chemin compte) |

**Essai en direct dans Claude Code :** _à compléter (section 8)._

**Limites** (détaillées dans `scripts/harness/README.md`) :

- Détection par motifs de texte, contournable (`rm --recursive`, python, `git -C`, scripts intermédiaires…).
- **Les hooks ne prouvent pas l'absence de changement de gameplay** : ils n'analysent pas le code.
- Faux positifs possibles (commande qui cite `git push` ou un fichier protégé avec `>`).
- Comportement de « ask » non documenté en `bypassPermissions`, `dontAsk` et `claude -p` ; documenté comme une demande à l'utilisateur en mode par défaut et en mode auto.
- Le hook Stop vérifie la présence d'un fichier modifié dans `docs/reviews/`, pas son contenu.
- Prérequis : bash, git, sed, grep (Git Bash sous Windows).

**Hooks supplémentaires de la spécification 0.2 :** non installés. La spécification n'ayant pas été fournie, la liste n'a pas pu être vérifiée ; report explicite.

## 6. Blocages, risques et décisions attendues du propriétaire

| # | Point | Proposition |
|---|---|---|
| D1 | **Push non autorisé, dépôt distant vide.** Le bac à sable cloud est temporaire : sans push, le travail est perdu à sa fermeture. | Autoriser le push de `chore/lot-0b-harnais`. |
| D2 | **Aucune branche `main`** : le dépôt distant est vide, une PR n'a pas de base. Le premier push fixera la branche par défaut sur GitHub. | Décider comment créer `main` (par exemple un commit initial vide), puis ouvrir une PR depuis `chore/lot-0b-harnais`. |
| D3 | **Nom de branche** : la session cloud prévoyait `claude/new-session-mgfohp`, le mandat impose `chore/lot-0b-harnais`. Le mandat a été suivi. | Confirmer. |
| D4 | Version .NET (T-101) : `net10.0` provisoire, compatibilité Godot non vérifiée. | Valider ou demander `net8.0`. |
| D5 | Version de Godot .NET à figer (T-002) ; projet Godot et test headless reportés. | Fixer la version ; mandat distinct pour le projet Godot. |
| D6 | Spécification v0.2 absente du dépôt. | La déposer telle quelle dans `docs/mandates/`. |
| D7 | Référence OXCE à figer (version/commit, licence). | Mandat ou décision distincte. |
| D8 | Choix provisoires T-102 à T-106. | Valider ou corriger. |

## 7. Revue indépendante

_À compléter._

## 8. Commits et essai en direct

_À compléter._

## 9. Déclaration

**Aucun gameplay implémenté.** Le seul code C# est une classe vide (`SimulationAssembly`) et deux tests techniques (nom de l'assembly, absence de référence à Godot). Aucune donnée de jeu, aucune mécanique, aucun asset, aucun code OXCE.

Arrêt à la fin du lot 0B. En attente des instructions de l'orchestrateur.
