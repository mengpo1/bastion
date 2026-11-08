# LOT-1A — Référence OXCE candidate

**Mandat :** `BASTION-MANDAT-LOT-1A-v1.0.md`, lu sur la branche `orchestration/mandats` au commit `035587c825c53f132c835a07c5852329e46ee409`, par le protocole Git (`git show`). Empreinte du fichier : SHA-256 `511a018548c20697abbc9368405891c50a154213bdd291513b5b925fca5002c6`, 5 100 octets. Il n'est pas recopié.
**Autorisation :** propriétaire, dans la conversation, le 8 nov. 2026 (distincte de la fusion de la PR n° 2).
**Branche :** `research/lot-1a-oxce-reference`, partie de `main` = `9e45c5db5daf3b13dd1e42dda8b50bb7f65567ca` (après `git fetch origin main`).
**Nature :** étude documentaire et **proposition** au propriétaire. Rien n'est adopté ; `docs/references/OXCE-BASELINE.md` n'est pas modifié.

## 0. Recommandation

| Élément | Proposition |
|---|---|
| Projet | OpenXcom Extended (OXCE) |
| Dépôt | `MeridianOXC/OpenXcom` — https://github.com/MeridianOXC/OpenXcom |
| Branche | `oxce-plus` (branche par défaut) — https://github.com/MeridianOXC/OpenXcom/tree/oxce-plus |
| **Commit** | **`441cae1b071d249d40a223858cb6bd07fd5d791b`** — https://github.com/MeridianOXC/OpenXcom/commit/441cae1b071d249d40a223858cb6bd07fd5d791b |
| Version | **OXCE 8.7.1** (`OPENXCOM_VERSION_SHORT "Extended 8.7.1"`, `OPENXCOM_VERSION_LONG "8.7.1.0"`) |
| Date | 2026-09-19 11:57:20 +0200, auteur et committeur Meridian, message « OXCE 8.7.1 » |
| Étiquette Git | **aucune** : la référence repose sur le SHA |
| Portée proposée | Moteur OXCE seul, avec un jeu de règles de base. **Aucun mod**, y compris les mods « standard » livrés avec le moteur (inactifs par défaut). Options du moteur à leurs valeurs par défaut. Le choix entre UFO (`xcom1`, actif par défaut) et Terror From the Deep (`xcom2`) est une décision distincte (D2). |

**Pourquoi ce commit ?**
- C'est le commit qui fixe la version 8.7.1, la plus récente publiée. Aucune version plus récente n'apparaît dans `openxcom.org/oxce/release/` ni dans `/oxce/installer/`.
- Les binaires Windows 64 bits de cette version, **seuls officiellement pris en charge**, portent `441cae1b0` dans leur nom. Le système de construction y insère le hash du commit (`git describe`). Rattacher ces binaires au commit est une **inférence solide**, non vérifiée par recompilation.
- La tête actuelle de `oxce-plus` (`f0134ef…`, 29 sept. 2026) contient le même moteur : seul un fichier de CI diffère.

**Limites :**
- pas d'étiquette Git ;
- reproductibilité des binaires non vérifiée ;
- environ 290 fichiers aux formats X-COM présents dans le dépôt, à exclure de toute reprise (section 4) ;
- aucune règle de jeu vérifiée par cette étude.

## 1. Méthode et légende

- **vérifié** : constaté par une commande exécutée dans cette session (sortie relevée) ou par lecture d'une page source ;
- **inférence** : déduit de faits vérifiés, sans constat direct ;
- **non vérifié** : non constaté ici.

**Contraintes d'accès du bac à sable :**
- les pages web et l'API de GitHub répondent 403 (proxy). Les faits GitHub sont donc vérifiés par le **protocole Git** (`git ls-remote`, clone anonyme en lecture du dépôt public). Les liens `github.com/…` du rapport sont construits à partir des SHA vérifiés : leur affichage n'est pas vérifié ici ;
- `openxcom.org` est accessible en HTTPS.

