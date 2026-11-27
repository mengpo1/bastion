# Bastion — Lot 1I : corrections documentaires RH-02 et RH-08

**Date :** 25 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md`. C'est la transcription du message du propriétaire du 2026-11-25T20:55:03Z, extraite mécaniquement du journal de session (SHA-256 `f2976095…3d9f`) ; son identité avec un fichier original n'est pas vérifiée. Statut du texte : « PRÉPARÉ — exécution non encore autorisée ».
**Autorisation d'exécution :** 2026-11-25T20:55:38Z. En réponse à une question de Claude Code, le propriétaire a choisi « Autoriser en local (Recommandé) » : exécution locale sur les quatre fichiers du §5 du mandat, sans commit, push, PR ni fusion.
**Base :** `origin/main` = `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5`, commit de fusion de la PR #27, établi par `git fetch origin main` avant toute modification. L'arbre de travail était propre.
**Branche :** `claude/lot-1i-corrections-documentaires`, créée localement à partir de cette base.
**Dernière correction :** message « BASTION — LOT-1I — Dernière correction documentaire » du 2026-11-25T21:49:12Z. L'orchestrateur y accepte RI-01 et RI-02 et décide de corriger la mention ambiguë de la CI à la ligne 205 de la notice (§5.2). Il n'autorise ni commit, ni push, ni PR, ni fusion.
**État :** lot exécuté et vérifié localement. La relecture indépendante conclut à la conformité au mandat, après correction de RI-01 et RI-02 (§5.1). La correction de la ligne 205 a été vérifiée par le même relecteur (§5.2). **Rien n'est commité ni publié.**

## 1. Contexte

La relecture indépendante du lot 1H (`docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`, §7) avait relevé deux observations hors de son périmètre.
- **RH-02 :** la notice du client Godot, `src/Bastion.Client.Godot/README.md`, contredisait le registre sur macOS. Elle annonçait six essais manuels et donnait les scénarios 2 à 4 pour non essayés, alors que le propriétaire avait déclaré, le 25 novembre 2026, sept essais satisfaisants du prototype du lot 1G.
- **RH-08 :** `docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` était présent dans le dépôt depuis le 18 novembre 2026, mais absent de l'index `docs/mandates/README.md`.

Le lot est exclusivement documentaire. Il n'introduit aucune règle ni fonctionnalité.

## 2. Modifications exactes

| Fichier | Changement |
|---|---|
| `src/Bastion.Client.Godot/README.md` | RH-02 : section macOS et section « Limites » ; +41 −9 |
| `docs/mandates/README.md` | RH-08 : une entrée pour le mandat MEC-0001 ; une entrée pour le présent mandat ; +2 |
| `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md` | nouveau : le mandat, tel que reçu |
| `docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md` | nouveau : ce rapport |

**Inchangés**, vérifiés par `git diff --stat origin/main` sans sortie :
- le code C# et Godot (`src/Bastion.Simulation/`, `*.cs`, `*.tscn`, `project.godot`) et les tests ;
- le registre et les autres registres (`docs/gameplay/`, `docs/decisions/`, `docs/references/`) ;
- la CI, les hooks et le harnais (`.github/`, `scripts/`, `.claude/`, `CLAUDE.md`) ;
- le README principal ;
- le mandat MEC-0001 lui-même.

### 2.1 RH-02 : notice du client Godot

**Section macOS :**
- **Titre (ancienne ligne 96) :** « six essais manuels déclarés conformes » devient « essais manuels déclarés par le propriétaire : six le 23 novembre 2026, sept le 25 novembre 2026 ; non reproduits de façon indépendante ».
- **Essais du 23 novembre 2026 :** un sous-titre « Essais déclarés le 23 novembre 2026, sur le prototype du lot 1D » est ajouté. Il date la déclaration, seule date établie par les sources (RI-03). Le compte rendu historique et ses six essais sont conservés mot pour mot.
- **Ancienne ligne 107 :** « Ces trois scénarios et les touches 1 à 4 et T n'ont pas été essayés sous macOS » devient « Ils ne couvrent ni ces trois scénarios, ni les touches 1 à 4 et T ». La phrase porte désormais sur les seuls essais du 23 novembre, ce qui reste exact.
- **Essais du 25 novembre 2026 :** une sous-section nouvelle, « Essais déclarés le 25 novembre 2026, sur le prototype du lot 1G », reprend le compte rendu de l'annexe A du rapport du lot 1H. Elle comprend :
  - le tableau des sept essais et de leurs résultats déclarés ;
  - la liste des points sur lesquels les essais portaient « notamment », tirée du même compte rendu ;
  - la mention que ce sont des déclarations sans reproduction indépendante, distinctes des six essais du 23 novembre ;
  - la mention que le compte rendu n'établit ni la version de macOS, ni le commit essayé, ni les modalités d'affichage, ni les périphériques (RI-04).
- **Commandes :** un sous-titre « Chemin et commandes » est ajouté avant le paragraphe existant, qui est inchangé, pour le séparer des deux comptes rendus.

**Section « Limites » :**
- **macOS (ancienne ligne 175) :** l'état au moment des lots 1F et 1G est conservé. La phrase inexacte « L'essai manuel du scénario 4 sous macOS n'a pas eu lieu » est remplacée par le renvoi aux sept essais déclarés le 25 novembre.
- **Écran réel (ancienne ligne 176) :** « aucun essai, sous aucun système » devient « aucun essai par Claude Code ni par la CI, sous aucun système ». Suivent trois sous-puces, qui distinguent les sources selon la décision de l'orchestrateur (§5.2) :
  - **CI GitHub Actions :** tests automatisés, dont le contrôle fumée en mode headless, sans affichage ni capture d'écran ;
  - **vérifications locales sous Xvfb :** captures automatiques qui permettent d'examiner le rendu ;
  - **macOS :** sept essais déclarés satisfaisants, sans reproduction indépendante ni précision sur les modalités matérielles.

  Rien n'est supposé sur le matériel. Deux formulations ont précédé celle-ci : « Le rendu vérifié de façon automatique… », corrigée pour RI-01, puis « Pour Claude Code et la CI, le rendu n'est connu que par des captures automatiques… », que la décision du §5.2 a jugée ambiguë.
- **Clavier et souris physiques (ancienne ligne 177) :** même reformulation ; les essais déclarés ne précisent pas les périphériques utilisés. Le mandat ne cite pas cette ligne, mais elle était devenue inexacte de la même façon que la ligne 176.
- **Scénarios 2 et 3 :** l'affirmation « aucune validation manuelle, sur aucun système » était devenue inexacte. L'essai « Vérifier les anciens scénarios » a été déclaré satisfaisant le 25 novembre. Le compte rendu cite l'absence d'effet de T dans les scénarios 1 à 3, sans détailler les autres points.
- **Scénario 4 :** « aucune validation manuelle, sur aucun système » devient : « cinq des sept essais déclarés satisfaisants par le propriétaire sous macOS le 25 novembre 2026 portent sur ce scénario (chargement, deux fins de tour, déplacement puis fin de tour, réinitialisation) […]. Aucune sur un autre système ». Les essais 6 et 7, sur les anciens scénarios et la fenêtre, ne sont pas comptés ici (RI-02).
- **Touches 1 à 4 et T :** « jamais avec un clavier physique » devient « jamais avec un clavier physique par Claude Code ni par la CI ». La phrase ajoutée précise que les essais déclarés citent les touches R, 4 et T, sans préciser le clavier ni sa disposition.
- **Récapitulatif macOS (ancienne ligne 197) :** il mentionne les deux comptes rendus, et les limites du second.

**Correspondance des numéros de ligne (RI-09).** Le mandat et le rapport du lot 1H citent les lignes de la notice d'avant le lot. Elles se trouvent désormais :

| Mention | Avant | Après |
|---|---|---|
| titre macOS | 96 | 96 |
| essais du 23 novembre : couverture | 107 | 109 |
| limites : macOS | 175 | 204 |
| limites : écran réel | 176 | 205 à 208 |
| limites : clavier et souris physiques | 177 | 209 |
| scénarios 2 et 3 : validation manuelle | 188 | 220 |
| scénario 4 : validation manuelle | 192 | 224 |
| touches : clavier physique | 196 | 228 |
| récapitulatif macOS | 197 | 229 |

**Ce qui est conservé :**
- la section Linux, son titre compris (« pas sur un écran réel ») ;
- la puce Linux des limites (« jamais essayé sur un écran réel ni avec une souris physique ») ;
- les mentions de la CI, avec leur réserve « au moment du lot » ;
- les captures Xvfb et les commandes d'installation et de lancement ;
- la mention de `gtimeout`.

### 2.2 RH-08 : index des mandats

**Entrée pour le mandat MEC-0001.** Elle est insérée après celle du mandat LOT-2J (15 novembre 2026), dans l'ordre chronologique des autres entrées.
- **Document :** le nom du fichier, l'objet, et le titre exact du texte : « BASTION — Mandat d'inscription documentaire MEC-0001 — v1.0 ».
- **Provenance :**
  - « original `.md` » ;
  - fichier joint au message du propriétaire du 17 novembre 2026, d'après `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md` ;
  - archivé sans modification le 18 novembre 2026 depuis l'archive `BASTION-LOT-ARCHIVAGE-MEC-0001-SOURCES-ET-MANDAT.zip`, empreinte recalculée sur l'original, d'après `docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` ;
  - commit `1ecc608`, inclus dans la fusion de la PR n° 15 (`818c646`).
- **Statut :**
  - celui du fichier, conservé tel quel : « AUTORISÉ POUR MODIFICATIONS DOCUMENTAIRES UNIQUEMENT », le 17 novembre 2026, par « Je valide » ;
  - sa portée : modifications locales, sans commit, push, publication ni fusion, et sans gameplay ;
  - son exécution, documentée par le rapport du 17 novembre. Ce rapport documente aussi une autorisation distincte, reçue ensuite : un commit et un push sur la seule branche `claude/new-session-mgfohp`, sans PR ni fusion. Elle n'est pas attribuée au mandat (RI-07) ;
  - MEC-0001 « restait reportée à l'indexation », formule qui ne vieillira pas ;
  - la colonne commence par « **Autorisé par le propriétaire le 17 novembre 2026** », et la mention « Indexé ici par le lot 1I » y figure, comme dans les entrées voisines (RI-08).
- **Empreinte :** `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0`. Elle est calculée sur le fichier présent (8 927 octets), et elle est identique à l'objet du commit `1ecc608` et à celle du rapport d'archivage.

**Entrée pour le présent mandat :** elle est ajoutée en fin d'index, au format des transcriptions précédentes.

## 3. Sources documentaires

- **Essais macOS du 25 novembre 2026 :** l'annexe A de `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`, désignée par le mandat.
- **Essais macOS du 23 novembre 2026 :** la notice elle-même, texte historique conservé.
- **Mandat MEC-0001 :** le document lui-même, en entier ; `docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` ; `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md` ; l'historique Git (`git log`, `git merge-base --is-ancestor 1ecc608 818c646`).
- **Observations RH-02 et RH-08 :** `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`, §7 et §8.

## 4. Vérifications

Toutes les commandes ont été lancées dans le dépôt de travail et renvoient le code 0.

| Vérification | Résultat |
|---|---|
| `git fetch origin main` ; `git rev-parse origin/main` | `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5` ; arbre propre avant le lot |
| `git status --short -uall` | `M docs/mandates/README.md`, `M src/Bastion.Client.Godot/README.md`, `?? docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md`, puis ce rapport |
| `git diff --stat origin/main` sur le code, les tests, les registres, la CI, le harnais, le README principal et le mandat MEC-0001 | aucune sortie |
| Empreintes de l'index, recalculées pour chaque entrée | 23 concordantes, 0 écart ; aucun fichier de `docs/mandates/` absent de l'index |
| Mentions de la notice (`grep` sur « macOS », « écran réel », « physique », « validation manuelle ») | chacune vérifiée ; celles devenues inexactes sont traitées (§2.1) |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |
| `dotnet format --verify-no-changes` | aucune sortie |
| `dotnet build` ; `dotnet test --no-build` | 0 Warning(s), 0 Error(s) ; « Passed! - Failed: 0, Passed: 65 » |

## 5. Relecture indépendante ciblée

### 5.1 Relecture du lot et vérification des corrections RI-01 à RI-08

Un agent distinct du développeur a relu le lot en lecture seule. Il a recalculé les empreintes, comparé l'archive au journal de session, relu les sources de la notice et de l'index, et lancé les contrôles dans une copie neuve. Il n'a pas relu le présent rapport.

Après les corrections, le même agent les a vérifiées ; c'est la dernière section de son rapport. Son rapport est reproduit ci-dessous sans modification, entre deux filets : c'est le fichier `relecture-1i/relecture.md` du dossier temporaire de la session, de SHA-256 `dff1f0a310bd02dcbfa61b67e8865df4a4b09f8cb5ecd4881e8b27f38abb644d`.

---

# Relecture indépendante — LOT-1I, corrections documentaires RH-02 et RH-08

- **Date :** 25 novembre 2026
- **Objet :** conformité du lot 1I (arbre de travail, rien n'est commité) au mandat `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md`
- **Relecteur :** agent relecteur indépendant, distinct du développeur. J'ai travaillé en lecture seule sur `/home/user/bastion`, sans édition, `git add`, commit, stash, checkout, reset, fetch ni push. Les contrôles ont tourné dans une copie neuve. Cette relecture n'est pas une validation finale : la décision revient au propriétaire.
- **Base :** branche `claude/lot-1i-corrections-documentaires`. HEAD = `origin/main` = `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5`, et `git ls-remote origin refs/heads/main` renvoie la même valeur (code 0).

**État relu (SHA-256) :**

| Fichier | Arbre de travail | HEAD |
|---|---|---|
| `src/Bastion.Client.Godot/README.md` | `c929af99e7da20b8c6d75b08d7d099332300c4259bb45d3afaf8ea47c1beef60` | `2181fe00914c8bf84ab8adb86f73cc2f382d40cbee23ede73d437fddc1dcc311` |
| `docs/mandates/README.md` | `ef9fbcad78c40206169ebe9475f4eb51560eaf4be09a04ffbe799313f7b82ae9` | `15d95fce5d483e41f5eb89e783dc9558123ccc841bb1ed1ce86353cbaab85b22` |
| `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md` | `f2976095b9c0a14069e556d55078db4c16d4eba26574a01cd12eb300b2ef3d9f` | absent |
| `docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` | identique |
| `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md` | `deb4bdd409e79d219a53337a717b8ccdab83acc331ef13335fcbebd0094d72fc` | inchangé |
| `docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md` | `7f457d789797f2fa7129ea1666ebfa66e6ad857534e8508d95419491252754c2` | inchangé |
| `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md` | `ac4d72c6baa75412406bec427cd348f53de03b635a0d45c62e13c3b2e12d09f1` | inchangé |

Comme demandé, je n'ai pas relu `docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md`, qui est en cours de rédaction.

## 1. Méthode

J'ai d'abord lu `CLAUDE.md` et le mandat 1I en entier. J'ai ensuite comparé la notice à HEAD, ligne par ligne, avec l'annexe A et le §5.2 du rapport 1H, et avec la ligne `GAMEPLAY-DECISIONS.md:650`. J'ai cherché dans toute la notice les mentions « macOS », « manuel », « écran réel », « physique », « clavier », « souris » et « essai ».

Pour le mandat MEC-0001, j'ai lu en entier le document, les deux rapports du 17 et du 18 novembre et l'historique git, et j'ai recalculé les empreintes. J'ai extrait le message à archiver et la réponse d'autorisation du journal de session. Enfin, j'ai recalculé toutes les empreintes de l'index avec un script (`relecture-1i/check-index.sh`), puis lancé les contrôles dans une copie neuve.

## 2. Commandes exécutées

| # | Commande (résumé) | Résultat | Code | Classement |
|---|---|---|---|---|
| C1 | `git status --porcelain -uall` (au début et à la fin) | ` M docs/mandates/README.md`, ` M src/Bastion.Client.Godot/README.md`, `?? docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md`, `?? docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md` ; aucun fichier ignoré hors `bin/`, `obj/` et `.godot/` ; aucun stash | 0 | exécuté et réussi |
| C2 | `git diff --stat` ; `git diff -U0` | notice : +38 −9, 9 lignes retirées (HEAD 96, 107, 175-177, 188, 192, 196, 197) ; index : 2 lignes ajoutées, 0 retirée | 0 | exécuté et réussi |
| C3 | `git diff --check` | aucune sortie | 0 | exécuté et réussi |
| C4 | `git diff --exit-code` sur le mandat MEC-0001 ; `git log` de ce fichier | inchangé ; un seul commit : `1ecc608 2026-11-18 03:55:50 +0100 docs(mec-0001): archiver le mandat validé et la consolidation v1.4.1` | 0 | exécuté et réussi |
| C5 | `sha256sum` du mandat MEC-0001 ; `git cat-file -p` de son blob à `1ecc608` et à HEAD | `90e049c7…85e0` trois fois, 66 lignes, 8 927 octets | 0 | exécuté et réussi |
| C6 | `git log --merges --ancestry-path 1ecc608..HEAD` | `818c646 2026-11-18 04:04:45 +0100 Merge pull request #15 from mengpo1/docs/archive-mec-0001-sources-2026-11-18` | 0 | exécuté et réussi |
| C7 | extraction de l'entrée `user` du journal (ligne 8868, 2026-11-25T20:55:03.787Z), puis `cmp` du texte plus un saut de ligne avec l'archive | 4 756 octets sans saut de ligne final ; SHA-256 sans LF `e57af3e0…9fc0`, avec LF `f2976095…ef9f` ; `cmp` sans différence | 0 | exécuté et réussi |
| C8 | même contrôle pour le mandat 1H (2026-11-25T19:47:54.665Z) | texte plus LF égal à l'archive : convention identique | 0 | exécuté et réussi |
| C9 | réponse d'autorisation (ligne 8891, 2026-11-25T20:55:38.443Z) | `tool_result` : « …Autorisez-vous l'exécution locale de LOT-1I sur la branche claude/lot-1i-corrections-documentaires, limitée aux quatre fichiers du §5 ? »="Autoriser en local (Recommandé)" | 0 | exécuté et réussi |
| C10 | annexe A du rapport 1H comparée au message du journal (2026-11-25T19:48:04Z) | identiques : SHA-256 `a4a22cae…e292d`, 1 980 octets | 0 | exécuté et réussi |
| C11 | `check-index.sh docs/mandates` : empreinte de chaque ligne de l'index, puis fichiers non indexés | 23 concordantes, 0 discordante, 0 fichier non indexé ; 23 lignes pour 23 fichiers | 0 | exécuté et réussi |
| C12 | recherche du titre et des statuts cités dans l'index (`grep -cF`) | titre « BASTION — Mandat d'inscription documentaire MEC-0001 — v1.0 » : 1 ; « AUTORISÉ POUR MODIFICATIONS DOCUMENTAIRES UNIQUEMENT » : 1 ; « PRÉPARÉ — exécution non encore autorisée » : présent dans le mandat 1I, ligne 4 | 0 | exécuté et réussi |
| C13 | copie neuve (`tar` sans `.git`, `bin`, `obj`, `.godot`), puis `diff -rq docs` avec le dépôt | copie identique | 0 | exécuté et réussi |
| C14 | `bash scripts/harness/test-hooks.sh` (copie neuve) | `== 75 tests, 0 échec(s) ==` | 0 | exécuté et réussi |
| C15 | `dotnet format --verify-no-changes` (copie neuve, SDK 10.0.115) | aucune sortie | 0 | exécuté et réussi |
| C16 | `dotnet build` (copie neuve) | 0 avertissement, 0 erreur | 0 | exécuté et réussi |
| C17 | `dotnet test` (copie neuve) | `Passed! - Failed: 0, Passed: 65, Skipped: 0, Total: 65` | 0 | exécuté et réussi |

