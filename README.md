# Bastion

Projet de jeu en C# avec Godot .NET.

**État :**

- le harnais de développement est installé et opérationnel : hooks Claude Code, tests des hooks, intégration continue ;
- le premier incrément de gameplay, `MEC-0003` (marche sur terrain plat), est implémenté, testé et intégré à `main` (PR #19) ;
- la simulation C# comprend désormais la marche sur terrain plat ; `MEC-0001` et `MEC-0002` restent reportées ;
- l'interface Godot n'est pas encore créée.

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
