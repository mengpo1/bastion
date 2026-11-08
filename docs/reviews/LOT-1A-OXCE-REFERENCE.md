# LOT-1A — Référence OXCE candidate

**Mandat :** `BASTION-MANDAT-LOT-1A-v1.0.md`, lu sur la branche `orchestration/mandats` au commit `035587c825c53f132c835a07c5852329e46ee409`. Empreinte du fichier : SHA-256 `511a018548c20697abbc9368405891c50a154213bdd291513b5b925fca5002c6`, 5 100 octets. Il n'est pas recopié.
**Autorisation :** propriétaire, dans la conversation, le 8 nov. 2026 (distincte de la fusion de la PR n° 2).
**Branche :** `research/lot-1a-oxce-reference`, partie de `main` = `9e45c5db5daf3b13dd1e42dda8b50bb7f65567ca` (après `git fetch origin main`).
**Nature :** étude documentaire et **proposition** au propriétaire. Rien n'est adopté ; `docs/references/OXCE-BASELINE.md` n'est pas modifié.

## 0. Recommandation

| Élément | Proposition |
|---|---|
| Projet | OpenXcom Extended (OXCE) |
| Dépôt | `MeridianOXC/OpenXcom` — https://github.com/MeridianOXC/OpenXcom |
| Branche | `oxce-plus` (branche par défaut) |
| **Commit** | **`441cae1b071d249d40a223858cb6bd07fd5d791b`** — https://github.com/MeridianOXC/OpenXcom/commit/441cae1b071d249d40a223858cb6bd07fd5d791b |
| Version | **OXCE 8.7.1** (`OPENXCOM_VERSION_SHORT "Extended 8.7.1"`, `OPENXCOM_VERSION_LONG "8.7.1.0"`) |
| Date | 2026-09-19 11:57:20 +0200, auteur et committeur Meridian, message « OXCE 8.7.1 » |
| Étiquette Git | **aucune** : la référence repose sur le SHA |
| Portée proposée | Moteur OXCE seul, avec son jeu de règles de base. **Aucun mod**, y compris les mods « standard » livrés avec le moteur. Le choix entre UFO (`xcom1`) et Terror From the Deep (`xcom2`) est une décision distincte (D2). |

**Pourquoi ce commit ?**
- C'est le commit qui fixe la version 8.7.1, la plus récente publiée.
- Les binaires officiels de cette version portent son hash dans leur nom (`Extended-8.7.1-441cae1b0-2026-09-19-…`).
- La tête actuelle de `oxce-plus` (`f0134ef…`, 29 sept. 2026) contient exactement le même moteur : seul un fichier de CI diffère.

**Limites :**
- pas d'étiquette Git ;
- pas de garantie que les binaires officiels soient reproductibles à l'identique depuis les sources ;
- aucune règle de jeu n'est vérifiée par cette étude.

## 1. Méthode et légende

- **vérifié** : constaté par une commande exécutée dans cette session (sortie relevée) ou par lecture d'une page source ;
- **inférence** : déduit de faits vérifiés, sans constat direct ;
- **non vérifié** : non constaté ici.

**Contraintes d'accès du bac à sable :**
- les pages web et l'API de GitHub répondent 403 (proxy). Les faits GitHub sont donc vérifiés par le **protocole Git** (`git ls-remote`, clone anonyme en lecture du dépôt public). Les liens `github.com/…` du rapport sont construits à partir des SHA vérifiés : leur affichage n'est pas vérifié ici ;
- `openxcom.org` est accessible en HTTPS.

Le dépôt OXCE a été cloné en lecture seule (`--depth 400`, branche `oxce-plus`) hors du dépôt Bastion. Il n'a été ni compilé ni exécuté.

## 2. Dépôts : officiel, forks, binaires, mods

