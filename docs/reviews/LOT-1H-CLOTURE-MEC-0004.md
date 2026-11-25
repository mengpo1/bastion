# Bastion — Lot 1H : clôture documentaire de MEC-0004

**Date :** 25 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md`. C'est la transcription du message du propriétaire du 2026-11-25T19:47:54Z, extraite mécaniquement du journal de session (SHA-256 `06e26806…b998`) ; son identité avec un fichier original n'est pas vérifiée. Statut du texte : « PRÉPARÉ — exécution soumise à autorisation ».
**Autorisation d'exécution :** message « BASTION — LOT-1H — Autorisation d'exécution » du 2026-11-25T19:36:28Z, reçu avant le texte du mandat.
- **Elle autorise :** l'exécution locale, sur cinq fichiers documentaires seulement, avec dans le registre les seules lignes « Tests de modification » et « État d'implémentation » de MEC-0004.
- **Elle interdit :** commit, push, PR et fusion.
- **Elle est confirmée** par le message « BASTION — LOT-1H — Complément sur les essais macOS » du 2026-11-25T19:48:04Z, qui sert aussi de source déclarative pour les sept essais macOS (annexe A).
**Base :** `origin/main` = `b4e2a4793dd1101ff4b81e6ad404613ec7671838`, commit de fusion de la PR #26, établi par `git fetch origin main` au démarrage.
**Branche :** `claude/lot-1h-cloture-mec-0004`, créée localement à partir de cette base, avec un arbre de travail propre.
**État :** lot exécuté et vérifié localement. **Rien n'est commité ni publié.**

## 1. Résumé

Le lot met la documentation en cohérence avec l'intégration de MEC-0004 par la PR #26. Il est strictement documentaire.
- **Registre :** dans la fiche MEC-0004, deux lignes changent, et seulement elles.
  - **« Tests de modification » :** le texte historique est conservé intégralement, suivi d'une annotation datée du 25 novembre 2026.
  - **« État d'implémentation » :** `non commencé` est remplacé par le texte du §2.B du mandat, suivi de la précision sur les essais macOS.
- **README principal :** MEC-0003 et MEC-0004 y figurent comme deux incréments intégrés. Il mentionne `Bastion.Simulation.Turns` et décrit le prototype à quatre scénarios.
- **Mandat :** archivé tel quel et indexé.
- **Vérifications :** compilation, tests, format et harnais réussis. Le contrôle de traçabilité de la CI lit toujours la fiche modifiée.
- **Relecture indépendante :** « conforme sous réserve de RH-01 », sans constat bloquant. RH-01, une imprécision de la ligne « Tests de modification », est corrigé, et le relecteur a vérifié la correction. Les autres constats sont des observations (§7).

## 2. Périmètre exact

| Fichier | Changement |
|---|---|
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | lignes 649 et 650, dans la fiche MEC-0004 : « Tests de modification » et « État d'implémentation » ; +2 −2 |
| `README.md` | section « État » (+4 −3) et deux lignes du tableau « Contenu » (+2 −2) |
| `docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md` | nouveau : le mandat, tel que reçu (108 lignes) |
| `docs/mandates/README.md` | une ligne d'index ajoutée |
| `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md` | nouveau : ce rapport |

**Inchangés**, vérifiés par `git diff --stat origin/main` sans aucune sortie :
- `src/`, `tests/`, `.github/`, `scripts/`, `.claude/` ;
- `CLAUDE.md`, `Bastion.slnx`, `global.json`, `Directory.Build.props` ;
- `docs/decisions/`, `docs/references/`.

**Dans le registre :** 848 lignes avant et après. La comparaison ligne à ligne ne trouve que les lignes 649 et 650 différentes. L'en-tête, les règles, MEC-0001, MEC-0002 et MEC-0003 sont identiques, de même que le reste de MEC-0004 : en-tête en gras, provenance, autres champs du tableau, sections 2 à 7 et résultats attendus T01 à T16.

## 3. Modifications du registre

### 3.1 « Tests de modification » (§2.A du mandat)

- **Texte historique conservé** : « T01 à T16, définis à la section 6, non encore implémentés. »
- **Annotation datée du 25 novembre 2026, en italique et entre parenthèses**, comme celle de MEC-0003. Elle reprend les points du mandat :
  - les seize scénarios sont désormais couverts ;
  - le moteur dispose de 19 tests xUnit ;
  - le contrôle fumée Godot compte 54 nouveaux contrôles ;
  - la CI de la PR #26 a exécuté avec succès 65 tests .NET et 120 contrôles fumée ;
  - le détail est renvoyé au rapport du lot 1G.
- **Ajouts du développeur**, pris dans le rapport du lot 1G et vérifiables dans le code :
  - la répartition : T01 à T09, T14 et T15 par les tests xUnit ; T05, T10 à T12 et T16 par les nouveaux contrôles fumée ; T13, l'absence de régression, par les 46 tests .NET et les 66 contrôles fumée antérieurs, inchangés. T05 est couvert des deux côtés. La première rédaction attribuait T13 aux nouveaux contrôles ; la relecture l'a relevé (RH-01), et c'est corrigé ;
  - les deux emplacements, `tests/Bastion.Simulation.Tests/Turns/` et `src/Bastion.Client.Godot/SmokeTest.cs`.
- **Date de l'inscription :** l'annotation précise que le texte historique décrit l'état à cette date. Les tests ne sont donc pas présentés comme réalisés à l'inscription.

### 3.2 « État d'implémentation » (§2.B du mandat)

- **Remplacement littéral :** la ligne commence par le texte du mandat, mot pour mot : « intégré — dans main par la PR #26, commit de fusion b4e2a4793dd1101ff4b81e6ad404613ec7671838 (25 novembre 2026). État à la date de l'inscription : non commencé. » Le mandat le donne entre accents graves, comme un littéral. Il est reproduit sans mise en forme ajoutée : contrairement à la fiche MEC-0003, `main` et le commit n'y sont pas en police de code.
- **Phrases ajoutées pour la précision demandée sur les essais macOS :**
  - « Vérifications automatisées : la CI de la PR #26 (ligne « Tests de modification »). »
  - « Essais manuels sous macOS, distincts de ces vérifications : sept contrôles du prototype du lot 1G (scénario 4, anciens scénarios et fenêtre), déclarés satisfaisants par le propriétaire le 25 novembre 2026. »
  - « C'est une déclaration du propriétaire, non reproduite de façon indépendante. »
  - un renvoi à ce rapport.
- **Valeur d'état :** « intégré » figure dans la liste des états du registre (« non commencé · en cours · testé · intégré »).

### 3.3 Ce qui n'est pas modifié

Aucune décision de gameplay et aucun résultat attendu ne change. Les sections 2 à 7 sont intactes. La provenance et la ligne « Décision du propriétaire » sont inchangées. Le périmètre accepté n'est pas élargi.

## 4. README principal

- **Section « État » :**
  - deux incréments de gameplay sont implémentés, testés et intégrés : `MEC-0003` (PR #19) et `MEC-0004` (PR #26) ;
  - la simulation comprend la marche sur terrain plat et, dans `Bastion.Simulation.Turns`, la gestion élémentaire des tours d'une seule unité. Une commande explicite termine le tour, récupère les TU et l'énergie, chacune dans la limite de son plafond, et passe au tour suivant ;
  - `MEC-0001` et `MEC-0002` restent reportées : la phrase est conservée, sur une ligne à part ;
  - le prototype Godot a quatre scénarios fixes de démonstration, trois pour la marche (lot 1F) et un pour la gestion des tours (lot 1G). Le README précise que ce n'est ni un jeu complet ni l'interface finale.
- **Tableau « Contenu » :** `Turns/` est ajouté aux lignes de `src/Bastion.Simulation/` et de `tests/Bastion.Simulation.Tests/`.

## 5. Preuves de tests : contrôles automatisés et essais manuels

### 5.1 Contrôles automatisés (CI GitHub Actions)

Les journaux ont été vérifiés par l'API publique de GitHub (`/actions/runs/<id>/jobs`, puis `/actions/jobs/<id>/logs`).

| Exécution | Événement | Commit | Conclusion | Résultats lus dans le journal |
|---|---|---|---|---|
| [45632937850](https://github.com/mengpo1/bastion/actions/runs/45632937850), job 139270709355 | push de la branche du lot 1G | `38d3d41` | succès | 65 tests .NET réussis ; 75 tests des hooks, 0 échec ; 120 « SMOKE OK », « SMOKE : RÉUSSITE » |
| [45633018137](https://github.com/mengpo1/bastion/actions/runs/45633018137), job 139270971166 | PR #26 | `38d3d41` | succès | mêmes résultats ; « Déclaration MEC-0004 reconnue (fiche présente, décision « acceptée ») » |
| [45683720344](https://github.com/mengpo1/bastion/actions/runs/45683720344), job 139450654733 | push sur `main` | `b4e2a47` (commit de fusion) | succès | 65 tests .NET réussis ; 75 tests des hooks, 0 échec ; 120 « SMOKE OK », « SMOKE : RÉUSSITE » |

L'exécution sur le commit de fusion n'est pas citée dans le registre, qui s'en tient à la CI de la PR #26 comme le mandat le demande. Elle figure ici comme preuve complémentaire (RH-06).

**Cohérence des chiffres :** l'exécution sur la base précédente, `1fa2769` (run 45470444406), compte 46 tests .NET et 66 contrôles fumée. Le lot 1G a donc ajouté 19 tests (46 → 65) et 54 contrôles fumée (66 → 120). L'arbre fusionné, `b4e2a47`, est identique au commit `38d3d41` testé par la CI de la PR : `git diff --stat 38d3d41 b4e2a47` est vide. Ces deux constats viennent de la relecture (C10, C11 et C13).

Le rapport du lot 1G, rédigé avant la publication, indique encore que la CI n'a pas tourné. Ce sont les preuves ci-dessus qui la documentent (RH-03).

### 5.2 Essais manuels sous macOS (déclaration du propriétaire)

Le propriétaire a transmis directement, dans la conversation Bastion le 25 novembre 2026, un compte rendu de sept essais, tous déclarés « Satisfaisant ». Son texte est reproduit à l'annexe A.

1. charger le scénario 4 ;
2. terminer le premier tour ;
3. terminer le deuxième tour ;
4. déplacer puis terminer le tour ;
5. réinitialiser ;
6. vérifier les anciens scénarios ;
7. vérifier la fenêtre.

**Ce que vaut cette preuve :** c'est une déclaration du propriétaire, et non une vérification indépendante de Claude Code. Ces essais sont distincts des six essais du prototype du lot 1D, déclarés le 23 novembre 2026. Le registre et le présent rapport les présentent séparément des contrôles automatisés.

## 6. Contrôles du lot

### 6.1 Commandes

Toutes ont été lancées dans le dépôt de travail et renvoient le code 0.

| Commande | Résultat |
|---|---|
| `git fetch origin main` ; `git rev-parse origin/main HEAD` | `b4e2a4793dd1101ff4b81e6ad404613ec7671838` deux fois ; arbre propre avant le lot |
| `dotnet build` | 0 Warning(s), 0 Error(s) |
| `dotnet test --no-build` | « Passed! - Failed: 0, Passed: 65, Skipped: 0, Total: 65 » |
| `dotnet format --verify-no-changes` | aucune sortie |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |
| `git diff --stat origin/main -- src tests .github scripts .claude CLAUDE.md docs/decisions docs/references Bastion.slnx global.json Directory.Build.props` | aucune sortie |

### 6.2 Lecture du registre par le contrôle de traçabilité de la CI

**Montage :** dans un clone jetable (`git clone --local`), le registre modifié est copié sur la base et une modification factice de `src/Bastion.Simulation/` est commitée. Le dépôt de travail n'est pas touché.

**Résultats de `scripts/harness/check-simulation-trace.sh` :**
- avec une déclaration MEC-0004 : « Déclaration MEC-0004 reconnue (fiche présente, décision « acceptée ») », code 0 ;
- avec une déclaration MEC-0001, comme témoin : « la décision du propriétaire n'est pas « acceptée » », code 1.

### 6.3 Vérifications de l'archive et de l'index

- **Archive :** l'extraction du journal de session est enregistrée avec un saut de ligne final, comme pour les mandats transcrits précédemment. Son SHA-256 est `06e268068c9dbceedbe77ca3a57f078c37f62acffcd6d114251c158b5716b998`.
- **Index :** la ligne ajoutée porte cette empreinte, la provenance « transcription » et les deux messages d'autorisation horodatés.

## 7. Relecture indépendante ciblée

Un agent distinct du développeur a relu le diff documentaire et ses preuves, en lecture seule. Il a relu les journaux de CI, le journal de session et le code, puis lancé les contrôles dans une copie neuve. Il n'a pas relu le présent rapport, encore en rédaction.

Après la correction de RH-01, le même agent a vérifié cette correction ; c'est la section 7 de son rapport. Son rapport est reproduit ci-dessous sans modification, entre deux filets : c'est le fichier `relecture-1h/relecture.md` du dossier temporaire de la session, de SHA-256 `4a5a979f876bc2b0c24e506d785560ca01cc6463376da6a3ecd725bb949521fb`.

---

# Relecture indépendante — LOT-1H, clôture documentaire de MEC-0004

- **Date :** 2026-11-25
- **Objet :** diff documentaire non commité du LOT-1H (registre, README principal, archive du mandat, index des mandats) et preuves associées (CI, journal de session, déclaration macOS).
- **Relecteur :** agent relecteur indépendant (Claude Opus 5.5), distinct du développeur, en lecture seule sur `/home/user/bastion`. Je ne m'accorde pas la validation finale.
- **Référence de conformité :** `docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md`, l'autorisation du 25 novembre 2026 (19:36:28 UTC) et le complément macOS (19:48:04 UTC).

**État relu :** branche `claude/lot-1h-cloture-mec-0004`, HEAD = `origin/main` = `b4e2a4793dd1101ff4b81e6ad404613ec7671838` (`git ls-remote origin main` exécuté pendant la relecture : même SHA). Rien n'est indexé, aucun stash.

| Fichier | SHA-256 de l'arbre de travail relu | SHA-256 à HEAD |
|---|---|---|
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | `20f149611e44bee2cba6fd9f6db01f0679ac9e2336204df22ed7c491c75cd8ef` | `7993e0c96faeb9d87cb23f1de4aba2e2100791af0b369f21f6271e135ba3ba24` |
| `README.md` | `ac25c816074dfdb3e25556c7ad1977c1dd5cbe1c7e408db90ff02822ce2386c0` | `6290a7524ac090740e90ade699677245bbe079bd96c963a6ac67fe06b62a8c2e` |
| `docs/mandates/README.md` | `15d95fce5d483e41f5eb89e783dc9558123ccc841bb1ed1ce86353cbaab85b22` | `8e4ba221240f8dd24f2437fb82ba69e21ab96a89efa9c3e79fd09fb30de64cd5` |
| `docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md` (nouveau) | `06e268068c9dbceedbe77ca3a57f078c37f62acffcd6d114251c158b5716b998` | absent |
| `scratchpad/lot1h/complement-extrait.txt` (source macOS, hors dépôt) | `a4a22cae020e0e78e9d16e869927ef357861028b6bffa8d4c6080d21a26e292d` | — |
| sortie de `git diff` (3 fichiers suivis) | `21da0f06d4ca4cfca504f8f4f2502399e763209835a5861458f001aff0ca2033` | — |

`docs/reviews/LOT-1H-CLOTURE-MEC-0004.md` est apparu dans l'arbre pendant la relecture. Conformément à la consigne, je ne l'ai **pas** relu.

## 1. Méthode

1. Lecture de `CLAUDE.md`, du mandat en entier, de l'autorisation et du complément (extraits du journal).
2. Périmètre : `git status --porcelain -uall [--ignored]`, `git diff --stat`, `git diff --name-only HEAD` sur les chemins interdits.
3. Registre : comparaison mécanique ligne à ligne de HEAD et de l'arbre de travail (script Python `-I`), puis contrôle des préfixes exigés par le mandat.
4. Faits chiffrés : source (`[Fact]`), journaux de CI téléchargés par l'API publique GitHub (runs 45632937850, 45633018137, 45683720344, plus le run 45470444406 de `1fa2769`, base antérieure, pour mesurer les deltas), métadonnées de la PR #26.
5. Archive et index : extraction des messages du journal `/root/.claude/projects/-home-user/7361641c-….jsonl` (Python `-I`, lecture seule), comparaison octet à octet, empreintes.
6. Contrôles dans une copie neuve (`tar` sans `.git`, `bin`, `obj`, `.godot`) ; contrôle de traçabilité dans un clone jetable `git clone --local`.

Fichiers de travail : `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1h/` (`copie/`, `clone-trace/`, `ci/`, `journal/`, `scripts/`).

## 2. Commandes exécutées

| # | Commande (résumé) | Résultat observé | Code | Classement |
|---|---|---|---|---|
| C1 | `git status --porcelain -uall` ; `git diff --stat` | `M README.md`, `M docs/gameplay/GAMEPLAY-DECISIONS.md`, `M docs/mandates/README.md`, `?? docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md` (puis `?? docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`) ; 3 fichiers, +9 −7 | 0 | exécuté et réussi |
| C2 | `git diff --name-only HEAD -- src tests .github scripts .claude CLAUDE.md docs/decisions docs/references \| wc -l` | `0` | 0 | exécuté et réussi |
| C3 | `git status --porcelain -uall --ignored` (hors `bin/`, `obj/`) | seuls les fichiers ci-dessus, plus `src/Bastion.Client.Godot/.godot/…` ignorés (cache d'éditeur, hors diff) | 0 | exécuté et réussi |
| C4 | diff mécanique registre HEAD / arbre (`check_lines.py`) | 847 lignes des deux côtés ; lignes modifiées : **[649, 650]** uniquement ; préfixe historique conservé : `True` ; texte exact du §2.B en tête de valeur : `True` | 0 | exécuté et réussi |
| C5 | `cmp` registre HEAD / `scratchpad/lot1h/registre-avant.md` | identiques | 0 | exécuté et réussi |
| C6 | `grep -c "\[Fact\]"` / `"\[Theory\]"` sur `TurnTests.cs` | 19 / 0 | 0 | exécuté et réussi |
| C7 | API GitHub : runs et jobs 45632937850, 45633018137, 45683720344 | push `38d3d41` success (job 139270709355) ; pull_request `38d3d41` success (job 139270971166) ; push `main` `b4e2a47` success (job 139450654733) | HTTP 200 | exécuté et réussi |
| C8 | journaux des trois jobs | chacun : `Passed: 65 … Total: 65`, `== 75 tests, 0 échec(s) ==`, 120 lignes `SMOKE OK`, 0 `SMOKE ÉCHEC`, `SMOKE : RÉUSSITE` | HTTP 200 | exécuté et réussi |
| C9 | `cmp` journal du job 139450654733 / `scratchpad/lot1h/ci-main-139450654733.log` | identiques | 0 | exécuté et réussi |
| C10 | run 45470444406 (`1fa2769`, avant la PR #26), job 138716658271 | 46 tests, 75 hooks, 66 `SMOKE OK` | HTTP 200 | exécuté et réussi |
| C11 | comparaison des lignes `SMOKE OK` avant/après | les 66 premières de `b4e2a47` = les 66 de `1fa2769`, dans l'ordre ; **54** nouvelles | 0 | exécuté et réussi |
| C12 | API `pulls/26` | `merged: true`, `merged_at 2026-11-25T19:17:28Z`, `merge_commit_sha b4e2a47…`, `head 38d3d41…` | HTTP 200 | exécuté et réussi |
| C13 | `git diff --stat 38d3d41 b4e2a47` | vide (arbre fusionné = arbre testé par la CI de la PR) | 0 | exécuté et réussi |
| C14 | extraction du journal (`journal.py`, `find.py`, `range.py`, Python `-I`) | mandat : entrée `user` 2026-11-25T19:47:54.665Z ; autorisation : 19:36:28.859Z ; complément : `queue-operation` 19:48:04.641Z | 0 | exécuté et réussi |
| C15 | comparaison archive / message | `fichier == message + "\n"` : `True` ; `sha256` = `06e26806…b998` = empreinte de l'index | 0 | exécuté et réussi |
| C16 | `cmp` complément du journal / `complement-extrait.txt` | identiques (1 980 octets) | 0 | exécuté et réussi |
| C17 | même contrôle pour les transcriptions 1E, 1F, 1G | chacune = message + `"\n"` (pratique constante) | 0 | exécuté et réussi |
| C18 | empreintes de toutes les entrées de l'index | 21 concordantes, 0 discordante ; 1 fichier non indexé (RH-08) | 0 | exécuté et réussi |
| C19 | `stat` de `.git/FETCH_HEAD` et des fichiers du lot ; `git reflog` | fetch `origin main` à 19:48:08 UTC (→ `b4e2a47`) ; fichiers modifiés entre 19:48:54 et 19:49:49 ; branche créée à 19:36:51 depuis `b4e2a47` | 0 | exécuté et réussi |
| C20 | copie : `dotnet build` | `Build succeeded. 0 Warning(s) 0 Error(s)` | 0 | exécuté et réussi |
| C21 | copie : `dotnet test` | `Passed! - Failed: 0, Passed: 65, Skipped: 0, Total: 65` | 0 | exécuté et réussi |
| C22 | copie : `dotnet format --verify-no-changes` | aucune sortie | 0 | exécuté et réussi |
| C23 | copie : `bash scripts/harness/test-hooks.sh` | `== 75 tests, 0 échec(s) ==` | 0 | exécuté et réussi |
| C24 | `diff -rq` dépôt / copie (hors `.git`, `bin`, `obj`, `.godot`) | aucune différence : les contrôles portent bien sur l'état relu | 0 | exécuté et réussi |
| C25 | clone jetable à `b4e2a47`, registre modifié copié, `check-simulation-trace.sh HEAD^1 <desc>` | `MEC-0004` : « Déclaration MEC-0004 reconnue (fiche présente, décision « acceptée ») », code 0 ; témoins négatifs : `MEC-0001` → « n'est pas « acceptée » », code 1 ; `MEC-0009` → « fiche absente », code 1 | 0 / 1 / 1 | exécuté et réussi (comportement attendu) |

## 3. Conformités constatées

- **Périmètre (C1–C3) :** seuls les fichiers autorisés sont touchés. Rien dans `src/`, `tests/`, `.github/`, `scripts/`, `.claude/`, `CLAUDE.md`, `docs/decisions/`, `docs/references/`. *Exécuté et réussi.*
- **Registre (C4, C5) :** seules `GAMEPLAY-DECISIONS.md:649` (« Tests de modification ») et `:650` (« État d'implémentation ») changent, toutes deux dans la fiche MEC-0004 (`:628` à `:847`). En-tête, règles, gabarit, MEC-0001 à MEC-0003 et sections 2 à 7 de MEC-0004 sont identiques à HEAD. *Exécuté et réussi.*
- **Texte historique (C4) :** `:649` commence par « T01 à T16, définis à la section 6, non encore implémentés. », intégralement. L'annotation est datée (« ajoutée le 25 novembre 2026 ») et dit que le texte historique « décrit l'état à la date de l'inscription » : les tests ne sont pas présentés comme faits à cette date. Même forme que le précédent de MEC-0003 (`:459`). *Exécuté et réussi.*
- **Texte du §2.B (C4) :** `:650` commence par le texte exact de `BASTION-MANDAT-LOT-1H-v1.0.md:36`, sans les accents graves de la mise en forme. La suite précise les essais macOS, comme le demande le §2.B. « intégré » figure dans la liste des états (`GAMEPLAY-DECISIONS.md:23` et `:42`). *Exécuté et réussi.*
- **Distinction automatisé / déclaré (`:650`) :** « Vérifications automatisées : la CI de la PR #26 » ; « Essais manuels sous macOS, distincts de ces vérifications : sept contrôles […] déclarés satisfaisants par le propriétaire […] C'est une déclaration du propriétaire, non reproduite de façon indépendante. » Ces mentions correspondent au complément : sept items, 7/7 satisfaisants, scénario 4, anciens scénarios et fenêtre. *Inspecté.*
- **Faits chiffrés (C6–C13) :** 19 tests xUnit dans `tests/Bastion.Simulation.Tests/Turns/` (19 `[Fact]` ; 46 → 65) ; 54 nouveaux contrôles fumée (66 → 120) ; 65 tests .NET et 120 contrôles fumée réussis dans la CI de la PR #26 (push et pull_request), et aussi sur `main` après la fusion ; 75 tests du harnais. La répartition T01–T09, T14, T15 côté moteur est exacte (`TurnTests.cs:8-10`). La seule inexactitude porte sur T13 : voir RH-01. Les chemins cités existent. *Exécuté et réussi.*
- **Périmètre de MEC-0004 :** aucune phrase ajoutée n'étend le périmètre autorisé (`:646`) ni les exclusions (`:647`). *Inspecté.*
- **README (§3 du mandat) :** `README.md:8` cite MEC-0003 (PR #19) et MEC-0004 (PR #26), implémentés, testés et intégrés. `:9` cite `Bastion.Simulation.Turns` (namespace vérifié, `TurnRules.cs:3`). La description correspond au code : `EndTurn` additionne avec plafond, ressource par ressource (`TurnRules.cs:61-74`), et le tour passe à `Turn + 1`. `:10` conserve « `MEC-0001` et `MEC-0002` restent reportées ». `:11` annonce quatre scénarios et dit « Ce n'est ni un jeu complet ni l'interface finale ». « hors de `Bastion.slnx` » est exact (vérifié sur `Bastion.slnx`). `:27-28` (`Turns/`) est exact. *Inspecté.*
- **Archive et index (C14–C18) :** l'archive est le message du 19:47:54 UTC, plus un saut de ligne final, comme pour 1E, 1F et 1G. L'empreinte de l'index est exacte. Les horodatages 19:36:28, 19:47:54 et 19:48:04 UTC sont exacts. Le nom sans « -transcription » est bien celui que désignent l'autorisation et le complément. Le statut « PRÉPARÉ — exécution soumise à autorisation » est bien cité tel quel (`BASTION-MANDAT-LOT-1H-v1.0.md:3`). La forme suit les lignes 1E à 1G. *Exécuté et réussi.*
- **`git fetch origin main` avant modification (C19) :** fait à 19:48:08 UTC. Les fichiers ont été modifiés après. *Exécuté et réussi (preuve indirecte : horodatages).*

## 4. Constats

### RH-01 — À corriger (mineur) — T13 attribué à tort aux « 54 nouveaux contrôles »

- **Où :** `docs/gameplay/GAMEPLAY-DECISIONS.md:649` : « T05, T10 à T13 et T16 par 54 nouveaux contrôles du contrôle fumée Godot ».
- **Preuve :**
  - Le rapport du lot 1G attribue T13 aux contrôles **antérieurs** : « 46 tests existants ; 66 contrôles fumée antérieurs, identiques ; carte, légende et panneau identiques au pixel près » (`docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md:129`, et `:539` : « T13 (66 lignes identiques) »).
  - Parmi les 54 nouvelles lignes `SMOKE OK` (C11), aucune n'est étiquetée T13. Les étiquettes présentes sont T01, T02, T05, T10, T11, T12 et T16.
  - Le résumé du lot 1G (`:34`) attribue T05 et T10 à T16 au contrôle fumée dans son ensemble (120 contrôles), pas aux 54 nouveaux.
- **Portée :** imprécision de traçabilité dans un registre protégé. Elle ne change aucune décision.
- **Correction suggérée** (reste dans la ligne autorisée et dans les points du §2.A) : remplacer le passage par « T05, T10 à T12 et T16 par 54 nouveaux contrôles du contrôle fumée Godot, dans `src/Bastion.Client.Godot/SmokeTest.cs` ; T13 (absence de régression) par les 46 tests et les 66 contrôles fumée antérieurs, inchangés ». Plus court : « T05, T10 à T13 et T16 par le contrôle fumée Godot, dans `src/Bastion.Client.Godot/SmokeTest.cs`, qui compte 54 nouveaux contrôles ». Après la correction, recalculer l'empreinte du registre dans le rapport.

### RH-02 — Observation, point à décider — la notice du client contredit désormais le registre sur macOS

- **Où :** `src/Bastion.Client.Godot/README.md:96` (« six essais manuels »), `:107` (« Ces trois scénarios et les touches 1 à 4 et T n'ont pas été essayés sous macOS ») et `:175` (« L'essai manuel du scénario 4 sous macOS n'a pas eu lieu », sous le titre « au moment de leur réalisation », `:174`).
- **Preuve :** le complément déclare des essais du scénario 4, des « anciens scénarios » et de la touche T dans les scénarios 1 à 3. `GAMEPLAY-DECISIONS.md:650` les inscrit.
- **Portée :** le fichier est hors des cinq fichiers autorisés (§6 du mandat), et sa non-modification est donc correcte. Mais la contradiction subsiste : `:107` est désormais inexact. `:175` reste défendable, grâce à son titre.
- **Suggestion :** le signaler dans le rapport du lot 1H (limites, points à décider). Une mise à jour de la notice demanderait un mandat distinct.

### RH-03 — Observation, condition sur le rapport — provenance de la déclaration macOS et des preuves de CI

- **Où :** `GAMEPLAY-DECISIONS.md:650` renvoie à « Détail : `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md` ».
- **Constat :** la seule source de la déclaration macOS est le message du complément (19:48:04 UTC), et il n'est archivé nulle part dans le dépôt. L'archiver sous `docs/mandates/` ajouterait un sixième fichier, non autorisé. De même, le rapport du lot 1G, cité comme « Détail » de la ligne `:649`, dit que la CI n'avait pas tourné (`LOT-1G-IMPLEMENTATION-MEC-0004.md:836`). La preuve de CI n'est donc pas dans le dépôt.
- **Suggestion :** le rapport du lot 1H devrait reproduire le complément mot pour mot, avec son empreinte (`a4a22cae…e292d`) et son horodatage. Il devrait aussi citer les runs 45632937850, 45633018137 et 45683720344, avec leurs job_id et leurs chiffres. Le rapport doit exister au moment de la publication, sinon le renvoi de `:650` est vide. *Non vérifié* : je n'ai pas relu le rapport.

### RH-04 — Observation — les sections 6 et 7 de MEC-0004 sont restées au temps de l'inscription

- **Où :** `GAMEPLAY-DECISIONS.md:814` (« ne sont pas encore implémentés »), `:837` (« futur mandat d'implémentation ») et `:847` (« ne demande pas encore d'écrire ce code »).
- **Constat :** le §2.C du mandat impose de conserver ces passages. L'annotation de `:649` les éclaire, mais elle est rattachée au seul tableau, si bien qu'une lecture isolée de la section 6 peut induire en erreur.
- **Suggestion :** aucune action dans ce lot. Le propriétaire pourra le traiter dans un futur mandat, s'il le souhaite.

### RH-05 — Observation (forme) — accents graves absents à `:650`

- **Constat :** MEC-0003 écrit `` `main` `` et le SHA entre accents graves (`:460`). MEC-0004 les écrit en texte simple, comme le texte du §2.B (`BASTION-MANDAT-LOT-1H-v1.0.md:36`). La conformité littérale au mandat est le bon choix.
- **Suggestion :** aucune action.

### RH-06 — Observation — la CI du commit de fusion n'est pas citée

- **Preuve :** le run 45683720344 (job 139450654733, push `main`, `b4e2a47`) a réussi, avec 65 tests, 75 tests du harnais et 120 contrôles fumée (C8). Le précédent MEC-0003 la cite (« et par celle du commit de fusion », `:459`). Le §2.A du mandat ne la demande pas.
- **Suggestion :** facultatif. La citer dans le rapport suffit.

### RH-07 — Observation (mineure) — « trois pour la marche (lot 1F) » dans `README.md:11`

- **Constat :** le scénario 1 est la scène du lot 1D, désignée « Scénario 1 — Référence » par le mandat 1F. Le banc de trois scénarios date bien du lot 1F (`src/Bastion.Client.Godot/README.md:3`), et la formulation est donc acceptable.
- **Suggestion :** aucune action requise. Au besoin, écrire « (lots 1D et 1F) ».

### RH-08 — Observation, hors périmètre — un mandat non indexé, antérieur au lot

- **Constat :** `docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` n'a pas de ligne dans `docs/mandates/README.md`. Il est déjà absent à HEAD (C18), archivé par `1ecc608` et documenté dans `docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md:18`.
- **Suggestion :** aucune action dans ce lot (hors périmètre). À signaler au propriétaire, au besoin.

## 5. Ce que je n'ai pas pu vérifier

- **Les sept essais macOS :** *non vérifié*. C'est une déclaration du propriétaire, sans trace exécutable. Je n'ai vérifié que l'identité du complément avec le journal (C16).
- **Le « oui » du propriétaire cité par le complément :** *non vérifié*. Il n'apparaît pas dans ce journal de session, qui contient seulement le message d'autorisation de 19:36:28 UTC. L'index ne cite d'ailleurs que ce message et le complément, ce qui est exact.
- **Le contrôle fumée Godot :** *non exécuté* par moi (pas de Godot dans ma copie). Ses 120 contrôles sont *inspectés* dans les journaux de CI.
- **`docs/reviews/LOT-1H-CLOTURE-MEC-0004.md` :** *non relu*, conformément à la consigne.
- **L'identité de l'archive avec un éventuel fichier original :** *non vérifié*. Seule l'identité avec le message du journal est établie, et l'index le dit (« identité avec un fichier original non vérifiée »).
- **Le rendu Markdown** des lignes `:649` et `:650` : *inspecté seulement*. La forme est identique au précédent `:459`.

## 6. Verdict

**Conforme sous réserve de RH-01.** Je ne relève aucun constat bloquant. Le périmètre est respecté :
- seules les deux lignes autorisées du registre changent ;
- le texte historique et le texte exact du §2.B sont présents ;
- la distinction entre contrôles automatisés et essais déclarés est nette ;
- le README, l'archive et l'index sont exacts ;
- les quatre contrôles réussissent, ainsi que le contrôle de traçabilité.

Une imprécision de traçabilité est à corriger dans la ligne autorisée : RH-01, l'attribution de T13. RH-02 et RH-03 sont à reporter dans le rapport du lot. Cette relecture n'est pas une validation finale : la décision revient au propriétaire.

## 7. Vérification de la correction de RH-01

- **Date :** 2026-11-25
- **Objet :** correction de RH-01 dans `docs/gameplay/GAMEPLAY-DECISIONS.md:649`. J'ai travaillé en lecture seule, comme pour la relecture principale.
- **Registre relu :** SHA-256 `6e5d13cccb07c9b0bd67e520868f85e33057f4b02c5ce9f42df7323423abf16d`. La version de la relecture principale avait pour empreinte `20f149611e44bee2cba6fd9f6db01f0679ac9e2336204df22ed7c491c75cd8ef` ; elle est conservée dans `relecture-1h/copie/`.
- **Autres fichiers :** `git status` et `git diff --stat` ne changent pas (3 fichiers suivis modifiés, +9 −7 ; 2 fichiers non suivis). Rien n'a changé dans les chemins interdits.

### Commandes exécutées

| # | Commande (résumé) | Résultat observé | Code | Classement |
|---|---|---|---|---|
| V1 | `git status --porcelain -uall` ; `git diff --stat` ; `git diff --name-only HEAD -- src tests .github scripts .claude CLAUDE.md docs/decisions docs/references \| wc -l` | les mêmes 5 fichiers qu'avant ; `0` dans les chemins interdits | 0 | exécuté et réussi |
| V2 | `check_rh01.py` (Python `-I`) : registre à HEAD, registre de la relecture principale et registre actuel | même nombre de lignes. Lignes qui diffèrent de HEAD : **[649, 650]**. Lignes qui diffèrent de la version déjà relue : **[649]**. Ligne 650 inchangée : `True`. Texte historique intact en tête de ligne : `True`. La version déjà relue, avec le seul fragment remplacé, est identique à la ligne actuelle : `True`. « T10 à T13 » absent : `True`. | 0 | exécuté et réussi |
| V3 | même script : présence des éléments du §2.A dans `:649` | « Annotation ajoutée le 25 novembre 2026 », « texte historique conservé, qui décrit l'état à la date de l'inscription », « Les seize scénarios T01 à T16 sont désormais couverts », « 19 tests xUnit », « 54 nouveaux contrôles », « La CI de la PR #26 a exécuté avec succès 65 tests .NET et 120 contrôles fumée », `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md` : tous `True` | 0 | exécuté et réussi |
| V4 | `git diff --stat 1fa2769 b4e2a47 -- tests/ src/Bastion.Simulation/` | seuls changent `Turns/TurnRules.cs`, `Turns/TurnState.cs` et `Turns/TurnTests.cs`, en ajouts purs (+374). Hors `Turns/`, la sortie compte `0` ligne : les sources des 46 tests antérieurs sont inchangées | 0 | exécuté et réussi |
| V5 | `git diff 1fa2769 b4e2a47 -- src/Bastion.Client.Godot/SmokeTest.cs \| grep '^-[^-]'` | 2 lignes retirées, toutes deux des commentaires de documentation (`///`) | 0 | exécuté et réussi |
| V6 | rappel de C10 et C11 (journaux de CI déjà téléchargés) | `1fa2769` : 46 tests .NET et 66 `SMOKE OK`. Les 66 premières lignes `SMOKE OK` de `b4e2a47` sont identiques, dans l'ordre. Aucune des 54 nouvelles lignes n'est étiquetée T13 | — | exécuté et réussi (relecture principale) |
| V7 | lecture de `GAMEPLAY-DECISIONS.md:830` | `\| T13 \| Scénarios 1 à 3 et contrôles existants \| Aucune régression \|` | 0 | inspecté |
| V8 | nouvelle copie `relecture-1h/copie-rh01/` (`tar` sans `.git`, `bin`, `obj`, `.godot`) ; `sha256sum` du registre copié | `6e5d13cc…f16d`, identique au dépôt ; `diff -rq` entre le dépôt et la copie : aucune différence | 0 | exécuté et réussi |
| V9 | copie : `dotnet format --verify-no-changes` | aucune sortie (0 octet) | 0 | exécuté et réussi |
| V10 | copie : `bash scripts/harness/test-hooks.sh` | `== 75 tests, 0 échec(s) ==` | 0 | exécuté et réussi |
| V11 | clone jetable à `b4e2a47`, avec le registre corrigé : `check-simulation-trace.sh HEAD^1 desc-mec4.txt` | « Déclaration MEC-0004 reconnue (fiche présente, décision « acceptée ») » | 0 | exécuté et réussi |

