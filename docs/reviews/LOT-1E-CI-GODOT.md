# Bastion — Lot 1E : qualification automatisée du client Godot

**Date :** 23 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1E-v1.0-transcription.md`. C'est une transcription du message du propriétaire du 2026-11-23T07:07:24Z, extraite mécaniquement du journal de session (SHA-256 `19620b27…b695`) ; son identité avec un fichier original n'est pas vérifiée. Statut du texte : « préparé — en attente d'autorisation du propriétaire ».
**Autorisation d'exécution :** 2026-11-23T09:23:17Z. En réponse à une question de Claude Code, le propriétaire a choisi « Autoriser, push du lot (Recommandé) » : exécution du mandat, avec commits et pushes sur la seule branche du lot pour faire tourner la CI. Elle n'autorise ni PR ni fusion. La vérification négative se fait en local, dans des copies jetables, avec les commandes de la CI.
**Base :** `origin/main` = `535bcaeba84c1769da13817946a596943ca471f1` (fusion de la PR #22), établie par `git fetch origin main` au démarrage et revérifiée avant la rédaction de ce rapport.
**Branche :** `claude/lot-1e-ci-godot`, créée à partir de `origin/main`.
**État :** lot exécuté.
- Le premier commit, `a39b2562dbaaf9af6c9482fdbd18325865a3afb4` (workflow, notice, archive du mandat), est poussé sur la branche du lot, et sa CI est verte (run 45148037933).
- Un second commit ajoute ce rapport, celui de la relecture, et la correction de la notice demandée par la relecture (RX-02). Ce rapport ne peut pas citer le SHA ni la CI du commit qui le contient : ils sont donnés au propriétaire dans le message de fin de lot.
- **Aucune PR n'est ouverte, rien n'est fusionné.**

## 1. Résumé

La CI existante contrôle désormais le client `Bastion.Client.Godot`, par six étapes ajoutées à la fin du job `build-test` :
1. restauration ;
2. compilation Release ;
3. format ;
4. installation de Godot 4.7.2 stable .NET, depuis la publication officielle, vérifiée par son empreinte SHA-512 ;
5. compilation Debug ;
6. contrôle fumée en mode headless, limité à 300 s.

Les étapes existantes ne sont pas modifiées. Le client reste hors de `Bastion.slnx`. Aucune action GitHub n'est ajoutée : `curl`, `sha512sum` et `unzip` suffisent.

**Résultats observés :**
- **CI réelle** (run 45148037933, sur le commit `a39b256`) : réussie. Le contrôle fumée s'y exécute vraiment : on lit dans le journal ses 21 lignes « SMOKE OK », « SMOKE : RÉUSSITE » puis « Contrôle fumée réussi (code 0). ».
- **Rejeu local** des six étapes, dans un clone neuf : code 0 partout (shell : voir §4.1).
- **Vérifications négatives**, dans des copies jetables : cinq défauts introduits ; chacun fait échouer l'étape visée, avec son code (1, 2 ou 124).
- **Non-régression :** 46 tests sur 46 et 75 tests des hooks, en local et dans la CI.

**Notice du client** mise à jour : périmètre désormais contrôlé par la CI, et les six essais macOS déclarés conformes par le propriétaire, présentés comme un retour d'utilisateur.

**Relecture indépendante ciblée :** « conforme sous réserves », sans constat bloquant. Les quatre constats à corriger (RX-01 à RX-04) sont traités ; les quatre observations (RX-05 à RX-08) sont reportées en limites ou en points à décider (§6).

**Non vérifié :**
- le chemin `pull_request` de la CI : aucune PR n'est autorisée ;
- l'affichage et l'export du client en CI : la CI ne fait ni l'un ni l'autre ;
- Windows ;
- une reproduction indépendante sous macOS.

## 2. Fichiers

| Fichier | Rôle | Changement |
|---|---|---|
| `.github/workflows/ci.yml` | workflow CI : en-tête complété et six étapes du client ajoutées à la fin du job | +43 −1 |
| `src/Bastion.Client.Godot/README.md` | notice du client : périmètre contrôlé par la CI, essais macOS déclarés, limites, sens du code 124 (RX-02) | +33 −9 |
| `docs/mandates/BASTION-MANDAT-LOT-1E-v1.0-transcription.md` | mandat archivé (transcription) | 53 lignes, nouveau |
| `docs/mandates/README.md` | une ligne d'index ajoutée : provenance, statut, empreinte | +1 |
| `docs/reviews/LOT-1E-CI-GODOT.md` | ce rapport | nouveau |
| `docs/reviews/LOT-1E-CI-GODOT-RELECTURE.md` | rapport de la relecture indépendante ciblée | nouveau |

Les changements sont ceux de `git diff --numstat origin/main`, relevés avant le second commit, sans compter les deux rapports.

Le premier commit `a39b256` portait « +32 −8 » sur la notice. La correction RX-02 y ajoute une ligne remplacée. Au total : 4 fichiers, 130 insertions et 10 suppressions, plus les deux rapports.

**Fichiers inchangés :**
- le code du client : `PrototypeScene.cs`, `SmokeTest.cs`, `Main.tscn`, `project.godot`, `Bastion.Client.Godot.csproj` ;
- le moteur `src/Bastion.Simulation/` et les tests `tests/Bastion.Simulation.Tests/` ;
- `Bastion.slnx`, `Directory.Build.props` et `global.json` ;
- le harnais (`.claude/`, `scripts/harness/`) et `CLAUDE.md` ;
- les registres `docs/gameplay`, `docs/decisions` et `docs/references`.

## 3. Conception

### 3.1 Ordre des étapes

Les six étapes du client viennent après toutes les étapes existantes. Un échec du client ne masque donc aucun contrôle antérieur ; chaque étape échoue si sa commande renvoie un code non nul.

| Étape | Commande | Raison |
|---|---|---|
| restauration | `dotnet restore src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` | le client n'est pas dans `Bastion.slnx`, donc pas restauré par l'étape existante |
| compilation Release | `dotnet build … --no-restore --configuration Release` | critère « sans avertissement ni erreur » : `TreatWarningsAsErrors` de `Directory.Build.props` s'applique au client. Il transforme en erreurs les avertissements du compilateur C#, mais pas ceux de MSBuild ni du SDK (RX-06) : voir §7 |
| format | `dotnet format … --verify-no-changes --no-restore` | même contrôle que pour la solution |
| installation de Godot | téléchargement, `sha512sum -c`, `unzip`, `--headless --version` | voir §3.2 |
| compilation Debug | `dotnet build … --no-restore` | Godot charge la compilation Debug quand il lance le projet depuis son dossier (constaté au lot 1D) |
| contrôle fumée | `timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test` | voir §3.3 |

### 3.2 Installation et intégrité

- **Source :** `https://github.com/godotengine/godot/releases/download/4.7.2-stable/Godot_v4.7.2-stable_mono_linux_x86_64.zip`, la publication officielle de la version épinglée par T-002.
- **Intégrité :** l'empreinte SHA-512 est écrite en clair dans le workflow et vérifiée par `sha512sum -c`. Une empreinte fausse arrête l'étape (§4.2). Cette empreinte a été relevée au lot 1C, et elle est égale à celle du fichier `SHA512-SUMS.txt` de la publication.
- **Version :** `--headless --version` affiche la version installée dans le journal (`4.7.2.stable.mono.official.ed1daf0bf`). Le contrôle fumée revérifie lui-même 4.7.2 stable au lancement.
- **Chemin du binaire :** il est transmis aux étapes suivantes par `$GITHUB_ENV` (variable `GODOT`). Il n'y a ni cache ni action tierce.

