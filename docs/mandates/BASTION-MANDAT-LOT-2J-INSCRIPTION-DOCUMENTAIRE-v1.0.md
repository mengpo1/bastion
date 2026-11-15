# BASTION — Mandat LOT-2J v1.0
## Inscription documentaire partielle de MEC-0001 et MEC-0002

**Date de préparation :** 15 novembre 2026  
**Dépôt cible :** `mengpo1/bastion`  
**Statut :** mandat préparé pour validation/transmission ; **aucune exécution, publication ou fusion effectuée au titre de ce document**.  
**Responsabilités :** propriétaire = décisions et autorisations ; ChatGPT = orchestration ; Claude Code = exécution ; relecteur distinct = revue en lecture seule.

### 0. Objet et autorisation

Le propriétaire a confirmé le 15 novembre 2026 la lecture de l'arbitrage A4.3A, puis autorisé la fusion de la PR nº 12. Il a ensuite validé la poursuite vers **l'inscription documentaire** de MEC-0001 et MEC-0002. Cette validation **ne constitue pas** une acceptation globale des mécaniques ni une autorisation de coder du gameplay.

**Condition de démarrage pour Claude Code :** recevoir du propriétaire la transmission explicite de ce mandat comme instruction d'exécution sur une branche dédiée. Avant de modifier le registre protégé, vérifier que cette autorisation couvre la présente version du mandat et les fichiers listés ci-dessous ; en cas de doute, s'arrêter. Le présent document local n'autorise, à lui seul, aucun push, aucune PR et aucune fusion.

Le but est **d'inscrire des principes déjà validés en conception**, sans réinterpréter ni compléter les 22 ambiguïtés encore ouvertes.

### 1. Référentiel obligatoire et état initial

Avant toute écriture, exécuter `git fetch origin main` et lire :

1. `CLAUDE.md` sur `main` : gouvernance, protection des registres, simplicité et traçabilité.
2. `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` : registre actuel, MEC-0001 uniquement.
3. `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md`, **§3** : **diff exact proposé, corrigé v1.2**, non encore appliqué.
4. `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md`, y compris §12 (ambiguïtés) et §14 (historique du correctif).
5. `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` et `docs/reviews/LOT-2I-EXECUTION.md` (§9).
6. `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`, ainsi que les rapports LOT-2F, LOT-2G, LOT-2H déjà fusionnés.
7. Les sources non intégrées à `main` mais identifiées par commit dans les documents du LOT-2I, **en lecture seule**, notamment la consolidation provisoire et les mandats v1.1/v1.2 sur `orchestration/mandats`. Ne pas les substituer aux décisions les plus récentes.

**Base vérifiée lors de la préparation :** `main` au commit de fusion PR nº 12 `9e119b64767553d2013795b4ccee4bb2db496fa2`. Recontrôler au démarrage ; ne pas présumer que `main` est resté identique.

**Important :** l'ancien mandat `BASTION-MANDAT-LOT-2I-INSCRIPTION-PARTIELLE-MEC-0001-v1.0.md` sur `orchestration/mandats` est historiquement conservé, mais **caduc pour exécution** : il prévoyait l'inscription des sauts et des chutes dans MEC-0001, alors que leur rattachement à MEC-0002 a été arbitré depuis.

### 2. Périmètre autorisé, sous condition de transmission explicite du mandat

**Branche proposée :** `docs/lot-2j-inscription-mec-0001-mec-0002`, créée depuis le dernier `origin/main`. Ne jamais travailler directement sur `main`.

Opération documentaire strictement limitée à :

1. **Modifier** `docs/gameplay/GAMEPLAY-DECISIONS.md` en y appliquant uniquement l'effet du **diff exact** du §3 du document LOT-2I, après vérification de son applicabilité. L'inscription :
   - conserve MEC-0001 et ses sous-décisions historiques ; ajoute les annotations prévues et le renvoi aux sauts/chutes/collisions dans MEC-0002 ;
   - crée MEC-0002 avec les **105 principes de conception** PE, GE, SA, CH, CO, ES, RP, EN ;
   - conserve les **deux décisions globales « reportée »**, classe `MODIFICATION-PROPOSEE`, état `non commencé`, périmètre « aucun changement de gameplay » ;
   - maintient explicitement les **22 ambiguïtés ouvertes** comme ouvertes, sans inventer de valeur, de seuil additionnel ni de loi physique définitive ;
   - respecte la lecture A4.3A confirmée le 15 novembre 2026 : saut descendant d'un étage = écart entre sols de 3 m, montée initiale non comptée, avec ou sans surcharge ; sans surcharge la réception normale est exempte de dégâts, avec surcharge des dégâts deviennent possibles.
