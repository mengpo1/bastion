# Relecture ciblée — MEC-0003, lot 1 : changements de l'avenant n° 2

| Champ | Valeur |
|---|---|
| Date | 22 novembre 2026 |
| Relecteur | agent relecteur indépendant ; même relecteur que la revue générale (`RAPPORT-RELECTURE-MEC-0003-LOT1.md`, SHA-256 `3d5941ec…4252`) ; aucune ligne du lot écrite par lui |
| Objet | les seuls changements faits au titre de l'avenant n° 2, pas une nouvelle revue générale |
| Dépôt relu | `/home/user/bastion`, branche locale `claude/implementation-mec-0003-lot1`, `HEAD` = `25e7a28d18d29fea3753f3313a10f27126c3f274` ; rien n'est commité |
| Référence | avenant n° 2, archivé dans `docs/mandates/BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-2-transcription.md`, comparé au message du journal de session du 2026-11-22T04:51:30.049Z |
| Portée de l'avis | Ce rapport ne valide ni le commit ni la publication. |

Conventions : **vérifié** = commande exécutée par le relecteur, sortie et code de sortie observés ; **inspecté seulement** = lecture sans exécution probante ; **non vérifié** = ni l'un ni l'autre.

Je n'ai rien écrit dans `/home/user/bastion` ; Git n'y a servi qu'en lecture. J'ai tout exécuté dans ma copie, `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-mec0003-lot1/avenant2/copie/`, puis dans des copies jetables pour les mutants. En fin de relecture, les 45 empreintes du dépôt (`src/`, `tests/`, `docs/mandates/`, rapports `docs/reviews/MEC-0003*`) sont inchangées : `sha256sum -c avenant2/empreintes-depot.txt`, 45 × OK. Aucun mutant ne subsiste dans le code.

## 1. Vérifications exécutées

| N° | Vérification | Commande | Code | Résultat |
|---|---|---|---|---|
| V1 | Moteur inchangé | `sha256sum -c …/impl/avenant2/moteur-avant.sha256` ; et contre `…/impl/empreintes-lot.txt` (lignes `src/`) | 0 ; 0 | 18 × OK dans les deux cas : moteur identique à celui de la revue générale |
| V2 | Registre, autres tests, mandat initial inchangés | `grep -E "GAMEPLAY\|ConfigurationTests\|CostTests\|TestWorld\|transcription" empreintes-lot.txt \| sha256sum -c -` | 0 | 5 × OK (registre `7b4931f3…`, état d'après l'avenant n° 1) |
| V3 | Harnais et projets inchangés | `git diff --quiet HEAD -- .claude scripts .github CLAUDE.md docs/decisions docs/references SmokeTests.cs *.csproj` ; fichiers non suivis sous `.claude scripts .github` | 0 ; 0 fichier | aucun changement |
| V4 | Inventaire du diff | `git status --porcelain`, `git diff --name-only HEAD`, `git ls-files --others` | 0 | voir RC-01 |
| V5 | Diff des tests | `diff -u …/GeometryTests.cs.avant …` et `diff -u …/SearchAndExecutionTests.cs.avant …` | 1 (différences attendues) | voir RC-02 à RC-05 ; les états `.avant` ont les empreintes de la revue générale (`ffa0fd70…`, `779db7dd…`) |
| V6 | Archives contre journal | script `python3 -I` : extraction du message (lignes 4138, 4381 et 4666 du journal), puis comparaison octet pour octet | 0 | les trois archives valent exactement le message suivi d'un `\n` (RC-06) |
| V7 | Restauration | `dotnet restore` | 0 | — |
| V8 | Compilation | `dotnet build --configuration Release` | 0 | 0 avertissement, 0 erreur |
| V9 | Tests | `dotnet test --configuration Release` | 0 | 46 tests, 46 réussis, dont RL01, RL02 (2 cas), RL03 et les deux T13 |
| V10 | Format | `dotnet format --verify-no-changes` | 0 | aucune sortie |
| V11 | Harnais | `bash scripts/harness/test-hooks.sh` | 0 | « 75 tests, 0 échec(s) » |
| V12 | Mutants du relecteur | `python3 -I avenant2/mutants-relecteur.py avenant2/copie avenant2/mut` | 0 | voir §2 |
| V13 | Recalcul indépendant des scénarios | modèle `indep/modele_independant.py` de la revue générale | 0 | voir RC-02 à RC-04 |
| V14 | Mutant A1b contre moteur réel | `python3 -I avenant2/comparer-cs.py …`, graines 21, 22 et 23, 150 cartes chacune | 0 × 3 | 0 pas différent sur 103 376 (RC-02) |