### 3.3 Codes de sortie et délai

L'étape du contrôle fumée capture le code de sortie, affiche un message qui dépend du code, puis sort avec ce même code :

| Code | Signification | Message |
|---|---|---|
| 0 | tous les contrôles réussissent | « Contrôle fumée réussi (code 0). » |
| 1 | au moins un contrôle échoue | `::error::Contrôle fumée : échec (code 1).` |
| 2 | exception dans le contrôle | `::error::Contrôle fumée : échec (code 2).` |
| 124 | `timeout` a dû arrêter Godot après 300 s | `::error::Contrôle fumée : délai de 300 s dépassé (code 124). La scène n'a pas terminé ; ce n'est pas un échec fonctionnel détecté.` |

Tout code non nul fait échouer l'étape, y compris 124. Le message 124 dit seulement que Godot n'a pas quitté dans le délai ; il ne prétend pas qu'un contrôle a échoué. Le délai de 300 s est le même qu'au lot 1D, alors que l'exécution réelle prend moins d'une seconde en CI.

## 4. Commandes et résultats

### 4.1 Rejeu local des étapes du client

Le script `rejouer-ci.py`, dans le dossier temporaire de la session, lit `ci.yml` avec PyYAML et exécute le bloc `run` de chaque étape « Client Godot ». Il les lance par `bash --noprofile --norc -eo pipefail -c`, et il émule `RUNNER_TEMP` et `GITHUB_ENV`.

