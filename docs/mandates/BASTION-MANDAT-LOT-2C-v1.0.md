# BASTION — Mandat LOT-2C v1.0
## Consolidation documentaire des décisions MEC-0001 (sans gameplay)

**Statut : PRÉPARÉ — exécution non autorisée par la seule publication.**  
**Dépôt :** `mengpo1/bastion`  
**Branche du mandat :** `orchestration/mandats`  
**Base attendue :** `main`, commit `a2418df007b486431dc25895dd4aca5230e58dc6` (à revérifier avant exécution).  
**Branche proposée :** `docs/lot-2c-mec-0001-decisions`.

## 1. Objet

**Consigner fidèlement les décisions de conception déjà exprimées par le propriétaire pour MEC-0001**, et identifier ce qui reste à décider avant toute autorisation de développement.

- **Ne pas implémenter de gameplay, tests de gameplay, IA, Godot ou interface.**
- **Ne pas déclarer MEC-0001 globalement « acceptée » : son périmètre complet n'est pas encore arbitré.** Les décisions individuelles explicitement acceptées ne constituent pas une approbation globale de la mécanique.
- **Ne pas transformer une proposition du propriétaire en décision acceptée.**
- Garder la structure existante du registre ; pas de nouveau système de suivi, outil, hook ni automatisation.

## 2. Sources de décision

Références existantes : `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`, `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`, `docs/gameplay/GAMEPLAY-DECISIONS.md` et `docs/references/OXCE-BASELINE.md` sur `main`. Le code OXCE figé est `MeridianOXC/OpenXcom` commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, lecture seulement, **pas d'exécution d'OXCE attestée**.

**Preuve fournie par l'orchestrateur :** les déclarations ci-dessous sont des transcriptions des messages directs du propriétaire dans la conversation Bastion du **8 novembre 2026**. Claude Code ne doit **pas** prétendre avoir consulté cette conversation ; il doit attribuer la transcription à ce mandat, en précisant qu'elle est à confirmer par l'autorisation explicite d'exécution du LOT-2C. En cas de divergence ou de doute, arrêter, sans compléter par déduction.

### A. Déclarations du propriétaire explicitement validantes

1. **Huit directions :** « Pour MEC-0001, je valide les déplacements à 8 directions, diagonales incluses. »
2. **Coût diagonal :** « Pour MEC-0001, je valide le coût des diagonales : coût de la case d'arrivée multiplié par 1,5, arrondi à l'entier inférieur (comme OXCE). »
3. **Angle bloqué :** « Pour MEC-0001, je valide la règle de passage diagonal : B — diagonale interdite uniquement lorsque les deux cases orthogonales voisines sont bloquées. »
4. **Unité adjacente :** « Pour MEC-0001, je valide qu'une unité voisine ne compte pas comme obstacle pour la règle des diagonales. »
5. **TU — décision initiale, à replacer dans la chronologie :** « Pour MEC-0001, je valide le déplacement partiel lorsque les TU sont insuffisantes, comme dans OXCE. » **Voir évolution §2.B : ne pas la présenter sans sa nuance ultérieure.**
6. **Destinations connues :** « Pour MEC-0001, les cases actuellement visibles et les cases déjà explorées sont autorisées comme destinations de déplacement. »
7. **Trajet connu :** « Pour MEC-0001, je valide que le trajet doit rester entièrement dans des cases actuellement visibles ou déjà explorées. »
8. **Dernier terrain connu :** « Pour MEC-0001, je valide le calcul du trajet selon le dernier état connu du terrain, avec interruption lorsqu'un obstacle inconnu est rencontré. »
9. **Découverte d'obstacle :** « Pour MEC-0001, je valide qu'un obstacle inconnu rencontré pendant un déplacement devient connu du joueur et actualise sa connaissance du terrain. »
10. **Occupation :** « Pour MEC-0001, je valide qu'une case occupée par une autre unité est infranchissable, aussi bien pour la traversée que pour la destination. »
11. **Rencontre d'un ennemi caché :** « Pour MEC-0001, je valide qu'une unité cachée rencontrée pendant un déplacement est révélée au joueur. »
12. **Disparition d'une unité :** « Pour MEC-0001, je valide qu'une unité révélée redevient cachée lorsqu'elle n'est plus observable, sans indication persistante de sa position. »

### B. Proposition ultérieure à distinguer d'une décision globale

Le propriétaire a écrit : « Pour MEC-0001, **je souhaite proposer** l'affichage de la zone atteignable et interdire de sélectionner une destination hors de cette zone. » Puis, après clarification, il a acquiescé (« Ok »).

**Ne pas étiqueter cette phrase « je valide » :** la consigner explicitement comme **proposition de fonctionnement**, à confirmer pour la fiche définitive. Cette proposition remplace, pour une sélection normale de destination, l'idée d'un ordre au-delà des TU exécuté partiellement : si la case n'est pas atteignable avec les TU connues, la sélection est interdite. En revanche, la règle déjà validée d'arrêt devant un obstacle inconnu demeure. **Ne pas inventer une décision** concernant un changement de coût imprévu en cours de trajet.

