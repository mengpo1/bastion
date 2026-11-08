# Référence OXCE

Registre protégé. OXCE (OpenXcom Extended) sert de référence de comportement pour Bastion.

**Statut :** référence **validée par le propriétaire le 8 novembre 2026** (décisions D1 à D6 ci-dessous). Elle ne valide aucune mécanique et **n'autorise aucun développement de gameplay**.

| Élément | Valeur |
|---|---|
| Projet | OpenXcom Extended (OXCE) |
| Version | **8.7.1** |
| Dépôt source | `MeridianOXC/OpenXcom` — https://github.com/MeridianOXC/OpenXcom |
| Branche source | `oxce-plus` (indicative : la référence est le commit, pas la branche) |
| **Commit figé** | **`441cae1b071d249d40a223858cb6bd07fd5d791b`** — https://github.com/MeridianOXC/OpenXcom/commit/441cae1b071d249d40a223858cb6bd07fd5d791b |
| Commit | 2026-09-19 11:57:20 +0200, Meridian, « OXCE 8.7.1 » |
| Jeu de référence initial | **UFO: Enemy Unknown**, jeu de règles `xcom1`. Terror From the Deep (`xcom2`) **n'est pas inclus**. |
| Options du moteur | **Valeurs par défaut de cette version précise**, pour toutes les options. Aucune liste n'est recopiée ni figée à la main. |
| Mods | **Aucun**, standard ou externe. |
| Licence | **À auditer avant toute réutilisation** (reprise exclue par D4). `LICENSE.txt` contient la GPL version 3. Les en-têtes des sources OpenXcom ajoutent « or (at your option) any later version ». Du code et des ressources tiers relèvent d'autres licences, dont `xbrz` sous GPL v3 seule : voir l'étude LOT-1A, §5. |
| Politique de réutilisation | Étudier les comportements d'OXCE. **Ne reprendre ni code, ni données, ni assets** d'OXCE ou des jeux X-COM. Politique du projet, pas une conclusion juridique générale. |
| Validation | Décision explicite du propriétaire dans la conversation du **8 novembre 2026**, sur les propositions D1 à D6 faites après la revue du LOT-1A. Inscrite par le mandat LOT-1B v1.0 (branche `orchestration/mandats`, commit `2666625a7c2df1c8ad7de24edc964c0b87ab5ff9`). |
| Étude source | [`docs/reviews/LOT-1A-OXCE-REFERENCE.md`](../reviews/LOT-1A-OXCE-REFERENCE.md) |
| Date de vérification | 8 novembre 2026 |
| Vérifié par | Claude Code (étude LOT-1A, relue par un agent indépendant en lecture seule) ; décisions prises par le propriétaire |

## Décisions du propriétaire du 8 novembre 2026

| # | Décision |
|---|---|
| D1 — Version | OpenXcom Extended (OXCE) **8.7.1**, dépôt `MeridianOXC/OpenXcom`, branche source `oxce-plus`, **commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b`**. Le SHA, et non une branche flottante ni une étiquette supposée, définit la référence. |
| D2 — Jeu de référence initial | **UFO: Enemy Unknown**, jeu de règles `xcom1`. **Terror From the Deep (`xcom2`) n'est pas inclus** dans cette référence initiale. |
| D3 — Options | Valeurs **par défaut de cette version précise** pour toutes les options du moteur, sans recopier ni figer manuellement une liste de 362 options. Toute exception ultérieure doit être décidée séparément. |
| D4 — Politique de réutilisation | Étudier les comportements OXCE ; **ne reprendre ni code, ni données, ni assets** d'OXCE ou des jeux X-COM. Une mécanique peut être **réimplémentée indépendamment** après décision du propriétaire et tests de comportement. Cette politique n'est pas une conclusion juridique générale. |
| D5 — Registre | La référence approuvée est consignée dans ce fichier par le mandat distinct LOT-1B, avec ses sources et ses limites de vérification. |
| D6 — Mods | **Aucun mod**, standard ou externe. Toute éventuelle addition exige un nouvel arbitrage. |

## Sources

- Dépôt officiel d'OXCE : fil principal du forum, https://openxcom.org/forum/index.php/topic,6586.0.html ; fil « OXCE v8.7.1 download & installation guide », https://openxcom.org/forum/index.php/topic,5258.0.html (« Source code PC/Apple : …/tree/oxce-plus »).
- Version au commit figé : `src/version.h` (`"Extended 8.7.1"`, `"8.7.1.0"`) et `install/win/installer.nsi` (`GAME_VERSION "8.7.1"`).
- Binaire officiel Windows 64 bits : `Extended-8.7.1-441cae1b0-2026-09-19-win64.7z` (https://openxcom.org/oxce/release/).
- Détail des vérifications, statuts (vérifié, inférence, non vérifié) et revue indépendante : étude LOT-1A.

## Limites de vérification (toujours ouvertes)

- **Aucun gameplay n'est validé ni implémenté** sur la base de cette référence. Aucune fiche `MEC`.
- **Binaires non reconstruits :** le rattachement des binaires officiels au commit figé repose sur leur nom (hash `441cae1b0`, nommage par `git describe`). C'est une inférence solide, non vérifiée par recompilation.
- **Compatibilité non vérifiée, dans les deux sens du terme :**
  - **licences :** la compatibilité des licences tierces avec Bastion n'est pas auditée exhaustivement (code tiers de `src/`, bibliothèques de `deps/`, shaders, ressources) ;
  - **comportement :** OXCE n'a été ni exécuté ni comparé à Bastion ; le hasard du moteur et l'effet de chaque option restent inconnus.
- **Fichiers aux formats X-COM :** 292 fichiers dans `bin/standard` (`.MAP`, `.RMP`, `.MCD`…), de provenance non vérifiée, exclus de toute reprise (D4).
- Les pages GitHub n'étaient pas accessibles depuis l'environnement d'étude : les faits GitHub ont été vérifiés par le protocole Git.

## Règles

- Aucun code OXCE copié et aucun asset X-COM original sans audit de licence et décision enregistrée.
- Utiliser OXCE comme référence d'une mécanique exige une décision au statut « Validée » dans `docs/gameplay/GAMEPLAY-DECISIONS.md`.
- Figer la référence (version ou commit exact, date, auteur de la vérification) avant toute comparaison de comportement.