Ce n'est pas exactement le shell du runner (RX-01). Sans `shell:` explicite, le journal de la CI montre `bash -e {0}` : un fichier de script, sans `pipefail`. La relecture a rejoué les étapes avec `bash -e <fichier>`. Elle a aussi comparé les deux shells sur le bloc du contrôle fumée, avec un faux binaire qui renvoie 0, 1, 2, 124, 137 et 255. Les résultats sont identiques. Sans `pipefail`, le pipe `echo … | sha512sum -c -` échoue quand même, car `sha512sum` est sa dernière commande.

Le rejeu s'est fait dans un clone neuf de `origin/main` (`535bcae`), sans dossier `.godot` ni import préalable. Seul `ci.yml` y est modifié, et il est identique à celui du commit (SHA-256 `68584c25…06bb`). `PrototypeScene.cs` et `SmokeTest.cs` sont identiques à ceux de la branche.

```
== Client Godot — restauration : code 0
== Client Godot — compilation Release : code 0
        0 Warning(s)
        0 Error(s)
== Client Godot — format : code 0
== Client Godot — installation de Godot 4.7.2 stable .NET : code 0
    …/runner/Godot_v4.7.2-stable_mono_linux_x86_64.zip: OK
    4.7.2.stable.mono.official.ed1daf0bf
== Client Godot — compilation Debug : code 0
        0 Warning(s)
        0 Error(s)
== Client Godot — contrôle fumée (headless) : code 0
    SMOKE : RÉUSSITE
    Contrôle fumée réussi (code 0).
TOUTES LES ÉTAPES DU CLIENT : code 0
```

L'archive a été téléchargée depuis la publication officielle, par le même `curl` que la CI.

### 4.2 Vérifications négatives (copies jetables)

Le script `negatifs.sh` crée un clone jetable par cas, depuis `origin/main`, et y copie le `ci.yml` du lot. Il y introduit un seul défaut, puis rejoue les étapes du client avec `rejouer-ci.py`. Les clones sont supprimés à la fin. Le dépôt de travail n'est jamais touché.

| Défaut introduit | Étape en échec | Code | Sortie observée |
|---|---|---|---|
| `StartTu = 21` au lieu de 20 (`PrototypeScene.cs`) | contrôle fumée | 1 | « SMOKE : ÉCHEC (2 contrôle(s)) », `::error::Contrôle fumée : échec (code 1).` |
| indentation de 6 espaces au lieu de 4 (`PrototypeScene.cs`, ligne 13) | format | 2 | `PrototypeScene.cs(13,5): error WHITESPACE` |
| variable `int unused = 0;` inutilisée | compilation Release | 1 | `error CS0219: The variable 'unused' is assigned but its value is never used` ; « 0 Warning(s), 1 Error(s) » |
| empreinte SHA-512 altérée (premier caractère `1` → `0`) | installation de Godot | 1 | « …zip: FAILED », « WARNING: 1 computed checksum did NOT match » |
| `Quit(…)` final remplacé par `_ = failures;` (`SmokeTest.cs`) | contrôle fumée | 124 | « SMOKE : RÉUSSITE », puis `::error::Contrôle fumée : délai de 300 s dépassé (code 124). La scène n'a pas terminé ; ce n'est pas un échec fonctionnel détecté.` |