Le dépôt OXCE a été cloné en lecture seule (`--depth 400`, branche `oxce-plus`) hors du dépôt Bastion. Il n'a été ni compilé ni exécuté.

**Rappel (mandat §2) :** le lot 0D est accepté avec réserves. Les limites conservées des lots 0C et 0C-R1 (contrôles non sémantiques, rapport vide accepté par le hook `Stop`, références Git possiblement périmées) s'appliquent. Elles n'ont pas d'incidence directe sur cette étude documentaire.

_Précision du 8 nov. 2026 (LOT-1B) :_ l'absence de protection technique de `main` relevée lors de la qualification du harnais n'est plus d'actualité.
- L'API GitHub des branches signale `main` comme protégée (`protected: true`). Constaté le 8 nov. 2026 par Claude Code, via l'outil GitHub de la session, hors bac à sable : le proxy bloque l'API GitHub, voir ci-dessus.
- Selon le mandat LOT-1B, GitHub affiche un ruleset actif ciblant `main` et imposant le job `build-test`. Ce détail n'est pas vérifié par Claude Code, faute d'accès à la configuration des rulesets.

## 2. Dépôts : officiel, forks, binaires, mods

| Source | Rôle | Statut | Preuve |
|---|---|---|---|
| `MeridianOXC/OpenXcom`, branche `oxce-plus` | **Dépôt officiel d'OXCE** | vérifié | `git ls-remote --symref` : `HEAD` → `refs/heads/oxce-plus`. Fil de téléchargement officiel (Meridian, modifié le 26 sept. 2026) : « Source code PC/Apple : https://github.com/MeridianOXC/OpenXcom/tree/oxce-plus » — https://openxcom.org/forum/index.php/topic,5258.0.html. Fil principal (Meridian, modifié le 22 nov. 2020) : « the main common GitHub repository is: https://github.com/MeridianOXC/OpenXcom/ — Yankes' repo is effectively frozen » — https://openxcom.org/forum/index.php/topic,6586.0.html |
| `MeridianOXC/OpenXcom`, branche `test` | Branche de travail : 2 commits de Yankes postérieurs à la 8.7.1, non publiés (`6ee48e7` « Fix freeze when civilian try move pass alien », 26 sept. ; `613ec4a` « Simplify visible enemies code », 28 sept.) | vérifié | `git fetch origin test` ; `git log 441cae1..FETCH_HEAD` |
| `MeridianOXC/OpenXcom`, branche `master` | Copie du dépôt d'origine, pas OXCE | vérifié | même SHA que `OpenXcom/OpenXcom` `master` : `4a4bae5fa2e5a09282928e84943fc84b093e34ff` |
| `OpenXcom/OpenXcom` (= `SupSuper/OpenXcom`) | **OpenXcom d'origine (« vanilla »)**, pas OXCE | vérifié | `master` identique dans les deux (`4a4bae5…`) ; lien `OpenXcom/OpenXcom` donné par le fil 6586 et par le README |
| `Yankes/OpenXcom` | Origine historique d'OXCE, gelée | vérifié (forum) | fil 6586 ; branche `OpenXcomExtended` présente (2018) |
| `MeridianOXC/openxcom-android`, `MeridianOXC/openxcom-ios` | Portages mobiles, non officiels | vérifié (liens) | fil 5258 ; non examinés |
| Binaires précompilés | Seuls officiellement pris en charge : **installeur et zip Windows 64 bits**. « All other builds and ports are unofficial, provided as-is » | vérifié | fil 5258 ; https://openxcom.org/oxce/release/ ; https://openxcom.org/oxce/installer/ |
| Paquets tiers | Non officiels (AUR `openxcom-extended` 8.6.1 selon la recherche web) | inférence | https://aur.archlinux.org/packages/openxcom-extended/ (non consulté directement) |
| Mods externes (mod.io, forum) | Contenus séparés du moteur | vérifié (lien) | `https://openxcom.mod.io/`, cité dans le README ; **aucun mod retenu** |

