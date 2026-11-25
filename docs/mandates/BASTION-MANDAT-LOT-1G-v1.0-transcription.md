BASTION — Mandat LOT-1G v1.0
Implémentation de MEC-0004
Statut : PRÉPARÉ — exécution non autorisée
Dépôt : `mengpo1/bastion`
Base : `main`, commit `1fa2769e309ea74390b678836d3203a16f7e66d4`
Branche proposée : `claude/lot-1g-implementation-mec-0004`
1. Objectif
Implémenter intégralement le périmètre accepté de MEC-0004 — Gestion élémentaire des tours et récupération des ressources.
Référence normative : `docs/gameplay/GAMEPLAY-DECISIONS.md`, fiche MEC-0004.
La fiche est acceptée le 23 novembre 2026 et intégrée dans `main` par la PR #25.
Aucune nouvelle règle de gameplay ne doit être inventée.
2. Simulation C#
Ajouter à `Bastion.Simulation` la gestion minimale des tours.
Fonctions attendues :

* Conserver le numéro de tour, initialement égal à 1.
* Gérer les plafonds et les récupérations configurables des TU et de l'énergie.
* Valider les paramètres et les états initiaux selon MEC-0004.
* Exécuter une fin de tour explicite.
* Calculer les deux récupérations et incrémenter le compteur.
* Conserver la position et l'orientation.
* Retourner un nouvel état immuable.

Profil initial : 60 TU maximales, 60 récupérées, 100 d'énergie maximale, 20 récupérées.
Architecture :

* Conserver `MovementModel.CreateState` et son contrat existant.
* Préférer une petite structure dédiée à la gestion des tours, plutôt qu'une refonte du moteur de mouvement.
* Réutiliser `UnitState` pour représenter les ressources et la position.
* Ne pas créer de moteur générique multi-unités, d'ordonnanceur ou de gestionnaire de phases.
* Ne pas introduire de dépendance Godot dans la simulation.
* Calculer les additions plafonnées sans débordement d'entier.

Le moteur de tours devra rester compatible avec les états retournés par le moteur de déplacement.
3. Client Godot
Modifier le prototype existant dans `src/Bastion.Client.Godot/` pour ajouter le scénario 4 décrit par MEC-0004.
Conserver les scénarios 1, 2 et 3 avec leurs comportements et ressources initiales.
Pour le scénario 4 :

* Reprendre la carte du scénario 1.
* Initialiser l'unité en (1,4), orientée N.
* Initialiser 12 TU, 35 points d'énergie et le tour 1.
* Permettre de se déplacer avec les mêmes commandes et règles que MEC-0003.
* Ajouter la commande T pour terminer le tour.
* Ajouter la sélection et la réinitialisation par la touche 4, y compris sur clavier AZERTY.
* Conserver le comportement de R.
* Afficher le numéro du tour uniquement dans ce scénario.
* Conserver le dernier chemin après une fin de tour.
* Actualiser le message du dernier résultat et les ressources.

Le client ne doit pas effectuer lui-même les calculs de récupération.
4. Tests
Implémenter les seize tests définis dans MEC-0004, T01 à T16, sans en modifier les résultats attendus.
La couverture doit notamment comprendre :

* Les récupérations successives et le plafonnement.
* Les paramètres personnalisés.
* Les récupérations nulles.
* Les paramètres et états initiaux invalides.
* Les ressources exactement aux plafonds.
* La conservation de la position et de l'orientation.
* La conservation du chemin après une fin de tour.
* La reconnaissance de la touche 4 sur AZERTY.
* L'absence d'effet de T dans les scénarios 1 à 3.
* La réinitialisation complète du scénario 4.
* La non-régression des trois scénarios existants.

Étendre `SmokeTest.cs` en envoyant de véritables événements Godot, comme pour le lot 1F.
Utiliser les résultats du moteur pour les vérifications d'intégration. Conserver les valeurs fixes spécifiées dans MEC-0004 comme assertions indépendantes.
5. Vérifications
Exécuter, avec preuves et codes de sortie :

* `dotnet build`
* `dotnet test`
* `dotnet format --verify-no-changes`
* `bash scripts/harness/test-hooks.sh`
* Les contrôles fumée Godot existants et étendus.

Produire des captures du scénario 4 avec un affichage virtuel lorsque celui-ci est disponible.
Effectuer une relecture indépendante ciblée sur :

1. La fidélité à MEC-0004.
2. La simplicité de l'architecture.
3. L'absence de régression de MEC-0003.
4. La séparation entre moteur et client.
5. Les tests et leurs éventuels angles morts.

Ne pas déclarer le test manuel macOS réalisé par le propriétaire tant qu'il n'a pas eu lieu.
6. Restrictions

* Ne pas modifier les règles de MEC-0001, MEC-0002, MEC-0003 ou MEC-0004.
* Ne pas modifier les registres protégés.
* Ne pas modifier la CI, les hooks, le harnais ni `CLAUDE.md`.
* Ne pas ajouter de fonctionnalités hors périmètre.
* Ne pas introduire d'ennemis, d'IA, de combats, de surcharge ou de gestion de plusieurs unités.
* Ne pas refactoriser les parties du programme sans rapport avec le lot.

7. Livrables

* Moteur de tours minimal.
* Quatrième scénario Godot.
* Tests T01 à T16.
* Contrôles de non-régression.
* Rapport `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`.
* Mandat archivé et indexé selon les conventions du dépôt.
* Rapport de relecture indépendante.

8. Conditions d'exécution
Le travail doit être réalisé sur une branche dédiée créée à partir de `origin/main` actualisée.
Autorisation proposée pour cette première étape : exécution locale uniquement.
Aucun commit, push, PR ou fusion à ce stade.
À la fin du développement et de la relecture, remettre le diff, les résultats de tests, les réserves et le rapport à l'orchestrateur.
S'arrêter ensuite pour décision du propriétaire.