À chaque fois, les étapes antérieures réussissent et le rejeu s'arrête à l'étape visée, comme la CI.

Le premier rejeu n'affichait que les quatre dernières lignes de chaque étape. Le texte de l'erreur CS0219 a donc été obtenu par une compilation séparée du même défaut, qui a aussi renvoyé le code 1.

Le dernier cas montre la différence entre délai et échec fonctionnel : tous les contrôles ont réussi, mais Godot n'a pas quitté. L'étape échoue avec le code 124 et un message qui ne parle pas de contrôle échoué. Le journal des cinq cas s'est terminé à 09:31:34 UTC, environ six minutes et demie après le rejeu du §4.1 (09:25:06 UTC). C'est cohérent avec une attente complète de 300 s, mais la durée de ce cas n'a pas été mesurée à part.

### 4.3 CI réelle sur la branche du lot

- **Run :** https://github.com/mengpo1/bastion/actions/runs/45148037933 (événement `push`, tentative 1).
- **Commit :** `a39b2562dbaaf9af6c9482fdbd18325865a3afb4`.
- **Job :** `build-test` (137602095716), sous `ubuntu-24.04` (image 20261116.133.1), de 09:32:57 à 09:33:45 UTC.
- **Conclusion :** `success`.

Résultat des étapes, lu par l'API publique de GitHub :

| N° | Étape | Résultat | Début → fin (UTC) |
|---|---|---|---|
| 4 | Restauration | success | 09:33:05 → 09:33:14 |
| 5 | Compilation | success | 09:33:14 → 09:33:19 |
| 6 | Format | success | 09:33:19 → 09:33:30 |
| 7 | Tests .NET | success | 09:33:30 → 09:33:31 |
| 8 | Tests des hooks | success | 09:33:31 → 09:33:32 |
| 9 | Traçabilité simulation (PR) | skipped (événement `push`) | — |
| 10 | Traçabilité simulation (hors PR) | success | 09:33:32 → 09:33:32 |
| 11 | Client Godot — restauration | success | 09:33:32 → 09:33:34 |
| 12 | Client Godot — compilation Release | success | 09:33:34 → 09:33:35 |
| 13 | Client Godot — format | success | 09:33:35 → 09:33:39 |
| 14 | Client Godot — installation de Godot 4.7.2 stable .NET | success | 09:33:39 → 09:33:42 |
| 15 | Client Godot — compilation Debug | success | 09:33:42 → 09:33:43 |
| 16 | Client Godot — contrôle fumée (headless) | success | 09:33:43 → 09:33:43 |

Extraits du journal du job :