## 3. Ce qui demeure ouvert

Ne pas transformer les propositions du LOT-2B en décisions du propriétaire :
- carte à un seul niveau, taille des unités, modèle précis du coût d'entrée par case, modèle de murs et obstacles ;
- valeurs réelles des coûts du terrain, capital initial et renouvellement des TU ;
- calcul de chemin garantissant le coût minimal et départage déterministe des chemins égaux ;
- orientation/rotation, énergie et interruptions non encore spécifiées ;
- conditions détaillées de visibilité et périmètre des règles de brouillard de guerre en dehors du déplacement ;
- interface précise de la zone accessible, présentation et sélection ;
- situation où un coût réel ou une occupation non connue rend un trajet devenu non payable ou non réalisable.

**Attention au changement du LOT-2B :** celui-ci supposait provisoirement toutes les unités connues et reportait la visibilité. Les décisions explicites ci-dessus introduisent maintenant les cases explorées, les informations de terrain mémorisées et les unités cachées. **Ne pas conserver l'ancienne hypothèse « toutes les unités connues » comme règle acceptée.**

## 4. Modification du registre — sous réserve de l'autorisation du LOT-2C

Modifier uniquement `docs/gameplay/GAMEPLAY-DECISIONS.md` pour **ouvrir la fiche MEC-0001 comme fiche de conception incomplète**, conforme au gabarit :
- **Classe :** `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'a pas été acceptée ; **état d'implémentation :** `non commencé`.
- **Décision du propriétaire (fiche globale) :** « reportée — arbitrages complémentaires requis » ; distinguer dans le texte les **sous-décisions de conception acceptées le 8 novembre 2026** et la proposition relative à la zone atteignable.
- **Périmètre de changement de gameplay autorisé :** **aucun**. Le contenu du registre documente les arbitrages, il n'est pas un mandat d'implémentation.
- **Sources/provenance :** citer les transcriptions dans ce mandat, le LOT-2A, le LOT-2B, la version OXCE figée ; indiquer le niveau de preuve (lecture du code, pas observation exécutée).
- Réduire/ajuster uniquement l'en-tête « Aucune mécanique n'est enregistrée à ce jour » pour décrire justement **une fiche proposée non acceptée** ; conserver la règle qu'aucun gameplay n'est autorisé sans approbation globale explicite.
- Tests de référence/modification : **critères futurs**, sans test exécuté ni fidélité démontrée à OXCE.
- Écrire de façon claire et compacte ; **ne pas copier les citations longues** dans la fiche : le présent mandat porte la transcription des preuves.
- Si le registre ou ses règles ne permettent pas de rendre cette distinction sans ambiguïté, **s'arrêter et signaler le problème** plutôt que déclarer la fiche acceptée.

Créer en complément un rapport court `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md` : changements, tableau « accepté / proposé / ouvert », preuve et limites, vérifications, revue indépendante, points à arbitrer.

**Fichiers autorisés (deux exclusivement) :**
1. `docs/gameplay/GAMEPLAY-DECISIONS.md`
2. `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md` (nouveau)

Aucune autre modification (notamment `CLAUDE.md`, code, CI, scripts, autres registres, anciennes études).

## 5. Contrôles et publication

1. **Ne rien exécuter avant autorisation explicite du propriétaire pour LOT-2C, y compris l'écriture du registre protégé.** Une autorisation d'exécution valide également la transcription des déclarations §2 comme base documentaire de cette inscription ; elle ne vaut **pas** acceptation globale de MEC-0001 ni autorisation de développer.
2. Lire le mandat **directement** sur `orchestration/mandats` au commit indiqué ; ne pas le recopier ni l'archiver.
3. `git fetch origin main` et contrôler la base attendue. Si `main` a avancé ou qu'une fiche MEC-0001 existe déjà, arrêter pour revue de l'écart.
4. Travailler sur la branche `docs/lot-2c-mec-0001-decisions` créée depuis `main`.
5. Revue indépendante en lecture seule, par un agent distinct : exactitude des transcriptions et statuts, absence d'approbation globale ou de gameplay, limites OXCE, conformité du gabarit et diff.
6. Contrôler les deux fichiers autorisés et `git diff --check`. Les tests .NET ne sont pas requis pour ce lot documentaire ; documenter les commandes réellement exécutées. CI après publication à vérifier sans inventer d'état.
7. Si publication autorisée dans l'accord d'exécution : commit/push **uniquement** sur la branche de lot et PR **en brouillon** vers `main`. **Aucune fusion**, aucun push direct sur `main`.
8. Dire brièvement au propriétaire que le travail est publié sur GitHub. ChatGPT retrouvera directement la PR et le rapport à « Claude a terminé » : aucun compte rendu à copier dans la conversation.

## 6. Arrêt

S'arrêter après publication de la fiche **proposée** et du rapport dans la PR en brouillon. Ne pas démarrer de gameplay ni inscrire une décision globale « acceptée » sans nouvel arbitrage explicite du propriétaire.