### Constats

1. **Périmètre :** le registre ne diffère toujours de HEAD qu'aux lignes 649 et 650. Depuis ma relecture principale, seule la ligne 649 a changé, et seulement par le fragment visé. La ligne 650 est identique, octet pour octet. *Exécuté et réussi.*
2. **RH-01 corrigé :**
   - T13 n'est plus attribué aux 54 nouveaux contrôles. La nouvelle phrase l'attribue aux 46 tests .NET et aux 66 contrôles fumée antérieurs, conformément à `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md:129`.
   - « 46 » est exact (run 45470444406), et les sources de ces tests sont inchangées (V4).
   - « 66 […] inchangés » est exact : les sorties sont identiques et dans le même ordre (V6), et les seules lignes retirées du source sont deux commentaires (V5).
   - « l'absence de régression » reprend le résultat attendu de T13 dans la fiche (`:830`), sans l'élargir ni le restreindre.
   - « T05, T10 à T12 et T16 » correspond aux étiquettes des 54 nouvelles lignes (T05, T10, T11, T12, T16 ; T01 et T02 y figurent aussi, ce que la phrase ne contredit pas).

   *Exécuté et réussi* pour les chiffres et les sources ; *inspecté* pour la concordance avec la fiche.
3. **Texte historique et §2.A :** le texte historique reste intact en tête de ligne. Les cinq points du §2.A sont toujours présents, dont « 54 nouveaux contrôles » (V3), et l'annotation garde sa date et sa réserve sur l'état à l'inscription. *Exécuté et réussi.*
4. **Contrôles :** `dotnet format --verify-no-changes` et `bash scripts/harness/test-hooks.sh` réussissent tous deux, code 0, dans une copie neuve de l'état corrigé. Le contrôle de traçabilité lit toujours la fiche. *Exécuté et réussi.* Je n'ai pas relancé `dotnet build` ni `dotnet test` : le changement est purement documentaire, et ces commandes n'étaient pas demandées pour cette vérification.
5. **Observation, sans action :** la correction modifie l'empreinte du registre. Le rapport du lot 1H, que je n'ai pas relu, doit citer `6e5d13cc…f16d`, et non `20f14961…d8ef`. *Non vérifié.*