```
Passed!  - Failed:     0, Passed:    46, Skipped:     0, Total:    46, Duration: 269 ms - Bastion.Simulation.Tests.dll (net10.0)
== 75 tests, 0 échec(s) ==
  Bastion.Client.Godot -> /home/runner/work/bastion/bastion/src/Bastion.Client.Godot/.godot/mono/temp/bin/Release/Bastion.Client.Godot.dll
Build succeeded.
    0 Warning(s)
    0 Error(s)
/home/runner/work/_temp/Godot_v4.7.2-stable_mono_linux_x86_64.zip: OK
4.7.2.stable.mono.official.ed1daf0bf
  Bastion.Client.Godot -> /home/runner/work/bastion/bastion/src/Bastion.Client.Godot/.godot/mono/temp/bin/Debug/Bastion.Client.Godot.dll
Build succeeded.
    0 Warning(s)
    0 Error(s)
Godot Engine v4.7.2.stable.mono.official.ed1daf0bf - https://godotengine.org
SMOKE OK : version de Godot épinglée 4.7.2 stable (4.7.2-stable (official))
SMOKE OK : carte de 5 × 5 cases de 1500 mm, case infranchissable (3,2), unité de 600 × 600 × 1800 mm (StandardHuman attendue)
SMOKE OK : état initial (1,4), N, 20 TU, 10 d'énergie : (1,4), N, 20 TU, 10 d'énergie
SMOKE OK : zone affichée = zone du moteur (22 cases)
SMOKE OK : panneau conforme à l'état initial
SMOKE OK : clic sur (2,4) = résultat d'ExecuteOrder : (2,4), E, 16 TU, 8 d'énergie (Destination (2,4) atteinte.)
SMOKE OK : arrivée en (2,4), E, 16 TU, 8 d'énergie
SMOKE OK : panneau conforme à l'état après le 1er ordre
SMOKE OK : (3,2) et (4,0) sont hors de la zone du moteur
SMOKE OK : clic sur la case de l'unité : état inchangé (Ordre refusé : la destination (2,4) n'appartient pas à la zone atteignable.)
SMOKE OK : clic à droite de la carte : état inchangé (Clic hors de la carte : aucun ordre transmis.)
SMOKE OK : clic sur la case infranchissable (3,2) : état inchangé (Ordre refusé : la destination (3,2) n'appartient pas à la zone atteignable.)
SMOKE OK : clic à gauche de la carte : état inchangé (Clic hors de la carte : aucun ordre transmis.)
SMOKE OK : clic sur la case hors zone (4,0) : état inchangé (Ordre refusé : la destination (4,0) n'appartient pas à la zone atteignable.)
SMOKE OK : panneau conforme à l'état après les clics refusés
SMOKE OK : (2,2) est dans la zone du moteur après le 1er ordre
SMOKE OK : 2e ordre vers (2,2), débité du coût du chemin du moteur : (2,2), N, 8 TU, 4 d'énergie
SMOKE OK : zone recalculée depuis le nouvel état (19 puis 10 cases)
SMOKE OK : panneau conforme à l'état après le 2e ordre
SMOKE OK : touche R : état initial restitué ((1,4), N, 20 TU, 10 d'énergie)
SMOKE OK : panneau conforme à l'état après la touche R
SMOKE : RÉUSSITE
Contrôle fumée réussi (code 0).
```

**Différence avec le local :** la CI utilise le SDK .NET 10.0.404 (« .NET Core SDK with version '10.0.404' is already installed »), et la machine locale le 10.0.115. Les deux respectent `global.json` (`10.0.100`, `rollForward: latestFeature`), et les deux donnent 0 avertissement.

### 4.4 Non-régression (dépôt de travail, local)

| Commande | Code | Résultat |
|---|---|---|
| `dotnet restore` | 0 | « All projects are up-to-date for restore. » |
| `dotnet build --no-restore --configuration Release` | 0 | 0 Warning(s), 0 Error(s) |
| `dotnet test --no-build --configuration Release` | 0 | « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » |
| `dotnet format --verify-no-changes --no-restore` | 0 | aucune sortie |
| `bash scripts/harness/test-hooks.sh` | 0 | « == 75 tests, 0 échec(s) == » |

La CI réelle (§4.3) donne les mêmes résultats sur les mêmes contrôles.

### 4.5 Vérifications refaites après la correction de la notice (RX-02)

La correction RX-02 change une ligne de `src/Bastion.Client.Godot/README.md` (`git diff --stat` : 1 insertion, 1 suppression). Toutes les commandes ci-dessous ont été relancées dans le dépôt de travail et renvoient le code 0.

| Commande | Résultat |
|---|---|
| `dotnet restore` | — |
| `dotnet build --no-restore --configuration Release` | 0 Warning(s), 0 Error(s) |
| `dotnet test --no-build --configuration Release` | « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » |
| `dotnet format --verify-no-changes --no-restore` | aucune sortie |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |
| `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --configuration Release` | 0 Warning(s), 0 Error(s) |
| `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes --no-restore` | aucune sortie |

Le contrôle fumée n'a pas été relancé en local après cette correction : aucun fichier compilé ni chargé par Godot n'a changé. La CI du second commit le relancera.

## 5. Essais manuels sous macOS (retour du propriétaire)

Le 23 novembre 2026, le propriétaire a déclaré conformes six essais manuels du prototype sous macOS. Il a confirmé cette liste en réponse à une question de Claude Code (« Oui, ces six essais ») :

1. lancement de la scène et affichage de la grille ;
2. état initial (1,4), N, 20 TU, 10 d'énergie, et zone atteignable affichée ;
3. clic sur (2,4), qui donne (2,4), E, 16 TU et 8 d'énergie ;
4. clic sur une case bloquée et sur une case hors zone, sans effet ;
5. deux ordres successifs, avec la zone mise à jour entre les deux ;
6. touche R, qui restaure l'état initial.