## 2. Mutants du relecteur

J'ai écrit mes propres mutants (`avenant2/mutants-relecteur.py`). Chacun s'applique dans une copie jetable de ma copie, supprimée ensuite. J'ai lu le script du développeur (`…/impl/avenant2/mutants.py`) : il est cohérent et nettoie ses copies, et son journal concorde avec mes résultats. Je ne m'y suis pas fié pour conclure.

| Mutant | Défaut introduit | Tests en échec (46 au total) |
|---|---|---|
| T0 | aucun (témoin) | aucun : 46/46 réussis |
| A1 | translation contrôlée aux seules emprises de départ et d'arrivée | **RL01**, RL02 (2 cas) |
| A1b | translation contrôlée au départ, au milieu et à l'arrivée | aucun (voir RC-02) |
| A2a | trajet en L : point intermédiaire et destination seulement | **RL02** (2 cas) |
| A2b | 1er segment balayé, 2e réduit à la destination | **RL02**, cas du mur à l'est de (1,0) |
| A2c | 1er segment réduit au point intermédiaire, 2e balayé | **RL02**, cas du mur au nord de (0,2) |
| A2d | L remplacé par la diagonale droite | RL02 (2 cas), T13 (nouvelle version), RL03, T10, T18, T23, T25, T26 |
| A2e | segments contrôlés avec l'orientation de départ, au lieu du pas engagé (A2) | **RL02** (2 cas) |
| A3a | ordre poursuivi après un refus | **RL03** |
| A3b | nouveau calcul de chemin vers la destination après un refus | **RL03** |
| A3c | retour à l'état initial après un refus (effets des pas exécutés perdus) | **RL03**, T17 |

## 3. Constats

### RC-01 — Le diff se limite à ce que l'avenant autorise
- **Gravité :** observation (conforme).
- **État :** vérifié (V1 à V5).
- **Changements depuis la revue générale :**
  - `GeometryTests.cs` : deux champs `UnitBody`, T13 renommé et complété, `RL01_…`, `RL02_…` ;
  - `SearchAndExecutionTests.cs` : `RL03_…` ;
  - deux archives nouvelles ;
  - `docs/mandates/README.md` : deux lignes ajoutées, aucune supprimée.
- **Inchangés :** moteur (18 fichiers), registre, autres tests, harnais, projets.
- **Fichiers antérieurs à l'avenant :** les deux rapports `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md` et `…-RELECTURE-2026-11-21.md` sont datés du 21 novembre, entre 23:03 et 23:06 UTC, donc d'avant l'avenant. Ils sont inchangés depuis :
  - le rapport d'exécution vaut `2d815c14…` = `rapport.avant.md` ;
  - la relecture est la copie exacte de mon rapport général (`3d5941ec…`).
- **Preuve :** sorties de V1 à V5, en particulier 18 × OK, 5 × OK et `git diff --quiet` = 0.

### RC-02 — RL01 détecte le défaut visé et réussit sur le moteur réel
- **Gravité :** observation.
- **État :** vérifié.
- **Preuves :**
  - **Défaut visé :** A1 (positions initiale et finale seulement) fait échouer `RL01_VolumeIsCheckedDuringTheWholeTranslation` ; le moteur réel le réussit (T0, V9).
  - **Exactitude du commentaire :** avec le modèle indépendant, emprises de départ et d'arrivée admissibles ; balayage en chevauchement de 100,00 mm (`translation_min_sep` = −100,0). Les valeurs sont exactes : 850 − 750 = 100 mm au nord ; 2 200 − 1 800 = 400 mm au départ ; 2 700 − 2 300 = 400 mm à l'arrivée. Le test prouve aussi l'admissibilité de l'arrivée par `CreateState`.
