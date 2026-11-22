BASTION — Mandat d'implémentation MEC-0003 v1.0
Objet : implémenter et tester le premier incrément de marche sur terrain plat.
Base obligatoire : `main`, commit `25e7a28d18d29fea3753f3313a10f27126c3f274`.
Statut : mandat préparé, en attente d'autorisation d'exécution du propriétaire.
1. Références
Lire et respecter :

* `CLAUDE.md` ;
* `docs/gameplay/GAMEPLAY-DECISIONS.md`, notamment MEC-0003 et les règles de MEC-0001 auxquelles elle renvoie ;
* les décisions techniques applicables ;
* les projets C# et tests existants.

Commencer par `git fetch origin main` et vérifier le commit de base.
Travailler exclusivement sur une branche dédiée :
`claude/implementation-mec-0003-lot1`
Ne jamais modifier directement `main`.
2. Travail à réaliser
Implémenter MEC-0003 dans `src/Bastion.Simulation` en C#, sans dépendance à Godot.
Procéder dans cet ordre :
Étape A — Modèles et ressources

* Carte, cases, terrains, murs et obstacles.
* Position, orientation et dimensions de l'unité.
* TU, énergie, coûts de déplacement et arrondis.
* Configurations et validation des paramètres.
* Tests T01 à T04, T03b et T19.

Étape B — Géométrie et déplacements

* Huit directions de déplacement.
* Rotations et contrôle du volume rectangulaire réel balayé.
* Translation et diagonales en L.
* Collisions, contact autorisé et passages entre obstacles.
* Priorités des passages et sens des rotations.
* Tests T10 à T14 et T20 à T29.

Étape C — Recherche de chemin et exécution

* Zone atteignable avec les deux ressources.
* Recherche de chemin minimisant d'abord les TU, ensuite l'énergie, avec départage déterministe.
* Exécution pas à pas et débit unique.
* Contrôles avant modification de l'état de l'unité, selon A9.
* Gestion d'un pas refusé et d'un coût modifié entre calcul et exécution.
* Tests T05 à T09 et T15 à T18.

L'ordre de travail est indicatif : Claude Code peut réorganiser les étapes pour limiter les dépendances, sans changer leur périmètre.
3. Exigences techniques

* Code simple, lisible et modulaire.
* Pas de framework supplémentaire sans besoin démontré.
* Pas d'architecture générique anticipant des mécaniques non autorisées.
* Pas de dépendance Godot dans la simulation.
* Pas de copie de code, données ou assets OXCE/X-COM.
* Géométrie fondée sur le volume rectangulaire réel, pas sur une approximation par disque.
* Vérification des collisions sur l'ensemble du mouvement, pas uniquement aux positions de départ et d'arrivée.
* Respect des calculs et arrondis déjà décidés, sans imposer une règle numérique nouvelle.
* Comportements déterministes et testables.
* Messages d'erreur compréhensibles.

Si un point du registre est insuffisamment défini pour produire un comportement correct, ne pas inventer une règle. Signaler précisément le blocage et son impact.
4. Tests et critères d'acceptation
Implémenter les 30 scénarios T01 à T29 et T03b inscrits dans MEC-0003.
Le résultat doit notamment démontrer :

* le calcul correct des TU et de l'énergie ;
* le choix déterministe des chemins ;
* le passage d'une diagonale lorsqu'un seul trajet en L est praticable ;
* le contrôle réel des rotations et des collisions ;
* la distinction entre contact autorisé et chevauchement interdit ;
* la conservation intégrale de l'état lors d'un pas refusé ;
* l'absence de modification de l'état lors des simples calculs de chemin et de zone.

Ne pas modifier les résultats attendus du registre pour faire réussir les tests.
Exécuter :

```
dotnet restore
dotnet build --configuration Release
dotnet test --configuration Release
dotnet format --verify-no-changes
bash scripts/harness/test-hooks.sh
```

Si l'environnement local ne dispose pas de .NET, le signaler. Ne pas présenter les vérifications non exécutées comme réussies.
La CI GitHub devra également être contrôlée.
5. Fichiers et restrictions
Fichiers autorisés dans le périmètre du mandat :

* `src/Bastion.Simulation/` ;
* `tests/Bastion.Simulation.Tests/` ;
* le mandat d'exécution dans `docs/mandates/` ;
* le rapport de fin dans `docs/reviews/`.

Ne pas modifier :

* les registres de décisions ;
* `CLAUDE.md` ;
* `.claude/`, `scripts/harness/` ou `.github/workflows/` ;
* l'interface utilisateur ;
* d'autres mécaniques.

MEC-0001 et MEC-0002 restent reportées.
6. Vérification et livraison
À la fin :

1. Vérifier le diff et l'absence de fichiers hors périmètre.
2. Faire relire le diff par un relecteur indépendant, distinct du développeur.
3. Corriger uniquement les non-conformités établies.
4. Produire un rapport dans `docs/reviews/`, donnant les résultats réels des tests, les limites et les éventuels blocages.
5. Sous réserve de l'autorisation de publication du propriétaire, commiter et pousser exclusivement sur la branche dédiée.
6. Ouvrir une PR vers `main`, sans la fusionner.

La description de la PR doit notamment contenir la déclaration de traçabilité attendue par la CI, seule sur sa ligne :
Traçabilité simulation : MEC-0003 — Implémentation et tests de la marche sur terrain plat, dans le périmètre validé.
Indiquer au propriétaire le lien de la PR, le SHA du commit et l'état réel de la CI.
Ne pas fusionner. Ne pas lancer le lot suivant.
Arrêter le mandat après livraison.