Source secondaire de contexte : GamingOnLinux, 16 janv. 2026, « OpenXcom Extended takes over from OpenXcom for the classic X-COM / UFO: Enemy Unknown » — https://www.gamingonlinux.com/2026/01/openxcom-extended-takes-over-from-openxcom-for-the-classic-x-com-ufo-enemy-unknown/page=1

## 3. Commit candidat

| Fait | Valeur | Statut | Source |
|---|---|---|---|
| SHA complet | `441cae1b071d249d40a223858cb6bd07fd5d791b` | vérifié (récupéré depuis GitHub par le protocole Git ; revérifié par la revue dans un dossier neuf) | `git rev-parse` |
| Message, auteur, date | « OXCE 8.7.1 », Meridian, 2026-09-19 11:57:20 +0200 | vérifié | `git log -1` |
| Parent | `6ef16e182f1bb80bce55d456f2cdd7558df59fe3` | vérifié | `git log -1 --format=%P` |
| Contenu du commit | `src/version.h` (8 lignes) et `install/win/installer.nsi` (2 lignes) : changement de version | vérifié | `git show --stat` |
| Version déclarée | `"Extended 8.7.1"`, `"8.7.1.0"`, `8,7,1,0`, `OPENXCOM_VERSION_GIT " (v2026-09-19)"`, `MIN_REQUIRED_RULESET_VERSION_NUMBER 8,7,0,0` | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/src/version.h |
| Installeur | `GAME_VERSION "8.7.1"` ; fichier produit `openxcom_extended_v8.7.1-win64.exe` (sans hash dans le nom) | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/install/win/installer.nsi |
| Appartient à `oxce-plus` | oui, ancêtre de la tête `f0134ef8065799c7723953d64b565f7832bfd782` | vérifié | `git merge-base --is-ancestor` |
| Tête de `oxce-plus` | `f0134ef…`, 2026-09-29, fusion de `SupSuper/master`. Diff avec le candidat : **seul `.github/workflows/nightly.test`** (4 insertions, 5 suppressions) | vérifié | `git diff --stat 441cae1 f0134ef` ; https://github.com/MeridianOXC/OpenXcom/compare/441cae1b071d249d40a223858cb6bd07fd5d791b...f0134ef8065799c7723953d64b565f7832bfd782 |
| Étiquettes Git | seulement `v0.1` à `v1.0`, héritées d'OpenXcom ; aucune pour OXCE | vérifié | `git ls-remote --tags` |
| Historique des versions | commits « OXCE 8.7.1 » (19 sept.), « OXCE v8.7 » `a62371b` (6 sept.), « OXCE 8.6.6 » (21 août)… | vérifié | `git log -G'OPENXCOM_VERSION_…' -- src/version.h` |
| Annonce officielle | fil « OXCE v8.7.1 download & installation guide », dernière modification le 26 sept. 2026 par Meridian | vérifié | https://openxcom.org/forum/index.php/topic,5258.0.html |
| Binaire officiel Windows 64 bits | `Extended-8.7.1-441cae1b0-2026-09-19-win64.7z` : HTTP 200, 7 140 431 octets, Last-Modified 19 sept. 2026 10:37:22 GMT ; installeur `openxcom_extended_v8.7.1-win64.exe` : HTTP 200 | vérifié (en-têtes HTTP, sans téléchargement) | https://openxcom.org/oxce/release/Extended-8.7.1-441cae1b0-2026-09-19-win64.7z |
| Rattachement du binaire au commit | **inférence solide**, pour trois raisons : `CMakeLists.txt` (l. 133-142) tire le hash de `git describe` ; la version précédente suit le même schéma (`Extended-8.7.0-a62371bbd-2026-09-06-win64.7z` ↔ commit `a62371b` « OXCE v8.7 ») ; `441cae1b0` ne désigne qu'un objet dans le clone partiel | inférence | — |
| Binaires reconstruits exactement depuis ce commit | — | **non vérifié** (aucune compilation ; reproductibilité non annoncée) | — |