| Source | Rôle | Statut | Preuve |
|---|---|---|---|
| `MeridianOXC/OpenXcom`, branche `oxce-plus` | **Dépôt officiel d'OXCE** | vérifié | `git ls-remote --symref` : `HEAD` → `refs/heads/oxce-plus`. Fil officiel du forum (Meridian, sept. 2018, modifié en nov. 2020) : « the main common GitHub repository is: https://github.com/MeridianOXC/OpenXcom/ — Yankes' repo is effectively frozen » — https://openxcom.org/forum/index.php/topic,6586.0.html |
| `MeridianOXC/OpenXcom`, branche `master` | Copie du dépôt d'origine, pas OXCE | vérifié | même SHA que `OpenXcom/OpenXcom` `master` : `4a4bae5fa2e5a09282928e84943fc84b093e34ff` |
| `OpenXcom/OpenXcom` (= `SupSuper/OpenXcom`) | **OpenXcom d'origine (« vanilla »)**, pas OXCE | vérifié | `master` identique dans les deux (`4a4bae5…`) ; lien `OpenXcom/OpenXcom` donné par le fil officiel et par le README |
| `Yankes/OpenXcom` | Origine historique d'OXCE, gelée | vérifié (forum) | message de Meridian cité ci-dessus ; branche `OpenXcomExtended` présente |
| `MeridianOXC/openxcom-android`, `MeridianOXC/openxcom-ios` | Portages mobiles | vérifié (liens) | liens du fil de téléchargement officiel ; non examinés |
| Binaires précompilés | Distribution officielle | vérifié | https://openxcom.org/oxce/release/ et https://openxcom.org/oxce/installer/ ; fil « OXCE v8.7.1 download & installation guide » — https://openxcom.org/forum/index.php/topic,5258.0.html |
| Paquets tiers (AUR, ALT Linux…) | Non officiels | inférence | la recherche web cite AUR `openxcom-extended` 8.6.1 ; non examinés |
| Mods (mod.io, forum) | Contenus séparés du moteur | vérifié (lien) | `https://openxcom.mod.io/` cité dans le README ; **aucun mod retenu** |

Source secondaire de contexte : GamingOnLinux, 16 janv. 2026, « OpenXcom Extended takes over from OpenXcom for the classic X-COM / UFO: Enemy Unknown » — https://www.gamingonlinux.com/2026/01/openxcom-extended-takes-over-from-openxcom-for-the-classic-x-com-ufo-enemy-unknown/page=1

## 3. Commit candidat

| Fait | Valeur | Statut | Source |
|---|---|---|---|
| SHA complet | `441cae1b071d249d40a223858cb6bd07fd5d791b` | vérifié | clone depuis `https://github.com/MeridianOXC/openxcom` ; `git rev-parse` |
| Message, auteur, date | « OXCE 8.7.1 », Meridian, 2026-09-19 11:57:20 +0200 | vérifié | `git log -1` |
| Parent | `6ef16e182f1bb80bce55d456f2cdd7558df59fe3` | vérifié | `git log -1 --format=%P` |
| Contenu du commit | `src/version.h` (8 lignes) et `install/win/installer.nsi` (2 lignes) : changement de version | vérifié | `git show --stat` |
| Version déclarée | `"Extended 8.7.1"`, `"8.7.1.0"`, `8,7,1,0`, `OPENXCOM_VERSION_GIT " (v2026-09-19)"`, `MIN_REQUIRED_RULESET_VERSION_NUMBER 8,7,0,0` | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/src/version.h |
| Installeur | `GAME_VERSION "8.7.1"` ; fichier produit `openxcom_extended_v8.7.1-win64.exe` | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/install/win/installer.nsi |
| Appartient à `oxce-plus` | oui, ancêtre de la tête `f0134ef8065799c7723953d64b565f7832bfd782` | vérifié | `git merge-base --is-ancestor` |
| Tête de `oxce-plus` | `f0134ef…`, 2026-09-29, fusion de `SupSuper/master` ; diff avec le candidat : **seul `.github/workflows/nightly.test`** (4 insertions, 5 suppressions) | vérifié | `git diff --stat 441cae1 f0134ef` |
| Étiquettes Git | seulement `v0.1` à `v1.0`, héritées d'OpenXcom ; aucune pour OXCE | vérifié | `git ls-remote --tags` |
| Historique des versions | commits « OXCE 8.7.1 » (19 sept.), « OXCE v8.7 » (6 sept.), « OXCE 8.6.6 » (21 août)… | vérifié | `git log -G'OPENXCOM_VERSION_…' -- src/version.h` |
| Annonce officielle | fil « OXCE v8.7.1 download & installation guide », dernière modification le 26 sept. 2026 par Meridian. Il précise : « the only officially supported builds are: Windows 64-bit installer and Windows 64-bit zip » | vérifié | https://openxcom.org/forum/index.php/topic,5258.0.html |
| Binaires officiels liés au commit | `Extended-8.7.1-441cae1b0-2026-09-19-win64.7z` (HTTP 200, 7 140 431 octets, Last-Modified 19 sept. 2026 10:37:22 GMT) ; `…-bionic-x86_64.7z` (HTTP 200, 23 sept.) ; aussi `-win32.7z`, `-macos.dmg`. Le hash `441cae1b0` dans le nom désigne ce commit. | vérifié (en-têtes HTTP, sans téléchargement) | https://openxcom.org/oxce/release/Extended-8.7.1-441cae1b0-2026-09-19-win64.7z |
| Binaires reconstruits exactement depuis ce commit | — | **non vérifié** (aucune compilation ; reproductibilité non annoncée) | — |

