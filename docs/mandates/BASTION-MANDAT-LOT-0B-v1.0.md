# BASTION — Mandat Claude Code LOT-0B

**Objet :** installer le harnais de développement, sans gameplay  
**Référence :** `BASTION-HARNAIS-LOT-0A-v0.2.md`, **validée par le propriétaire le 8 novembre 2026**  
**Statut :** mandat prêt à transmettre à Claude Code  
**Responsabilités :** propriétaire = validation ; ChatGPT = orchestration ; Claude Code = exécution.

## 1. Règle prioritaire

**Simplicité avant tout.** Choisir la solution la plus simple, compréhensible, testable et suffisante. Ne pas ajouter de couches, frameworks, scripts, agents ou automatisations sans besoin démontré. Avant tout ajout complexe, présenter la justification et demander un arbitrage.

## 2. Objectif unique

Mettre en place le **minimum opérationnel** permettant de développer Bastion sous contrôle : dépôt, instructions, décisions, compilation/tests élémentaires, protections raisonnables et CI. Ne pas développer de mécanique de jeu.

## 3. Avant toute écriture : état des lieux

1. Indiquer le répertoire de travail et si un dépôt Git existe déjà ; relever `git status`, la branche actuelle et les fichiers présents.
2. Vérifier les versions réellement disponibles de `.NET`, Godot .NET, Git et Claude Code. Ne pas présumer de leur installation ni de leur compatibilité. Garder le choix de version précis en attente tant qu'il n'est pas vérifié.
3. Identifier les fichiers/code préexistants. **Ne rien écraser, supprimer, déplacer ou migrer silencieusement.** Si un prototype est déjà présent, le préserver ; ne pas le présenter comme validé.
4. Signaler toute ambiguïté sur le répertoire cible, la propriété du dépôt, les droits ou un changement destructif. Dans ce cas, demander confirmation avant d'agir.
5. Si le dépôt Git existe, travailler sur une branche dédiée `chore/lot-0b-harnais`. Ne pas travailler directement sur `main`.

## 4. Travaux autorisés

### A. Gouvernance et documentation

- Créer ou adapter, **sans effacer le contenu utile existant** : `README.md`, `CLAUDE.md`, `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/decisions/TECHNICAL-DECISIONS.md`, `docs/references/OXCE-BASELINE.md`, `docs/mandates/` et `docs/reviews/`.
- Inscrire les règles permanentes dans `CLAUDE.md` : périmètre strict des mandats, simplicité, pas de mécanique sans décision explicite, pas de copie d'assets, pas de fusion/push sans approbation, preuves de tests obligatoires.
- Initialiser les registres **sans inventer de décisions validées**. Le document OXCE doit indiquer « version/commit à figer », sauf si une référence a effectivement été vérifiée.
- Conserver une référence à la spécification v0.2 validée, sans la modifier.

### B. Socle technique minimal

- Préparer une solution C# compilable avec un **test fumée sans logique de jeu** (par exemple, une assertion triviale sur une valeur technique), en choisissant un framework de tests simple et déjà disponible ou installable de façon contrôlée.
- Respecter l'architecture cible : simulation indépendante de Godot et interface distincte. **Ne créer que les projets nécessaires au lot 0B** ; documenter les futurs projets, sans générer de coquilles vides inutiles.
- Préparer le point d'entrée du projet Godot .NET **uniquement si l'environnement et les versions sont compatibles**. Sinon signaler le blocage sans improviser de contournement.
- Ajouter un `.gitignore` adapté et des dépendances déclarées/versionnées lorsque possible.

### C. Contrôles simples

- Configurer dans `.claude/settings.json` **le minimum utile de hooks**, en privilégiant :
  - un contrôle avant opération sensible (`PreToolUse`) pour signaler ou bloquer des tentatives explicites d'écriture dans les registres protégés, de modification hors mandat et de commandes destructives ;
  - un contrôle de clôture (`Stop`) pour vérifier qu'un rapport de fin est présent.
- Mettre les scripts dans `scripts/harness/`, lisibles et courts. Fournir au moins un test positif et un test négatif pour les contrôles ajoutés.
- Documenter honnêtement les limites : ces hooks ne reconnaissent pas tous les contournements et ne prouvent pas l'absence de changement de gameplay.
- Installer les hooks supplémentaires de la spécification 0.2 **seulement si nécessaires maintenant** ; sinon les reporter explicitement.

### D. Intégration continue

- Créer une seule CI minimale : restauration, compilation, format si disponible, tests.
- La CI doit échouer si la compilation ou un test échoue.
- Si aucun dépôt distant n'est accessible, préparer le fichier de workflow sans annoncer qu'une CI distante a tourné.

## 5. Interdictions explicites

- **Aucun gameplay** : déplacement, unités de temps, tirs, dégâts, IA, inventaire, cartes, progression, règles X-COM/OXCE, équilibrage, données de jeu.
- Aucun moteur de mods, convertisseur de données OXCE, moteur de rendu sophistiqué ou framework maison.
- Aucun asset X-COM original ni copie de code OXCE sans audit de licence et décision.
- Aucune modification de mécanique, même présentée comme simplification temporaire.
- Pas de `git push`, de fusion, de publication, de modification de `main`, d'effacement, ni de changement global de la machine sans autorisation explicite.
- Ne pas modifier, neutraliser ou contourner les règles du harnais sans mandat distinct.

## 6. Vérifications et preuves attendues

Fournir les **commandes réellement exécutées**, leur résultat, leur code de sortie et les limites :

1. `git status` et liste synthétique des fichiers créés/modifiés.
2. `dotnet --info` et `dotnet build` / `dotnet test` si l'environnement est opérationnel.
3. Au moins un essai autorisé et un essai interdit sur les hooks ; préciser la réaction réellement observée.
4. Lancement du projet Godot en mode headless **si réalisable** ; sinon justifier le report.
5. CI : lien vers l'exécution et statut si effectivement lancée ; sinon « workflow préparé, CI non exécutée ».
6. Revue indépendante du diff, **si un agent distinct est disponible** ; sinon signaler explicitement « revue non effectuée ».

Un succès déclaré sans sortie observable n'est pas une preuve suffisante.

## 7. Critères d'acceptation du lot

- Le travail respecte le périmètre et les fichiers antérieurs sont préservés.
- Les règles de gouvernance et les registres existent ; aucune approbation de gameplay n'est inventée.
- Le socle C# minimal compile et un test fumée passe, ou un empêchement précis est documenté.
- Les hooks installés disposent de tests démontrant leurs effets **et leurs limites**.
- Une CI minimale est préparée, avec état d'exécution clairement indiqué.
- Aucun changement de mécanique ni code de gameplay n'a été ajouté.
- Un rapport de fin permet à ChatGPT d'examiner le diff et les preuves.

## 8. Rapport final obligatoire

Rédiger `docs/reviews/LOT-0B-EXECUTION.md` avec :

1. Résumé factuel de ce qui a été réalisé.
2. Inventaire des fichiers modifiés et liens vers diff/commits locaux, s'il y en a.
3. Versions et décisions techniques vérifiées ; incertitudes restantes.
4. Tableau des vérifications : commande, résultat, code de sortie, preuve.
5. Tests de hooks réussis et échoués ; limites connues.
6. Blocages, risques et points nécessitant une décision du propriétaire.
7. **Déclaration explicite : « Aucun gameplay implémenté »**, si elle est vraie.

**Arrêt à la fin du lot 0B.** Ne pas enchaîner automatiquement sur la qualification 0C ni sur les mécaniques de jeu. Soumettre le rapport à l'orchestrateur et attendre les instructions.
