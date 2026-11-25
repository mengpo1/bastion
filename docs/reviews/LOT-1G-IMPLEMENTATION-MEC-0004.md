# Bastion — Lot 1G : implémentation de MEC-0004

**Date :** 24 novembre 2026 ; finalisation le 25 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1G-v1.0-transcription.md`. C'est une transcription du message du propriétaire du 2026-11-24T19:42:22Z, extraite mécaniquement du journal de session (SHA-256 `c792934e…11b1`) ; son identité avec un fichier original n'est pas vérifiée. Statut du texte : « PRÉPARÉ — exécution non autorisée ».
**Autorisation d'exécution :** 2026-11-24T19:44:40Z. En réponse à une question de Claude Code, le propriétaire a choisi « Autoriser, avec Xvfb (Recommandé) » : exécution locale, avec des captures du scénario 4 sous affichage virtuel. Ces captures sont un rendu automatisé, et non une validation manuelle. L'autorisation n'ouvre ni commit, ni push, ni PR.
**Autorisation formelle :** message « BASTION — LOT-1G v1.0 — Autorisation d'exécution » du 2026-11-24T20:05:26Z. Il concorde avec la précédente : exécution locale, sans commit, push, PR ni fusion, et arrêt avant toute publication.
**Finalisation :** message « BASTION — LOT-1G — Finalisation avant publication » du 2026-11-25T12:17:17Z, après examen du compte rendu par l'orchestrateur.
- **Arbitrages :** fenêtre de 720 pixels conservée ; message de la touche R conservé, jugé conforme à MEC-0004 ; titre du panneau du lot 1F dans les scénarios 1 à 3, « Bastion — banc d'essai MEC-0004 (lot 1G) » dans le scénario 4, sans autre changement du panneau.
- **Demandes :** vérifications finales, relecture indépendante ciblée des corrections, rapport et empreintes actualisés, aucun refactoring supplémentaire.
- **Interdits :** aucun commit, push ni PR ; fiche MEC-0004 et registres protégés inchangés.
**Référence normative :** la fiche `MEC-0004` de `docs/gameplay/GAMEPLAY-DECISIONS.md`, acceptée le 23 novembre 2026 et intégrée dans `main` par la PR #25.
**Base :** `origin/main` = `1fa2769e309ea74390b678836d3203a16f7e66d4`, établie par `git fetch origin main` au démarrage.
**Branche :** `claude/lot-1g-implementation-mec-0004`, créée localement à partir de `origin/main`.
**État :** lot exécuté, relu, finalisé selon les arbitrages, relu une seconde fois et vérifié localement. **Rien n'est commité ni publié.**

## 1. Résumé

**Moteur.** `Bastion.Simulation` gagne un petit espace de noms `Turns`, sans toucher au moteur de marche de MEC-0003. Il contient trois types immuables :
- `TurnRules` : quatre paramètres validés (profil initial `TurnRules.Initial` : 60, 60, 100, 20) et trois opérations, `Start`, `WithUnit` et `EndTurn` ;
- `TurnState` : le numéro de tour et l'état `UnitState` de l'unité ;
- `TurnOutcome` : les états avant et après, les récupérations effectives et le compte rendu.

La fin de tour applique `min(courante + récupération, plafond)` à chaque ressource, sur 64 bits pour éviter tout débordement. Elle incrémente le tour et conserve la position et l'orientation.

**Client.** Le prototype Godot gagne un scénario 4 :
- la carte du scénario 1 ; (1,4), N ; 12 TU, 35 d'énergie ; tour 1 ;
- la touche 4 le charge, y compris sur un clavier AZERTY, et la touche T termine le tour ;
- le numéro de tour ne s'affiche que dans ce scénario ;
- le panneau y porte le titre « Bastion — banc d'essai MEC-0004 (lot 1G) » ; les scénarios 1 à 3 gardent exactement celui du lot 1F ;
- la scène ne fait aucun calcul de récupération : elle passe par `TurnRules`.

**Tests.** Les seize tests T01 à T16 de la fiche sont couverts :
- **par 19 tests xUnit** pour le moteur : T01 à T09, T14, T15, plus quatre tests complémentaires (immutabilité, compte rendu, profil, conservation du tour par `WithUnit`) ;
- **par le contrôle fumée** du client, avec de vrais événements Godot : T05, T10 à T13 et T16. T05 est couvert des deux côtés.

**Résultats observés :**
- `dotnet test` : 65 tests réussis sur 65, dont les 46 existants ;
- contrôle fumée headless : 120 contrôles réussis, code 0. Les 66 contrôles des lots 1D et 1F sont inchangés, au mot près ; 54 contrôles sont nouveaux ;
- sous Xvfb : 162 « SMOKE OK », dont 42 captures. Le titre du scénario 4 est entièrement visible, sur deux lignes ; le texte du panneau descend au plus à 617 pixels dans une fenêtre de 720. Pour les 23 captures des scénarios 1 à 3, la carte, la légende et le panneau sont identiques au pixel près à celles du lot 1F, sauf la ligne d'aide « 1 à 4 : choisir le scénario » ;
- dix-huit défauts introduits dans des copies jetables : tous détectés, dont trois que la première relecture avait fait passer au vert et deux sur le titre ;
- compilations sans avertissement, format conforme, 75 tests des hooks.

**Première relecture indépendante :** « conforme sous réserves », sans constat bloquant.
- **RG-01**, un angle mort du contrôle fumée : la zone après une fin de tour n'était pas comparée au moteur. Il est corrigé.
- **RG-02** relevait des changements de présentation dans les scénarios 1 à 3. Le titre des scénarios 1 à 3 est revenu à celui du lot 1F ; la fenêtre de 720 pixels et le titre du scénario 4 sont arbitrés par l'orchestrateur.
- **Observations :** RG-03, RG-04 et RG-06 sont traitées ; RG-05, RG-07 et RG-08 sont conservées en l'état.

**Seconde relecture indépendante**, ciblée sur les corrections et la finalisation : « corrections conformes, sous réserve de l'actualisation du rapport du lot », sans constat bloquant ni constat sur le code. Les deux constats sur le rapport (RC-01 pour les empreintes, RC-02 pour le §6.2) sont corrigés ; RC-03 à RC-06 sont des observations sans action requise. Voir §6.2.

**Non effectué :**
- l'essai manuel du scénario 4 sous macOS par le propriétaire n'a pas eu lieu ;
- aucun essai sur un écran réel, ni avec un clavier ou une souris physiques ;
- la CI n'a pas tourné, puisque rien n'est poussé.

## 2. Fichiers

| Fichier | Rôle | Changement |
|---|---|---|
| `src/Bastion.Simulation/Turns/TurnRules.cs` | paramètres validés, `Start`, `WithUnit`, `EndTurn` | 105 lignes, nouveau |
| `src/Bastion.Simulation/Turns/TurnState.cs` | `TurnState` et `TurnOutcome`, immuables | 45 lignes, nouveau |
| `tests/Bastion.Simulation.Tests/Turns/TurnTests.cs` | 19 tests xUnit (T01 à T09, T14, T15, et quatre tests complémentaires) | 224 lignes, nouveau |
| `src/Bastion.Client.Godot/PrototypeScene.cs` | scénario 4, touche T, ligne de tour, titre du scénario 4, appels à `TurnRules` | +71 −19 (361 lignes) |
| `src/Bastion.Client.Godot/SmokeTest.cs` | 54 contrôles ajoutés après les 66 existants, inchangés | +126 −2 (518 lignes) |
| `src/Bastion.Client.Godot/project.godot`, `Main.tscn` | fenêtre de 800 × 720 (au lieu de 640) et panneau prolongé, pour les lignes du scénario 4 | +1 −1 chacun |
| `src/Bastion.Client.Godot/README.md` | notice : scénario 4, touches 4 et T, contrôle fumée, essais non effectués | +29 −14 |
| `docs/mandates/BASTION-MANDAT-LOT-1G-v1.0-transcription.md` | mandat archivé (transcription) | 113 lignes, nouveau |
| `docs/mandates/README.md` | une ligne d'index | +1 |
| `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md` | ce rapport, avec les deux relectures indépendantes | nouveau |

**Inchangés**, vérifiés par `git diff --stat origin/main` sans aucune sortie :
- `src/Bastion.Simulation/Movement/` (MEC-0003, `MovementModel.CreateState` compris) ;
- les tests existants ;
- `.github/`, `scripts/`, `.claude/`, `CLAUDE.md`, `Bastion.slnx` ;
- `docs/gameplay/`, `docs/decisions/`, `docs/references/`.

La fiche MEC-0004 reste donc à l'état « non commencé » dans le registre (§9).

## 3. Conception

### 3.1 Moteur de tours (`Bastion.Simulation.Turns`)

- **`TurnRules`** (`record` immuable) :
  - **paramètres :** quatre, `MaxTu`, `TuRecovery`, `MaxEnergy` et `EnergyRecovery`, validés par le constructeur selon le §3.2. Les plafonds doivent être strictement positifs et les récupérations positives ou nulles ; une récupération supérieure au plafond est admise. Le profil initial `TurnRules.Initial` vaut `(60, 60, 100, 20)` (Q4.6). Les propriétés sont en lecture seule : une expression `with` ne peut pas contourner la validation ;
  - **`Start(UnitState)`** : rend le tour 1. Un état dont une ressource est négative ou dépasse son plafond est refusé (`ArgumentException`), sans réduction silencieuse ; un état exactement aux plafonds est accepté ;
  - **`WithUnit(TurnState, UnitState)`** : remplace l'état de l'unité par celui que rend le moteur de marche après un déplacement. Le numéro de tour ne change pas, et le nouvel état est validé de la même façon ;
  - **`EndTurn(TurnState)`** : rend un `TurnOutcome`. L'état de départ est revalidé contre les plafonds de ces règles. Chaque ressource vaut ensuite `min(courante + récupération, plafond)`, calculé sur 64 bits (`long`) puis ramené en `int` : il ne peut pas déborder. Le tour augmente de 1 (`checked`). L'unité est reprise par `with`, donc sa position et son orientation sont conservées.
- **`TurnState`** : numéro de tour et `UnitState`, avec un constructeur interne. Seul `TurnRules` peut en créer un, et toujours validé.
- **`TurnOutcome`** : contient les états `Before` et `After`, ainsi que `RecoveredTu` et `RecoveredEnergy`, différences entre ces deux états. Son `Message` sert de compte rendu du §3.4, par exemple « Fin du tour 1 : 48 TU et 20 d'énergie récupérées. Début du tour 2. ». Il est rendu par le moteur, comme `OrderOutcome.Message` pour la marche.

**Hors de ce périmètre :** ni moteur multi-unités, ni ordonnanceur, ni gestionnaire de phases, ni dépendance à Godot. `MovementModel` et `CreateState` ne changent pas. Les états rendus par le moteur de marche sont repris tels quels.

### 3.2 Scénario 4 (client Godot)

- **Configuration :** `BuildMap(4)` est la carte du scénario 1. `ResetScenario` crée l'état (1,4), N, 12 TU, 35 d'énergie par `MovementModel.CreateState`, puis `Turns = TurnRules.Initial.Start(State)`. Dans les scénarios 1 à 3, `Turns` vaut `null`.
- **Entrées :**
  - **clic :** inchangé. Dans le scénario 4, l'état rendu par `ExecuteOrder` est repris par `TurnRules.WithUnit`.
  - **touche T** (libellé `Key.T`) : appelle `TurnRules.EndTurn` si `Turns` n'est pas `null`, et ne fait rien sinon. La scène reprend l'état rendu, garde `LastPath` et remplace `LastResult` par `TurnOutcome.Message` (§3.4).
  - **touches 1 à 4 :** la boucle existante (libellé ou position) couvre désormais la touche 4, dont le libellé AZERTY est « ' ». Appuyer sur 4 dans le scénario 4 recharge le scénario.
  - **touche R :** inchangée dans les scénarios 1 à 3. Dans le scénario 4, elle restaure le tour 1, l'état initial, le chemin « aucun » et le message initial.
- **« Message initial » du scénario 4 :** la fiche demande que R restaure « le message initial ». Le message « Scénario 4 dans son état initial : tour 1. » est utilisé à la fois au chargement par la touche 4 et pour R : les deux mènent au même état (T11). L'arbitrage du 25 novembre conserve ce message, jugé conforme à MEC-0004.
- **Panneau :**
  - dans le seul scénario 4, une ligne « Tour : n » et la commande « T : terminer le tour » ;
  - **titre, selon l'arbitrage du 25 novembre :** « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans les scénarios 1 à 3, exactement comme au lot 1F, et « Bastion — banc d'essai MEC-0004 (lot 1G) » dans le scénario 4. Le choix se fait sur le numéro du scénario (`Scenario == TurnScenario`) ;
  - dans tous les scénarios, la ligne d'aide devient « 1 à 4 : choisir le scénario ». La touche 4 agit en effet depuis n'importe quel scénario. Les lignes de position, d'orientation, de TU, d'énergie, de chemin et de résultat gardent leur format.
- **Fenêtre :** elle passe de 800 × 640 à 800 × 720, et le bas du panneau de 616 à 696 pixels. La carte et la légende ne bougent pas (§5.3).
  - **Pourquoi :** les captures avaient révélé un panneau coupé en bas dans le scénario 4.
  - **Mesuré** (script `bas_panneau.py` de la relecture, dernier pixel de texte du panneau) :
    - lot 1F, 23 captures : au plus 591 pixels (`13-s2-clic-hors-zone`, scénario 2 après un clic refusé) ;
    - lot 1G, 42 captures, titre du lot 1F rétabli : au plus 617 pixels (`34-s4-fin-tour-1`). La relecture a obtenu la même valeur dans son essai X1, avec une fenêtre de 640 pixels : les 42 états capturés tiennent donc dans 640 pixels.
  - **Calculé, non observé :** les deux lignes du scénario 4 (« Tour : n » et « T : terminer le tour ») ajoutent 52 pixels. Un état du scénario 4 aussi chargé que le pire cas du lot 1F atteindrait donc environ 591 + 52 = 643 pixels et serait coupé dans une fenêtre de 640 pixels. Aucune capture ne montre un tel état ; la relecture formule la même réserve (RG-02).
  - **Statut :** la hauteur de 720 pixels est acceptée par l'arbitrage du 25 novembre pour le prototype du lot 1G.

## 4. Correspondance des tests T01 à T16

| Test | Couverture | Où |
|---|---|---|
| T01 | tour 1, 12/35 → tour 2, 60/55 | `T01_EndOfTurnFrom12TuAnd35Energy` ; contrôle fumée (scénario 4, première touche T) |
| T02 | tour 2, 60/55 → tour 3, 60/75 | `T02_NextEndOfTurnWithoutMovement` ; contrôle fumée |
| T03 | 58/95 → 60/100 | `T03_BothResourcesAreCapped` |
| T04 | +1 sans déplacement | `T04_TurnCounterIncreasesByOneWithoutMovement` |
| T05 | position et orientation conservées après un déplacement | `T05_PositionAndOrientationAreKeptAfterAMovement` (moteur de marche et `WithUnit`) et `WithUnitKeepsTheTurnNumberAfterTheFirstTurn` (déplacement au tour 2) ; contrôle fumée (clic sur (2,4), puis T) |
| T06 | 40/25, 30/10 ; 12/15 → 37/25 | `T06_CustomParametersAreApplied` |
| T07 | récupération supérieure au plafond → plafonnée ; aucun débordement avec `int.MaxValue` | `T07_RecoveryAboveTheCapIsAllowedAndCapped` |
| T08 | récupération nulle → ressource inchangée | `T08_ZeroRecoveryLeavesTheResourceUnchanged` |
| T09 | paramètre négatif, plafond nul, état hors plafond, ressources négatives ; aucune modification d'état | cinq tests `T09_…` |
| T10 | touche T sans effet dans les scénarios 1 à 3, après un déplacement | contrôle fumée (« T10 : … ») |
| T11 | R, ou 4 dans le scénario 4 actif : réinitialisation complète | contrôle fumée (« T11 : … », deux contrôles) |
| T12 | touche 4 AZERTY (« ' », position 4) | contrôle fumée (« T12 : … ») |
| T13 | scénarios 1 à 3 et contrôles existants sans régression | 46 tests existants ; 66 contrôles fumée antérieurs, identiques ; carte, légende et panneau identiques au pixel près, sauf la ligne d'aide |
| T14 | 60/100 → inchangées, tour +1 | `T14_EndOfTurnAtTheCapsKeepsResourcesAndIncrementsTheCounter` |
| T15 | état initial exactement aux plafonds accepté | `T15_InitialStateExactlyAtTheCapsIsAccepted` |
| T16 | chemin conservé, dernier résultat actualisé après une fin de tour qui suit un déplacement | contrôle fumée (« T16 : … ») |

**Méthode des assertions :**
- **moteur :** les valeurs de la fiche (60/55, 60/75, 60/100, 37/25…) sont écrites en constantes ;
- **client :** chaque fin de tour est comparée au résultat de `TurnRules.Initial.EndTurn`, calculé depuis l'état de tour de la scène. La zone affichée est comparée à celle que le moteur de marche calcule pour le nouvel état (RG-01). Les valeurs de la fiche sont vérifiées en plus, en constantes indépendantes (T01, T02, T12 et l'état restauré par T11). La présence de la ligne « Tour » et de la commande T est contrôlée dans le scénario 4, leur absence dans les scénarios 1 à 3 (RG-04). Le titre du panneau est comparé, aux mêmes moments, à une constante écrite dans le contrôle fumée : celui du lot 1F dans les scénarios 1 à 3, celui du lot 1G dans le scénario 4.

## 5. Commandes et résultats

### 5.1 Compilation, tests, format, harnais

Toutes les commandes ont été lancées dans le dépôt de travail et renvoient le code 0.

| Commande | Résultat |
|---|---|
| `dotnet restore` | — |
| `dotnet build --no-restore --configuration Release` | 0 Warning(s), 0 Error(s) |
| `dotnet test --no-build --configuration Release` | « Passed! - Failed: 0, Passed: 65, Skipped: 0, Total: 65 » |
| `dotnet format --verify-no-changes --no-restore` | aucune sortie |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |
| `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` (Debug et `--configuration Release`) | 0 Warning(s), 0 Error(s) |
| `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes --no-restore` | aucune sortie |

### 5.2 Contrôle fumée en mode headless

```
timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test
```

Le code de sortie est 0, avec 120 lignes « SMOKE OK » et « SMOKE : RÉUSSITE ». Les 66 premières lignes sont identiques, au mot près, à la sortie finale du lot 1F (`diff`, sans écart). Hors les dix lignes du titre, les 110 lignes sont identiques à celles du passage précédant la finalisation (`diff`, sans écart). Les 54 nouvelles lignes :

```
SMOKE OK : scénario 1 chargé puis déplacé en (2,4) avant la touche T ((2,4), E, 16 TU, 8 d'énergie)
SMOKE OK : T10 : touche T sans effet dans le scénario 1 ((2,4), E, 16 TU, 8 d'énergie, chemin E)
SMOKE OK : aucun tour ni commande T affichés dans le scénario 1
SMOKE OK : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans le scénario 1
SMOKE OK : scénario 2 chargé puis déplacé en (2,4) avant la touche T ((2,4), SE, 10 TU, 5 d'énergie)
SMOKE OK : T10 : touche T sans effet dans le scénario 2 ((2,4), SE, 10 TU, 5 d'énergie, chemin N → SE)
SMOKE OK : aucun tour ni commande T affichés dans le scénario 2
SMOKE OK : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans le scénario 2
SMOKE OK : scénario 3 chargé puis déplacé en (2,4) avant la touche T ((2,4), E, 14 TU, 7 d'énergie)
SMOKE OK : T10 : touche T sans effet dans le scénario 3 ((2,4), E, 14 TU, 7 d'énergie, chemin E)
SMOKE OK : aucun tour ni commande T affichés dans le scénario 3
SMOKE OK : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans le scénario 3
SMOKE OK : T12 : touche 4 (AZERTY) : scénario 4 chargé, (1,4), N, 12 TU, 35 d'énergie (Scénario 4 dans son état initial : tour 1.)
SMOKE OK : carte du scénario 4 = carte du scénario 1 : murs : aucun ; cases infranchissables : (3,2) ; terrains non normaux : aucun
SMOKE OK : zone affichée = zone du moteur (12 cases)
SMOKE OK : tour 1 et commande T affichés au chargement du scénario 4
SMOKE OK : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » au chargement du scénario 4
SMOKE OK : panneau conforme à l'état au chargement du scénario 4
SMOKE OK : panneau : scénario 4, chemin « aucun » attendu au chargement du scénario 4 (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE OK : touche T = résultat du moteur de tours : tour 2, (1,4), N, 60 TU, 55 d'énergie (Fin du tour 1 : 48 TU et 20 d'énergie récupérées. Début du tour 2.)
SMOKE OK : zone affichée après la fin de tour = zone du moteur pour le nouvel état (23 cases, 23 attendues)
SMOKE OK : T01 : tour 2, 60 TU et 55 d'énergie attendus : tour 2, (1,4), N, 60 TU, 55 d'énergie
SMOKE OK : tour 2 et commande T affichés après la 1re fin de tour
SMOKE OK : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la 1re fin de tour
SMOKE OK : panneau conforme à l'état après la 1re fin de tour
SMOKE OK : panneau : scénario 4, chemin « aucun » attendu après la 1re fin de tour (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE OK : touche T = résultat du moteur de tours : tour 3, (1,4), N, 60 TU, 75 d'énergie (Fin du tour 2 : 0 TU et 20 d'énergie récupérées. Début du tour 3.)
SMOKE OK : zone affichée après la fin de tour = zone du moteur pour le nouvel état (23 cases, 23 attendues)
SMOKE OK : T02 : tour 3, 60 TU et 75 d'énergie attendus : tour 3, (1,4), N, 60 TU, 75 d'énergie
SMOKE OK : tour 3 et commande T affichés après la 2e fin de tour
SMOKE OK : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la 2e fin de tour
SMOKE OK : clic sur (2,4) dans le scénario 4 = résultat d'ExecuteOrder, tour inchangé : (2,4), E, 56 TU, 73 d'énergie
SMOKE OK : panneau conforme à l'état après l'ordre vers (2,4)
SMOKE OK : panneau : scénario 4, chemin « E » attendu après l'ordre vers (2,4) (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : touche T = résultat du moteur de tours : tour 4, (2,4), E, 60 TU, 93 d'énergie (Fin du tour 3 : 4 TU et 20 d'énergie récupérées. Début du tour 4.)
SMOKE OK : zone affichée après la fin de tour = zone du moteur pour le nouvel état (23 cases, 23 attendues)
SMOKE OK : T05 : position et orientation conservées après la fin de tour : (2,4), E, 60 TU, 93 d'énergie
SMOKE OK : T16 : chemin « E » conservé, dernier résultat actualisé (Fin du tour 3 : 4 TU et 20 d'énergie récupérées. Début du tour 4.)
SMOKE OK : tour 4 et commande T affichés après la fin de tour qui suit le déplacement
SMOKE OK : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la fin de tour qui suit le déplacement
SMOKE OK : panneau conforme à l'état après la fin de tour qui suit le déplacement
SMOKE OK : panneau : scénario 4, chemin « E » attendu après la fin de tour qui suit le déplacement (LastPath : « E » ; panneau : « Chemin du dernier ordre exécuté : E »)
SMOKE OK : T11 : touche R : tour 1, (1,4), N, 12 TU, 35 d'énergie, chemin effacé, message initial (Scénario 4 dans son état initial : tour 1.)
SMOKE OK : tour 1 et commande T affichés après la touche R
SMOKE OK : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la touche R
SMOKE OK : touche T = résultat du moteur de tours : tour 2, (2,4), E, 60 TU, 53 d'énergie (Fin du tour 1 : 52 TU et 20 d'énergie récupérées. Début du tour 2.)
SMOKE OK : zone affichée après la fin de tour = zone du moteur pour le nouvel état (23 cases, 23 attendues)
SMOKE OK : état déplacé au tour 2 avant la touche 4 ((2,4), E, 60 TU, 53 d'énergie)
SMOKE OK : T11 : touche 4 dans le scénario 4 actif : réinitialisation complète ((1,4), N, 12 TU, 35 d'énergie, tour 1)
SMOKE OK : tour 1 et commande T affichés après la touche 4
SMOKE OK : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la touche 4
SMOKE OK : touche 1 depuis le scénario 4 : scénario 1 dans son état initial ((1,4), N, 20 TU, 10 d'énergie)
SMOKE OK : aucun tour ni commande T affichés après le retour au scénario 1
SMOKE OK : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » après le retour au scénario 1
SMOKE : RÉUSSITE
```

### 5.3 Rendu sous Xvfb et non-régression visuelle

```
timeout 300 xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test --capture=<dossier>
```

- **Résultat :** code 0, « SMOKE : RÉUSSITE », 162 « SMOKE OK » (120 contrôles et 42 captures) ; rendu OpenGL 3 de Mesa llvmpipe.
- **Captures 33 à 41 (scénario 4)**, examinées par Claude Code :
  - la carte du scénario 1 ;
  - le titre « Bastion — banc d'essai MEC-0004 (lot 1G) », replié sur deux lignes ;
  - un panneau avec « Tour : 1 », 12 TU et 35 d'énergie au chargement ;
  - après le déplacement et la fin de tour : « Tour : 4 », (2,4), E, 60 TU, 93 d'énergie, « Chemin du dernier ordre exécuté : E » et le compte rendu « Fin du tour 3 : 4 TU et 20 d'énergie récupérées. Début du tour 4. ».

  Ce sont les captures d'un rendu automatisé, et non une validation manuelle.
- **Titre du scénario 4 entièrement visible :**
  - **examen des captures :** dans les captures 33 à 41, le titre se lit en entier sur deux lignes, « Bastion — banc d'essai » puis « MEC-0004 (lot 1G) », sans coupure ni troncature ;
  - **mesure** sur la capture 33 : les pixels du titre occupent x = 529 à 703 et y = 29 à 70, à l'intérieur du panneau (bord droit du texte à 784, de la fenêtre à 800) ;
  - **bas du texte** (script `bas_panneau.py`) : au plus 617 pixels sur les 42 captures (`34-s4-fin-tour-1`), pour une fenêtre de 720 pixels. Les positions verticales sont les mêmes qu'avant la finalisation : le nouveau titre occupe deux lignes, comme celui du lot 1F.
- **Effet de la finalisation sur le rendu :** les captures ont été comparées à celles du passage précédent avec Pillow. Les captures 01 à 32 et 42 (scénarios 1 à 3) sont identiques au pixel près. Les captures 33 à 41 (scénario 4) ne diffèrent que dans le rectangle (594,30)–(728,71), celui du titre.
- **Correction issue des captures :** dans la première version, la dernière ligne du panneau du scénario 4 (« (débogage) ») était coupée en bas de la fenêtre. La fenêtre est passée à 720 pixels de haut, et le titre du scénario 4 a été raccourci en « gestion des tours ». Toutes les vérifications ont été relancées ensuite.
- **Scénarios 1 à 3 identiques au lot 1F :** les 23 captures 01 à 23 ont été comparées à celles du lot 1F avec Pillow, sur trois zones :
  - la carte, (0,0)–(527,511) : **identique au pixel près** dans les 23 captures ;
  - la légende, (0,512)–(527,639) : **identique au pixel près** dans les 23 captures ;
  - le panneau, (528,0)–(799,639) : identique, sauf une bande de 15 pixels de haut, celle de la ligne d'aide « 1 à 4 : choisir le scénario », qui remplace « 1, 2, 3 : choisir le scénario ».

  Seule la hauteur de la fenêtre diffère (720 au lieu de 640), avec une bande vide en bas.

### 5.4 Vérifications négatives (copies jetables)

Le script `negatifs.sh`, dans le dossier temporaire de la session :
- copie l'arbre de travail, sans `.git`, `bin`, `obj` ni `.godot` ;
- y introduit un défaut ;
- lance `dotnet test` pour les défauts du moteur, ou la compilation Debug puis le contrôle fumée pour ceux du client.

Le dépôt de travail n'est pas touché. Les défauts R1 à R3 reprennent trois défauts de la première relecture (S5, S6 et N1) qui passaient au vert avant les corrections. T1 et T2 portent sur le titre de la finalisation. Les dix-huit défauts ont été rejoués sur l'état final (script `negatifs3.sh`).

```
######## E1. TU non plafonnées
Failed!  - Failed:    10, Passed:    55, Skipped:     0, Total:    65, Duration: 427 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.T08_ZeroRecoveryLeavesTheResourceUnchanged [3 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T03_BothResourcesAreCapped [< 1 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.WithUnitKeepsTheTurnNumberAfterTheFirstTurn [67 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T02_NextEndOfTurnWithoutMovement [< 1 ms]
dotnet test : code 1
######## E2. compteur de tours non incrémenté
Failed!  - Failed:    11, Passed:    54, Skipped:     0, Total:    65, Duration: 422 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.T08_ZeroRecoveryLeavesTheResourceUnchanged [24 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T03_BothResourcesAreCapped [< 1 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.WithUnitKeepsTheTurnNumberAfterTheFirstTurn [70 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T02_NextEndOfTurnWithoutMovement [< 1 ms]
dotnet test : code 1
######## E3. état au-dessus du plafond de TU accepté
Failed!  - Failed:     2, Passed:    63, Skipped:     0, Total:    65, Duration: 393 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.T09_InitialStateAboveACapIsRefusedWithoutSilentReduction [2 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T09_RejectionLeavesTheStateUnchanged [< 1 ms]
dotnet test : code 1
######## E4. addition plafonnée sur 32 bits (débordement)
Failed!  - Failed:     1, Passed:    64, Skipped:     0, Total:    65, Duration: 375 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.T07_RecoveryAboveTheCapIsAllowedAndCapped [1 ms]
dotnet test : code 1
######## E5. récupération d'énergie prise dans celle des TU
Failed!  - Failed:     6, Passed:    59, Skipped:     0, Total:    65, Duration: 467 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.T08_ZeroRecoveryLeavesTheResourceUnchanged [6 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T02_NextEndOfTurnWithoutMovement [< 1 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T05_PositionAndOrientationAreKeptAfterAMovement [< 1 ms]
Failed Bastion.Simulation.Tests.Turns.TurnTests.T01_EndOfTurnFrom12TuAnd35Energy [< 1 ms]
dotnet test : code 1
######## E6. plafond nul accepté
Failed!  - Failed:     1, Passed:    64, Skipped:     0, Total:    65, Duration: 393 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.T09_ZeroCapsAreRefused [1 ms]
dotnet test : code 1
######## C1. scénario 4 démarré avec 20 TU
compilation Debug : code 0
SMOKE ÉCHEC : T12 : touche 4 (AZERTY) : scénario 4 chargé, (1,4), N, 20 TU, 35 d'énergie (Scénario 4 dans son état initial : tour 1.)
SMOKE : ÉCHEC (1 contrôle(s))
contrôle fumée : code 1
######## C2. la fin de tour efface le chemin
compilation Debug : code 0
SMOKE ÉCHEC : T16 : chemin « aucun » conservé, dernier résultat actualisé (Fin du tour 3 : 4 TU et 20 d'énergie récupérées. Début du tour 4.)
SMOKE ÉCHEC : panneau : scénario 4, chemin « E » attendu après la fin de tour qui suit le déplacement (LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)
SMOKE : ÉCHEC (2 contrôle(s))
contrôle fumée : code 1
######## C3. la touche R garde le tour et l'état de tour
compilation Debug : code 0
SMOKE ÉCHEC : T11 : touche R : tour 1, (1,4), N, 12 TU, 35 d'énergie, chemin effacé, message initial (Scénario 4 dans son état initial : tour 1.)
SMOKE ÉCHEC : tour 1 et commande T affichés après la touche R
SMOKE ÉCHEC : état déplacé au tour 2 avant la touche 4 ((2,4), E, 60 TU, 53 d'énergie)
contrôle fumée : code 1
######## C4. la scène garde l'ancien état après la fin de tour
compilation Debug : code 0
SMOKE ÉCHEC : touche T = résultat du moteur de tours : tour 2, (1,4), N, 12 TU, 35 d'énergie (Fin du tour 1 : 48 TU et 20 d'énergie récupérées. Début du tour 2.)
SMOKE ÉCHEC : zone affichée après la fin de tour = zone du moteur pour le nouvel état (12 cases, 23 attendues)
SMOKE ÉCHEC : T01 : tour 2, 60 TU et 55 d'énergie attendus : tour 2, (1,4), N, 12 TU, 35 d'énergie
contrôle fumée : code 1
######## C5. touche 4 non reconnue
compilation Debug : code 0
SMOKE ÉCHEC : T12 : touche 4 (AZERTY) : scénario 4 chargé, (2,4), E, 14 TU, 7 d'énergie (Destination (2,4) atteinte.)
SMOKE ÉCHEC : carte du scénario 4 = carte du scénario 1 : murs : aucun ; cases infranchissables : aucune ; terrains non normaux : (2,4) difficile, (3,4) très difficile
SMOKE ÉCHEC : tour 1 et commande T affichés au chargement du scénario 4
contrôle fumée : code 2
######## C6. tour affiché dans tous les scénarios
compilation Debug : code 0
SMOKE ÉCHEC : aucun tour ni commande T affichés dans le scénario 1
SMOKE ÉCHEC : aucun tour ni commande T affichés dans le scénario 2
SMOKE ÉCHEC : aucun tour ni commande T affichés dans le scénario 3
contrôle fumée : code 1
######## C7. dernier résultat non actualisé à la fin de tour
compilation Debug : code 0
SMOKE ÉCHEC : touche T = résultat du moteur de tours : tour 2, (1,4), N, 60 TU, 55 d'énergie (Scénario 4 dans son état initial : tour 1.)
SMOKE ÉCHEC : touche T = résultat du moteur de tours : tour 3, (1,4), N, 60 TU, 75 d'énergie (Scénario 4 dans son état initial : tour 1.)
SMOKE ÉCHEC : touche T = résultat du moteur de tours : tour 4, (2,4), E, 60 TU, 93 d'énergie (Destination (2,4) atteinte.)
contrôle fumée : code 1
######## R1. zone non recalculée après le tour 1 (relecture, S5)
compilation Debug : code 0
SMOKE ÉCHEC : zone affichée après la fin de tour = zone du moteur pour le nouvel état (12 cases, 23 attendues)
SMOKE ÉCHEC : zone affichée après la fin de tour = zone du moteur pour le nouvel état (12 cases, 23 attendues)
SMOKE ÉCHEC : zone affichée après la fin de tour = zone du moteur pour le nouvel état (12 cases, 23 attendues)
contrôle fumée : code 1
######## R2. commande T absente du panneau (relecture, S6)
compilation Debug : code 0
SMOKE ÉCHEC : tour 1 et commande T affichés au chargement du scénario 4
SMOKE ÉCHEC : tour 2 et commande T affichés après la 1re fin de tour
SMOKE ÉCHEC : tour 3 et commande T affichés après la 2e fin de tour
contrôle fumée : code 1
######## R3. WithUnit remet le tour à 1 (relecture, N1)
Failed!  - Failed:     1, Passed:    64, Skipped:     0, Total:    65, Duration: 666 ms - Bastion.Simulation.Tests.dll (net10.0)
Failed Bastion.Simulation.Tests.Turns.TurnTests.WithUnitKeepsTheTurnNumberAfterTheFirstTurn [160 ms]
dotnet test : code 1
######## T1. scénario 4 avec le titre du lot 1F
compilation Debug : code 0
SMOKE ÉCHEC : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » au chargement du scénario 4
SMOKE ÉCHEC : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la 1re fin de tour
SMOKE ÉCHEC : titre du panneau « Bastion — banc d'essai MEC-0004 (lot 1G) » après la 2e fin de tour
contrôle fumée : code 1
######## T2. titre du lot 1G dans tous les scénarios
compilation Debug : code 0
SMOKE ÉCHEC : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans le scénario 1
SMOKE ÉCHEC : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans le scénario 2
SMOKE ÉCHEC : titre du panneau « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » dans le scénario 3
contrôle fumée : code 1
```

Dans les journaux, la sortie de chaque défaut suit la ligne qui l'annonce.

**Les dix-huit défauts sont tous détectés :**
- les sept défauts du moteur (E1 à E6, R3) font échouer `dotnet test`, avec le code 1 ;
- dix défauts du client sur onze (C1 à C4, C6, C7, R1, R2, T1, T2) font sortir le contrôle fumée avec le code 1 ;
- C5 (touche 4 non reconnue) donne le code 2, une exception, parce que le contrôle suivant suppose un scénario 4 chargé. Le code est non nul et la CI échouerait aussi.

## 6. Relecture indépendante ciblée

### 6.1 Première relecture, avant les corrections

Un agent distinct du développeur a relu l'arbre de travail avant les corrections, sur les cinq axes du §5 du mandat. Son rapport est reproduit ci-dessous sans modification, entre deux filets.

---

### Relecture indépendante du lot 1G : implémentation de MEC-0004

**Date :** 24 novembre 2026
**Objet :** relecture ciblée demandée au §5 du mandat `docs/mandates/BASTION-MANDAT-LOT-1G-v1.0-transcription.md` (5 axes, plus reproduction des vérifications).
**Relecteur :** agent distinct du développeur, sans outil d'édition sur le dépôt. Je n'ai rien modifié, commité ni poussé. Je ne m'accorde pas la validation finale.
**État relu :** branche locale `claude/lot-1g-implementation-mec-0004`, HEAD = `origin/main` = `1fa2769e309ea74390b678836d3203a16f7e66d4`, rien de commité.
- 6 fichiers modifiés : `docs/mandates/README.md`, `src/Bastion.Client.Godot/{Main.tscn, PrototypeScene.cs, README.md, SmokeTest.cs, project.godot}`.
- 4 fichiers non suivis : `src/Bastion.Simulation/Turns/{TurnRules.cs, TurnState.cs}`, `tests/Bastion.Simulation.Tests/Turns/TurnTests.cs` et la transcription du mandat.
- Le rapport du développeur n'était pas écrit au moment de la relecture.

---

### Méthode

Toutes les commandes ont tourné dans une **copie identique** du dépôt, pour ne pas écrire de `bin/`, `obj/` ni `.godot/` dans le dépôt réel. La copie est `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g/repo`. J'ai vérifié qu'elle était identique avant de commencer : même `git status --porcelain` et mêmes empreintes SHA-256 pour les 192 fichiers suivis et non suivis.

**Exécuté et réussi (codes de sortie réels) :**

| Commande | Résultat |
|---|---|
| `dotnet build` puis `dotnet build --no-incremental` | 0 avertissement, 0 erreur, code 0 |
| `dotnet test` | `Passed: 64, Failed: 0`, code 0 (18 tests `TurnTests`) |
| `dotnet test` sur `origin/main` (worktree jetable) | `Passed: 46`, code 0 : 46 + 18 = 64 |
| `dotnet build -c Release` + `dotnet test --no-build -c Release` (forme de la CI) | 64 réussis, code 0 |
| `dotnet format --verify-no-changes` | code 0 |
| `bash scripts/harness/test-hooks.sh` | `== 75 tests, 0 échec(s) ==`, code 0 |
| Client : Release `--no-incremental`, Debug `--no-incremental`, `dotnet format <csproj> --verify-no-changes` | 0 avertissement, codes 0 / 0 / 0 |
| Contrôle fumée headless (`timeout 300 … --smoke-test`) | 106 `SMOKE OK`, 0 `SMOKE ÉCHEC`, `SMOKE : RÉUSSITE`, code 0. Journal identique ligne à ligne à `lot1g/smoke2.log`. |
| Contrôle fumée sous Xvfb avec `--capture` | 148 `SMOKE OK`, 0 échec, code 0 ; 42 captures, **identiques au pixel** aux 42 de `lot1g/captures2` |
| Contrôle fumée de `origin/main` (headless) | 66 `SMOKE OK`, code 0 |
| Les 66 premières lignes `SMOKE OK` du lot 1G | identiques (`diff` vide) à celles de `origin/main` et à `lot1f/smoke3.log` |
| `git diff origin/main --stat -- src/Bastion.Simulation tests .github scripts .claude CLAUDE.md docs/gameplay docs/decisions docs/references` | vide |
| `sha256sum` de la transcription du mandat | `c792934e…11b1`, conforme à la ligne ajoutée à `docs/mandates/README.md` |
| `grep -rn Godot src/Bastion.Simulation` | seulement le commentaire du `.csproj` ; aucun paquet Godot dans `project.assets.json` ; seule `Bastion.Simulation.dll` dans `bin/` |
| Dépôt réel après la relecture | `git status` et empreintes des 192 fichiers identiques à l'état initial ; `git worktree list` ne montre que le dépôt lui-même ; HEAD inchangé |

**Comparaison au pixel des 23 premières captures avec celles du lot 1F** (script `relecture-1g/scripts/compare.py`) :
- **carte** (0–528 × 0–516) : 0 pixel différent sur 23/23 images ;
- **légende** : 0 pixel différent sur 23/23 images ;
- **panneau** : différent sur 23/23 images (voir RG-02) ;
- **fenêtre** : 800×640 au lot 1F, 800×720 au lot 1G.

**Captures du scénario 4 examinées** : 33-scenario-4, 34-s4-fin-tour-1 et 37-s4-fin-tour-apres-ordre.
- 33 : (1,4) N, 12 TU, 35 d'énergie, « Tour : 1 », 12 cases atteignables, ligne « T : terminer le tour » présente.
- 34 : tour 2, 60 TU, 55 d'énergie, 23 cases.
- 37 : tour 4, (2,4) E, 60 TU, 93 d'énergie, chemin « E » conservé, message « Fin du tour 3 : 4 TU et 20 d'énergie récupérées. Début du tour 4. ».

**Vrais événements X11 sous Xvfb (XTest), disposition AZERTY imitée** : keycodes 10 à 13 remappés en `&/1, é/2, "/3, '/4`. C'est un essai nouveau : le README l'indique comme non fait pour 4 et T.
- Séquence : T, 4 (keysym apostrophe), T, T, R, T, 4, & (touche 1), T.
- Captures : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g/x11/` ; planche : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g/planche-x11.png`.
- Résultat **inspecté sur les captures** (l'application ne rend pas de code de sortie dans ce mode) :
  - la touche de position 4 charge le scénario 4 au tour 1 (12 / 35) ;
  - T donne le tour 2 (60 / 55), puis le tour 3 (60 / 75) ;
  - R ramène au tour 1 (12 / 35) avec le message initial ;
  - T donne le tour 2 ;
  - 4 dans le scénario 4 actif ramène au tour 1 ;
  - & charge le scénario 1 ;
  - T dans le scénario 1 ne change rien.

**Défauts introduits par le relecteur**, un par copie jetable sous `relecture-1g/sab/` (script `relecture-1g/scripts/sabotage.sh`). Aucun ne reprend les défauts E1–E6 ni C1–C7 du développeur.

| # | Défaut | `dotnet test` | Contrôle fumée |
|---|---|---|---|
| N1 | `WithUnit` remet le tour à 1 | **64/64, code 0 : non détecté** | 104 OK / 2 ÉCHEC, code 1 |
| N2 | `WithUnit` ne valide plus l'état | 1 échec (`T09_RejectionLeavesTheStateUnchanged`), code 1 | — |
| N3 | `EndTurn` ne valide plus l'état | 1 échec (même test), code 1 | — |
| N4 | récupération supérieure au plafond refusée | 1 échec (`T07`), code 1 | — |
| N5 | état aux plafonds refusé (`>=`) | 5 échecs (T15, T02, T14, T04, T07), code 1 | — |
| N6 | la fin de tour remet l'orientation à N | 1 échec (`T05`), code 1 | 105 / 1 ÉCHEC (T05), code 1 |
| N7 | énergie négative acceptée | 1 échec (`T09_NegativeResourcesAreRefused`), code 1 | — |
| N8 | premier tour numéroté 0 | 13 échecs, code 1 | — |
| S1 | clic sans `WithUnit` dans la scène | — | 104 / 2, code 1 |
| S2 | T actif dans les scénarios 1 à 3 | — | 100 / 6, code 1 |
| S3 | récupération appliquée deux fois | — | 94 / 12, code 1 |
| S4 | tour affiché = tour − 1 | — | 100 / 6, code 1 |
| S5 | zone non recalculée après une fin de tour | — | **106 / 0, code 0 : non détecté** |
| S6 | ligne « T : terminer le tour » absente du panneau | — | **106 / 0, code 0 : non détecté** |
| S7 | touche 4 ignorée dans le scénario 4 actif | — | 104 / 2, code 1 |
| S8 | R du scénario 4 avec le message générique | — | 105 / 1 (T11), code 1 |
| I1 | `with { MaxTu = -1 }`, `with { Turn = 7 }`, `new TurnState(…)`, `with { After = … }` depuis les tests | refus de compiler : CS0200 ×3 et CS1729, code 1 | — |
| X1 | titre du lot 1F + fenêtre de 640 px + `offset_bottom = 616` | — | Xvfb : 148 OK, code 0 ; voir RG-02 |

---

### Constats

**Aucun constat bloquant.**

#### RG-01 — à corriger — Après une fin de tour, aucun contrôle ne compare la zone affichée au moteur
- **Emplacement :**
  - `src/Bastion.Client.Godot/SmokeTest.cs:360-368` (`EndTurnAsync`) compare `Turns`, `State` et `LastResult` seulement ;
  - `CheckHud` (`SmokeTest.cs:69-77`) ne lit pas la ligne « Cases atteignables ».
- **Preuve :** défaut S5. La zone reste figée dès que le tour dépasse 1 (`PrototypeScene.cs:340`). Le contrôle fumée donne 106 OK, 0 échec, code 0.
  - La capture Xvfb de ce défaut (`relecture-1g/sab/S5-captures/34-s4-fin-tour-1.png`) affiche « TU restantes : 60 » et « Cases atteignables : 12 ».
  - La version livrée affiche 23 cases dans le même état (`relecture-1g/captures/34-s4-fin-tour-1.png`).
- **Conséquence :** une régression dans l'effet le plus visible de la récupération (zone élargie) passerait la suite et la CI au vert. Seules les captures ou l'essai manuel la montreraient. Le README (`README.md:146`) annonce que « chaque fin de tour est comparée au résultat du moteur de tours ». C'est vrai pour l'état, pas pour la zone. Le code livré est correct ; c'est un angle mort du test.
- **Correction suggérée :** dans `EndTurnAsync`, comparer `scene.Reachability.Zone` à `turnModel.ComputeReachability(expected.After.Unit).Zone`, comme le lot 1F le fait après chaque ordre.

#### RG-02 — à corriger, ou à faire arbitrer explicitement — Changements visibles dans les scénarios 1 à 3 non demandés
- **Emplacement :**
  - `PrototypeScene.cs:342` : le titre devient « banc d'essai de MEC-0003 et MEC-0004 (lots 1D à 1G) » ;
  - `project.godot:20` : `viewport_height` passe de 640 à 720 ;
  - `Main.tscn:12` : `offset_bottom` passe de 616 à 696.
- **Preuve :**
  - Sur les 23 premières captures : carte et légende identiques au pixel au lot 1F, panneau différent 23/23. Le titre passe sur 3 lignes et tout le panneau descend de 26 px. La fenêtre fait 720 px.
  - Mesure du dernier pixel de texte du panneau (`scripts/bas_panneau.py`) : au plus y = 643 dans le lot 1G (34-s4-fin-tour-1). Le panneau déborderait donc d'une fenêtre de 640 px.
  - Essai X1 (titre du lot 1F, 640 px) : au plus y = 617 sur les 42 captures, 148 OK, code 0.
  - Avec ce titre, les 23 captures ne diffèrent plus du lot 1F que sur la ligne « 1 à 4 : choisir le scénario » (cadre de 187×15 px).
- **Conséquence :**
  - L'agrandissement de la fenêtre ne sert qu'à compenser le nouveau titre. Pour les 42 états capturés, il n'est pas nécessaire au scénario 4.
  - La fiche dit « Les scénarios 1, 2 et 3 restent inchangés ». Leur comportement, leurs ressources et leur carte le sont. Leur présentation ne l'est pas : titre et taille de fenêtre, que le propriétaire verra sous macOS.
  - La ligne « 1 à 4 » est en revanche une conséquence légitime : la touche 4 agit depuis tous les scénarios.
  - Réserve sur ma propre mesure : un message de résultat de 4 lignes dans le scénario 4 dépasserait 640 px même avec l'ancien titre. Je n'en ai observé aucun.
- **Correction suggérée :** revenir au titre du lot 1F et à 640 / 616 (mesuré suffisant). Sinon, déclarer ces changements dans le rapport et les faire valider par le propriétaire.

#### RG-03 — observation — Les tests du moteur ne gardent pas la conservation du numéro de tour par `WithUnit`
- **Emplacement :** `TurnRules.cs:50-54`. Le commentaire dit « Le numéro de tour ne change pas ». `TurnTests.cs:83-84` n'appelle `WithUnit` qu'au tour 1.
- **Preuve :** défaut N1. `dotnet test` donne 64/64, code 0. Le contrôle fumée donne 2 échecs, code 1, car il se déplace au tour 3.
- **Conséquence :** le contrat du moteur n'est gardé que par le contrôle fumée. Celui-ci tourne en CI (`ci.yml:92`), donc le défaut serait détecté, mais pas par `dotnet test`.
- **Correction suggérée :** une assertion sur `WithUnit` à un tour ≥ 2 dans `TurnTests`.

#### RG-04 — observation — La présence de la commande T dans le panneau du scénario 4 n'est pas contrôlée
- **Emplacement :** `PrototypeScene.cs:355` ; `CheckTurnLine` (`SmokeTest.cs:315-321`) ne vérifie que la ligne « Tour : ».
- **Preuve :** défaut S6. Contrôle fumée 106 OK, code 0. La fiche (§4, Affichage) exige que le panneau présente « les commandes ». Les captures 33 et 37 montrent que la ligne est bien présente dans le code livré.

#### RG-05 — observation — Le « message initial » restauré par R : interprétation jugée fidèle
- **Emplacement :** `PrototypeScene.cs:31` (le message), `:110` (R), `:122` (touche 4).
- **Analyse (inspecté, puis exécuté par S8 et par les vrais événements X11) :**
  - La fiche dit que R « restaure … le message initial ». Le message initial du scénario 4 est celui qu'il affiche à son chargement. Il n'existe pas d'autre chargement : le lancement se fait sur le scénario 1.
  - Utiliser un même texte pour la touche 4 et pour R rend la restauration exacte par construction.
  - L'alternative « Scénario 4 chargé (touche 4). » aurait affiché « (touche 4) » après un appui sur R.
  - Le §3.4 formule la règle de façon générale (« du scénario »). L'implémentation ne l'applique qu'au scénario 4 ; l'appliquer aux scénarios 1 à 3 contredirait « restent inchangés ».
- **Point à signaler au propriétaire :**
  - Le libellé « Scénario 4 dans son état initial : tour 1. » est un texte d'affichage choisi par le développeur, pas une règle.
  - Après R ou 4, l'utilisateur ne peut pas distinguer textuellement laquelle des deux touches a agi. Les deux sont des réinitialisations complètes.
  - Aucune règle inventée n'a été relevée par ailleurs.

#### RG-06 — observation — Documentation non actualisée
- `PrototypeScene.cs:35` dit « dans l'ordre des touches 1, 2 et 3 » alors qu'il y a 4 titres.
- `PrototypeScene.cs:52` dit « Numéro du scénario chargé : 1, 2 ou 3 ».
- `PrototypeScene.cs:11` : ligne de 159 caractères, non repliée comme ses voisines.
- `README.md:107` (section macOS) ne mentionne ni le scénario 4 ni T. La section Limites (`README.md:174` et suivantes) les couvre.
- `README.md:195` dit que ni 4 ni T n'ont été essayés par de vrais événements X11. Cette relecture vient de le faire (voir Méthode) ; le rapport du lot peut le reprendre en le citant.

#### RG-07 — observation — Deux assertions sans pouvoir de détection propre
- `TurnTests.cs:166-168` (`Assert.Same(before, state.Unit)`, tour = 1 après le rejet) ne peut pas échouer. L'immuabilité est garantie par les types : l'essai I1 le prouve (CS0200, CS1729). Ce n'est pas un défaut, mais T09 « sans modification d'état » est établi par le compilateur, pas par le test.
- `TurnTests.cs:90` calcule l'énergie attendue par la formule (`Math.Min(… + 20, 100)`) et non par une constante (53). La fiche ne fixe pour T05 que la position et l'orientation, qui sont bien des constantes. C'est acceptable.

#### RG-08 — observation — Double source d'état dans la scène
- **Emplacement :** `State` et `Turns.Unit` sont synchronisés à la main en trois endroits : `PrototypeScene.cs:287-291`, `:310` et `:331`.
- **Preuve :** une désynchronisation est détectée (S1 : 2 échecs, code 1).
- Le choix reste simple et conforme à « préférer une petite structure dédiée ». Il est néanmoins fragile si d'autres points d'entrée sont ajoutés.

**Constats positifs, exécutés ou inspectés :**
- **Formules :** addition plafonnée sur 64 bits (`TurnRules.cs:74`), sans débordement (T07 avec `int.MaxValue`). Ressources indépendantes (N4–N8 et E5 du développeur détectés).
- **Validations du §3.2 :** toutes présentes et testées (N2, N3, N5, N7).
- **Déroulement :** tour 1, +1, position et orientation conservées (N6 détecté). Fin de tour possible sans action et aux plafonds. Aucune fin de tour automatique (inspecté). `Echo: false` empêche une répétition à la touche maintenue.
- **Architecture :** pas de moteur multi-unités, d'ordonnanceur ni de gestionnaire de phases. Les trois types sont immuables (I1). `Bastion.Simulation` ne dépend pas de Godot.
- **Séparation moteur / client :** le client ne peut pas fabriquer de `TurnState` (CS1729). Il passe par `Start`, `WithUnit` et `EndTurn` et ne fait aucun calcul de récupération (`grep` : aucun `Min`, `60` ni `20` dans la scène).
- **MEC-0003 :** `Movement/` et les tests existants sont inchangés (`diff` vide). Les 46 tests et les 66 contrôles fumée antérieurs réussissent à l'identique.
- **Couverture de T01 à T16 :**
  - moteur : T01–T09, T14, T15 et la part moteur de T05 ;
  - contrôle fumée : T10, T11 (R et 4), T12 (AZERTY), T13 (66 lignes identiques), T05 et T16 ;
  - les valeurs de la fiche sont des constantes : 12/35, 60/55, 60/75, (2,4) E, tour 1.

---

### Ce que je n'ai pas pu vérifier

- **Non vérifié :** l'autorisation du propriétaire (24 novembre 2026, 19:44:40 UTC) et l'horodatage du mandat cités dans `docs/mandates/README.md`. La conversation n'est pas dans le dépôt.
- **Non vérifié :** l'identité de la transcription avec un original. Seule l'empreinte déclarée est confirmée.
- **Non vérifié :** tout essai sur macOS, sur un écran réel ou avec un clavier physique. Les événements X11 ont été injectés par XTest avec un remappage `XChangeKeyboardMapping`, pas avec une vraie disposition XKB `fr`.
- **Non vérifié :** l'exécution en CI GitHub de cet état (rien n'est poussé).
- **Non vérifié :** le rapport `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`, qui n'existe pas encore.
- **Inspecté seulement :** l'absence d'une fin de tour automatique et de tout calcul de récupération dans le client (lecture du code et `grep`, pas de test dédié).
- **Inspecté seulement :** le comportement des messages de résultat de plus de 3 lignes dans le scénario 4 (cf. la réserve de RG-02).

---

### Verdict

**Conforme sous réserves.** L'implémentation est fidèle à MEC-0004 et je n'ai relevé aucune règle inventée. L'architecture est minimale et immuable. Les vérifications annoncées sont reproduites à l'identique : 64 tests, 106 et 148 contrôles fumée, 42 captures identiques au pixel.

Deux réserves sont à corriger ou à faire arbitrer avant le commit :
- **RG-01 :** la zone affichée après une fin de tour n'est pas contrôlée. C'est un angle mort démontré par un défaut non détecté.
- **RG-02 :** le titre et la taille de la fenêtre des scénarios 1 à 3 ont changé sans que ce soit demandé. Mesure faite, l'agrandissement n'est rendu nécessaire que par ce nouveau titre.

RG-03 à RG-08 sont des observations. La validation finale appartient au propriétaire.

Artefacts de la relecture, tous sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g/` :
- journaux : `smoke-headless.log`, `xvfb.log`, `smoke-base.log` ;
- captures : `captures/`, `sab/S5-captures/`, `sab/X1-captures/`, `x11/` ;
- défauts : `sab/*-test.log`, `sab/*-smoke.log` ;
- scripts : `scripts/`.

---

**Traitement des constats :**

| Constat | Classement | Traitement |
|---|---|---|
| RG-01 : zone affichée non contrôlée après une fin de tour | à corriger | **Corrigé.** `EndTurnAsync` compare la zone affichée à `ComputeReachability` du nouvel état. Le défaut S5 (R1) est maintenant détecté. |
| RG-02 : titre et taille de la fenêtre changés pour les scénarios 1 à 3 | à corriger ou à arbitrer | **Titre : corrigé.** Le titre du lot 1F est rétabli dans les scénarios 1 à 3 ; la carte, la légende et le panneau des scénarios 1 à 3 ne diffèrent plus que par la ligne d'aide « 1 à 4 ». Le scénario 4 porte « Bastion — banc d'essai MEC-0004 (lot 1G) », selon l'arbitrage du 25 novembre. **Fenêtre : conservée à 720 pixels, acceptée par le même arbitrage.** Mesuré : au plus 617 pixels sur les 42 captures, ce qui tiendrait dans 640. Calculé : un état du scénario 4 aussi chargé que le pire cas du lot 1F (591 pixels) atteindrait environ 643 pixels (§3.2). |
| RG-03 : `WithUnit` non testé au-delà du tour 1 | observation | **Traité.** Le test `WithUnitKeepsTheTurnNumberAfterTheFirstTurn` est ajouté, et N1 (R3) est maintenant détecté par `dotnet test`. |
| RG-04 : la commande T du panneau n'était pas contrôlée | observation | **Traité.** `CheckTurnLine` exige la ligne « T : terminer le tour » dans le scénario 4 et son absence ailleurs. Le défaut S6 (R2) est maintenant détecté. |
| RG-05 : « message initial » restauré par R | observation | **Conservé.** La relecture juge l'interprétation fidèle ; l'arbitrage du 25 novembre conserve le message, jugé conforme à MEC-0004. |
| RG-06 : documentation non actualisée | observation | **Corrigé.** Les commentaires de `PrototypeScene.cs` (touches 1 à 4, scénario 1 à 4, ligne repliée), la section macOS de la notice (scénario 4 et T non essayés) et la mention des événements X11 (touches 4, T, R et 1 lors de la relecture du lot 1G) sont mis à jour. |
| RG-07 : deux assertions sans pouvoir de détection propre | observation | **Non modifié.** L'immuabilité est garantie par les types, comme la relecture l'a prouvé (CS0200, CS1729). |
| RG-08 : `State` et `Turns.Unit` synchronisés à la main | observation | **Non modifié.** Le choix reste simple, et une désynchronisation est détectée (S1). |

Après ces corrections, puis après la finalisation du 25 novembre, toutes les vérifications du §5 ont été relancées. Les corrections et la finalisation ont ensuite été relues par un second agent indépendant (§6.2).

### 6.2 Seconde relecture, après les corrections et la finalisation

Un second agent, distinct du développeur et du premier relecteur, a relu les corrections faites depuis la première relecture et le titre arbitré le 25 novembre. Il a reçu le texte de l'arbitrage, la première relecture, la copie de l'état qu'elle avait relu et le diff des corrections. Il a recalculé lui-même toutes les différences et relancé les vérifications dans sa propre copie.

Il a lu le rapport du lot dans une version intermédiaire, avant l'ajout de ce paragraphe. Son rapport, tel qu'il l'a écrit dans `relecture-1g-bis/relecture.md`, est reproduit ci-dessous sans modification, entre deux filets.

---

### Seconde relecture indépendante du lot 1G : corrections depuis la première relecture

**Date :** 25 novembre 2026 (de 12:21 à 12:31 UTC environ).
**Objet :** relecture ciblée des corrections apportées depuis la première relecture (RG-01 à RG-08) et de l'arbitrage du titre du panneau. Mandat : `docs/mandates/BASTION-MANDAT-LOT-1G-v1.0-transcription.md`. Fiche : MEC-0004 de `docs/gameplay/GAMEPLAY-DECISIONS.md`.
**Relecteur :** agent distinct du développeur. Je n'ai rien modifié, commité, remisé ni poussé dans `/home/user/bastion`, et je n'y ai lancé aucune compilation. Je ne m'accorde pas la validation finale.
**État relu :**
- branche `claude/lot-1g-implementation-mec-0004`, HEAD = `origin/main` = `1fa2769e309ea74390b678836d3203a16f7e66d4`, rien de commité ;
- arbre de travail relevé à 12:21:37 UTC : 193 fichiers suivis et non suivis, empreintes dans `relecture-1g-bis/hash-avant.txt` ;
- 4 fichiers diffèrent de l'état de la première relecture : `PrototypeScene.cs`, `SmokeTest.cs`, `README.md` du client et `TurnTests.cs`. Leurs empreintes actuelles :

| Fichier | SHA-256 |
|---|---|
| `src/Bastion.Client.Godot/PrototypeScene.cs` | `c5620987768928077b5df6c9fa3f32fd68e2fad3644d9fba7d13b0f7e327a3c6` |
| `src/Bastion.Client.Godot/SmokeTest.cs` | `35d16a714b505843f7ae807731f3d96b298ff641c2769eeb2149976d7b98469b` |
| `src/Bastion.Client.Godot/README.md` | `2181fe00914c8bf84ab8adb86f73cc2f382d40cbee23ede73d437fddc1dcc311` |
| `tests/Bastion.Simulation.Tests/Turns/TurnTests.cs` | `aa691d2efef54dd1377f0f14ae5e533e2b008bc2820e7871955b9000314a4499` |

Tous les chemins de travail cités sont sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/`.

---

### Méthode

- **Copies :**
  - `relecture-1g-bis/repo` : copie de l'arbre actuel, sans `.git`, `bin`, `obj` ni `.godot` ;
  - `relecture-1g-bis/base` : `git archive origin/main`.
- **Intégrité de la référence :** la copie de la première relecture (`relecture-1g/repo`) est encore conforme à ses empreintes (`sha256sum -c relecture-1g/hash-avant.txt`, code 0).
- **Défauts introduits :** un par copie jetable sous `relecture-1g-bis/sab/` (script `relecture-1g-bis/scripts/sabotage.sh`).
- **Mesures d'image :** Pillow, avec `python3 -I`. Scripts dans `relecture-1g-bis/scripts/` : `compare23.py`, `compare_x1.py`, `bords_panneau.py` et `crop_bbox.py`, plus `relecture-1g/scripts/bas_panneau.py`.
- **Dépôt réel en fin de relecture (exécuté) :**
  - empreintes identiques au relevé initial, sauf `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`. Ce rapport, que le développeur rédige en parallèle, a été modifié à 12:23:57 ;
  - `git status --porcelain` inchangé, HEAD et branche inchangés ;
  - `git worktree list` ne montre que le dépôt, aucune remise ;
  - `diff -rq` entre le dépôt réel et ma copie : vide (code 0) ;
  - les artefacts ignorés `src/Bastion.Client.Godot/.godot/mono/temp/obj/*` du dépôt réel portent la date 12:21:37. Je n'ai lancé aucune compilation dans le dépôt réel ; ma première compilation, dans la copie, date de 12:22:57. **Non vérifié :** qu'il s'agisse d'une compilation de la session du développeur.

---

### Commandes exécutées (copie `relecture-1g-bis/repo`, sauf mention)

| Commande | Résultat | Code |
|---|---|---|
| `diff -rq` / `diff -ru` (sans `bin`, `obj`, `.godot`, `.git` ni le rapport) entre `relecture-1g/repo` et l'arbre actuel | 4 fichiers différents. L'ensemble des lignes +/- est identique, après tri, à `lot1g/corrections/corrections-depuis-relecture-1.patch` (`diff` vide) | 1 attendu ; 0 pour la comparaison au patch |
| `dotnet build` ; `dotnet build --no-incremental` | 0 avertissement, 0 erreur | 0 ; 0 |
| `dotnet test` | `Passed: 65, Failed: 0` (64 + 1 nouveau test) | 0 |
| `dotnet test --filter WithUnitKeepsTheTurnNumber…` | 1 test réussi | 0 |
| Forme de la CI : `dotnet build -c Release`, puis `dotnet test --no-build -c Release` | 0 avertissement ; 65 réussis | 0 ; 0 |
| `dotnet format --verify-no-changes` | aucune modification | 0 |
| `bash scripts/harness/test-hooks.sh` | `== 75 tests, 0 échec(s) ==` | 0 |
| Client : `dotnet build <csproj> -c Release`, puis Debug | 0 avertissement, 0 erreur | 0 ; 0 |
| `dotnet format <csproj client> --verify-no-changes` | aucune modification | 0 |
| Contrôle fumée headless (`timeout 300 … --smoke-test`) | 120 `SMOKE OK`, 0 `SMOKE ÉCHEC`, `SMOKE : RÉUSSITE` | 0 |
| Contrôle fumée sous Xvfb avec `--capture` | 162 `SMOKE OK` (120 + 42 captures), 0 échec | 0 |
| `origin/main` (copie `base`) : client Debug, puis contrôle fumée headless | 66 `SMOKE OK`, 0 échec | 0 ; 0 |
| `origin/main` sous Xvfb avec `--capture` | 89 `SMOKE OK` (66 + 23 captures) | 0 |
| `diff` des 66 lignes `SMOKE OK` d'`origin/main` avec les 66 premières de l'arbre actuel | vide | 0 |
| `diff` des lignes `SMOKE` entre la première relecture (106) et maintenant (120) | 10 libellés reformulés (« tour n et commande T affichés »), 10 lignes de titre et 4 lignes de zone ajoutées, rien d'autre | — |
| `git -C /home/user/bastion diff --stat origin/main -- src/Bastion.Simulation/Movement tests/Bastion.Simulation.Tests/Movement .github scripts .claude CLAUDE.md docs/gameplay docs/decisions docs/references` | **vide** ; aucun fichier non suivi dans ces chemins (`git status --porcelain -uall`) | 0 |

**Défauts réintroduits ou nouveaux** (copies jetables de l'arbre actuel ; « fumée » = contrôle fumée headless après compilation Debug, code 0 pour chacune) :

| # | Défaut | Première relecture | Maintenant |
|---|---|---|---|
| N1 | `WithUnit` remet le tour à 1 (`TurnRules.cs`) | `dotnet test` 64/64, **code 0** | `dotnet test` : 1 échec (`WithUnitKeepsTheTurnNumberAfterTheFirstTurn`), **code 1** ; fumée 118 / 2, code 1 |
| S5 | zone figée dès le tour 2 (`Refresh`) | fumée 106 / 0, **code 0** | fumée 116 / 4 (« 12 cases, 23 attendues » ×3, « 8 cases, 23 attendues »), **code 1** |
| S6 | ligne « T : terminer le tour » supprimée | fumée 106 / 0, **code 0** | fumée 114 / 6 (« tour n et commande T affichés … »), **code 1** |
| S6b | ligne T affichée dans tous les scénarios | — | fumée 116 / 4 (« aucun tour ni commande T affichés … »), code 1 |
| T1 | scénario 4 avec l'ancien titre « … de MEC-0003 et MEC-0004 (lots 1D à 1G) » | — | 114 / 6, code 1 |
| T2 | titres inversés (`!=`) | — | 110 / 10, code 1 |
| T3 | faute d'un caractère : « (lots 1G) » | — | 114 / 6, code 1 |
| T4 | tiret simple « - » au lieu de « — » dans le titre du lot 1F | — | 116 / 4, code 1 |
| T5 | titre du scénario 4 dans tous les scénarios | — | 116 / 4, code 1 |

---

### Vérification des corrections

**RG-01 (zone après une fin de tour) : corrigé, exécuté et réussi.**
- `SmokeTest.cs:376-378` compare `scene.Reachability.Zone` à `scene.Model.ComputeReachability(expected.After.Unit).Zone`, à chacune des 4 fins de tour.
- Le défaut d'origine S5 est maintenant détecté (4 échecs, code 1).
- Limite résiduelle : voir RC-03.

**RG-03 (`WithUnit` au-delà du tour 1) : corrigé, exécuté et réussi.**
- Le test `TurnTests.cs:93-104` vérifie le tour 2 conservé, l'unité transmise et le passage au tour 3.
- N1, auparavant invisible pour `dotnet test`, le fait maintenant échouer (code 1).

**RG-04 (commande T dans le panneau) : corrigé, exécuté et réussi.**
- `SmokeTest.cs:317-322` exige « T : terminer le tour\n » dans le scénario 4 et son absence dans les scénarios 1 à 3.
- S6 et la variante inverse S6b sont détectés (codes 1).

**RG-06 (documentation) : corrigé, inspecté.**
- `PrototypeScene.cs:35` et `:52` disent maintenant « 1 à 4 ».
- Le commentaire de classe (`:8-13`) est replié : la ligne de 159 caractères n'existe plus. Il est aussi reformulé, voir RC-05.
- `README.md:107` mentionne le scénario 4 et T pour macOS.
- `README.md:195` reprend fidèlement l'essai X11 de la première relecture : touches 4, T, R et 1.
- `grep` : plus aucune mention de « 1, 2 ou 3 », « 1, 2 et 3 » ou « 1, 2, 3 » dans le client, hors la boucle `SmokeTest.cs:333`, qui est légitime.

**Titre (arbitrage 3) : conforme, exécuté et réussi.**
- **Source :** `PrototypeScene.cs:342-344` affiche « Bastion — banc d'essai de MEC-0003 (lots 1D à 1F) » hors du scénario 4. C'est le texte d'`origin/main` (`PrototypeScene.cs:295`), caractère pour caractère. Le scénario 4 affiche « Bastion — banc d'essai MEC-0004 (lot 1G) », exactement le texte de l'arbitrage.
- **Aucun autre comportement du panneau changé :** dans le diff de `Refresh`, seule l'expression du titre change.
- **Preuve au pixel :** les 42 captures actuelles ont été comparées à celles de l'essai X1 de la première relecture, c'est-à-dire l'état relu avec le seul titre du lot 1F et une fenêtre de 640 px :
  - captures 01 à 32 et 42 : **identiques au pixel** sur 800 × 640 ;
  - captures 33 à 41 : différences limitées au rectangle (594,30)–(728,71), soit les deux lignes du titre ;
  - bande 640–720 : uniforme, couleur du fond, sur les 42 captures.
- **Contrôle fumée du titre :** `SmokeTest.cs:325-329` vérifie la première ligne exacte (`StartsWith(title + "\n")`), 10 fois. Il détecte les cinq défauts de titre essayés (T1 à T5), y compris une faute d'un seul caractère dans chaque titre (codes 1).

**Visibilité du titre dans 720 px : exécuté et réussi (mesure), inspecté (images).**
- **Titre :** sur 2 lignes, « Bastion — banc d'essai » puis « MEC-0004 (lot 1G) » (capture 33 et `relecture-1g-bis/titres.png`, agrandie). Lignes de texte à y = 29–41 et 56–70, x ≤ 703 ; le libellé finit à x = 784.
- **Zone du titre :** identique au pixel dans les captures 33 à 41.
- **Panneau :**
  - bas du texte au plus à y = 617 sur les 42 captures (`34-s4-fin-tour-1`, `bas_panneau.py`), soit une marge de 102 px ;
  - bord droit au plus à x = 777 ;
  - ni la colonne x = 799 ni la ligne y = 719 ne sont touchées (`bords_panneau.py`).
- **Examen à l'œil :** les captures 33 et 37 (cas le plus chargé, compte rendu sur 3 lignes) montrent tout le panneau lisible, jusqu'à « (débogage) ».

**Captures 01 à 23 comparées à `origin/main` : exécuté et réussi.**
- Dans la zone commune de 800 × 640, chaque image diffère par exactement 1 446 pixels, dans un cadre de 187 × 15 px situé en x = 537–724. Ce cadre est à y = 419, 445 ou 471 selon la position de la ligne.
- Une vue agrandie (`relecture-1g-bis/aide-ligne.png`) montre que ce cadre est la ligne d'aide : « 1, 2, 3 : choisir le scénario » devient « 1 à 4 : choisir le scénario ».
- La bande 640–720 est uniforme.

**RG-05, RG-07 et RG-08 : traitement acceptable.**
- **RG-05 :** clos par l'arbitrage 2, qui conserve le message et le juge conforme à MEC-0004.
- **RG-07 :** la première relecture le qualifiait elle-même de « pas un défaut » et d'« acceptable ». Le modifier serait un refactoring, ce que l'arbitrage exclut.
- **RG-08 :** le choix reste simple. Une désynchronisation reste détectée :
  - côté scène, par S1 (première relecture) ;
  - côté moteur, maintenant aussi par `dotnet test` (N1).
- La correction du titre ajoute une nuance, notée en RC-04, sans action requise.

**Périmètre des changements : conforme.**
- Les 4 fichiers modifiés se rattachent tous à RG-01, RG-03, RG-04, RG-06 ou à l'arbitrage du titre.
- `Main.tscn` et `project.godot` n'ont pas changé depuis la première relecture : 720 / 696, acceptés par l'arbitrage 1.
- Aucun refactoring : `_UnhandledInput`, `OrderTo`, `EndTurn`, `LoadScenario` et `ResetScenario` sont inchangés, comme `TurnRules.cs` et `TurnState.cs`.

---

### Constats

**Aucun constat bloquant. Aucun constat sur le code à corriger.**

#### RC-01 — à corriger (rapport du lot, pas le code) — Annexe A : empreintes périmées pour deux fichiers
- **Emplacement :** `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md:635-636`, dans la version lue (modifiée à 12:23:57, SHA-256 `713358659dd9f114286fb5fb25c18a68bb9f7ce62d95c04656447068a5c44af3`).
- **Preuve (exécuté) :**

| Fichier | Annexe A | Arbre actuel |
|---|---|---|
| `PrototypeScene.cs` | `a0844883…` | `c5620987…` |
| `SmokeTest.cs` | `81f0144b…` | `35d16a71…` |

  Les valeurs de l'annexe sont celles de `lot1g/hashes.txt` (24 novembre, 20:11), avant l'arbitrage du titre. Les 8 autres empreintes de l'annexe sont exactes.
- **Correction suggérée :** recalculer l'annexe sur l'arbre final, juste avant la publication.

#### RC-02 — à corriger (rapport du lot) — La seconde relecture est annoncée avant d'avoir eu lieu
- **Emplacement :** le rapport, dans la même version, renvoie trois fois à un « §6.2 » qui n'existe pas (titres : `6.1` seulement) :
  - `:48` « Seconde relecture indépendante … voir §6.2 » ;
  - `:587` « … ont ensuite été relues par un second agent indépendant (§6.2) » ;
  - `:618` (« seconde relecture »).
- **Conséquence :** une vérification est présentée comme faite sans preuve observable (CLAUDE.md §6).
- **Correction suggérée :** insérer le présent rapport au §6.2 avec son verdict réel, puis seulement ensuite garder ces renvois.

#### RC-03 — observation — Ce que la correction de RG-01 couvre exactement
- **Ce qui est couvert :** le contrôle porte sur la propriété `Reachability` (`PrototypeScene.cs:340`). Elle alimente le dessin et la ligne « Cases atteignables » (`:352`) dans la même méthode `Refresh`.
- **Ce qui ne l'est pas (inspecté) :** le texte de cette ligne n'est comparé nulle part (`CheckHud`, `SmokeTest.cs:69-79`), et le dessin n'est contrôlé que par les captures (`SmokeTest.cs:14-15`). C'est un angle mort antérieur au lot 1G, depuis le lot 1D.
- **Suite :** aucune action demandée ; la consigne exclut tout refactoring supplémentaire. La correction est celle que la première relecture suggérait.

#### RC-04 — observation — Deux discriminants du scénario 4 dans `Refresh`
- **Emplacement :** le titre se choisit sur `Scenario == TurnScenario` (`PrototypeScene.cs:342`) ; les lignes « Tour » et « T » sur `Turns is null` (`:346`, `:357`).
- **Pourquoi c'est cohérent :** les deux discriminants sont liés par construction (`ResetScenario`, `:325-331`). `CheckTurnLine` les contrôle ensemble à chaque appel (titre du lot 1F si et seulement si aucun tour), et T2 et T5 le prouvent.
- **Suite :** prolonge RG-08, aucune action.

#### RC-05 — observation — Commentaire de classe reformulé en plus d'être replié
- **Emplacement :** `PrototypeScene.cs:11-13`. Ajouts : « récupérations » et « transmet les ordres et les commandes aux moteurs et affiche leurs résultats ».
- **Appréciation :** c'est exact (fin de tour via `TurnRules.EndTurn`), cela se rattache à RG-06 (documentation non actualisée) et n'a aucun effet sur le code. Ce n'est pas un refactoring.

#### RC-06 — observation, facultative — La notice n'énumère pas les nouveaux contrôles fumée
- **Emplacement :** `README.md:140-147` décrit le contenu du contrôle fumée sans citer le titre, la ligne T ni la zone après une fin de tour.
- **Appréciation :** la phrase « chaque fin de tour est comparée au résultat du moteur de tours » (`:146`) est désormais vraie aussi pour la zone. Ajout possible, non requis.

---

### Ce que je n'ai pas pu vérifier

- **Non vérifié :** l'exécution en CI GitHub de cet état, puisque rien n'est poussé.
- **Non vérifié :** tout essai sur macOS, sur un écran réel, avec une mise à l'échelle HiDPI ou avec un clavier physique. La visibilité du titre n'est établie que sous Xvfb (Mesa llvmpipe), en 800 × 720.
- **Non rejoué :** les vrais événements X11 sur l'état corrigé.
  - **Inspecté :** la gestion des entrées (`_UnhandledInput`) est inchangée depuis la première relecture, qui les avait essayés.
  - **Exécuté :** les touches simulées par `PushInput` dans le contrôle fumée.
- **Non observé :** un compte rendu de 4 lignes dans le scénario 4. Le cas calculé atteint environ 643 px et tiendrait dans 720 ; aucun des 42 états capturés n'en contient.
- **Non vérifié :** la version finale du rapport du lot, en cours de rédaction. Je n'en ai lu que la version modifiée à 12:23:57.
- **Hors champ :** l'authenticité de la transcription du mandat, des autorisations et de l'arbitrage, reçus par la conversation.

---

### Verdict

**Corrections conformes, sous réserve de l'actualisation du rapport du lot.**
- **Corrections prouvées :**
  - RG-01, RG-03 et RG-04 : les défauts d'origine S5, N1 et S6, autrefois muets (code 0), sont maintenant détectés (code 1) ;
  - RG-06 : documentation corrigée (inspecté).
- **Titre :** conforme à l'arbitrage, au caractère près. Il est entièrement visible dans 720 px, sur 2 lignes, et le texte du panneau finit au plus à y = 617. Son contrôle fumée détecte toutes les erreurs essayées, y compris d'un seul caractère.
- **Rien d'autre n'a changé dans le panneau :** au pixel près par rapport à X1.
- **Non-régression :**
  - les 66 premières lignes `SMOKE OK` sont identiques à `origin/main` ;
  - les captures 01 à 23 ne diffèrent de celles d'`origin/main` que par la ligne d'aide « 1 à 4 » ;
  - le périmètre protégé est intact.
- **Traitement des observations :** acceptable pour RG-05, RG-07 et RG-08.
- **Reste à faire avant publication, dans le rapport du lot seulement :** RC-01 (empreintes de l'annexe A) et RC-02 (§6.2 absent mais annoncé).
- **Observations sans action requise :** RC-03 à RC-06.

La validation finale appartient au propriétaire.

**Artefacts**, sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g-bis/` :
- journaux : `smoke-headless.log`, `xvfb.log`, `base-smoke-headless.log`, `base-xvfb.log`, `test.log`, `harness.log` ;
- captures : `captures/`, `base-captures/` ;
- vues : `titres.png`, `aide-ligne.png` ;
- mesures : `bas-panneau.txt`, `bords-panneau.txt` ;
- défauts : `sab/`, `sab-1.log`, `sab-2.log` ;
- différence : `diff-depuis-relecture-1.patch` ;
- empreintes : `hash-avant.txt`.

---

**Traitement des constats :**

| Constat | Classement | Traitement |
|---|---|---|
| RC-01 : empreintes de l'annexe A périmées pour `PrototypeScene.cs` et `SmokeTest.cs` | à corriger (rapport) | **Corrigé.** L'annexe A est recalculée sur l'arbre final, après la relecture. |
| RC-02 : seconde relecture annoncée avant d'avoir eu lieu | à corriger (rapport) | **Corrigé.** Ce §6.2 reproduit la relecture et son verdict ; les renvois du §1, du §6.1 et du §8 désignent désormais une section existante. |
| RC-03 : texte « Cases atteignables » non comparé ; dessin contrôlé par les seules captures | observation | **Non modifié.** L'angle mort existe depuis le lot 1D, et l'arbitrage exclut tout refactoring. Il est reporté au §7. |
| RC-04 : deux critères (`Scenario == TurnScenario` et `Turns is null`) désignent le scénario 4 | observation | **Non modifié.** Les deux critères sont liés par `ResetScenario`, et `CheckTurnLine` les contrôle ensemble. |
| RC-05 : commentaire de classe reformulé en plus d'être replié | observation | **Conservé.** La reformulation relève de RG-06 et n'a aucun effet sur le code. |
| RC-06 : la notice n'énumère pas les nouveaux contrôles fumée | observation facultative | **Non modifié**, pour ne pas étendre la finalisation au-delà de l'arbitrage. |

**Fichiers ignorés `.godot/mono/temp/obj` datés de 12:21:37** (méthode de la relecture) : leur date correspond aux compilations du client lancées par Claude Code dans le dépôt de travail au début de la relecture (§5.1). C'est une constatation d'horodatage seulement. Ces fichiers sont ignorés par Git.

## 7. Limites et contrôles non effectués

- **Essai manuel sous macOS :** l'essai manuel du scénario 4 par le propriétaire **n'a pas eu lieu**. Aucun essai des scénarios 2 à 4 sous macOS.
- **Événements clavier réels :** lors de la relecture, les touches 4, T, R et 1 ont été envoyées par de vrais événements X11 (XTest) sous Xvfb, avec une disposition AZERTY imitée ; le résultat a été inspecté sur des captures. Ce n'est ni un clavier physique ni une disposition XKB complète.
- **Écran réel, clavier et souris physiques :** aucun essai.
- **CI :** rien n'est poussé, donc le contrôle fumée étendu et les 65 tests n'ont pas tourné dans GitHub Actions. La future PR modifiera `src/Bastion.Simulation/` : sa description devra porter une ligne « Traçabilité simulation : MEC-0004 — … », que le contrôle de traçabilité reconnaît depuis le lot 1G-A.
- **Panneau des scénarios 1 à 3 :** seule la ligne d'aide change (« 1 à 4 »), et la fenêtre est plus haute (§3.2), ce que l'arbitrage du 25 novembre accepte. La carte, la légende, le titre, le reste du panneau, l'état, les ressources et les contrôles sont identiques.
- **Notice du client :** elle ne décrit le titre du panneau ni avant ni après ce lot ; elle n'a pas été modifiée pour le titre du scénario 4. Elle n'énumère pas non plus les nouveaux contrôles fumée (RC-06).
- **Ligne « Cases atteignables » et dessin de la zone :** le contrôle fumée compare la zone calculée par la scène, mais ni le texte de cette ligne ni le dessin, contrôlé par les seules captures (RC-03). Cet angle mort existe depuis le lot 1D.
- **Messages de l'orchestrateur :** l'autorisation formelle du 24 novembre et le message de finalisation du 25 novembre sont cités dans ce rapport, mais ne sont pas archivés dans `docs/mandates/`.
- **Registre :** la fiche MEC-0004 reste à l'état « non commencé », puisque ce lot n'a pas le droit de modifier le registre.

## 8. Conformité au mandat

| Exigence | Réalisation | Preuve |
|---|---|---|
| §2 tour initial 1 ; plafonds et récupérations configurables ; validation ; fin de tour explicite ; récupérations ; tour +1 ; position et orientation conservées ; nouvel état immuable | `TurnRules`, `TurnState`, `TurnOutcome` | §3.1, §4, §5.1 |
| §2 profil initial 60, 60, 100, 20 | `TurnRules.Initial` | `InitialProfileIsTheTestProfileOfTheCard` |
| §2 `CreateState` conservé ; petite structure dédiée ; `UnitState` réutilisé ; pas de moteur multi-unités ni d'ordonnanceur ; pas de Godot ; pas de débordement | `Movement/` inchangé ; addition sur 64 bits | §2, §3.1, T07 |
| §3 scénario 4 : carte du scénario 1, (1,4) N, 12/35, tour 1 ; déplacements de MEC-0003 ; T ; touche 4 (AZERTY compris) ; R ; tour affiché seulement dans le scénario 4 ; chemin conservé ; message et ressources actualisés ; aucun calcul dans le client | `PrototypeScene.cs` | §3.2, §5.2 |
| §3 scénarios 1 à 3 conservés | 66 contrôles identiques ; carte, légende et panneau identiques au pixel près, sauf la ligne d'aide | §5.2, §5.3 |
| §4 T01 à T16 ; valeurs fixes en assertions indépendantes ; véritables événements Godot | 19 tests xUnit et 54 contrôles fumée | §4 |
| §5 build, test, format, hooks, contrôles fumée, captures | voir la preuve | §5 |
| §5 relecture indépendante ciblée | « conforme sous réserves » ; réserves traitées | §6 |
| §5 ne pas déclarer l'essai manuel sous macOS | déclaré non effectué | §7 |
| §6 registres, CI, harnais, `CLAUDE.md` et règles des mécaniques intacts ; aucune fonctionnalité hors périmètre | `git diff --stat` vide sur ces chemins | §2 |
| §7 livrables | moteur, scénario 4, tests, contrôles, rapport, mandat archivé, relecture | §2, §6 |
| §8 exécution locale, sans commit, push ni PR | rien n'est commité | `git status` |
| Finalisation : fenêtre de 720 pixels et message de R conservés | inchangés | §3.2 |
| Finalisation : titre du lot 1F dans les scénarios 1 à 3, « Bastion — banc d'essai MEC-0004 (lot 1G) » dans le scénario 4, rien d'autre dans le panneau | choix sur le numéro du scénario ; dix contrôles fumée du titre ; captures | §3.2, §5.2, §5.3 |
| Finalisation : contrôles rejoués, titre entièrement visible, seconde relecture, rapport et empreintes actualisés | 65 tests, hooks, 120 et 162 contrôles fumée, mesure du titre, dix-huit défauts ; relecture ; annexe | §5, §6.2, annexe A |

## 9. Points à décider par le propriétaire

1. **Publication :** commit, push de la branche `claude/lot-1g-implementation-mec-0004` et PR, qui ne sont pas encore autorisés. La description de la PR devra contenir « Traçabilité simulation : MEC-0004 — … ».
2. **État de la fiche MEC-0004 :** passer de « non commencé » à l'état atteint demandera un mandat documentaire distinct, comme le lot 1B l'a fait pour MEC-0003.
3. **Essai manuel :** si vous le souhaitez, essayer le scénario 4 sous macOS. Il n'a pas eu lieu.

**Points tranchés par l'arbitrage du 25 novembre**, et donc retirés de cette liste : le message de la touche R (conservé), la ligne d'aide et la fenêtre de 720 pixels (conservées), le titre du panneau (celui du lot 1F dans les scénarios 1 à 3, celui du lot 1G dans le scénario 4).

## Annexe A — Empreintes SHA-256

| Fichier | Sur `origin/main` (`1fa2769`) | Dans l'arbre de travail du lot |
|---|---|---|
| `src/Bastion.Simulation/Turns/TurnRules.cs` | absent | `c00bd8d83a6011336c2c16bf844eb9b02b757aaf483f6f2c9b8857a7f4b1c7cc` |
| `src/Bastion.Simulation/Turns/TurnState.cs` | absent | `62b829c4b6543e734ce305100d55a55e24831469c3d8f31301462080ac3b2cbd` |
| `tests/Bastion.Simulation.Tests/Turns/TurnTests.cs` | absent | `aa691d2efef54dd1377f0f14ae5e533e2b008bc2820e7871955b9000314a4499` |
| `src/Bastion.Client.Godot/PrototypeScene.cs` | `f767b204fe4575e625aa8e3e86a122006120e051a35416f1f3601ca7d0b29623` | `c5620987768928077b5df6c9fa3f32fd68e2fad3644d9fba7d13b0f7e327a3c6` |
| `src/Bastion.Client.Godot/SmokeTest.cs` | `4af6d1ad2d35031cf1278a70dc3f720b8c7103a953db5748e707010c155841e3` | `35d16a714b505843f7ae807731f3d96b298ff641c2769eeb2149976d7b98469b` |
| `src/Bastion.Client.Godot/README.md` | `82a208e80dbd3becaa701aced8fadbad3e2f73ba1879b253ed29d30805831b8b` | `2181fe00914c8bf84ab8adb86f73cc2f382d40cbee23ede73d437fddc1dcc311` |
| `src/Bastion.Client.Godot/Main.tscn` | `5b101ac563da2c4d50aecbc315cd6ec9fe1d94457fb4571978e8782be21b43e6` | `1ae72a6bd2e18103931d502a6c92719c983582861e570cf25d464231c562b3bb` |
| `src/Bastion.Client.Godot/project.godot` | `e96064e768b9f310fa5e5ac8cb89447a958ad5498f4309adb4b9bd773aef026d` | `9083811d0d2abfbfdfff0a7c84956da0910e96189fb34a1bb8ab036df5e7f42d` |
| `docs/mandates/README.md` | `668fd8eef603a19a924c2e0d0742113874deb1052b2690eb264f981121c569e0` | `8e4ba221240f8dd24f2437fb82ba69e21ab96a89efa9c3e79fd09fb30de64cd5` |
| `docs/mandates/BASTION-MANDAT-LOT-1G-v1.0-transcription.md` | absent | `c792934ef12607aee0b6f3097cc616c419389401106bcdfe881d196e8eda11b1` |

Empreintes recalculées sur l'arbre final, le 25 novembre, après la seconde relecture. Ce rapport ne peut pas porter sa propre empreinte.
