# Bastion — Lot 1F : relecture indépendante ciblée

**Date :** 23 novembre 2026
**Objet :** relecture indépendante du lot 1F (banc d'essai visuel de MEC-0003), demandée au §5.6 du mandat `docs/mandates/BASTION-MANDAT-LOT-1F-v1.0-transcription.md`. Je ne suis pas le développeur, je n'ai rien modifié dans le dépôt et je ne m'accorde pas la validation finale : elle revient au propriétaire.
**Base :** `origin/main` = `ccd3cdf033c1ecc53244b3d9812eecd48ded5235`. `git ls-remote origin refs/heads/main` donne le même SHA (exécuté, code 0).
**État relu :** branche locale `claude/lot-1f-scenarios-mouvement`, HEAD = `ccd3cdf`, rien de commité ni d'indexé. Le diff est dans l'arbre de travail : 6 fichiers modifiés (`PrototypeScene.cs`, `SmokeTest.cs`, `README.md` du client, `Main.tscn`, `project.godot`, `docs/mandates/README.md`) et 2 fichiers non suivis (la transcription du mandat et `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md`).

Légende : **[exécuté, réussi]**, **[exécuté, échoué]**, **[inspecté seulement]**, **[non vérifié]**.

---

## 1. Méthode

### 1.1 Lectures [inspecté seulement]

- `CLAUDE.md` ; le mandat en entier ; le diff complet (`git diff origin/main`) ; les fichiers actuels `PrototypeScene.cs` et `SmokeTest.cs`.
- Le moteur, pour connaître les API utilisées :
  - `TacticalMap.cs` : `WallBetween` ne lève pas d'exception hors de la carte ; `AddWall` refuse une arête de bord ; chaque mur est rangé comme arête E ou S de sa case ouest ou nord ;
  - `MovementModel.cs`, `PathSearch.cs` (la case de départ est retirée de la zone), `StepResults.cs`, `WallType.cs`, `TerrainType.cs`, `MovementRules.cs`.
- La notice du client, le rapport du développeur, l'index `docs/mandates/README.md`, le §3 du mandat 0C (protocole d'archivage) et l'étape « contrôle fumée » de `.github/workflows/ci.yml`.
- Les journaux et le script du développeur, dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/lot1f/`.

### 1.2 Exécutions

Tous mes artefacts sont dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1f/`.

**Conditions d'exécution :**
- Le client a été compilé et lancé dans une copie de l'arbre de travail, `copie/`, faite par `tar` sans `.git`, `bin`, `obj` ni `.godot`. `diff -r` avec le dépôt : identique.
- La référence `main` vient de `git archive origin/main`, dans `main/`.
- Godot 4.7.2 stable .NET est le binaire indiqué dans le mandat de relecture.

**État du dépôt [exécuté, réussi] :**
- Avant toute action, j'ai enregistré `git status --porcelain` et le SHA-256 des 185 fichiers suivis et non suivis.
- À la fin, les deux sont **identiques**. HEAD = `ccd3cdf`, l'index est vide.

**Empreintes [exécuté, réussi] :** `sha256sum` des 7 fichiers de l'annexe A, et `git show origin/main:<f> | sha256sum` pour leur version sur `main`. Les 13 valeurs sont toutes identiques à celles du rapport, dont la transcription : `72f548a7090dec71523b1cb26679985fc6b241cd9fddf32fc77c534c6a295432`.

**Décomptes [exécuté, réussi] :** `git diff --numstat origin/main` donne :
- `PrototypeScene.cs` : 163/19 ;
- `SmokeTest.cs` : 142/1 ;
- `README.md` du client : 46/12 ;
- `Main.tscn` et `project.godot` : 1/1 chacun ;
- `docs/mandates/README.md` : 1/0.

`wc -l` donne 309, 345 et 167 lignes, et la transcription compte 88 lignes. Tout est conforme au rapport.

**Zones protégées [exécuté, réussi] :** `git diff --stat origin/main` sur les chemins suivants ne produit aucune ligne :
- `src/Bastion.Simulation`, `tests` ;
- `.github`, `scripts`, `.claude`, `CLAUDE.md`, `Bastion.slnx` ;
- `docs/gameplay`, `docs/decisions`, `docs/references` ;
- le `.csproj` et les fichiers `*.uid` du client.

`grep -rn InternalsVisibleTo src/` ne trouve rien : le client ne peut utiliser que les API publiques du moteur, ce que sa compilation confirme.

**Compilation et format du client, dans la copie [exécuté, réussi] :**
- `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` : code 0, « 0 Warning(s), 0 Error(s) » ;
- même commande avec `--configuration Release` : code 0, « 0 Warning(s), 0 Error(s) » ;
- `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes --no-restore` : code 0, aucune sortie.

**Contrôle fumée headless [exécuté, réussi] :**
- `timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test` : **code 0**, **48** lignes `SMOKE OK`, « SMOKE : RÉUSSITE ».
- Les lignes `SMOKE` sont identiques, octet pour octet, à `lot1f/smoke1.log`.

**Les 21 contrôles du lot 1D sont inchangés [exécuté, réussi] :**
- Dans le code : de `internal static class SmokeTest` jusqu'à `CheckHud("après la touche R");` (146 lignes), `diff` entre `git show origin/main:…/SmokeTest.cs` et le fichier actuel ne trouve **aucune différence**. Seul le commentaire d'en-tête change.
- À l'exécution : sur `main` (`git archive`), la compilation Debug réussit et le contrôle fumée headless sort avec le code 0 et 21 `SMOKE OK`. Ces 21 lignes sont identiques aux 21 premières du lot 1F.

**Rendu Xvfb [exécuté, réussi] :**
- `timeout 300 xvfb-run -a "$GODOT" --path … -- --smoke-test --capture=<dossier>` :
  - lot 1F : code 0, 66 `SMOKE OK`, 18 captures ;
  - `main` : code 0, 30 `SMOKE OK`, 9 captures.
- Le rendu est en OpenGL 3, avec Mesa llvmpipe, après l'avertissement sur Vulkan.
- Mes 18 captures sont **identiques au pixel près** à celles du développeur (`ImageChops.difference(...).getbbox()` = `None` pour les 18).

**« Scénario 1 identique au pixel près à main » [exécuté, réussi] :**
- Comparaison faite par mon script `outils/compare.py`, sur la zone (0,0)–(527,511), avec Pillow.
- `None` pour les 9 paires `01` à `09` (lot 1F contre `main`), et pour `18-retour-scenario-1` contre `01-initial` de `main`.
- Sur la zone commune, les différences commencent sous la carte, dans la légende (y ≥ 512), ou dans le panneau (x ≥ 528). L'affirmation est confirmée.

**Examen visuel des captures 10, 11, 15 et 18 [exécuté, réussi] :**
- Scénario 2 : mur noir sur l'arête est de (1,4), 23 cases vertes. Après l'ordre : unité en (2,4) orientée SE, panneau « N → SE », 10 TU, 5 d'énergie.
- Scénario 3 : cadre orange en (2,4), cadre brun en (3,4), 6 TU et 3 d'énergie, légende lisible.
- Capture 18 : scénario 1, panneau « chemin : aucun ».
- Ce sont des captures d'un rendu automatisé, non une validation manuelle.

**Vérifications négatives du développeur, rejouées [exécuté, réussi] :**
- `bash lot1f/scripts/negatifs.sh <mon dossier>` : les six défauts A à F compilent, puis le contrôle fumée sort avec le **code 1** pour chacun.
- Le journal produit est identique à `lot1f/negatifs.log`, lignes vides mises à part.

**Mes propres vérifications négatives, absentes du script du développeur [exécuté] :**
- Un défaut par copie jetable, introduit par mon script `outils/sabotage.sh` (remplacement à occurrence unique vérifiée).
- La compilation Debug réussit, puis je lance le contrôle fumée headless.
- Les copies sont supprimées après usage.

