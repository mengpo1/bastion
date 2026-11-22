BASTION — Mandat de clôture documentaire MEC-0003 — Lot 1B
Statut : préparé, en attente d'autorisation du propriétaire.
1. Objectif
Mettre la documentation de Bastion en cohérence avec la fusion du lot 1 de MEC-0003.
Référence de fusion : PR #19, commit de fusion `eeebc57001cd73a1ff1b45375960dc9b99ae3281`.
Cette opération est exclusivement documentaire.
2. Travail demandé
A. README.md
Actualiser la présentation du projet pour indiquer :

* Le harnais est installé et opérationnel.
* Le premier incrément de gameplay, MEC-0003, est implémenté, testé et intégré.
* La simulation C# comprend désormais la marche sur terrain plat.
* L'interface Godot n'est pas encore créée.

Conserver une description factuelle de l'architecture existante.
B. docs/gameplay/GAMEPLAY-DECISIONS.md
Pour MEC-0003 uniquement :

* Proposer le remplacement de « État d'implémentation : non commencé » par « intégré ».
* Ajouter une référence documentaire concise à la PR #19, au commit de fusion et aux tests réalisés, sans modifier les règles ni les résultats attendus.

Conserver l'historique de la fiche, notamment les mentions exactes à la date de son inscription.
Ne modifier aucun autre champ de gameplay.
C. Réserves
Ne pas lever artificiellement RL-11, RL-13 ou les limites de couverture encore ouvertes.
Ne modifier ni MEC-0001 ni MEC-0002.
3. Procédure

1. Exécuter `git fetch origin main` et vérifier la base.
2. Contrôler les deux documents en lecture seule.
3. Préparer le diff documentaire proposé.
4. Soumettre ce diff à l'autorisation explicite du propriétaire avant toute écriture dans le registre protégé.
5. Après autorisation, appliquer exclusivement les corrections approuvées.
6. Vérifier le diff et exécuter les contrôles applicables.
7. Produire un rapport de clôture documentaire.

4. Restrictions

* Aucun changement de code C#.
* Aucun changement des tests ou du harnais.
* Aucune nouvelle règle de gameplay.
* Aucun nouveau framework ni projet.
* Aucune fusion, publication ou suppression de branche sans autorisation distincte.

Le présent mandat autorise uniquement sa préparation et les vérifications en lecture seule. Il n'autorise pas encore son exécution.
