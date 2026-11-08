# BASTION — Mandat Claude Code LOT-0B-CLOTURE

**Objet :** corriger les trois non-conformités restantes du harnais, publier le lot 0B et vérifier la CI.  
**Date :** 8 novembre 2026  
**Statut :** autorisé par le propriétaire dans la conversation Bastion du 8 novembre 2026.  
**Branche de travail :** `chore/lot-0b-harnais`.  
**Références :** spécification `BASTION-HARNAIS-LOT-0A-v0.2.md` validée ; `docs/reviews/LOT-0B-RETOUR-1.md` ; `docs/reviews/LOT-0B-EXECUTION.md` ; retour d'orchestration du lot 0B.

## 1. Règle fondamentale

**Simplicité avant tout.** Faire seulement ce qui est demandé, avec les changements minimaux nécessaires. Pas de refonte, de nouveaux outils ou de nouvelles abstractions. **Aucun gameplay.**

## 2. Autorisations explicites

Le propriétaire autorise **uniquement dans le cadre de ce mandat** :

- Les corrections **NC-1, NC-2, NC-3**, y compris l'édition des fichiers protégés concernés.
- L'archivage, **sans modification du contenu**, de la spécification v0.2 et du précédent retour de l'orchestrateur dans `docs/mandates/`, ainsi que la mise à jour de l'index documentaire.
- La création exceptionnelle de `main` avec un **commit initial vide**, selon le plan du rapport `LOT-0B-RETOUR-1.md` §7.
- La fusion de cette nouvelle branche `main` **dans `chore/lot-0b-harnais` uniquement**, pour établir un historique commun **sans réécrire les commits existants**.
- Le push de **ces deux seules branches** et l'ouverture d'une **pull request en brouillon** de `chore/lot-0b-harnais` vers `main`.
- L'observation et la consignation du résultat réel des exécutions GitHub Actions.

**Non autorisés :** fusion de la PR dans `main`, approbation automatique, changement de gameplay, push forcé, rebase, suppression, changement de branche cible, publication d'une release, changement de permissions ou contournement des hooks.

Les demandes d'accord affichées par les hooks restent à respecter. Cette autorisation ne dispense pas des confirmations de Claude Code ou de GitHub.

## 3. Corrections avant publication

**NC-1 — `docs/gameplay/GAMEPLAY-DECISIONS.md`**

- Remplacer le gabarit `G-NNN` par `MEC-NNNN`.
- Ajouter les champs requis par le §3.1 de la v0.2 : système, description, classe (`OXCE-REFERENCE`, `MODIFICATION-PROPOSEE`, `MODIFICATION-VALIDEE`, `A-VERIFIER`), référence et preuves, changement demandé, décision explicite du propriétaire avec date et preuve, périmètre, tests de référence et de modification, état d'implémentation séparé.
- **Ne créer aucune décision de gameplay.** Laisser le registre vide.

**NC-2 — `CLAUDE.md`**

- Compléter les rôles avec « relecteur indépendant » et « contrôles automatiques ».
- Ajouter qu'une idée de conversation n'est pas une décision validée.
- Ajouter l'interdiction d'affirmer une fidélité à OXCE sans référence vérifiable et tests adaptés.
- Rendre explicite l'interdiction de modifier l'équilibrage sans accord.
- Conserver toutes les règles existantes, dont « simplicité avant tout ».

**NC-3 — Hook `Stop`**

- Ajouter au rappel de fin de session la demande d'indiquer dans le rapport **les contrôles non exécutés**.
- Ne pas inventer de détection automatique de ces contrôles : **simple message**, pas de nouveau mécanisme.
- Mettre à jour les tests pertinents si nécessaire ; démontrer que le hook s'arrête sans boucle.

**Documents de référence**

- Copier à l'identique `BASTION-HARNAIS-LOT-0A-v0.2.md` et `BASTION-LOT-0B-RETOUR-ORCHESTRATEUR.md` dans `docs/mandates/` ; vérifier leurs SHA-256 respectifs :
  - `d81a1c2e77414fef25d7c7ef29b8f13820e82b09028c33dbba25bf919030b001`
  - `98ad142f4814d00c063fde78f9786be90b8bbbeff1a3a9c095550ae807973223`
- Ne **pas** modifier le mot « PROPOSÉ » à l'intérieur de la spécification historique. Indiquer séparément dans `docs/mandates/README.md` qu'elle a été **validée le 8 novembre 2026**.
- Archiver ce mandat dans `docs/mandates/`, sans en élargir le périmètre.

## 4. Arbitrages techniques approuvés