## 3. Conformités constatées

- **Périmètre (C1, C2) :** quatre fichiers, ceux du §5 du mandat. Rien n'est modifié dans `src/` hors de la notice, ni dans `tests/`, `docs/gameplay/`, `docs/decisions/`, `docs/references/`, `.github/`, `scripts/`, `.claude/` ou `CLAUDE.md`, ni dans un document historique, dont le mandat MEC-0001 (C4). *Exécuté et réussi.*
- **Compte rendu du 23 novembre conservé :** les lignes 100 à 108 sont identiques aux lignes 98 à 106 de HEAD (aucun hunk). Seule la ligne 107, que le mandat demande de corriger, est reformulée (`:109`) : « Ils ne couvrent ni ces trois scénarios, ni les touches 1 à 4 et T », ce qui est exact. *Inspecté.*
- **Compte rendu du 25 novembre (`:111-134`) :**
  - il est présenté à part ;
  - son tableau est identique à celui du §2 du mandat et aux sept lignes de l'annexe A, toutes « Satisfaisant » ;
  - la liste « notamment » reprend les sept puces de l'annexe A sans ajout ;
  - la provenance est fidèle à la ligne « Source » de l'annexe ;
  - la phrase imposée « Ces sept résultats sont des déclarations du propriétaire, sans reproduction indépendante. » est reprise mot pour mot (`:134`).

  La fenêtre de 800 × 720 pixels concorde avec `project.godot:19-20`. *Inspecté ; l'identité de l'annexe A avec le journal est exécutée et réussie (C10).*