### Verdict

**RH-01 est corrigé.** La nouvelle phrase est exacte, et le périmètre reste limité aux lignes 649 et 650. La ligne 650 n'a pas bougé, le texte historique et les exigences du §2.A restent satisfaits, et les contrôles demandés réussissent. Je ne relève aucun nouveau constat bloquant ni à corriger. Les observations RH-02 à RH-08 restent en l'état. Cette vérification n'est pas une validation finale : la décision revient au propriétaire.

---

**Traitement des constats :**

| Constat | Classement | Traitement |
|---|---|---|
| RH-01 : T13 attribué aux 54 nouveaux contrôles | à corriger | **Corrigé** dans la ligne autorisée : « T05, T10 à T12 et T16 par 54 nouveaux contrôles […] ; T13, l'absence de régression, par les 46 tests .NET et les 66 contrôles fumée antérieurs, inchangés ». La correction est vérifiée par le relecteur (§7 de son rapport). |
| RH-02 : la notice du client contredit le registre sur macOS | observation, point à décider | **Signalé** au §8 et soumis au propriétaire au §9. La notice n'est pas modifiée, car elle ne fait pas partie des fichiers autorisés. |
| RH-03 : pas de provenance dans le dépôt pour la déclaration macOS et la CI | observation | **Traité dans ce rapport** : le compte rendu macOS est reproduit à l'annexe A, avec son empreinte et son horodatage ; les runs et les jobs de CI sont cités au §5.1, avec leurs chiffres. |
| RH-04 : sections 6 et 7 de MEC-0004 au temps de l'inscription | observation | **Non modifié** : leur conservation est imposée par le §2.C du mandat. Signalé au §8. |
| RH-05 : accents graves absents à la ligne 650 | observation de forme | **Conservé** : le texte suit littéralement le §2.B du mandat. |
| RH-06 : CI du commit de fusion non citée dans le registre | observation | **Citée dans ce rapport** (§5.1). Le registre s'en tient à ce que demande le §2.A. |
| RH-07 : « trois pour la marche (lot 1F) » dans le README | observation mineure | **Conservé** : le banc de trois scénarios date du lot 1F, et le relecteur juge la formulation acceptable. |
| RH-08 : un mandat antérieur absent de l'index | observation hors périmètre | **Non modifié**, signalé au §8. |

