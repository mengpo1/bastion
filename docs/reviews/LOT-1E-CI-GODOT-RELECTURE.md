# Bastion — Lot 1E : relecture indépendante ciblée

**Date :** 23 novembre 2026
**Objet :** relecture du lot 1E (client Godot dans la CI), menée contre le mandat `docs/mandates/BASTION-MANDAT-LOT-1E-v1.0-transcription.md`. Le rapport du développeur, `docs/reviews/LOT-1E-CI-GODOT.md` (non commité, SHA-256 `34b40953…00ce` au moment de la relecture), est traité comme une déclaration, pas comme une preuve.
**Base :** `origin/main` = `535bcaeba84c1769da13817946a596943ca471f1`.
**Commit relu :** `a39b2562dbaaf9af6c9482fdbd18325865a3afb4` sur `claude/lot-1e-ci-godot`. C'est le seul commit au-dessus de la base (`git merge-base` = `535bcae`).
**Relecteur :** agent distinct du développeur. Je n'ai rien modifié dans le dépôt : `git status` est identique avant et après la relecture (seul `?? docs/reviews/LOT-1E-CI-GODOT.md`), HEAD est inchangé et il n'y a aucun stash.

## Méthode

**Lu (inspecté) :**
- `CLAUDE.md` et le mandat en entier ;
- le diff complet `git diff origin/main...HEAD` (4 fichiers) ;
- `ci.yml`, `README.md`, `SmokeTest.cs`, `PrototypeScene.cs`, `Main.tscn`, `project.godot` et le `.csproj` du client ;
- `Directory.Build.props`, `global.json`, `Bastion.slnx`, l'index `docs/mandates/README.md` et le protocole d'archivage (LOT-0C §3) ;
- les rapports 1C et 1D ;
- les scripts `rejouer-ci.py` et `negatifs.sh` du développeur et leurs journaux.