- **Rien n'est inventé :**
  - le commit, les modalités d'affichage et les périphériques sont déclarés « non établis » (`:134`, `:205`, `:206`, `:226`) ;
  - le clavier et sa disposition sont donnés comme non précisés (`:225`) ;
  - aucune version de macOS n'est avancée.

  *Inspecté.*
- **Mentions citées par le mandat :** toutes sont traitées : HEAD 96 → `:96`, 107 → `:109`, 175 → `:204`, 176 → `:205`, 197 → `:226`. Les autres mentions devenues inexactes le sont aussi : HEAD 177 (clavier et souris) → `:206`, 188 et 192 (« aucune validation manuelle ») → `:217` et `:221`, 196 (clavier physique) → `:225`. La ligne Linux (`:213`) et le titre Linux (`:74`) restent exacts et sont inchangés. *Inspecté.*
- **Informations préservées :** Linux, CI, Xvfb et commandes d'installation. Aucun hunk ne touche les lignes 40-94 ni 146-199 de la notice actuelle (C2). *Exécuté et réussi.*
- **Cohérence avec le registre :** `:226` reprend « (scénario 4, anciens scénarios et fenêtre) », comme `GAMEPLAY-DECISIONS.md:650`. *Inspecté.*
- **Entrée MEC-0001 de l'index (`docs/mandates/README.md:24`) :**
  - le titre du texte est exact (C12) ;
  - l'empreinte est exacte (C5, C11) ;
  - la provenance est exacte : l'empreinte du fichier joint le 17 novembre (`MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md:8`), celle de l'archive (`MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md:18`) et celle du fichier sont la même ; l'archivage date du 18 novembre (`:3` de ce rapport) ; la PR n° 15 est établie par le commit de fusion `818c646` (C6) ;
  - le statut cite exactement la ligne 3 du document, y compris l'exclusion du commit, du push, de la publication, de la fusion et du gameplay ;
  - l'exécution du 17 novembre est établie par le commit `b20d5ac` du 2026-11-17 ;
  - « MEC-0001 reste reportée » est vrai à HEAD (`GAMEPLAY-DECISIONS.md:60`) ;
  - l'entrée ne convertit pas l'autorisation locale en autorisation de publication ou d'implémentation ; l'autorisation ultérieure est attribuée à un message distinct, documenté au rapport (`:13`) ;
  - sa position, entre le 15 et le 21 novembre, respecte l'ordre chronologique.

  *Inspecté, avec les empreintes exécutées et réussies.*
- **Archive et entrée 1I (`:35`) :**
  - l'archive est mécaniquement identique au message suivi d'un saut de ligne final, selon la même convention que le mandat 1H (C7, C8) ;
  - les horodatages 20:55:03 et 20:55:38 UTC, le libellé de l'option et la limite aux « quatre fichiers du §5 » sont exacts (C9) ;
  - le statut cité, « PRÉPARÉ — exécution non encore autorisée », est exact.

  *Exécuté et réussi.*

## 4. Constats

### RI-01 — À corriger (mineur) — « Le rendu vérifié de façon automatique », `src/Bastion.Client.Godot/README.md:205`

- **Preuve :** la nouvelle phrase dit « Le rendu vérifié de façon automatique n'est connu que par des captures sous affichage virtuel (Xvfb) ». Or la notice dit ailleurs que le dessin « n'est pas contrôlé automatiquement : seules les captures le montrent » (`:148`), et que les captures ont été inspectées lors des relectures (`:224`, « résultat inspecté sur des captures »). L'ancienne formulation était exacte (HEAD 176, « des captures automatiques ») : ce sont les captures qui sont automatiques, pas la vérification du rendu.
- **Correction suggérée :** « Pour Claude Code et la CI, le rendu n'est connu que par des captures automatiques sous affichage virtuel (Xvfb). »

### RI-02 — À corriger (mineur) — sept essais attribués au seul scénario 4, `:221`

- **Preuve :** sous « Scénario 4 (lot 1G) », la notice écrit « validation manuelle : sept essais déclarés satisfaisants ». Mais l'essai 6, « Vérifier les anciens scénarios », porte sur les scénarios 1 à 3 : il est d'ailleurs compté aussi sous « Scénarios 2 et 3 » (`:217`). L'essai 7, « Vérifier la fenêtre », n'est rattaché à aucun scénario. `:226` et `GAMEPLAY-DECISIONS.md:650` ventilent correctement « (scénario 4, anciens scénarios et fenêtre) ».
- **Correction suggérée :** « validation manuelle : cinq des sept essais déclarés satisfaisants par le propriétaire sous macOS le 25 novembre 2026 portent sur ce scénario (chargement, deux fins de tour, déplacement puis fin de tour, réinitialisation) ; sans reproduction indépendante. Aucune sur un autre système. »

### RI-03 — Observation — les titres datent les essais, `:98` et `:111`

- **Preuve :** l'annexe A établit la date de transmission du compte rendu, « le 25 novembre 2026, après les essais du LOT-1G », et non la date des essais. De même, `:100` dit « a déclaré conformes ». La PR #26 a été fusionnée le 2026-11-25 à 19:17 UTC et le compte rendu date de 19:48 UTC : le jour des essais n'est pas établi. Le titre `:96`, qui dit « déclarés … six le 23 novembre 2026, sept le 25 novembre 2026 », est exact.
- **Correction suggérée (facultative) :** « Essais déclarés le 23 novembre 2026… » et « Essais déclarés le 25 novembre 2026… ».

### RI-04 — Observation — version de macOS non mentionnée pour le 25 novembre, `:134` et `:226`

- **Preuve :** rien n'est inventé, mais là où `:100` précise que la version de macOS n'est pas connue pour le 23 novembre, `:134` ne le précise pas pour le 25 novembre.
- **Correction suggérée (facultative) :** ajouter « ni la version de macOS » à `:134`.