**Alternatives écartées :**
- **`f0134ef…` (tête de `oxce-plus`)** : moteur identique, mais ce n'est pas le point de version que désignent les binaires officiels.
- **Versions 8.6.x (paquets tiers)** : plus anciennes, aucune raison de les préférer.
- **Builds « nightly » (`oxce_git_2026_09_19_1313_*`)** : même date, mais leur nom ne porte pas le hash, donc moins traçables.
- **OpenXcom d'origine (`4a4bae5…`)** : ce n'est pas OXCE, hors mandat.

## 4. Portée

| Élément | Constat | Statut |
|---|---|---|
| Moteur | Code C++ du dépôt au commit candidat | vérifié |
| Jeux de règles de base | `bin/standard/xcom1` (UFO: Enemy Unknown / X-COM: UFO Defense) et `bin/standard/xcom2` (Terror From the Deep) | vérifié |
| Mods « standard » livrés avec le moteur | environ 45 dossiers optionnels dans `bin/standard/` (XcomUtil, UFOextender, `TFTD_Damage`, `PSX_Static_Cydonia_Map`…) | vérifié (présence) ; désactivés par défaut = **inférence** (le README les décrit comme « standard mods ») |
| Options du moteur | `src/Engine/Options.inc.h` déclare 118 options, dont 88 préfixées `oxce` ; certaines peuvent modifier le jeu | vérifié (décompte) ; effet sur le jeu = inférence |
| Données du jeu d'origine | **non incluses** : `bin/UFO` et `bin/TFTD` ne contiennent qu'un `README.txt`. Le README exige « a vanilla copy of the X-COM resources » | vérifié |
| Mods externes | aucun | — |

**Proposition :** moteur OXCE 8.7.1 seul, jeu de règles de base, **aucun** mod standard ni externe, options par défaut. Trois décisions restent distinctes : le jeu de base (D2), les options (D3), et tout mod éventuel (D6).

## 5. Licences au commit candidat (pas un avis juridique)

| Élément | Licence | Statut | Lien |
|---|---|---|---|
| Moteur (`LICENSE.txt`) | GNU GPL **version 3** (texte complet ; SHA-256 du fichier `c53a65c2fd561c87eaabf1072ef5dcab8653042bc15308465f52413585eb6271`) | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/LICENSE.txt |
| En-têtes des sources | « GPL version 3 … or (at your option) any later version » | vérifié (exemple : `src/main.cpp`) | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/src/main.cpp |
| Paquet Debian (`install/debian/copyright`) | `GPL-3.0+`, copyright 2009 Daniel Filipe « SupSuper » et autres | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/install/debian/copyright |
| `libs/miniz` | permissive de type MIT (avec mention « All Rights Reserved ») | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/libs/miniz/LICENSE |
| `libs/rapidyaml` | MIT | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/libs/rapidyaml/LICENSE.txt |
| Ressources `Resources/Extended/Touch` et `Resources/Weapons` (`xcom1` et `xcom2`) | **CC BY-SA 4.0** (Riccardo Gasperi ; Niklas Jansson) | vérifié | https://github.com/MeridianOXC/OpenXcom/blob/441cae1b071d249d40a223858cb6bd07fd5d791b/bin/standard/xcom1/Resources/Weapons/license.txt |
| Code tiers dans `src/` | 32 fichiers sur 809 sans l'en-tête OpenXcom : `Engine/Adlib/fmopl` (LGPL), `Engine/OpenGL` (domaine public), `Engine/Scalers/xbrz` (GPL-3.0), autres sans licence identifiée en tête | vérifié (liste) ; licences individuelles **non auditées** | — |
| Autres ressources de `bin/` (jeux de règles YAML, langues, images) | pas de fichier de licence propre : couvertes par la licence du dépôt = **inférence** | inférence | — |
| Données d'origine de X-COM | **propriétaires**, non incluses, non redistribuables par Bastion | vérifié (absence) ; statut juridique = inférence | — |

**Questions de redistribution, à soumettre à un audit (CLAUDE.md §4) :**
- reprendre ou adapter du **code** OXCE dans Bastion entraînerait les obligations de la GPL-3.0-or-later pour Bastion distribué ;
- reprendre le **contenu** des jeux de règles (fichiers YAML du dépôt) soulève la même question ; la frontière entre données factuelles et expression protégée reste à apprécier ;
- les ressources **CC BY-SA 4.0** imposent attribution et partage aux mêmes conditions ;
- les **données d'origine de X-COM** ne doivent pas servir d'assets à Bastion (règle déjà en vigueur) ;
- **réimplémenter** un comportement observé, sans copier de code, est une question distincte, à trancher par l'audit. Aucune conclusion n'est tirée ici.