**Exécuté.** Tout ce qui suit a été joué par moi. Clones jetables du commit `a39b256` sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1e/`, supprimés à la fin ; journaux conservés dans `…/relecture-1e/logs/`.

1. **API GitHub publique** (codes HTTP 200).
   - Run 45148037933 : `event push`, `conclusion success`, `head_sha a39b2562…`, `run_attempt 1`.
   - Job 137602095716 `build-test` : `ubuntu-24.04`, de 09:32:57 à 09:33:45Z.
   - Les 16 étapes et leurs horodatages sont identiques au tableau §4.3 du rapport.
   - Le journal du job (397 lignes) contient `grep -c 'SMOKE OK'` = **21**, 0 « SMOKE ÉCHEC », puis « SMOKE : RÉUSSITE » et « Contrôle fumée réussi (code 0). ». Il montre aussi `…zip: OK`, `4.7.2.stable.mono.official.ed1daf0bf`, « Passed: 46 », « == 75 tests, 0 échec(s) == », « 0 Warning(s) / 0 Error(s) » en Release et en Debug, l'image `20261116.133.1` et le SDK `10.0.404`.
   - La branche distante est à `a39b256`, `main` à `535bcae`, aucune PR n'existe (`pulls?state=all&head=…` → `[]`) et la branche n'a eu qu'un seul run.
2. **Shell réel du runner :** les 12 étapes `run` du journal portent `shell: /usr/bin/bash -e {0}`.
3. **Intégrité.**
   - `SHA512-SUMS.txt` téléchargé depuis la publication `4.7.2-stable` (HTTP 200) : sa ligne 29 donne `1855960b…8402d13  Godot_v4.7.2-stable_mono_linux_x86_64.zip`, identique au workflow et à `LOT-1C-QUALIFICATION-GODOT-DOTNET.md:31`.
   - La taille de l'archive téléchargée est de 107 698 034 octets, comme au lot 1C.
4. **Empreintes SHA-256 recalculées :**
   - transcription du mandat : `19620b278e21c8743d02bb8888b5274f26366646456617330004a5c02d63b695` (fichier de travail et `git show HEAD:`), égale à l'index ;
   - les 6 empreintes de l'annexe A sont exactes, base et branche ;
   - `PrototypeScene.cs` et `SmokeTest.cs` sont identiques sur `main` et sur `HEAD`.
5. **Étapes existantes :** `diff <(git show origin/main:ci.yml | sed -n '4,$p') <(git show HEAD:ci.yml | sed -n '5,57p')` → aucune différence. Seul l'en-tête de commentaire change (lignes 2 et 3).
6. **Non-régression** dans le dépôt :

   | Commande | Code | Résultat |
   |---|---|---|
   | `dotnet build` | 0 | 0 Warning(s), 0 Error(s) |
   | `dotnet test` | 0 | « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » |
   | `dotnet format --verify-no-changes` | 0 | — |
   | `bash scripts/harness/test-hooks.sh` | 0 | « == 75 tests, 0 échec(s) == » |

7. **Mon propre rejeu.** Script `…/relecture-1e/scripts/rejeu.py`, distinct de celui du développeur : chaque bloc `run` est écrit dans un fichier et lancé par **`bash -e <fichier>`**, comme le runner. `RUNNER_TEMP` et `GITHUB_ENV` sont émulés. Lanceur : `cas.sh <nom> <fichier> <ancien> <nouveau>`, sur un clone neuf de `a39b256`, avec un seul remplacement vérifié (motif présent une fois).

| Cas | Défaut introduit | Étape en échec | Code | Sortie pertinente | Fait par le développeur ? |
|---|---|---|---|---|---|
| A | aucun | — | **0** | 0 Warning(s) en Release et Debug, `…zip: OK`, 21 « SMOKE OK », « Contrôle fumée réussi (code 0). » (0,7 s) | oui (sur `origin/main` + `ci.yml`) |
| B | `_ = int.Parse("sabotage", …)` en tête du `try` de `SmokeTest.RunAsync` | contrôle fumée | **2** | `SMOKE EXCEPTION : System.FormatException…`, `::error::Contrôle fumée : échec (code 2).` | **non** |
| C | `GetNode<Label>("HudAbsent")` dans `PrototypeScene._Ready` | contrôle fumée | **2** | `ERROR: Node not found: "HudAbsent"`, `SMOKE EXCEPTION à l'initialisation de la scène : System.NullReferenceException`, `échec (code 2)` | **non** |
| D | étape « compilation Debug » sautée (Release seule) | contrôle fumée | **124** en **300,0 s** | `ERROR: Cannot instantiate C# script because the associated class could not be found. Script: 'res://PrototypeScene.cs'`, puis le message 124 | **non** |
| E | URL `4.7.9-stable` (inexistante) | installation | **22** (0,4 s) | `curl: (22) The requested URL returned error: 404` ; `GITHUB_ENV` vide, ni `sha512sum` ni `unzip` exécutés | **non** |
| F1 | ligne `curl` remplacée par `true` (archive absente) | installation | **1** | `No such file or directory`, `FAILED open or read`, `WARNING: 1 listed file could not be read` ; `GITHUB_ENV` vide | **non** |
| F2 | archive tronquée à 1 000 000 octets | installation | **1** | `…zip: FAILED`, `WARNING: 1 computed checksum did NOT match` ; pas de dossier `godot/` | **non** (le développeur avait altéré l'empreinte, pas l'archive) |
| H | cible MSBuild `<Warning Text="…"/>` ajoutée au `.csproj` | **aucune** | **0** | « 1 Warning(s), 0 Error(s) » en Release et Debug ; chaîne entière verte | **non** (voir RX-06) |
| I | `int unused = 0;` (reprise du cas du développeur) | compilation Release | **1** | `error CS0219: The variable 'unused' is assigned but its value is never used`, « 0 Warning(s), 1 Error(s) » | oui (confirmé) |

8. **Comparaison des shells.** J'ai lancé le bloc `run` du contrôle fumée, extrait du `ci.yml` du commit, avec un faux binaire `GODOT` qui renvoie un code fixé. Codes essayés : 0, 1, 2, 124, 137 et 255, sous `bash -e` et sous `bash --noprofile --norc -eo pipefail`.
   - Les deux shells donnent des résultats **identiques**.
   - L'étape sort avec le code reçu.
   - 0 donne « réussi », 124 le message de délai, et tous les autres codes `échec (code N)`.
   - Le `|| code=$?` capture le code sous `-e` dans les deux cas.
   - Le pipe `echo | sha512sum -c -` échoue sans pipefail (cas F1, F2), parce que `sha512sum` est la dernière commande du pipe.