### RI-05 — Observation (forme) — la rubrique « Essais non effectués » mentionne désormais des essais faits, `:203-204`

- **Preuve :** le titre « …au moment de leur réalisation » est répété par « à la réalisation des lots ». La puce rapporte aussi, après « Depuis », les sept essais du 25 novembre.
- **Appréciation :** le texte reste exact et lisible, et le marqueur temporel est explicite. Aucune action n'est requise.

### RI-06 — Observation — « seules les captures le montrent », `:148`

- **Preuve :** la phrase n'est pas modifiée. Elle se lit dans le contexte du contrôle fumée, et elle coexistait déjà avec les essais du 23 novembre.
- **Appréciation :** elle est défendable, et la modifier serait un excès. Aucune action.

### RI-07 — Observation — « autorisation de publication distincte », `docs/mandates/README.md:24`

- **Preuve :** l'autorisation ultérieure (`MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md:13`) ne porte que sur « un commit et […] un push exclusivement sur la branche `claude/new-session-mgfohp` », avec « Ne crée pas de PR et ne fusionne pas dans `main` ». Le mot « publication » est exact au sens de `CLAUDE.md` §6, mais il est plus large.
- **Correction suggérée (facultative) :** « l'autorisation distincte, reçue ensuite, d'un commit et d'un push sur la seule branche `claude/new-session-mgfohp`, sans PR ni fusion ».

### RI-08 — Observation (forme) — l'entrée MEC-0001 diffère légèrement des autres, `docs/mandates/README.md:24`

- **Preuve :**
  - la colonne « Statut » ne commence pas par « **Autorisé par le propriétaire le …** », comme celles des entrées 0C à 1I (`:18-35`) ;
  - la mention « Indexé ici par le lot 1I » est dans la colonne « Provenance », alors que l'avenant n° 2 place une mention comparable dans la colonne « Statut » (`:27`) ;
  - « MEC-0001 reste reportée » est un état courant, exact à HEAD, qui peut vieillir.
- **Appréciation :** rien d'inexact. Une harmonisation serait facultative.

### RI-09 — Observation — les numéros de ligne des documents historiques sont décalés

- **Preuve :** `LOT-1H-CLOTURE-MEC-0004.md` (RH-02 : `:96`, `:107`, `:175`) et le mandat 1I, §2, visent désormais d'autres lignes : 107 → 109, 175 → 204, 176 → 205, 197 → 226. C'est inévitable, et ces documents ne doivent pas être modifiés.
- **Suggestion :** donner cette table de correspondance dans le rapport du lot. Je ne l'ai pas vérifié, puisque je n'ai pas relu le rapport.

### RI-10 — Observation — demande du hook `Stop` contraire au mandat

- **Preuve :** le journal porte, à 2026-11-25T20:59:19Z, « Stop hook feedback: … Please commit and push these changes to the remote branch. ». Le §8 du mandat interdit commit, push, PR et fusion. À la fin de ma relecture, HEAD est toujours égal à `origin/main` et rien n'est commité (C1) : la demande n'a pas été suivie, ce qui est conforme.
- **Suggestion :** le signaler dans le rapport du lot comme limite connue du harnais. Le harnais ne doit pas être modifié.

## 5. Ce que je n'ai pas pu vérifier

- **Essais macOS :** leur réalité, la configuration employée et le commit essayé, pour le 23 comme pour le 25 novembre. *Non vérifié* : ce sont des déclarations.
- **Fichier joint du 17 novembre :** son identité avec le fichier du dépôt ne repose que sur l'empreinte consignée dans `MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md:8`. Le journal de la session du 17 novembre et le message « Je valide » n'étaient pas consultés. *Non vérifié* directement.
- **PR n° 15 sur GitHub :** je n'ai pas consulté son contenu ; seul le message du commit de fusion local `818c646` l'atteste.
- **Rendu Markdown sur GitHub :** tableaux, titres de niveau 4 et listes sans ligne vide. *Inspecté seulement*, non rendu.
- **Rapport du lot :** `docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md` n'est pas relu, conformément à la consigne.
- **CI :** elle n'a pas tourné, puisque rien n'est poussé.
- **Contrôle fumée Godot :** non exécuté, car le lot ne touche aucun code.

## 6. Verdict

**Conforme au mandat sous réserve de RI-01 et RI-02.** Ce sont deux imprécisions mineures de la notice, à corriger dans le fichier autorisé. Je ne relève aucun constat bloquant :

- le périmètre est respecté ;
- les mentions demandées sont toutes traitées ;
- rien n'est inventé ;
- les informations Linux, CI, Xvfb et d'installation sont intactes ;
- l'entrée RH-08 est exacte ;
- l'archive 1I est identique au message ;
- les 23 empreintes concordent ;
- les contrôles réussissent : harnais 75/0, format 0, build 0/0, tests 65/65.

RI-03 à RI-10 sont des observations, dont les corrections sont facultatives. Cette relecture n'est pas une validation finale : la décision revient au propriétaire.

## Vérification des corrections RI-01 à RI-08

- **Date :** 25 novembre 2026. Comme la relecture principale, cette vérification est faite en lecture seule sur `/home/user/bastion`.
- **Base :** HEAD = `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5`. Rien n'est commité.

**Empreintes :**

| Fichier | Version relue (copie conservée) | Version actuelle |
|---|---|---|
| `src/Bastion.Client.Godot/README.md` | `c929af99e7da20b8c6d75b08d7d099332300c4259bb45d3afaf8ea47c1beef60` (`lot1i/notice-relue.md`, concordante) | `7e23f2297b77d85fbb8dcc37e4f2d45e8f199e6d642a54e39f1de59a6381bfba` |
| `docs/mandates/README.md` | `ef9fbcad78c40206169ebe9475f4eb51560eaf4be09a04ffbe799313f7b82ae9` (`lot1i/index-relu.md`, concordante) | `c34e6718d754ccdd243fe311323279dad052006f95b760edb53ac801f404d3fc` |
| `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md` | `f2976095…ef9f` | inchangée |

### Commandes

| # | Commande (résumé) | Résultat | Code | Classement |
|---|---|---|---|---|
| V1 | `sha256sum` des deux copies relues | `c929af99…` et `ef9fbcad…` : ce sont bien les versions relues | 0 | exécuté et réussi |
| V2 | `diff` de la copie relue de la notice avec la notice actuelle | 5 lignes changées et aucune autre : `:98`, `:111`, `:134`, `:205`, `:221` | 1 (différences attendues) | exécuté et réussi |
| V3 | `diff` de la copie relue de l'index avec l'index actuel | 1 ligne changée et aucune autre : `:24` | 1 (différences attendues) | exécuté et réussi |
| V4 | `git status --porcelain -uall` ; `git diff --stat` ; `git diff --check` | les 4 fichiers autorisés seulement ; +40 −9 sur les deux fichiers suivis ; aucun défaut de blanc | 0 | exécuté et réussi |
| V5 | `git diff --exit-code --quiet` sur le mandat MEC-0001, `docs/gameplay/`, le rapport 1H et le rapport d'inscription MEC-0001 | inchangés | 0 | exécuté et réussi |
| V6 | `check-index.sh docs/mandates` | 23 empreintes concordantes, 0 discordante, 0 fichier non indexé | 0 | exécuté et réussi |
| V7 | extraction des citations de `MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md:13` | « Je t'autorise maintenant à créer un commit et à effectuer un push exclusivement sur la branche `claude/new-session-mgfohp`. » et « Ne crée pas de PR et ne fusionne pas dans `main`. » | 0 | exécuté et réussi |
| V8 | copie neuve `relecture-1i/copie-neuve-2`, puis `diff -rq docs` et `cmp` de la notice avec le dépôt | identiques | 0 | exécuté et réussi |
| V9 | `bash scripts/harness/test-hooks.sh` (copie neuve) | `== 75 tests, 0 échec(s) ==` | 0 | exécuté et réussi |
| V10 | `dotnet format --verify-no-changes` (copie neuve) | sortie vide (0 octet) | 0 | exécuté et réussi |

### Résultats

1. **Seules les corrections annoncées sont faites (V2, V3).**
   - Notice :
     - `:98` et `:111` : intertitres « Essais déclarés le … » (RI-03) ;
     - `:134` : « ni la version de macOS » (RI-04) ;
     - `:205` : RI-01 ;
     - `:221` : RI-02.
   - Index : seule la ligne `:24` change (RI-07 et RI-08). L'entrée 1I et les autres lignes sont intactes.
2. **RI-01 est corrigé (`:205`).** La notice écrit maintenant « Pour Claude Code et la CI, le rendu n'est connu que par des captures automatiques sous affichage virtuel (Xvfb) ». Elle ne contredit plus `:148`. *Inspecté.*
   - **Observation, sans action requise :** c'est la formulation que j'avais suggérée. Or la CI ne fait aucune capture : elle n'affiche pas le client (`:58`, `:228`). La phrase reste exacte au sens restrictif, mais elle pourrait laisser croire que la CI fait des captures. Variante facultative : « Le rendu n'est connu que par des captures automatiques sous affichage virtuel (Xvfb), faites en local ; la CI n'affiche pas le client. »
