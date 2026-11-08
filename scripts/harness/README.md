# Harnais Claude Code — hooks

Branchés dans `.claude/settings.json`. Tests : `bash scripts/harness/test-hooks.sh` (lancé aussi par la CI).

| Script | Événement | Effet |
|---|---|---|
| `pre-tool-use.sh` | PreToolUse (Bash, Write, Edit, MultiEdit, NotebookEdit, outils MCP `mcp__github__*`) | **Bloque** les commandes destructives (`rm -r…`, `git reset --hard`, `git clean -f`, `git branch -D`, `git push --force` / `-f`) et les commits sur `main`. **Demande l'accord** du propriétaire (« ask ») pour écrire dans un fichier protégé, pour `git push`, `pull`, `merge`, `rebase`, `gh pr merge`, et pour tout outil MCP GitHub qui écrit (tout sauf `get_*`, `list_*`, `search_*`, `*_read`, `*_get`, `*_list`). |
| `stop-report-check.sh` | Stop | Si des fichiers ont changé (non commités, ou sur la branche depuis `main`), exige qu'un fichier de `docs/reviews/` en fasse partie. Sinon, un rappel est renvoyé à Claude. |

Fichiers protégés : `docs/gameplay/`, `docs/decisions/`, `docs/references/`, `docs/mandates/`, `CLAUDE.md`, `.claude/settings*.json` (projet et utilisateur), `scripts/harness/`, `.github/workflows/`.

## Limites

- **Détection par motifs de texte, contournable** : `rm --recursive`, écriture via un autre programme (python…), `git -C`, variables, scripts intermédiaires, `git checkout main && git commit` dans la même commande. Les tests « LIMITE » de `test-hooks.sh` le montrent.
- **Ne prouve pas l'absence de gameplay** : aucun hook n'analyse le contenu du code.
- **Faux positifs** : une commande qui *cite* `git push` déclenche une demande d'accord ; une commande qui *cite* `rm -rf` (recherche de texte, message de commit) est **bloquée**. Reformuler la commande.
- **« ask »** : selon la documentation Claude Code, la demande s'affiche en mode par défaut et en mode auto ; le comportement en `bypassPermissions`, `dontAsk` et `claude -p` n'est pas documenté.
- **Hook Stop** :
  - vérifie qu'un fichier de `docs/reviews/` a changé, pas son contenu ;
  - s'exécute à chaque fin de tour, y compris quand Claude s'arrête pour poser une question : un seul rappel, puis l'arrêt est accepté (`stop_hook_active`) ;
  - **tant que la branche `main` n'existe pas**, seules les modifications non commitées sont contrôlées.
- **Portée** : uniquement les outils de Claude Code. Non couverts : les actions humaines, la CI, l'interface web de GitHub, les serveurs MCP autres que `github`.
- **Prérequis** : bash, git, sed, grep. Sous Windows, Git Bash est nécessaire (sans lui, Claude Code lance les hooks avec PowerShell et ils échouent). Testé sous Linux (GNU) ; macOS (BSD) non testé.