**Alternatives écartées :**
- **`f0134ef…` (tête de `oxce-plus`)** : moteur identique, mais ce n'est pas le point de version que désignent les binaires.
- **Branche `test`** : contient des corrections postérieures à la 8.7.1, non publiées ni annoncées.
- **Versions 8.6.x (paquets tiers)** : plus anciennes, non officielles.
- **Builds « nightly » (`oxce_git_2026_09_19_1313_*`)** : non officiels, et leur nom ne porte pas le hash.
- **Autres binaires 8.7.1 (`win32`, `macos`, `bionic`)** : non officiels selon le fil 5258.
- **OpenXcom d'origine (`4a4bae5…`)** : ce n'est pas OXCE, hors mandat.

## 4. Portée

| Élément | Constat | Statut |
|---|---|---|
| Moteur | Code C++ du dépôt au commit candidat | vérifié |
| Jeux de règles de base | `bin/standard/xcom1` (UFO: Enemy Unknown / X-COM: UFO Defense), **actif par défaut** ; `bin/standard/xcom2` (Terror From the Deep), actif seulement si les données UFO sont absentes | vérifié (`src/Engine/Options.cpp`, l. 619 et 624) |
| Mods « standard » livrés avec le moteur | environ 45 dossiers optionnels dans `bin/standard/` (XcomUtil, UFOextender, `TFTD_Damage`, `PSX_Static_Cydonia_Map`…), **inactifs par défaut** | vérifié (`Options.cpp`, « not active by default ») |
| Options du moteur | `src/Engine/Options.inc.h` : **118 déclarations `OPT`, soit 362 options**, dont 88 préfixées `oxce`. Des options non `oxce` changent aussi le jeu (`aggressiveRetaliation`, `storageLimitsEnforced`, `canSellLiveAliens`…) | vérifié (décompte et présence) ; effet de chaque option = non vérifié |
| Données complètes du jeu d'origine | **non incluses** : `bin/UFO` et `bin/TFTD` ne contiennent qu'un `README.txt`. Le README exige « a vanilla copy of the X-COM resources » | vérifié |
| Fichiers aux formats X-COM inclus | **292 fichiers dans `bin/standard`** : 184 `.MAP`, 86 `.RMP`, 15 `.MCD`, 3 `.PCK`, 3 `.TAB`, 1 `.SCR`. Sans doute des fichiers d'origine corrigés ou dérivés. **À exclure de toute reprise** (CLAUDE.md §4) ; statut à auditer | vérifié (décompte) ; provenance = inférence |
| Mods externes | aucun | — |

**Proposition :** moteur OXCE 8.7.1 seul, un jeu de règles de base, **aucun** mod standard ni externe, **toutes** les options à leurs valeurs par défaut. Trois décisions restent distinctes : le jeu de base (D2), les options (D3), et tout mod éventuel (D6).

## 5. Licences au commit candidat (pas un avis juridique)

