# Contrôle indépendant de l'erratum AR-01/AR-02 de la consolidation MEC-0001 v0.4.3

- **Objet :** le diff `D/verif-v043e/diff-v0.4.3-erratum-AR01-AR02.patch` (SHA-256 `645915da758001dc701a0ab42e23e32b028f09f51b8a1a3e080ff9a7665c4d3d`). Il mène de la v0.4.3 initiale (`cd1c808b…6602`, 1 008 lignes) à la v0.4.3 avec erratum AR-01/AR-02 (`16bfac9d…6c51`, 1 013 lignes).
- **Relecteur :** agent distinct de l'auteur de l'erratum. J'ai travaillé en lecture seule et n'ai écrit que dans `D/revue-v043e-relecteur/`. Je ne m'accorde pas la validation finale : elle revient au propriétaire.
- **Date :** 20 novembre 2026.
- **Mandat de l'erratum :** JS-40, message 40 du propriétaire dans le journal (2026-11-20T17:09:00.014Z). Le texte cité dans ma commande est identique aux parties 1 et 2 de JS-40 et à sa ligne sur OC-01 à OC-07.
- **Bases :**
  - `origin/main` = `818c646c7d33b819d8b69b81679749be6e77eff9` ;
  - registre `docs/gameplay/GAMEPLAY-DECISIONS.md`, SHA-256 `9117d20c…d39e`, identique sur `origin/main` et dans l'arbre de travail ;
  - clone OXCE au commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, commit figé de `docs/references/OXCE-BASELINE.md` (l.13).
- **Notations :**
  - `D` = `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad` ;
  - « v043:N » : ligne N de la v0.4.3 initiale ; « err:N » : ligne N de l'erratum ;
  - au commit `441cae1b` : « BU:N » pour `src/Savegame/BattleUnit.cpp`, « AR:N » pour `src/Mod/Armor.cpp`, « RSB:N » pour `src/Mod/RuleStatBonus.cpp`, « RSo:N » pour `src/Mod/RuleSoldierBonus.cpp` ;
  - « RC43 » : rapport du contrôle indépendant de la v0.4.3 (`427e0736…02c2`), qui définit AR-01 et AR-02 (§2.1).
- **États** employés, sans mélange : **exécuté et réussi** ; **exécuté et échoué** ; **inspecté seulement** ; **non vérifié**.

## 1. Verdict : conforme sous réserves

**Ce que j'ai vérifié par mes propres contrôles (exécuté et réussi) :**
- **Empreintes.** Les six empreintes annoncées sont exactes.
- **Intégrité de la v0.4.3 initiale.** Elle est intacte. Son empreinte est celle que le propriétaire cite dans JS-39 (16:36:50Z), et le fichier n'a pas changé depuis 16:22:12Z.
- **Diff.** Mon diff est identique au patch fourni, octet pour octet. Le script `make_erratum.py`, rejoué sur la v0.4.3 initiale, reproduit l'erratum à l'identique.
- **Périmètre.** Le diff ne contient que quatre changements : le titre, une ligne d'erratum en en-tête, une phrase du §5 et l'introduction du §17.
  - Toutes les autres sections sont identiques.
  - Les 462 lignes de tableau sont identiques : matrices, scénarios, décisions et tableau des contrôles du §17.
  - Aucun marqueur de statut ne change de nombre.
  - OC-01 à OC-07 ne sont pas corrigées.
- **AR-01.** Les neuf renvois au code de la nouvelle phrase sont exacts au commit figé. La phrase remplit les cinq exigences de JS-40.
- **AR-02.** Les contrôles 3, 4, 9 et 11 ne sont plus présentés comme automatisés. Le classement du contrôle 6 en relecture est exact. J'ai relancé les scripts des contrôles classés comme automatisés : tous se terminent par 0, sur la v0.4.3 initiale comme sur l'erratum.
- **Règles.** Aucune règle de Bastion n'est créée ni modifiée.

**Ce qui empêche le verdict « conforme » :** deux défauts mineurs introduits par l'erratum. Ils ne touchent aucune règle (§3.1).
- **AE-01 (AR-01).** La phrase « Sans ce paramétrage, il vaut le bonus `energyRegen` » omet les bonus du soldat, que la phrase précédente vient d'ajouter au gain. L'égalité n'est exacte que si aucun bonus de soldat ne définit de récupération d'énergie, ce qui se paramètre par une autre clé `recovery` que celle de l'armure.
- **AE-02 (AR-02).** L'introduction affirme que, pour le contrôle 11, « la comparaison des sections » est automatisée. Rien ne l'établit : ni la colonne « Méthode », ni l'inventaire du §15, ni les fichiers de `verif-v043/`. Or RC43 range précisément cette comparaison parmi les relectures.

S'y ajoutent cinq observations facultatives (§3.2) et les réserves structurelles déjà connues (§3.3).

**Aucune anomalie bloquante ni importante. Aucun écart au périmètre (§4). Aucune décision de gameplay modifiée.**

## 2. Contrôle point par point

### 2.1 Vérification 1 — Empreintes et intégrité

