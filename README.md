# Bastion

Projet de jeu en C# avec Godot .NET.

**État : lot 0B — harnais de développement uniquement. Aucun gameplay n'est implémenté.**

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
| `src/Bastion.Simulation/` | Simulation, indépendante de Godot (aucun gameplay à ce stade) |
| `tests/Bastion.Simulation.Tests/` | Tests xUnit (test fumée technique) |
| `scripts/harness/` | Hooks Claude Code, leurs tests et leurs limites |
| `.claude/settings.json` | Branchement des hooks |
| `.github/workflows/ci.yml` | Intégration continue |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | Registre des décisions de gameplay |
| `docs/decisions/TECHNICAL-DECISIONS.md` | Registre des décisions techniques |
| `docs/references/OXCE-BASELINE.md` | Référence OXCE (version à figer) |
| `docs/mandates/` | Mandats et spécifications reçus, non modifiés |
| `docs/reviews/` | Rapports d'exécution et revues |

Le projet Godot (interface) n'existe pas encore : voir `docs/decisions/TECHNICAL-DECISIONS.md`.

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
