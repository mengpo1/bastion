# BASTION — Mandat LOT-2D v1.0
## Actualisation documentaire de MEC-0001 après le LOT-2C

**Statut : PRÉPARÉ — l'exécution exige une nouvelle autorisation explicite du propriétaire.**
**Dépôt :** `mengpo1/bastion`
**Branche du mandat :** `orchestration/mandats`
**Base attendue de `main` :** `6497e6b4c12b2804bc6b7c99a49fc645a820983e` — à revérifier avant exécution.
**Branche proposée pour Claude :** `docs/lot-2d-mec-0001-actualisation`.

## 1. But et règles

Documenter dans la fiche MEC-0001 les décisions explicites prises **après le LOT-2C**, sans valider la mécanique globale et **sans gameplay**.

- Garder la **classe** `MODIFICATION-PROPOSEE`, la **décision globale** « reportée — arbitrages complémentaires requis », le **périmètre autorisé** « aucun changement de gameplay » et l’**état d’implémentation** « non commencé ».
- Mettre **Z1** au statut « acceptée » ; articuler son effet sur l'ancienne S5 : plus de sélection normale d'une destination hors zone atteignable ; une interruption imprévue reste possible.
- Enregistrer les nouveaux choix du propriétaire sur les murs, diagonales, niveaux, moyens de déplacement vertical, chutes et encombrement ; **ne pas inventer de paramètres**.
- Pour chaque point, distinguer explicitement : décision du propriétaire, référence OXCE **vérifiée**, écart à OXCE **établi**, information OXCE **à vérifier**.
- Appliquer la politique D4 : étude du comportement OXCE mais aucune copie de code, de données ou d'assets.
- Ne modifier ni code ni scripts, tests, CI, hooks, configuration, autres mécaniques ni équilibrage.

## 2. Preuve de décision fournie par l'orchestrateur

**Provenance :** paroles du propriétaire dans la conversation Bastion du **8 novembre 2026**. Claude Code ne peut consulter cette conversation : ne pas déclarer le contraire. Le propriétaire doit **autoriser explicitement le LOT-2D** avant que ces transcriptions soient utilisées pour écrire dans le registre protégé. Cette autorisation ne vaut pas approbation globale de MEC-0001.

| Réf. temporaire | Paroles du propriétaire | Portée du choix |
|---|---|---|
| Z1 | « Pour MEC-0001, je valide définitivement Z1 : afficher la zone atteignable selon les TU et les informations connues, et interdire la sélection d'une destination hors de cette zone. » | Z1 **acceptée** : zone accessible fondée sur les informations connues ; interdiction de destination hors zone ; interruption imprévue maintenue. |
| N1 | « Modèle B avec les diagonales alors » | Le modèle B précédemment présenté : terrain constitué de **cases et de murs séparant les cases** ; huit directions maintenues. |
| N2 | « Regle permissive » | Dans le modèle B, diagonale permise si **au moins un** des deux passages orthogonaux autour du coin est ouvert ; interdite si les deux sont bloqués. Ne pas réécrire S4 sur les unités voisines. |
| N3 | « B » | Choix « plusieurs étages dès MEC-0001 » au lieu d'un report ; représentation de principe (x, y, z). |
| N4 | « B » | Plusieurs moyens de changement de niveau prévus dès la conception : escaliers, échelles et ascenseurs ; les chutes sont confirmées séparément ci-dessous. |
| N5 | « A » | Chutes **volontaires et involontaires** autorisées. |
| N6 | « A » | Dégâts de chute croissants avec la hauteur. |
| N7 | « A » | Les petites chutes n'infligent pas de dégâts ; seuil exact à décider. |
| N8 | « B » | Les caractéristiques individuelles et les équipements **peuvent modifier** les conséquences d'une chute. |
| N9 | « B » | L'armure peut protéger mais son poids peut également aggraver les conséquences d'une chute. |
| N10 | « A » | Le **poids de l'inventaire** (armes, munitions, matériel) contribue aussi à l'effet de la charge lors d'une chute. |
| N11 | « A » | Le poids total porté affecte aussi le déplacement normal. |
| N12 | « Pénalité progressive avec un état encombré sans pouvoir bouger si le poids est trop important » | Souhait d'une pénalité progressive de surcharge et d'un état compréhensible pour le joueur. **Cette formulation a été précisée ultérieurement : ne pas créer de seuil.** |
| N13 | « Oui en fonction de la force mais en t'inspirant de ce que tu as proposé » | La **Force** détermine l'effet de la surcharge ; souhait d'une pénalité progressive. |
| N14 | « Pas de seuil mais comme oxce » | **Décision la plus récente et prioritaire** : appliquer le principe d'OXCE **sans seuil d'immobilisation supplémentaire**. Le personnage ne peut plus avancer seulement quand ses TU restantes ne permettent pas de payer le pas. « Encombré » peut rester un simple **indicateur informatif**, sans nouveau modificateur ni statut technique décidé. |

**La question « progressif ou par paliers sur le coût d'un pas » a été abandonnée**, remplacée par le modèle OXCE. Ne pas présenter comme acceptée une augmentation du coût des pas liée au poids. Ne pas consigner une immobilisation automatique à 200 % de la Force : c'était une proposition non validée et explicitement écartée.

## 3. Source OXCE, vérification et limites