| Élément | Licence | Statut | Lien |
|---|---|---|---|
| Moteur (`LICENSE.txt`) | GNU GPL **version 3** (texte complet ; SHA-256 du fichier `c53a65c2fd561c87eaabf1072ef5dcab8653042bc15308465f52413585eb6271`) | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/LICENSE.txt |
| En-têtes des sources OpenXcom | « GPL version 3 … or (at your option) any later version » | vérifié (exemple : `src/main.cpp`) | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/src/main.cpp |
| Paquet Debian (`install/debian/copyright`) | `GPL-3.0+`, copyright 2009 Daniel Filipe « SupSuper » et autres | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/install/debian/copyright |
| `libs/miniz` | permissive de type MIT (avec mention « All Rights Reserved ») | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/libs/miniz/LICENSE |
| `libs/rapidyaml` | MIT | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/libs/rapidyaml/LICENSE.txt |
| Code tiers dans `src/` | 32 fichiers `.cpp`/`.h`/`.hpp`/`.c` sur 809 sans l'en-tête OpenXcom. Notamment : `Engine/Adlib/fmopl` (LGPL) ; `Engine/OpenGL` (domaine public) ; `Engine/Scalers/hqx` (LGPL 2.1 ou ultérieure) ; `scale2x` (GPL 2 ou ultérieure) ; `xbrz` (GPL v3 **sans** « or later », avec une exception pour le projet MAME) ; `lodepng` (zlib) ; `md5` (RSA Data Security) | vérifié (en-têtes) ; audit fichier par fichier non fait | — |
| Code SDL_gfx modifié | « Uses modified code from SDL_gfx (LGPL) with permission from author » (README) | vérifié | README au commit |
| `deps/` | en-têtes SDL (`deps/include/SDL`) et **40 bibliothèques précompilées** `.dll`/`.lib` pour Windows (SDL, SDL_gfx, SDL_image, SDL_mixer, libFLAC, libjpeg, libmikmod…) | vérifié (liste) ; licences de chacune **non auditées** | — |
| Shaders (`bin/common/Shaders`) | licences propres à chaque fichier (GPL 2 ou ultérieure, ou domaine public) : 14 fichiers concernés | vérifié (décompte) | — |
| Ressources `Resources/Extended/Touch` et `Resources/Weapons` (`xcom1` et `xcom2`) | **CC BY-SA 4.0** (Riccardo Gasperi ; Niklas Jansson) | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/bin/standard/xcom1/Resources/Weapons/license.txt |
| Autres ressources de `bin/` (jeux de règles YAML, langues, images) | pas de fichier de licence propre : couvertes par la licence du dépôt = **inférence** | inférence | — |
| Fichiers aux formats X-COM de `bin/standard` (292) | statut inconnu ; possiblement dérivés de données propriétaires | non vérifié | — |
| Données complètes de X-COM | **propriétaires**, non incluses, non redistribuables par Bastion | vérifié (absence) ; statut juridique = inférence | — |

**Questions de redistribution, à soumettre à un audit (CLAUDE.md §4) :**
- reprendre ou adapter du **code** OXCE dans Bastion **pourrait entraîner** les obligations de la GPL (selon les fichiers : GPL-3.0-or-later, GPL-3.0 seule, LGPL, etc.) ;
- reprendre le **contenu** des jeux de règles (fichiers YAML du dépôt) soulève la même question ; la frontière entre données factuelles et expression protégée reste à apprécier ;
- les ressources **CC BY-SA 4.0** imposent attribution et partage aux mêmes conditions ;
- les **fichiers aux formats X-COM** de `bin/standard` et les **données d'origine** ne doivent pas servir d'assets à Bastion ;
- **réimplémenter** un comportement observé, sans copier de code, est une question distincte, à trancher par l'audit. Aucune conclusion n'est tirée ici.

## 6. Ce qui sera vérifiable ensuite, et ce qui reste inconnu

**Vérifiable à partir de cette référence :**
- **Code source** au commit candidat (C++), lisible et consultable par SHA.
- **Jeux de règles de base** (`bin/standard/xcom1` ou `xcom2`) : valeurs des données de jeu.
- **Options** et leurs valeurs par défaut (`Options.inc.h`, `Options.cpp`).
- **Annonces et changelog** du fil officiel.
- **Comportements observables**, en exécutant le binaire officiel Windows 64 bits 8.7.1 avec une copie légitime du jeu d'origine. Cela demande la copie du propriétaire et Windows.
- Documentation communautaire : la page UFOpaedia « OpenXcom » liée par le README répond 200 (contenu non examiné) ; une page « OpenXcom_Extended » testée répond 404.