## 8. Limites et réserves

- **Essais macOS :** déclaratifs. Le compte rendu ne dit pas sur quel commit ni sur quelle version exacte du prototype ils ont porté : « après les essais du LOT-1G ». Le registre écrit donc « prototype du lot 1G », sans commit.
- **Message « oui » :** l'autorisation et le complément mentionnent une réponse « oui » du propriétaire. Elle n'apparaît pas telle quelle dans cette session ; c'est le message d'autorisation de 19:36:28 UTC qui a été retenu.
- **Mise en forme :** dans la ligne « État d'implémentation », `main` et le commit de fusion ne sont pas en police de code, par fidélité au texte littéral du mandat. C'est un écart de forme avec la fiche MEC-0003.
- **Notice du client (RH-02) :** elle ne fait pas partie des cinq fichiers autorisés et n'est donc pas mise à jour (§9). Or `src/Bastion.Client.Godot/README.md` contredit désormais le registre sur macOS :
  - la ligne 96 annonce « six essais manuels » ;
  - la ligne 107 dit que les scénarios 2 à 4 et les touches 1 à 4 et T « n'ont pas été essayés sous macOS ».
- **Sections 6 et 7 de MEC-0004 (RH-04) :** elles restent au temps de l'inscription, par exemple « ne sont pas encore implémentés ». Le §2.C du mandat impose leur conservation, et l'annotation du tableau les éclaire.
- **Mandat non indexé (RH-08) :** `docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` manque à l'index depuis un lot antérieur. C'est hors du périmètre de ce lot, et rien n'est changé.
- **Rapport du lot 1G :** il indique encore que la CI n'a pas tourné, puisqu'il a été rédigé avant la publication. Il n'est pas modifié ici, puisqu'il ne fait pas partie des fichiers autorisés.
- **CI :** rien n'est poussé, donc la CI n'a pas tourné sur ce lot.