**Référence :** `MeridianOXC/OpenXcom`, commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b`, version OXCE 8.7.1, règles `xcom1`, paramètres par défaut, sans mods (`docs/references/OXCE-BASELINE.md`).

**Comportements confirmés par lecture du code source, sans exécution en jeu :**

- `src/Savegame/BattleUnit.cpp:2709-2726` : à la récupération des TU, si le rapport Force/Poids est inférieur à 1, les TU sont multipliées par ce rapport et tronquées. Le calcul est suivi d'autres pénalités possibles (ex. blessures). Ce n'est **pas** une augmentation directe du coût des pas.
- `src/Savegame/BattleUnit.cpp:4852-4861` : poids porté = poids de l'armure + somme du poids des objets d'inventaire.
- `src/Battlescape/UnitWalkBState.cpp:295-323` : arrêt si le prochain pas dépasse les TU restantes.
- `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md` : coût des diagonales et distinction sol/murs/objets ; étude documentaire, non testée en exécution.

**Non vérifié pour ce mandat** : fonctionnement exact d'OXCE des escaliers, échelles, ascenseurs, chutes, dégâts de chute et influences de la charge sur les chutes ; ne pas affirmer que ces choix reproduisent OXCE. Si une nouvelle étude source est indispensable à une comparaison, la demander dans un lot de recherche distinct, sans retenir une analogie comme preuve.

## 4. Mise à jour à effectuer après autorisation

Modifier au plus **3 fichiers** :

1. **`docs/gameplay/GAMEPLAY-DECISIONS.md`** :
   - Changer Z1 « proposée à confirmer » en « acceptée le 8 novembre 2026 », avec son origine et sa portée ; modifier le texte d'en-tête de la fiche et la liste des points ouverts en conséquence.
   - Conserver S5 **comme historique** de la première décision, mais indiquer explicitement qu'elle est **supplantée pour la sélection normale par Z1** ; interrompre si un obstacle/unité inconnue apparaît demeure conforme à S8/S11. Ne pas prétendre que le comportement en cas d'augmentation imprévue du coût est totalement défini.
   - Ajouter les nouvelles sous-décisions N1 à N14 (ou renuméroter clairement dans le registre, sans casser les liens S1–S12), sous une rubrique distincte datée ; **fusionner les étapes de surcharge en la décision finale N14** sans perdre la provenance.
   - Revoir les points ouverts pour ne plus présenter comme non décidés le modèle B, la verticalité, les chutes ou Z1. Garder **ouverts** : géométrie précise des murs/angles et portes, coûts de terrain et de changements d'étages, formule/valeurs des dégâts de chute, hauteur de chute sans dégâts, caractéristiques/modificateurs, actions volontaires/involontaires, règle précise des échelles/ascenseurs, cas de coût imprévu, visibilité détaillée, coût minimal et départage, et tout autre paramètre non explicitement accepté.
   - Maintenir le gabarit et les règles de gouvernance. La mécanique entière reste **non approuvée** ; aucun développement autorisé.
2. **`docs/references/OXCE-BASELINE.md`** : corriger **uniquement** l'affirmation devenue obsolète « Aucune fiche `MEC` » : désormais MEC-0001 est une fiche documentaire incomplète et non approuvée, toujours sans gameplay implémenté ; ne pas changer la référence OXCE.
3. **`docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`** : rapport court contenant décisions, statuts, passages OXCE établis/non vérifiés, changements effectifs, limites, contrôles et revue indépendante.

**Ne toucher à aucun autre fichier.** Aucune modification dans `main` directement.

## 5. Travail, contrôles et livraison

1. **Attendre l'accord explicite du propriétaire pour exécuter le LOT-2D.** Cet accord autorise le lot documentaire (y compris registres protégés) et la publication d'une PR en brouillon, mais **aucun gameplay ni aucune fusion**.
2. Lire ce mandat **directement sur la branche `orchestration/mandats`** à son SHA. Ne pas le recopier ni l'archiver.
3. Faire `git fetch origin main` et vérifier le commit de base ci-dessus et l'absence de nouvelle modification conflictuelle. Arrêter si la base a changé ou si un autre lot a modifié MEC-0001.
4. Créer la branche `docs/lot-2d-mec-0001-actualisation` à partir de `origin/main`.
5. Rédiger la modification limitée aux trois fichiers. Relecture indépendante par un agent distinct, en lecture seule, vérifiant notamment que Z1 ne reste pas « à confirmer », que N14 remplace la proposition de seuil, et qu'aucune fidélité OXCE non prouvée n'est déclarée. Corriger les constats avant publication ; faire `git diff --check`, vérifier la liste exacte des fichiers.
6. Déclarer les tests non exécutés si non lancés ; tests .NET non requis pour ce lot documentaire. Documenter uniquement les contrôles effectivement réalisés, sans annoncer de CI réussie avant son résultat.
7. Committer/pousser **uniquement sur la branche du lot** et ouvrir une **PR en brouillon** vers `main`, si et seulement si le propriétaire autorise l'exécution/publication.
8. Après publication, arrêter et signaler au propriétaire simplement : branche, commit, PR, chemin du rapport et état réel de la CI. L'orchestrateur ChatGPT vérifiera directement la PR à « Claude a terminé ».

## 6. Interdictions finales

Aucune fusion, aucun changement de `main`, aucune acceptation globale de MEC-0001, aucune implémentation, aucun test de gameplay, aucune reproduction ou utilisation des fichiers OXCE/X-COM. Les arbitrages encore ouverts ne sont pas résolus par déduction.
