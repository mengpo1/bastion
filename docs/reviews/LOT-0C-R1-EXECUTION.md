# LOT-0C-R1 — Rapport d'exécution

**Mandat :** `BASTION-MANDAT-LOT-0C-R1-v1.0.md`, lu sur la branche `orchestration/mandats` au commit `a00a7fac18f280acf5282474ff285a6022c6ab1c`. Empreinte du fichier : SHA-256 `d1322a2060423848bf4b7de2b4c5b5552c95ae19d2fee303b32f400143c67499`, 10 340 octets. Il n'est pas recopié sur la branche de travail (§2.3).
**Exécutant :** Claude Code · **Date :** 8 nov. 2026
**Branche :** `chore/lot-0c-qualification` · **PR :** https://github.com/mengpo1/bastion/pull/2 (brouillon, non fusionnée)

## 1. Résumé

| Correction | Changement | Statut |
|---|---|---|
| **H-Q05** : traçabilité des changements de simulation | Nouveau script `scripts/harness/check-simulation-trace.sh`, lancé par la CI sur les pull requests. Si la PR ajoute, modifie, renomme ou supprime un fichier de `src/Bastion.Simulation/`, sa description doit contenir une ligne `Traçabilité simulation : TECHNIQUE — <justification>` ou `Traçabilité simulation : MEC-NNNN — <justification>`. Pour `MEC`, la fiche doit exister et porter une décision « acceptée ». Sinon, la CI échoue avec une erreur explicite. | **Corrigé, contrôle syntaxique seulement.** Il ne prouve pas l'absence de gameplay. Non requalifié. |
| **H-Q06** : hook `Stop` | Base `origin/main` de préférence, `main` à défaut ; aucun `git fetch` dans le hook ; message reformulé ; `stop_hook_active` conservé. | **Corrigé en partie.** Faux passage avec `main` locale périmée corrigé, message compris en session réelle. Un rapport vide reste accepté et les références périmées restent un risque. Non requalifié. |
| Règles permanentes | `CLAUDE.md` : `git fetch origin main` au démarrage de chaque lot (§5) ; règle de notification de fin de mandat (§6). | Fait, ajouts seulement. |

## 2. Préconditions vérifiées

| Élément | Attendu (mandat) | Constaté | Résultat |
|---|---|---|---|
| `main` (local après `git fetch origin main:main`, et distant) | `9ece89d…` | `9ece89df9acd88bcf8c8c2eb8215ffd5937a04b4` | conforme |
| Tête de la PR n° 2 et branche distante | `1d18dc2…` | `1d18dc206900ec44f40aa8e689058cf94a88c73a` ; 3 commits ; `draft: true`, `merged: false`, `mergeable_state: clean` | conforme |
| Rapports du lot 0C | présents | `LOT-0C-QUALIFICATION.md`, `LOT-0C-PREUVES.md` | conforme |
| Mandat | commit `a00a7fa` sur `orchestration/mandats` | commit présent, ancêtre de la tête de `orchestration/mandats`, auteur `mengpo1` | conforme |

## 3. Fichiers modifiés et commits

Commits ajoutés sur `chore/lot-0c-qualification`, sans rebase ni amendement :
- `0a1d1d7` : corrections ;
- `220f231` : brouillon de ce rapport ;
- `6e3212e` : suites de la revue indépendante ;
- puis le commit de ce rapport.

| Fichier | Changement |
|---|---|
| `scripts/harness/check-simulation-trace.sh` | **Nouveau** (unique script ajouté) : contrôle de traçabilité |
| `.github/workflows/ci.yml` | Déclencheurs PR `opened, synchronize, reopened, edited` ; `fetch-depth: 2` ; étapes « Traçabilité simulation (PR) » et « (hors PR) » |
| `scripts/harness/stop-report-check.sh` | Base `origin/main` puis `main` ; message reformulé ; commentaires |
| `scripts/harness/test-hooks.sh` | 27 cas ajoutés : 75 tests au lieu de 48 |
| `scripts/harness/README.md` | Contrôle de traçabilité et limites ; limites du hook `Stop` |
| `CLAUDE.md` | 8 lignes ajoutées, aucune retirée |
| `docs/reviews/LOT-0C-R1-EXECUTION.md` | Ce rapport |

