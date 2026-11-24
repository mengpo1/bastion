# Bastion — Lot 1G-A : inscription de MEC-0004 au registre

**Date :** 24 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1G-A-INSCRIPTION-MEC-0004-transcription.md`, intitulé « BASTION — Mandat d'inscription MEC-0004 v1.2 ». C'est une transcription du message du propriétaire du 2026-11-24T16:42:02Z, extraite mécaniquement du journal de session (SHA-256 `89447962…cb11`) ; son identité avec un fichier original n'est pas vérifiée. Statut du texte : « PRÉPARÉ — exécution non encore autorisée ».
**Autorisation d'exécution :** message du propriétaire du 2026-11-24T17:10:53Z, qui confirme l'exécution de « BASTION — LOT-1G-A v1.0, conformément au mandat transmis précédemment ». Claude Code a considéré que ce nom désigne le mandat d'inscription ci-dessus, le seul mandat transmis.

Conditions de l'autorisation :
- travail exclusivement local, sur une branche dédiée issue de `origin/main` ;
- quatre fichiers documentaires ;
- aucune modification de code, de tests, de CI ni du harnais ;
- aucun commit, push, PR ni fusion ;
- pas d'implémentation du lot 1G.

**Texte inscrit :** le texte consolidé de MEC-0004 v1.2. Il a été transmis par le propriétaire le 2026-11-24T17:15:02Z, en réponse à une question de Claude Code qui signalait que ce texte manquait. Il est reproduit sans modification à l'annexe A (SHA-256 `f81fa456…3695`).
**Base :** `origin/main` = `56fecf3a69c8f342644fbe5568f4be25eb5d3515` (fusion de la PR #24), établie par `git fetch origin main` au démarrage.
**Branche :** `claude/lot-1g-a-inscription-mec-0004`, créée localement à partir de `origin/main`.
**Autorisation de publication :** message du propriétaire du 2026-11-24T17:41:06Z (« BASTION — LOT-1G-A — Autorisation de publication conditionnelle »). Il exige une relecture indépendante des corrections, faite au §6. S'il ne reste aucun constat bloquant, il autorise un seul commit des quatre fichiers, le push de la seule branche du lot et une PR en brouillon vers `main`. La fusion reste interdite.
**État :** inscription faite, relue par deux agents indépendants successifs et vérifiée localement, puis publiée par un commit unique. Ce rapport ne peut pas citer le SHA ni la CI du commit qui le contient : ils sont donnés dans le compte rendu de fin de lot. **Rien n'est fusionné.**

## 1. Résumé

`MEC-0004 — Gestion élémentaire des tours et récupération des ressources` est inscrite à la fin de `docs/gameplay/GAMEPLAY-DECISIONS.md`. Elle porte la classe `MODIFICATION-VALIDEE`, la décision « acceptée » du 23 novembre 2026 avec sa preuve, l'état d'implémentation `non commencé` et les seize tests T01 à T16. L'en-tête du registre annonce désormais quatre fiches.

Les sections 2 à 7 de la fiche reprennent **ligne pour ligne** le texte consolidé de la v1.2 :
- §2, portée des décisions existantes et surcharge ;
- §3, fonctionnement ;
- §4, scénario 4 du prototype Godot ;
- §5, exclusions ;
- §6, tests ;
- §7, architecture.

Une comparaison ordonnée, ligne pour ligne (§4.1), le vérifie. Les seize tests sont identiques et dans le même ordre. Les seules adaptations sont de forme, et elles sont déclarées au §3 et dans la fiche elle-même :
- les niveaux de titres ;
- un en-tête composé du libellé « Fiche de périmètre restreint : », repris de la convention du registre (`MEC-0003`), puis de phrases de la v1.2 mot pour mot ;
- la preuve ajoutée à la ligne « Décision » ;
- le premier mot de cette ligne, « acceptée », écrit à la forme du gabarit.

Cette dernière adaptation vient de la relecture (RI-01) : avec « Acceptée », le contrôle de traçabilité de la CI aurait refusé la fiche lors de la future PR d'implémentation.

**Rien d'autre n'a changé.** Les fiches MEC-0001, MEC-0002 et MEC-0003 du registre sont intactes : la seule ligne modifiée avant MEC-0004 est la phrase d'en-tête. Le code, les tests, la CI, le harnais et les autres registres sont inchangés.

**Relectures indépendantes ciblées :** deux agents distincts et successifs (§6).
- **Première relecture :** « non conforme en l'état », pour un constat bloquant de forme (RI-01). Il a été corrigé, ainsi que les deux constats à corriger (RI-02, RI-03).
- **Seconde relecture,** exigée par le propriétaire sur ces corrections : « conforme sous réserves », sans constat bloquant. Ses réserves (RJ-01 à RJ-03) portent sur l'exactitude de ce rapport ; elles y sont corrigées, sans retouche du registre ni de l'index.

## 2. Fichiers

| Fichier | Changement |
|---|---|
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | phrase d'en-tête (quatre fiches) ; fiche `MEC-0004` ajoutée à la fin (+222 −1, 847 lignes) |
| `docs/mandates/BASTION-MANDAT-LOT-1G-A-INSCRIPTION-MEC-0004-transcription.md` | mandat archivé (transcription, 82 lignes, nouveau) |
| `docs/mandates/README.md` | une ligne d'index : provenance, statut, empreinte (+1) |
| `docs/reviews/LOT-1G-A-INSCRIPTION-MEC-0004.md` | ce rapport, avec le texte v1.2 en annexe A |

Ce sont les quatre fichiers autorisés. Le texte v1.2 et la relecture indépendante, faute de fichier propre, sont reproduits dans ce rapport.

## 3. Méthode d'inscription

La fiche a été construite à partir du texte v1.2, par extraction mécanique (script `…/scratchpad/lot1g-a/`), puis complétée par Claude Code.

| Élément de la fiche | Origine |
|---|---|
| Titre `### MEC-0004 — Gestion élémentaire des tours et récupération des ressources` | titre de niveau 2 de la v1.2, au niveau des autres fiches |
| Phrase d'en-tête en gras | « Fiche de périmètre restreint : », suivi de quatre phrases de la v1.2, mot pour mot : la ligne « Classe » du §1, les deux phrases qui terminent le §2, et la dernière phrase du §8. La première version contenait une paraphrase non déclarée, corrigée après la relecture (RI-02) |
| « Provenance » | ligne de la v1.2, reprise à l'identique |
| « Ce document consolide les règles acceptées… » | phrase de la v1.2, citée entre guillemets, puisque « ce document » ne désigne plus le registre |
| Paragraphe « Adaptations à l'inscription » | rédigé par Claude Code. Il déclare dans la fiche les principales adaptations de forme, et il cite l'étape 4 du §8 (« Autorisation distincte d'implémentation. »), puisque le §8 n'est pas repris |
| Tableau du gabarit | tableau du §1 de la v1.2, ligne pour ligne. Seule la ligne « Décision du propriétaire » change, de deux façons. D'abord, son premier mot est écrit « acceptée » au lieu de « Acceptée », comme dans le gabarit du registre (« acceptée / refusée / reportée ») et dans `MEC-0003` (RI-01). Ensuite, elle est complétée par sa **preuve**, que le registre exige (« explicite, datée et prouvée ») : la réponse « oui » à la question de validation, déclarée au §1 du mandat et dans la v1.2, avec un renvoi à l'annexe A |
| Sections 2 à 7 | §2 à §7 de la v1.2, à l'identique. Seuls les niveaux de titres changent : `##` devient `####`, et `###` devient `#####` |
| §8 de la v1.2 | non repris dans le registre : il décrit les étapes d'autorisation, et non des règles. Il figure à l'annexe A |

Aucune règle n'a été ajoutée, retirée ou reformulée.

**Omissions de forme déclarées ici seulement**, et non dans la fiche (RJ-04) :
- le titre « 1. Fiche du registre » n'est pas repris : le tableau suit directement le titre de la fiche, comme pour `MEC-0003` ;
- les lignes 4 à 6 de la v1.2 (« Statut : ACCEPTÉE… », « Classe… », « État d'implémentation… ») ne sont pas reprises : leur contenu est porté par les lignes « Décision », « Classe » et « État d'implémentation » du tableau ;
- la ligne finale « Fin de la spécification MEC-0004 v1.2 consolidée. » n'est pas reprise ;
- le titre de la v1.2 et son sous-titre sont fusionnés en un seul titre de fiche.

Le paragraphe « Adaptations » dit du §8 qu'il « décrit les étapes d'autorisation ». La formule est un peu étroite : intitulé « Autorisations et étapes », le §8 énumère aussi le développement et la publication.

**MEC-0003 n'est pas modifiée.** Sa fiche dit qu'il n'y a « ni tour, ni récupération, ni surcharge » et les met hors de son périmètre. C'est toujours vrai pour son périmètre. Les tours et la récupération relèvent de `MEC-0004`, une fiche distincte qui, d'après son propre texte, ne modifie pas les règles de marche de `MEC-0003`.

## 4. Vérifications

### 4.1 Conformité au texte v1.2

**Comparaison stricte et ordonnée.** Le script `verifier2.py` (dossier temporaire de la session) remplace le premier contrôle, qui ne testait que la présence des lignes, sans ordre ni emplacement (RI-03). Il sort avec le code 0 si tout est conforme, et 1 sinon.

```
python3 -I verifier2.py mec-0004-v1.2.md docs/gameplay/GAMEPLAY-DECISIONS.md <(git show origin/main:docs/gameplay/GAMEPLAY-DECISIONS.md)
```

```
OK    A. sections 2 à 7 identiques, dans l'ordre (196 lignes de la v1.2, 196 lignes inscrites)
OK    B. tableau identique (13 lignes), sauf la ligne « Décision du propriétaire »
OK    B. ligne « Décision » : texte de la v1.2 (premier mot « acceptée », forme du gabarit) suivi de la seule preuve
OK    C. ligne « Provenance » identique
OK    C. citation littérale
OK    D. en-tête composé de phrases de la v1.2, mot pour mot
OK    E. registre avant MEC-0004 identique à main, sauf les lignes [5]
OK    F. tests T01 à T16 identiques et dans l'ordre
OK    F. valeurs de T01, T02, T03, T06 et T14 recalculées par les formules du §3.1 : T01 (60, 55), T02 (60, 75), T03 (60, 100), T06 (37, 25), T14 (60, 100)
```

Code de sortie : 0.

**Ce que ce script couvre, et ce qu'il ne couvre pas** (seconde relecture, RJ-01 et RJ-02) :
- **Points A à C :** ils comparent mécaniquement les parties **reprises** de la v1.2 : sections 2 à 7, tableau, provenance, citation. Le point B ne vérifie que le **début** de la ligne « Décision » : le texte de la v1.2, puis « Preuve : ».
- **Point D :** il accepte le libellé « Fiche de périmètre restreint : », qui est écrit en dur dans le script.
- **Parties rédigées par Claude Code :** le paragraphe « Adaptations », la phrase qui introduit la citation, et la preuve à la fin de la ligne « Décision ». Aucun contrôle mécanique ne les couvre ; elles ont été vérifiées par lecture, par l'auteur puis par les deux relectures. La seconde relecture a constaté qu'une règle inventée glissée dans ces zones passerait le script (sabotages Sb, Sc et Sd).
- **Second point F :** il recalcule les valeurs attendues de la v1.2 à partir de valeurs recopiées dans le script, sans rien lire dans les fichiers. Il vérifie donc la cohérence interne de ces valeurs, et non leur inscription. Les tests inscrits sont comparés au point F précédent. La seconde relecture a aussi recalculé les valeurs **à partir des lignes du tableau du registre**, avec le même résultat.

**Témoin.** Sur une copie du registre où deux exclusions du §5 sont permutées, le même script affiche « ÉCHEC A. sections 2 à 7 identiques, dans l'ordre » et sort avec le code 1. La comparaison détecte donc un écart d'ordre, que le premier contrôle laissait passer.

**Contrôle de traçabilité de la CI (RI-01).** Deux clones jetables ont été faits, sur la base `56fecf3`. Dans chacun :
1. le registre du lot est commité ;
2. un commit modifie `src/Bastion.Simulation/Movement/MovementModel.cs` ;
3. `bash scripts/harness/check-simulation-trace.sh HEAD~1 description.txt` est lancé, avec la déclaration « Traçabilité simulation : MEC-0004 — essai de reconnaissance de la fiche ».

| Registre | Sortie | Code |
|---|---|---|
| registre du lot (« acceptée ») | « Déclaration MEC-0004 reconnue (fiche présente, décision « acceptée »). » | 0 |
| témoin, avec « Acceptée » | « MEC-0004 : la décision du propriétaire n'est pas « acceptée ». » | 1 |

La future PR d'implémentation pourra donc déclarer `MEC-0004`.

### 4.2 Exigences du mandat

| Exigence du mandat | Emplacement dans la fiche inscrite |
|---|---|
| §2 identifiant `MEC-0004` | titre de la fiche |
| §2 classe `MODIFICATION-VALIDEE` | ligne « Classe » |
| §2 décision acceptée le 23 novembre 2026 | ligne « Décision du propriétaire » (« acceptée le 23 novembre 2026 », forme du gabarit), avec la preuve |
| §2 fonctionnement de référence : ARB-D, Q3.6, Q4.6, aucune fidélité à OXCE | ligne « Fonctionnement de référence et preuves ». La v1.2 cite aussi Q3.14 |
| §2 état d'implémentation `non commencé` | ligne « État d'implémentation » |
| §2 tests T01 à T16, prévus et non exécutés | ligne « Tests de modification » (« non encore implémentés ») et §6 |
| §3 une seule unité, commande explicite de fin de tour | ligne « Description » ; §3.3 ; §5 |
| §3 tour initial numéroté 1 | §3.3, point 1 ; §4, « Configuration » |
| §3 TU 60 et 60, énergie 100 et 20, paramètres configurables | §3.1 |
| §3 TU : addition plafonnée | §3.1 ; §2 (ARB-D) |
| §3 énergie : addition plafonnée, décision nouvelle de MEC-0004 | §3.1 ; §2 (« nouvelle décision de MEC-0004 ») |
| §3 plafonds strictement positifs, récupérations nulles admises, valeurs négatives refusées | §3.2 |
| §3 récupération supérieure au plafond autorisée, état initial au-dessus du plafond refusé | §3.2 |
| §3 aucune fin de tour automatique | §3.3 |
| §3 position et orientation conservées | §3.3, point 6 |
| §3 chemin conservé, dernier résultat remplacé par le compte rendu de fin de tour | §3.4 ; §4, « Affichage » |
| §3 surcharge exclue, facteur neutre égal à 1 (Q3.14) | §2, « Surcharge » ; §5 |
| §3 scénario 4 : touches 4 (AZERTY compris), T et R ; 12 TU et 35 d'énergie ; scénarios 1 à 3 inchangés | §4 |
| §3 exclusions, architecture, seize tests | §5, §7, §6 |
| §3 « Ne pas inventer de règles complémentaires » | §4.1, points A à D, pour les parties reprises ; lecture par l'auteur et les deux relectures, pour les parties rédigées (paragraphe « Adaptations », preuve) |
| §4 MEC-0001, MEC-0002 et MEC-0003 non modifiées | §4.1, point E |
| §4 ni simulation, ni client, ni tests, ni code, ni CI, ni harnais | §4.3 |
| §5 en-tête du registre : quatre fiches | ligne 5 du registre |
| §5 rapport et archivage du mandat | ce rapport ; transcription et index |

### 4.3 Périmètre et non-régression

Les commandes ont été lancées dans le dépôt de travail et renvoient toutes le code 0.

| Commande | Résultat |
|---|---|
| `git diff --stat origin/main -- src tests .github scripts .claude CLAUDE.md Bastion.slnx docs/decisions docs/references` | aucune sortie |
| `git status --short` | les trois fichiers attendus, avant la rédaction de ce rapport ; les quatre fichiers du lot ensuite |
| `dotnet restore` puis `dotnet build --no-restore --configuration Release` | 0 Warning(s), 0 Error(s) |
| `dotnet test --no-build --configuration Release` | « Passed! - Failed: 0, Passed: 46, Skipped: 0, Total: 46 » |
| `dotnet format --verify-no-changes --no-restore` | aucune sortie |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |

Le lot ne modifie que de la documentation. Ces commandes montrent seulement que le dépôt reste sain ; elles ne vérifient pas l'inscription.

## 5. Limites

- **Validation du propriétaire :** la réponse « oui » à « Validez-vous MEC-0004 v1.2 dans son ensemble ? » a été donnée hors de cette conversation. Elle est déclarée par le mandat (§1) et par le texte v1.2 ; l'échange d'origine n'est pas dans le dépôt et n'a pas été vérifié.
- **Texte v1.2 :** sa source est le message du propriétaire du 24 novembre 2026 (17:15:02 UTC). Son identité avec le document validé par le propriétaire n'est pas vérifiable ici.
- **Rendu du registre :** le Markdown n'a pas été rendu sur GitHub.
- **Nom du mandat :** l'autorisation parle de « LOT-1G-A v1.0 », le texte reçu s'intitule « BASTION — Mandat d'inscription MEC-0004 v1.2 ». Claude Code les a considérés comme un seul et même mandat, le seul transmis.
- **Casse de « acceptée » :** l'inscription écrit « acceptée » là où la v1.2 et le mandat écrivent « Acceptée ». Ce n'est pas un changement de fond, et c'est la forme du gabarit, que le mandat demande de respecter. C'est tout de même un écart littéral au texte validé (§7).

## 6. Relecture indépendante ciblée

Un agent distinct de l'auteur a relu les quatre fichiers avant les corrections. Son rapport est reproduit ci-dessous sans modification, entre deux filets.

---

### Relecture indépendante ciblée du lot 1G-A : inscription de MEC-0004

**Date :** 24 novembre 2026
**Objet :** l'inscription de MEC-0004 v1.2 au registre, l'archivage du mandat et le rapport d'inscription.
**État relu :** branche locale `claude/lot-1g-a-inscription-mec-0004`, `HEAD` = `origin/main` = `56fecf3a69c8f342644fbe5568f4be25eb5d3515`, rien de commité. Deux fichiers modifiés : `docs/gameplay/GAMEPLAY-DECISIONS.md` (SHA-256 `f9e09181…a46`) et `docs/mandates/README.md` (`7965facf…a76`). Deux fichiers non suivis : la transcription du mandat (`89447962…b11`) et `docs/reviews/LOT-1G-A-INSCRIPTION-MEC-0004.md` (`e803c850…0e4`, avant l'ajout de cette section).
**Relecteur :** agent distinct de l'auteur. Je n'ai rien modifié dans le dépôt (`/home/user/bastion`). Les sabotages et les compilations ont été faits sur des copies jetables, sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g-a/`.

### Méthode

**Lectures (inspecté seulement)**
- `CLAUDE.md` et le mandat transcrit en entier.
- L'autorisation et le texte v1.2 du dossier `lot1g-a`.
- Le gabarit et les fiches MEC-0001 à MEC-0003 du registre : ARB-D l. 124, Q3.6 l. 213, Q4.6 l. 214, Q3.14 l. 216, MEC-0001 « Encore ouvert » l. 240-262, MEC-0003 l. 444-626.
- Le §3 de `BASTION-MANDAT-LOT-0C-v1.2.md` et l'index `docs/mandates/README.md`.
- Le script `verifier.py` et son journal.
- `scripts/harness/check-simulation-trace.sh`, `scripts/harness/README.md` et `.github/workflows/ci.yml`.

**Exécuté et réussi**
- **État du dépôt :** `git status --porcelain`, avant et après la relecture, est identique (2 `M`, 2 `??`). `git ls-remote origin refs/heads/main` renvoie `56fecf3a…`, la base est donc à jour.
- **Taille du diff :** `git diff --numstat origin/main` donne `222 1` pour le registre et `1 0` pour l'index. `wc -l` donne 847 lignes pour le registre (626 sur `main`) et 82 pour la transcription. Les chiffres du rapport (§2) sont exacts.
- **Hors périmètre :** `git diff --stat origin/main -- src tests .github scripts .claude CLAUDE.md Bastion.slnx docs/decisions docs/references` ne produit aucune sortie (code 0).
- **Registre avant la fiche :** `diff` entre le registre de `main` et les 626 premières lignes du registre : seule la ligne 5 (phrase d'en-tête) diffère. La ligne 627 est vide. MEC-0001 à MEC-0003 sont intactes.
- **§2 à §7, comparaison stricte :**
  - extraction des lignes 28-223 de la v1.2, titres abaissés de deux niveaux (`sed -E 's/^(#+ )/##\1/'`) ;
  - `cmp` avec les lignes 652-847 du registre : **code 0**, 196 lignes de part et d'autre ;
  - le `diff` brut ne montre que 14 lignes de titres (`##`→`####`, `###`→`#####`).
- **Tableau du §1 :** v1.2 l. 14-26 contre registre l. 638-650. Seule la ligne « Décision du propriétaire » diffère. La ligne inscrite reprend celle de la v1.2 mot pour mot, puis lui ajoute « Preuve : … L'échange d'origine n'est pas dans le dépôt. ».
- **Provenance et citation :** la provenance (v1.2 l. 8 contre registre l. 632) est identique au `cmp` (code 0). La citation « Ce document consolide… » (l. 634) est littérale.
- **Annexe A :** extraite du rapport, elle est identique au `cmp` (code 0) au fichier `lot1g-a/mec-0004-v1.2.md`, y compris les deux espaces de fin de ligne des l. 4 et 5. Empreinte commune : `f81fa456…3695`.
- **Empreintes :** celle de la transcription (`89447962…cb11`) est égale à celle de `lot1g-a/mandat.md` (`cmp` code 0) et à celle de l'index. Les quatre empreintes de l'annexe B sont recalculées et exactes.
- **Harnais :** `bash scripts/harness/test-hooks.sh` se termine avec le code 0, sur « == 75 tests, 0 échec(s) == ».
- **Compilation et tests, sur une copie de l'arbre de travail :**
  - `dotnet build --configuration Release` : 0 Warning(s), 0 Error(s), code 0 ;
  - `dotnet test --no-build --configuration Release` : « Passed! - Failed: 0, Passed: 46 », code 0 ;
  - `dotnet format --verify-no-changes --no-restore` : code 0.
- **Contrôle CI « Traçabilité simulation », sur une copie :** voir RI-01.
- **Sabotages S1 à S4 de `verifier.py`, sur des copies du registre :** voir RI-03.

**Exécuté et échoué**
- La lecture du journal de session, pour contrôler les messages du propriétaire, a été refusée par le système de permissions.

### Constats

**RI-01 — bloquant. La décision de MEC-0004 n'est pas reconnue comme « acceptée » par la CI.**
- **Emplacement :** `docs/gameplay/GAMEPLAY-DECISIONS.md:645`. La cellule commence par « Acceptée », avec une majuscule.
- **Règle du contrôle :** `scripts/harness/check-simulation-trace.sh:58` exige, en tenant compte de la casse, `^[[:space:]]*acceptée`. Le contrôle est appelé par `.github/workflows/ci.yml:52` sur toute PR qui touche `src/Bastion.Simulation/`.
- **Conventions du registre :** le gabarit (l. 37) écrit « acceptée / refusée / reportée », MEC-0003 (l. 455) écrit « acceptée — », et `scripts/harness/README.md:31` décrit la même règle.
- **Preuve (copie jetable) :** une base est commitée, puis un commit modifie `MovementModel.cs`, et `check-simulation-trace.sh` est lancé.
  - Déclaration « MEC-0004 » : « MEC-0004 : la décision du propriétaire n'est pas « acceptée ». », code 1.
  - Déclaration « MEC-0003 » : reconnue, code 0.
  - Témoin : même registre, avec la seule casse de « acceptée » changée. MEC-0004 est reconnue, code 0.
- **Consequence :** la PR d'implémentation du lot 1G, qui devra déclarer MEC-0004, échouera en CI. Après le commit, corriger ce défaut demandera :
  - soit de modifier une décision du registre, ce qui exige une validation explicite (`CLAUDE.md` §3) ;
  - soit de modifier le harnais, ce qui exige un mandat distinct (`CLAUDE.md` §8).
- **Pourquoi personne ne l'a vu :** la majuscule vient fidèlement de la v1.2 (§1) et du mandat (§2). Ni `verifier.py` ni `test-hooks.sh` ne l'ont détectée.
- **Correction suggérée, avant le commit :**
  - mettre le premier mot de la cellule à la forme du gabarit (« acceptée ») ;
  - déclarer cette adaptation de forme, au même titre que l'ajout de la preuve (registre l. 636 et §3 du rapport) ;
  - mettre à jour l'annexe B.
  - Le fond de la v1.2 n'est pas touché. Le propriétaire peut arbitrer s'il tient à la casse littérale.

**RI-02 — à corriger. La phrase d'en-tête contient une paraphrase non déclarée.**
- **Emplacement :** `docs/gameplay/GAMEPLAY-DECISIONS.md:630`. Le membre « et seulement sous un mandat d'implémentation distinct » ne figure pas dans la v1.2.
- **Preuve :** recherché dans la v1.2, ce membre est absent. Les seules sources proches sont l. 213 (« futur mandat d'implémentation ») et l. 233-234 (« Préparation du mandat d'implémentation LOT-1G. » ; « Autorisation distincte d'implémentation. »).
- **Ce qui est inexact :**
  - la paraphrase perd la notion d'« autorisation distincte » ;
  - le rapport (l. 55) affirme que l'en-tête « ne fait que reprendre la v1.2 » : périmètre, statuts et dernière phrase du §8 ;
  - la ligne 636 du registre ne déclare que la reprise de cette dernière phrase.
- **Consequence :** aucune règle de gameplay n'est créée, mais le registre protégé porte une reformulation du processus qui n'est pas déclarée.
- **Correction suggérée :** citer littéralement l'étape 4 du §8, ou bien déclarer la paraphrase à la ligne 636 et au §3 du rapport.

**RI-03 — à corriger. La preuve citée par le rapport est plus faible que sa conclusion.**
- **Emplacement :** le rapport écrit « ligne pour ligne » (l. 23) puis « Un contrôle mécanique (§4) le vérifie » (l. 31). Il présente aussi les points 1 et 2 du §4.1 comme la preuve de « Ne pas inventer de règles complémentaires » (l. 125).
- **Pourquoi le script ne l'établit pas :** `verifier.py:10` et `:15` testent seulement la présence de chaque ligne, sans ordre ni emplacement. La comparaison se fait contre toute la v1.2, en-tête et §8 compris, après suppression des `#` et des lignes vides. Son point 4 affiche « fin identique : None ». Cette expression ne peut afficher que `True` ou `None`.
- **Preuve (sabotages S1 à S4, sur des copies du registre) :**
  - S1 : deux exclusions du §5 permutées ;
  - S2 : « récupération conditionnelle au repos » déplacée du §5 (exclusions) au §3.2 (règles) ;
  - S3 : « 4. Autorisation distincte d'implémentation. » insérée au §3.3 ;
  - S4 : une règle transformée en titre.
  - Résultat : pour les quatre, la sortie de `verifier.py` est identique à celle du registre réel (« 2 », « 5 », « True »). Ma comparaison stricte les détecte toutes (`cmp` code 1) et vaut 0 sur le registre réel.
- **Consequence :** la conclusion est vraie, et ma comparaison l'établit. Mais la preuve citée par le rapport ne l'établit pas.
- **Correction suggérée :** citer une comparaison ordonnée octet pour octet, comme celle de la Méthode.

**RI-04 — observation. Le §8 de la v1.2 n'est pas repris dans le registre.**
- Ce choix est légitime à mes yeux :
  - le §8 décrit des étapes, pas des règles ;
  - le §3 du mandat ne le compte pas parmi les éléments à reprendre ;
  - l'omission est déclarée (l. 636) ;
  - le texte est conservé à l'identique à l'annexe A.
- Le texte validé complet ne vit donc que dans un rapport, et le §7 du rapport ne soumet pas ce choix au propriétaire.

**RI-05 — observation. Cohérence interne : aucune contradiction de règle.**
- **Avec MEC-0003 :**
  - les exclusions « ni tour, ni récupération, ni surcharge » (l. 479, A4 (f) l. 530, l. 580) bornent le périmètre de MEC-0003 ;
  - MEC-0004 dit la laisser inchangée (l. 644, 673, 807) ;
  - en revanche, la phrase de MEC-0003 « Ces sujets restent régis par `MEC-0001` et `MEC-0002` » (l. 575) devient en partie dépassée, sans renvoi croisé. L'ajouter est interdit par le §4 du mandat, et c'est un sujet possible pour le propriétaire.
- **Avec les sous-décisions de MEC-0001 :**
  - les renvois (l. 658-661) correspondent bien à ARB-D, Q3.6, Q4.6 et Q3.14 ;
  - la formule de récupération de l'énergie est bien nouvelle : MEC-0001 n'en fixe aucune (ARB-D : « L'énergie est récupérée séparément » ; Q3.6 ; l. 254) ;
  - Q4.6 est de niveau [CIT], ses valeurs de niveau [DÉC], « confirmés par ailleurs » (l. 155). MEC-0004 ne le mentionne pas, mais n'utilise que les valeurs.
- **Statut reporté de MEC-0001 et MEC-0002 :** il est cohérent (l. 5, 60, 673).

**RI-06 — observation. Le traitement du nom du mandat est honnête.**
- L'index (`docs/mandates/README.md:31`) et le rapport (l. 5 et 151) déclarent les deux noms et l'interprétation retenue.
- Le nom de fichier n'a pas de version, contrairement aux transcriptions précédentes (`-v1.0-transcription`).
- Le titre cité dans l'index omet le préfixe « BASTION — » de la ligne 1 de la transcription.
- La ligne d'index respecte le protocole du §3 du LOT-0C : provenance « transcription… identité… non vérifiée », statut, autorisation, empreinte exacte.

**RI-07 — observation. Les quatre fichiers dépendent les uns des autres.**
- La ligne 645 du registre renvoie à la transcription et à l'annexe A du rapport, deux fichiers non suivis : les quatre fichiers doivent être commités ensemble.
- L'empreinte du registre dans l'annexe B changera si RI-01 ou RI-02 sont corrigés.

### Ce que je n'ai pas pu vérifier

- **Messages du propriétaire (non vérifié) :** ceux de 16:42:02, 17:10:53 et 17:15:02 UTC, l'identité de la transcription et du texte v1.2 avec ces messages, et l'affirmation « seul mandat transmis ». L'accès au journal de session m'a été refusé.
- **Validation « oui » du 23 novembre 2026 :** absente du dépôt, donc non vérifiée.
- **`git fetch origin main` au démarrage :** non vérifié. Le reflog n'a aucune entrée le 24 novembre, ce qui est compatible avec un fetch sans effet. La base est confirmée à jour par `ls-remote`.
- **Rendu GitHub du Markdown :** non vérifié (titres de niveau 5, tableaux).
- **Compilation et tests :** ils ont été exécutés sur une copie de l'arbre de travail, pas dans le dépôt lui-même.

### Verdict

**Non conforme en l'état**, à cause d'un seul constat bloquant, de forme : RI-01.

Sur le fond, l'inscription est fidèle :
- les §2 à §7 sont identiques octet pour octet à la v1.2, aux niveaux de titres près ;
- le tableau est fidèle, et sa seule ligne complétée est déclarée ;
- les seize tests sont identiques ;
- MEC-0001 à MEC-0003 sont intactes ;
- rien n'a changé hors des quatre fichiers ;
- l'archivage et les empreintes sont exacts ;
- l'annexe A est exacte.

Une fois RI-01 corrigé (et de préférence RI-02 et RI-03), l'état relevé justifierait au mieux « conforme sous réserves ». Ce n'est qu'une appréciation : je ne m'accorde pas la validation finale.

---

**Traitement des constats :**

| Constat | Classement | Traitement |
|---|---|---|
| RI-01 : avec « Acceptée », la décision n'était pas reconnue par le contrôle de traçabilité de la CI | bloquant | **Corrigé.** Le premier mot est écrit « acceptée », à la forme du gabarit, et l'adaptation est déclarée dans la fiche et au §3. Le contrôle réel de la CI reconnaît désormais `MEC-0004`, et le témoin avec « Acceptée » est refusé (§4.1). |
| RI-02 : la phrase d'en-tête contenait une paraphrase non déclarée (« et seulement sous un mandat d'implémentation distinct ») | à corriger | **Corrigé.** Hormis le libellé « Fiche de périmètre restreint : », convention du registre (RJ-03), l'en-tête ne contient plus que des phrases de la v1.2, mot pour mot (point D du §4.1). Le paragraphe « Adaptations à l'inscription » cite l'étape 4 du §8. |
| RI-03 : la preuve citée (un contrôle de présence, sans ordre) était plus faible que la conclusion | à corriger | **Corrigé.** Une comparaison stricte et ordonnée remplace ce contrôle ; un témoin vérifie qu'elle détecte une permutation (§4.1). |
| RI-04 : le §8 de la v1.2 ne figure que dans ce rapport | observation | **Non modifié.** Choix déclaré dans la fiche ; soumis au propriétaire au §7. |
| RI-05 : la phrase de `MEC-0003` « Ces sujets restent régis par `MEC-0001` et `MEC-0002` » devient en partie dépassée pour les tours et la récupération | observation | **Non modifié** : le §4 du mandat interdit de modifier `MEC-0003`. Soumis au propriétaire au §7. |
| RI-06 : traitement honnête du nom du mandat ; titre cité sans « BASTION — » | observation | **Corrigé** : l'index cite le titre complet. Le nom de fichier sans version est conservé. |
| RI-07 : les quatre fichiers dépendent les uns des autres | observation | **Pris en compte** : ils devront être commités ensemble ; l'annexe B est recalculée. |

Après ces corrections, les contrôles du §4 ont été relancés, tous avec le code 0 :
- comparaison stricte ;
- contrôle de traçabilité ;
- `git diff --stat` hors périmètre, sans sortie ;
- compilation, 46 tests, format, et 75 tests des hooks.

### Seconde relecture, exigée avant publication

Le propriétaire a exigé de faire relire les corrections RI-01, RI-02, RI-03 et RI-06, et le traitement de RI-04 à RI-07 (message de 17:41:06 UTC). Un second agent, ni auteur de l'inscription ni auteur de la première relecture, a relu l'état corrigé. Son rapport est reproduit ci-dessous sans modification, entre deux filets.

Les numéros de ligne qu'il cite renvoient au rapport tel qu'il l'a relu, avant l'insertion de son propre texte et les corrections ci-dessous.

---

### Seconde relecture indépendante ciblée du lot 1G-A : corrections après la première relecture

**Date :** 24 novembre 2026
**Objet :** vérifier les corrections RI-01, RI-02, RI-03 et RI-06, et le traitement des observations RI-04 à RI-07. Quatre points demandés : l'inscription de MEC-0004 v1.2 comme décision « acceptée » en minuscule ; la fidélité intégrale des règles et des tests T01 à T16 au texte v1.2 ; MEC-0001 à MEC-0003 inchangées ; un périmètre de quatre fichiers.
**État relu :** branche locale `claude/lot-1g-a-inscription-mec-0004`, `HEAD` = `origin/main` = `56fecf3a69c8f342644fbe5568f4be25eb5d3515` (confirmé par `git ls-remote origin refs/heads/main`), rien de commité. Empreintes SHA-256 :
- `docs/gameplay/GAMEPLAY-DECISIONS.md` : `7993e0c9…ba24` ;
- `docs/mandates/README.md` : `668fd8ee…69e0` ;
- `docs/mandates/BASTION-MANDAT-LOT-1G-A-INSCRIPTION-MEC-0004-transcription.md` : `89447962…cb11` ;
- `docs/reviews/LOT-1G-A-INSCRIPTION-MEC-0004.md` : `c0fcc699…2c2c`, avant l'ajout de cette section ;
- texte v1.2 (`lot1g-a/mec-0004-v1.2.md`) : `f81fa456…3695`.

**Relecteur :** agent distinct de l'auteur de l'inscription et du premier relecteur. Je n'ai rien modifié dans le dépôt. Les copies, les clones et les sabotages sont sous `/tmp/claude-0/-home-user/7361641c-6eb6-5649-a764-279757212cf3/scratchpad/relecture-1g-a-bis/`.

#### Méthode

**Exécuté et réussi**
- **Sections 2 à 7, avec ma propre comparaison** (je n'ai pas réutilisé le script de l'auteur) :
  - méthode : v1.2 l. 28-223, titres abaissés par `sed -E 's/^(#+ )/##\1/'`, comparés par `cmp` aux lignes 652-847 du registre ;
  - résultat : **code 0**, 196 lignes de chaque côté ;
  - le `diff` brut ne trouve que les 14 titres : 6 `##`→`####` et 8 `###`→`#####` ;
  - rien après la l. 847, et le fichier finit par un saut de ligne.
- **Tableau du §1 :** `diff` entre la v1.2 l. 14-26 et le registre l. 638-650. Une seule ligne diffère, la l. 645 (« Décision du propriétaire ») :
  - dans la partie commune, seul le caractère n° 1 de la cellule change (`'A'`→`'a'`) ;
  - le reste est un ajout final, « Preuve : … L'échange d'origine n'est pas dans le dépôt. » ;
  - la ligne compte 3 `|`, donc aucune cellule parasite ;
  - `od -c` montre une cellule qui commence par « ␠acceptée ».
- **Provenance :** `cmp` entre la v1.2 l. 8 et le registre l. 632 donne le code 0. La citation de la l. 634 est littérale (v1.2 l. 10).
- **En-tête en gras (l. 630) :** les quatre phrases sont présentes mot pour mot dans la v1.2. Ce sont la l. 18 (cellule « Classe »), la l. 49 (deux phrases) et la l. 238. Une fois ces phrases et « Fiche de périmètre restreint : » retirées, il ne reste rien (`''`). Le libellé « Fiche de périmètre restreint » est absent de la v1.2 (voir RJ-03).
- **Les seize tests :** ils sont identiques et dans l'ordre (inclus dans le `cmp`). J'ai recalculé T01, T02, T03, T06 et T14 en lisant les lignes du tableau du registre, et non des valeurs recopiées à la main. Résultat : (60, 55), (60, 75), (60, 100), (37, 25) et (60, 100), tous cohérents avec les formules du §3.1.
- **MEC-0001 à MEC-0003 :** j'ai comparé avec `diff` le registre de `main` (626 lignes) et les 626 premières lignes du registre. Seule la l. 5 diffère, et la l. 627 est vide. `git diff --numstat origin/main` donne `222 1` pour le registre et `1 0` pour l'index.
- **Périmètre :**
  - `git diff --stat origin/main -- src tests .github scripts .claude CLAUDE.md Bastion.slnx docs/decisions docs/references` : aucune sortie, code 0 ;
  - `git status --porcelain -uall` : exactement 4 entrées (2 `M`, 2 `??`) ;
  - `git ls-files --others --exclude-standard` : les deux fichiers non suivis du lot, et rien d'autre.
- **Contrôle de traçabilité de la CI, rejoué** dans deux clones jetables (`git clone --no-local`, base `56fecf3`) :
  - dans chaque clone, un premier commit porte le registre, puis un second ajoute une ligne à `src/Bastion.Simulation/Movement/MovementModel.cs` ;
  - la commande est `bash scripts/harness/check-simulation-trace.sh HEAD~1 <description>`, avec la déclaration « Traçabilité simulation : MEC-0004 — essai ».

| Registre | MEC-0004 | MEC-0003 (non-régression) | MEC-0001 (reportée) |
|---|---|---|---|
| registre du lot (« acceptée ») | **code 0**, « Déclaration MEC-0004 reconnue (fiche présente, décision « acceptée »). » | code 0 | code 1 |
| témoin, seule la l. 645 remise à « Acceptée » | **code 1**, « MEC-0004 : la décision du propriétaire n'est pas « acceptée ». » | code 0 | code 1 |

  Avec la base `56fecf3` (l'équivalent de `HEAD^1` en CI) et le registre du lot, le code est aussi 0. Les clones `trace-minuscule` et `trace-majuscule` de l'auteur sont conformes à sa description : leurs registres ne diffèrent de celui du lot qu'à la l. 645 pour le témoin, et sont identiques pour l'autre.
- **`verifier2.py` rejoué** (copie de même empreinte) : sortie identique, octet pour octet, à `verifier2.log` et au bloc des l. 84-92 du rapport ; code 0. Le témoin de l'auteur, qui permute les l. 798 et 799, donne « ÉCHEC A. » et le code 1.
- **Annexe A :** extraite entre les balises `~~~~`, elle est identique au fichier v1.2 (`cmp` code 0, même empreinte `f81fa456…`, deux fins de ligne à deux espaces conservées).
- **Annexe B :** les six empreintes sont recalculées et toutes exactes (registre `36b5ac5b…` / `7993e0c9…`, index `0e1d27ab…` / `668fd8ee…`, transcription `89447962…`, v1.2 `f81fa456…`). L'empreinte de la transcription est aussi celle de l'index (README:31).
- **Messages du propriétaire, dans le journal de session** (`/root/.claude/projects/-home-user/7361641c-6eb6-5649-a764-279757212cf3.jsonl`). J'ai pu le lire, alors que la première relecture n'y avait pas eu accès :
  - message de 2026-11-24T16:42:02.014Z : la transcription est égale à ce message suivi d'un saut de ligne (`True`) ;
  - message de 17:10:53.018Z : `autorisation.md` est égal au message, au saut de ligne final près ;
  - réponse de 17:15:02.249Z, à une question de Claude Code qui signalait l'absence de la v1.2 : le texte v1.2 est égal à cette réponse suivie d'un saut de ligne (`True`) ;
  - le 24 novembre, c'est le seul mandat reçu avant l'autorisation.
- **§6, copie de la première relecture :** les l. 169-302 du rapport sont égales à `lot1g-a/relecture-1.md`. Ce fichier est égal au rapport de l'agent reçu à 17:26:46Z dans le journal, une fois retirés l'indentation de deux espaces du cadre de transmission et les espaces de fin de ligne (`diff` code 0).
- **Non-régression :**
  - `bash scripts/harness/test-hooks.sh` : code 0, « == 75 tests, 0 échec(s) == » ;
  - `git status --porcelain=v1 -uall` est identique avant et après ma relecture (`diff` code 0) ;
  - `sha256sum -c` sur les quatre fichiers donne OK.

**Exécuté : sabotages de `verifier2.py`, sur des copies du registre**

| Sabotage | Code | Détecté ? |
|---|---|---|
| Se : T01 « 56 énergie » dans le registre seul | 1 (ÉCHEC A, ÉCHEC F tests) | oui |
| Sg : « Acceptée » restauré à la l. 645 | 1 (ÉCHEC B) | oui |
| Sh : en-tête l. 630 modifié | 1 (ÉCHEC D) | oui |
| Sb : la ligne « Une fin de tour automatique est introduite après 30 secondes. » insérée après la l. 636 | **0**, aucun échec | **non** |
| Sc : « La récupération est doublée au tour 1. » ajoutée après la preuve de la l. 645 | **0**, aucun échec | **non** |
| Sd : à la l. 636, « sans changement de fond, sauf que la touche T termine aussi le tour dans les scénarios 1 à 3 : » | **0**, aucun échec | **non** |
| Sf : T01 « 56 énergie » dans la v1.2 et dans le registre | **0** ; la ligne « OK F. valeurs … T01 (60, 55) » reste affichée | **non** |

**Inspecté seulement**
- Le mandat, l'autorisation du 24 novembre à 17:10:53, et l'autorisation de publication conditionnelle de 17:41:06Z (dans le journal).
- `check-simulation-trace.sh` et `ci.yml:49-52`.
- Le gabarit (l. 37) et la ligne « Décision » de MEC-0003 (l. 455, « acceptée — »).
- MEC-0003, l. 446, 479 et 575.
- Le paragraphe « Adaptations » (l. 636) et la preuve de la l. 645 : je les ai lus. Ils ne contiennent aucune règle de gameplay.
- Le rapport en entier.

#### Constats

**RJ-01 — à corriger. La comparaison stricte ne couvre pas le texte rédigé par Claude Code, contrairement à ce que dit le rapport.**
- **Emplacement :** rapport l. 134 (« §3 « Ne pas inventer de règles complémentaires » | §4.1, comparaison stricte, points A à D ») et l. 86 (« suivi de la seule preuve ») ; traitement de RI-03, l. 312. Côté script : `verifier2.py:28` vérifie seulement `startswith(attendu + " Preuve : ")`, et aucun point ne lit les l. 634 à 637, sauf la citation, recherchée par simple inclusion.
- **Preuve :** les sabotages Sb, Sc et Sd ajoutent une règle inventée dans le paragraphe « Adaptations », dans la preuve, ou entre ce paragraphe et le tableau. Tous sortent avec le code 0 et neuf « OK ».
- **Conséquence :** dans l'état actuel, la conclusion est vraie, d'après ma lecture et ma propre comparaison. Mais les seules parties écrites par l'auteur (l. 634, 636 et la fin de la l. 645) ne sont couvertes par aucune preuve mécanique. C'est le même écart, en plus étroit, que celui de RI-03.
- **Correction suggérée :** au §4.1 et au §4.2, dire que ces zones ont été vérifiées par lecture (ou par la présente relecture), et non par les points A à D.

**RJ-02 — à corriger. Le second point F ne peut pas échouer.**
- **Emplacement :** `verifier2.py:48-51` ; rapport l. 92.
- **Preuve :** les valeurs attendues sont écrites en dur dans le script, et rien n'est lu dans les fichiers. Avec Sf, la ligne « OK F. valeurs de T01… : T01 (60, 55) » s'affiche alors que les deux fichiers portent 56.
- **Conséquence :** la ligne présente comme une vérification de l'inscription un calcul indépendant de ses entrées. La cohérence des valeurs est réelle : je l'ai recalculée à partir des lignes du registre (voir Méthode).
- **Correction suggérée :** décrire ce point comme une vérification de la cohérence interne de la v1.2, faite sur des valeurs recopiées, ou citer un recalcul qui lit le tableau.

**RJ-03 — à corriger. L'en-tête contient un libellé qui n'appartient pas à la v1.2, et deux phrases du rapport disent le contraire.**
- **Emplacement :** registre l. 630, « Fiche de périmètre restreint : ».
  - Ce libellé est absent de la v1.2 (`"Fiche de périmètre" in v1.2` → `False`). C'est une convention du registre (MEC-0003, l. 446).
  - Le §3 du rapport (l. 61) le déclare.
  - En revanche, le rapport écrit ailleurs : « un en-tête composé de phrases de la v1.2 » (l. 33) et « L'en-tête ne contient plus que des phrases de la v1.2, mot pour mot » (l. 311, traitement de RI-02). La l. 636 du registre dit aussi seulement « assemble des phrases de ce texte ».
  - Le point D (`verifier2.py:39`) accepte ce libellé parce qu'il est écrit en dur dans le script.
- **Conséquence :** aucune règle n'est ajoutée, et le sens est celui de la cellule « Classe ». Mais l'affirmation de correction de RI-02 est littéralement inexacte, et l'auto-description de la fiche dans le registre protégé est incomplète.
- **Correction suggérée :** au minimum, rectifier les l. 33 et 311 du rapport. Déclarer le libellé à la l. 636 changerait l'empreinte du registre, donc l'annexe B, et demanderait une nouvelle vérification.

**RJ-04 — observation. D'autres omissions de forme ne sont pas déclarées dans la fiche.**
- Ces omissions sont :
  - les l. 4-6 de la v1.2 (« Statut : ACCEPTÉE… », « Classe », « État d'implémentation »), non déclarées nulle part ;
  - la l. 240, « Fin de la spécification… », non déclarée nulle part ;
  - le titre « 1. Fiche du registre », déclaré seulement au rapport, l. 69 ;
  - la fusion des deux titres, déclarée seulement au rapport, l. 60.
- Le rapport affirme pourtant que le paragraphe « Adaptations » déclare « toutes les adaptations de forme » (l. 64).
- « qui décrit les étapes d'autorisation » (l. 636) est une caractérisation légère : le §8 s'intitule « Autorisations et étapes », et ses étapes comprennent aussi le développement et la publication.
- **Conséquence :** aucune règle n'est perdue. Le contenu des l. 4-6 est porté par les lignes « Classe », « État » et « Décision » du tableau.

**RJ-05 — observation. Le titre du mandat reste tronqué dans le rapport.**
- RI-06 est bien corrigé dans l'index : README:31 cite « BASTION — Mandat d'inscription MEC-0004 v1.2 ».
- Le rapport cite pourtant encore « Mandat d'inscription MEC-0004 v1.2 » à la l. 4, alors que la l. 160 cite le titre complet.
- Le traitement de RI-06 (l. 315), qui ne vise que l'index, est exact.

**RJ-06 — observation. Ce qui deviendra faux après l'intégration de cette relecture, ou après la publication.**
- Les affirmations suivantes deviendront fausses :
  - l. 324, « Les corrections n'ont pas été relues par un second agent indépendant. » ;
  - l. 41 et l. 165, qui ne mentionnent qu'une relecture ;
  - l. 17, « Rien n'est commité ni publié », après la publication ;
  - §7, point 1 (l. 328), « Elle demande une autorisation distincte » : l'autorisation de publication conditionnelle du propriétaire (2026-11-24T17:41:06Z) existe déjà. Elle n'est citée ni dans l'en-tête du rapport (l. 5-12), ni dans l'index (README:31, « sans commit, push, PR ni fusion »).
- Les limites du §5 (l. 157-158) restent vraies. En revanche, la non-vérification des messages du propriétaire relevée par la première relecture (l. 283) est désormais levée par la présente relecture : voir Méthode.
- **Annexe B :** aucune valeur ne dépend de l'ajout de ce texte, car l'annexe ne porte pas l'empreinte du rapport. Elle restera exacte tant que le registre, l'index et la transcription restent intacts. Toute retouche de l'un d'eux, par exemple pour RJ-03 ou pour citer l'autorisation dans l'index, la rendra fausse.
- Les numéros de ligne cités dans cette relecture renvoient à l'état relu ; l'insertion de ce texte au §6 les décalera pour le rapport (l. 324 et suivantes).

**Pas de constat sur RI-01, RI-04, RI-05 et RI-07.**
- RI-01 est corrigé et vérifié par le contrôle réel de la CI (tableau ci-dessus).
- RI-04 et RI-05 sont bien soumis au propriétaire (§7, points 3 et 4).
- RI-07 est traité : l'annexe B est exacte.

#### Ce que je n'ai pas pu vérifier

- **La réponse « oui » du 23 novembre 2026 (non vérifié) :** la question « Validez-vous MEC-0004 » n'apparaît dans le journal qu'à partir du mandat du 24 novembre, à 16:42:02. Cela concorde avec la mention « hors de cette conversation » (§5), sans la prouver.
- **Le texte v1.2 transmis et le document validé le 23 novembre (non vérifié) :** leur identité ne peut pas être établie, faute du document validé.
- **Compilation, 46 tests et format (non vérifié par moi) :** `dotnet build`, `dotnet test` et `dotnet format` n'ont pas été rejoués. Le lot ne touche aucun code.
- **Rendu GitHub (non vérifié) :** titres de niveaux 4 et 5, tableaux.

#### Verdict

**Conforme sous réserves.**

Les quatre points exigés par le propriétaire sont établis par des commandes exécutées :
- **« acceptée » en minuscule :** la cellule commence par « acceptée » ; la CI réelle la reconnaît (code 0), et le témoin « Acceptée » est refusé (code 1) ;
- **fidélité :** les §2 à §7 et les seize tests sont identiques octet pour octet à la v1.2, aux titres près ; le tableau n'en diffère que par la casse et la preuve déclarées ; la provenance est identique ; aucune règle n'est ajoutée dans l'en-tête, la preuve ou le paragraphe « Adaptations » ;
- **MEC-0001 à MEC-0003 :** elles sont intactes, et seule la l. 5 change avant la fiche ;
- **périmètre :** exactement quatre fichiers.

Aucun constat bloquant ne subsiste. Les réserves RJ-01 à RJ-03 portent sur l'exactitude du rapport : ses preuves mécaniques sont décrites plus largement que ce qu'elles couvrent, et deux affirmations sur l'en-tête sont inexactes. Leur correction ne demande pas de modifier le registre. Je ne m'accorde pas la validation finale.

---

**Traitement des constats de la seconde relecture :**

| Constat | Classement | Traitement |
|---|---|---|
| RJ-01 : la comparaison stricte ne couvre pas le texte rédigé par Claude Code, contrairement à ce que disait le rapport | à corriger | **Corrigé dans ce rapport** : le §4.1 précise la portée exacte des points A à D, et le §4.2 distingue parties reprises et parties rédigées. Le registre n'est pas modifié : sa conformité a été vérifiée par lecture et par les deux relectures. |
| RJ-02 : le second point F ne peut pas échouer | à corriger | **Corrigé dans ce rapport** : ce point est décrit au §4.1 comme une vérification de cohérence interne des valeurs de la v1.2. Le recalcul de la seconde relecture, à partir du registre, y est cité. Le script n'est pas modifié. |
| RJ-03 : le libellé « Fiche de périmètre restreint : » n'appartient pas à la v1.2, alors que deux phrases du rapport disaient le contraire | à corriger | **Corrigé dans ce rapport** (§1 et traitement de RI-02). Dans le registre, la phrase « l'en-tête en gras assemble des phrases de ce texte » reste incomplète sur ce point. La corriger changerait l'empreinte du registre et demanderait une nouvelle vérification : elle est soumise au propriétaire (§7). |
| RJ-04 : des omissions de forme ne sont pas déclarées dans la fiche | observation | **Déclarées dans ce rapport** (§3). Le registre n'est pas modifié. |
| RJ-05 : titre du mandat tronqué dans l'en-tête du rapport | observation | **Corrigé** (en-tête du rapport). |
| RJ-06 : affirmations qui deviendraient fausses (une seule relecture citée, « Rien n'est commité », autorisation de publication non citée) | observation | **Corrigé dans ce rapport** : en-tête, §1, §6 et §7. L'index des mandats garde la description de l'autorisation d'exécution, sans commit ni push, qui est historiquement exacte ; il n'est pas modifié, si bien que l'annexe B reste exacte. |

La seconde relecture a pu lire le journal de session. Elle a constaté que la transcription du mandat, l'autorisation et le texte v1.2 sont identiques aux messages du propriétaire, ce qui lève la réserve correspondante de la première relecture. La réponse « oui » du 23 novembre 2026 reste non vérifiée.

Les corrections faites après la seconde relecture ne touchent que ce rapport, et n'ont pas été relues par un troisième agent.

## 7. Points à décider par le propriétaire

1. **Publication :** autorisée sous conditions le 24 novembre 2026 (17:41:06 UTC) : un commit des quatre fichiers, push de la branche `claude/lot-1g-a-inscription-mec-0004`, PR en brouillon. **La fusion dans `main` demande une autorisation distincte.**
2. **Auto-description de la fiche (RJ-03, RJ-04) :** faut-il compléter, dans le registre, le paragraphe « Adaptations à l'inscription » pour qu'il mentionne le libellé « Fiche de périmètre restreint : » et les omissions de forme ? Cela demanderait une retouche du registre et sa vérification.
3. **Casse de « acceptée » (RI-01) :** confirmer cette adaptation de forme. Garder « Acceptée » ferait échouer le contrôle de traçabilité de la CI pour `MEC-0004`, sauf à modifier le harnais par un mandat distinct.
4. **§8 de la v1.2 (RI-04) :** il ne figure qu'à l'annexe A de ce rapport. Convient-il, ou faut-il l'archiver ailleurs ?
5. **Renvoi depuis `MEC-0003` (RI-05) :** sa phrase « Ces sujets restent régis par `MEC-0001` et `MEC-0002` » ne mentionne pas `MEC-0004`. Ajouter un renvoi croisé demanderait votre validation et un mandat, puisque ce lot interdit de modifier `MEC-0003`.
6. **Suite :** préparer le mandat d'implémentation du lot 1G (§8 de la v1.2, étape 3), puis l'autoriser séparément.

## Annexe A — Texte consolidé de MEC-0004 v1.2, tel que transmis

Le texte transmis par le propriétaire le 24 novembre 2026 à 17:15:02 UTC est reproduit ci-dessous sans modification. Une ligne finale de fin de fichier lui est ajoutée.

~~~~markdown
# BASTION — MEC-0004 v1.2
## Gestion élémentaire des tours et récupération des ressources

**Statut : ACCEPTÉE — décision du propriétaire du 23 novembre 2026**  
**Classe : `MODIFICATION-VALIDEE`**  
**État d'implémentation : `non commencé`**

**Provenance :** MEC-0004 v1.1, complétée par les trois précisions proposées par l'orchestrateur dans MEC-0004 v1.2, puis validée intégralement par le propriétaire le 23 novembre 2026, en réponse à la question « Validez-vous MEC-0004 v1.2 dans son ensemble ? » par « oui ».

Ce document consolide les règles acceptées. Il n'est pas une nouvelle proposition de gameplay.

## 1. Fiche du registre

| Champ | Valeur |
|---|---|
| Système | Combat tactique : gestion élémentaire des tours d'une seule unité. |
| Description | Une commande explicite termine le tour, récupère les TU et l'énergie et incrémente le compteur de tours. |
| Classe | `MODIFICATION-VALIDEE`, uniquement pour le périmètre de cette fiche. |
| Fonctionnement de référence et preuves | Règles propres à Bastion. Renvoi à ARB-D, Q3.6, Q4.6 et Q3.14 de MEC-0001. Aucun comportement ni fidélité à OXCE revendiqué. |
| Changement demandé | Introduire la mécanique restreinte décrite ci-dessous, sans modifier MEC-0003. |
| Décision du propriétaire | Acceptée le 23 novembre 2026 : validation explicite de MEC-0004 v1.2 dans son ensemble, comprenant la fiche v1.1 et ses trois précisions finales. |
| Périmètre autorisé | Uniquement le fonctionnement décrit dans les sections 2 à 4. |
| Éléments exclus | Section 5 et tout comportement non décrit dans cette fiche. |
| Tests de référence | Aucun : aucune fidélité à OXCE revendiquée. |
| Tests de modification | T01 à T16, définis à la section 6, non encore implémentés. |
| État d'implémentation | `non commencé` |

## 2. Portée des décisions existantes

MEC-0004 applique par renvoi certaines sous-décisions de MEC-0001, sans valider MEC-0001 dans son ensemble.

Les décisions existantes sont :

- **ARB-D :** récupération des TU par addition du solde et du montant récupéré, avec plafonnement.
- **Q3.6 :** énergie disposant d'une réserve maximale et d'une récupération distinctes de celles des TU.
- **Q4.6 :** profil initial de test configurable de 60 TU maximales, 60 TU récupérées par tour, 100 points d'énergie maximale et 20 récupérés par tour.
- **Q3.14 :** facteur de surcharge égal à 1 lorsque la charge est nulle.

La formule de récupération de l'énergie par addition plafonnée est une **nouvelle décision de MEC-0004**, et non une formule précédemment fixée par MEC-0001.

### Surcharge

MEC-0004 ne modélise aucune charge portée. Le facteur de surcharge est donc neutre (1), conformément au cas sans charge prévu par Q3.14.

La récupération des TU utilise ainsi la formule d'ARB-D sans réduction supplémentaire.

Aucune règle de surcharge n'est implémentée.

MEC-0001 et MEC-0002 conservent leur statut reporté. MEC-0003 reste inchangée.

## 3. Fonctionnement

### 3.1. Ressources

Profil initial de test :

| Paramètre | Valeur |
|---|---:|
| TU maximales | 60 |
| Récupération de TU par tour | 60 |
| Énergie maximale | 100 |
| Récupération d'énergie par tour | 20 |

Les quatre paramètres sont configurables. Ces valeurs ne constituent pas l'équilibrage définitif du jeu.

**TU après récupération :**

`TU suivantes = min(TU courantes + récupération TU, TU maximales)`

**Énergie après récupération :**

`Énergie suivante = min(énergie courante + récupération énergie, énergie maximale)`

La récupération est indépendante pour les deux ressources.

### 3.2. Validation des paramètres

- Les plafonds sont strictement positifs.
- Les récupérations sont positives ou nulles.
- Une récupération supérieure au plafond est autorisée.
- Les ressources courantes doivent être comprises entre zéro et leur plafond respectif, bornes incluses.
- Les valeurs négatives sont refusées.
- Un état initial dépassant un plafond est refusé, sans réduction silencieuse.
- Un état initial exactement égal aux plafonds est accepté.

Ces contrôles appartiennent au nouveau système de tours.

Ils ne modifient pas les règles existantes de création des états de MEC-0003, notamment `MovementModel.CreateState`.

### 3.3. Déroulement d'un tour

1. L'unité commence au tour numéro 1.
2. Le joueur peut déplacer l'unité selon MEC-0003.
3. Le joueur déclenche explicitement « Fin de tour ».
4. Le moteur applique les deux récupérations.
5. Le numéro de tour augmente de 1.
6. La position et l'orientation de l'unité restent inchangées.
7. Le joueur peut de nouveau déplacer l'unité.

La fin de tour est autorisée même si aucune action n'a été effectuée ou si les deux ressources sont déjà à leur maximum.

Aucune fin de tour automatique n'est introduite.

### 3.4. Conservation des informations affichées

Après une fin de tour :

- Le chemin du dernier ordre de déplacement est conservé.
- Le dernier résultat est remplacé par un message indiquant la fin du tour et la récupération effectuée.
- Le compteur de tours est actualisé.
- Les ressources affichées correspondent au nouvel état.

La fin de tour n'est pas un nouvel ordre de déplacement.

La touche R efface le chemin et restaure le message initial du scénario.

## 4. Prototype Godot — Scénario 4

Les scénarios 1, 2 et 3 restent inchangés.

### Configuration

- Carte identique à celle du scénario 1.
- Une seule unité.
- Position initiale : (1,4).
- Orientation initiale : nord.
- TU initiales : 12.
- Énergie initiale : 35.
- Tour initial : 1.

### Commandes

**Touche 4 :**

Charge le scénario 4 dans son état initial.

Appuyer sur 4 lorsque le scénario 4 est déjà actif provoque également une réinitialisation complète.

Sur clavier AZERTY, la position physique de la touche 4 est reconnue, notamment lorsque son libellé est une apostrophe.

**Touche T :**

Termine le tour dans le scénario 4.

Elle est sans effet dans les scénarios 1, 2 et 3.

**Touche R :**

Réinitialise le scénario courant.

Dans le scénario 4, elle restaure :
- le tour 1 ;
- les 12 TU ;
- les 35 points d'énergie ;
- la position initiale ;
- l'orientation initiale ;
- le chemin initial effacé ;
- le message initial.

### Affichage

Le panneau du scénario 4 présente le numéro de tour, les ressources, les commandes et le dernier résultat.

Le compteur de tours ne s'affiche que dans le scénario 4.

Le chemin affiché est celui du dernier déplacement exécuté par le moteur, conservé conformément à la section 3.4.

Les règles de récupération appartiennent exclusivement à `Bastion.Simulation`. Le client Godot transmet les commandes et affiche les résultats.

## 5. Hors périmètre

Ne pas introduire :

- plusieurs unités ;
- adversaires ou intelligence artificielle ;
- alternance entre camps ou phases ennemies ;
- combats, réactions ou surveillance ;
- gestion de l'initiative ;
- inventaire, équipements et surcharge ;
- récupération conditionnelle au repos ;
- limite temporelle des tours ;
- animation ou interface définitive ;
- modification des règles de marche de MEC-0003 ;
- implémentation générale de MEC-0001 ou MEC-0002.

Tout comportement non explicitement décrit dans la présente fiche est hors périmètre.

## 6. Tests de comportement

Les tests suivants sont définis et acceptés, mais ne sont pas encore implémentés.

| ID | Situation | Résultat attendu |
|---|---|---|
| T01 | Tour 1, 12 TU, 35 énergie ; fin de tour | Tour 2, 60 TU, 55 énergie |
| T02 | Tour 2, 60 TU, 55 énergie ; fin de tour sans déplacement | Tour 3, 60 TU, 75 énergie |
| T03 | 58 TU, 95 énergie ; fin de tour | 60 TU, 100 énergie |
| T04 | Fin de tour sans déplacement | Compteur augmenté de 1 |
| T05 | Fin de tour après déplacement | Position et orientation conservées |
| T06 | Maximum TU 40, récupération TU 25 ; maximum énergie 30, récupération énergie 10 ; ressources courantes 12 TU, 15 énergie | 37 TU, 25 énergie |
| T07 | Récupération supérieure au plafond | Résultat plafonné |
| T08 | Récupération égale à zéro | Ressource inchangée |
| T09 | Paramètre négatif, plafond nul ou état initial hors plafond | Rejet explicite, sans modification d'état |
| T10 | Touche T dans les scénarios 1 à 3 | Aucun effet |
| T11 | Touche R ou 4 dans le scénario 4 | Réinitialisation complète |
| T12 | Touche 4 simulée avec un clavier AZERTY | Scénario 4 chargé |
| T13 | Scénarios 1 à 3 et contrôles existants | Aucune régression |
| T14 | 60 TU, 100 énergie ; fin de tour | Ressources inchangées, compteur +1 |
| T15 | État initial exactement aux plafonds | Accepté |
| T16 | Fin de tour après déplacement | Chemin conservé, message du dernier résultat actualisé |

## 7. Architecture et qualité

Prescriptions destinées au futur mandat d'implémentation :

- La logique des tours appartient à `Bastion.Simulation`.
- Le moteur ne dépend pas de Godot.
- Les états restent immuables.
- Le client Godot ne recalcule pas les ressources.
- Les fonctionnalités existantes sont réutilisées.
- Aucune dépendance, abstraction ou framework supplémentaire sans justification.
- Les tests unitaires, les contrôles fumée et une relecture indépendante accompagnent l'implémentation.

La présente fiche ne demande pas encore d'écrire ce code.

## 8. Autorisations et étapes

La mécanique MEC-0004 v1.2 a été acceptée par le propriétaire le 23 novembre 2026.

Les étapes sont :

1. Inscription de cette fiche acceptée dans le registre.
2. Vérification de la conformité de l'inscription.
3. Préparation du mandat d'implémentation LOT-1G.
4. Autorisation distincte d'implémentation.
5. Développement, tests et relecture indépendante.
6. Publication et fusion sous autorisations distinctes.

La validation fonctionnelle de MEC-0004 ne vaut pas autorisation générale de modification du dépôt.

**Fin de la spécification MEC-0004 v1.2 consolidée.**
~~~~

## Annexe B — Empreintes SHA-256

| Fichier | Sur `origin/main` (`56fecf3`) | Dans l'arbre de travail du lot |
|---|---|---|
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | `36b5ac5b288fcd48756d628a7b1a7d613658cdea3208b1b58029dd43dc2f9812` | `7993e0c96faeb9d87cb23f1de4aba2e2100791af0b369f21f6271e135ba3ba24` |
| `docs/mandates/README.md` | `0e1d27abc0ecd9a11a06800944b9e4f10f260eb20734e2989b7aae4049116fbb` | `668fd8eef603a19a924c2e0d0742113874deb1052b2690eb264f981121c569e0` |
| `docs/mandates/BASTION-MANDAT-LOT-1G-A-INSCRIPTION-MEC-0004-transcription.md` | absent | `89447962c4f6677a90286b109f8ca0c42a59b2dcf0d1f1151ef5df19fe73cb11` |
| texte v1.2 (annexe A, extrait du journal de session, avec une fin de ligne finale) | — | `f81fa45670ea8913d7e2a8229fa4aa471a50a751db07541b7e44b0c406b73695` |

Ce rapport ne peut pas porter sa propre empreinte.