- Conserver **.NET 10** provisoirement avec `global.json` (`10.0.100`, `latestFeature`), sans affirmer la compatibilité Godot tant qu'elle n'est pas testée.
- Conserver `Bastion.slnx` et `chore/lot-0b-harnais`.
- Accepter provisoirement les deux limites documentées : faux positif sur une commande citant `rm -rf` et détection incomplète des dépendances Godot non utilisées.
- **Conserver `TreatWarningsAsErrors`**, y compris pour les alertes NuGet ; si la CI échoue sur un avis de sécurité, en rendre compte plutôt que le masquer.
- Ne marquer aucune mécanique de gameplay « validée ». Les décisions techniques non couvertes par l'accord explicite restent proposées ou à confirmer.

## 5. Vérifications locales, puis plan Git

**Avant toute opération distante :**

1. Vérifier `git status`, la branche courante, les commits locaux et `git ls-remote origin` ; s'assurer que le dépôt distant n'a pas changé. **Si `main` ou d'autres commits distants existent déjà, arrêter le plan d'initialisation et demander arbitrage.**
2. Appliquer les corrections et archiver les documents sur `chore/lot-0b-harnais` ; créer un ou plusieurs commits normaux, sans réécrire les cinq précédents.
3. Exécuter et relever les codes de retour de `dotnet restore`, `dotnet build --no-restore --configuration Release`, `dotnet format --verify-no-changes --no-restore`, `dotnet test --no-build --configuration Release` et `bash scripts/harness/test-hooks.sh`.
4. Vérifier l'absence de gameplay, de secrets dans le diff et de modifications hors périmètre. Si ces vérifications échouent ou sont impossibles, s'arrêter et le signaler.

**Puis seulement, appliquer le plan Git approuvé dans `LOT-0B-RETOUR-1.md` §7 :**

1. Créer `main` à partir d'un **commit vide, sans parent**, sans écrire de fichier sur `main`.
2. Depuis `chore/lot-0b-harnais`, fusionner `main` **dans la branche du lot** avec `--allow-unrelated-histories`, sans rebase.
3. Vérifier le graphe Git et le diff `main...chore/lot-0b-harnais` : seuls les fichiers du lot 0B doivent apparaître.
4. Pousser `main`, puis `chore/lot-0b-harnais`, **sans `--force`**.
5. Ouvrir la PR **en brouillon** vers `main`, avec un résumé, les tests et les limites ; **ne pas la fusionner**.

**Si un push est refusé, si le dépôt distant a changé, si l'historique est inattendu ou si une confirmation nécessaire n'est pas obtenue : arrêter et demander arbitrage, sans contournement.**

## 6. CI et conditions de clôture

- Fournir le **lien vers la PR** et les **liens vers les exécutions GitHub Actions** réellement observées, avec statut, étapes en échec et identifiant du commit testé.
- Vérifier que la CI s'exécute sur la branche ou sur la PR ; ne pas déclarer le critère NC-4 satisfait avant de disposer d'une preuve d'exécution.
- En cas de CI rouge, diagnostiquer ; n'effectuer que les ajustements strictement autorisés ci-dessus. Tout autre correctif exige un nouvel arbitrage.
- Vérifier que `main` ne contient que le commit d'initialisation vide, que la PR est **Draft**, et qu'aucune fusion dans `main` n'a eu lieu.
- La protection de `main` sur GitHub relève d'une **étape distincte à confirmer**, et non d'une permission de la mettre en place silencieusement.

## 7. Rapport final et arrêt

Créer un **nouveau rapport de clôture** `docs/reviews/LOT-0B-CLOTURE.md` (sans réécrire `LOT-0B-RETOUR-1.md`), contenant :

- Corrections effectuées (NC-1 à NC-3), avec fichiers et commits.
- Contrôles locaux : commandes, codes de sortie et nombres de tests.
- Graphe Git final : branches et identifiants des commits, sans réécriture de l'existant.
- URL de PR, état Draft, preuve de la CI et statut réel.
- Limites acceptées, vérifications reportées, anomalies non résolues.
- Déclaration explicite : **« Aucun gameplay implémenté ; aucune fusion dans main. »**, si exacte.

Préparer le rapport avant le premier push avec la mention « CI distante non exécutée à ce stade ». Après la première CI, y ajouter **une seule fois** les preuves réelles (PR, statut, liens), créer un nouveau commit sur la branche du lot et pousser cette branche. Vérifier ensuite la CI de ce dernier commit et donner son statut dans le message final, **sans réécrire de nouveau le rapport uniquement pour actualiser le statut**. Si un push est refusé ou une vérification échoue, signaler l'état exact et s'arrêter.

**S'arrêter à l'issue du lot 0B.** Ne pas démarrer le lot 0C, créer de moteur Godot ou développer des mécaniques sans nouveau mandat.