3. **RI-02 est corrigé (`:221`).** La notice écrit maintenant « cinq des sept essais … portent sur ce scénario (chargement, deux fins de tour, déplacement puis fin de tour, réinitialisation ; section macOS) ». C'est exact au vu de l'annexe A du rapport 1H : ce sont les essais 1 à 5. Leur rattachement au scénario 4 est appuyé par les points vérifiés que liste l'annexe : la conservation après « un déplacement et une fin de tour », et « la réinitialisation avec R et 4 ». Il concorde avec `GAMEPLAY-DECISIONS.md:650`. Le double compte avec `:217` disparaît. *Inspecté.*
4. **Corrections facultatives :**
   - **RI-03 :** les deux intertitres reprennent la date de déclaration, qui seule est établie : `:100` pour le 23 novembre, la ligne « Source » de l'annexe A pour le 25 novembre. *Inspecté.*
   - **RI-04 :** l'annexe A ne mentionne aucune version de macOS, donc « n'établit ni la version de macOS » est exact. *Inspecté.*
   - **RI-07 :** l'autorisation distincte est maintenant décrite comme « un commit et un push sur la seule branche `claude/new-session-mgfohp`, sans PR ni fusion », ce qui est conforme à V7. *Inspecté.*
   - **RI-08 :**
     - la colonne « Statut » s'ouvre sur « **Autorisé par le propriétaire le 17 novembre 2026** (« Je valide ») », ce qui est conforme à la ligne 3 du mandat et au rapport d'inscription (`:10`) ;
     - la limitation aux modifications locales, sans commit, push, publication, fusion ni gameplay, est conservée ;
     - « restait reportée à l'indexation » est vrai à HEAD (`GAMEPLAY-DECISIONS.md:60`) ;
     - « Indexé ici par le lot 1I, le 25 novembre 2026 » est passé dans la colonne « Statut », comme pour l'avenant n° 2 (`:27`).

     *Inspecté.*
   - Aucune de ces corrections n'introduit d'inexactitude ni d'information inventée.
5. **Périmètre et empreintes (V4 à V6) :** quatre fichiers seulement ; aucun document historique modifié ; les 23 empreintes de l'index concordent. *Exécuté et réussi.*
6. **Contrôles (V9, V10) :** 75 tests du harnais sans échec ; `dotnet format` sans changement. *Exécuté et réussi.*

**Non vérifié :** le rendu Markdown sur GitHub. Le rapport `docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md` n'est toujours pas relu.

### Verdict

**RI-01 et RI-02 sont corrigés**, et les corrections facultatives RI-03, RI-04, RI-07 et RI-08 sont exactes. Il n'y a aucune autre modification, aucun nouveau constat bloquant et aucun constat à corriger. Une seule observation facultative, dans le résultat 2, porte sur la mention de la CI à `:205`. Le lot est **conforme au mandat**, selon cette relecture. Cette vérification n'est pas une validation finale : la décision revient au propriétaire.

---

**Traitement des constats :**

| Constat | Classement | Traitement |
|---|---|---|
| RI-01 : « rendu vérifié de façon automatique » contredit la notice | à corriger | **Corrigé** : « Pour Claude Code et la CI, le rendu n'est connu que par des captures automatiques sous affichage virtuel (Xvfb). » Le relecteur a vérifié la correction. |
| RI-02 : « sept essais » comptés pour le scénario 4 | à corriger | **Corrigé** : « cinq des sept essais […] portent sur ce scénario ». Le relecteur a vérifié la correction. |
| RI-03 : intertitres datant les essais eux-mêmes | observation | **Appliqué** : « Essais déclarés le … ». |
| RI-04 : version de macOS non mentionnée pour le 25 novembre | observation | **Appliqué** : « ni la version de macOS ». |
| RI-05 : redite « au moment de leur réalisation » | observation de forme | **Conservé** : le texte reste exact. |
| RI-06 : « Seules les captures le montrent » | observation | **Conservé** : la phrase reste exacte dans le contexte du contrôle fumée. |
| RI-07 : « autorisation de publication distincte » trop large | observation | **Appliqué** : un commit et un push sur la seule branche `claude/new-session-mgfohp`, sans PR ni fusion. |
| RI-08 : forme de l'entrée MEC-0001 de l'index | observation de forme | **Appliqué** : la colonne Statut commence par « **Autorisé par le propriétaire le 17 novembre 2026** » ; « Indexé ici » y est placé ; « restait reportée à l'indexation ». |
| RI-09 : numéros de ligne décalés | observation | **Traité dans ce rapport** : table de correspondance au §2.1. |
| RI-10 : demandes du hook `Stop` de commiter et pousser | observation | **Signalé** au §6 ; elles n'ont pas été suivies. |
| Observation de la vérification : la mention de la CI à la ligne 205 | facultative | **Corrigée** sur décision de l'orchestrateur, après cette relecture ; la correction est vérifiée au §5.2. |

### 5.2 Correction de la ligne 205 et sa vérification

**Décision de l'orchestrateur** (2026-11-25T21:49:12Z) :
- corriger la formulation ambiguë sur la CI, à la ligne 205 de la notice : la CI exécute le contrôle fumée en mode headless et ne produit pas de captures ;
- distinguer explicitement la CI GitHub Actions, les vérifications locales sous Xvfb et les sept essais macOS déclarés ;
- ne modifier aucune autre partie de la notice ;
- ne pas recommencer de relecture générale.

**Correction :** la ligne 205 devient les lignes 205 à 208. La notice passe de `7e23f229…` à `623402b0…`, et le `diff` ne compte qu'un hunk, `205c205,208` :

```
- **Écran réel :** aucun essai par Claude Code ni par la CI, sous aucun système (Linux, macOS ou Windows). Trois sources distinctes, à ne pas confondre :
  - **CI GitHub Actions :** tests automatisés, dont le contrôle fumée en mode headless, sans affichage ni capture d'écran ;
  - **vérifications locales sous Xvfb :** captures automatiques sous affichage virtuel, qui permettent d'examiner le rendu ;
  - **macOS :** sept essais manuels déclarés satisfaisants par le propriétaire le 25 novembre 2026, sans reproduction indépendante ni précision sur les modalités matérielles.
```

**Vérification :** le même relecteur indépendant l'a faite, limitée à cette correction. Sa section est ajoutée à la fin de son rapport, dont le SHA-256 est désormais `60628fd24e1459229b608a527832248456c69fd51dbb4b5893b314506d581814`. Elle est reproduite ci-dessous sans modification, entre deux filets.

---

## Vérification de la correction de la ligne 205

- **Date :** 25 novembre 2026. La vérification est faite en lecture seule et se limite à cette correction.
- **Base :** HEAD = `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5`. Rien n'est commité.

**Empreintes :**

| Fichier | Avant | Maintenant |
|---|---|---|
| `src/Bastion.Client.Godot/README.md` | `7e23f2297b77d85fbb8dcc37e4f2d45e8f199e6d642a54e39f1de59a6381bfba` (`lot1i/notice-avant-205.md`, concordante) | `623402b0625909cb660a4809ffce954b4b00f36a42be53245a89f24179653fdd` |
| `docs/mandates/README.md` | `c34e6718…d3fc` | inchangé |
| `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md` | `f2976095…ef9f` | inchangé |

### Commandes

| # | Commande (résumé) | Résultat | Code | Classement |
|---|---|---|---|---|
| W1 | `sha256sum` de la copie conservée et des fichiers du lot | la copie vaut `7e23f229…` ; la notice vaut `623402b0…` ; l'index et l'archive sont inchangés | 0 | exécuté et réussi |
| W2 | `diff` de `notice-avant-205.md` avec la notice actuelle | un seul hunk, `205c205,208`, et aucune autre différence | 1 (différence attendue) | exécuté et réussi |
| W3 | `git diff --quiet HEAD -- .github/` ; recherche de `xvfb`, `capture`, `upload-artifact`, `headless`, `smoke` et `DISPLAY` dans `.github/workflows/*.yml` | CI inchangée. Le contrôle fumée tourne en `--headless` sans `--capture` (`ci.yml:89-92`) ; aucun Xvfb, aucune capture, aucun artefact. La CI exécute aussi `dotnet test` (`:39`) et `test-hooks.sh` (`:42`) | 0 | exécuté et réussi |
| W4 | `git diff --check` ; recherche de tabulations et de blancs de fin de ligne aux lignes 205 à 208 | aucun défaut ; 0 ligne concernée | 0 | exécuté et réussi |
| W5 | `git status --porcelain -uall` ; `git diff --stat` | les 4 fichiers autorisés seulement ; notice +41 −9 par rapport à HEAD | 0 | exécuté et réussi |
| W6 | `check-index.sh docs/mandates` | 23 empreintes concordantes, 0 discordante, 0 fichier non indexé | 0 | exécuté et réussi |
| W7 | copie neuve `relecture-1i/copie-neuve-3`, puis `cmp` de la notice et `diff -rq docs` avec le dépôt | identiques | 0 | exécuté et réussi |
| W8 | `bash scripts/harness/test-hooks.sh` (copie neuve) | `== 75 tests, 0 échec(s) ==` | 0 | exécuté et réussi |
| W9 | `dotnet format --verify-no-changes` (copie neuve) | sortie vide | 0 | exécuté et réussi |

