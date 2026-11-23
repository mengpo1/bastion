BASTION — Mandat LOT-1F v1.0
Banc d'essai visuel de MEC-0003
Statut : PRÉPARÉ — exécution non autorisée
Dépôt : `mengpo1/bastion`
Branche proposée : `claude/lot-1f-scenarios-mouvement`
Base : `origin/main`, à actualiser et vérifier.
1. Objectif
Étendre le prototype Godot des lots 1D et 1E pour permettre au propriétaire d'observer plusieurs situations représentatives de MEC-0003.
Ne créer aucune nouvelle mécanique de gameplay.
Principe fondamental : simplicité avant tout.
2. Scénarios à réaliser
Conserver une scène Godot unique et proposer trois scénarios fixes, sélectionnables par les touches 1, 2 et 3.
Scénario 1 — Référence
Conserver exactement le scénario du lot 1D :

* grille 5 × 5 ;
* case infranchissable (3,2) ;
* unité en (1,4), orientée N ;
* 20 TU et 10 points d'énergie.

Les comportements validés et les contrôles existants doivent rester inchangés.
Scénario 2 — Mur et recherche de chemin
Utiliser une grille 5 × 5 avec :

* unité initiale en (1,4), orientée N, 20 TU et 10 points d'énergie ;
* un mur standard sur l'arête est de la case (1,4) ;
* terrain normal partout.

Afficher le mur sur la grille.
Le moteur doit déterminer seul si une destination reste accessible par un autre chemin. Ne jamais confondre l'interdiction de traverser directement un mur avec l'impossibilité d'atteindre la case située derrière lui.
Afficher dans le panneau la suite des directions choisies par le moteur pour le dernier ordre exécuté.
Scénario 3 — Coûts des terrains
Utiliser une grille 5 × 5 avec :

* unité initiale en (1,4), orientée N, 20 TU et 10 points d'énergie ;
* terrain difficile en (2,4) ;
* terrain très difficile en (3,4) ;
* terrain normal ailleurs.

Distinguer visuellement les catégories de terrain par des couleurs simples et une légende.
Avec les règles initiales existantes, vérifier notamment :

* clic sur (2,4) : arrivée avec 14 TU et 7 points d'énergie ;
* clic suivant sur (3,4) : arrivée avec 6 TU et 3 points d'énergie.

Ces valeurs doivent être confirmées par le moteur, sans calcul parallèle dans la scène.
3. Interface

* Touches 1, 2 et 3 : charger un scénario.
* Touche R : réinitialiser le scénario courant.
* Clic gauche : transmettre un ordre à `ExecuteOrder`.
* Afficher le numéro du scénario, les commandes, les TU, l'énergie, l'orientation et le résultat de l'ordre.
* Afficher les murs et les terrains à partir des données du moteur.

Conserver une présentation 2D minimale. Aucun sprite, aucune animation ni interface définitive.
4. Architecture et contraintes

* `Bastion.Simulation` reste inchangée et indépendante de Godot.
* Réutiliser exclusivement les API publiques du moteur.
* Aucune règle de calcul de chemin, coût, collision ou rotation dans le client.
* Pas de framework, système de scènes générique, chargeur de niveaux ou configuration externe.
* Les scénarios sont des données fixes de démonstration, pas des règles de gameplay.
* Ne pas modifier MEC-0001, MEC-0002 ni les registres protégés.
* Ne pas modifier `Bastion.slnx`, le harnais ou la CI.

5. Vérifications

1. Préserver les contrôles automatisés du scénario initial.
2. Ajouter des contrôles fumée ciblés pour les scénarios 2 et 3, en passant par les mêmes entrées Godot que le joueur.
3. Vérifier les murs, les terrains, les changements de scénario, les ressources et la touche R.
4. Comparer les résultats à ceux des API du moteur et, pour les valeurs spécifiées, aux constantes du mandat.
5. Exécuter les tests existants, le format, le harnais et les contrôles du client Godot.
6. Demander une relecture indépendante ciblée du diff.

Ne déclarer aucune validation manuelle graphique si elle n'a pas réellement été effectuée.
6. Livrables

* Prototype Godot enrichi.
* Notice de lancement et d'utilisation.
* Mandat archivé et indexé suivant le protocole.
* Rapport `docs/reviews/LOT-1F-SCENARIOS-MOUVEMENT.md`.
* Rapport de relecture indépendante.

7. Autorisations
L'exécution nécessite l'accord explicite du propriétaire.
Les commits, pushes et l'ouverture d'une PR nécessitent également une autorisation explicite déterminant leur périmètre.
Aucune fusion dans `main` sans accord distinct.
Ne commencer aucun autre lot.