Non modifiés : registres gameplay et technique, fichiers C#, hook PreToolUse, rapports du lot 0C, dossier `docs/mandates/`. Aucun nouveau dossier.

## 4. H-Q05 — contrôle de traçabilité

**Fonctionnement en CI** (étape « Traçabilité simulation (PR) », exécutée seulement sur les événements `pull_request`) :

- **Base de comparaison :** le commit testé est la fusion de test de GitHub (`refs/pull/N/merge`), et son premier parent est la base. La comparaison se fait donc entre `HEAD^1` et `HEAD`, avec `git diff --name-only --no-renames` sur `src/Bastion.Simulation/`.
  - `fetch-depth: 2` suffit à disposer de ces deux commits.
  - Une garde vérifie que `HEAD^2` existe ; sinon l'étape échoue avec une erreur claire.
- **Description de la PR :** elle passe par une variable d'environnement (`env: DESCRIPTION_PR: ${{ github.event.pull_request.body }}`), est écrite dans un fichier par `printf`, puis lue par le script. Elle n'est jamais interpolée dans du shell, et aucune dépendance n'est ajoutée.
- **Événement `edited` :** modifier la description relance le contrôle, sans nouveau commit.
- **Événement `push` :** l'étape « (hors PR) » indique que le contrôle ne s'applique qu'aux PR et ne bloque pas une fusion.
- **Messages :**
  - erreur `::error::` en cas de déclaration absente, mal formée (puce, gras, backticks…), sans justification, avec une justification laissée au gabarit (`<…>`), ou avec un `MEC` inexistant ou non « accepté » ;
  - succès explicite pour `TECHNIQUE`, avec le rappel que la revue doit vérifier l'absence de gameplay.