### Résultats

1. **Seule la ligne 205 a changé (W2).** Elle occupe maintenant les lignes 205 à 208. La première phrase, « aucun essai par Claude Code ni par la CI, sous aucun système », est conservée. Le reste de la notice est identique octet pour octet. *Exécuté et réussi.*
2. **La formulation respecte la décision et elle est exacte.** Les trois sources sont distinguées explicitement :
   - **CI GitHub Actions (`:206`) :** « tests automatisés, dont le contrôle fumée en mode headless, sans affichage ni capture d'écran ». C'est conforme à `ci.yml:39`, `:42` et `:89-92` (W3).
   - **Vérifications locales sous Xvfb (`:207`) :** « captures automatiques sous affichage virtuel, qui permettent d'examiner le rendu ». C'est conforme à `:195-199`.
   - **macOS (`:208`) :** « sept essais manuels déclarés satisfaisants par le propriétaire le 25 novembre 2026, sans reproduction indépendante ni précision sur les modalités matérielles ». C'est conforme à l'annexe A du rapport 1H, qui ne dit rien de l'écran ni des périphériques.

   Aucune information n'est inventée, et l'ambiguïté que j'avais relevée sur la CI disparaît. *Inspecté.*
3. **La formulation est cohérente avec le reste de la notice :**
   - avec `:58` (« La CI n'exécute pas le client avec un affichage ») ;
   - avec `:148` (« seules les captures le montrent ») ;
   - avec `:231`, la puce CI des limites (« contrôle fumée en mode headless seulement ; ni affichage, ni export ») ;
   - avec la section macOS (`:111-134`) et avec `:224` et `:229`.

   La puce ne cite pas les six essais du 23 novembre, qui portent sur le lot 1D. C'est cohérent avec la rubrique, « Essais non effectués pour les lots 1F et 1G », et avec la décision de l'orchestrateur. Ces six essais restent décrits à `:100` et `:229`. *Inspecté ; observation, aucune action.*
4. **Le Markdown est correct.**
   - La puce parente commence à la colonne 0, et ses trois sous-puces sont indentées de deux espaces, comme aux lignes `:213-216` du même fichier.
   - La puce suivante (`:209`) revient au niveau 0.
   - Il n'y a ni tabulation ni blanc final (W4).

   *Inspecté ; le rendu sur GitHub n'est pas vérifié.*
5. **Périmètre et contrôles :**
   - le périmètre reste de quatre fichiers (W5) ;
   - les empreintes de l'index concordent (W6) ;
   - le harnais passe ses 75 tests et `dotnet format` ne signale aucun changement, dans une copie neuve (W8, W9).

   *Exécuté et réussi.*

### Verdict

**La correction de la ligne 205 est conforme à la décision de l'orchestrateur.** Elle est exacte au vu de `.github/workflows/ci.yml` et de l'annexe A, cohérente avec le reste de la notice, et limitée à cette ligne. Je ne relève aucun nouveau constat bloquant ni à corriger. Cette vérification n'est pas une validation finale : la décision revient au propriétaire.

---

## 6. Réserves non résolues

- **Essais macOS :** ce sont des déclarations du propriétaire. Les comptes rendus ne précisent ni la version de macOS, ni les commandes, ni le commit essayé, ni les modalités d'affichage, ni les périphériques. La notice le dit sans rien supposer.
- **Mentions « au moment du lot » :** dans la section « Limites », la phrase « pas encore dans la CI au moment du lot 1F » (et de même pour le lot 1G) reste exacte telle qu'elle est datée. Elle n'est pas complétée, puisque le mandat demande de préserver les informations sur la CI.
- **CI :** rien n'est poussé, donc la CI n'a pas tourné sur ce lot.
- **Demandes du hook `Stop` (RI-10) :** à la fin de plusieurs tours, le hook a demandé de commiter et de pousser (« Please commit and push »). Le §8 du mandat l'interdit : elles n'ont pas été suivies. HEAD reste `origin/main` et rien n'est commité.
- **Observations conservées :** la redite « au moment de leur réalisation » et « à la réalisation des lots » reste en l'état (RI-05). Il en va de même de la phrase « Seules les captures le montrent » du contrôle fumée (RI-06) ; les deux restent exactes.

## 7. Diff final

Ce diff couvre les deux fichiers suivis modifiés. Le mandat archivé est un fichier nouveau, dont le contenu est le message du propriétaire. Ce rapport ne peut pas contenir son propre diff.

```diff
diff --git a/docs/mandates/README.md b/docs/mandates/README.md
index 42eae1e..98430a1 100644
--- a/docs/mandates/README.md
+++ b/docs/mandates/README.md
@@ -21,6 +21,7 @@ Les documents de ce dossier sont conservés tels que reçus. Ne pas les modifier
 | `BASTION-MANDAT-LOT-2H-PREPARATION-INSCRIPTION-v1.0.md` — mandat du lot 2H | copie octet pour octet du fichier publié sur la branche `orchestration/mandats` (commit `24ca7569bd3a25cc2b0f3807a0afc92b403ebcd7`), désignée par le propriétaire | **Autorisé par le propriétaire le 13 novembre 2026** dans la conversation. Le fichier indique « PRÉPARÉ POUR EXÉCUTION SUR AUTORISATION DU PROPRIÉTAIRE », conservé tel quel. | `5dff21c4e0040d81ea2bb14a7142ffcc87a077d287de967978349dc130d7f6e9` |
 | `BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` — consolidation des arbitrages DS1 à DS5 du propriétaire | copie octet pour octet du fichier publié sur la branche `orchestration/mandats` (commit `197d8b953540b178143b7c365335e19ec33e9c40`, inchangé au commit `24ca7569bd3a25cc2b0f3807a0afc92b403ebcd7`), désignée par le propriétaire | Décisions partielles du propriétaire, datées du 13 novembre 2026 par le document ; **non inscrites au registre** ; aucune implémentation autorisée. | `dee88998c561247a5941fe2d04854a95b74e863d31b837b86f3de1acad9f335f` |
 | `BASTION-MANDAT-LOT-2J-INSCRIPTION-DOCUMENTAIRE-v1.0.md` — mandat du lot 2J | original `.md` | **Autorisé par le propriétaire le 15 novembre 2026** dans la conversation. Le fichier indique « mandat préparé pour validation/transmission », conservé tel quel. Exécution : `docs/reviews/LOT-2J-INSCRIPTION-DOCUMENTAIRE.md`. | `460a83f201308b4e1faafa8683ddd5f9fdf9b232042c188730bd010c7c7ebb17` |
+| `BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` — mandat d'inscription documentaire des sous-décisions de MEC-0001 du 17 novembre 2026 (ARB-A à ARB-E, G1 à G4) ; titre du texte : « BASTION — Mandat d'inscription documentaire MEC-0001 — v1.0 » | original `.md` : fichier joint au message du propriétaire du 17 novembre 2026 (voir `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md`), archivé le 18 novembre 2026 sans modification depuis l'archive `BASTION-LOT-ARCHIVAGE-MEC-0001-SOURCES-ET-MANDAT.zip` fournie dans la conversation, empreinte recalculée sur l'original (commit `1ecc608`, PR n° 15 ; voir `docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md`) | **Autorisé par le propriétaire le 17 novembre 2026** (« Je valide ») pour des modifications documentaires locales seulement, sans commit, push, publication ni fusion, et sans gameplay. Le fichier indique « AUTORISÉ POUR MODIFICATIONS DOCUMENTAIRES UNIQUEMENT », conservé tel quel. Exécuté le 17 novembre 2026 : `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md`. Ce rapport documente aussi une autorisation distincte reçue ensuite : un commit et un push sur la seule branche `claude/new-session-mgfohp`, sans PR ni fusion. MEC-0001 restait reportée à l'indexation. Indexé ici par le lot 1I, le 25 novembre 2026. | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` |
 | `BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-transcription.md` — mandat d'implémentation de MEC-0003, lot 1 (marche sur terrain plat) | **transcription depuis la conversation** : message du propriétaire du 21 novembre 2026 à 21:06:41 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 21 novembre 2026** dans la conversation (21:09:26 UTC), par le choix de l'option « Autoriser, avec installation .NET (Recommandé) » proposée par Claude Code. Le fichier indique encore « mandat préparé, en attente d'autorisation d'exécution du propriétaire », conservé tel quel. Avenant n° 1 : ligne suivante. Exécution : `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md`. | `c8d9a38f4fb91cac07da621dfad7a21e8324553513d940fb228f98dd9b6d5fd8` |
 | `BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-1-transcription.md` — avenant n° 1 au mandat d'implémentation de MEC-0003 : correction de la dernière phrase de T13 et de l'assertion C# correspondante | **transcription depuis la conversation** : message du propriétaire du 21 novembre 2026 à 22:18:31 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 21 novembre 2026** : le message est lui-même l'autorisation. Exécuté : voir `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md`. | `6055e752655178b214df8804a1b8e373578388be7827258607272da2d79e74d3` |
 | `BASTION-MANDAT-IMPLEMENTATION-MEC-0003-v1.0-AVENANT-2-transcription.md` — avenant n° 2 au mandat d'implémentation de MEC-0003 : tests de RL-01, RL-02 et RL-03, complément de T13, archivage | **transcription depuis la conversation** : message du propriétaire du 22 novembre 2026 à 04:51:30 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 22 novembre 2026** : le message est lui-même l'autorisation. Exécuté : voir `docs/reviews/MEC-0003-IMPLEMENTATION-LOT1-2026-11-21.md`. Indexé ici sur autorisation du propriétaire du 22 novembre 2026 (09:43:00 UTC). | `6027eb3215eff97212c8fcfef54cfccc95a1357fe9537c40cd209d59a8e8264f` |
@@ -31,3 +32,4 @@ Les documents de ce dossier sont conservés tels que reçus. Ne pas les modifier
 | `BASTION-MANDAT-LOT-1G-A-INSCRIPTION-MEC-0004-transcription.md` — mandat d'inscription de MEC-0004 (gestion élémentaire des tours) au registre, sans implémentation ; titre du texte : « BASTION — Mandat d'inscription MEC-0004 v1.2 », désigné par le propriétaire « BASTION — LOT-1G-A v1.0 » dans son autorisation | **transcription depuis la conversation** : message du propriétaire du 24 novembre 2026 à 16:42:02 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 24 novembre 2026** dans la conversation (17:10:53 UTC) : travail local sur une branche dédiée, quatre fichiers documentaires, sans commit, push, PR ni fusion. Le texte consolidé de MEC-0004 v1.2 a été transmis par le propriétaire à 17:15:02 UTC, en réponse à une question de Claude Code ; il est reproduit à l'annexe A du rapport. Le fichier indique « PRÉPARÉ — exécution non encore autorisée », conservé tel quel. Exécution : `docs/reviews/LOT-1G-A-INSCRIPTION-MEC-0004.md`. | `89447962c4f6677a90286b109f8ca0c42a59b2dcf0d1f1151ef5df19fe73cb11` |
 | `BASTION-MANDAT-LOT-1G-v1.0-transcription.md` — mandat du lot 1G : implémentation de MEC-0004 (gestion élémentaire des tours et récupération des ressources) | **transcription depuis la conversation** : message du propriétaire du 24 novembre 2026 à 19:42:22 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 24 novembre 2026** dans la conversation (19:44:40 UTC), par le choix de l'option « Autoriser, avec Xvfb (Recommandé) » proposée par Claude Code : exécution locale, avec des captures sous affichage virtuel ; sans commit, push ni PR. Le fichier indique « PRÉPARÉ — exécution non autorisée », conservé tel quel. Exécution : `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`. | `c792934ef12607aee0b6f3097cc616c419389401106bcdfe881d196e8eda11b1` |
 | `BASTION-MANDAT-LOT-1H-v1.0.md` — mandat du lot 1H : clôture documentaire de MEC-0004 (registre, README principal, archivage) | **transcription depuis la conversation** : message du propriétaire du 25 novembre 2026 à 19:47:54 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée. Le nom du fichier, sans suffixe « -transcription », est celui que désigne l'autorisation du propriétaire | **Autorisé par le propriétaire le 25 novembre 2026** dans la conversation (message « BASTION — LOT-1H — Autorisation d'exécution », 19:36:28 UTC, reçu avant le texte du mandat ; autorisation confirmée par le message « BASTION — LOT-1H — Complément sur les essais macOS », 19:48:04 UTC) : exécution locale, sans commit, push, PR ni fusion. Le fichier indique « PRÉPARÉ — exécution soumise à autorisation », conservé tel quel. Exécution : `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`. | `06e268068c9dbceedbe77ca3a57f078c37f62acffcd6d114251c158b5716b998` |