9. **`timeout` face à un processus qui ignore SIGTERM** (processus de substitution, pas Godot) :
   - `timeout 2 bash -c 'trap "" TERM; sleep 8'` → code 124 après **8,0 s** ;
   - `timeout -k 1 2 …` → code **137** après 3,0 s.
   - Godot 4.7.2, lui, s'est bien arrêté au SIGTERM : cas D, 300,0 s.

## Constats

**RX-01 — à corriger (rapport) — `docs/reviews/LOT-1E-CI-GODOT.md:97` et `:24`.**
- **Description :** le rapport dit que le rejeu utilise « le shell de GitHub Actions (`bash --noprofile --norc -eo pipefail -c`) ». C'est inexact. Sans `shell:` explicite, le runner emploie `bash -e {0}`, un fichier de script sans pipefail. `rejouer-ci.py:17` ajoute donc `pipefail` et passe par `-c`.
- **Preuve :** le journal du job porte 12 fois `shell: /usr/bin/bash -e {0}`. Mon rejeu fidèle (`bash -e <fichier>`) donne les mêmes codes que celui du développeur (cas A, I) ; la comparaison des shells (Méthode, point 8) est identique ; les cas F1 et F2 échouent sans pipefail.
- **Conséquence :** aucune sur les résultats, mais le rejeu n'était pas une copie exacte du runner, et le rapport le présente comme tel.
- **Correction suggérée :** corriger la phrase. Indiquer que le rejeu a utilisé la variante `shell: bash`, et que l'équivalence avec `bash -e {0}` a été vérifiée en relecture.

**RX-02 — à corriger (notice) — `src/Bastion.Client.Godot/README.md:114`.**
- **Description :** la notice réduit le code 124 à « la scène n'a pas démarré le contrôle ». Or la CI (`ci.yml:95`) dit « La scène n'a pas terminé », et le seul cas 124 du développeur est l'inverse : contrôle exécuté jusqu'au bout (« SMOKE : RÉUSSITE »), puis Godot qui ne quitte pas. Un contrôle bloqué en cours de route donnerait aussi 124. La ligne vient du lot 1D, mais le §2.8 du mandat demande une notice qui reflète *précisément* le périmètre testé, et ce paragraphe décrit justement ce que la CI rapporte.
- **Preuve :** `negatifs.log`, 5e cas (« SMOKE : RÉUSSITE » puis code 124). Mon cas D confirme la cause donnée en exemple par la notice : compilation Release seule → `Cannot instantiate C# script…`, puis 124 en 300,0 s.
- **Conséquence :** un lecteur de la notice peut mal interpréter un 124 en CI.
- **Correction suggérée :** aligner la ligne sur le message de la CI, par exemple « Godot n'a pas quitté dans le délai : scène non démarrée, ou contrôle bloqué ou non terminé ».

**RX-03 — à corriger, mineur (rapport) — `docs/reviews/LOT-1E-CI-GODOT.md:43`.**
- **Description :** la ligne de `README.md` indique « +31 −9 ».
- **Preuve :** `git diff --numstat origin/main...HEAD` donne `32 8 src/Bastion.Client.Godot/README.md`. Les totaux « 129 insertions, 9 suppressions » (ligne 49) sont justes ; c'est la répartition qui est fausse (43+53+1+31 = 128).
- **Correction suggérée :** « +32 −8 ».

**RX-04 — à corriger, mineur (rapport) — `docs/reviews/LOT-1E-CI-GODOT.md:91`.**
- **Description :** « Le délai de 300 s est le même qu'aux lots 1C et 1D. » Rien ne l'établit pour le lot 1C.
- **Preuve :** `grep -c timeout docs/reviews/LOT-1C-QUALIFICATION-GODOT-DOTNET.md` → `0`. Aucune mention de 300 s ni de limite de temps pour Godot dans ce rapport (lignes 104 à 106 : commandes sans `timeout`). `timeout 300` apparaît bien au lot 1D (`LOT-1D-PROTOTYPE-GODOT.md:118-119`).
- **Correction suggérée :** « le même qu'au lot 1D », ou citer la source pour le lot 1C.

