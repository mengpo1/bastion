# Bastion

Projet de jeu en C# avec Godot .NET.

**État :**

- le harnais de développement est installé et opérationnel : hooks Claude Code, tests des hooks, intégration continue ;
- le premier incrément de gameplay, `MEC-0003` (marche sur terrain plat), est implémenté, testé et intégré à `main` (PR #19) ;
- la simulation C# comprend désormais la marche sur terrain plat ; `MEC-0001` et `MEC-0002` restent reportées ;
- un prototype technique Godot, `src/Bastion.Client.Godot/`, existe depuis le lot 1D : une scène reliée à la simulation, qui n'est pas l'interface finale. Il reste hors de `Bastion.slnx`, mais la CI le compile et lance son contrôle fumée depuis le lot 1E.

## Organisation

| Rôle | Responsabilité |
|---|---|
| Propriétaire | Valide les décisions |
| ChatGPT | Orchestre et rédige les mandats |
| Claude Code | Exécute un mandat à la fois |

Règles permanentes de travail : [`CLAUDE.md`](CLAUDE.md).

## Contenu

| Chemin | Rôle |
|---|---|
| `src/Bastion.Simulation/` | Simulation, indépendante de Godot : marche sur terrain plat de `MEC-0003` (`Movement/`) |
| `tests/Bastion.Simulation.Tests/` | Tests xUnit : tests fumée techniques et tests de `MEC-0003` (`Movement/`) |
| `scripts/harness/` | Hooks Claude Code, leurs tests et leurs limites |
| `.claude/settings.json` | Branchement des hooks |
| `.github/workflows/ci.yml` | Intégration continue |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | Registre des décisions de gameplay |
| `docs/decisions/TECHNICAL-DECISIONS.md` | Registre des décisions techniques |
| `docs/references/OXCE-BASELINE.md` | Référence OXCE (commit figé, validée le 8 novembre 2026) |
| `docs/mandates/` | Mandats et spécifications reçus, non modifiés |
| `docs/reviews/` | Rapports d'exécution et revues |

Le prototype Godot, `src/Bastion.Client.Godot/` (lot 1D), n'est pas dans `Bastion.slnx` : les commandes ci-dessous, lancées à la racine, ne le compilent pas. Sa compilation et son lancement sont décrits dans sa notice, `src/Bastion.Client.Godot/README.md`.

## Prérequis

- SDK .NET 10 (`global.json`).
- bash, git, sed et grep pour les hooks (Git Bash sous Windows).

## Commandes

```bash
dotnet build
dotnet test
dotnet format --verify-no-changes
bash scripts/harness/test-hooks.sh
```