**C'est un retour d'utilisateur, et non une reproduction indépendante.** La version de macOS, l'architecture du processeur et les commandes exactes ne sont pas connues ici. Claude Code n'a exécuté aucun essai sous macOS. La notice du client le dit dans les mêmes termes. Le chemin `/Applications/Godot_mono.app/Contents/MacOS/Godot`, le contrôle fumée en ligne de commande et `gtimeout` y restent marqués comme non vérifiés.

## 6. Relecture indépendante ciblée

Un agent distinct du développeur a relu le commit `a39b256` et une première version de ce rapport. Son rapport est copié sans modification dans `docs/reviews/LOT-1E-CI-GODOT-RELECTURE.md`.

**Ce qu'il a exécuté lui-même :**
- lecture du run 45148037933 et du journal du job par l'API publique ;
- vérification de l'empreinte dans le fichier `SHA512-SUMS.txt` de la publication ;
- recalcul des empreintes SHA-256 ;
- non-régression ;
- un rejeu des étapes du client avec `bash -e <fichier>` ;
- huit cas jetables, dont sept nouveaux. Il a obtenu le code 2 pour une exception dans le contrôle et pour une scène qui ne s'initialise pas, et le code 124 en 300,0 s sans compilation Debug. L'installation a échoué sur un HTTP 404, sur une archive absente et sur une archive tronquée.

**Verdict :** « conforme sous réserves », sans constat bloquant. Il ne s'accorde pas la validation finale.

| Constat | Classement | Traitement |
|---|---|---|
| RX-01 : le rejeu local n'utilisait pas exactement le shell du runner (`bash -e {0}`), contrairement à ce que disait le rapport | à corriger | **corrigé** : §1 et §4.1 rectifiés. L'équivalence est établie par la relecture. |
| RX-02 : la notice réduisait le code 124 à « la scène n'a pas démarré le contrôle » | à corriger | **corrigé** dans `src/Bastion.Client.Godot/README.md` : Godot n'a pas quitté dans le délai, et ce n'est pas un contrôle en échec. Trois causes possibles : scène non démarrée, contrôle bloqué, ou contrôle terminé sans que Godot quitte. |
| RX-03 : répartition des lignes de la notice fausse (« +31 −9 » au lieu de « +32 −8 ») | à corriger | **corrigé** au §2, avec le nouveau décompte après RX-02 |
| RX-04 : « même délai qu'aux lots 1C et 1D » : rien ne l'établit pour le lot 1C | à corriger | **corrigé** : « le même qu'au lot 1D » |
| RX-05 : le commentaire du `.csproj` du client dit encore « Hors de Bastion.slnx et de la CI ». Le `README.md` racine dit, depuis le lot 1D, que l'interface Godot n'existe pas encore. | observation | **non modifié**, laissé à la décision du propriétaire (§9). Le mandat ne demande que la notice du client, et le `.csproj` fait partie du prototype. |
| RX-06 : les avertissements de MSBuild ou du SDK ne font pas échouer les compilations, ni celles du client ni celle de la racine | observation | **non modifié** : formulation nuancée au §3.1, limite au §7, point à décider au §9 |
| RX-07 : si Godot ignorait SIGTERM, `timeout 300` ne le borne pas, faute de `-k` ou de `timeout-minutes` | observation | **non modifié**, déjà déclaré au §7 ; point à décider au §9 |
| RX-08 : sur une PR, chaque modification de la description relance aussi le téléchargement de Godot et le contrôle fumée | observation | **non modifié**, ajouté au §7 |

La correction RX-02 ne touche que la notice : aucun code, aucun workflow. Les vérifications refaites après elle sont au §4.5.

## 7. Limites et contrôles non exécutés