- **Limite constatée :**
  - A1b (contrôle au départ, au milieu et à l'arrivée) n'est pas détecté. Ce n'est pas exigé par l'avenant, qui vise un contrôle aux seules extrémités.
  - Sur 450 cartes aléatoires (103 376 pas), A1b donne exactement les résultats du moteur réel (V14).
  - L'explication probable est géométrique : les obstacles sont alignés sur les arêtes, et une translation orthogonale franchit toujours l'arête à mi-course. La pose médiane capte alors tout chevauchement de balayage. C'est constaté empiriquement, sans démonstration.
  - Aucune action requise.

### RC-03 — RL02 détecte le défaut visé, et contrôle chaque segment séparément
- **Gravité :** observation.
- **État :** vérifié.
- **Preuves :**
  - **Défaut visé par l'avenant :** A2a (point intermédiaire et destination seulement) fait échouer les deux cas de `RL02_VolumeIsCheckedOnBothLegsOfTheDiagonalPath`.
  - **Chaque segment séparément :**
    - A2b (2e segment non balayé) n'est détecté que par le cas du mur à l'est de (1,0) ;
    - A2c (1er segment non balayé) n'est détecté que par le cas du mur au nord de (0,2) ;
    - chaque cas vise donc bien un seul segment.
  - **Autres défauts :** A2d (diagonale droite) et A2e (orientation de départ, contre A2) sont détectés aussi. Le moteur réel réussit les deux cas.
  - **Recalcul indépendant :**
    - demi-diagonale 600√2 = 848,53 mm ;
    - pénétration 848,53 − 750 = 98,53 mm ;
    - mur au nord de (0,2) : marges des segments du passage N = (−98,53 ; +425,30) ;
    - mur à l'est de (1,0) : marges = (+425,30 ; −98,53) ;
    - repos orientés NE au départ, en (1,1) et en (2,1) admissibles ; rotation N → NE libre ;
    - pas NE admis par le passage E dans les deux cas, et par le passage N sans mur, comme l'affirme le test ;
    - aucun mur n'est sur une arête traversée.
  - **Commentaire :** il est exact, et la carte de 4 × 4 est minimale (avec 3 lignes ou 3 colonnes, l'emprise de 848,53 mm chevaucherait un bord).

### RC-04 — RL03 détecte le défaut visé, ainsi que le nouveau calcul et la perte des effets
- **Gravité :** observation.
- **État :** vérifié.
- **Preuves :**
  - **Défauts détectés :** `RL03_OrderStopsAtTheFirstRefusedStep` échoue sous A3a (ordre poursuivi), A3b (nouveau calcul de chemin) et A3c (effets du 1er pas perdus). Le moteur réel le réussit.
  - **Recalcul indépendant des valeurs :**
    - chemin vers (1,0) : [N, N, NE], pour 14 TU et 7 d'énergie ;
    - sur la carte modifiée, 2e pas refusé (case d'arrivée infranchissable) ;
    - NE depuis (0,2) admis par le passage E ;
    - (1,0) atteignable depuis (0,2) par [NE, N], pour 10 TU et 5 d'énergie.
  - **Commentaire :** exact, y compris « le 3e pas, NE depuis (0,2), resterait exécutable ». Il s'agit du pas NE appliqué depuis la position atteinte, comme le ferait un moteur fautif. Le débit (56, 98) et `Assert.Same(Steps[0].State, FinalState)` établissent la conservation des effets.

### RC-05 — T13 est conforme à l'avenant
- **Gravité :** observation.
- **État :** vérifié (V5, V9 ; A2d fait aussi échouer la nouvelle version).
- **Points relevés :**
  - nom `T13_TargetCellRemainsInTheReachableZoneAndIsReachedFacingNorthWest` (l. 86), conforme au résultat attendu ;
  - commentaire précisant que la zone est calculée depuis l'état initial en (2,4), et non depuis (2,3) ;
  - assertions sur `Completed`, les passages N puis W, l'arrivée en (2,2) orientée NW et le solde (48, 94), commenté « 60 − 12 TU, 100 − 6 d'énergie » ;
  - assertions antérieures conservées : présence de (2,2), chemin [NE, NW], (12, 6) ;
  - le premier test T13 (refus du 2e pas N, `Assert.Same`, position, orientation, 56 TU et 98 d'énergie, soit le coût du 1er pas) est inchangé : `diff` sans différence sur l. 66-83.
- **Effet sur la revue générale :** les constats RL-08 et RL-09 sont levés.

### RC-06 — Les archives reproduisent fidèlement les messages du journal
- **Gravité :** observation.
- **État :** vérifié (V6).
- **Preuves :**
  - **Avenant n° 1** : message du 2026-11-21T22:18:31.802Z (uuid `9f833755…`), 1 957 caractères ; archive = message + `\n`, SHA-256 `6055e752655178b214df8804a1b8e373578388be7827258607272da2d79e74d3`.
  - **Avenant n° 2** : message du 2026-11-22T04:51:30.049Z (uuid `00757c65…`), 4 300 caractères ; archive = message + `\n`, SHA-256 `6027eb3215eff97212c8fcfef54cfccc95a1357fe9537c40cd209d59a8e8264f`.
  - **Convention :** c'est la même que pour la transcription du mandat initial, qui vaut aussi exactement le message + `\n` (`c8d9a38f…`). Chaque message ne compte qu'un bloc de texte.

### RC-07 — Lignes du README exactes, dans l'autorisation
- **Gravité :** observation.
- **État :** vérifié.
- **Preuves :**
  - `git diff` : deux lignes ajoutées, aucune supprimée ; elles portent sur le mandat initial et sur l'avenant n° 1, et lui seul, comme l'autorise le §4 de l'avenant n° 2.
  - **Empreintes citées :** égales à celles des fichiers.
  - **Horodatages :** 21:06:41 et 22:18:31 UTC, conformes au journal.
  - **Statut du mandat initial** : l'autorisation de 21:09:26 UTC existe ; c'est la réponse « Autoriser, avec installation .NET (Recommandé) » à une question posée par Claude Code. L'en-tête cité, « mandat préparé, en attente d'autorisation… », figure bien dans le fichier. Le renvoi au rapport d'exécution est exact.
  - **Avenant n° 1** : « le message est lui-même l'autorisation » ; c'est exact, le texte commence par « Je valide… J'autorise exclusivement… ».
  - L'avenant n° 2 n'est pas inscrit au README, ce qui est conforme : l'autorisation ne couvre que le mandat initial et l'avenant n° 1.
- **Remarque mineure :** « dans la conversation » pourrait préciser que l'autorisation de 21:09:26 est un choix parmi des options proposées. Aucune action requise.

### RC-08 — Avenant n° 2 archivé, mais son origine et son statut ne sont encore indiqués nulle part
- **Gravité :** à corriger (étape de l'avenant non encore exécutée).
- **État :** vérifié. Le rapport d'exécution vaut `2d815c14…`, inchangé depuis avant l'avenant ; le README n'en parle pas, ce qui est correct (RC-07).
- **Constat :** le §4 de l'avenant demande d'ajouter l'avenant n° 2 aux pièces du lot « en indiquant son origine et son statut ». Le fichier est archivé tel que reçu, sans en-tête, ce qui est correct. Mais aucune pièce du dépôt n'indique encore son origine (message du propriétaire du 2026-11-22T04:51:30.049Z, transcription extraite du journal) ni son statut. Deux autres points de l'avenant restent à faire au même endroit :
  - le §3 (RL-13 à documenter comme comportement observé dans les tests à carte modifiée ; RL-11 à conserver) ;
  - le §5.5 (actualisation du rapport d'exécution).

  Ils n'ont pas pu être relus. **Non vérifié.**
- **Correction suggérée :** dans le rapport d'exécution actualisé, citer l'archive, son SHA-256 (`6027eb32…`), son origine et son statut, ainsi que les points des §3 et §5. Faire ensuite contrôler ces seuls ajouts.

### RC-09 — Scénarios explicites, deux cartes un peu plus grandes que nécessaire
- **Gravité :** observation.
- **État :** vérifié par le modèle indépendant.
- **Constat :** RL01 marche aussi sur une carte de 2 × 3 (départ en (0,1), mur à l'est de (0,0)), et RL03 sur une carte de 2 × 4. RL02 est minimal. Les tests sont bien marqués « hors registre » et citent les règles (A2, ARB-A, G1, Q3.4, Q4.21, A9, A4 g). Dans RL02, le contrôle sur carte libre est refait dans chaque cas de la théorie : redondant, sans effet.
- **Correction suggérée :** aucune.

## 4. Verdict sur les changements de l'avenant n° 2

**Conforme sous réserves** : une seule réserve, RC-08. Les changements faits sont conformes et dans le périmètre autorisé. L'indication de l'origine et du statut de l'avenant n° 2 n'est pas encore faite, et les §3 et §5.5 restent à exécuter.

Réserves de la revue générale :
- **RL-01 : levée.** `RL01_…` échoue sous A1 (extrémités seulement) et réussit sur le moteur réel ; valeurs recalculées indépendamment (RC-02).
- **RL-02 : levée.**
  - `RL02_…` échoue sous A2a (point intermédiaire et destination seulement) ;
  - chaque segment est contrôlé séparément : A2b et A2c ne sont détectés que par leur cas respectif ;
  - l'orientation pendant le L (A2e) est détectée ;
  - T13 affirme maintenant les passages N puis W (RC-03, RC-05).
- **RL-03 : levée.** `RL03_…` échoue sous A3a (ordre poursuivi), A3b (nouveau calcul) et A3c (effets perdus), et réussit sur le moteur réel (RC-04).
- **RL-08 et RL-09 : levées** par la nouvelle version de T13 (RC-05).
- **RL-15** : levée pour l'avenant n° 1 (archivé et référencé) ; reste RC-08 pour l'avenant n° 2.
- **Non traitées par l'avenant, donc maintenues :**
  - RL-04 à RL-07, RL-10, RL-12, RL-14 et RL-16 à RL-19 ;
  - RL-11 et RL-13, conservées sur décision du propriétaire, qui demande seulement de documenter RL-13.

Ce verdict ne vaut ni validation du commit ni autorisation de publication.

## 5. Fichiers du relecteur

Dans `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/revue-mec0003-lot1/avenant2/` :
- `mutants-relecteur.py` et `mut/mutants-relecteur.log` ;
- `comparer-cs.py`, `ref/` et `a1b/` (programmes d'interrogation du moteur réel et du mutant A1b) ;
- `journal-*.txt` (messages extraits du journal) ;
- `empreintes-depot.txt` ;
- journaux `restore.log`, `build.log`, `test.log`, `format.log`, `hooks.log`.

## 6. Contrôle complémentaire : ajouts liés à RC-08

**Objet :** les seuls ajouts qui répondent à RC-08 (22 novembre 2026).
- **Rapport d'exécution actualisé :** `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md`, SHA-256 `44da10dbd0131bd9243a7f209b497d032d586af7b8570256f0a31668d66e8183`, identique à la copie figée `…/impl/avenant2/rapport.soumis-RC08.md`.
- **README modifié :** SHA-256 `c5f34bc87db8188018b2eda92fb2ddd745caee92d6c0aac958c80ef47fef70aa`.

Comparaison faite avec `rapport.avant.md` (`2d815c14…`), avec l'avenant n° 2 archivé, avec le journal de session et avec mes résultats des sections 1 à 5. Les sections 1 à 5 ci-dessus ne sont pas retouchées : leur version d'avant ce contrôle, `RAPPORT-RELECTURE-CIBLEE-AVENANT-2.sections1-5.md`, a pour SHA-256 `967cde3e…949e`. Je n'ai rien écrit dans `/home/user/bastion`.

### 6.1 Vérifications exécutées

| N° | Vérification | Commande | Code | Résultat |
|---|---|---|---|---|
| W1 | Empreintes des deux fichiers soumis | `sha256sum` du rapport, de sa copie figée et du README | 0 | `44da10db…` (deux fois) et `c5f34bc8…`, comme annoncé |
| W2 | Rien d'autre n'a changé depuis la relecture ciblée | `sha256sum -c avenant2/empreintes-depot.txt` (45 fichiers) ; `find . -newer RAPPORT-RELECTURE-CIBLEE-AVENANT-2.md` (hors `.git`, `bin`, `obj`) ; `git status --porcelain` ; `sha256sum` du registre ; `git diff --quiet HEAD -- .claude scripts .github CLAUDE.md docs/decisions docs/references *.csproj SmokeTests.cs` | 0 | 43 × OK ; seuls `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md` et `docs/mandates/README.md` diffèrent ou sont plus récents ; mêmes 9 entrées Git qu'avant (28 fichiers non suivis) ; registre `7b4931f3…` ; harnais inchangé |
| W3 | Diff du README par rapport à `HEAD` | `git diff docs/mandates/README.md` | 0 | toujours 2 lignes ajoutées, aucune supprimée ; seule la ligne du mandat initial a changé depuis la relecture ciblée |
| W4 | Réponse du propriétaire de 21:09:26 UTC | extraction `python3 -I` du journal, ligne 4172 | 0 | libellé choisi : « Autoriser, avec installation .NET (Recommandé) », identique à celui que cite le README |
| W5 | Zones modifiées du rapport | `diff` et `difflib`, de `rapport.avant.md` vers la version soumise | 0 | 261 lignes sur 471 reprises telles quelles ; ajouts aux §1 à §10 et en annexes A et B, lus en entier |
| W6 | Citations de l'annexe B | extraction `python3 -I` du journal, lignes 4338 et 4381 ; comparaison avec B.2 et B.3 | 0 | B.3 = avenant n° 1 archivé (sans le `\n` final) ; B.2 est contenu mot pour mot dans la réponse du propriétaire de 21:41:14.860Z |
| W7 | Chiffres du diff cités au §5.2 | `diff` et `git diff --no-index --numstat` contre les copies `.avant` | 0 | `GeometryTests.cs` : 67 lignes ajoutées, dont 59 non vides, et 2 retirées ; `SearchAndExecutionTests.cs` : 32 ajoutées, dont 28 non vides, et 0 retirée |
| W8 | Comportement RL-13 décrit au §3 | test temporaire `RevueRc08Tests`, dans ma copie seulement, supprimé ensuite : chemin [NE] calculé sur carte libre, avec passage N ; exécution sur la carte où un mur est ajouté au nord de (1,1) ; `dotnet test --configuration Release --filter FullyQualifiedName~RevueRc08Tests` | 0 | 1/1 réussi : ordre achevé, pas NE exécuté par le passage E, arrivée en (2,0) |
| W9 | Fichier de relecture ciblée annoncé | `ls docs/reviews/ \| grep CIBLEE` | 1 | absent à la date du contrôle (RC-17) |
| W10 | Base | `git rev-parse HEAD origin/main` | 0 | `25e7a28d…` pour les deux. Je n'ai pas lancé `git fetch`, qui écrirait dans `.git` |

### 6.2 Constats

#### RC-10 — Rien d'autre n'a changé dans le dépôt
- **Gravité :** observation (conforme).
- **État :** vérifié (W2).
- **Preuve :** depuis la relecture ciblée, seuls le rapport d'exécution et le README ont changé. Moteur, tests, archives des mandats, registre, harnais et rapport de relecture générale sont inchangés.

#### RC-11 — Nouvelle ligne du README exacte, dans l'autorisation
- **Gravité :** observation (conforme).
- **État :** vérifié (W3, W4).
- **Preuve :**
  - le libellé ajouté reproduit exactement l'option choisie ;
  - la ligne reste celle du mandat initial, et l'index ne gagne aucune entrée ;
  - l'avenant n° 2 n'y est toujours pas indexé, ce qui respecte l'autorisation (« référencer le mandat initial et l'avenant n° 1 ») ;
  - la remarque de RC-07 est traitée.

#### RC-12 — Origine et statut de l'avenant n° 2 indiqués exactement (§10, annexe B.4)
- **Gravité :** observation.
- **État :** vérifié (V6 et RC-06 des sections précédentes ; W5).
- **Preuve :**
  - **Horodatage :** 2026-11-22T04:51:30.049Z, exact.
  - **Mode d'extraction :** « extrait mécaniquement du journal de session », exact (archive = message + `\n`).
  - **Archive :** chemin exact.
  - **Statut :** « autorisé par le message lui-même », exact, le texte s'ouvrant sur « Décision du propriétaire : autorisation limitée à l'exécution du présent avenant ». « Non indexé (§8) » est exact et justifié au §8.
  - **Annexe B.4 :** elle renvoie à l'archive au lieu de reproduire le texte. C'est acceptable, puisque l'archive est fidèle.
- **Réserves de forme :**
  - le statut « exécuté » ne sera exact qu'une fois remplis les marqueurs de RC-17 ;
  - l'empreinte annoncée en annexe A n'y figure pas encore (RC-17).

#### RC-13 — RL-13 documenté comme demandé ; RL-11 conservé
- **Gravité :** observation (conforme).
- **État :** vérifié (W5, W8).
- **Preuve, pour RL-13 :**
  - §3, l. 120-124, et §8, l. 341 : le comportement est décrit comme observé dans le seul contexte des tests qui modifient la carte (A4 g) ;
  - il est dit expressément qu'il ne s'agit pas d'une règle de gameplay validée, en citant le point laissé ouvert par MEC-0001 (registre, l. 232 et 258) ;
  - rien n'est arbitré : le §9, point 4, renvoie l'arbitrage au propriétaire ;
  - le texte le dit honnêtement : le comportement « découle de la structure du code », et « aucun test ne le couvre » ;
  - je l'ai confirmé par exécution (W8).
- **Preuve, pour RL-11 :** il est conservé comme réserve au §1 (l. 39), au §7.1 (l. 292), au §8 (l. 340) et au §9 (point 3, à autoriser à part).

#### RC-14 — §1, l. 41 : réserves restantes mal listées
- **Gravité :** à corriger.
- **État :** vérifié (W5).
- **Constat :** la liste « RL-04 à RL-07, RL-09, RL-10, RL-12 et RL-14 à RL-19 » compte RL-09 et RL-15 parmi les observations restantes. Elle contredit :
  - le §1, l. 36 (RL-09 levée, RL-15 levée pour l'avenant n° 1) ;
  - le §7.1 (RL-09 « traité », RL-15 « archivé et indexé ») ;
  - le §7.2 (RL-08 et RL-09 levées).

  RL-15 n'était d'ailleurs pas une observation, mais un constat « à corriger ». Ce n'est pas une levée sans preuve, c'est l'inverse, mais l'incohérence est réelle.
- **Correction suggérée :** « RL-04 à RL-07, RL-10, RL-12, RL-14 et RL-16 à RL-19 », comme au §7.2.

#### RC-15 — §5.2, l. 193 : nombre de lignes ajoutées inexact tel qu'il est écrit
- **Gravité :** à corriger.
- **État :** vérifié (W7).
- **Constat :** « 59 ajoutées » et « 28 ajoutées » ne comptent que les lignes non vides. Le diff donne 67 et 32 lignes ajoutées ; les lignes retirées (2 et 0) sont exactes.
- **Correction suggérée :** « 67 lignes ajoutées (59 non vides) » et « 32 lignes ajoutées (28 non vides) ».

#### RC-16 — Imprécisions mineures dans les ajouts
- **Gravité :** observation.
- **État :** vérifié (W5, W6) ; lecture du script `mutants.py` pour le premier point.
- **Constats, point par point :**
  - **§5.2, l. 202** : « Chaque mutant remplace une seule ligne du moteur ». M22 supprime en fait le bloc `if (!outcome.Accepted) { break; }`, soit quatre lignes. Écrire « un seul passage du moteur ».
  - **§7.1, tableau** : « Les gravités sont celles du relecteur », mais RL-12 et RL-13 y figurent comme « à décider » et RL-14 comme « limite ». Ma gravité était « observation », avec point à décider ou limite à déclarer. Ce tableau existait déjà dans `rapport.avant.md`.
  - **§8, l. 343** : « les tests correspondants du relecteur réussissent ». Aucun test du relecteur ne correspond à RL-10.
  - **§7.2, l. 310** : « Recalcul indépendant des valeurs des trois scénarios et de T13 ». Dans la relecture ciblée, j'ai recalculé les trois scénarios ; pour T13, le chemin et le coût l'avaient été lors de la revue générale, et les passages observés par le moteur C# (Rv07), puis par les tests. Écrire par exemple « des trois scénarios, et de T13 lors de la revue générale ».
  - **§10, ligne des consignes de T13** : « message du propriétaire du 2026-11-21T21:41:14.860Z ». C'est la réponse libre du propriétaire à une question posée par Claude Code (journal, ligne 4338), comme l'autorisation de 21:09:26. B.2 en reproduit exactement le texte. On pourrait le préciser, à la manière de la nouvelle ligne du README.

#### RC-17 — Marqueurs et copie de relecture encore à produire
- **Gravité :** observation (en attente).
- **État :** non vérifié (W9).
- **Constat :** trois éléments restent à produire :
  - les marqueurs `COMPLEMENT_RC08` (§7.2, l. 336) et `EMPREINTES` (annexe A, l. 381) ;
  - le fichier `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-RELECTURE-CIBLEE-AVENANT-2-2026-11-22.md`, annoncé au §2 (l. 70), au §7.2 (l. 304) et au §10 (l. 374), mais absent.

  Ces trois éléments conditionnent l'exactitude des mentions « copié sans modification » et « empreinte en annexe A ».
- **Conditions de clôture :**
  - le fichier de relecture ciblée est la copie octet pour octet du présent rapport définitif, dont j'indique l'empreinte dans ma réponse ;
  - l'annexe A comprend au moins :
    - les deux archives d'avenant (`6055e752…`, `6027eb32…`) et le mandat initial (`c8d9a38f…`) ;
    - le README (`c5f34bc8…`, ou sa version finale) et le registre (`7b4931f3…`) ;
    - les 18 sources du moteur, inchangées ;
    - les tests modifiés (`GeometryTests.cs` `b79fc99e…`, `SearchAndExecutionTests.cs` `700efad3…`) et les autres fichiers de tests ;
    - les deux rapports de relecture ;
  - le diff final du rapport, par rapport à `44da10db…`, se limite aux deux marqueurs remplis et aux corrections de RC-14 à RC-16.

### 6.3 Verdict actualisé

**Conforme sous réserves.**
- **RC-08 est levée.** L'origine et le statut de l'avenant n° 2 sont indiqués exactement (RC-12). RL-13 est documenté dans les termes demandés, sans arbitrage, et le comportement est confirmé par exécution (RC-13). RL-11 est conservé (RC-13). Les résultats rapportés aux §1, §4, §5.2, §6, §7, §8 et §9 sont les résultats réels, sauf deux inexactitudes à corriger : RC-14 et RC-15. Aucune réserve n'y est annoncée levée sans preuve. Le résumé de ma relecture ciblée au §7.2 est fidèle, à une imprécision près (RC-16).
- **La nouvelle ligne du README est exacte, dans l'autorisation (RC-11), et rien d'autre n'a changé dans le dépôt (RC-10).**
- **Réserves restantes :** RC-14 et RC-15 (à corriger, corrections locales du rapport) ; RC-17 (en attente : marqueurs et copie du rapport de relecture ciblée).
- **RL-01, RL-02 et RL-03 restent levées**, sur les preuves de la section 4.

Ce verdict ne valide ni le commit ni la publication.