| Document | SHA-256 recalculé | Annoncé | État |
|---|---|---|---|
| v0.4.3 initiale | `cd1c808b10dbcf39f96e557f9d6ef994b232bdcacc44e696122edd4dbee76602` | identique | exécuté et réussi |
| v0.4.3 avec erratum | `16bfac9d1b5995b5eb2f4ba418639f9e24ffe56435b5fbf279ab3ff80d196c51` | identique | exécuté et réussi |
| Diff de l'erratum | `645915da758001dc701a0ab42e23e32b028f09f51b8a1a3e080ff9a7665c4d3d` | identique | exécuté et réussi |
| `make_erratum.py` | `11f1054a50dd252900e0c8376f1d2ddcbe39671338b8e6def486b8964ae2d783` | identique | exécuté et réussi |
| RC43 | `427e0736235ad1eb5340cfb028eb19c24c315b030399e899fb41421a5ca902c2` | identique | exécuté et réussi |
| Extraction 4 | `9ef7d01f16c351b929c7ee411285cf78539703bc352d7a774c7a830e3740c019` | identique | exécuté et réussi |

| Contrôle | Résultat | État |
|---|---|---|
| v0.4.3 initiale intacte | L'empreinte `cd1c808b…` est celle que cite le propriétaire dans JS-39 (extraction, l.1564), et celle de RC43 (l.3). Elle est aussi celle de la copie reproduite par RC43 (`revue-v043-relecteur/v043-reproduite.md`). Dernière modification du fichier : 16:22:12Z, avant JS-39 et JS-40 | exécuté et réussi |
| Diff refait | `diff -u` de la v0.4.3 initiale à l'erratum : code 1, attendu puisque les fichiers diffèrent. `cmp` de mon diff avec le patch fourni, en-têtes et horodatages compris : 0 | exécuté et réussi |
| Script de l'erratum | `make_erratum.py`, rejoué sur la v0.4.3 initiale avec une sortie dans mon dossier : code 0. La sortie a l'empreinte `16bfac9d…`, et `cmp` avec l'erratum donne 0. Chaque remplacement exige une occurrence unique, faute de quoi le script s'arrête. Il ne fait que quatre remplacements, qui sont exactement les quatre changements du diff | exécuté et réussi |
| Extraction des messages | Refaite avec O-2 (`extract_user_msgs.py`, `206ca788…`, empreinte conforme au §15) : 40 messages. Elle est identique à l'extraction 4 (`cmp` : 0) | exécuté et réussi |

### 2.2 Vérification 2 — Périmètre

| Bloc | v043 | err | Contenu | Jugement | État |
|---|---|---|---|---|---|
| 1 | l.1 | l.1 | titre : ajout de « (erratum AR-01/AR-02) » | métadonnée nécessaire : JS-40, 2.1, demande une version « identifiée comme v0.4.3 avec erratum AR-01/AR-02 » | exécuté et réussi |
| 2 | — | l.5 | ligne « **Erratum AR-01/AR-02** » insérée entre « Nature » et « Statut » | métadonnée nécessaire : mandat, base, ce qui est corrigé et ce qui ne l'est pas (§2.5) | exécuté et réussi (position) ; contenu : §2.5 |
| 3 | l.355 | l.356 | §5, point d'articulation (OB-06) : la phrase « Or OXCE ne réduit pas… au torse. » est remplacée | le préfixe et le suffixe de la ligne sont identiques. Sont conservés : le marqueur [OUV], la citation de N14 (R:104-105) et la phrase finale du point (« L'articulation de N14 et d'ARB-D avec M-04=B… ») | exécuté et réussi |
| 4 | l.833 | l.834-838 | §17 : introduction | La phrase « Chaque contrôle a été exécuté… code de sortie 0 » est retirée. La suite (« Les scripts sont inventoriés au §15… sont nouveaux. ») est conservée mot pour mot. Le tableau (15 lignes), la correspondance avec le §4 de P7 et les « Impossibilités de vérification » sont identiques | exécuté et réussi |

Résultats de mon script `perimetre.py` (34 contrôles, code 0) :
- seules les §5 et §17 diffèrent, hors en-tête. Le bloc « Statut » et la phrase finale sont identiques ;
- les 462 lignes de tableau sont identiques. **Aucune décision, valeur, aucun scénario ni aucune matrice n'est modifié** ;
- les marqueurs ont le même nombre d'occurrences : [OUV] 49, [DÉD] 23, [INS] 25, [VAL] 19, [TR] 78, [TR-M] 21, [PNV 11, « Sp » 35, « Pa » 25, « (recommandé) » 3 ;
- **OC-01 à OC-07 ne sont pas corrigées** :
  - le texte visé par OC-01, OC-02, OC-03, OC-05 et OC-07 est présent, avec le même nombre d'occurrences ;
  - pour OC-04, la ligne T47 est identique ;
  - pour OC-06, la sous-liste du §5 finit toujours par « n'est fixé ; » (err:354), juste avant le rappel du registre.

Autres constats sur le périmètre :
- **L'affirmation visée par AR-01 ne figure qu'au §5** (v043:355). J'ai cherché `prepareEnergy`, « ne réduit pas » et « récupération d'énergie » dans tout le document. Le point du §14 (v043:721) ne la reprend pas. Corriger le seul §5 suffit donc. (exécuté et réussi)
- **La phrase remplacée devient sept phrases**, soit 1 024 caractères. L'endroit est respecté : seule la phrase visée change. La longueur se justifie par les cinq exigences du mandat (OE-05). (exécuté et réussi pour la mesure ; inspecté seulement pour le jugement)

### 2.3 Vérification 3 — AR-01, sur le code d'OXCE

**Nouvelle rédaction (err:356, après « (R:104-105). ») :**