## 9. Points à décider par le propriétaire

1. **Publication :** commit, push de la branche `claude/lot-1h-cloture-mec-0004` et PR. Le lot ne touche pas `src/Bastion.Simulation/`. Le script de traçabilité sort alors avec le code 0, sans exiger de déclaration (« Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise. », `scripts/harness/check-simulation-trace.sh:24-26`). C'est inspecté dans le script, non exécuté.
2. **Notice du client Godot :** faut-il mettre à jour ses mentions des essais macOS par un mandat distinct ?

## 10. Diff final

Ce diff couvre les trois fichiers suivis modifiés. Le mandat archivé est un fichier nouveau : son contenu est celui du message du propriétaire, et son empreinte figure à l'annexe B. Ce rapport ne peut pas contenir son propre diff.

```diff
diff --git a/README.md b/README.md
index 09dd6f8..0a7e098 100644
--- a/README.md
+++ b/README.md
@@ -5,9 +5,10 @@ Projet de jeu en C# avec Godot .NET.
 **État :**
 
 - le harnais de développement est installé et opérationnel : hooks Claude Code, tests des hooks, intégration continue ;
-- le premier incrément de gameplay, `MEC-0003` (marche sur terrain plat), est implémenté, testé et intégré à `main` (PR #19) ;
-- la simulation C# comprend désormais la marche sur terrain plat ; `MEC-0001` et `MEC-0002` restent reportées ;
-- un prototype technique Godot, `src/Bastion.Client.Godot/`, existe depuis le lot 1D : une scène reliée à la simulation, qui n'est pas l'interface finale. Il reste hors de `Bastion.slnx`, mais la CI le compile et lance son contrôle fumée depuis le lot 1E.
+- deux incréments de gameplay sont implémentés, testés et intégrés à `main` : `MEC-0003`, la marche sur terrain plat (PR #19), et `MEC-0004`, la gestion élémentaire des tours et la récupération des ressources (PR #26) ;
+- la simulation C# comprend la marche sur terrain plat et, dans `Bastion.Simulation.Turns`, la gestion élémentaire des tours d'une seule unité : une commande explicite termine le tour, récupère les TU et l'énergie, chacune dans la limite de son plafond, et passe au tour suivant ;
+- `MEC-0001` et `MEC-0002` restent reportées ;
+- un prototype technique Godot, `src/Bastion.Client.Godot/`, existe depuis le lot 1D : une scène reliée à la simulation, avec quatre scénarios fixes de démonstration, trois pour la marche (lot 1F) et un pour la gestion des tours (lot 1G). Ce n'est ni un jeu complet ni l'interface finale. Il reste hors de `Bastion.slnx`, mais la CI le compile et lance son contrôle fumée depuis le lot 1E.
 
 ## Organisation
 
@@ -23,8 +24,8 @@ Règles permanentes de travail : [`CLAUDE.md`](CLAUDE.md).
 
 | Chemin | Rôle |
 |---|---|
-| `src/Bastion.Simulation/` | Simulation, indépendante de Godot : marche sur terrain plat de `MEC-0003` (`Movement/`) |
-| `tests/Bastion.Simulation.Tests/` | Tests xUnit : tests fumée techniques et tests de `MEC-0003` (`Movement/`) |
+| `src/Bastion.Simulation/` | Simulation, indépendante de Godot : marche sur terrain plat de `MEC-0003` (`Movement/`) et gestion élémentaire des tours de `MEC-0004` (`Turns/`) |
+| `tests/Bastion.Simulation.Tests/` | Tests xUnit : tests fumée techniques, tests de `MEC-0003` (`Movement/`) et de `MEC-0004` (`Turns/`) |
 | `scripts/harness/` | Hooks Claude Code, leurs tests et leurs limites |
 | `.claude/settings.json` | Branchement des hooks |
 | `.github/workflows/ci.yml` | Intégration continue |
diff --git a/docs/gameplay/GAMEPLAY-DECISIONS.md b/docs/gameplay/GAMEPLAY-DECISIONS.md
index cebddd6..f620b47 100644
--- a/docs/gameplay/GAMEPLAY-DECISIONS.md
+++ b/docs/gameplay/GAMEPLAY-DECISIONS.md
@@ -646,8 +646,8 @@ Adaptations à l'inscription, sans changement de fond : les sections numérotée
 | Périmètre autorisé | Uniquement le fonctionnement décrit dans les sections 2 à 4. |
 | Éléments exclus | Section 5 et tout comportement non décrit dans cette fiche. |
 | Tests de référence | Aucun : aucune fidélité à OXCE revendiquée. |
-| Tests de modification | T01 à T16, définis à la section 6, non encore implémentés. |
-| État d'implémentation | `non commencé` |
+| Tests de modification | T01 à T16, définis à la section 6, non encore implémentés. *(Annotation ajoutée le 25 novembre 2026 : texte historique conservé, qui décrit l'état à la date de l'inscription. Les seize scénarios T01 à T16 sont désormais couverts : T01 à T09, T14 et T15 par les 19 tests xUnit du moteur, dans `tests/Bastion.Simulation.Tests/Turns/` ; T05, T10 à T12 et T16 par 54 nouveaux contrôles du contrôle fumée Godot, dans `src/Bastion.Client.Godot/SmokeTest.cs` ; T13, l'absence de régression, par les 46 tests .NET et les 66 contrôles fumée antérieurs, inchangés. La CI de la PR #26 a exécuté avec succès 65 tests .NET et 120 contrôles fumée. Détail : `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`.)* |
+| État d'implémentation | intégré — dans main par la PR #26, commit de fusion b4e2a4793dd1101ff4b81e6ad404613ec7671838 (25 novembre 2026). État à la date de l'inscription : non commencé. Vérifications automatisées : la CI de la PR #26 (ligne « Tests de modification »). Essais manuels sous macOS, distincts de ces vérifications : sept contrôles du prototype du lot 1G (scénario 4, anciens scénarios et fenêtre), déclarés satisfaisants par le propriétaire le 25 novembre 2026. C'est une déclaration du propriétaire, non reproduite de façon indépendante. Détail : `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`. |
 
 #### 2. Portée des décisions existantes
 
diff --git a/docs/mandates/README.md b/docs/mandates/README.md
index a68d000..42eae1e 100644
--- a/docs/mandates/README.md
+++ b/docs/mandates/README.md
@@ -30,3 +30,4 @@ Les documents de ce dossier sont conservés tels que reçus. Ne pas les modifier
 | `BASTION-MANDAT-LOT-1F-v1.0-transcription.md` — mandat du lot 1F : banc d'essai visuel de MEC-0003 | **transcription depuis la conversation** : message du propriétaire du 23 novembre 2026 à 13:32:13 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 23 novembre 2026** dans la conversation (13:33:54 UTC), par le choix de l'option « Autoriser, avec Xvfb (Recommandé) » proposée par Claude Code : exécution locale, avec des captures sous affichage virtuel ; sans commit, push ni PR. Le fichier indique « PRÉPARÉ — exécution non autorisée », conservé tel quel. Exécution : `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md`. | `72f548a7090dec71523b1cb26679985fc6b241cd9fddf32fc77c534c6a295432` |
 | `BASTION-MANDAT-LOT-1G-A-INSCRIPTION-MEC-0004-transcription.md` — mandat d'inscription de MEC-0004 (gestion élémentaire des tours) au registre, sans implémentation ; titre du texte : « BASTION — Mandat d'inscription MEC-0004 v1.2 », désigné par le propriétaire « BASTION — LOT-1G-A v1.0 » dans son autorisation | **transcription depuis la conversation** : message du propriétaire du 24 novembre 2026 à 16:42:02 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 24 novembre 2026** dans la conversation (17:10:53 UTC) : travail local sur une branche dédiée, quatre fichiers documentaires, sans commit, push, PR ni fusion. Le texte consolidé de MEC-0004 v1.2 a été transmis par le propriétaire à 17:15:02 UTC, en réponse à une question de Claude Code ; il est reproduit à l'annexe A du rapport. Le fichier indique « PRÉPARÉ — exécution non encore autorisée », conservé tel quel. Exécution : `docs/reviews/LOT-1G-A-INSCRIPTION-MEC-0004.md`. | `89447962c4f6677a90286b109f8ca0c42a59b2dcf0d1f1151ef5df19fe73cb11` |
 | `BASTION-MANDAT-LOT-1G-v1.0-transcription.md` — mandat du lot 1G : implémentation de MEC-0004 (gestion élémentaire des tours et récupération des ressources) | **transcription depuis la conversation** : message du propriétaire du 24 novembre 2026 à 19:42:22 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 24 novembre 2026** dans la conversation (19:44:40 UTC), par le choix de l'option « Autoriser, avec Xvfb (Recommandé) » proposée par Claude Code : exécution locale, avec des captures sous affichage virtuel ; sans commit, push ni PR. Le fichier indique « PRÉPARÉ — exécution non autorisée », conservé tel quel. Exécution : `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`. | `c792934ef12607aee0b6f3097cc616c419389401106bcdfe881d196e8eda11b1` |
+| `BASTION-MANDAT-LOT-1H-v1.0.md` — mandat du lot 1H : clôture documentaire de MEC-0004 (registre, README principal, archivage) | **transcription depuis la conversation** : message du propriétaire du 25 novembre 2026 à 19:47:54 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée. Le nom du fichier, sans suffixe « -transcription », est celui que désigne l'autorisation du propriétaire | **Autorisé par le propriétaire le 25 novembre 2026** dans la conversation (message « BASTION — LOT-1H — Autorisation d'exécution », 19:36:28 UTC, reçu avant le texte du mandat ; autorisation confirmée par le message « BASTION — LOT-1H — Complément sur les essais macOS », 19:48:04 UTC) : exécution locale, sans commit, push, PR ni fusion. Le fichier indique « PRÉPARÉ — exécution soumise à autorisation », conservé tel quel. Exécution : `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`. | `06e268068c9dbceedbe77ca3a57f078c37f62acffcd6d114251c158b5716b998` |
```