| Défaut introduit dans `PrototypeScene.cs` | Résultat du contrôle fumée |
|---|---|
| N1 : `LoadScenario` conserve `LastPath` d'un scénario à l'autre | **non détecté** : code 0, 48 OK ; le journal affiche « SMOKE OK : panneau : scénario 1 et chemin « E » après le retour au scénario 1 » |
| N2 : un ordre refusé remplace `LastPath` par « chemin inventé par le client » | **non détecté** : code 0, 48 OK |
| N3 : chemin mis à jour seulement dans le scénario 2 (`&& Scenario == 2`) | **non détecté** : code 0 ; le journal affiche « SMOKE OK : panneau : scénario 3 et chemin « aucun » après les deux ordres » |
| N4 : mur ajouté au scénario 1, sur l'arête S de (4,0) | **détecté** : code 1, par le seul contrôle « touche 1 : scénario 1 rechargé… murs : (4,0) S standard » |
| N5 : touche reconnue par sa seule position (clause `Keycode` retirée) | **non détecté** : code 0, 48 OK |

**Vrais événements clavier X11 sous Xvfb [exécuté, réussi] :**
- Cette vérification n'a pas été faite par le développeur.
- Sur l'écran `:77`, la disposition est imitée par `XChangeKeyboardMapping` (keycodes 10, 11, 12 → `&`/`1`, `é`/`2`, `"`/`3`), comme le ferait `xmodmap` : `setxkbmap fr` ne s'appliquait pas sous ce Xvfb.
- Le jeu est lancé normalement, sans `--smoke-test`. Les touches sont envoyées par XTest, puis l'écran est capturé par `import`. Scripts : `outils/clavier_x11.py` et `outils/azerty.py`.

Code livré :
- « é » → scénario 2 ; « " » → scénario 3 ; R → « Scénario réinitialisé » (scénario 3 conservé) ; « & » → scénario 1 ;
- Maj+« é » → scénario 2 ;
- touche 3 du pavé numérique (keycode 89) → aucun effet.

Planche : `planche-x11-fr.png`.

Copie où les touches ne sont reconnues que par leur libellé, c'est-à-dire le défaut C du développeur :
- « é » → scénario 2 (**reconnue**) ;
- « " », « & » et Maj+« & » → **non reconnues**.

Planches : `planche-x11-fr-libelle.png` et `planche-x11-fr-libelle2.png`.

Ce n'est ni un clavier physique ni une disposition XKB complète, mais c'est la vraie chaîne d'entrée X11 de Godot.

**Non-régression à la racine, dans le dépôt [exécuté, réussi] :**
- `dotnet build` : code 0, « 0 Warning(s), 0 Error(s) » ;
- `dotnet test` : code 0, « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » ;
- `dotnet format --verify-no-changes` : code 0, aucune sortie ;
- `bash scripts/harness/test-hooks.sh` : code 0, « == 75 tests, 0 échec(s) == ».

`git status` et les empreintes sont inchangés après ces commandes.

**Archivage [exécuté, réussi] :**
- `cmp` entre la transcription et `lot1f/mandat.md` : identiques.
- La ligne d'index compte 6 champs, comme les 20 lignes du tableau.
- Elle reprend la formule du protocole 0C (§3) : « transcription depuis la conversation… identité avec un fichier original non vérifiée ». Sa forme suit la ligne du lot 1E.
- Le statut cité, « PRÉPARÉ — exécution non autorisée », correspond à la ligne 3 de la transcription.

**CI [inspecté seulement] :** l'étape fumée sort avec le code de Godot (`exit "$code"`) et ne fait aucune hypothèse sur le nombre de contrôles. Les 27 contrôles nouveaux y tourneront sans modifier le workflow.

---

## 2. Constats

### RX-01 — à corriger : l'effacement du chemin au changement de scénario n'est pas gardé, et trois lignes « chemin » du contrôle fumée s'appuient sur la valeur qu'elles vérifient

**Emplacement :** `src/Bastion.Client.Godot/SmokeTest.cs:168-175` (`CheckScenario`), utilisée en `:227`, `:245` et `:261` ; contrôles `:182`, `:219` et `:258`.

**Description :**
- `CheckScenario` vérifie que le panneau contient « Chemin du dernier ordre exécuté : {scene.LastPath} ». La valeur attendue est donc lue dans la scène elle-même : le contrôle prouve que le panneau recopie `LastPath`, pas que `LastPath` est juste.
- `LastPath` n'est comparé à une valeur attendue qu'en deux endroits du scénario 2 : en `:182` (« aucun ») et en `:201-202` (chemin du moteur).
- Or en `:182`, `LastPath` vaut déjà « aucun » avant la touche 2, puisque la touche R vient d'être pressée en `:162`. Ce contrôle passe donc même si le changement de scénario n'efface rien.
- `:219` (touche 3) et `:258` (touche 1) ne vérifient pas `LastPath`.

**Preuve :**
- N1 [exécuté] : `LoadScenario` conserve `LastPath`. Résultat : code 0, 48 OK. Le panneau du scénario 1 rechargé montre le chemin « E » du scénario 3, et la ligne `SMOKE OK : panneau : scénario 1 et chemin « E » après le retour au scénario 1` passe.
- N3 [exécuté] : chemin jamais mis à jour dans le scénario 3. Résultat : code 0, et la ligne `SMOKE OK : panneau : scénario 3 et chemin « aucun » après les deux ordres` passe.

**Conséquences :**
- Le rapport du développeur présente comme vérifiées les lignes « chemin « aucun » au chargement du scénario 3 », « chemin « E » après les deux ordres » et « chemin « aucun » après le retour au scénario 1 » (§4.2, lignes 138, 142 et 147). Elles ne vérifient que la recopie.
- §3.3 l. 94 : « le changement de scénario l'efface ». C'est vrai dans le code [inspecté] et sur la capture 18 [exécuté], mais une régression passerait au vert.
- Le défaut F du §4.4 (l. 194), intitulé « touche R et changement de scénario… », est détecté à cause de la touche R : les deux chemins passent par `ResetScenario`. Sa détection ne prouve rien sur le changement de scénario seul.
- Le §5.3 du mandat (« vérifier… les changements de scénario ») n'est couvert qu'en partie pour le chemin. L'état, la carte, la zone et le numéro du scénario sont bien gardés.

**Correction suggérée :**
- comparer `scene.LastPath` à « aucun » au chargement du scénario 3 et au retour au scénario 1, depuis un état où le chemin n'est pas déjà « aucun » ;
- le comparer au chemin d'`expectedVeryDifficult.Path` après les ordres du scénario 3 ;
- reformuler le libellé du défaut F.

### RX-02 — observation : « un ordre refusé ne modifie pas le chemin affiché » n'est gardé par aucun contrôle

**Emplacement :** `PrototypeScene.cs:266-269` ; rapport §3.3 l. 94.

**Description :**
- Le comportement est juste [inspecté seulement] : `LastPath` n'est mis à jour que si `outcome.Path` n'est pas `null`.
- Mais aucun clic refusé n'a lieu, dans les scénarios 2 et 3, après un ordre exécuté dont le chemin serait ensuite vérifié.

**Preuve :** N2 [exécuté]. Avec un faux chemin écrit à chaque refus : code 0, 48 OK.

**Conséquence :** l'affichage du « dernier ordre exécuté » exigé par le mandat (§2, scénario 2) peut régresser sans qu'aucun contrôle échoue.

**Correction suggérée :** dans le scénario 2, après l'ordre vers (2,4), cliquer une destination hors de la zone puis vérifier que `LastPath` est inchangé.

### RX-03 — observation : la reconnaissance par libellé n'est pas isolée par les tests, et le rapport surestime la nécessité de la position pour la touche 2