+| `BASTION-MANDAT-LOT-1I-v1.0.md` — mandat du lot 1I : correction des incohérences documentaires RH-02 (notice du client Godot, essais macOS) et RH-08 (index des mandats) | **transcription depuis la conversation** : message du propriétaire du 25 novembre 2026 à 20:55:03 UTC, extrait mécaniquement du journal de session ; identité avec un fichier original non vérifiée | **Autorisé par le propriétaire le 25 novembre 2026** dans la conversation (20:55:38 UTC), par le choix de l'option « Autoriser en local (Recommandé) » proposée par Claude Code : exécution locale sur les quatre fichiers du §5, sans commit, push, PR ni fusion. Le fichier indique « PRÉPARÉ — exécution non encore autorisée », conservé tel quel. Exécution : `docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md`. | `f2976095b9c0a14069e556d55078db4c16d4eba26574a01cd12eb300b2ef3d9f` |
diff --git a/src/Bastion.Client.Godot/README.md b/src/Bastion.Client.Godot/README.md
index bf25b19..5a39104 100644
--- a/src/Bastion.Client.Godot/README.md
+++ b/src/Bastion.Client.Godot/README.md
@@ -93,7 +93,9 @@ Ouvrir le projet dans l'éditeur Godot :
 "$GODOT" --editor --path src/Bastion.Client.Godot
 ```
 
-### macOS (six essais manuels déclarés conformes par le propriétaire ; non reproduits de façon indépendante)
+### macOS (essais manuels déclarés par le propriétaire : six le 23 novembre 2026, sept le 25 novembre 2026 ; non reproduits de façon indépendante)
+
+#### Essais déclarés le 23 novembre 2026, sur le prototype du lot 1D
 
 Le 23 novembre 2026, le propriétaire a déclaré conformes six essais manuels du prototype sous macOS. C'est un retour d'utilisateur, et non une reproduction indépendante : ni la version de macOS, ni les commandes exactes employées ne sont connues ici. Les essais déclarés conformes sont les suivants :
 
@@ -104,7 +106,34 @@ Le 23 novembre 2026, le propriétaire a déclaré conformes six essais manuels d
 5. refus d'une destination inaccessible ;
 6. touche R.
 
-Ces essais portent sur le prototype du lot 1D, avant l'ajout des scénarios 2 et 3 par le lot 1F et du scénario 4 par le lot 1G. Ces trois scénarios et les touches 1 à 4 et T n'ont pas été essayés sous macOS.
+Ces essais portent sur le prototype du lot 1D, avant l'ajout des scénarios 2 et 3 par le lot 1F et du scénario 4 par le lot 1G. Ils ne couvrent ni ces trois scénarios, ni les touches 1 à 4 et T.
+
+#### Essais déclarés le 25 novembre 2026, sur le prototype du lot 1G
+
+Le 25 novembre 2026, après les essais du lot 1G sous macOS, le propriétaire a transmis directement dans la conversation Bastion le compte rendu suivant. Il est reproduit à l'annexe A de `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`.
+
+| Essai | Résultat déclaré |
+|---|---|
+| Charger le scénario 4 | Satisfaisant |
+| Terminer le premier tour | Satisfaisant |
+| Terminer le deuxième tour | Satisfaisant |
+| Déplacer puis terminer le tour | Satisfaisant |
+| Réinitialiser | Satisfaisant |
+| Vérifier les anciens scénarios | Satisfaisant |
+| Vérifier la fenêtre | Satisfaisant |
+
+D'après ce compte rendu, les essais portaient notamment sur :
+- l'état initial du scénario 4 : tour 1, 12 TU, 35 d'énergie ;
+- la première fin de tour : tour 2, 60 TU, 55 d'énergie ;
+- la deuxième fin de tour : tour 3, 60 TU, 75 d'énergie ;
+- la conservation de la position, de l'orientation et du chemin après un déplacement et une fin de tour ;
+- la réinitialisation avec R et 4 ;
+- l'absence d'effet de T dans les scénarios 1 à 3 ;
+- la lisibilité de la fenêtre de 800 × 720 pixels.
+
+Ces sept résultats sont des déclarations du propriétaire, sans reproduction indépendante. Ils sont distincts des six essais du 23 novembre 2026. Le compte rendu n'établit ni la version de macOS, ni le commit essayé, ni les modalités d'affichage, ni les périphériques utilisés.
+
+#### Chemin et commandes
 
 Le chemin et les commandes ci-dessous n'ont pas été vérifiés de façon indépendante sous macOS. Avec l'application officielle `Godot_mono.app` 4.7.2 placée dans `/Applications` :
 
@@ -172,9 +201,12 @@ timeout 300 xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test
 ## Limites
 
 **Essais non effectués pour les lots 1F et 1G**, au moment de leur réalisation :
-- **macOS :** aucun essai des scénarios 2 à 4 ni des touches 1 à 4 et T. Les six essais déclarés par le propriétaire portent sur le prototype du lot 1D. L'essai manuel du scénario 4 sous macOS n'a pas eu lieu.
-- **Écran réel :** aucun essai, sous aucun système (Linux, macOS ou Windows). Le rendu n'est connu que par des captures automatiques sous affichage virtuel (Xvfb).
-- **Clavier et souris physiques :** aucun essai. Les entrées sont simulées par le contrôle fumée et, lors de la relecture, par des événements X11 sous Xvfb.
+- **macOS :** à la réalisation des lots, aucun essai des scénarios 2 à 4 ni des touches 1 à 4 et T ; les six essais déclarés par le propriétaire le 23 novembre 2026 portent sur le prototype du lot 1D. Depuis, le 25 novembre 2026, le propriétaire a déclaré satisfaisants sept essais du prototype du lot 1G sous macOS (section macOS ci-dessus), sans reproduction indépendante.
+- **Écran réel :** aucun essai par Claude Code ni par la CI, sous aucun système (Linux, macOS ou Windows). Trois sources distinctes, à ne pas confondre :
+  - **CI GitHub Actions :** tests automatisés, dont le contrôle fumée en mode headless, sans affichage ni capture d'écran ;
+  - **vérifications locales sous Xvfb :** captures automatiques sous affichage virtuel, qui permettent d'examiner le rendu ;
+  - **macOS :** sept essais manuels déclarés satisfaisants par le propriétaire le 25 novembre 2026, sans reproduction indépendante ni précision sur les modalités matérielles.
+- **Clavier et souris physiques :** aucun essai par Claude Code ni par la CI. Les entrées sont simulées par le contrôle fumée et, lors de la relecture, par des événements X11 sous Xvfb. Les essais manuels déclarés par le propriétaire sous macOS ne précisent pas les périphériques utilisés.
 
 **Ce qui est vérifié, et ses limites :**
 
@@ -185,16 +217,16 @@ timeout 300 xvfb-run -a "$GODOT" --path src/Bastion.Client.Godot -- --smoke-test
 - **Scénarios 2 et 3 (lot 1F) :**
   - vérifiés en local, par le contrôle fumée en mode headless et par des captures sous Xvfb ;
   - pas encore dans la CI au moment du lot 1F ;
-  - aucune validation manuelle, sur aucun système.
+  - validation manuelle : aucune au moment du lot 1F. Le 25 novembre 2026, l'essai « Vérifier les anciens scénarios » du propriétaire sous macOS est déclaré satisfaisant, sans reproduction indépendante ; le compte rendu cite l'absence d'effet de la touche T dans les scénarios 1 à 3, sans détailler les autres points vérifiés. Aucune sur un autre système.
 - **Scénario 4 (lot 1G) :**
   - vérifié en local, par le contrôle fumée en mode headless et par des captures sous Xvfb ;
   - pas encore dans la CI au moment du lot 1G ;
-  - aucune validation manuelle, sur aucun système.
+  - validation manuelle : cinq des sept essais déclarés satisfaisants par le propriétaire sous macOS le 25 novembre 2026 portent sur ce scénario (chargement, deux fins de tour, déplacement puis fin de tour, réinitialisation ; section macOS), sans reproduction indépendante. Aucune sur un autre système.
 - **Touches 1 à 4 et T :**
   - vérifiées par des événements simulés : la touche 2 par son seul libellé ; les touches 3, 1 et 4 comme un clavier AZERTY les transmet (libellé « " », « & » ou « ' », position de la touche) ;
   - aussi par de vrais événements X11 sous Xvfb, avec une disposition AZERTY imitée : les touches 1 à 3 et R lors de la relecture du lot 1F, les touches 4, T, R et 1 lors de celle du lot 1G (résultat inspecté sur des captures) ;
-  - jamais avec un clavier physique.
-- **macOS :** six essais manuels déclarés conformes par le propriétaire le 23 novembre 2026, sur le prototype du lot 1D. C'est un retour d'utilisateur, non reproduit de façon indépendante. Le contrôle fumée en ligne de commande et `gtimeout` n'y sont pas vérifiés.
+  - jamais avec un clavier physique par Claude Code ni par la CI. Les essais déclarés par le propriétaire sous macOS le 25 novembre 2026 citent les touches R, 4 et T, sans préciser le clavier ni sa disposition.
+- **macOS :** six essais manuels déclarés conformes par le propriétaire le 23 novembre 2026, sur le prototype du lot 1D, et sept essais déclarés satisfaisants le 25 novembre 2026, sur le prototype du lot 1G (scénario 4, anciens scénarios et fenêtre). Ce sont des retours d'utilisateur, non reproduits de façon indépendante ; le compte rendu du 25 novembre n'établit ni le commit essayé, ni les modalités d'affichage, ni les périphériques. Le contrôle fumée en ligne de commande et `gtimeout` n'y sont pas vérifiés.
 - **Windows :** aucun essai.
 - **CI :** compilation, format et contrôle fumée en mode headless seulement ; ni affichage, ni export.
 - **Export :** aucun export de jeu n'est testé.
```