## 6. Ce qui sera vérifiable ensuite, et ce qui reste inconnu

**Vérifiable à partir de cette référence :**
- **Code source** au commit candidat (C++), lisible et consultable par SHA.
- **Jeux de règles de base** (`bin/standard/xcom1` ou `xcom2`) : valeurs des données de jeu.
- **Annonces et changelog** du fil officiel.
- **Comportements observables**, en exécutant les binaires officiels 8.7.1 avec une copie légitime du jeu d'origine. Cela demande la copie du propriétaire et, en pratique, Windows 64 bits, seule plateforme officiellement prise en charge.
- Documentation communautaire (UFOpaedia) : existence **non vérifiée** ici (une page testée répond 404).

**Inconnu à ce stade :**
- la reproductibilité exacte des binaires officiels depuis les sources ;
- l'effet de chacune des 88 options OXCE ;
- le hasard du moteur (graine, déterminisme), qui conditionne des tests de comparaison reproductibles ;
- les versions des dépendances embarquées dans les binaires officiels.

**Rien dans Bastion n'est « conforme à OXCE »** : toute affirmation de fidélité exigera une référence figée et des tests de comportement dédiés (CLAUDE.md §3).

## 7. Vérifications exécutées

| Commande ou action | Résultat |
|---|---|
| `git fetch origin main` ; `git rev-parse main origin/main` | `9e45c5d…` des deux côtés |
| Lecture du mandat : `git show 035587c:docs/mandates/BASTION-MANDAT-LOT-1A-v1.0.md` | SHA-256 `511a0185…02c6`, 5 100 octets |
| `git ls-remote --symref https://github.com/MeridianOXC/OpenXcom HEAD` | `HEAD` → `refs/heads/oxce-plus` → `f0134ef…` |
| `git ls-remote --heads / --tags` sur `MeridianOXC`, `SupSuper`, `OpenXcom`, `Yankes` | 6 branches chez MeridianOXC ; 7 étiquettes héritées ; `master` identiques (`4a4bae5…`) |
| `git clone --depth 400 --branch oxce-plus https://github.com/MeridianOXC/openxcom` | tête `f0134ef…` ; 954 commits disponibles |
| `git log -G'OPENXCOM_VERSION_…' -- src/version.h` | commits de version, dont « OXCE 8.7.1 » = `441cae1…` |
| `git show 441cae1:src/version.h`, `install/win/installer.nsi`, fichiers de licence | valeurs citées en sections 3 et 5 |
| `git diff --stat 441cae1 f0134ef` | 1 fichier : `.github/workflows/nightly.test` |
| `curl` du fil 6586 (forum OXCE) et du fil 5258 (téléchargement) | dépôt officiel confirmé ; « OXCE v8.7.1 download & installation guide » ; noms des binaires avec `441cae1b0` |
| `curl -I` sur deux binaires et sur l'installeur | HTTP 200 (taille et date relevées) |
| Recherche web et `curl` de l'article GamingOnLinux | contexte de janvier 2026 |

Non pertinents pour cette étude documentaire et non exécutés : compilation et tests C#, compilation ou exécution d'OXCE. La CI de la PR est relevée après publication.

## 8. Revue indépendante

_À compléter._

## 9. Questions à arbitrer par le propriétaire

| # | Question |
|---|---|
| D1 | Valider OXCE 8.7.1 au commit `441cae1b071d249d40a223858cb6bd07fd5d791b` comme référence de Bastion, ou en demander une autre. |
| D2 | Jeu de base de référence : UFO: Enemy Unknown (`xcom1`), Terror From the Deep (`xcom2`), ou les deux. |
| D3 | Options OXCE : retenir les valeurs par défaut de la 8.7.1 comme référence ? |
| D4 | Politique de licence : Bastion s'interdit-il toute reprise de code ou de données d'OXCE (réimplémentation seulement), ou accepte-t-il la GPL ? Un audit est requis avant toute reprise. |
| D5 | Inscription de la référence validée dans `docs/references/OXCE-BASELINE.md`, par mandat distinct. |
| D6 | Mods : aucun pour l'instant ; tout mod, standard ou externe, fera l'objet d'une décision distincte. |

## 10. Contrôle du diff

Un seul fichier ajouté : ce rapport. Aucun registre, aucune règle, aucun harnais, aucun projet C# ni test modifié. Aucun code OXCE copié, aucun asset X-COM.

## 11. Déclaration

**Aucun gameplay implémenté. Aucune fiche `MEC`. Aucune modification des registres de décisions. Aucune fusion dans `main`.**

Arrêt après publication : en attente de la décision du propriétaire sur la référence.