2. **Créer** `docs/reviews/LOT-2J-INSCRIPTION-DOCUMENTAIRE.md` : autorisations, provenance des sources, diff avant/après, contrôles réellement exécutés, résultats et limites de preuve.
3. **Archiver une copie identique du présent mandat** dans `docs/mandates/BASTION-MANDAT-LOT-2J-INSCRIPTION-DOCUMENTAIRE-v1.0.md` après réception de l'original par Claude Code, et ajouter une unique ligne dans `docs/mandates/README.md` indiquant la provenance et le SHA-256 vérifié. Si cette copie n'est pas disponible, ne pas inventer son contenu ni son empreinte : signaler le blocage.

Aucun autre fichier n'est modifiable. **Ne pas** archiver la consolidation C2 ni les anciens mandats LOT-2I v1.1/v1.2 dans ce lot : leur éventuelle copie dans `main` demande une décision distincte ; conserver les renvois exacts vers leurs commits existants.

### 3. Interdictions

- Aucun changement dans `src/`, `tests/`, `.claude/`, `scripts/`, `.github/`, `CLAUDE.md`, `docs/decisions/`, `docs/references/` ou les rapports des lots précédents.
- Aucun code de gameplay, aucun nouvel équilibrage, aucun nouveau test de mécanique exécutable.
- Aucun changement de statut à `acceptée` ou `MODIFICATION-VALIDEE` pour les mécaniques globales.
- Aucun écrasement silencieux des décisions historiques, aucune attribution des résultats à des tests non exécutés.
- Pas de `git push`, création/mise à jour de PR, fusion ou rebase sans autorisation **séparée et explicite** du propriétaire.

### 4. Procédure minimale

1. Vérifier l'autorisation, la branche et les chemins protégés ; noter le SHA initial de `origin/main` et l'empreinte du registre.
2. Vérifier que le diff proposé est toujours applicable à une **copie** du registre. S'il n'est plus applicable ou si `main` a changé, arrêter et produire un diagnostic ; ne pas improviser une réécriture du registre.
3. Sur la branche dédiée uniquement, appliquer le diff exact autorisé au registre, sans extrapolation. Contrôler l'identité avec le texte de fiche proposé dans le LOT-2I v1.2.
4. Copier le mandat original octet pour octet sous `docs/mandates/` et actualiser l'index, avec empreinte vérifiée.
5. Faire relire **en lecture seule** le diff et les preuves par un agent distinct de l'exécutant ; traiter les constats dans le périmètre.
6. Rédiger le rapport de contrôle ; commiter localement les quatre chemins autorisés. S'arrêter avant publication.

### 5. Critères de sortie

- Seuls les quatre chemins de la section 2 ont été modifiés/ajoutés ; aucun changement de code, de harnais ou d'autre registre.
- MEC-0001 et MEC-0002 sont inscrites dans le registre, mais demeurent globalement **reportées** et **non implémentables**.
- 105 identifiants de conception présents une seule fois dans la nouvelle fiche ; cohérence avec la consolidation et la matrice LOT-2I v1.2.
- Ancien seuil de blessure de 0,25 étage et ancienne courbe `B(n)` non présentés comme actifs ; hauteur d'étage 3 m et seuil de chute ordinaire 3 m inclus correctement distingués.
- Les 22 ambiguïtés et paramètres ouverts ne sont ni masqués ni réputés tranchés.
- `git diff --check`, `bash scripts/harness/test-hooks.sh` et contrôles de cohérence sont exécutés et documentés avec leur résultat réel ; les tests .NET sont lancés s'ils sont disponibles, sinon marqués non exécutés. Les critères de tests futurs ne sont jamais qualifiés de tests réussis.
- Revue indépendante en lecture seule et rapport daté ; aucune affirmation de fidélité fonctionnelle à OXCE sans démonstration.

### 6. Arrêt et restitution

**Fin du mandat :** fournir le SHA du commit local, le nom de branche, les quatre fichiers et les résultats des contrôles, les écarts éventuels, les réserves et les prochaines autorisations requises. Aucun push, PR ou fusion sans feu vert distinct du propriétaire. L'inscription documentaire ne change pas l'interdiction d'implémenter MEC-0001 ou MEC-0002.
