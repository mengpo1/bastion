# Registre des décisions techniques

Registre protégé. Une décision ne passe au statut « Validée » qu'avec l'accord explicite et daté du propriétaire.

Statuts :

- **Validée** : décision définitive du propriétaire.
- **Arbitrée provisoirement** : choix retenu par le propriétaire, révisable ; ce n'est pas une validation définitive.
- **Exigence de mandat** : imposée par un mandat, à confirmer par le propriétaire.
- **Proposée** : à valider, peut changer.
- **Rejetée**, **Remplacée**.

**Aucune décision technique n'est au statut « Validée » à ce jour.**

Arbitrages du 8 novembre 2026 : mandat `LOT-0B-CLOTURE` v1.0 §4 et mandat `LOT-0C` v1.2 §2.5 (archivés dans `docs/mandates/`).

## Architecture et moteur

| ID | Décision | Statut | Source |
|---|---|---|---|
| T-001 | La simulation (C#) est indépendante de Godot ; l'interface est un projet distinct. | Arbitrée provisoirement (8 nov. 2026) | Mandat LOT-0B §4.B ; spécification v0.2 §5 ; arbitrage du 8 nov. 2026 (LOT-0C v1.2 §2.5). |
| T-002 | Moteur Godot .NET, langage C#. Version de Godot **à figer**. | Exigence de mandat | Mandat LOT-0B §3.2 et §4.B. |

## Choix techniques du lot 0B

| ID | Choix | Statut | Raison | Risque / alternative |
|---|---|---|---|---|
| T-101 | SDK .NET 10 (`global.json` : `10.0.100`, `rollForward: latestFeature`) ; cible `net10.0` (dans `Directory.Build.props`). | Arbitrée provisoirement (8 nov. 2026) | .NET 8 arrive en fin de support le 10 nov. 2026 ; .NET 10 est la version LTS en cours. SDK 10.0.114 en local, 10.0.403 en CI. | Compatibilité de `net10.0` avec Godot .NET **toujours non vérifiée** (aucun essai Godot au 8 nov. 2026). Alternative : `net8.0`. |
| T-102 | Tests avec xUnit 2.9.3, `xunit.runner.visualstudio` 3.1.4, `Microsoft.NET.Test.Sdk` 17.14.1 (versions du modèle `dotnet new xunit` du SDK 10.0.114). | Proposée | Framework courant, fourni par le SDK. | xUnit v3 ou MSTest possibles. |
| T-103 | Solution au format `.slnx` (format par défaut du SDK 10). | Arbitrée provisoirement (8 nov. 2026) | Lisible, format par défaut. | Outils anciens : `.sln`. Godot génère son propre `.sln` : à revoir lors de la création du projet Godot. |
| T-104 | Hooks Claude Code en bash (sans jq) : `scripts/harness/`. | Proposée | Bash est requis par Claude Code sous Windows (Git Bash) ; pas de dépendance supplémentaire. | Sans Git Bash sous Windows, les hooks ne fonctionnent pas. |
| T-105 | CI GitHub Actions : `ubuntu-24.04`, `actions/checkout@v7`, `actions/setup-dotnet@v6`. | Proposée | Le dépôt est sur GitHub ; versions majeures vérifiées le 8 nov. 2026. | — |
| T-106 | Noms de projets : `Bastion.Simulation`, `Bastion.Simulation.Tests`. | Proposée | Reflète l'architecture T-001. | Noms à confirmer avec la spécification v0.2. |
| T-107 | `TreatWarningsAsErrors` conservé, alertes de sécurité NuGet comprises. | Arbitrée provisoirement (8 nov. 2026) | Les alertes de dépendances restent un signal bloquant. | Une alerte publiée sur un paquet peut faire échouer la CI sans changement de code : la signaler, ne pas la masquer. |
| T-108 | Deux limites des hooks acceptées : faux positif bloquant sur une commande qui cite `rm -rf` ; dépendance Godot déclarée mais inutilisée non détectée par le test d'architecture. | Arbitrée provisoirement (8 nov. 2026) | Corrections jugées non nécessaires à ce stade. | À réexaminer si elles gênent ou masquent un défaut. |

## Projets futurs (non créés)

| Projet | Rôle | Condition de création |
|---|---|---|
| Interface Godot .NET (nom à définir) | Interface du jeu ; référencera `Bastion.Simulation`. | Godot .NET installé, version figée (T-002) et compatibilité avec T-101 vérifiée. |
