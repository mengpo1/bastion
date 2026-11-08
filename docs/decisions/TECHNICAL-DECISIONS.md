# Registre des décisions techniques

Registre protégé. Une décision ne passe au statut « Validée » qu'avec l'accord explicite du propriétaire, ou si elle provient d'un document qu'il a validé (source indiquée).

Statuts : **Validée**, **Proposée** (à valider, peut changer), **Rejetée**, **Remplacée**.

## Décisions issues de documents validés

| ID | Décision | Statut | Source |
|---|---|---|---|
| T-001 | La simulation est indépendante de Godot ; l'interface est un projet distinct. | Validée | Spécification `BASTION-HARNAIS-LOT-0A-v0.2.md` (validée le 8 nov. 2026), citée par le mandat LOT-0B §4.B. Le texte de la spécification n'est pas dans le dépôt. |
| T-002 | Moteur Godot .NET, langage C#. Version de Godot **à figer**. | Validée (version non figée) | Mandat LOT-0B §3.2 et §4.B. |

## Choix provisoires du lot 0B — à valider par le propriétaire

| ID | Choix | Statut | Raison | Risque / alternative |
|---|---|---|---|---|
| T-101 | SDK .NET 10 (`global.json` : `10.0.100`, `rollForward: latestFeature`) ; cible `net10.0` (dans `Directory.Build.props`). | Proposée | .NET 8 arrive en fin de support le 10 nov. 2026 ; .NET 10 est la version LTS en cours. SDK 10.0.114 vérifié dans l'environnement d'exécution du lot 0B. | Compatibilité de `net10.0` avec la version de Godot .NET retenue **non vérifiée**. Alternative : `net8.0`. |
| T-102 | Tests avec xUnit 2.9.3, `xunit.runner.visualstudio` 3.1.4, `Microsoft.NET.Test.Sdk` 17.14.1 (versions du modèle `dotnet new xunit` du SDK 10.0.114). | Proposée | Framework courant, fourni par le SDK. | xUnit v3 ou MSTest possibles. |
| T-103 | Solution au format `.slnx` (format par défaut du SDK 10). | Proposée | Lisible, format par défaut. | Outils anciens : `.sln`. Godot génère son propre `.sln` : à arbitrer lors de la création du projet Godot. |
| T-104 | Hooks Claude Code en bash (sans jq) : `scripts/harness/`. | Proposée | Bash est requis par Claude Code sous Windows (Git Bash) ; pas de dépendance supplémentaire. | Sans Git Bash sous Windows, les hooks ne fonctionnent pas. |
| T-105 | CI GitHub Actions : `ubuntu-24.04`, `actions/checkout@v7`, `actions/setup-dotnet@v6`. | Proposée | Le dépôt est sur GitHub ; versions majeures vérifiées le 8 nov. 2026. | — |
| T-106 | Noms de projets : `Bastion.Simulation`, `Bastion.Simulation.Tests`. | Proposée | Reflète l'architecture T-001. | Noms à confirmer avec la spécification v0.2. |

## Projets futurs (non créés)

| Projet | Rôle | Condition de création |
|---|---|---|
| Interface Godot .NET (nom à définir) | Interface du jeu ; référencera `Bastion.Simulation`. | Godot .NET installé, version figée (T-002) et compatibilité avec T-101 vérifiée. |
