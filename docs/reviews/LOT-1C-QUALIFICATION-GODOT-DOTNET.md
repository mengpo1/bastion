# Bastion — Lot 1C : qualification technique de Godot .NET

**Date :** 22 novembre 2026
**Mandat :** « BASTION — Mandat 1C — Qualification technique Godot .NET », transmis par le propriétaire dans la conversation le 2026-11-22T16:26:36.985Z (horodatage du journal de session). Statut du mandat : « préparé — exécution à autoriser par le propriétaire ».
**Autorisation d'exécution :** 2026-11-22T16:40:18.276Z, en réponse à une question de Claude Code : le propriétaire a choisi « Autoriser l'exécution (Recommandé) ». Elle n'autorise ni commit, ni push, ni PR.
**Base :** `main` au commit `4cdd5e4cf989586b1d2a3e9c1fad075097398c50`, qui contient la fusion de la PR #20 ; contrôlée par `git fetch origin main`.
**Branche :** `claude/lot-1c-godot-qualification`, créée à partir de `origin/main`.
**État :** expérimentation terminée ; ce rapport est le seul fichier ajouté au dépôt. **Rien n'est commité ni publié.**

## 1. Conclusion

**Compatible, dans l'environnement vérifié.**
- Godot 4.7.2 .NET (`4.7.2.stable.mono.official.ed1daf0bf`) restaure et compile un projet C# en `net10.0` avec le SDK .NET 10.0.115, sans avertissement ni erreur.
- Ce projet référence `Bastion.Simulation` par une référence de projet, sans copie de son code.
- Exécuté par Godot en mode headless, sur le runtime .NET 10.0.15, le script appelle réellement la simulation : un pas E sur une carte de 3 × 3 cases amène l'unité de (1,1) à (2,1), avec 56 TU et 98 d'énergie. Le processus se termine avec le code 0.
- **Contrôle négatif :** le même script, réglé pour attendre volontairement 55 TU, se termine avec le code 1. Le code de sortie reflète donc bien le résultat.

Cette conclusion repose sur les exécutions réelles décrites ci-dessous, et non sur la documentation. Sa portée se limite à l'environnement testé (§7).

## 2. Versions exactes

| Élément | Version | Comment elle a été établie |
|---|---|---|
| Système | Ubuntu 24.04.5 LTS, noyau Linux 6.18.44, x86_64 (conteneur, sans affichage) | `uname -srm`, `/etc/os-release` |
| SDK .NET | 10.0.115, seul SDK installé | `dotnet --list-sdks` |
| Runtime .NET utilisé par Godot | .NET 10.0.15 | `RuntimeInformation.FrameworkDescription`, affiché par le script exécuté dans Godot |
| Godot | `4.7.2.stable.mono.official.ed1daf0bf` | `--version` et `--headless --version` du binaire |
| Archive Godot | `Godot_v4.7.2-stable_mono_linux_x86_64.zip`, 107 698 034 octets | téléchargée depuis la publication officielle `4.7.2-stable` du dépôt `godotengine/godot` sur GitHub |
| SHA-512 de l'archive | `1855960b27ee3ef5e66e5e228cced69d55637b24334a7411162687dcd077d8f9f645348cdb8eae984bec8135d49ed855a1e3a16476786b8bce60774fd8402d13` | `sha512sum -c` contre le fichier `SHA512-SUMS.txt` de la même publication : OK |
| SHA-256 du binaire | `fc1bd592b5e771c65d52968f99835b4f2b7fe7b7cbc141e202cb63e01c95ec4d` (`Godot_v4.7.2-stable_mono_linux.x86_64`, ELF 64 bits x86-64) | `sha256sum`, `file` |
| Paquets NuGet résolus | `Godot.NET.Sdk` 4.7.2, `GodotSharp` 4.7.2, `GodotSharpEditor` 4.7.2, `Godot.SourceGenerators` 4.7.2 | `project.assets.json` du projet de qualification ; cache NuGet |
| Cible du projet de qualification | `net10.0` | `project.assets.json` (cible unique `net10.0`) ; `runtimeconfig.json` (`tfm` `net10.0`, `Microsoft.NETCore.App` 10.0.0, `rollForward` `LatestMinor`) |
| Bastion | `main` au commit `4cdd5e4`, cible `net10.0` inchangée | copie de travail temporaire, `git rev-parse HEAD` |

## 3. Environnement et installation