## Annexe A — Compte rendu des essais macOS (source déclarative)

C'est le message du propriétaire du 2026-11-25T19:48:04Z, extrait mécaniquement du journal de session et reproduit sans modification. Son SHA-256, sans saut de ligne final, est `a4a22cae020e0e78e9d16e869927ef357861028b6bffa8d4c6080d21a26e292d` (1 980 octets). Ce rapport est le seul endroit du dépôt où ce compte rendu est conservé, car l'archiver à part demanderait un sixième fichier, non autorisé (RH-03).

```
BASTION — LOT-1H — Complément sur les essais macOS
Source : compte rendu transmis directement par le propriétaire dans la conversation Bastion le 25 novembre 2026, après les essais du LOT-1G sur macOS.
Le propriétaire a déclaré les résultats suivants :

1. Charger le scénario 4 : Satisfaisant
2. Terminer le premier tour : Satisfaisant
3. Terminer le deuxième tour : Satisfaisant
4. Déplacer puis terminer le tour : Satisfaisant
5. Réinitialiser : Satisfaisant
6. Vérifier les anciens scénarios : Satisfaisant
7. Vérifier la fenêtre : Satisfaisant

Bilan : 7/7 essais déclarés satisfaisants.
Les essais portaient notamment sur :

* L'état initial du scénario 4 : tour 1, 12 TU, 35 d'énergie.
* La première fin de tour : tour 2, 60 TU, 55 d'énergie.
* La deuxième fin de tour : tour 3, 60 TU, 75 d'énergie.
* La conservation de la position, de l'orientation et du chemin après un déplacement et une fin de tour.
* La réinitialisation avec R et 4.
* L'absence d'effet de T dans les scénarios 1 à 3.
* La lisibilité de la fenêtre de 800 × 720 pixels.

Ces résultats constituent une déclaration du propriétaire, pas une vérification indépendante de Claude Code.
Ils sont distincts des six essais du prototype LOT-1D réalisés précédemment.
Autorisation
Le propriétaire a déjà répondu « oui » à la demande d'exécution locale du mandat LOT-1H v1.0.
Cette autorisation reste valable. La transmission du texte intégral du mandat ne constitue pas un nouveau mandat et ne modifie pas son périmètre.
Instruction
Archiver le mandat de la section précédente tel quel dans :
`docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md`
Utiliser ce complément comme source déclarative pour les sept essais macOS.
Exécuter maintenant LOT-1H sur la branche locale déjà préparée.
Aucun commit, push, PR ou fusion n'est autorisé.
À la fin, transmettre le diff, le rapport et les conclusions de la relecture indépendante, puis arrêter le travail.
```

## Annexe B — Empreintes SHA-256

| Fichier | Sur `origin/main` (`b4e2a47`) | Dans l'arbre de travail du lot |
|---|---|---|
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | `7993e0c96faeb9d87cb23f1de4aba2e2100791af0b369f21f6271e135ba3ba24` | `6e5d13cccb07c9b0bd67e520868f85e33057f4b02c5ce9f42df7323423abf16d` |
| `README.md` | `6290a7524ac090740e90ade699677245bbe079bd96c963a6ac67fe06b62a8c2e` | `ac25c816074dfdb3e25556c7ad1977c1dd5cbe1c7e408db90ff02822ce2386c0` |
| `docs/mandates/README.md` | `8e4ba221240f8dd24f2437fb82ba69e21ab96a89efa9c3e79fd09fb30de64cd5` | `15d95fce5d483e41f5eb89e783dc9558123ccc841bb1ed1ce86353cbaab85b22` |
| `docs/mandates/BASTION-MANDAT-LOT-1H-v1.0.md` | absent | `06e268068c9dbceedbe77ca3a57f078c37f62acffcd6d114251c158b5716b998` |

Ce rapport ne peut pas porter sa propre empreinte.