> Côté OXCE, le code lu au commit `441cae1b`, sans exécution, montre ceci. La fonction `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`) ne retranche du gain d'énergie qu'elle reçoit que l'effet des blessures mortelles au torse ; elle ne fait pas intervenir la charge. Ce gain est calculé ailleurs, par l'armure ([code OXCE retiré — D4], l.2946), qui y ajoute les bonus du soldat (l.2902-2909). Il est paramétrable par la clé `recovery` de l'armure, éventuellement par script (`src/Mod/Armor.cpp:234`). Sans ce paramétrage, il vaut le bonus `energyRegen` (`Armor.cpp:60` ; `src/Mod/RuleStatBonus.cpp:537-544`) : le tiers des TU initiales d'un soldat, ou la récupération d'énergie fixée par la règle de l'unité (`RuleStatBonus.cpp:292` et `144-155`), sans terme de charge. Dans la récupération, la charge (`getCarriedWeight`) n'intervient qu'au calcul des TU (l.2717). Les paramétrages possibles de la clé `recovery` n'ont pas été étudiés : le constat ne vaut que pour la configuration par défaut.

J'ai lu les fichiers avec `git show HEAD:<fichier>`. Mon script `citations_oxce.py` vérifie 24 points de ces fichiers (code 0). Le comportement du code est **lu, non exécuté** : je n'ai ni compilé ni lancé OXCE.