Tout a été fait dans le dossier temporaire de la session, hors du dépôt : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/lot1c/`. Ce dossier contient :
- `dl/` : l'archive téléchargée ;
- `godot/` : son contenu extrait ;
- `bastion-copie/` : la copie de travail de Bastion ;
- `qualif/` : le projet Godot de qualification.

| Étape | Commande | Code | Résultat |
|---|---|---|---|
| Base | `git fetch origin main` ; `git merge-base --is-ancestor 702b055… origin/main` | 0 ; 0 | `main` = `4cdd5e4…`, contient la fusion de la PR #20 |
| Téléchargement | `curl -L -o Godot_v4.7.2-stable_mono_linux_x86_64.zip https://github.com/godotengine/godot/releases/download/4.7.2-stable/…` ; idem pour `SHA512-SUMS.txt` | 0 ; 0 | 107 698 034 octets ; 5 682 octets |
| Intégrité | `sha512sum -c` (ligne de l'archive dans `SHA512-SUMS.txt`) | 0 | « OK » |
| Extraction | `unzip` dans `godot/` | 0 | binaire `Godot_v4.7.2-stable_mono_linux.x86_64` et dossier `GodotSharp/` |
| Version | `Godot_v4.7.2-stable_mono_linux.x86_64 --version` | 0 | `4.7.2.stable.mono.official.ed1daf0bf` |
| Mode headless | `… --headless --version` | 0 | `4.7.2.stable.mono.official.ed1daf0bf` |

**Aucune installation système.**
- Le binaire n'a été ni copié dans un dossier système, ni ajouté au `PATH`.
- Aucune variable d'environnement n'a été définie : Godot a trouvé seul le runtime .NET installé.

En revanche, plusieurs écritures ont eu lieu hors du dossier temporaire, au niveau de l'utilisateur et non du système, dans ce conteneur éphémère :
- Godot a créé ses réglages et caches : `~/.config/godot/` (réglages de l'éditeur, créés par `--import`), `~/.cache/godot/` et `~/.local/share/godot/app_userdata/` ;
- la restauration NuGet a placé les quatre paquets Godot dans le cache `~/.nuget/packages/`.

Ces fichiers n'ont pas été supprimés.

## 4. Projet minimal et intégration de `Bastion.Simulation`

**Copie de travail temporaire de Bastion :**
- obtenue par `git clone` local du dépôt, puis `git checkout --detach 4cdd5e4…` ;
- elle n'est pas modifiée par l'expérience : `git status --porcelain` y est vide après la compilation, `bin/` et `obj/` étant ignorés.

**Projet Godot** (`qualif/`, hors du dépôt et de sa copie), composé de quatre fichiers, reproduits en annexe A :
- `project.godot` : scène principale `res://Main.tscn`, assemblage `BastionQualification` ;
- `BastionQualification.csproj` :
  - `Sdk="Godot.NET.Sdk/4.7.2"` ;
  - `TargetFramework` = `net10.0` ;
  - une seule référence, `ProjectReference` vers `../bastion-copie/src/Bastion.Simulation/Bastion.Simulation.csproj` ;
- `Main.cs` : le seul script C#, attaché à un nœud `Node` ;
- `Main.tscn` : la seule scène, un nœud portant ce script.

**Ce que fait le script**, au démarrage de la scène :
1. il crée une carte de 3 × 3 cases de 1 500 mm (`TacticalMapBuilder`) ;
2. il construit un `MovementModel` avec `MovementRules.Initial` et `UnitBody.StandardHuman` ;
3. il crée une unité en (1,1), orientée E, avec 60 TU et 100 d'énergie (`CreateState`) ;
4. il demande un pas vers l'est (`EvaluateStep`) ;
5. il vérifie l'arrivée en (2,1), avec 56 TU et 98 d'énergie ;
6. il affiche le résultat, puis quitte par `GetTree().Quit(code)`, avec le code 0 en cas de réussite, 1 en cas de résultat inattendu et 2 en cas d'exception.

Il n'y a ni interface graphique, ni animation, ni autre gameplay. Avec l'argument utilisateur `--controle-negatif`, le script attend volontairement 55 TU : c'est le contrôle négatif.

## 5. Preuve de compilation

| Étape | Commande (dans `qualif/`) | Code | Résultat |
|---|---|---|---|
| Restauration | `dotnet restore` | 0 | `Bastion.Simulation.csproj` et `BastionQualification.csproj` restaurés |
| Compilation | `dotnet build --no-restore` | 0 | `Bastion.Simulation -> …/bastion-copie/src/Bastion.Simulation/bin/Debug/net10.0/Bastion.Simulation.dll` ; `BastionQualification -> …/qualif/.godot/mono/temp/bin/Debug/BastionQualification.dll` ; « 0 Warning(s) », « 0 Error(s) » |
| Seconde compilation, après ajout de la ligne « environnement » au script | `dotnet build` | 0 | « 0 Warning(s) », « 0 Error(s) » |
| Assemblage embarqué | `sha256sum` de `Bastion.Simulation.dll` dans la sortie Godot et dans la copie de travail | 0 | identiques : `0f103b55a5c49edc310b1fa0dafde6ede9aa6451ade5c206776b43a314653885` |

`Bastion.Simulation` s'est compilé avec ses propres réglages (`Directory.Build.props` de la copie : `net10.0`, `TreatWarningsAsErrors`).

## 6. Preuve d'exécution depuis Godot

| Étape | Commande | Code | Résultat |
|---|---|---|---|
| Import du projet | `Godot_v4.7.2-stable_mono_linux.x86_64 --headless --path qualif --import` | 0 | import terminé |
| Exécution nominale | `… --headless --path qualif` | **0** | sortie ci-dessous |
| Contrôle négatif | `… --headless --path qualif -- --controle-negatif` | **1** | sortie ci-dessous |

Sortie complète de l'exécution nominale :

```
Godot Engine v4.7.2.stable.mono.official.ed1daf0bf - https://godotengine.org

BASTION-QUALIF environnement : .NET 10.0.15 ; Bastion.Simulation chargé depuis 
BASTION-QUALIF départ : (1,1), E, 60 TU, 100 d'énergie
BASTION-QUALIF pas E : accepté = True, refus = None, arrivée = (2,1), E, 56 TU, 98 d'énergie
BASTION-QUALIF attendu : (2,1), 56 TU, 98 d'énergie
BASTION-QUALIF : RÉUSSITE
```

Sortie complète du contrôle négatif :

```
Godot Engine v4.7.2.stable.mono.official.ed1daf0bf - https://godotengine.org

BASTION-QUALIF environnement : .NET 10.0.15 ; Bastion.Simulation chargé depuis 
BASTION-QUALIF départ : (1,1), E, 60 TU, 100 d'énergie
BASTION-QUALIF pas E : accepté = True, refus = None, arrivée = (2,1), E, 56 TU, 98 d'énergie
BASTION-QUALIF attendu : (2,1), 55 TU, 98 d'énergie (contrôle négatif)
BASTION-QUALIF : ÉCHEC
```

**Ce que montrent ces sorties :**
- la simulation s'exécute réellement dans le processus Godot, sur le runtime .NET 10.0.15 ;
- elle calcule le pas : il est accepté, l'unité arrive en (2,1), orientée E, avec 56 TU et 98 d'énergie, valeurs conformes au barème de `MEC-0003` (4 TU et 2 d'énergie par pas orthogonal sur terrain normal) ;
- le code de sortie distingue la réussite (0) de l'échec (1).

Aucun avertissement ni erreur n'apparaît dans ces journaux.

**Chemin de l'assemblage chargé.** La ligne « environnement » affiche un emplacement vide pour l'assemblage `Bastion.Simulation`. Explication probable, non vérifiée : Godot charge les assemblages du projet depuis la mémoire, par exemple pour permettre leur rechargement, et non depuis un fichier. Le lien entre l'assemblage exécuté et la copie de travail repose donc sur deux éléments : le fichier embarqué est identique à celui de la copie (§5), et les valeurs calculées correspondent au comportement de la simulation.

## 7. Contrôles côté Bastion

| Contrôle | Commande | Code | Résultat |
|---|---|---|---|
| Absence de dépendance Godot dans `Bastion.Simulation` | `project.assets.json` de `Bastion.Simulation` dans la copie, après la compilation par le projet Godot | 0 | aucun paquet ; cible unique `net10.0` |
| | recherche de « godot » dans les `.cs`, `.csproj` et `.props` de `src/Bastion.Simulation` de la copie | 0 | une seule occurrence : le commentaire du `.csproj`, « Ne doit jamais référencer Godot » |
| | test fumée `SimulationDoesNotReferenceGodot` (dans la suite ci-dessous) | 0 | réussi |
| Absence de modification des sources de Bastion | `git status --porcelain` dans le dépôt, avant et après l'expérience ; `git diff --quiet origin/main -- src tests` | 0 | 0 fichier modifié ; `src/` et `tests/` identiques à `origin/main` |
| | `git status --porcelain` dans la copie de travail | 0 | vide |
| Tests existants (dans le dépôt) | `dotnet restore` ; `dotnet build --configuration Release` | 0 ; 0 | 0 avertissement, 0 erreur |
| | `dotnet test --configuration Release` | 0 | 46 tests, 46 réussis |
| | `dotnet format --verify-no-changes` | 0 | aucun écart |
| | `bash scripts/harness/test-hooks.sh` | 0 | « 75 tests, 0 échec(s) » |

## 8. Difficultés rencontrées

Aucune difficulté bloquante :
- le téléchargement, la vérification d'intégrité, la restauration NuGet, la compilation et l'exécution ont réussi du premier coup ;
- aucune variable d'environnement n'a été nécessaire (`DOTNET_ROOT`, par exemple).

**Seul point notable :** l'emplacement vide de l'assemblage chargé (§6).

## 9. Limites de la vérification

### 9.1 Nature des constats

| Nature | Constats |
|---|---|
| **Contrôles exécutés, résultats observés** (commande lancée, sortie et code de sortie relevés) | intégrité SHA-512 de l'archive ; version du binaire, y compris en mode headless ; restauration et compilation du projet en `net10.0`, sans avertissement ; paquets et cible résolus ; empreinte identique de `Bastion.Simulation.dll` dans la sortie Godot et dans la copie de travail ; exécution par Godot, sur .NET 10.0.15, avec sortie 0 et valeurs (2,1), 56 TU, 98 d'énergie ; contrôle négatif, sortie 1 ; absence de paquet dans `Bastion.Simulation` ; sources de Bastion inchangées ; 46 tests sur 46 et 75 tests du harnais réussis |
| **Déductions tirées de ces observations** | l'assemblage exécuté par Godot est celui de la copie de travail (empreinte identique, valeurs calculées conformes) ; le code de sortie reflète le résultat du test (une exécution réussie, sortie 0 ; une exécution en échec, sortie 1) ; la compatibilité est démontrée dans l'environnement testé, et seulement dans celui-ci |
| **Hypothèse non vérifiée** | l'emplacement vide de l'assemblage chargé tiendrait à un chargement depuis la mémoire par Godot (§6) |
| **Non vérifié** | tout ce qu'énumère le §9.2 |

### 9.2 Ce qui n'est pas vérifié

- **Plateforme unique :** Linux x86_64, en conteneur, sans affichage. Windows, macOS, Linux ARM et l'exécution avec rendu graphique ne sont pas vérifiés.
- **Mode headless seulement :** l'éditeur graphique, le rendu, l'entrée et l'audio ne sont pas exercés.
- **Compilation par `dotnet build` :** la compilation lancée par l'éditeur Godot lui-même n'a pas été utilisée. L'exécution s'est faite depuis le projet, en configuration `Debug`.
- **Pas d'export :** aucun modèle d'export (« export templates ») n'est installé, et aucun export de jeu n'est testé. La compatibilité d'un jeu exporté en `net10.0` n'est donc pas vérifiée.
- **Intégrité, et non authenticité :** la somme SHA-512 vient du fichier publié avec la même version, sur la même page de publication. Elle établit l'intégrité du téléchargement par rapport à cette publication, mais aucune signature cryptographique n'a été vérifiée.
- **Un seul scénario :** l'intégration n'exerce qu'un pas E. Le reste de l'API de `Bastion.Simulation` (zone, chemins, rotations, diagonales) n'est appelé que par les tests xUnit, hors de Godot.
- **T-103 non examiné :** la cohabitation entre la solution `.slnx` de Bastion et un projet Godot placé dans le dépôt n'est pas testée, puisque le mandat exclut de créer ce projet dans le dépôt.
- **CI :** la CI de Bastion n'exécute pas Godot ; ce rapport ne la modifie pas.

## 10. Points à décider par le propriétaire

1. **Version de Godot.** Le registre technique (T-002) indique « Version de Godot à figer ». Ce rapport fournit les éléments d'une décision : version `4.7.2.stable.mono.official.ed1daf0bf`, compatible avec `net10.0` dans l'environnement testé. Il ne modifie pas le registre : la décision vous appartient.
2. **Réserve de T-101.** Le registre note « Compatibilité de `net10.0` avec Godot .NET toujours non vérifiée ». Sa mise à jour éventuelle relève aussi d'une décision distincte.
3. **Projet d'interface Godot.** Sa création, ainsi que ses conditions (T-002 figé, compatibilité vérifiée), relève d'un mandat ultérieur.
4. **Publication de ce rapport.** Commit, push de la seule branche `claude/lot-1c-godot-qualification` et PR en brouillon : elle attend votre autorisation distincte.

## Annexe A — Fichiers du projet de qualification (hors dépôt)

Les quatre fichiers sont reproduits tels qu'ils ont été exécutés. Le projet n'est pas ajouté au dépôt.

`project.godot` (SHA-256 `5ef3905bf0daa2b736574ec015b9a6a558c21335aa154c7cde4939a02d86966e`) :

```ini
; Projet de qualification temporaire (mandat 1C), hors du dépôt Bastion.
config_version=5

[application]

config/name="BastionQualification"
run/main_scene="res://Main.tscn"
config/features=PackedStringArray("4.7", "C#")

[dotnet]

project/assembly_name="BastionQualification"
```

`BastionQualification.csproj` (SHA-256 `ca518ff1afe2bb8d10c7cca072d7f6619b147f305c270543cbbe0c8662a80307`) :

```xml
<Project Sdk="Godot.NET.Sdk/4.7.2">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <EnableDynamicLoading>true</EnableDynamicLoading>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <ItemGroup>
    <!-- Référence au projet de la copie de travail temporaire : aucun code de Bastion n'est copié ici. -->
    <ProjectReference Include="../bastion-copie/src/Bastion.Simulation/Bastion.Simulation.csproj" />
  </ItemGroup>
</Project>
```

`Main.tscn` (SHA-256 `71d780e865be1ec22e0bb6ab6dbdd27b831dfbfd0bfebbbd5b02f79d3a027e71`) :

```
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://Main.cs" id="1_main"]

[node name="Main" type="Node"]
script = ExtResource("1_main")
```

`Main.cs` (SHA-256 `3b47a03584e83770ea51361a9f3ecb2fda997a516d16897a39d473bfd825cf0f`) :

```csharp
using System;
using System.Linq;
using Bastion.Simulation.Movement;
using Godot;

/// <summary>
/// Qualification 1C : exécute un pas E de Bastion.Simulation depuis Godot, puis quitte avec un code de sortie.
/// 0 = réussite, 1 = résultat inattendu, 2 = exception. L'argument utilisateur « --controle-negatif »
/// attend volontairement 55 TU, pour vérifier que l'échec produit bien un code non nul.
/// </summary>
public partial class Main : Node
{
    public override void _Ready()
    {
        GetTree().Quit(Run());
    }

    private static int Run()
    {
        try
        {
            bool negativeControl = OS.GetCmdlineUserArgs().Contains("--controle-negatif");
            int expectedTu = negativeControl ? 55 : 56;

            TacticalMap map = new TacticalMapBuilder(3, 3, 1500m).Build();
            var model = new MovementModel(map, MovementRules.Initial, UnitBody.StandardHuman);
            UnitState start = model.CreateState(new GridPosition(1, 1), Direction.E, 60, 100);
            StepOutcome outcome = model.EvaluateStep(start, Direction.E);
            UnitState end = outcome.State;

            bool ok = outcome.Accepted
                && end.Position == new GridPosition(2, 1)
                && end.Tu == expectedTu
                && end.Energy == 98;
            GD.Print($"BASTION-QUALIF environnement : {System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription} ; Bastion.Simulation chargé depuis {typeof(MovementModel).Assembly.Location}");
            GD.Print($"BASTION-QUALIF départ : {start.Position}, {start.Orientation}, {start.Tu} TU, {start.Energy} d'énergie");
            GD.Print($"BASTION-QUALIF pas E : accepté = {outcome.Accepted}, refus = {outcome.Refusal}, arrivée = {end.Position}, {end.Orientation}, {end.Tu} TU, {end.Energy} d'énergie");
            GD.Print($"BASTION-QUALIF attendu : (2,1), {expectedTu} TU, 98 d'énergie{(negativeControl ? " (contrôle négatif)" : string.Empty)}");
            GD.Print(ok ? "BASTION-QUALIF : RÉUSSITE" : "BASTION-QUALIF : ÉCHEC");
            return ok ? 0 : 1;
        }
        catch (Exception exception)
        {
            GD.PrintErr($"BASTION-QUALIF : EXCEPTION {exception}");
            return 2;
        }
    }
}
```