**RX-05 — observation — `src/Bastion.Client.Godot/Bastion.Client.Godot.csproj:3`, et `README.md:10` et `:37` à la racine.**
- **Description :** le commentaire du `.csproj` dit encore « Hors de Bastion.slnx et de la CI ». C'est devenu faux pour la CI.
- **Préexistant, hors du lot 1E :** le `README.md` racine dit encore « l'interface Godot n'est pas encore créée » et « Le projet Godot (interface) n'existe pas encore » ; c'est faux depuis le lot 1D.
- **Preuve :** `grep -n` sur ces fichiers ; la CI compile le client (journal, étapes 12 et 15).
- **Conséquence :** documentation contradictoire.
- **À décider par le propriétaire :** le développeur a laissé le `.csproj` intact, ce qui se défend au regard du §3 (« ne modifier aucun comportement du prototype »), même si un commentaire n'est pas un comportement. Corriger dans ce lot (commentaire seul) ou plus tard.

**RX-06 — observation — `ci.yml:63-64` et `:84-85` ; formulation du rapport `LOT-1E-CI-GODOT.md:67`.**
- **Description :** le critère « compilation sans avertissement » est **respecté sur le commit relu** : 0 Warning(s) en Release et en Debug, en CI et en local. En revanche, la CI ne l'**impose** que pour les avertissements du compilateur, via `TreatWarningsAsErrors`. Un avertissement de niveau MSBuild ne fait pas échouer l'étape. Le rapport présente `TreatWarningsAsErrors` comme la garantie du critère, sans cette nuance.
- **Preuve :** cas H → étape « compilation Release » en code 0 avec « 1 Warning(s) », puis toute la chaîne verte. Le cas I (CS0219) est, lui, bloqué (code 1).
- **Conséquence :** une régression qui ne produit qu'un avertissement MSBuild (conflit d'assemblage, avertissement du SDK) passerait en vert. L'étape racine « Compilation », préexistante, a la même limite.
- **Correction suggérée :** nuancer la phrase du rapport. Le durcissement (`-warnaserror` ou `MSBuildTreatWarningsAsErrors`) est à arbitrer par le propriétaire, éventuellement dans un autre mandat.

**RX-07 — observation — `ci.yml:92` (pas de `-k`) et `ci.yml:89-98` (pas de `timeout-minutes`).**
- **Description :** `timeout 300` envoie SIGTERM, puis attend sans limite la fin du processus. Si Godot ignorait SIGTERM, l'étape ne serait bornée que par la limite par défaut du job. Le rapport le déclare honnêtement (`:246`). Ajouter `-k` ne suffirait pas : le code deviendrait 137, que le `case` classerait comme « échec (code 137) » et non comme un délai.
- **Preuve :** Méthode, point 9 (8,0 s au lieu de 2 s, code 124 ; avec `-k 1`, code 137) et faux binaire à 137 (point 8). Godot 4.7.2 réel : arrêt à 300,0 s (cas D).
- **Ambiguïté résiduelle, mineure :** un Godot qui sortirait de lui-même avec 124 serait signalé comme un délai (faux binaire à 124, point 8). `SmokeTest` ne quitte qu'avec 0, 1 ou 2.
- **Conséquence :** aucune constatée avec Godot 4.7.2 ; c'est une limite déclarée.
- **Correction suggérée :** si le propriétaire veut une borne stricte, `timeout-minutes` sur l'étape, qui garde la signification de 124.

**RX-08 — observation, inspecté seulement — `ci.yml:9-11`.**
- **Description :** les étapes du client n'ont pas de condition. Avec le déclencheur `edited`, préexistant, chaque modification de la description d'une PR relancera aussi le téléchargement de l'archive Godot (107 698 034 octets) et le contrôle fumée.
- **Preuve :** lecture du workflow seulement. Aucune PR n'existe, donc ce chemin n'est pas exécuté.
- **Conséquence :** surcoût, et dépendance réseau (déclarée au `:245`) à chaque édition. Ce n'est pas un défaut de conformité.