**Emplacement :**
- `PrototypeScene.cs:188-204`, en particulier le commentaire de `:189-190` (« par son libellé (clavier QWERTY) ») ;
- `README.md:163` du client (« vérifiées… avec le libellé d'un clavier QWERTY ») ;
- rapport §3.2 l. 79 (« sans la position, elles ne seraient pas reconnues ») ;
- `SmokeTest.cs:178`.

**Description :**
- La touche 2 est simulée avec `Keycode = Key2` **et** `PhysicalKeycode = Key2`. Retirer la clause `Keycode` ne change donc rien au contrôle fumée.
- Sur un vrai clavier QWERTY, la position suffit d'ailleurs. La clause `Keycode` ne sert que pour une disposition où les chiffres sont ailleurs, et ce cas n'est pas testé.
- Sous X11, la disposition AZERTY imitée montre que « é » est reconnue sans la position. Godot donne sans doute `Key2` faute de constante pour « é » ; c'est une inférence, pas une mesure. « & » et « " » ne sont pas reconnues sans la position : le choix de conception est donc justifié pour les touches 1 et 3.

**Preuve :**
- N5 [exécuté] : code 0, 48 OK.
- Planches X11 [exécuté] : en libellé seul, « é » charge le scénario 2 ; « " », « & » et Maj+« & » sont sans effet.

**Conséquence :** aucune sur le comportement livré. Avec la position, les trois touches fonctionnent, avec ou sans Maj, et R aussi : planche `planche-x11-fr.png`. Seules les phrases citées sont imprécises.

**Correction suggérée :** nuancer la phrase du rapport (« les touches 1 et 3 ne seraient pas reconnues ») et celle de la notice (le libellé seul n'est pas isolé par un contrôle).

### RX-04 — observation : le chemin affiché est le chemin planifié, et non les pas réellement exécutés

**Emplacement :** `PrototypeScene.cs:266-269` (`outcome.Path.Steps`).

**Description [inspecté seulement] :**
- Si un ordre de la zone était interrompu en cours d'exécution (`Execution.Completed == false`), le panneau afficherait sous « dernier ordre exécuté » la totalité du chemin prévu.
- Avec ce moteur, ce cas ne peut pas se produire : `ExecuteOrder` exécute le chemin issu de `ComputeReachability`, sur le même modèle et avec les mêmes coûts.
- Le libellé du mandat (« directions choisies par le moteur ») est respecté.

**Conséquence :** aucune aujourd'hui. Le libellé pourrait devenir trompeur si le moteur introduisait un jour des interruptions.

**Correction suggérée :** aucune dans ce lot. À garder en tête.

### RX-05 — observation : le dessin des terrains et la légende ne connaissent que les trois terrains actuels

**Emplacement :** `PrototypeScene.cs:206-210` (`TerrainColor`) et `:250` (« Sans cadre : terrain normal »).

**Description [inspecté seulement] :** un autre `TerrainType` serait dessiné sans cadre et présenté comme « normal » par la légende. Avec des données fixes, c'est sans effet ; aucune règle n'est en jeu.

**Correction suggérée :** aucune dans ce lot.

### RX-06 — observation : imprécisions mineures du rapport du développeur

**Emplacement :** `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md`.

- **l. 175 :** « seule (4,0) est hors de la zone ». La case de l'unité, (1,4), est aussi hors de la zone, par construction du moteur (`PathSearch.cs:84`) : 25 − 23 = 2 [exécuté, capture 10].
- **l. 243 (§8) :** le défaut E est cité comme preuve qu'« aucune règle [n'est] dans le client ». E montre que la scène ne retouche pas l'état rendu ; il ne prouve pas l'absence de règle. Le rapport et `SmokeTest.cs:13-14` le disent d'ailleurs : seule la lecture du code l'établit. Ma lecture [inspecté seulement] confirme qu'aucun calcul de chemin, de coût, de collision ou de rotation ne se trouve dans le client.
- **l. 58 et l. 222 :** le fichier de relecture et le §6 restent à compléter (« En cours »).

**Correction suggérée :** retouches de forme.

---

## 3. Conformité au mandat

Chaque point indique sur quoi repose la conclusion.

**§2 Scénarios :**
- **Scène unique et touches 1, 2 et 3 :** exécuté (contrôle fumée et X11).
- **Scénario 1 strictement conservé :**
  - données (`BuildMap(1)` = `Block(3,2)`, `MovementRules.Initial`, `StandardHuman`, état initial identique) : inspecté ;
  - comportement et contrôles : exécutés (21 contrôles identiques à `main`, carte identique au pixel près, N4 détecté).
- **Scénario 2 :** mur affiché, pas direct refusé par `WallOnEdge`, (2,4) atteinte par N → SE, chemin affiché. Exécuté.
- **Scénario 3 :** 14/7 puis 6/3, comparés à `ExecuteOrder` et aux constantes du mandat (`SmokeTest.cs:236,243`) ; couleurs et légende. Exécuté.

**§3 Interface :**
- touches, R, clic, numéro du scénario, commandes, TU, énergie, orientation et résultat : exécuté (captures) ;
- murs et terrains lus par `WallBetween` et `TerrainAt` : inspecté ;
- présentation 2D minimale : inspecté.

**Lecture des murs :** les arêtes E et S de chaque case, avec les bornes `column + 1 < Columns` et `row + 1 < Rows`. C'est exhaustif, puisque le constructeur range tout mur entre deux cases de la carte comme arête E ou S de sa case ouest ou nord (`TacticalMap.cs:61-71,137-144`). Inspecté.

**§4 Architecture et contraintes :**
- simulation, tests, CI, harnais, `Bastion.slnx` et registres inchangés : exécuté ;
- API publiques seulement : exécuté (compilation, aucun `InternalsVisibleTo`) ;
- aucune règle de jeu dans le client, ni framework, ni chargeur, ni configuration externe : inspecté.

**§5 Vérifications :** couvertes, avec la réserve RX-01 sur le chemin lors d'un changement de scénario. Aucune validation manuelle n'est déclarée.

**§6 Livrables :** présents ; la relecture est ce document.

**§7 Autorisations :** rien n'est commité ni poussé (exécuté).

**Touches 1, 2 et 3 :**
- Pas de double déclenchement [inspecté et exécuté] : seul l'appui est traité (`Pressed: true, Echo: false`), et un événement ne donne qu'un seul `LoadScenario`.
- Pas de conflit avec R [inspecté et exécuté] : R est testée d'abord, par son libellé, et fonctionne sous la disposition AZERTY imitée en X11.
- Touches non voulues [inspecté seulement] : Ctrl, Alt ou Maj combinées à 1, 2 ou 3 chargent aussi un scénario ; c'est sans conséquence.
- Pavé numérique : sans effet (exécuté sous X11).

---

## 4. Ce que je n'ai pas pu vérifier

- **Fidélité de la transcription au message du propriétaire** (13:32:13 UTC) et **heure de l'autorisation** (13:33:54 UTC) [non vérifié] :
  - ma lecture du journal de session a été refusée par le système de permissions ;
  - j'ai seulement vérifié l'identité avec l'extraction du développeur (`lot1f/mandat.md`) et l'empreinte.
- **Clavier physique, écran réel, macOS et Windows** [non vérifié]. Mon essai X11 imite une disposition AZERTY par la table de touches du serveur, et non par une disposition XKB complète.
- **CI GitHub Actions avec le contrôle étendu** [non vérifié] : rien n'est poussé.
- **Première compilation en échec (CS1002)**, citée au §4.1 du rapport [non vérifié] : il n'en reste aucune trace consultable.
- **Dessin des murs et des terrains** [non vérifié automatiquement] : seulement l'examen visuel de captures d'un rendu automatisé, ce qui ne vaut pas validation manuelle.

---

## 5. Verdict

**Conforme sous réserves.**

**Justification :**
- J'ai rejoué le comportement livré et il est conforme au mandat :
  - contrôle fumée headless : 48 contrôles, code 0 ;
  - 21 contrôles du lot 1D identiques, dans le code et dans leur sortie ;
  - carte du scénario 1 identique au pixel près à `main` ;
  - valeurs 14/7 puis 6/3 obtenues par le moteur ;
  - mur contourné par le moteur ;
  - touches 1, 2, 3 et R fonctionnelles par la vraie chaîne d'entrée X11 ;
  - non-régression à la racine : 46 tests, 75 tests des hooks, format conforme.
- Les six vérifications négatives du développeur se reproduisent à l'identique.
- Aucun constat n'est bloquant.
- **Réserve à lever (RX-01) :** l'effacement du chemin au changement de scénario n'est gardé par aucun contrôle, et trois lignes « chemin » du contrôle fumée s'appuient sur la valeur qu'elles vérifient. Le rapport du développeur les présente pourtant comme vérifiées.
- RX-02 à RX-06 sont des observations.

La validation finale appartient au propriétaire.

---

<!-- Seconde relecture : rapport d'un second agent indépendant, copié sans modification à la suite du premier. -->

# Seconde relecture ciblée (corrections après la première relecture)

**Date :** 23 novembre 2026
**Objet :** le propriétaire a demandé une relecture indépendante ciblée des corrections apportées après la première relecture du lot 1F : RX-01, et les nouveaux contrôles censés détecter les défauts introduits. Il a aussi demandé de vérifier que les essais non effectués (macOS, écran réel) sont documentés explicitement. Je ne suis ni le développeur ni l'auteur de la première relecture. Je n'ai rien modifié dans le dépôt et je ne m'accorde pas la validation finale : elle revient au propriétaire.
**Base :** `origin/main` = `ccd3cdf033c1ecc53244b3d9812eecd48ded5235` ; HEAD au même SHA ; index vide.
**État relu :**
- branche locale `claude/lot-1f-scenarios-mouvement`, rien de commité ;
- corrections = différence entre la copie conservée par la première relecture (`…/scratchpad/relecture-1f/copie/`) et l'arbre de travail actuel ;
- empreintes SHA-256 des fichiers relus :
  - `SmokeTest.cs` : `f23e6cdc…2b71` ;
  - `README.md` du client : `ed2859f8…b947` ;
  - rapport `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md` : `a08cac52…dfb2`.

Légende : **[exécuté, réussi]**, **[exécuté, échoué]**, **[inspecté seulement]**, **[non vérifié]**. Pour un défaut volontaire, « détecté » signifie que le contrôle fumée sort avec le code 1, ce qui est le résultat recherché.

Mes artefacts sont dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1f-bis/` :
- journaux `*.log` ;
- captures `cap/` ;
- scripts `outils/defaut.sh` et `outils/cmp.py`.

---

## 1. Méthode

### 1.1 Lectures [inspecté seulement]

- `CLAUDE.md`, le mandat 1F et la première relecture (RX-01 à RX-06).
- Le rapport du développeur en entier et la notice du client en entier.
- `SmokeTest.cs` actuel en entier, et `PrototypeScene.cs`, inchangé depuis la première relecture.
- Le diff `copie → arbre actuel` de `SmokeTest.cs` et de `README.md`.
- Le script `lot1f/scripts/negatifs.sh` et son journal `negatifs2.log`.
- Le script `sabotage.sh` de la première relecture. Ses remplacements exacts N1 à N5 n'ont pas été archivés : j'ai donc écrit mes propres formulations, d'après les descriptions de RX-01 à RX-03.

### 1.2 Exécutions

**État du dépôt [exécuté, réussi] :**
- `git status --porcelain` et `sha256sum` des 186 fichiers suivis et non suivis, avant et après : `diff` vide pour les deux.
- HEAD reste `ccd3cdf` et l'index reste vide.
- Le client n'a été compilé et lancé que dans des copies (`tar` sans `.git`, `bin`, `obj` ni `.godot`). La copie de travail est identique au dépôt (`diff -r`, code 0).
- Les copies jetables des défauts ont été supprimées : `ls` → « No such file or directory ».

**Périmètre des corrections [exécuté, réussi] :**
- `diff -rq -x .git -x bin -x obj -x .godot <copie 1re relecture> <dépôt>` signale seulement :
  - `SmokeTest.cs`, `README.md` du client et `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md` (modifiés) ;
  - `LOT-1F-SCENARIOS-MOUVEMENT-RELECTURE.md` (ajouté depuis).
- `sha256sum` : `PrototypeScene.cs` (`f767b204…`), `Main.tscn` (`5b101ac5…`) et `project.godot` (`e96064e7…`) sont identiques dans la copie et dans le dépôt.
- `git diff --stat origin/main` sur la simulation, `tests`, `.github`, `scripts`, `.claude`, `CLAUDE.md`, `Bastion.slnx`, `docs/gameplay|decisions|references`, le `.csproj` et les `*.uid` : 0 ligne. `git status --porcelain` sur ces chemins : 0 ligne.
- Le diff de `SmokeTest.cs` ne touche que le contrôle fumée, qui ne s'exécute qu'avec `--smoke-test`. Aucune fonctionnalité n'est ajoutée à la scène.

**21 contrôles du lot 1D [exécuté, réussi] :**
- Dans le code : le bloc compris entre `internal static class SmokeTest` et `CheckHud("après la touche R");` (146 lignes) est identique dans `git show origin/main:…/SmokeTest.cs` et dans le fichier actuel (`diff`, code 0). Le reste du diff est le commentaire d'en-tête et du code ajouté à la suite.
- Dans la sortie, j'ai rejoué `main` moi-même : `git archive origin/main`, puis compilation Debug (code 0, « 0 Warning(s), 0 Error(s) »), puis contrôle fumée headless (code 0, 21 `SMOKE OK`). Ces 21 lignes sont identiques aux 21 premières du lot 1F (`diff`, code 0).

**Compilation et format du client, dans la copie [exécuté, réussi] :**
- `dotnet build src/Bastion.Client.Godot/Bastion.Client.Godot.csproj` : code 0, « 0 Warning(s), 0 Error(s) » ;
- même commande avec `--configuration Release` : code 0, « 0 Warning(s), 0 Error(s) » ;
- `dotnet format src/Bastion.Client.Godot/Bastion.Client.Godot.csproj --verify-no-changes --no-restore` : code 0, sortie vide.

**Contrôle fumée headless [exécuté, réussi] :**
- `timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test` : **code 0**, **60** `SMOKE OK`, 0 `SMOKE ÉCHEC`, « SMOKE : RÉUSSITE ».
- Les 39 lignes 22 à 60 sont identiques, octet pour octet, à la liste du §4.2 du rapport (`diff`, code 0).

**Xvfb [exécuté, réussi] :**
- `timeout 300 xvfb-run -a "$GODOT" --path … -- --smoke-test --capture=<cap>` : code 0, **81** `SMOKE OK`, dont 21 captures, et 0 échec.
- Rendu : OpenGL 3, « Mesa - llvmpipe », après l'erreur Vulkan.
- Sans les lignes de capture, la sortie est identique à la sortie headless.
- Captures :
  - mes 21 captures sont identiques au pixel près à celles du développeur (`lot1f/captures`) : `ImageChops.difference(...).getbbox()` = `None` pour les 21 ;
  - sur la zone (0,0)–(528,512), `01` à `09` sont identiques à `main` (`relecture-1f/cap-main`), de même que `10-s1-chemin` contre `02-ordre-2-4` et `21-retour-scenario-1` contre `01-initial` ;
  - témoin : `11-scenario-2` contre `01-initial` de `main` donne la boîte `(213, 215, 407, 504)`, la comparaison sait donc trouver une différence.
- Examen visuel de `10`, `13` et `08` : panneau « E », puis « N → SE » après le refus de (4,0), puis « N → N » après le second ordre du scénario 1.

**Défauts volontaires, un par copie jetable** (script `outils/defaut.sh` : remplacement à occurrence unique vérifiée, `diff` affiché, compilation Debug, contrôle fumée headless). Chaque compilation : code 0, 0 avertissement.

| Défaut introduit dans `PrototypeScene.cs` | Résultat |
|---|---|
| N1 : `LoadScenario` garde `LastPath` | **détecté**, code 1, 56 OK. Premiers échecs : « touche 2 : scénario 2 chargé… » ; « chemin « aucun » attendu au chargement du scénario 2 (affiché : « E ») » ; idem scénario 3 (« N → SE ») et retour au scénario 1 (« E ») |
| N2 : un refus écrit « chemin inventé par le client » | **détecté**, code 1, 59 OK : « chemin « N → SE » attendu après l'ordre refusé (affiché : « chemin inventé par le client ») » |
| N2b : un refus efface le chemin | **détecté**, code 1, 59 OK (affiché : « aucun ») |
| N3 : chemin mis à jour seulement si `Scenario == 2` | **détecté**, code 1, 57 OK : scénario 1 « E » ; scénario 3 « E » après les deux ordres ; scénario 3 « E » après le nouvel ordre |
| N5 : clause `Keycode` retirée | **détecté**, code 1, 49 OK : « touche 2 : scénario 2 chargé, état initial (2,4), E, 16 TU, 8 d'énergie » |
| L1 : seul le chargement du scénario 1 garde le chemin (R et touches 2, 3 l'effacent) | **détecté**, code 1, 59 OK : « scénario 1, chemin « aucun » attendu après le retour au scénario 1 (affiché : « E ») » |
| L2 : idem pour le seul scénario 2 | **détecté**, code 1, 58 OK |
| L3 : idem pour le seul scénario 3 | **détecté**, code 1, 59 OK (affiché : « N → SE ») |
| C : clause `PhysicalKeycode` retirée | **détecté**, code 1, 50 OK, à la touche 3 |
| C1 : position ignorée pour la seule touche 1 | **détecté**, code 1, 58 OK, à la touche 1 |
| P : le panneau formate le chemin autrement que `LastPath` (`Replace(" → ", ", ")`) | **détecté**, code 1, 57 OK |
| **K** : le chemin n'est mis à jour que s'il vaut « aucun » (`&& LastPath == NoPath`) | **non détecté** : code 0, **60 OK**, « SMOKE : RÉUSSITE » (RY-01) |
| **M** : toute touche autre que R, 1, 2 ou 3 charge le scénario 1 (`return null;` → `return 1;`) | **non détecté** : code 0, **60 OK** (RY-05) |

**Script du développeur, rejoué [exécuté, réussi] :**
- `bash lot1f/scripts/negatifs.sh <mon dossier>` : les dix défauts A à J compilent (code 0), puis le contrôle fumée sort avec le code 1 pour chacun.
- Mon journal est identique à `lot1f/negatifs2.log`, lignes vides mises à part (`diff`, code 0).

**Rendu Markdown, avec un outil local [exécuté] :**
- `sed -n '159,181p' README.md | pandoc -f gfm -t html` ;
- même commande sur le §7 du rapport, lignes 296 à 312.

Je n'ai rien envoyé à GitHub.

**Chiffres et empreintes [exécuté] :**
- `git diff --numstat origin/main` ;
- `wc -l` ;
- `sha256sum` des fichiers de l'annexe A, et `git show origin/main:<f> | sha256sum` pour leur version sur `main`.

**Non-régression à la racine, dans le dépôt [exécuté, réussi] :**
- `dotnet build` : code 0, « 0 Warning(s), 0 Error(s) » ;
- `dotnet test` : code 0, « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » ;
- `dotnet format --verify-no-changes` : code 0, sortie vide ;
- `bash scripts/harness/test-hooks.sh` : code 0, « == 75 tests, 0 échec(s) == ».

Ces commandes ne réécrivent que des sorties de compilation ignorées (`bin/`, `obj/` de la simulation et des tests). `git status` et les 186 empreintes sont inchangés.

---

## 2. Vérification des corrections annoncées

**RX-01 : corrigé, avec la limite RY-01.**
- `CheckScenario` (`SmokeTest.cs:169-176`) reçoit `expectedPath` et exige à la fois `scene.LastPath == expectedPath` et un panneau contenant `Chemin du dernier ordre exécuté : {expectedPath}\n` [inspecté].
- Les valeurs attendues viennent de `PathText(OrderOutcome)`, c'est-à-dire du moteur, ou du littéral « aucun ». Aucune n'est lue dans la scène [inspecté].
- Chaque changement de scénario part d'un chemin affiché qui n'est pas « aucun » [exécuté] :
  - « E » avant la touche 2 (`:184`) ;
  - « N → SE » avant la touche 3 (`:234`) ;
  - « E » avant la touche 1 (`:278`).
- Le chemin est vérifié après les ordres du scénario 3 (`:268`) et après chaque R des scénarios 2 et 3 (`:227`, `:230`, `:274`) [exécuté].
- N1, L1, L2 et L3 sont détectés : chaque changement de scénario est gardé séparément [exécuté].
- P est détecté : la clause sur le texte du panneau porte réellement [exécuté].

**RX-02 : traité.**
- `:216-223` : la précondition `!expectedRefusal.InZone` est établie dans le test.
- Le message attendu (« Ordre refusé : … ») diffère du message précédent, ce qui prouve que le clic est arrivé.
- L'état reste `afterDetour`, et le chemin « N → SE » est vérifié par `CheckScenario`.
- N2 et N2b sont détectés [exécuté].

**RX-03 : traité.**
- Les touches sont envoyées ainsi :
  - touche 2 : `PressKey(scene, Key.Key2, Key.None)` (`:188`) ;
  - touche 3 : `Quotedbl`/`Key3` (`:238`) ;
  - touche 1 : `Ampersand`/`Key1` (`:281`).
- N5 est détecté : `PushInput` ne complète donc pas `PhysicalKeycode`. C (touche 3) et C1 (touche 1 seule) sont détectés. Chaque clause de reconnaissance est isolée [exécuté].
- Le commentaire `PrototypeScene.cs:189-190` (« clavier QWERTY ») est inchangé. La correction suggérée par RX-03 ne le visait pas.

**Contrôles ajoutés : non tautologiques**, sauf la limite RY-01. Chacun a été mis en échec par au moins un défaut, à l'exception de la propriété visée par K.

---

## 3. Constats

### RY-01 — à corriger : la propriété « *dernier* ordre exécuté » n'est gardée par aucun contrôle ; le contrôle « après les deux ordres » ne peut pas distinguer le premier ordre du second

**Emplacement :**
- `src/Bastion.Client.Godot/SmokeTest.cs:255-268`, contrôle `:268` ;
- contrôles « chemin » `:184`, `:214`, `:223`, `:234`, `:278` ;
- comportement en `PrototypeScene.cs:266-269`.

**Description :**
- Chaque contrôle du chemin fait après un ordre exécuté suit soit un chargement ou un R, où le chemin valait « aucun », soit, en `:268`, un premier ordre dont le chemin est identique (« E » puis « E »).
- Le remplacement d'un chemin affiché par celui d'un ordre exécuté ensuite n'est donc jamais mis à l'épreuve.
- Le scénario 1 contient bien deux ordres consécutifs (« E », puis « N → N »), mais dans la partie du lot 1D, qui ne contrôle aucun chemin et doit rester inchangée.
- C'est le même type de faiblesse que RX-01 : une prémisse non établie.

**Preuve :**
- [exécuté] Défaut K `if (outcome.Path is not null && LastPath == NoPath)` : compilation code 0, puis contrôle fumée **code 0, 60 OK**, « SMOKE : RÉUSSITE ».
- La ligne `SMOKE OK : panneau : scénario 3, chemin « E » attendu après les deux ordres (affiché : « E »)` passe.
- Le comportement livré est juste : la capture `08-ordre-2-2` affiche « N → N » après le second ordre [exécuté, capture]. `OrderTo` met à jour le chemin à chaque ordre exécuté [inspecté].

**Conséquence :** une régression du mot « dernier », exigé par le mandat (§2, scénario 2 : « pour le dernier ordre exécuté »), passerait la CI au vert. La notice (`README.md:132`) et le rapport (§4.2, l. 155) présentent le contrôle du scénario 3 comme une comparaison au chemin du moteur. C'est exact à la lettre, mais il ne prouve rien sur le remplacement.

**Correction suggérée :** dans la partie 1F, un contrôle après un second ordre consécutif dont le chemin diffère du précédent.

### RY-02 — à corriger : la section « Essais non effectués » de la notice se fond, une fois rendue, dans la liste des limites qui la suit

**Emplacement :** `src/Bastion.Client.Godot/README.md:161-166`.

**Description :** la liste des essais non effectués (`:162-164`) et la liste suivante (`:166-181`) ne sont séparées que par une ligne vide. En CommonMark et en GFM, cela forme une seule liste.

**Preuve :**
- [exécuté] `pandoc -f gfm` produit **un seul `<ul>` de 11 éléments**, sous « Essais non effectués pour le lot 1F ». On y trouve :
  - « Linux x86_64 : vérifié en mode headless… » ;
  - « Scénarios 2 et 3 : vérifiés en local… » ;
  - une seconde entrée macOS : « six essais manuels déclarés conformes… ».
- Témoin : le §7 du rapport (l. 298-312) intercale « **Autres limites :** » et se rend en deux listes distinctes.

**Conséquence :** la mention explicite demandée par le propriétaire devient contradictoire à la lecture rendue. Une même liste « non effectués » annonce « macOS : aucun essai » puis « macOS : six essais… conformes », et énumère des vérifications faites. Le rendu GitHub lui-même n'a pas été vérifié ; c'est une déduction tirée de la spécification et de pandoc.

**Correction suggérée :** séparer les deux listes, comme au §7 du rapport.

### RY-03 — à corriger : décompte et empreinte de la notice périmés dans le rapport

**Emplacement :**
- `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md:54`, qui indique « +55 −12 » ;
- même fichier, `:349` (annexe A), qui indique `2b52ec38…a5b2`.

**Preuve [exécuté] :**
- `git diff --numstat origin/main` donne `60	12	src/Bastion.Client.Godot/README.md`.
- `sha256sum` donne `ed2859f85a002dfa5095bfca6c62a31b7afe1187c0f36724961352fb3503b947`.
- En retirant de la notice actuelle les 5 lignes `:161-165` (la section « Essais non effectués »), on obtient exactement `2b52ec385c7f1f242b9012134e6ef03b78a8f9cba24201b79aabb78cadb7a5b2`. L'annexe A et le décompte précèdent donc cet ajout.
- Les autres valeurs sont exactes :
  - empreintes de l'annexe : les 7 autres côté lot et les 6 côté `main` ;
  - `PrototypeScene.cs` : +163 −19, 309 lignes ;
  - `SmokeTest.cs` : +167 −1, 370 lignes ;
  - transcription : 88 lignes ; relecture : 304 lignes ;
  - 60 et 39 contrôles, 81 `SMOKE OK` sous Xvfb, 21 captures, dix défauts détectés.

**Conséquence :** la référence d'intégrité ne correspond pas à la notice livrée. Quelqu'un qui la vérifierait conclurait que le fichier a été altéré.

### RY-04 — observation : passages du rapport à mettre à jour, et petites imprécisions

**Emplacement :** `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md`.

- **l. 294** : « Le correctif n'a pas été relu une seconde fois par un agent indépendant » devient faux après cette relecture.
- **l. 38 et l. 332** : « réserve levée » est une déclaration du développeur. Cette relecture confirme les points de RX-01, mais signale RY-01, de même nature.
- **l. 58 et l. 354** : si ce texte est ajouté à la suite de `LOT-1F-SCENARIOS-MOUVEMENT-RELECTURE.md`, « 304 lignes » et l'empreinte `798d8b97…` deviendront fausses.
- **l. 232-233** (défauts F et G) : le premier contrôle en échec est « touche 2 : scénario 2 chargé, état initial (1,4), N, 20 TU, 10 d'énergie » (`negatifs2.log`, et mon N1 [exécuté]). La ligne « panneau … au chargement » citée par le rapport n'est que la seconde.

### RY-05 — observation : aucune touche « sans effet » n'est envoyée ; une reconnaissance qui accepterait toute touche passe au vert

**Emplacement :** `PrototypeScene.cs:203` (`return null;`, jamais exercé) ; `SmokeTest.cs`, qui n'envoie que R, 1, 2 et 3.

**Preuve :** [exécuté] défaut M (`return 1;`) : code 0, 60 OK.

**Conséquence :**
- Une régression où Espace, une lettre ou le pavé numérique rechargerait le scénario 1 ne serait pas détectée.
- « Le pavé numérique n'est pas pris en charge » (`README.md:32`) ne repose que sur l'essai X11 de la première relecture. Il porte sur le même `PrototypeScene.cs` (empreinte `f767b204…` identique), mais n'est garanti par aucun contrôle automatique.

**Correction suggérée :** facultative. Envoyer une touche qui ne doit avoir aucun effet, et vérifier que le scénario et l'état ne changent pas.

### RY-06 — observation : le message de `CheckScenario` présente `LastPath` comme la valeur « affichée »

**Emplacement :** `SmokeTest.cs:175` (`(affiché : « {scene.LastPath} »)`).

**Preuve :** [exécuté] avec le défaut P, la ligne d'échec est `SMOKE ÉCHEC : panneau : scénario 2, chemin « N → SE » attendu après l'ordre vers (2,4) (affiché : « N → SE »)`. La valeur attendue et la valeur « affichée » y sont identiques, alors que le panneau montre « N, SE ».

**Conséquence :** la détection n'est pas affectée, mais le diagnostic est trompeur.

---

## 4. Ce que je n'ai pas pu vérifier

- **macOS, écran réel, clavier et souris physiques, Windows** [non vérifié] : aucun moyen ici. Je constate seulement que le rapport (§7, l. 298-302) et la notice (`:161-164`) les déclarent non essayés. Le §1 (l. 40-44) et le §4 du rapport n'affirment rien de plus [inspecté]. La notice garde son titre « Linux (vérifié … dans la CI …) » (`:71`), repris tel quel de `main`. La CI y est nuancée pour le lot 1F en `:172`.
- **Rendu Markdown sur GitHub** [non vérifié] : pandoc seulement, en local. Je n'ai rien envoyé à un service extérieur.
- **Vrais événements clavier X11** [non rejoué] : `PrototypeScene.cs` a la même empreinte qu'à la première relecture ; ses résultats X11 portent donc sur le même code.
- **CI GitHub Actions** [non vérifié] : rien n'est poussé.
- **Remplacements exacts N1 à N5 de la première relecture** [non vérifié] : ils ne sont pas archivés. J'ai rejoué des formulations équivalentes, plus des variantes (N2b, L1 à L3, C1).
- **Transcription du mandat et heure de l'autorisation** : hors du périmètre de cette relecture. Seule l'empreinte `72f548a7…` est reconfirmée.

---

## 5. Verdict

**Conforme sous réserves.**

**Justification :**
- Les corrections restent dans leur périmètre : `SmokeTest.cs`, la notice et le rapport. La scène, `Main.tscn`, `project.godot`, la simulation, la CI, le harnais et les registres sont identiques.
- Les 21 contrôles du lot 1D sont inchangés, dans le code comme dans la sortie, que j'ai rejouée sur `main`.
- RX-01, RX-02 et RX-03 sont réellement corrigés :
  - N1, N2, N3 et N5, qui passaient au vert, sont détectés ;
  - chaque changement de scénario, chaque voie de reconnaissance et la clause sur le panneau sont mis en échec par un défaut ciblé ;
  - les dix défauts du développeur se reproduisent à l'identique.
- Chiffres reproduits : 60 contrôles (code 0), 81 `SMOKE OK` et 21 captures sous Xvfb, identiques au pixel près ; non-régression avec 46 tests et 75 tests des hooks ; format conforme.
- **Réserves, sans constat bloquant :**
  - **RY-01** : le caractère « dernier » du chemin affiché n'est pas gardé (défaut K au vert), une faiblesse de même nature que RX-01 ;
  - **RY-02** : la mention explicite des essais non effectués se rend de façon contradictoire dans la notice ;
  - **RY-03** : l'empreinte de la notice dans l'annexe A et son décompte sont périmés.
- RY-04 à RY-06 sont des observations.

La validation finale appartient au propriétaire.

---

<!-- Troisième relecture : rapport d'un troisième agent indépendant, copié sans modification à la suite des deux premiers. -->

# Troisième relecture ciblée (corrections RY-01 à RY-06)

**Date :** 23 novembre 2026
**Objet :** relecture indépendante des seules corrections faites après la seconde relecture du lot 1F (constats RY-01 à RY-06). Je ne suis ni le développeur ni l'auteur des deux relectures précédentes. Je n'ai rien modifié dans le dépôt et je ne m'accorde pas la validation finale.
**Base :** `origin/main` = HEAD = `ccd3cdf033c1ecc53244b3d9812eecd48ded5235`, index vide, branche `claude/lot-1f-scenarios-mouvement`, rien de commité.

**État relu (SHA-256) :**
- `SmokeTest.cs` : `4af6d1ad…41e3` (la seconde relecture avait relu `f23e6cdc…`) ;
- `README.md` du client : `82a208e8…b8b` (avant : `ed2859f8…`) ;
- `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md` : `588400d4…c5c` (avant : `a08cac52…`) ;
- `LOT-1F-SCENARIOS-MOUVEMENT-RELECTURE.md` : `83528348…a7f` ;
- inchangés : `PrototypeScene.cs` `f767b204…`, `Main.tscn` `5b101ac5…`, `project.godot` `e96064e7…`.

Légende : **[exécuté, réussi]**, **[exécuté, échoué]**, **[inspecté seulement]**, **[non vérifié]**. Pour un défaut volontaire, « détecté » veut dire que le contrôle fumée sort avec le code 1, ce qui est le résultat recherché.

Artefacts : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1f-ter/` (journaux `*.log`, captures `cap/` et `cap-main/`, scripts `outils/defaut.sh` et `outils/cmp.py`).

---

## 1. Méthode

### 1.1 Périmètre des corrections [exécuté, réussi]

- `diff -rq -x .git -x bin -x obj -x .godot` entre la copie de la seconde relecture (`relecture-1f-bis/copie`, empreintes `f23e6cdc`, `ed2859f8`, `a08cac52` vérifiées) et le dépôt. Seuls quatre fichiers diffèrent : `SmokeTest.cs`, le `README.md` du client, le rapport, et `…-RELECTURE.md` (où la seconde relecture a été ajoutée).
- `git diff --stat origin/main` sur la simulation, `tests`, `.github`, `scripts`, `.claude`, `CLAUDE.md`, `Bastion.slnx`, les registres, le `.csproj` et les `*.uid` : 0 ligne. `git status --porcelain` sur ces chemins : 0 ligne.
- Diff de `SmokeTest.cs` depuis `f23e6cdc` : trois ajouts seulement.
  - `:175-176` et `:180-182` : message de `CheckScenario` et `PathLine` (RY-06).
  - `:229-237` : second ordre vers (3,4) (RY-01).
  - `:294-302` : touches sans effet (RY-05).
- **21 contrôles du lot 1D :** le bloc compris entre `internal static class SmokeTest` et `CheckHud("après la touche R");` (146 lignes) est identique à `git show origin/main:…/SmokeTest.cs` (`diff`, code 0). Seule ligne retirée par rapport à `main` : l'en-tête du commentaire de documentation.

### 1.2 Compilation, format et contrôle fumée, dans une copie `tar` sans `.git`, `bin`, `obj` ni `.godot` (`diff -r` : code 0) [exécuté, réussi]

- `dotnet build …/Bastion.Client.Godot.csproj` : code 0, « 0 Warning(s), 0 Error(s) ». Même résultat en `--configuration Release`.
- `dotnet format …/Bastion.Client.Godot.csproj --verify-no-changes --no-restore` : code 0, sortie vide.
- `timeout 300 "$GODOT" --headless --path src/Bastion.Client.Godot -- --smoke-test` : **code 0, 66 `SMOKE OK`**, 0 échec, « SMOKE : RÉUSSITE ».
- Les lignes 22 à 67 de ma sortie sont identiques, octet pour octet, aux lignes 127 à 172 du rapport (§4.2) (`diff`, code 0).
- **`main` rejoué** (`git archive origin/main`, compilation Debug code 0, 0 avertissement ; contrôle fumée code 0, 21 OK) : les 21 lignes sont identiques aux 21 premières du lot (`diff`, code 0).
- **Xvfb** (`xvfb-run -a … --capture=<dossier>`) : code 0, **89 `SMOKE OK`, dont 23 captures**, 0 échec. Rendu OpenGL 3 llvmpipe, après l'erreur Vulkan. Sans les lignes de capture, la sortie est identique à la sortie headless.
- **Captures** (Pillow, zone (0,0)–(528,512)) :
  - `01` à `09` sont identiques à mes propres captures de `main` ;
  - `10-s1-chemin` est identique à `02-ordre-2-4` de `main`, et `23-retour-scenario-1` à `01-initial` de `main` ;
  - témoin : `11-scenario-2` contre `01-initial` donne la boîte `(213, 215, 407, 504)` ;
  - mes 23 captures sont identiques, image entière, à celles du développeur (`lot1f/captures`).
- Examen visuel de `14-s2-ordre-3-4` : (3,4), E, 6 TU, 3 d'énergie, « Chemin du dernier ordre exécuté : E ».

### 1.3 Défauts volontaires, un par copie jetable

Script `outils/defaut.sh` : remplacement à occurrence unique vérifiée, `diff` affiché, compilation Debug, contrôle fumée headless, puis suppression de la copie. Chaque compilation : code 0, 0 avertissement.

| Défaut introduit dans `PrototypeScene.cs` | Résultat |
|---|---|
| **K** `if (outcome.Path is not null && LastPath == NoPath)` | **détecté**, code 1, 65 OK : `SMOKE ÉCHEC : panneau : scénario 2, chemin « E » attendu après le second ordre (LastPath : « N → SE » ; panneau : « Chemin du dernier ordre exécuté : N → SE »)` |
| **M** `return null;` → `return 1;` dans `ScenarioKey` | **détecté**, code 1, 64 OK : `touche 1 du pavé numérique et espace : aucun effet ((1,4), N, 20 TU, 10 d'énergie)`, puis le chemin « aucun » au lieu de « E » |
| K2 (nouveau, RY-01) : chemin remplacé seulement par un chemin d'au moins autant de pas (`&& outcome.Path.Steps.Count >= LastPath.Split(" → ").Length`) | **détecté**, code 1, 65 OK, même ligne que K |
| M1 (nouveau, RY-05) : en tête de `ScenarioKey`, `if (key.Keycode == Key.Space) return 1;` | **détecté**, code 1, 64 OK. La barre d'espace atteint donc bien `ScenarioKey` |
| M2 (nouveau, RY-05) : pavé reconnu (`\|\| key.Keycode == Key.Kp0 + scenario`) | **détecté**, code 1, 64 OK. `Kp1` atteint donc bien la boucle de `ScenarioKey` |
| M3 (nouveau, RY-05) : Espace agit comme R | **détecté**, code 1, 64 OK |
| P (RY-06) : le panneau joint les directions par « , » | **détecté**, code 1, 63 OK. Le message montre désormais l'écart : `(LastPath : « N → SE » ; panneau : « Chemin du dernier ordre exécuté : N, SE »)` |
| P2 (RY-06) : ligne « Chemin… » retirée du panneau | **détecté**, code 1, 53 OK, avec le message `panneau : « (ligne absente) »` |

**Script du développeur, rejoué** (`bash lot1f/scripts/negatifs.sh <mon dossier>`) [exécuté, réussi] :
- les 12 cas (A à M, sans L) compilent avec le code 0 ;
- le contrôle fumée sort avec le code 1 dans les 12 cas ;
- mon journal est identique à `lot1f/negatifs3.log`, lignes vides mises à part (`diff`, code 0).

### 1.4 Notice et rapport

- `sed -n '161,$p' README.md | pandoc -f gfm -t html`, puis décompte des `<li>` de premier niveau (`html.parser`) [exécuté, réussi] : **2 listes, de 3 et 7 éléments**.
- `git diff --numstat origin/main`, `wc -l`, `sha256sum` et `git show origin/main:<f> | sha256sum` [exécuté, réussi].
- Comparaison des extraits du §4.4 au journal rejoué [exécuté] ; lecture du diff du rapport depuis `a08cac52` [inspecté].

### 1.5 Non-régression à la racine, dans la copie [exécuté, réussi]

- `dotnet build` : code 0, 0 avertissement.
- `dotnet test --no-build` : code 0, « Passed: 46, Total: 46 ».
- `dotnet format --verify-no-changes` : code 0, sortie vide.
- `Bastion.slnx` ne contient pas le client, donc ces commandes ne dépendent pas des corrections relues.
- `test-hooks.sh` n'a pas été relancé : le harnais n'a pas changé.

### 1.6 État du dépôt [exécuté, réussi]

- `git status --porcelain` (9 lignes) et `sha256sum` des 186 fichiers suivis et non suivis, avant et après : `diff` vide pour les deux.
- HEAD reste `ccd3cdf`, l'index reste vide.
- Le dossier ignoré `src/Bastion.Client.Godot/.godot` date du 22 novembre : aucun fichier n'y est plus récent que mon début de relecture.

---

## 2. Vérification des corrections

**RY-01 : corrigé** (`SmokeTest.cs:229-237`).
- Le second ordre part de `afterDetour` (2,4) vers (3,4). Le chemin du moteur est « E », celui du premier ordre « N → SE » : les chemins diffèrent réellement.
- La prémisse est établie dans le test, à partir du moteur (`PathText(expectedSecond) != PathText(expectedDetour)`, `:234`).
- K et K2 sont détectés par ce seul contrôle `:237`. Aucun contrôle du lot 1D n'est touché.

**RY-05 : traité** (`:294-302`).
- `Kp1` et `Space` passent le test `Key.R`, puis traversent la boucle de `ScenarioKey` sans correspondance : ils exercent donc bien `return null`.
- M, M1, M2 et M3 sont détectés. Chaque touche est prouvée arriver séparément (M1 pour Espace, M2 pour `Kp1`).

**RY-06 : corrigé** (`:175-176`, `:180-182`). Avec P et P2, le message montre la ligne réellement affichée. La condition du contrôle n'a pas changé.

**RY-02 : corrigé** (`README.md:168`). La liste « Essais non effectués » se rend seule, avec ses 3 éléments : macOS, écran réel, clavier et souris physiques.

**RY-03 : corrigé.**
- §2 : `numstat` donne `164/19` → non : `163 19` pour `PrototypeScene.cs` (309 lignes) et `191 1` pour `SmokeTest.cs` (394 lignes) ;
- `64 12` pour `README.md` (185 lignes) ; `1 1` pour `Main.tscn` et pour `project.godot` ; `1 0` pour `docs/mandates/README.md` ;
- transcription : 88 lignes ; relecture : 576 lignes ;
- les 16 empreintes de l'annexe A sont exactes, 8 sur `main` ou absentes et 8 dans l'arbre de travail.

**RY-04 : traité, sauf RZ-02 et RZ-03.**
- Les chiffres du §1, du §4.3 et du §6.2 (66, 45, 89, 23 captures, douze défauts, répartition 6 + 4 + 2) sont reproduits.
- Le premier échec de F et G est désormais exact.

---

## 3. Constats

### RZ-01 — à corriger : le rapport deviendra faux dès que cette relecture sera ajoutée

**Emplacement :** `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md` :
- `:9` (« relu deux fois ») ;
- `:39` et `:346` (« n'ont pas été relues par un troisième agent ») ;
- `:59` (« 576 lignes ») ;
- `:384` (« deux relectures ») ;
- `:406` (empreinte `83528348…`).

**Preuve [exécuté] :** aujourd'hui, `wc -l` donne 576 et `sha256sum` donne `83528348…a7f`. Les deux valeurs changeront mécaniquement quand ce texte sera copié à la suite.

**Conséquence :** la référence d'intégrité de l'annexe A ne correspondra plus au fichier livré, et trois phrases nieront une relecture qui aura eu lieu. C'est le même mécanisme que RY-03 et RY-04.

**Correction suggérée :** recalculer ces valeurs et ces phrases après la copie de ce rapport.

### RZ-02 — observation : deux extraits du §4.4 citent l'ancien format du message

**Emplacement :** `LOT-1F-SCENARIOS-MOUVEMENT.md:240` (défaut D) et `:244` (défaut H), qui citent « (affiché : « … ») ».

**Preuve [exécuté] :** mon rejeu de `negatifs.sh`, identique à `negatifs3.log`, donne :
- `(LastPath : « aucun » ; panneau : « Chemin du dernier ordre exécuté : aucun »)` pour D ;
- `(LastPath : « chemin inventé par le client » ; panneau : « … chemin inventé par le client »)` pour H.

**Conséquence :** ces deux extraits ne viennent pas de la sortie actuelle. Ils reprennent précisément le mot « affiché » que RY-06 a corrigé. La détection n'est pas en cause.

### RZ-03 — observation : la seconde relecture a introduit treize défauts, et non douze

**Emplacement :** `LOT-1F-SCENARIOS-MOUVEMENT.md:321` (« douze défauts à lui »).

**Preuve [exécuté] :** le tableau de la seconde relecture (`…-RELECTURE.md:386-398`) compte 13 lignes : N1, N2, N2b, N3, N5, L1, L2, L3, C, C1, P, K et M.

### RZ-04 — observation : le rapport a changé au-delà des corrections annoncées

**Emplacement :** `LOT-1F-SCENARIOS-MOUVEMENT.md` : `:8` (autorisation de publication et ses conditions), `:9`, `:45`, `:362`, `:387` et `:391`.

**Preuve [inspecté] :** diff depuis `a08cac52`. Ces passages ne relèvent ni des chiffres, ni du §6.2, ni de l'annexe A.

**Conséquence :** l'existence et les termes du message « BASTION — Lot 1F — Autorisation de publication » ne sont pas vérifiables ici. Le propriétaire est seul à pouvoir les confirmer.

### RZ-05 — observation : l'arrivée des touches sans effet n'est prouvée que par sabotage

**Emplacement :** `SmokeTest.cs:297-302`.

**Constat :**
- Contrairement aux clics refusés, dont le message change, une touche sans effet ne laisse aucune trace observable.
- Si `Kp1` ou Espace cessaient un jour d'atteindre `_UnhandledInput` (par exemple, un contrôle d'interface qui prendrait le focus et consommerait Espace), le contrôle passerait au vert sans rien vérifier.
- Aujourd'hui, M1 et M2 établissent que les deux touches arrivent [exécuté].

C'est une limite structurelle. Aucune correction n'est exigée.

---

## 4. Ce que je n'ai pas pu vérifier

- **Rendu de la notice sur GitHub** [non vérifié] : pandoc seulement, en local. Rien n'a été envoyé à un service extérieur.
- **CI GitHub Actions** [non vérifié] : rien n'est poussé.
- **macOS, Windows, écran réel, clavier et souris physiques** [non vérifié].
- **Événements X11 réels pour `Kp1` et Espace** [non vérifié] : seuls des événements `PushInput` ont été envoyés.
- **Autorisation de publication** citée par le rapport (RZ-04) [non vérifié].
- **Fidélité des deux rapports de relecture recopiés** [inspecté seulement] :
  - la première partie de `…-RELECTURE.md` (l. 1-304) est identique à la version de la copie de la seconde relecture ;
  - la seconde partie (l. 310-576) est identique à `lot1f/seconde-relecture.md` ;
  - je n'ai pas accès au texte original rendu par le second relecteur.
- **`test-hooks.sh`** : non relancé, puisque le harnais n'a pas changé.

---

## 5. Verdict

**Conforme sous réserves.**

- RY-01, RY-05 et RY-06 sont réellement corrigés dans `SmokeTest.cs`, sans toucher les 21 contrôles du lot 1D (dans le code comme dans la sortie, rejouée sur `main`) ni le code de la scène.
- K et M, qui passaient au vert, sont détectés (code 1). Mes quatre défauts nouveaux (K2, M1, M2, M3) sont détectés aussi. Le diagnostic de P et de P2 est désormais exact.
- RY-02 et RY-03 sont corrigés. 66 OK en headless (code 0), 89 OK et 23 captures sous Xvfb, et le §2 et l'annexe A sont reproduits à l'identique.
- **Réserve RZ-01 :** les décomptes, l'empreinte et les mentions de relecture du rapport sont à mettre à jour après l'ajout de ce texte.
- RZ-02 à RZ-05 sont des observations.

La validation finale appartient au propriétaire.

---

**Correction de ma section 2, RY-03 :** la première puce contient un faux départ (« `164/19` → non »). La valeur exacte, mesurée par `git diff --numstat origin/main`, est `163 19` pour `PrototypeScene.cs`. Supprimez « `164/19` → non : » avant la copie dans le dépôt.
