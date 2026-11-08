# BASTION — Mandat LOT-0C-R1 v1.0

**Titre :** Corrections limitées après qualification du harnais  
**Date :** 8 novembre 2026  
**Statut :** AUTORISÉ PAR LE PROPRIÉTAIRE — corrections limitées validées dans la conversation  
**Dépôt :** `mengpo1/bastion`  
**Base attendue :** `main` au commit `9ece89df9acd88bcf8c8c2eb8215ffd5937a04b4`  
**Branche de travail :** `chore/lot-0c-qualification`  
**Tête examinée :** `1d18dc206900ec44f40aa8e689058cf94a88c73a`  
**PR :** https://github.com/mengpo1/bastion/pull/2 (brouillon, non fusionnée)

## 1. Objectif unique

Corriger uniquement les deux insuffisances prioritaires révélées au lot 0C :

- **H-Q05 :** absence de contrôle minimal de traçabilité des changements de code de simulation dans les PR.
- **H-Q06 :** faux passage du hook `Stop` avec une référence `main` locale périmée et message d'absence de rapport ambigu.

Inscrire aussi dans `CLAUDE.md` la règle permanente de **notification au propriétaire à la fin de chaque mandat**.

**Règle fondamentale : rien d'alambiqué.** Corriger les défauts observés, sans chercher à rendre les hooks impossibles à contourner. Le contrôle humain reste indispensable.

## 2. Préconditions et gestion Git

1. Vérifier que `main`, la tête de la PR n° 2 et les rapports du lot 0C correspondent aux références ci-dessus. En cas de changement distant imprévu : arrêter et demander arbitrage, sans écraser ni réécrire les commits.
2. Rester sur `chore/lot-0c-qualification` ; conserver tous les commits existants, sans rebase ni amendement.
3. Lire le mandat directement depuis la branche GitHub `orchestration/mandats`, chemin `docs/mandates/BASTION-MANDAT-LOT-0C-R1-v1.0.md`. **Ne pas le recopier ni l'archiver** sur la branche de travail ; sa publication est prise en charge par l'orchestrateur. La branche `orchestration/mandats` est en lecture seule pour Claude Code.
4. Le mandat autorise les nouveaux commits et le **push de cette seule branche**, puis la mise à jour de la PR n° 2 en brouillon. Il n'autorise **aucun** push direct vers `main`, force push, fusion, suppression de branche ni publication d'autre chose.

## 3. Correction H-Q05 — Signalement obligatoire des changements de simulation

Ajouter **un contrôle minimal en CI**, exécuté sur les événements `pull_request` :

- Comparer les fichiers de la PR à sa branche de base, avec une référence Git correcte et disponible dans le runner (adapter la profondeur de `checkout` si nécessaire).
- Si **aucun fichier de `src/Bastion.Simulation/`** n'a changé : passage sans déclaration supplémentaire.
- Si **au moins un fichier** a été ajouté, modifié, renommé ou supprimé sous `src/Bastion.Simulation/` : exiger **dans la description de la PR** une ligne explicite de traçabilité, avec justification non vide, sous l'une des formes suivantes :
  - `Traçabilité simulation : TECHNIQUE — <justification précise>` ;
  - `Traçabilité simulation : MEC-0001 — <justification précise>` (identifiant adapté à la fiche réelle).
- En l'absence de déclaration, avec une justification vide, ou avec un identifiant `MEC` inexistant : **faire échouer le contrôle CI avec une erreur claire**. Ne jamais créer une fiche `MEC` fictive pour faire passer la CI.
- Une déclaration `MEC` n'est recevable que si une fiche correspondante existe et porte une **décision du propriétaire « acceptée »**. Le contrôle peut vérifier simplement les éléments explicites du registre ; **la validité de la décision, les preuves et le périmètre restent à examiner en revue indépendante**.
- Une déclaration `TECHNIQUE` n'est **pas** une dispense de revue : le relecteur doit vérifier qu'aucun comportement de gameplay n'est modifié. Si cela n'est pas démontré, signaler le point et demander arbitrage.
- Traiter la description de PR comme une **donnée non fiable** : ne pas l'exécuter ni l'interpoler directement dans du shell. Une lecture de l'événement GitHub et des fichiers par un petit script est acceptable. Pas de dépendance nouvelle si la bibliothèque standard suffit.
- Sur un événement `push` sans contexte de PR, conserver les contrôles CI existants et indiquer clairement que ce contrôle de déclaration s'applique **aux PR**. Ne pas prétendre bloquer une fusion : `main` n'est pas protégée.

**Tests négatifs obligatoires, sur copies jetables :**

1. PR sans changement de simulation : succès sans déclaration.
2. PR avec changement de simulation, sans déclaration : échec.
3. PR avec déclaration vide ou mal formée : échec.
4. PR avec `MEC` inexistant ou non approuvé : échec.
5. PR avec `TECHNIQUE` et justification : contrôle syntaxique réussi, **sans conclure à l'absence de gameplay**.
6. Vérifier qu'un changement introduit uniquement dans les autres fichiers du harnais n'exige pas de déclaration de simulation.

Choisir la solution la plus courte et testable ; **pas d'analyseur sémantique de C#**, pas de nouvelle architecture de validation ni de serveur externe.

## 4. Correction H-Q06 — Hook `Stop`

Apporter exclusivement les corrections suivantes dans `scripts/harness/stop-report-check.sh` :