- **Chemin `pull_request` :** les étapes du client s'exécutent sans condition, donc aussi sur une PR, mais aucune PR n'est autorisée par le mandat. Le run du §4.3 est un `push` : l'étape « Traçabilité simulation (PR) » y est sautée par sa condition, comme avant le lot.
- **Affichage :** la CI lance Godot en mode headless. Le dessin de la grille, de la zone et de l'unité n'y est pas contrôlé ; seules les captures sous Xvfb du lot 1D le montrent, en local.
- **Export :** aucun export du jeu n'est fait ni testé.
- **Windows :** aucun essai.
- **macOS :** six essais déclarés par le propriétaire, non reproduits (§5).
- **Écran réel sous Linux :** jamais essayé.
- **Intégrité :** l'empreinte SHA-512 est épinglée dans le workflow. Elle garantit que l'archive est celle relevée au lot 1C ; aucune signature cryptographique de l'éditeur n'est vérifiée.
- **Dépendance réseau :** l'étape d'installation dépend de la disponibilité de `github.com` et de ses téléchargements de publications (`curl --retry 3`). Une indisponibilité ferait échouer la CI sans défaut du client.
- **Code 124 :** il signale que Godot n'a pas quitté dans le délai, sans dire pourquoi. Le cas a été vérifié avec un contrôle qui ne quitte jamais (§4.2). Godot s'y est arrêté au signal SIGTERM de `timeout`. Un Godot qui ignorerait ce signal n'est pas couvert ; la CI serait alors bornée par la limite de durée par défaut du job.
- **SDK :** la CI et le local n'utilisent pas le même correctif du SDK .NET 10 (§4.3).
- **Avertissements hors compilateur (RX-06) :** `TreatWarningsAsErrors` ne s'applique qu'aux avertissements du compilateur C#. Un avertissement de MSBuild ou du SDK laisse la compilation en code 0 ; la relecture l'a constaté avec un `<Warning>` ajouté au `.csproj`. Le critère « sans avertissement » est respecté sur le commit relu (0 Warning(s) en Release et en Debug). La CI ne l'impose cependant pas pour ces avertissements-là. L'étape « Compilation » de la racine, qui existait avant le lot, a la même limite.
- **Déclencheur `edited` (RX-08) :** sur une PR, chaque modification de la description relance tout le job : le téléchargement de l'archive Godot (107 698 034 octets) et le contrôle fumée compris.

## 8. Conformité au mandat

| Exigence du mandat | Réalisation | Preuve |
|---|---|---|
| §2.1 restauration, compilation, format du client dans la CI | étapes 11, 12, 13 | §4.3 |
| §2.2 Godot 4.7.2 stable .NET officiel, intégrité, sans action tierce | étape 14 : `curl`, `sha512sum -c`, `unzip` | §3.2, §4.2 (empreinte fausse), §4.3 |
| §2.3 compilation Debug avant le contrôle fumée | étape 15 avant l'étape 16 | §4.3 |
| §2.4 limite de temps explicite | `timeout 300` | §3.3, §4.2 (code 124) |
| §2.5 tout code non nul échoue, 124 compris ; délai distinct d'un échec fonctionnel | `exit "$code"` et messages distincts | §3.3, §4.2 |
| §2.6 vérifications existantes conservées | étapes 4 à 10 inchangées | §4.3, diff de `ci.yml` |
| §2.7 six essais macOS, retour d'utilisateur | notice et §5 | `src/Bastion.Client.Godot/README.md` |
| §2.8 notice fidèle, sans extension à l'export ni à Windows | notice mise à jour | « Windows : aucun essai », « Export : aucun export de jeu n'est testé » |
| §3 pas de changement du prototype ni de la simulation | aucun fichier de code modifié | §2 |
| §3 client hors de `Bastion.slnx` | commandes ciblées sur le `.csproj` | §2, §3.1 |
| §3 registres protégés intacts | aucun fichier sous `docs/gameplay`, `docs/decisions`, `docs/references` | `git diff --stat` |
| §4 CI complète réussie sur la branche | run 45148037933 : `success` | §4.3 |
| §4 compilation sans avertissement ni erreur | 0 Warning(s), 0 Error(s), en Release et en Debug | §4.3 |
| §4 contrôle fumée réellement exécuté en CI, code 0, résultat observable | 21 lignes « SMOKE OK », « SMOKE : RÉUSSITE » | §4.3 |
| §4 vérification négative jetable | cinq défauts, cinq échecs | §4.2 |
| §4 pas de régression (46 tests, harnais) | 46/46, 75 tests des hooks | §4.3, §4.4 |
| §4 relecture indépendante ciblée | « conforme sous réserves », RX-01 à RX-04 corrigés | §6, `LOT-1E-CI-GODOT-RELECTURE.md` |
| §5 mandat archivé et indexé | transcription et ligne d'index | Annexe A |