**Points vérifiés conformes, sans constat :**
- Le périmètre se limite à 4 fichiers. Le client n'est pas ajouté à `Bastion.slnx`. Aucun registre protégé, harnais hors `ci.yml`, code du client ou code de la simulation n'est modifié.
- Les étapes existantes sont identiques octet pour octet, et les nouvelles viennent après elles.
- Aucune action tierce n'est ajoutée, et aucune expression `${{ }}` n'apparaît dans les lignes ajoutées (`grep -c` → 0).
- `GODOT` est bien propagé par `$GITHUB_ENV` : visible dans l'`env:` des étapes 15 et 16 du journal.
- La compilation Debug précède le contrôle fumée.
- Tout code non nul fait échouer l'étape, et 124 a un message distinct qui ne parle pas de contrôle échoué.
- L'intégrité est réellement contrôlée : empreinte fausse, archive absente, archive tronquée et HTTP 404 échouent tous avant `unzip`.
- La notice ne s'étend ni à Windows ni à l'export. Les six essais macOS sont présentés comme « un retour d'utilisateur, et non une reproduction indépendante » (`README.md:82`, `:130`). Le chemin macOS et `gtimeout` sont marqués non vérifiés.
- La ligne d'index est cohérente avec le protocole (« transcription… identité avec un fichier original non vérifiée ») et son empreinte est exacte.

## Ce que je n'ai pas pu vérifier

- **Fidélité de la transcription du mandat** au message du propriétaire (07:07:24 UTC), **horodatage et contenu de l'autorisation** (09:23:17 UTC, option « Autoriser, push du lot »), **confirmation des six essais macOS** (« Oui, ces six essais »). Ma tentative de consulter le journal de session a été refusée par les permissions. Ces trois points restent **non vérifiés**. Seule l'empreinte de la transcription l'est.
- **Les six essais macOS eux-mêmes :** non vérifiés. Je n'ai pas de macOS.
- **Chemin `pull_request` de la CI :** non exécuté (aucune PR).
- **Mauvaise version de Godot** (archive d'une autre version avec son empreinte) : non essayé. La garantie vient de l'empreinte (cas F2 et empreinte fausse du développeur) et de la vérification de version par `SmokeTest`, que j'ai lue mais pas sabotée.
- **Durée du 5e cas négatif du développeur :** non mesurée par lui, et pas rejouée par moi. Mon cas D mesure 300,0 s pour un 124 d'une autre cause.
- **Limite de durée par défaut d'un job GitHub (360 min) :** connue par la documentation, non observée.
- **Rejeu sur le SDK 10.0.404 de la CI :** non fait. En local, le SDK est le 10.0.115 (`dotnet --version`).

## Verdict

**Conforme sous réserves.**

Toutes les exigences du mandat sont remplies, et je les ai vérifiées par exécution :
- CI réelle verte sur `a39b256`, avec un contrôle fumée réellement exécuté et un résultat observable ;
- compilation sans avertissement et format conforme, sur ce commit ;
- défauts intentionnels détectés : cinq par le développeur, et huit cas rejoués par moi, dont sept nouveaux ;
- installation intègre et sans action tierce ;
- codes de sortie correctement propagés, et 124 distingué d'un échec fonctionnel ;
- 46 tests et 75 tests des hooks sans régression ;
- périmètre respecté.

Aucun constat n'est bloquant. Les réserves sont documentaires :
- **RX-01 à RX-04, à corriger :** la description du shell, la notice sur le code 124, et deux chiffres ou références inexacts du rapport ;
- **RX-05 à RX-08 :** observations laissées à l'appréciation du propriétaire.

Je ne m'accorde pas la validation finale : c'est au propriétaire de décider.

**Fichiers utiles :**
- `/home/user/bastion/.github/workflows/ci.yml`
- `/home/user/bastion/src/Bastion.Client.Godot/README.md`
- `/home/user/bastion/docs/reviews/LOT-1E-CI-GODOT.md`
- `/home/user/bastion/src/Bastion.Client.Godot/Bastion.Client.Godot.csproj`
- mes scripts : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1e/scripts/` (`rejeu.py`, `cas.sh`, `remplace.py`)
- journaux des cas A à I : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1e/logs/`
- journal du job CI téléchargé : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1e/job.log`