## Annexe — Empreintes SHA-256

| Fichier | Sur `origin/main` (`10f4a0a`) | Dans l'arbre de travail du lot |
|---|---|---|
| `src/Bastion.Client.Godot/README.md` | `2181fe00914c8bf84ab8adb86f73cc2f382d40cbee23ede73d437fddc1dcc311` | `623402b0625909cb660a4809ffce954b4b00f36a42be53245a89f24179653fdd` |
| `docs/mandates/README.md` | `15d95fce5d483e41f5eb89e783dc9558123ccc841bb1ed1ce86353cbaab85b22` | `c34e6718d754ccdd243fe311323279dad052006f95b760edb53ac801f404d3fc` |
| `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md` | absent | `f2976095b9c0a14069e556d55078db4c16d4eba26574a01cd12eb300b2ef3d9f` |
| `docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` (inchangé) | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` |

Ce rapport ne peut pas porter sa propre empreinte.

## Addendum — Publication du lot 1I

Cet addendum est ajouté le 27 novembre 2026, à la demande du message « BASTION — LOT-1I — Addendum de publication », pour finaliser la traçabilité de la PR #28. Le reste du rapport n'est pas modifié :
- les relectures indépendantes et leur traitement (§5) ;
- les réserves sur les essais macOS (§6) ;
- le diff (§7) et les empreintes (annexe).

**Portée des mentions historiques.** Elles décrivent l'état du travail local avant la publication, le 25 novembre 2026. Elles étaient exactes à cette date et restent écrites telles quelles. Ce sont :
- « Rien n'est commité ni publié », dans la ligne « État » de l'en-tête ;
- « rien n'est poussé, donc la CI n'a pas tourné sur ce lot », au §6 ;
- « HEAD reste `origin/main` et rien n'est commité », au §6 (demandes du hook `Stop`) ;
- les mentions semblables des relectures reproduites au §5, par exemple « CI : elle n'a pas tourné, puisque rien n'est poussé ».

**Publication**, autorisée par le message « BASTION — LOT-1I — Autorisation de publication » du 25 novembre 2026, sans fusion. Les éléments ci-dessous ont été vérifiés le 27 novembre 2026, vers 13:02 UTC :

| Élément | Constat | Vérification |
|---|---|---|
| Commit publié | `6a0ccea27ed7e0a42953eb10df0e08bccd502bb7`, du 25 novembre 2026, sur la branche `claude/lot-1i-corrections-documentaires` ; son parent est `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5` | `git fetch`, puis `git rev-parse` de la branche locale et de la branche distante, qui sont identiques |
| Contenu du commit | les quatre fichiers autorisés, et eux seuls. Le présent rapport y figure dans sa version antérieure à cet addendum, de SHA-256 `d109c6b37ab1e13299f5ea1247e6e6eeb433d01ecbbc2760ee1c15a718f3dc66` | `git show --name-only 6a0ccea` ; `git show 6a0ccea:docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md` passé à `sha256sum` |
| PR #28 | https://github.com/mengpo1/bastion/pull/28 : ouverte, **en brouillon**, vers `main`, tête `6a0ccea`, sans conflit (`mergeable` vrai, état `clean`) | API GitHub, `pulls/28` |
| CI sur le push | exécution [45708625153](https://github.com/mengpo1/bastion/actions/runs/45708625153), **succès** | API GitHub, `actions/runs/45708625153` ; journal du job, lu le 25 novembre |
| CI sur la PR | exécution [45708667900](https://github.com/mengpo1/bastion/actions/runs/45708667900), **succès** | API GitHub, `actions/runs/45708667900` ; journal du job, lu le 25 novembre |
| Fusion | **aucune** : la PR n'est pas fusionnée (`merged_at` vide), et `origin/main` vaut toujours `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5` | API GitHub ; `git fetch origin main` |

**Résultats lus dans les journaux de la CI, le 25 novembre 2026,** pour chacune des deux exécutions :
- compilations sans avertissement ni erreur, client Godot compris ;
- format conforme ;
- 65 tests .NET réussis sur 65 ;
- 75 tests des hooks, 0 échec ;
- 120 contrôles fumée Godot réussis, « SMOKE : RÉUSSITE ».

Sur l'exécution de la PR, le contrôle de traçabilité indique : « Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise. » Ces deux exécutions sont les seules sur le commit `6a0ccea`.

**Statut de cet addendum à la date de sa rédaction, le 27 novembre 2026 :** une modification locale du seul rapport, ni commitée ni poussée ; sa publication demandait alors une nouvelle autorisation explicite. Une fois publié, l'addendum change la tête de la PR : les exécutions de CI citées ci-dessus portent sur le commit `6a0ccea`, et non sur le commit qui le contient.