## 9. Points à décider par le propriétaire

1. **Publication :** autoriser ou non l'ouverture d'une PR de `claude/lot-1e-ci-godot` vers `main`. Elle exécuterait aussi le chemin `pull_request` de la CI. La fusion demande une autorisation distincte.
2. **Signature de Godot :** se contenter de l'empreinte épinglée, ou demander plus tard un contrôle de signature, si la publication en fournit une. Ce serait un autre mandat.
3. **Textes devenus inexacts (RX-05) :**
   - le commentaire du `.csproj` du client, « Hors de Bastion.slnx et de la CI », est devenu faux avec ce lot ;
   - les deux phrases du `README.md` racine sur l'interface Godot sont fausses depuis le lot 1D.

   Faut-il les corriger, dans ce lot ou dans un autre ? Je ne les ai pas modifiés.
4. **Avertissements MSBuild (RX-06) :** faire échouer aussi les compilations sur les avertissements de MSBuild et du SDK (`-warnaserror` ou `MSBuildTreatWarningsAsErrors`), pour le client et pour la racine ? Ce serait un durcissement d'un contrôle existant, donc à arbitrer.
5. **Borne stricte du contrôle fumée (RX-07) :** ajouter `timeout-minutes` à l'étape, pour le cas d'un Godot qui ignorerait SIGTERM ? `timeout -k` ne conviendrait pas, car il changerait le code en 137.

## Annexe A — Empreintes SHA-256

| Fichier | Sur `origin/main` (`535bcae`) | Au commit `a39b256` | Après la correction RX-02 |
|---|---|---|---|
| `.github/workflows/ci.yml` | `e160e1d83fa4bd4541e78a4ef40003e1fd92f0219f7f6a92b3f9ac2d9249f55d` | `68584c2546e01624bfcb6afa13c5c8fdd809796ed535fd298732d9d3a56b06bb` | inchangé |
| `src/Bastion.Client.Godot/README.md` | `5198592713bf7f824dd9338b024cdee5682b69f2513281a0ec3123db069562b0` | `da52489e8dca67379f89499d771a424359d3bf65ddeaf391480e77dfadfb1a1f` | `43260f3c0eb911c41b936d82ed51b9efb5ac53f379cd7c075474a3b7d59c6b54` |
| `docs/mandates/README.md` | `6b4d65b31219d49174761391d39074efba5c422ce66c8f9f1bcbcae87ba7f4dd` | `8cd9953a75cc44bf1d01f501330111f35b42b3b7e1093960bcd59b2fb4cce7aa` | inchangé |
| `docs/mandates/BASTION-MANDAT-LOT-1E-v1.0-transcription.md` | absent | `19620b278e21c8743d02bb8888b5274f26366646456617330004a5c02d63b695` | inchangé |
| `docs/reviews/LOT-1E-CI-GODOT-RELECTURE.md` | absent | absent | `f3c022e8d05bf197ce5b96435698beb7d4aee7a3c369c85e8ff8ea0c17a27d4f` |
| `src/Bastion.Client.Godot/PrototypeScene.cs` | `62b2cce35de4a372352365e0714b7d85aeed62aec598189d1a549fd1e1675f27` | identique | identique |
| `src/Bastion.Client.Godot/SmokeTest.cs` | `eedf802f690c187e25b5c35665e5175a811ebd603ab1a4875670bfd4983fa207` | identique | identique |

Ce rapport ne peut pas porter sa propre empreinte.

Archive Godot vérifiée par la CI : `Godot_v4.7.2-stable_mono_linux_x86_64.zip`, SHA-512 `1855960b27ee3ef5e66e5e228cced69d55637b24334a7411162687dcd077d8f9f645348cdb8eae984bec8135d49ed855a1e3a16476786b8bce60774fd8402d13`.
