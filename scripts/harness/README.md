# Harnais Claude Code — hooks et contrôle de traçabilité

Hooks branchés dans `.claude/settings.json` ; contrôle de traçabilité lancé par la CI. Tests : `bash scripts/harness/test-hooks.sh` (lancé aussi par la CI).

| Script | Déclencheur | Effet |
|---|---|---|
| `pre-tool-use.sh` | Hook PreToolUse (Bash, Write, Edit, MultiEdit, NotebookEdit, outils MCP `mcp__github__*`) | **Bloque** les commandes destructives (`rm -r…`, `git reset --hard`, `git clean -f`, `git branch -D`, `git push --force` / `-f`) et les commits sur `main`. **Demande l'accord** du propriétaire (« ask ») pour écrire dans un fichier protégé, pour `git push`, `pull`, `merge`, `rebase`, `gh pr merge`, et pour tout outil MCP GitHub qui écrit (tout sauf `get_*`, `list_*`, `search_*`, `*_read`, `*_get`, `*_list`). |
| `stop-report-check.sh` | Hook Stop | Si des fichiers ont changé (non commités, ou sur la branche depuis `origin/main`, ou `main` à défaut), exige qu'un fichier de `docs/reviews/` en fasse partie. Sinon, un rappel est renvoyé à Claude. |
| `check-simulation-trace.sh` | CI, sur les pull requests (étape « Traçabilité simulation (PR) ») | Si la PR ajoute, modifie, renomme ou supprime un fichier de `src/Bastion.Simulation/`, exige dans la description de la PR une ligne `Traçabilité simulation : TECHNIQUE — <justification>` ou `Traçabilité simulation : MEC-NNNN — <justification>`. Pour `MEC`, la fiche doit exister et porter une décision « acceptée ». Sinon, la CI échoue. |

Fichiers protégés : `docs/gameplay/`, `docs/decisions/`, `docs/references/`, `docs/mandates/`, `CLAUDE.md`, `.claude/settings*.json` (projet et utilisateur), `scripts/harness/`, `.github/workflows/`.

## Limites

- **Détection par motifs de texte, contournable** : `rm --recursive`, écriture via un autre programme (python…), `git -C`, variables, scripts intermédiaires, `git checkout main && git commit` dans la même commande. Les tests « LIMITE » de `test-hooks.sh` le montrent.
- **Ne prouve pas l'absence de gameplay** : aucun hook n'analyse le contenu du code.
- **Faux positifs** : une commande qui *cite* `git push` déclenche une demande d'accord ; une commande qui *cite* `rm -rf` (recherche de texte, message de commit) est **bloquée**. Reformuler la commande.
- **« ask »** : selon la documentation Claude Code, la demande s'affiche en mode par défaut et en mode auto ; le comportement en `bypassPermissions`, `dontAsk` et `claude -p` n'est pas documenté.
- **Hook Stop** :
  - vérifie qu'un fichier de `docs/reviews/` a changé, **pas son contenu** : un rapport vide est accepté (limite connue) ;
  - compare la branche à `origin/main`, qu'il ne met pas à jour. **Faire `git fetch origin main` au début de chaque lot** : sans cette commande, `origin/main` peut être périmée et le hook laisser passer à tort ;
  - plusieurs mandats sur une même branche : le rapport d'un mandat précédent suffit au hook ;
  - s'exécute à chaque fin de tour, y compris quand Claude s'arrête pour poser une question : un seul rappel, puis l'arrêt est accepté (`stop_hook_active`) ;
  - **sans branche `main` ni `origin/main`**, la branche est délimitée par ses commits absents des autres branches locales : si la branche d'origine a été supprimée, son rapport compte encore.
- **Contrôle de traçabilité** :
  - contrôle **syntaxique** : une déclaration `TECHNIQUE` ne prouve pas l'absence de changement de gameplay, la revue doit le vérifier ;
  - pour `MEC`, il vérifie seulement que la fiche existe dans le registre de la PR et que sa décision commence par « acceptée ». Une PR qui ajoute elle-même une fiche « acceptée » passe : la revue doit vérifier que la décision vient du propriétaire ;
  - s'applique aux **pull requests** seulement et ne bloque pas une fusion (`main` n'est pas protégée) ;
  - ne surveille que `src/Bastion.Simulation/`.
- **Portée** : les hooks ne voient que les outils de Claude Code. Non couverts : les actions humaines, l'interface web de GitHub, les serveurs MCP autres que `github`.
- **Prérequis** : bash, git, sed, grep, awk. Sous Windows, Git Bash est nécessaire (sans lui, Claude Code lance les hooks avec PowerShell et ils échouent). Testé sous Linux (GNU) ; macOS (BSD) non testé. En CI, `jq` (présent sur le runner) lit la description de la PR.