**Tests de `test-hooks.sh`** (dépôts temporaires, registre d'essai propre au test) :

| Cas demandé par le mandat | Résultat attendu | Obtenu |
|---|---|---|
| 1. PR sans changement de simulation | succès | succès |
| 2. Simulation modifiée sans déclaration (description vide ou texte libre) ; fichier ajouté, supprimé, renommé hors du dossier ou vers le dossier | échec | échec (6 cas) |
| 3. Déclaration vide ou mal formée (sans justification, type inconnu, gabarit `<…>`, puce Markdown, une ligne valide plus une invalide) | échec | échec (5 cas) |
| 4. `MEC` inexistant, refusé, ou recopié du gabarit | échec | échec (3 cas) |
| 5. `TECHNIQUE` justifié | succès syntaxique, **sans conclure à l'absence de gameplay** | succès (test étiqueté « LIMITE ») |
| 6. PR ne touchant que le harnais | succès sans déclaration | succès |
| Autres | — | `MEC` accepté (données d'essai) : succès ; fins de ligne Windows : succès ; **LIMITE** déclaration dans un bloc de code : acceptée ; **LIMITE** fiche `MEC` ajoutée par la PR : acceptée |

Les 21 cas passent sous les réglages de langue `C`, `C.UTF-8` et `en_US.UTF-8`.

**Étape CI réelle rejouée sur copies jetables.** Le texte de l'étape est lu dans `ci.yml` au commit `6e3212e`. Les copies sont des clones superficiels (profondeur 2) dont la tête est un commit de fusion construit comme celui de GitHub (premier parent = base).

| Cas | Sortie | Code |
|---|---|---|
| Simulation modifiée, description vide | `::error::Traçabilité simulation : déclaration absente de la description de la PR…` | 1 |
| Simulation modifiée, `Traçabilité simulation : TECHNIQUE — commentaire ajouté, aucun effet de jeu` | `Déclaration TECHNIQUE reconnue (contrôle syntaxique)…` | 0 |
| Simulation modifiée, `- **Traçabilité simulation : TECHNIQUE — mis en forme**` | `::error::… déclaration mal formée : écrivez-la seule sur sa ligne…` | 1 |
| Simulation modifiée, déclaration contenant `$(touch …)` et `` `touch …` `` | déclaration reconnue ; **aucun fichier créé** | 0 |
| Documentation seulement, description vide | `Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise.` | 0 |

Une version antérieure de l'étape lisait la description avec `jq`. Rejouée dans les mêmes conditions, elle donnait les mêmes résultats, et aucune substitution n'était exécutée, y compris dans une ligne mal formée recopiée dans le message d'erreur.

**Sur GitHub :** la PR n° 2 ne modifie aucun fichier de simulation. Sur sa vraie description, l'étape répond `Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise.` (exécution n° 12, section 9). **Non démontré sur GitHub :** un échec réel. Il faudrait une PR qui modifie la simulation, ce que le mandat n'autorise pas ; ce cas est démontré seulement sur copies jetables.

## 5. H-Q06 — hook `Stop`

**Corrections :**
1. Base : `git merge-base HEAD origin/main`, puis `main` à défaut. Le hook ne lance pas `git fetch`.
2. `CLAUDE.md` §5 et README : `git fetch origin main` au démarrage de chaque lot. Le README précise que `origin/main` reste périmée sans cette commande.
3. Nouveau message : « Harnais Bastion : Aucun rapport du lot n'a été ajouté ou modifié dans docs/reviews/ alors que des fichiers ont changé sur cette branche (commités ou non). Si le mandat est terminé, rédigez son rapport avec les contrôles exécutés et non exécutés ; sinon indiquez explicitement que le mandat est incomplet ou en attente d'arbitrage. »
4. `stop_hook_active` est conservé, ainsi que les autres comportements : les tests existants passent toujours.
5. Aucune analyse du contenu des rapports.

**Avant / après.** La suite enrichie a été lancée **avant** toute correction : `67 tests, 17 échec(s)`, code 1. Parmi ces 17 échecs :
- **2** sont un vrai avant/après du hook `Stop` : « main locale périmée, origin/main à jour : branche sans rapport », attendu « bloque », obtenu « autorise » ; et le test du message ;
- **15** sont des codes 127, parce que le script de traçabilité n'existait pas encore. Ils ne prouvent qu'une absence, pas un comportement.

Après correction : `67 tests, 0 échec(s)`. Puis, avec les cas ajoutés après la revue : `75 tests, 0 échec(s)`, code 0.

**Copie jetable du vrai dépôt.** `main` locale = `fdbff5d` (périmée), `origin/main` = tête du lot, branche avec un commit sans rapport. Le hook est lancé directement.

| Situation | Ancien hook (`1d18dc2`) | Nouveau hook |
|---|---|---|
| `main` périmée, `origin/main` à jour | code 0 (**faux passage**) | code 2, nouveau message |
| `origin/main` absente, `main` périmée (repli) | — | code 0 (**faux passage conservé**, limite) |
| `origin/main` absente, `main` à jour (repli) | — | code 2 |
| Second arrêt (`stop_hook_active: true`) | — | code 0 |

**Session réelle** (`claude -p`, Claude Code 2.1.319, mode `acceptEdits`, même copie, branche sans rapport) :
- `Stop` répond code 2 avec le nouveau message ;
- la session répond : « Aucun rapport n'a été rédigé, et ce n'est pas un oubli : le changement de cette branche ne correspond à aucun mandat », puis liste les contrôles non exécutés ;
- second arrêt : code 0. Fin : `success`, 4 tours, 0,006 $.
- Le message n'est plus lu comme « des changements dans `docs/reviews/` », alors qu'il l'avait été 5 fois sur 5 au lot 0C. **Un seul essai.**

**Nouveaux tests du hook `Stop`** dans `test-hooks.sh` :
- branche identique à `origin/main` : autorisé, pas de faux blocage ;
- `main` périmée et `origin/main` à jour, branche sans rapport : bloqué ;
- contenu du message ;
- même cas avec un rapport présent : autorisé ;
- **LIMITE** `origin/main` absente et `main` périmée : faux passage ;
- **LIMITE** `main` à jour et `origin/main` périmée : faux passage.

Le cas « `origin/main` absente » est aussi couvert par les dépôts de test existants, qui n'ont pas de dépôt distant.

## 6. Règle de fin de mandat

Ajoutée à `CLAUDE.md` §6, fidèle au §5 du mandat :
- rapport commité et poussé sur la seule branche autorisée ;
- notification avec le chemin GitHub, la branche, le SHA, la PR et l'état réel de la CI ;
- signalement si la publication est impossible ;
- aucune revue automatique présumée ;
- aucune fusion ni écriture sur `main` sans autorisation distincte ;
- la règle n'autorise aucun push à elle seule.

## 7. Vérifications locales

Commit `6e3212e`, SDK .NET 10.0.114 local.

| Commande | Résultat | Code |
|---|---|---|
| `dotnet restore` | projets à jour | 0 |
| `dotnet build --no-restore --configuration Release` | 0 avertissement, 0 erreur | 0 |
| `dotnet format --verify-no-changes --no-restore` | aucune sortie | 0 |
| `dotnet test --no-build --configuration Release` | `Passed: 2, Failed: 0, Total: 2` | 0 |
| `bash scripts/harness/test-hooks.sh` | `75 tests, 0 échec(s)` | 0 |
| Validation YAML de `ci.yml` | 9 étapes, conditions `if` correctes | 0 |
| Recherche de secrets dans le diff `1d18dc2..6e3212e` | aucune correspondance | 1 (= rien trouvé) |

**Erreur interceptée avant le push :** la première version de `ci.yml` contenait « : » dans un texte non entre guillemets. La validation YAML a échoué (`mapping values are not allowed here`, ligne 53) ; c'est corrigé, et rien n'a été poussé avec cette erreur.

## 8. Revue indépendante

Sous-agent distinct, en lecture seule, sur le commit `0a1d1d7`. Il n'a rien modifié dans le dépôt et a rejoué les tests et l'étape CI dans des copies.

| Constat | Traitement |
|---|---|
| Limites non documentées : déclaration dans un bloc de code ou un commentaire HTML acceptée ; fiche `MEC` dans un bloc de code ; décision à peine remplie ou annulée plus loin ; la PR exécute son propre `ci.yml` et son propre script | **Documentées** dans le README ; 2 tests « LIMITE » ajoutés |
| Rejets à tort avec le message trompeur « absente » (puce, gras, backticks, citation, espace insécable…) | **Corrigé :** message « mal formée » qui demande une ligne seule, sans mise en forme ; test ajouté |
| Avec `main` locale à jour et `origin/main` périmée, une branche sans rapport passe désormais, alors que l'ancien hook la bloquait | **Documenté** (README, test « LIMITE »). Non corrigé : le mandat demande de préférer `origin/main`. Point d'arbitrage B1 |
| README : mention « non qualifié » supprimée ; « la CI » retirée des cas non couverts par les hooks | **Rétabli** (renvoi aux rapports 0C et 0C-R1) |
| Tests : pas d'ajout ni de renommage ; pas de « LIMITE » ; 15 des 17 échecs « avant » sont des codes 127 | **4 cas et 4 « LIMITE » ajoutés** ; nature des échecs « avant » précisée en section 5 |
| `jq` n'est pas une bibliothèque standard ; la variable d'environnement suffit | **Changé :** description lue par variable d'environnement, sans `jq` |
| `Directory.Build.props` et `global.json` agissent sur la simulation mais ne sont pas surveillés | **Documenté.** Conforme au mandat ; point d'arbitrage B2 |
| Injection de commandes de workflow (`::…`) via le texte affiché | Vérifié par le relecteur : impossible (texte sur la même ligne, après `::error::`) |

Points vérifiés exacts par la revue :
- base `HEAD^1`, profondeur 2, garde `HEAD^2` ;
- détection des ajouts, renommages (noms avec espace et accent), suppressions, du `.csproj` et des changements de droits ;
- rejet des fiches refusées, reportées, du gabarit, et des décisions vides ou non acceptées ;
- hook `Stop` sans faux blocage sur `main`, en HEAD détachée, sans `origin` ou avec un `origin/main` sans ancêtre commun ;
- `CLAUDE.md` : ajouts seulement ;
- périmètre conforme.

## 9. CI GitHub Actions

Commit `6e3212ec8e5846708f85a2e69da3f483c0954185`, observé après le push :

| Exécution | Événement | Résultat | Étapes |
|---|---|---|---|
| [n° 11 — 42485326718](https://github.com/mengpo1/bastion/actions/runs/42485326718) | `push` | **success** | Toutes vertes ; « Tests des hooks » : `75 tests, 0 échec(s)` ; « Traçabilité simulation (PR) » ignorée ; « (hors PR) » : `Contrôle de déclaration non applicable à l'événement push : il ne s'applique qu'aux pull requests et ne bloque pas une fusion (main non protégée).` |
| [n° 12 — 42485330916](https://github.com/mengpo1/bastion/actions/runs/42485330916) | `pull_request` | **success** | Toutes vertes ; « Traçabilité simulation (PR) », sur la vraie description de la PR n° 2 : `Aucun fichier de src/Bastion.Simulation/ modifié : aucune déclaration requise.` ; « (hors PR) » ignorée |

Le journal de l'étape PR affiche la description dans son en-tête, puisque GitHub montre les variables d'environnement. Aucune donnée sensible n'y figure.

L'état de la CI sur le commit de ce rapport est donné dans la notification de fin de mandat.

## 10. Limites conservées

- **`main` n'a aucune protection technique :** une PR rouge reste fusionnable, et le contrôle de traçabilité ne bloque pas une fusion.
- **Les hooks et la CI ne garantissent aucune validation sémantique :** une déclaration `TECHNIQUE` peut être fausse, et une fiche `MEC` peut avoir été ajoutée par la PR elle-même. La revue indépendante et le propriétaire restent indispensables.
- **Un rapport vide est toujours accepté** par le hook `Stop`. C'est une limite connue, pas une réussite.
- **Les références Git peuvent être périmées.** `origin/main` reste périmée sans `git fetch origin main`, et le repli sur `main` locale aussi. Plusieurs mandats sur une même branche : le rapport d'un mandat précédent suffit au hook. C'est le cas de ce mandat, exécuté sur la branche du lot 0C.
- **Contrôles Godot et OXCE reportés** (H-Q03, H-Q09, H-Q10).
- **Contournements :** une PR peut modifier son propre contrôle ; une déclaration cachée dans un bloc de code passe ; `Directory.Build.props` et `global.json` ne sont pas surveillés.
- **Un seul essai** en session réelle pour le nouveau message ; demande d'accord en session interactive toujours non qualifiée.

## 11. Points nécessitant un arbitrage

| # | Point |
|---|---|
| B1 | Hook `Stop` : quand `main` et `origin/main` existent toutes deux, faut-il prendre la base la plus récente (sans `git fetch`), plutôt que préférer toujours `origin/main` comme le demande ce mandat ? |
| B2 | Surveiller aussi `Directory.Build.props` et `global.json` dans le contrôle de traçabilité ? |
| B3 | Un essai sur GitHub d'une PR qui modifie la simulation (branche jetable, puis fermeture) pour démontrer un échec réel du contrôle ? |
| B4 | Les arbitrages restants du lot 0C (A1 protection de `main`, A4/A10/A11 et suivants) restent ouverts. |

## 12. Déclaration

**Aucun gameplay implémenté. Aucune fusion. Aucune écriture sur `main`.** La PR n° 2 reste en brouillon.

Arrêt à la fin du mandat LOT-0C-R1. Le lot 0D n'est pas commencé.
