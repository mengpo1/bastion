# LOT-0B — Rapport d'exécution

**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-0B-v1.0.md` · **Exécutant :** Claude Code · **Date :** 8 nov. 2026
**Branche locale :** `chore/lot-0b-harnais` · **Push :** non effectué (non autorisé)

> **Complément :** voir `docs/reviews/LOT-0B-RETOUR-1.md` (conformité à la spécification v0.2, correction du contrôle `Stop` sans `main`, 48 tests de hooks, plan Git). Le présent rapport décrit l'état au commit `46629b4`.

## 1. Résumé

- Dépôt trouvé **vide** (aucun commit, aucun fichier ; dépôt distant `github.com/mengpo1/bastion` vide aussi). Rien n'a été écrasé, déplacé ni supprimé.
- Créés : règles permanentes (`CLAUDE.md`), registres sans aucune décision de gameplay, solution C# minimale (1 bibliothèque + 1 projet de tests, 2 tests fumée techniques), 2 hooks Claude Code avec 44 tests, une CI GitHub Actions.
- Les hooks sont **actifs** : un `rm -rf` tenté dans cette session a été bloqué par Claude Code (section 5).
- Revue indépendante faite par un agent distinct : 13 points, 10 corrigés, 3 documentés (section 7).
- Exécution dans un **bac à sable cloud** (Ubuntu 24.04), pas sur la machine du propriétaire : les versions relevées sont celles de ce bac à sable.
- **Non fait, avec raison :** projet Godot et lancement headless (Godot absent, téléchargement bloqué) ; exécution de la CI distante (aucun push autorisé).

## 2. Fichiers créés

Aucun fichier préexistant : tous les fichiers sont nouveaux.

| Fichier | Rôle |
|---|---|
| `README.md` | Présentation, structure, commandes |
| `CLAUDE.md` | Règles permanentes de Claude Code |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | Registre gameplay — aucune décision |
| `docs/decisions/TECHNICAL-DECISIONS.md` | Registre technique — aucune décision « Validée » ; 2 exigences du mandat ; 6 choix « Proposée » |
| `docs/references/OXCE-BASELINE.md` | Référence OXCE — « version/commit à figer » |
| `docs/mandates/BASTION-MANDAT-LOT-0B-v1.0.md` | Copie à l'identique du mandat (SHA-256 identique à l'original) |
| `docs/mandates/README.md` | Index ; référence la spécification v0.2 (absente du dépôt), sans la modifier |
| `docs/reviews/LOT-0B-EXECUTION.md` | Ce rapport |
| `.gitignore`, `.gitattributes` | Exclusions .NET/Godot/IDE ; fins de ligne LF pour `*.sh` |
| `global.json`, `Directory.Build.props`, `Bastion.slnx` | SDK, cible `net10.0`, solution |
| `src/Bastion.Simulation/` (csproj + `SimulationAssembly.cs`) | Bibliothèque de simulation : une classe vide servant de repère technique |
| `tests/Bastion.Simulation.Tests/` (csproj + `SmokeTests.cs`) | 2 tests fumée : nom de l'assembly ; aucun usage de Godot |
| `scripts/harness/pre-tool-use.sh` | Hook PreToolUse |
| `scripts/harness/stop-report-check.sh` | Hook Stop |
| `scripts/harness/test-hooks.sh` | 44 tests des hooks (effets et limites) |
| `scripts/harness/README.md` | Fonctionnement et limites des hooks |
| `.claude/settings.json` | Branchement des 2 hooks |
| `.github/workflows/ci.yml` | CI : restauration, compilation, format, tests .NET, tests des hooks |

## 3. Versions et décisions techniques

### Versions relevées (bac à sable)

| Outil | Version | Commentaire |
|---|---|---|
| Git | 2.43.0 | préinstallé |
| Claude Code | 2.1.319 | préinstallé |
| .NET SDK | 10.0.114 (runtime 10.0.14) | **Absent au départ.** Paquets officiels Ubuntu `dotnet-sdk-10.0` téléchargés (`apt-get download`) et **extraits dans un dossier temporaire du bac à sable** (`dpkg -x`), sans installation système. Seul effet global : `apt-get update` (index des paquets). Les serveurs Microsoft (`dot.net`, `builds.dotnet.microsoft.com`) sont refusés par le réseau du bac à sable. |
| Godot .NET | **absent** | `github.com/godotengine/godot/releases` refusé (403) par le réseau du bac à sable. Non installé, pas de contournement. |
| bash / sed / grep | 5.2.21 / GNU / GNU | les hooks n'utilisent pas jq |
| `actions/checkout`, `actions/setup-dotnet` | v7 (7.0.1), v6 (6.1.0) | étiquettes lues avec `git ls-remote` le 8 nov. 2026 ; `setup-dotnet` v6 prend en charge `global.json` avec `rollForward: latestFeature` (README de l'action) |

### Décisions

Toutes dans `docs/decisions/TECHNICAL-DECISIONS.md`. **Aucune n'est « Validée ».** T-001 (simulation indépendante de Godot) et T-002 (Godot .NET / C#, version à figer) ont le statut « Exigence de mandat ». Les choix du lot (T-101 à T-106) sont « Proposée ».

### Incertitudes

- **Compatibilité `net10.0` ↔ Godot .NET non vérifiée** (Godot indisponible). Pour passer à `net8.0` : une ligne dans `Directory.Build.props`, une dans `global.json`. .NET 8 arrive en fin de support le 10 nov. 2026.
- Versions de la machine du propriétaire inconnues.
- Spécification `BASTION-HARNAIS-LOT-0A-v0.2.md` **non fournie** : noms de projets et liste des hooks qu'elle prévoit non vérifiés.
- Hooks testés sous Linux (GNU) uniquement ; macOS (BSD) et Windows (Git Bash) non testés.

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
| 8 | `bash scripts/harness/test-hooks.sh` | `44 tests, 0 échec(s)` | 0 |
| 9 | La CI doit échouer — copie du dépôt avec un test faux, puis `dotnet test` | `Failed! - Failed: 1, Passed: 1` | 1 |
| 10 | La CI doit échouer — copie avec une erreur de compilation, puis `dotnet build` | 2 erreurs `CS` | 1 |
| 11 | La CI doit échouer — copie avec un espace en trop, puis `dotnet format --verify-no-changes` | `error WHITESPACE` | 2 |
| 12 | 1re version de la suite (28 tests) contre un hook PreToolUse neutralisé (copie) | `28 tests, 15 échec(s)` : la suite détecte un hook inopérant | 1 |
| 13 | Suite actuelle (44 tests) contre les hooks du commit `7532b04` (copie) | `44 tests, 11 échec(s)` : exactement les défauts relevés par la revue | 1 |
| 14 | `jq` sur la sortie « ask » et sur `.claude/settings.json` | JSON valide | 0 |
| 15 | Entrées produites par `JSON.stringify` (format de Claude Code) | décisions attendues (section 5) | — |
| 16 | Lecture du YAML de CI (`yaml.safe_load`) | 7 étapes, YAML valide | 0 |
| 17 | **En direct dans Claude Code**, après activation : `rm -rf` sur un dossier vide jetable | refusé : `PreToolUse:Bash hook error: [command hook]: Harnais Bastion — BLOQUÉ : commande destructive. Voir CLAUDE.md.` | appel refusé |
| 18 | En direct : `ls -d` du même dossier | dossier toujours présent | 0 |
| 19 | Projet Godot headless | **non réalisé** : Godot absent | — |
| 20 | CI distante | **workflow préparé, CI non exécutée** (aucun push) | — |
| 21 | Revue indépendante | 13 points (section 7) | — |

## 5. Hooks : tests et limites

Sortie complète de `bash scripts/harness/test-hooks.sh` (code de sortie 0) :

```
== PreToolUse : effets ==
OK     [autorise] écriture d'un fichier source
OK     [autorise] commande ordinaire (dotnet test)
OK     [autorise] lecture d'un fichier protégé (cat CLAUDE.md)
OK     [autorise] git merge-base (lecture seule)
OK     [autorise] commit sur une branche de travail
OK     [autorise] plan de Claude dans ~/.claude/plans/
OK     [autorise] lecture GitHub par MCP (get_file_contents)
OK     [autorise] lecture GitHub par MCP (pull_request_read)
OK     [demande] Edit du registre de gameplay
OK     [demande] nouveau fichier dans docs/gameplay/
OK     [demande] Write de .claude/settings.json
OK     [demande] Write de ~/.claude/settings.json
OK     [demande] Write d'un registre, chemin Windows
OK     [demande] NotebookEdit dans docs/mandates/
OK     [demande] redirection shell vers un registre
OK     [demande] git push
OK     [demande] git pull
OK     [demande] git merge
OK     [demande] gh pr merge
OK     [demande] fusion GitHub par MCP (merge_pull_request)
OK     [demande] écriture GitHub par MCP (push_files)
OK     [bloque] rm -rf
OK     [bloque] rm -fr sur une 2e ligne
OK     [bloque] git reset --hard
OK     [bloque] git clean -fd
OK     [bloque] git push --force
OK     [bloque] git push -f
OK     [bloque] git branch -D
OK     [bloque] commit sur main
OK     [bloque] premier commit sur main (dépôt neuf)
== PreToolUse : limites connues ==
OK     [autorise] LIMITE rm --recursive non détecté
OK     [autorise] LIMITE écriture via python non détectée
OK     [autorise] LIMITE code de gameplay dans src/ non détecté
OK     [autorise] LIMITE checkout main puis commit dans la même commande
OK     [demande] LIMITE faux positif : message de commit citant git push
OK     [bloque] LIMITE faux positif bloquant : recherche du texte rm -rf
== Stop : effets et limites ==
OK     [autorise] dépôt propre sur main
OK     [bloque] branche modifiée sans rapport
OK     [autorise] LIMITE un seul rappel (stop_hook_active)
OK     [autorise] rapport ajouté par renommage, nom avec espace
OK     [autorise] branche modifiée avec rapport dans docs/reviews/
OK     [bloque] modification non commitée sur main sans rapport
OK     [autorise] LIMITE sans main : commits non contrôlés
OK     [bloque] sans main : ancien rapport commité, nouvelle modification
== 44 tests, 0 échec(s) ==
```

Essais avec des entrées produites par `JSON.stringify`, sur les hooks finaux :

| Entrée | Résultat |
|---|---|
| `echo "a\"b" && rm -rf /tmp/x` | code 2 (bloqué) |
| `ls` puis, à la ligne, `rm -Rf build` | code 2 (bloqué) |
| `git push origin HEAD` | code 0 + « ask » |
| `grep -n "command" x.json` | code 0 (autorisé) |
| `echo "\\server\share"` | code 0 (autorisé) |
| Edit de `C:\Users\p\bastion\docs\gameplay\GAMEPLAY-DECISIONS.md` | « ask » (chemin Windows reconnu) |
| Write de `src/a.cs` dont le contenu contient `"file_path":"CLAUDE.md" rm -rf /` | code 0 (seul le chemin compte) |
| `mcp__github__create_pull_request` | « ask » |

**Essais en direct dans Claude Code** (hooks rechargés automatiquement après création de `.claude/settings.json`) :

- **Interdit :** `rm -rf` sur un dossier vide du bac à sable → appel refusé par Claude Code avec le message du hook ; dossier intact.
- **Autorisé :** commandes ordinaires (`ls`, `git status`, `git add`, `git commit` sur la branche de travail, tests) → exécutées normalement.
- **« ask » non essayé en direct** : il aurait affiché une demande d'accord au propriétaire et bloqué la session en son absence. Vérifié seulement par les tests du script.

Autre observation : un hook Stop propre à l'environnement cloud (hors dépôt) a demandé de « commit and push ». Le commit local a été fait ; le push ne l'a pas été (mandat §5).

**Limites** (détaillées dans `scripts/harness/README.md`) :

- Détection par motifs de texte, contournable (`rm --recursive`, python, `git -C`, scripts intermédiaires…).
- **Les hooks ne prouvent pas l'absence de changement de gameplay** : ils n'analysent pas le code.
- Faux positifs : citer `git push` déclenche une demande d'accord ; citer `rm -rf` (recherche, message de commit) **bloque** la commande.
- « ask » : documenté comme une demande à l'utilisateur en mode par défaut et en mode auto ; non documenté en `bypassPermissions`, `dontAsk` et `claude -p`.
- Hook Stop : vérifie la présence d'un fichier modifié dans `docs/reviews/`, pas son contenu ; un seul rappel par arrêt ; **tant que `main` n'existe pas, seules les modifications non commitées sont contrôlées**.
- Non couverts : actions humaines, CI, interface web de GitHub, serveurs MCP autres que `github`.
- Prérequis : bash, git, sed, grep (Git Bash sous Windows).

**Hooks supplémentaires de la spécification 0.2 :** non installés. La spécification n'ayant pas été fournie, sa liste n'a pas pu être vérifiée ; report explicite.

## 6. Blocages, risques et décisions attendues du propriétaire

| # | Point | Proposition |
|---|---|---|
| D1 | **Push non autorisé.** Le bac à sable cloud est temporaire : sans push, le travail est perdu à sa fermeture. | Autoriser le push. |
| D2 | **Aucune branche `main`** (dépôt distant vide). Une PR exige une base ayant un historique commun avec la branche. | Créer `main` par un commit initial vide, replacer les commits du lot dessus (rebase d'une branche locale jamais poussée), pousser les deux branches, ouvrir une PR en brouillon. Chaque étape demande votre accord. |
| D3 | **Nom de branche** : la session cloud prévoyait `claude/new-session-mgfohp`, le mandat impose `chore/lot-0b-harnais`. Le mandat a été suivi. | Confirmer. |
| D4 | Version .NET (T-101) : `net10.0` provisoire, compatibilité Godot non vérifiée. | Valider ou demander `net8.0`. |
| D5 | Version de Godot .NET à figer (T-002) ; projet Godot et test headless reportés. | Fixer la version ; mandat distinct pour le projet Godot. |
| D6 | Spécification v0.2 absente du dépôt. | La déposer telle quelle dans `docs/mandates/`. |
| D7 | Référence OXCE à figer (version/commit, licence). | Décision ou mandat distinct. |
| D8 | Exigences T-001, T-002 et choix provisoires T-102 à T-106. | Valider ou corriger. |
| D9 | `TreatWarningsAsErrors` transforme aussi en erreur les alertes de sécurité NuGet : un avis publié sur un paquet de test peut faire échouer la CI sans changement de code. | Conserver (signal de sécurité) ou exclure ces alertes. |
| D10 | Comportement de « ask » non vérifié dans votre mode de permission habituel. | Le vérifier lors d'une session sur votre poste. |

## 7. Revue indépendante

Faite par un agent distinct (sous-agent Claude, contexte séparé, lecture seule ; pas une revue humaine), sur la version du commit `7532b04` et le futur `.claude/settings.json`. Chaque point est vérifié par un test dans la suite actuelle, sauf mention contraire.

| # | Constat de la revue | Traitement |
|---|---|---|
| 1 | Hook Stop inopérant tant que `main` n'existe pas (tout le dépôt comptait, ancien rapport compris) | **Corrigé** : sans `main`, seules les modifications non commitées comptent ; limite documentée |
| 2 | `git push -f` seulement soumis à accord, pas bloqué | **Corrigé** |
| 3 | Premier commit sur un `main` pas encore créé non bloqué | **Corrigé** (`git symbolic-ref`) |
| 4 | Faux positifs **bloquants** quand une commande cite `rm -rf` | **Documenté** (README, test « LIMITE ») ; motif gardé large par prudence |
| 5 | `git merge-base` (lecture seule) soumis à accord | **Corrigé** |
| 6 | Le hook Stop s'exécute aussi quand Claude s'arrête pour poser une question | **Message reformulé** et limite documentée |
| 7 | Statut « Validée » de T-001/T-002 non étayé par les sources ; règle du registre plus souple que `CLAUDE.md` | **Corrigé** : statut « Exigence de mandat », règle alignée |
| 8 | Chemins protégés plus étroits que `CLAUDE.md` ; `~/.claude/plans/` soumis à accord à tort | **Corrigé** : dossiers des registres protégés ; seuls les fichiers `settings*.json` de `.claude/` |
| 9 | `gh pr merge`, `git pull` et outils MCP GitHub non surveillés | **Corrigé** ; autres serveurs MCP et interface web documentés comme non couverts |
| 10 | Hook Stop : faux blocage sur un renommage ou un nom entre guillemets | **Corrigé** |
| 11 | `test-hooks.sh` échoue si la signature des commits est activée | **Corrigé** (`-c commit.gpgsign=false`) ; pas de test dédié |
| 12 | Le test « pas de Godot » ne voit pas un paquet Godot déclaré mais inutilisé | **Documenté** dans le test |
| 13 | `TreatWarningsAsErrors` et alertes NuGet | **Non modifié** : décision D9 |

Points contrôlés sans remarque par la revue : copie du mandat (SHA-256), périmètre (aucun gameplay, aucun projet Godot vide), chaîne .NET et ses échecs attendus, versions des paquets de test, versions des actions de CI, robustesse de l'extraction JSON (guillemets, barres obliques inverses, chemins Windows, accents, entrée de 2 Mo).

## 8. Commits locaux

| Commit | Contenu |
|---|---|
| `7532b04` | Harnais initial (22 fichiers) |
| `9039493` | Corrections de la revue, activation des hooks |
| commit suivant | Ce rapport, version finale |

Diff complet du lot : `git log -p chore/lot-0b-harnais`. Aucun push : ces commits n'existent que dans le bac à sable.

## 9. Déclaration

**Aucun gameplay implémenté.** Le seul code C# est une classe vide (`SimulationAssembly`) et deux tests techniques (nom de l'assembly, absence d'usage de Godot). Aucune donnée de jeu, aucune mécanique, aucun asset, aucun code OXCE.

Arrêt à la fin du lot 0B. En attente des instructions de l'orchestrateur.