| # | Affirmation | Code au commit `441cae1b` | Constat | État |
|---|---|---|---|---|
| 1 | « le code lu au commit `441cae1b`, sans exécution » | — | La formule correspond à la nature de la preuve. Le commit cité est conservé | inspecté seulement |
| 2 | `prepareEnergy` (BU:2733-2742) ne retranche du gain reçu que l'effet des blessures mortelles au torse, sans faire intervenir la charge | BU:2733 ouvre la fonction et BU:2742 la ferme. La seule soustraction est à BU:2738 : [code OXCE retiré — D4]. Aucun terme de poids, de charge ni d'encombrement n'y figure | **Exact.** Précisions, qui n'infirment rien : le terme retranché vaut 10 % de l'énergie *courante* par blessure ; le résultat est ensuite borné entre 0 et `stamina` (BU:2740) ; rien ne se passe si l'unité est hors de combat (BU:2735) | renvois : exécuté et réussi ; comportement : inspecté seulement |
| 3 | le gain est calculé par l'armure (BU:2946) | BU:2946 : [code OXCE retiré — D4] | **Exact** | exécuté et réussi |
| 4 | l'armure « y ajoute les bonus du soldat (l.2902-2909) » | BU:2902-2909 : [code OXCE retiré — D4], puis [code OXCE retiré — D4] pour chaque bonus. BU:2910 ne contient que l'accolade fermante du `if`. Le script par défaut de l'armure part de la valeur reçue ([code OXCE retiré — D4], RSB:579 ; [code OXCE retiré — D4], RSB:382), puis y ajoute `energyRegen` (RSB:384-407) | **Exact** dans la configuration par défaut. Avec un script propre à l'armure (RSB:363-366), cet ajout dépend du script. Les lignes citées montrent le calcul des bonus du soldat, et non leur ajout par l'armure (OE-01) | exécuté et réussi (lignes) ; inspecté seulement (comportement) |
| 5 | gain paramétrable par la clé `recovery` de l'armure, éventuellement par script (AR:234) | AR:234 : [code OXCE retiré — D4]. Une chaîne placée sous la clé est chargée comme script (RSB:363-366) | **Exact** | exécuté et réussi |
| 6 | sans ce paramétrage, le gain vaut le bonus `energyRegen` (AR:60 ; RSB:537-544) | AR:60 : [code OXCE retiré — D4]. RSB:537-544 : [code OXCE retiré — D4]. Le script par défaut renvoie l'arrondi de `ENRecovery` + `energyRegen` (RSB:379-409, 579). `ENRecovery` est la somme des récupérations d'énergie des bonus du soldat (BU:2902-2909). Chacune se lit sous la clé `recovery` propre au bonus (RSo:57-60) et vaut 0 sans elle ([code OXCE retiré — D4] et `_bonusOrig` vide, `RuleStatBonus.h:40-42`) | **Renvois exacts.** **L'égalité est incomplète** : elle ne vaut que si aucun bonus de soldat ne définit de récupération d'énergie. La phrase précédente vient pourtant d'ajouter ces bonus au gain → **AE-01** | renvois : exécuté et réussi ; comportement : inspecté seulement |
| 7 | `energyRegen` = le tiers des TU initiales d'un soldat, ou la récupération de la règle de l'unité (RSB:292 ; RSB:144-155) | RSB:292 : [code OXCE retiré — D4]. RSB:144-155 : [code OXCE retiré — D4] pour une unité qui a un soldat du Géoscape, sinon [code OXCE retiré — D4] | **Exact**, à la division entière près ([code OXCE retiré — D4] est un tiers tronqué) | exécuté et réussi (lignes) ; inspecté seulement (comportement) |
| 8 | « sans terme de charge » | Aucun terme de poids à RSB:144-155. Les 50 termes de bonus disponibles (RSB:235-293) n'en comportent aucun lié au poids ou à la charge | **Exact** | exécuté et réussi |
| 9 | dans la récupération, `getCarriedWeight` n'intervient qu'au calcul des TU (l.2717) | BU:2717 est dans `prepareTimeUnits` (BU:2709-2727). Dans tout `src/`, `getCarriedWeight` n'apparaît qu'à BU:2717, BU:3110 (`addItem`, placement d'un objet), BU:4852 (définition), `BattleUnit.h:696` (déclaration) et `InventoryState.cpp:656` (inventaire). `updateUnitStats` (BU:2894-2948) ne l'appelle pas | **Exact** | exécuté et réussi |
| 10 | paramétrages de `recovery` non étudiés ; constat limité à la configuration par défaut | — | La limite est juste, et nécessaire. Ce que je constate en plus, sans l'exiger : les 111 fichiers `.rul` de `bin/` ne contiennent aucune clé `recovery:` ni `soldierBonuses:`. Les données standard livrées au commit figé relèvent donc de la configuration par défaut | exécuté et réussi (recherche) ; la portée de l'information est inspectée seulement |

**Les cinq exigences de JS-40 :**

| Exigence | Constat | État |
|---|---|---|
| limiter le constat à ce que démontre le code | Oui : lecture sans exécution, et constat limité à la configuration par défaut. Seule réserve : l'égalité de la phrase 5 (AE-01) | inspecté seulement |
| distinguer la fonction examinée des paramètres calculés ailleurs | Oui : la phrase 2 traite de `prepareEnergy`, les phrases 3 à 5 du calcul du gain par l'armure et les bonus | inspecté seulement |
| tenir compte des paramètres éventuels de l'armure | Oui : clé `recovery`, script et valeur par défaut, avec la limite déclarée. Le paramétrage des bonus du soldat n'est pas nommé (AE-01) | inspecté seulement |
| conserver les références au code vérifié | Oui : `src/Savegame/BattleUnit.cpp:2733-2742` et le commit `441cae1b` sont conservés. Les références que proposait RC43 sont ajoutées (BU:2946, AR:234, RSB:144-155 et 537-544, BU:2717), ainsi que AR:60, RSB:292 et BU:2902-2909. Les neuf renvois de lignes sont exacts | exécuté et réussi |
| ne modifier aucune règle de Bastion | Oui : la citation de N14, le marqueur [OUV] et la phrase qui renvoie aux modalités de M-04=B sont inchangés. La nouvelle rédaction ne décrit que le code d'OXCE (§2.6) | exécuté et réussi (texte inchangé) ; inspecté seulement (absence de portée normative) |

**La phrase va-t-elle au-delà du code ?** Pour l'essentiel, non. Elle ne présente plus comme générale l'affirmation « OXCE ne réduit pas la récupération d'énergie selon la charge » ; elle décrit le code et borne le constat à la configuration par défaut. Le seul dépassement est l'égalité de la phrase 5 (AE-01). Il est sans effet sur la conclusion « sans terme de charge » dans la configuration par défaut.

### 2.4 Vérification 4 — AR-02

**Nouvelle introduction (err:834-836) :**

> Elle comprend deux sortes de contrôles :
> - **contrôles automatisés**, exécutés par un script (`python3 -I`) ou une commande du shell, dont le code de sortie est connu et vaut 0 : contrôles 1, 2, 5, 7, 8, 10, 12 et 13. Pour le contrôle 7, l'interprétation de la sortie relative à JS-22 est une lecture ;
> - **vérifications documentaires par relecture** : contrôles 3, 4 et 6 entièrement ; contrôles 9 et 11 en partie. Pour le 9, la relecture du §3.5 et du §13 complète S-8. Pour le 11, le diff (O-8) et la comparaison des sections sont automatisés, mais leur rapprochement avec le §21 est une relecture. Une relecture n'a pas de code de sortie : sa conclusion repose sur l'examen décrit dans la colonne « Méthode ».

Chacun des 13 contrôles est classé une fois. Aucun n'est oublié ni compté deux fois. J'ai relancé les scripts de l'auteur sur les mêmes fichiers, avec `python3 -I` et des sorties dans mon dossier. Ce sont des scripts en lecture seule : j'ai lu leur code avant de les lancer. Ces relances montrent que les scripts tournent et se terminent par 0 ; **elles n'établissent pas que l'auteur les a lancés à l'époque** (non vérifié, §3.3).

| N° | Méthode (colonne du §17) | Classement de l'erratum | Outil inventorié au §15 | Constat | État |
|---|---|---|---|---|---|
| 1 | S-7 | automatisé | S-7 (`check_textes.py`) se termine par 1 en cas d'échec | exact. Relancé : 0, sur la v0.4.3 initiale et sur l'erratum | exécuté et réussi |
| 2 | S-7 | automatisé | S-7 | exact. Relancé : 0, sur les deux versions | exécuté et réussi |
| 3 | « lecture des lignes citées » | relecture entière | aucun | exact | inspecté seulement |
| 4 | « relecture du diff O-8 bloc par bloc » | relecture entière | O-8 est le diff lui-même, et non un contrôle | exact | inspecté seulement |
| 5 | S-5, S-9 et S-12 | automatisé | S-9 et S-12 reposent sur des assertions ; S-5 n'en contient que deux et affiche surtout des valeurs | Exact. Relancés : 0 chacun. La concordance des valeurs de S-5 avec le document se lit dans la sortie (OE-02) | exécuté et réussi |
| 6 | aucun outil nommé : la colonne ne donne que le critère (« AN-01 à AN-08 et OB-01 à OB-08 ont chacun une ligne au §21 ; … ») | relecture entière | Aucun. S-10 ne vérifie pas les lignes des §18, §20 et §21 | **Exact** : c'est le classement prudent, et la colonne ne cite aucun outil. Le mandat ne cite pas ce contrôle, mais chaque contrôle devait être rangé dans une catégorie. RC43 avait omis le 6 dans sa proposition. J'ai refait sa conclusion par script : AN-01 à AN-08 et OB-01 à OB-08 sont au §21 ; I-1, M-01 à M-18 et A-1 à A-6 au §20 ; W-01 à W-14 au §18. Elle est complète | classement : inspecté seulement ; conclusion : exécuté et réussi |
| 7 | « O-5 sur O-7 » | automatisé, avec une lecture pour JS-22 | O-5 (`omissions.py`) se termine toujours par 0 | Exact. Relancé : 0. La sortie est conforme à la colonne « Résultat » : JS-22 « PARTIEL » sur 47 caractères ; JS-23, JS-29 et JS-37 non copiés ; JS-31 partiel. La réserve sur JS-22 est juste (OE-02) | exécuté et réussi |
| 8 | S-8 | automatisé | S-8 (`check_matrice.py`) se termine par 1 si un rattachement n'est pas cité | exact. Relancé : 0 ; 65 rattachements, aucun non cité, sur les deux versions | exécuté et réussi |
| 9 | « relecture du §3.5 et du §13 ; S-8 » | relecture partielle, S-8 en complément | S-8 | exact | inspecté seulement |
| 10 | « empreintes recalculées » | automatisé | S-10 compare au §15, par script, les empreintes de 12 scripts. Pour les autres fichiers, la commande n'est pas nommée | Cohérent avec la colonne (« recalculées ») et avec la proposition de RC43 (OE-03) | inspecté seulement ; exécution par l'auteur : non vérifié |
| 11 | « diff de la v0.4.2 à la v0.4.3 (O-8), comparé section par section » | relecture partielle. Selon l'erratum, « le diff (O-8) et la comparaison des sections sont automatisés » | Aucun script de comparaison par sections, ni au §15 ni dans `verif-v043/` | Le classement partiel est exact. En revanche, l'automatisation affirmée de la comparaison des sections n'est pas étayée → **AE-02** | inspecté seulement ; exécution par l'auteur : non vérifié |
| 12 | S-10 | automatisé | S-10 (`check_v043.py`) se termine par 1 en cas d'échec | exact. Relancé : 0 sur les deux versions. Sur l'erratum, ses tests sur OB-06 (`prepareEnergy` au §5), sur la « concordance fortuite » du §17 et sur la phrase finale passent encore | exécuté et réussi |
| 13 | S-11 | automatisé | S-11 (`citations_v043.py`) se termine toujours par 0 | Exact. Relancé : 0. Sur la v0.4.3 initiale : 269 passages, 254 dans les sources primaires, 15 dans le document, 0 introuvable, conformément au tableau. Sur l'erratum : 270 passages, 255 dans les sources primaires, 15 dans le document, 0 introuvable. Le passage de plus est « Méthode », retrouvé dans les sources | exécuté et réussi |

**Conclusions :**
- **Les contrôles 3, 4, 9 et 11 ne sont plus présentés comme entièrement automatisés.** (exécuté et réussi : aucun n'est dans la liste des contrôles automatisés)
- **Le classement est exact au regard de la colonne « Méthode »**, avec une exception : la phrase sur le contrôle 11 (AE-02).
- **Le classement du contrôle 6 en relecture est exact.** Il ne cache pas une conclusion fausse : je l'ai refaite.
- Les empreintes des huit scripts que j'ai lus sont conformes au §15 : S-5, S-7, S-8, S-9, S-10, S-11, S-12 et O-5. (exécuté et réussi)

### 2.5 Vérification 5 — Métadonnées

Ligne d'erratum (err:5) :

> **Erratum AR-01/AR-02** (mandat d'erratum du propriétaire, JS-40, 2026-11-20T17:09:00Z) : seules deux corrections sont faites, au §5 (comparaison avec OXCE, AR-01) et dans l'introduction du §17 (nature des contrôles, AR-02). Le reste du texte est celui de la v0.4.3 initiale (SHA-256 `cd1c808b…6602`), conservée intacte. Pour limiter l'erratum à ces deux corrections, le mandat d'erratum et le rapport de contrôle indépendant de la v0.4.3 initiale (SHA-256 `427e0736…02c2`) ne sont pas ajoutés au §15, et la phrase finale n'est pas actualisée.

| Élément | Constat | État |
|---|---|---|
| Identifiant JS-40 | C'est le message 40 de ma réextraction, identique à l'extraction 4. Il commence par « BASTION — Mandat d'erratum documentaire v0.4.3 » | exécuté et réussi |
| Horodatage | Le journal donne 2026-11-20T17:09:00.014Z, tronqué à la seconde comme ailleurs dans le document (§15 : « JS-38 (2026-11-20T16:12:04Z) ») | exécuté et réussi |
| Empreinte de la v0.4.3 initiale | `cd1c808b…` est exacte et complète, et c'est celle de JS-39 | exécuté et réussi |
| Empreinte du rapport de contrôle | `427e0736…` est exacte et complète. C'est la « Base » que nomme JS-40 (« rapport de contrôle indépendant correspondant ») | exécuté et réussi |
| Ce qui est corrigé | « au §5 (…, AR-01) et dans l'introduction du §17 (…, AR-02) » : c'est exact, et ce sont les seuls changements de fond | exécuté et réussi |
| Ce qui n'est pas corrigé | Le §15 et la phrase finale ne sont pas modifiés : c'est exact (§2.2). Deux autres mentions, désormais dépassées, ne sont pas nommées (OE-04) | exécuté et réussi ; OE-04 : inspecté seulement |
| Titre | « v0.4.3 (erratum AR-01/AR-02) » est conforme à JS-40, 2.1 | exécuté et réussi |
| Caractère « strictement nécessaire » | Le titre et la ligne sont nécessaires pour identifier la version et pour la traçabilité. La dernière phrase de la ligne évite au lecteur de croire le §15 et la phrase finale actualisés. Aucune autre information n'est ajoutée | inspecté seulement |

### 2.6 Vérification 6 — Absence de règle nouvelle

- Les 462 lignes de tableau sont identiques. Seules les §5 et §17 changent, hors en-tête. Le nombre de chaque marqueur de statut est inchangé. (exécuté et réussi)
- **§5.** Le texte remplacé et le nouveau texte ne décrivent que le code d'OXCE. Les verbes du nouveau texte sont descriptifs : « montre », « ne retranche », « est calculé », « est paramétrable », « vaut », « n'intervient », « n'ont pas été étudiés ». La règle N14, sa citation (R:104-105), le marqueur [OUV] du point d'articulation et le renvoi aux modalités de M-04=B sont inchangés. Le texte n'affirme aucune fidélité à OXCE (CLAUDE.md, §3), et la mention « **Aucune fidélité n'est affirmée** » du §11 (err:499) est inchangée. (exécuté et réussi pour le texte inchangé ; inspecté seulement pour l'absence de portée normative)
- **§17.** L'introduction décrit la nature des contrôles internes. Elle ne porte aucune règle de Bastion. (inspecté seulement)
- **Registre.** `docs/gameplay/GAMEPLAY-DECISIONS.md` a l'empreinte `9117d20c…d39e`, sur `origin/main` comme dans l'arbre de travail. C'est la valeur relevée par RC43. (exécuté et réussi)

**Aucune règle de Bastion n'est créée ni modifiée.**

## 3. Anomalies restantes

### 3.1 Défauts de l'erratum

| N° | Endroit | Preuve | Gravité | Correction proposée | État |
|---|---|---|---|---|---|
| **AE-01** | §5, point d'articulation (err:356) : « Sans ce paramétrage, il vaut le bonus `energyRegen` (…) » | La phrase précédente dit que l'armure « ajoute les bonus du soldat » au gain. Le code le confirme. Le script par défaut de l'armure part de `externalBonuses` = `ENRecovery` (RSB:579, 382), puis y ajoute `energyRegen` (RSB:384-407). `ENRecovery` est la somme des récupérations d'énergie des bonus du soldat (BU:2902-2909). Chacune est lue sous la clé `recovery` propre au bonus (RSo:57-60), et vaut 0 sans cette clé (`RuleStatBonus.h:40-42`). Dans sa lecture naturelle (« il » = le gain), l'égalité n'est donc exacte que si aucun bonus de soldat ne définit de récupération d'énergie. Ce paramétrage n'est pas nommé : la dernière phrase parle de « la clé `recovery` », après n'avoir présenté que celle de l'armure | **mineure.** Le défaut est nouveau, introduit par l'erratum. La conclusion « sans terme de charge » n'en dépend pas dans la configuration par défaut, et aucune règle de Bastion n'en dépend | Écrire : « Sans paramétrage, ni de l'armure ni des bonus du soldat, il vaut le bonus `energyRegen` (…). La récupération propre à ces bonus est lue sous leur clé `recovery` (`src/Mod/RuleSoldierBonus.cpp:57-60`), et elle est nulle par défaut. » Et, à la fin du point : « Les paramétrages possibles des clés `recovery` de l'armure et des bonus du soldat n'ont pas été étudiés » | lignes : exécuté et réussi ; comportement : inspecté seulement (code lu, non exécuté) |
| **AE-02** | §17, introduction (err:836) : « Pour le 11, le diff (O-8) et la comparaison des sections sont automatisés, mais leur rapprochement avec le §21 est une relecture. » | La colonne « Méthode » du contrôle 11 (err:854) dit « diff de la v0.4.2 à la v0.4.3 (O-8), comparé section par section », sans nommer d'outil pour la comparaison. Le §15 inventorie S-1 à S-13 et O-1 à O-8 : aucun ne compare des sections, et O-8 est le diff lui-même. `verif-v043/` ne contient que `calculs_v043.py`, `check_v043.py`, `citations_v043.py`, le diff, `make_v043.py` et l'extraction 3. RC43 (§2.1, AR-02) range précisément « comparé section par section » parmi les relectures. L'erratum affirme donc une automatisation que le document n'établit pas : c'est le défaut même qu'AR-02 corrige | **mineure.** Défaut de traçabilité, nouveau. La conclusion du contrôle 11 reste exacte : RC43 a vérifié que chaque bloc tombe dans une section déclarée au §21 | Écrire : « Pour le 11, le diff (O-8) est produit par une commande ; sa comparaison section par section avec le §21 est une relecture. » Si une commande de comparaison a réellement été exécutée, il faudrait la nommer avec son code de sortie, et l'inventorier au §15, ce qui sort du périmètre de l'erratum | inspecté seulement ; exécution par l'auteur : non vérifié |

### 3.2 Observations (ce ne sont pas des erreurs ; correction facultative)

| N° | Endroit | Constat | Proposition |
|---|---|---|---|
| OE-01 | §5 (err:356) | (a) « qui y ajoute les bonus du soldat (l.2902-2909) » : ces lignes montrent la somme des bonus dans `ENRecovery`. Leur ajout par l'armure se voit à AR:789-791 et RSB:575-583, et le script par défaut à RSB:379-409 ; ces lignes ne sont pas citées. (b) « (l.2717) » vient après des renvois à `RuleStatBonus.cpp` : le fichier sous-entendu est `BattleUnit.cpp`. (c) « le tiers » est un tiers tronqué ([code OXCE retiré — D4], RSB:149) | (a) ajouter « `Armor.cpp:789-791` ; `RuleStatBonus.cpp:575-583` » ; (b) écrire « `BattleUnit.cpp:2717` » ; (c) sans objet pour la conclusion |
| OE-02 | §17 (err:835) | Pour les contrôles 5 (S-5), 7 (O-5) et 13 (S-11), le code de sortie 0 atteste l'exécution, et non le verdict. O-5 et S-11 n'échouent jamais, et S-5 n'a que deux assertions : le verdict se lit dans la sortie. L'erratum ne le dit que pour JS-22 (contrôle 7). Le mandat demandait seulement de distinguer automatisé et relecture, et cette distinction est faite | si l'on veut : « Pour les contrôles 5, 7 et 13, le code 0 atteste l'exécution ; la conclusion se lit dans la sortie. » |
| OE-03 | §17, contrôle 10 | Le classement en automatisé suit la colonne (« empreintes recalculées ») et la proposition de RC43. S-10 compare au §15, par script, les empreintes de 12 scripts. Pour les autres fichiers du §15, la méthode de comparaison n'est pas décrite | aucune correction requise |
| OE-04 | « Nature » (err:4, « Non revu ») ; §17, « Impossibilités de vérification » (err:863, « contrôle indépendant du diff de la v0.4.3 : non fait ») | Depuis RC43, ces deux mentions sont dépassées. La ligne d'erratum ne nomme que le §15 et la phrase finale (err:1013). La phrase « Le reste du texte est celui de la v0.4.3 initiale » couvre le cas en termes généraux, et les modifier sortirait du périmètre | les nommer dans la ligne d'erratum, ou laisser tel quel |
| OE-05 | §5 (err:356) | La phrase remplacée (environ 190 caractères) devient sept phrases (1 024 caractères). L'endroit est respecté. Le détail se justifie par les cinq exigences du mandat | à l'appréciation du propriétaire |

### 3.3 Réserves structurelles déjà connues (ce ne sont pas des défauts de l'erratum)

- **Sources non authentifiées** (RD-1, RD-6, RD-9) :
  - P1 à P7 sont des copies ;
  - le journal n'a pas d'empreinte stable ;
  - RV41 et RV42 ne sont authentifiés que par leur empreinte ;
  - JS-40 n'existe que dans le journal : par choix de l'erratum, il n'est pas inventorié au §15.
- **Archivage non effectué** (RD-1). C'est un préalable à toute inscription. RD-10 subordonne un verdict « pleinement conforme » à la vérification des preuves.
- **Paramètres volontairement ouverts** :
  - les modalités de M-04=B et de R-5=A ;
  - les neuf PNV ;
  - les points [OUV], dont le point d'articulation du §5, qui reste [OUV].

  Je n'en exige pas la résolution.
- **Comportement d'OXCE.** Il est lu, non exécuté. Aucune compilation, aucune exécution.
- **Commandes de l'auteur.** Je n'ai pas vérifié les commandes réellement lancées par l'auteur, ni pour la v0.4.3 ni pour l'erratum. Conformément à ma commande, je n'ai pas consulté ses réponses dans le journal. Mes relances (§2.4) établissent l'état actuel, et non l'historique.
- **Empreinte de S-13** (`make_v043.py`) : elle n'est toujours pas annoncée (RC43, §2.3). L'erratum n'y touche pas.

## 4. Écarts au périmètre

**De l'erratum : aucun.**
- Il apporte quatre changements : le titre, la ligne d'erratum, une phrase du §5 et l'introduction du §17.
- OC-01 à OC-07 ne sont pas touchées.
- Aucune décision, valeur, aucun scénario ni aucune matrice n'est modifié.
- Le classement du contrôle 6 n'est pas un écart : AR-02 impose de ranger chaque contrôle dans l'une des deux catégories.

**De mon contrôle :**
- Je n'ai écrit que dans `D/revue-v043e-relecteur/` (§6).
- J'ai utilisé git uniquement avec `show`, `rev-parse` et `ls-tree`.
- Python a toujours été lancé avec `python3 -I`.
- Aucun accès réseau, aucune action sur GitHub.
- J'ai relancé, en lecture seule, des scripts de l'auteur (S-5, S-7 à S-12 et O-5) après avoir lu leur code. Ils n'écrivent que sur la sortie standard, redirigée vers mon dossier. S-11 appelle lui-même `git -C /home/user/bastion show origin/main:<fichier>`, qui fait partie des commandes autorisées. Il lit aussi un fichier de `/root/.claude/uploads/`.
- Un de mes scripts a échoué une fois (`perimetre.py`, code 1). La cause était dans mon script, non dans le document : la chaîne d'OC-06 figure aussi au §2 bis (err:170), et le test prenait la première occurrence. J'ai visé l'occurrence du §5, puis relancé le script : code 0.
- Je n'ai pris aucune décision de gameplay ni rendu aucun arbitrage.

## 5. Commandes exécutées et codes de sortie

| # | Commande | Code | Résultat |
|---|---|---|---|
| 1 | `sha256sum` des six documents ; `ls -la` | 0 | six empreintes conformes |
| 2 | `cat` du patch et de `make_erratum.py` | 0 | lecture |
| 3 | `diff -u` de la v0.4.3 initiale à l'erratum, vers `mon-diff.patch` | 1 | attendu : les fichiers diffèrent |
| 4 | `diff` des corps de patch, puis `cmp` des deux patchs complets | 0 ; 0 | identiques |
| 5 | `python3 -I make_erratum.py <v0.4.3> <mon dossier>/erratum-reproduit.md` ; `sha256sum` ; `cmp` | 0 ; 0 ; 0 | erratum reproduit, `16bfac9d…` |
| 6 | `sha256sum revue-v043-relecteur/v043-reproduite.md` ; `grep cd1c808b` | 0 | `cd1c808b…`, également cité dans JS-39 |
| 7 | `sed`, `grep` et `wc` sur la v0.4.3 et l'erratum (§5, §15, §17, §21, en-tête, numéros de ligne) | 0 | lecture |
| 8 | `cat` de S-7, S-8, S-9, S-10, S-11, S-12 et O-5 ; `grep` sur S-5 ; `sha256sum` des huit scripts | 0 | empreintes conformes au §15 |
| 9 | `git -C <clone> rev-parse HEAD` ; `git -C bastion rev-parse origin/main` ; `git show origin/main:docs/references/OXCE-BASELINE.md \| grep` | 0 ; 0 ; 0 | `441cae1b…` ; `818c646c…` ; commit figé à la l.13 |
| 10 | `git show HEAD:src/Savegame/BattleUnit.cpp` (l.2700-2760, 2870-2965, 3090-3120) | 0 | lecture |
| 11 | `git show HEAD:src/Mod/Armor.cpp`, `RuleStatBonus.cpp`, `RuleStatBonus.h` et `RuleSoldierBonus.cpp` | 0 | lecture |
| 12 | boucle `git ls-tree -r HEAD src/` + `git show \| grep getCarriedWeight` | 0 | cinq occurrences (§2.3, n° 9) |
| 13 | boucles `git ls-tree -r HEAD bin/` + `git show \| grep` sur `recovery` | 0 ; 0 | 111 fichiers `.rul` ; 0 clé `recovery:`, 0 clé `soldierBonuses:` |
| 14 | `python3 -I verif-v04/extract_user_msgs.py <journal> <mon dossier>/messages-reextraits.md` ; `cmp` avec l'extraction 4 | 0 ; 0 | 40 messages ; identiques |
| 15 | `python3 -I perimetre.py <v0.4.3> <erratum>`, premier passage | **1** | erreur de mon script (§4) |
| 16 | `python3 -I perimetre.py <v0.4.3> <erratum>`, après correction | 0 | 34 contrôles réussis |
| 17 | `python3 -I citations_oxce.py <clone>` | 0 | 24 contrôles réussis |
| 18 | `python3 -I` S-7, S-8, S-10 et S-11 sur la v0.4.3 initiale | 0 chacun | conformes au tableau du §17 |
| 19 | `python3 -I` S-7, S-8, S-10 et S-11 sur l'erratum | 0 chacun | idem ; S-11 : 270 passages, 0 introuvable |
| 20 | `python3 -I` S-5, S-9, S-12 ; O-5 sur O-7 et les sept copies | 0 chacun | conformes au tableau du §17 |
| 21 | `python3 -I -c` : contrôle 6 refait (§18, §20 et §21 de l'erratum) | 0 | complet |
| 22 | `git show origin/main:docs/gameplay/GAMEPLAY-DECISIONS.md \| sha256sum` ; `sha256sum` de l'arbre de travail | 0 ; 0 | `9117d20c…d39e` dans les deux cas |
| 23 | `stat` des versions, de la pièce P7 et des fichiers de `verif-v043e/` | 0 | horodatages cohérents (§2.1) |
| 24 | `sha256sum` de mes fichiers produits | 0 | §6 |

## 6. Fichiers produits (tous dans `D/revue-v043e-relecteur/`)

| Fichier | SHA-256 | Rôle |
|---|---|---|
| `mon-diff.patch` | `645915da758001dc701a0ab42e23e32b028f09f51b8a1a3e080ff9a7665c4d3d` | diff refait, identique au patch fourni |
| `erratum-reproduit.md` | `16bfac9d1b5995b5eb2f4ba418639f9e24ffe56435b5fbf279ab3ff80d196c51` | sortie de `make_erratum.py`, rejoué |
| `messages-reextraits.md` | `9ef7d01f16c351b929c7ee411285cf78539703bc352d7a774c7a830e3740c019` | réextraction des 40 messages du propriétaire |
| `perimetre.py` | `a7cc0241f331ebf520f535a6f926dc2da95993a509e130fc03e6d605e8bd2032` | contrôle du périmètre |
| `sortie-perimetre.txt` | `3e396732510a45f364731ca7dd2e3aa0a2f9246471d0293bca83ec2643c46a9c` | sa sortie (code 0) |
| `citations_oxce.py` | `34ea55e1e948ab60caab2efe8d811e6779dfbafe50b800d64d8d4ce1fd41ea19` | contrôle des renvois au code d'OXCE |
| `sortie-citations-oxce.txt` | `c01928086bd47ad5b7a7f4f576b0ef67fb019cecc88bf05e761cc4ad664c00c2` | sa sortie (code 0) |
| `sorties-scripts-auteur.txt` | `c58e8a0862e93baf6e72c9c7e3b97b8e0680abe92c54dc196b21bab8b15ca694` | sorties des scripts de l'auteur, relancés |
| `RAPPORT-CONTROLE-ERRATUM-v0.4.3.md` | donnée hors du fichier | le présent rapport |

La décision sur AE-01 et AE-02, et sur les observations OE-01 à OE-05, revient au propriétaire. MEC-0001 et MEC-0002 restent reportées.
