BASTION — MEC-0003 — Avenant n° 2 et clôture des vérifications

Décision du propriétaire : autorisation limitée à l'exécution du présent avenant.

1. Objectif

Compléter les tests de MEC-0003 à la suite du rapport de relecture indépendant, sans modifier les règles de gameplay ni le comportement du moteur.

Les réserves RL-01, RL-02 et RL-03 doivent être traitées avant la publication du lot.

Simplicité avant tout : aucun refactoring, aucune nouvelle architecture, aucune fonctionnalité supplémentaire.

2. Modifications autorisées

A. Ajouter des tests pour RL-01, RL-02 et RL-03

RL-01 — Collision pendant une translation

Ajouter un test vérifiant que le volume réel de l'unité est contrôlé pendant toute la translation, et pas seulement à ses deux extrémités.

Le test doit échouer si le moteur ne vérifie que les positions initiale et finale.

RL-02 — Contrôle du trajet diagonal en L

Ajouter un test démontrant que le volume physique réel est contrôlé sur les deux segments du trajet en L.

Le test doit détecter une implémentation qui vérifie uniquement le point intermédiaire et la destination.

RL-03 — Arrêt au premier refus

Ajouter un test démontrant qu'un ordre s'interrompt au premier pas refusé, sans exécuter les pas suivants, sans nouveau calcul de chemin et sans modifier les effets des pas déjà exécutés.

Le test doit détecter une implémentation qui poursuivrait l'ordre après le refus.

Pour les trois cas, privilégier des scénarios minimaux et explicites.

B. Compléter T13

Dans le test C# existant :

- Renommer la méthode pour que son nom corresponde désormais au résultat attendu.
- Vérifier les passages successifs N puis W pour le chemin [NE, NW].
- Vérifier l'arrivée en (2,2), orientée NW.
- Vérifier le solde de 48 TU et 94 points d'énergie, à partir de l'état initial de 60 TU et 100 points d'énergie.
- Conserver toutes les assertions sur le refus du deuxième pas N, le maintien de l'état et la conservation du coût du premier pas.

Préciser dans le test que la zone atteignable est calculée depuis l'état initial en (2,4).

Aucune nouvelle modification du registre n'est autorisée.

3. Autres réserves

RL-11 — "UnitState"

Ne pas modifier le moteur dans ce lot. Conserver cette réserve dans le rapport.

RL-13 — Recalcul du passage diagonal

Conserver le comportement actuel sans le présenter comme une règle de gameplay validée. Documenter clairement qu'il s'agit d'un comportement observé dans le contexte des tests autorisant une modification de carte.

Aucun arbitrage de gameplay supplémentaire n'est autorisé.

RL-18 — Formulation de T13

Ne pas modifier le registre. La précision concernant l'état initial doit figurer dans le test.

4. Archivage documentaire

Autorisation de :

- Conserver l'avenant n° 1 dans "docs/mandates/", sous forme d'un document distinct, avec une provenance fidèle.
- Mettre à jour "docs/mandates/README.md" pour référencer le mandat initial et l'avenant n° 1.
- Ajouter le présent avenant n° 2 aux pièces documentaires du lot, en indiquant son origine et son statut.

Ne pas modifier les autres mandats existants.

5. Vérifications obligatoires

Après les modifications :

1. Vérifier le diff exact.
2. Exécuter compilation, tests, formatage et tests du harnais.
3. Vérifier que chaque nouveau test détecte effectivement le défaut qu'il vise, au moyen des mutants correspondants, sans laisser de mutant dans le code final.
4. Demander au relecteur indépendant une relecture ciblée des changements de l'avenant n° 2, et non une nouvelle revue générale.
5. Actualiser le rapport d'exécution avec les résultats réels, les limites et les réserves restantes.

Ne pas annoncer qu'une réserve est levée sans preuve correspondante.

6. Interdictions

Aucune modification :

- du moteur C# ;
- des règles de gameplay ;
- de MEC-0001 ou MEC-0002 ;
- du harnais ;
- des autres tests, hormis les ajouts autorisés et T13 ;
- de fichiers sans lien direct avec ce mandat.

7. Publication

Aucun commit, push, création de PR ou fusion n'est autorisé par cet avenant.

Conserver les modifications sur la branche locale existante "claude/implementation-mec-0003-lot1".

À la fin de l'avenant, présenter le bilan des contrôles, le diff définitif et la conclusion de la relecture ciblée.

La publication fera l'objet d'une autorisation distincte.