**Inconnu à ce stade :**
- la reproductibilité exacte des binaires officiels depuis les sources ;
- l'effet de chacune des 362 options ;
- le hasard du moteur (graine, déterminisme), qui conditionne des tests de comparaison reproductibles ;
- les versions et licences des bibliothèques précompilées de `deps/` ;
- la provenance des fichiers aux formats X-COM.

**Rien dans Bastion n'est « conforme à OXCE »** : toute affirmation de fidélité exigera une référence figée et des tests de comportement dédiés (CLAUDE.md §3).

## 7. Vérifications exécutées

| Commande ou action | Résultat |
|---|---|
| `git fetch origin main` ; `git rev-parse main origin/main` | `9e45c5d…` des deux côtés |
| Lecture du mandat : `git show 035587c:docs/mandates/BASTION-MANDAT-LOT-1A-v1.0.md` | SHA-256 `511a0185…02c6`, 5 100 octets |
| `git ls-remote --symref https://github.com/MeridianOXC/OpenXcom HEAD` | `HEAD` → `refs/heads/oxce-plus` → `f0134ef…` |
| `git ls-remote --heads / --tags` sur `MeridianOXC`, `SupSuper`, `OpenXcom`, `Yankes` | 6 branches chez MeridianOXC ; 7 étiquettes héritées ; `master` identiques (`4a4bae5…`) |
| `git clone --depth 400 --branch oxce-plus https://github.com/MeridianOXC/openxcom` ; `git fetch --depth 50 origin test` | tête `f0134ef…` ; 954 commits ; branche `test` : 2 commits après 8.7.1 |
| `git log -G'OPENXCOM_VERSION_…' -- src/version.h` | commits de version, dont « OXCE 8.7.1 » = `441cae1…` |
| `git show 441cae1:…` (`version.h`, `installer.nsi`, `CMakeLists.txt`, `Options.inc.h`, `Options.cpp`, fichiers de licence, en-têtes) | valeurs citées en sections 3 à 5 ; 118 déclarations / 362 options / 88 `oxce` |
| `git diff --stat 441cae1 f0134ef` | 1 fichier : `.github/workflows/nightly.test` |
| `git ls-tree -r 441cae1 bin/standard deps` | 292 fichiers aux formats X-COM ; 40 bibliothèques précompilées |
| `curl` du fil 6586 et du fil 5258 | dépôt officiel ; « Source code PC/Apple » ; builds officiels Windows 64 bits ; noms avec `441cae1b0` |
| `curl` de `openxcom.org/oxce/release/` | 8.7.1 la plus récente ; `Extended-8.7.0-a62371bbd-…` pour la 8.7.0 |
| `curl -I` sur deux binaires et sur l'installeur | HTTP 200 (taille et date relevées) |
| Recherche web et `curl` de l'article GamingOnLinux | contexte de janvier 2026 |

Non pertinents pour cette étude documentaire et non exécutés : compilation et tests C# de Bastion, compilation ou exécution d'OXCE. La CI de la PR documentaire est relevée après publication.

## 8. Revue indépendante

Sous-agent distinct, en lecture seule, sans approuver à la place du propriétaire. Il a revérifié les faits dans un dossier séparé, avec une récupération neuve du commit depuis GitHub, et n'a rien modifié.

| Constat | Traitement |
|---|---|
| « Données d'origine non incluses » trop fort : 292 fichiers aux formats X-COM dans `bin/standard` | **Corrigé** (sections 0, 4, 5, 6) ; exclusion et audit demandés |
| Nombre d'options faux : 118 déclarations, mais 362 options ; des options non `oxce` changent le jeu | **Corrigé** (sections 4 et 6, D3) ; recompté |
| Binaires « officiels » : seul Windows 64 bits l'est ; le rattachement par le hash est une inférence | **Corrigé** : statut « inférence solide » avec ses appuis (`CMakeLists.txt`, nommage de la 8.7.0 vérifié) |
| Licences incomplètes : `deps/`, shaders, SDL_gfx, code tiers mal décrit, `xbrz` sans « or later » | **Corrigé** (section 5) ; tout revérifié |
| Preuve directe absente : « Source code PC/Apple : …/tree/oxce-plus » | **Ajoutée** (section 2), avec les liens `tree` et `compare` |
| Branche `test` non traitée | **Ajoutée** (sections 2 et 3, alternative écartée) |
| Mineurs : mods standard inactifs par défaut, URL AUR, page UFOpaedia, limites du lot 0C, mandat lu par Git | **Intégrés** |

