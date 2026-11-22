# Bastion — MEC-0003, lot 1B : clôture documentaire

**Date :** 22 novembre 2026
**Mandat :** « BASTION — Mandat de clôture documentaire MEC-0003 — Lot 1B ». Il a été proposé par ChatGPT et transmis par le propriétaire dans la conversation le 2026-11-22T15:38:29.847Z. Il est archivé dans `docs/mandates/BASTION-MANDAT-CLOTURE-DOCUMENTAIRE-MEC-0003-LOT-1B-transcription.md`.
**Autorisation d'exécution :** « BASTION — Lot 1B — Autorisation d'exécution », message du propriétaire du 2026-11-22T15:43:00.985Z (annexe B). Elle n'autorise pas la publication.
**Base :** `main` au commit de fusion de la PR #19, `eeebc57001cd73a1ff1b45375960dc9b99ae3281`, contrôlée par `git fetch origin main` avant toute écriture (inchangée depuis la préparation).
**Branche :** `claude/lot-1b-cloture-mec-0003`, créée à partir de `origin/main`.
**État :** modifications appliquées et vérifiées localement. **Rien n'est commité ni publié.**

## 1. Résumé

Le lot est exclusivement documentaire. Il met `README.md` et la fiche `MEC-0003` du registre en cohérence avec la fusion du lot 1 de `MEC-0003` (PR #19).
- **`README.md` :** l'état du projet est actualisé, de même que les descriptions de la simulation et des tests ; la ligne de la référence OXCE est corrigée.
- **Fiche `MEC-0003` :** deux champs sont modifiés.
  - Le champ « Tests de modification » reçoit une annotation historique.
  - L'état d'implémentation passe à « intégré ».
- **Mandat 1B :** il est archivé dans `docs/mandates/` et indexé dans `docs/mandates/README.md`.

Les modifications sont exactement celles du diff présenté et validé. Aucun code, aucun test, aucune règle de gameplay, aucune décision technique et aucun élément du harnais n'est modifié. `MEC-0001` et `MEC-0002` sont inchangées, et restent reportées.

## 2. Modifications

| Fichier | Modification |
|---|---|
| `README.md` | voir §2.1 |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` | deux lignes de la fiche `MEC-0003` (l. 459 et 460) : voir §2.2 |
| `docs/mandates/BASTION-MANDAT-CLOTURE-DOCUMENTAIRE-MEC-0003-LOT-1B-transcription.md` | nouveau : le mandat 1B, archivé (§3) |
| `docs/mandates/README.md` | une ligne ajoutée, pour le mandat 1B (§3) |
| `docs/reviews/MEC-0003-CLOTURE-DOCUMENTAIRE-LOT1B-2026-11-22.md` | nouveau : ce rapport |

### 2.1 `README.md`

- **État du projet**, à la place de « lot 0B — harnais de développement uniquement. Aucun gameplay n'est implémenté » :
  - le harnais de développement est installé et opérationnel : hooks Claude Code, tests des hooks, intégration continue ;
  - le premier incrément de gameplay, `MEC-0003` (marche sur terrain plat), est implémenté, testé et intégré à `main` (PR #19) ;
  - la simulation C# comprend désormais la marche sur terrain plat ; `MEC-0001` et `MEC-0002` restent reportées ;
  - l'interface Godot n'est pas encore créée.
- **Table « Contenu » :**
  - `src/Bastion.Simulation/` : « marche sur terrain plat de `MEC-0003` (`Movement/`) », au lieu de « aucun gameplay à ce stade » ;
  - `tests/Bastion.Simulation.Tests/` : « tests fumée techniques et tests de `MEC-0003` (`Movement/`) », au lieu de « test fumée technique » ;
  - `docs/references/OXCE-BASELINE.md` : « commit figé, validée le 8 novembre 2026 », au lieu de « version à figer ». Le registre de référence porte en effet le commit figé `441cae1b…`, validé le 8 novembre 2026.
- **Inchangé :** la phrase « Le projet Godot (interface) n'existe pas encore », toujours exacte.

### 2.2 Fiche `MEC-0003`

- **« Tests de modification ».** Le texte d'origine est conservé mot pour mot : « T01 à T29 et T03b, ci-dessous. Aucun n'est écrit ni exécuté à la date de l'inscription. »
  - Une annotation datée du 22 novembre 2026 le suit, sur le modèle des annotations déjà présentes dans le registre (« texte historique conservé »).
  - Elle indique que les 30 scénarios sont couverts par des tests écrits et réussis, exécutés avec succès par la CI de la PR #19 et par celle du commit de fusion.
  - Elle mentionne la correction de la dernière phrase de T13 par l'avenant n° 1, et renvoie au rapport d'exécution.
- **« État d'implémentation ».** La valeur passe de « non commencé » à « intégré », qui appartient au vocabulaire du registre (« non commencé · en cours · testé · intégré »).
  - Le champ cite la PR #19 et le commit de fusion.
  - Il conserve l'état à la date de l'inscription, « non commencé ».
  - Il mentionne les réserves ouvertes : RL-11, RL-13 et la limite de couverture de RL-01. Aucune n'est présentée comme levée.

Aucun autre champ, aucune règle, aucun scénario et aucun résultat attendu de la fiche n'est modifié.

## 3. Archivage du mandat 1B

- **Fichier :** `docs/mandates/BASTION-MANDAT-CLOTURE-DOCUMENTAIRE-MEC-0003-LOT-1B-transcription.md`.
- **Contenu :** le texte du message du 2026-11-22T15:38:29.847Z, extrait mécaniquement du journal de session et reproduit octet pour octet, suivi d'un saut de ligne final. C'est la convention des autres transcriptions du dossier. Le texte n'est pas réécrit : il indique toujours « Statut : préparé, en attente d'autorisation du propriétaire ».
- **Index :** une ligne ajoutée à `docs/mandates/README.md`, sur le modèle des lignes existantes.
  - Provenance : mandat proposé par ChatGPT, transmis par le propriétaire dans la conversation ; identité avec un fichier original non vérifiée.
  - Statut : approuvé et autorisé par le propriétaire le 22 novembre 2026, à 15:43:00 UTC.
  - Empreinte SHA-256 du fichier.

## 4. Contrôles exécutés

Toutes les commandes ont été exécutées dans `/home/user/bastion`, sur la branche `claude/lot-1b-cloture-mec-0003`, après application des modifications.

| Contrôle | Commande | Résultat |
|---|---|---|
| Base | `git fetch origin main` ; `git rev-parse origin/main` | code 0 ; `eeebc57001cd73a1ff1b45375960dc9b99ae3281`, inchangé |
| Fichiers de départ | `cmp` de `README.md` et du registre avec les versions sur lesquelles le diff avait été préparé | identiques : le diff reste applicable |
| Diff appliqué | comparaison octet pour octet des fichiers obtenus avec les versions proposées | identiques |
| Périmètre du registre | `git diff -U0 docs/gameplay/GAMEPLAY-DECISIONS.md` | un seul bloc, l. 459-460, dans la fiche `MEC-0003` (l. 444 et suivantes) ; `MEC-0001` (l. 49) et `MEC-0002` (l. 265) intactes |
| Périmètre du lot | `git status --porcelain`, puis `git status --porcelain -- src tests scripts .claude .github docs/decisions docs/references CLAUDE.md` | seuls les fichiers du §2 ; 0 fichier dans les chemins exclus |
| Archive | comparaison avec le message du journal, suivi d'un saut de ligne | identique |
| Restauration | `dotnet restore` | code 0 |
| Compilation | `dotnet build --configuration Release` | code 0 ; 0 avertissement, 0 erreur |
| Tests | `dotnet test --configuration Release` | code 0 ; 46 tests, 46 réussis |
| Format | `dotnet format --verify-no-changes` | code 0 |
| Harnais | `bash scripts/harness/test-hooks.sh` | code 0 ; « 75 tests, 0 échec(s) » |
| Traçabilité | `bash scripts/harness/check-simulation-trace.sh origin/main <description>` ; `git diff --name-only -- src/` | code 0 : « Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise » ; 0 fichier de `src/` modifié dans l'arbre de travail |

**Limite du contrôle de traçabilité.** Le script compare des commits, et rien n'est encore commité : il ne voit donc aucun fichier. L'absence de changement dans `src/` est établie par `git diff` et `git status` sur l'arbre de travail. La CI refera ce contrôle sur la PR.

Pas de relecture indépendante : vous ne l'avez pas demandée pour ce lot strictement documentaire.

## 5. Écarts et limites

- **Aucun écart** avec le diff validé.
- **Branche de suivi.** `git switch -c … origin/main` a configuré `origin/main` comme branche de suivi de la nouvelle branche. Cela n'a aucun effet sur le contenu. À la publication, le push devra viser explicitement `origin claude/lot-1b-cloture-mec-0003`, avec `-u`, pour suivre la branche distante de même nom.
- **Rapports historiques :** aucun n'est modifié, en particulier le rapport d'exécution du lot 1.
- **CI :** elle n'a pas tourné, puisque rien n'est publié.

## 6. Points à décider

1. **Publication :** commit unique, push de la seule branche `claude/lot-1b-cloture-mec-0003`, puis PR en brouillon vers `main`. Elle attend votre autorisation distincte. La PR ne modifiant pas `src/`, aucune déclaration de traçabilité n'est requise.

## Annexe A — Empreintes SHA-256

Après les modifications :

```
13cf328f92130eb36ec2e82502c2490dc8041f17de139d15a0818c1e7d106563  README.md
36b5ac5b288fcd48756d628a7b1a7d613658cdea3208b1b58029dd43dc2f9812  docs/gameplay/GAMEPLAY-DECISIONS.md
d6a1459bc302b19adf109867db5c76c305eb5a3bf48e34c904382036ca2500ed  docs/mandates/README.md
16dd374025f085f876c97a8021726a399990fd9df78d5ac78390f70e9559f09b  docs/mandates/BASTION-MANDAT-CLOTURE-DOCUMENTAIRE-MEC-0003-LOT-1B-transcription.md
```

Avant, sur `main` (`eeebc57`) :

```
1577f381ce4fcd11240c26350150f10013edf3587cc236034a45459e9edc6e68  README.md
7b4931f37171ffbd66b825d53547413623303d3884564a6884fe2e75c4b0bbb7  docs/gameplay/GAMEPLAY-DECISIONS.md
ebd4ded515d89fabf875245403c5938a7fbc029fc4a02c97009bc7743d8d52c5  docs/mandates/README.md
```

## Annexe B — Autorisation d'exécution, mot pour mot (2026-11-22T15:43:00.985Z)

> BASTION — Lot 1B — Autorisation d'exécution
> Je valide le diff documentaire présenté pour le lot 1B de clôture de MEC-0003.
> J'autorise son exécution, dans les limites suivantes.
> 1. Modifications du README
> Appliquer exactement les modifications proposées :
>
> * Actualisation de l'état du projet.
> * Mention de MEC-0003 comme premier incrément de gameplay intégré.
> * Maintien du statut reporté de MEC-0001 et MEC-0002.
> * Actualisation des descriptions de la simulation et des tests.
> * Correction de la référence OXCE, dont le commit est déjà figé et validé.
>
> 2. Modification du registre protégé
> J'autorise explicitement les deux modifications proposées dans la fiche MEC-0003 de `docs/gameplay/GAMEPLAY-DECISIONS.md` :
>
> * Annotation historique du champ « Tests de modification », avec conservation du texte d'origine et mention de la correction de T13.
> * Passage de l'état d'implémentation de « non commencé » à « intégré », avec conservation de l'état historique et mention des réserves ouvertes.
>
> Aucune autre modification du registre n'est autorisée.
> 3. Branche
> Créer une branche dédiée :
> `claude/lot-1b-cloture-mec-0003`
> Elle doit partir du `main` distant actualisé, après `git fetch origin main`.
> Ne pas réutiliser `claude/new-session-mgfohp`.
> Si la base a évolué, vérifier que le diff proposé reste applicable avant toute écriture.
> 4. Archivage
> J'autorise l'archivage du mandat 1B dans `docs/mandates/` ainsi que son référencement dans `docs/mandates/README.md`.
> Conserver fidèlement le texte du mandat, sans réécriture rétroactive. Indiquer sa provenance réelle : mandat proposé par ChatGPT, transmis et approuvé par le propriétaire.
> Le présent message constitue l'autorisation d'exécution, mais pas une autorisation de publication.
> 5. Rapport et contrôles
> Créer le rapport :
> `docs/reviews/MEC-0003-CLOTURE-DOCUMENTAIRE-LOT1B-2026-11-22.md`
> Exécuter les contrôles applicables : compilation, tests, formatage, harnais, vérification du diff et contrôle de traçabilité.
> Une nouvelle relecture indépendante n'est pas demandée pour ce lot strictement documentaire.
> Ne pas multiplier les contrôles sans nécessité.
> 6. Restrictions
> Aucune modification :
>
> * du code C# ;
> * des tests ;
> * du harnais ;
> * des règles de gameplay ;
> * de MEC-0001 ou MEC-0002 ;
> * des décisions techniques.
>
> Ne pas modifier les rapports historiques déjà publiés.
> Aucun commit, push, création de PR ou fusion n'est autorisé pour le moment.
> Après exécution, présenter le diff définitif, les résultats réels des contrôles et les éventuels écarts.
> La publication sera autorisée séparément.
