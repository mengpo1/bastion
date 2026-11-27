BASTION — Proposition de mandat LOT-1J v1.0
Objet
Préparer la spécification de la gestion de plusieurs unités et de l'alternance des trois camps, en s'appuyant sur les mécaniques MEC-0003 et MEC-0004 déjà intégrées.
Référence Git : `364b46acc486fa723ba1787c6e4b01e9a3537678`
Travail demandé

1. Examiner l'architecture actuelle de `Bastion.Simulation`, particulièrement `Movement/` et `Turns/`, et les tests correspondants.
2. Retrouver et qualifier la provenance de la décision Q1-B : trois camps, phases Joueur → Hostile → Neutre, phase neutre autonome. Ne pas considérer les éléments non retrouvés comme vérifiés.
3. Identifier les règles déjà décidées et les décisions complémentaires nécessaires.
4. Étudier notamment :
   * la sélection et l'activation des unités ;
   * la distinction entre tour, phase et activation individuelle ;
   * le passage d'une unité à une autre ;
   * la récupération des TU et de l'énergie ;
   * le traitement des unités incapables d'agir ;
   * les phases des camps sans unités actives ;
   * l'articulation avec une future IA hostile ou neutre.
5. Proposer une spécification minimale, sans imposer de comportement non validé.
6. Définir les scénarios de tests attendus et les risques de régression.
7. Préparer une proposition de fiche de mécanique, sous un nouvel identifiant à confirmer.

Contraintes

* Aucun changement de gameplay.
* Aucune modification du registre protégé.
* Aucun code ni test à écrire.
* Ne pas modifier MEC-0003 ou MEC-0004.
* Ne pas implémenter MEC-0001 ou MEC-0002.
* Aucun commit, push, PR ou fusion.

Livrable
Un dossier de conception contenant les règles acquises, les questions encore ouvertes, les propositions clairement identifiées comme non validées, les impacts techniques et une matrice de tests prévisionnels.
Le travail doit rester préparatoire. La validation des règles et l'autorisation d'implémentation feront l'objet de décisions distinctes.
Ce mandat est une proposition de cadrage, non une autorisation d'exécution.