Points vérifiés exacts par la revue :
- `HEAD` → `oxce-plus` → `f0134ef` ;
- les 6 branches et les 7 étiquettes héritées ;
- les citations des fils 6586 et 5258 ;
- les métadonnées et le contenu du commit `441cae1` ;
- le diff limité à `nightly.test` ;
- aucune version plus récente que la 8.7.1 ;
- les en-têtes HTTP ;
- les licences principales, les 45 mods standard, les liens et l'empreinte du mandat ;
- le périmètre du diff (un fichier).

Non vérifiable ici :
- l'affichage des pages GitHub (403) ;
- le contenu et la reproductibilité des binaires ;
- l'unicité du préfixe `441cae1b0` sur tout l'historique (clone partiel) ;
- la provenance des fichiers aux formats X-COM.

## 9. Questions à arbitrer par le propriétaire

| # | Question |
|---|---|
| D1 | Valider OXCE 8.7.1 au commit `441cae1b071d249d40a223858cb6bd07fd5d791b` comme référence de Bastion, ou en demander une autre. |
| D2 | Jeu de base de référence : UFO: Enemy Unknown (`xcom1`, actif par défaut), Terror From the Deep (`xcom2`), ou les deux. |
| D3 | Options : retenir les valeurs par défaut de la 8.7.1 pour **toutes** les options (362), y compris les options non `oxce` qui changent le jeu ? |
| D4 | Politique de licence : Bastion s'interdit-il toute reprise de code ou de données d'OXCE (réimplémentation seulement), ou accepte-t-il les licences correspondantes ? Un audit est requis avant toute reprise. Les fichiers aux formats X-COM restent exclus. |
| D5 | Inscription de la référence validée dans `docs/references/OXCE-BASELINE.md`, par mandat distinct. |
| D6 | Mods : aucun pour l'instant ; tout mod, standard ou externe, fera l'objet d'une décision distincte. |

## 10. Contrôle du diff

Un seul fichier ajouté : ce rapport. Aucun registre, aucune règle, aucun harnais, aucun projet C# ni test modifié. Aucun code OXCE copié, aucun asset X-COM.

## 11. Déclaration

**Aucun gameplay implémenté. Aucune fiche `MEC`. Aucune modification des registres de décisions. Aucune fusion dans `main`.**

Arrêt après publication : en attente de la décision du propriétaire sur la référence.

## Additif du 8 novembre 2026 — décisions du propriétaire (LOT-1B)

Cette étude a été rédigée **avant** la décision du propriétaire : ses sections 0 à 11 restent des propositions et ne sont pas réécrites, hormis la précision datée ajoutée à la section 1 sur la protection de `main`.

Le **8 novembre 2026**, le propriétaire a explicitement décidé, sur les propositions D1 à D6 :
- **D1** : OXCE 8.7.1, commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b` ;
- **D2** : jeu de référence initial UFO: Enemy Unknown (`xcom1`) ; Terror From the Deep (`xcom2`) n'est pas inclus ;
- **D3** : options par défaut de cette version, toute exception étant décidée séparément ;
- **D4** : aucune reprise de code, de données ni d'assets ; réimplémentation indépendante possible après décision et tests ;
- **D5** : inscription dans le registre ;
- **D6** : aucun mod.

Ces décisions sont inscrites dans [`docs/references/OXCE-BASELINE.md`](../references/OXCE-BASELINE.md) par le mandat LOT-1B v1.0. Elles n'autorisent aucun développement de gameplay.