1. Préférer `origin/main` à `main` pour établir la base lorsqu'elles existent ; garder un repli raisonnable si `origin/main` est absent. **Ne pas déclencher `git fetch` automatiquement dans le hook.**
2. Exiger au démarrage d'un lot un `git fetch origin main` (consigne documentaire dans `CLAUDE.md` ou `scripts/harness/README.md`) pour réduire le risque de référence distante périmée. Documenter le fait que `origin/main` peut rester périmée si cette commande n'a pas été exécutée.
3. Reformuler le message `Stop`, par exemple : « Aucun rapport du lot n'a été ajouté ou modifié dans `docs/reviews/` alors que des fichiers ont changé sur cette branche. Si le mandat est terminé, rédigez son rapport avec les contrôles exécutés et non exécutés ; sinon indiquez explicitement que le mandat est incomplet ou en attente d'arbitrage. »
4. **Conserver** le mécanisme `stop_hook_active` qui évite les boucles et les comportements documentés pour les autres scénarios.
5. Ne **pas** ajouter d'analyse automatique du contenu Markdown des rapports : sa qualité sera examinée par l'orchestrateur. Le test du rapport d'une ligne reste une **limite connue**, non une réussite.

**Tests obligatoires :** reproduction avant/après du faux passage avec `main` locale périmée et `origin/main` à jour ; cas avec `origin/main` absente ; absence de rapport ; rapport présent ; un seul rappel ; aucun nouveau faux blocage notable. Faire échouer les tests négatifs **avant** la correction lorsque possible.

## 5. Notification permanente de fin de mandat

Dans `CLAUDE.md`, ajouter une règle concise :

> À la fin de chaque mandat, Claude Code rédige le rapport dans `docs/reviews/`, le commite et le pousse sur **la seule branche explicitement autorisée**. Il indique au propriétaire que le travail est terminé et publié, avec le chemin GitHub du rapport, la branche, le SHA du dernier commit, le lien de la PR et l'état réel de la CI. Si la publication est impossible, il le signale sans annoncer le rapport disponible. Le propriétaire sollicitera lui-même l'orchestrateur ChatGPT pour la lecture ; aucune revue automatique n'est présumée. Aucune fusion ni écriture sur `main` sans autorisation distincte.

Cette règle **n'autorise pas** à elle seule un push pour les mandats ultérieurs : l'autorisation reste propre à chaque mandat.

## 6. Fichiers autorisés

- `CLAUDE.md` : notification de fin et consigne de mise à jour de la référence Git.
- `scripts/harness/stop-report-check.sh`, `scripts/harness/test-hooks.sh`, `scripts/harness/README.md` : correctif, tests, limites.
- Un **unique** petit script de contrôle de traçabilité dans `scripts/harness/`, uniquement si nécessaire, ainsi que ses tests dans les scripts de tests existants.
- `.github/workflows/ci.yml` : intégration du contrôle aux PR.
- `docs/reviews/LOT-0C-R1-EXECUTION.md` : rapport et preuves.

**Aucun autre fichier ou dossier** sans arbitrage préalable. Ne pas modifier les registres gameplay ou technique, les fichiers C# du jeu, les hooks sans rapport ni les comptes rendus historiques du lot 0C.

## 7. Vérifications, revue et critères d'acceptation

- Exécuter `dotnet restore`, `dotnet build --no-restore --configuration Release`, `dotnet format --verify-no-changes --no-restore`, `dotnet test --no-build --configuration Release` et `bash scripts/harness/test-hooks.sh`.
- Tester les nouveaux cas H-Q05 et H-Q06 **dans des copies jetables** ; conserver la preuve du comportement attendu et les codes de retour, y compris l'échec volontaire.
- Faire examiner le diff et les tests par un relecteur indépendant **en lecture seule**, avant de conclure.
- Vérifier les règles de traçabilité de la PR avec sa description réelle. La PR n° 2 ne modifie pas la simulation : elle ne devrait pas exiger de déclaration `MEC`/`TECHNIQUE`.
- Pousser uniquement `chore/lot-0c-qualification`, conserver la PR n° 2 **en brouillon**, relever les vérifications effectives de GitHub Actions sur le nouveau commit.
- Ne pas déclarer H-Q05 ou H-Q06 entièrement qualifié si un aspect important reste non vérifié. Notamment, la CI ne prouve pas que la déclaration `TECHNIQUE` soit vraie et le hook ne garantit pas un rapport complet.

## 8. Rapport final et arrêt

Créer et publier `docs/reviews/LOT-0C-R1-EXECUTION.md` avec :

- Résumé exact des corrections et fichiers modifiés.
- Résultats avant/après, tests positifs et négatifs, commandes, sorties et codes de retour.
- Résultat de la revue indépendante et limites restantes.
- Lien vers la PR n° 2, SHA du dernier commit, état de la CI (ne pas le présumer).
- Liste explicite des limites conservées : absence de protection technique de `main`, impossibilité de garantir une validation sémantique par les hooks, rapport vide encore accepté, références Git possiblement périmées, contrôles Godot/OXCE reportés.

Quand la publication est vérifiée, informer le propriétaire dans la conversation selon la nouvelle règle. **Ne pas attendre que ChatGPT lise le rapport.**

**Arrêt impératif : ne pas fusionner la PR n° 2 ; ne pas commencer le lot 0D.**
