# Harnais Claude Code — hooks

Branchés dans `.claude/settings.json`. Tests : `bash scripts/harness/test-hooks.sh` (lancé aussi par la CI).

| Script | Événement | Effet |
|---|---|---|
| `pre-tool-use.sh` | PreToolUse (Bash, Write, Edit, MultiEdit, NotebookEdit) | **Bloque** les commandes destructives (`rm -r…`, `git reset --hard`, `git clean -f`, `git branch -D`, `git push --force`) et les commits sur `main`. **Demande l'accord** du propriétaire (« ask ») pour écrire dans un fichier protégé et pour `git push`, `git merge`, `git rebase`. |
| `stop-report-check.sh` | Stop | Si des fichiers ont changé (non commités, ou sur la branche depuis `main`), exige qu'un fichier de `docs/reviews/` en fasse partie. Sinon, un rappel est renvoyé à Claude. |

Fichiers protégés : `GAMEPLAY-DECISIONS.md`, `TECHNICAL-DECISIONS.md`, `OXCE-BASELINE.md`, `CLAUDE.md`, `docs/mandates/`, `.claude/`, `scripts/harness/`, `.github/workflows/`.

## Limites

- **Détection par motifs de texte, contournable** : `rm --recursive`, écriture via un autre programme (python…), `git -C`, variables, scripts intermédiaires, `git checkout main && git commit` dans la même commande. Les tests « LIMITE » de `test-hooks.sh` le montrent.
- **Ne prouve pas l'absence de gameplay** : aucun hook n'analyse le contenu du code.
- **Faux positifs** : une commande qui *cite* `git push`, ou un fichier protégé avec `>`, `cp`, `mv`…, déclenche une demande d'accord.
- **« ask »** : selon la documentation Claude Code, la demande s'affiche en mode par défaut et en mode auto ; le comportement en `bypassPermissions`, `dontAsk` et `claude -p` n'est pas documenté. Non observé en direct dans le lot 0B.
- **Hook Stop** : vérifie seulement qu'un fichier de `docs/reviews/` a changé, pas son contenu ; un seul rappel par arrêt (`stop_hook_active`).
- **Portée** : uniquement les outils de Claude Code ; pas les actions humaines ni la CI.
- **Prérequis** : bash, git, sed, grep. Sous Windows, Git Bash est nécessaire (sans lui, Claude Code lance les hooks avec PowerShell et ils échouent).
