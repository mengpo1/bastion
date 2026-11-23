BASTION — Mandat LOT-1E v1.0
Qualification automatisée du client Godot
Statut : préparé — en attente d'autorisation du propriétaire
Dépôt : `mengpo1/bastion`
Branche proposée : `claude/lot-1e-ci-godot`
Base : `origin/main`, à vérifier au démarrage.
1. Objectif
Intégrer le client `Bastion.Client.Godot` à la CI existante afin qu'une régression de compilation, de formatage ou de fonctionnement du prototype puisse être signalée automatiquement.
Conserver une architecture simple et les règles permanentes de `CLAUDE.md`.
2. Périmètre autorisé après validation du mandat

1. Ajouter à la CI existante la restauration, la compilation et le contrôle de format du projet `src/Bastion.Client.Godot/Bastion.Client.Godot.csproj`.
2. Installer dans l'environnement CI la version de référence Godot 4.7.2 stable .NET, depuis sa distribution officielle, avec vérification d'intégrité et sans nouvelle action GitHub tierce si une commande suffit.
3. Compiler le client en Debug avant d'exécuter son contrôle fumée headless.
4. Exécuter `-- --smoke-test` sous une limite de temps explicite.
5. Faire échouer la CI pour tout code de sortie non nul, y compris 124. Ne pas confondre expiration du délai et échec fonctionnel.
6. Conserver les vérifications actuelles de la simulation, du harnais et de la traçabilité.
7. Documenter les six essais manuels macOS déclarés conformes par le propriétaire le 23 novembre 2026, en précisant qu'il s'agit d'un retour utilisateur, non d'une reproduction indépendante.
8. Actualiser la notice du client pour refléter précisément le périmètre désormais testé, sans étendre les affirmations aux exports ou à Windows.

3. Contraintes

* Ne modifier aucun comportement du prototype ni de la simulation.
* Ne pas ajouter le client à `Bastion.slnx` uniquement pour faciliter la CI : les commandes ciblées sont suffisantes si elles fonctionnent.
* Ne pas modifier les registres protégés.
* Les modifications du workflow CI sont autorisées uniquement dans le cadre de ce mandat, après son approbation explicite.
* Ne pas introduire de framework, infrastructure ou abstraction supplémentaire.
* Ne jamais désactiver un contrôle existant pour obtenir une CI verte.

4. Tests et critères d'acceptation

* CI complète réussie sur la branche du lot.
* Compilation du client sans avertissement ni erreur.
* Format du client conforme.
* Contrôle fumée Godot réellement exécuté dans GitHub Actions, avec code 0 et résultat observable.
* Vérification négative en environnement jetable : un défaut intentionnel du client doit faire échouer le contrôle concerné.
* Absence de régression des 46 tests de simulation et du harnais.
* Relecture indépendante ciblée du diff et des preuves.

Si l'installation ou l'exécution de Godot en CI se révèle impossible sans complexité excessive, arrêter cette partie et documenter précisément le blocage. Ne pas remplacer silencieusement le test d'exécution par une simple compilation.
5. Livrables

* Workflow CI modifié.
* Notice du client actualisée.
* Rapport `docs/reviews/LOT-1E-CI-GODOT.md`.
* Rapport de relecture indépendante.
* Mandat archivé et indexé conformément au protocole du dépôt.

6. Git et publication
Branche dédiée, sans modification de `main`.
Présenter le diff, les résultats et le rapport avant publication.
Aucun commit, push, création de PR ou fusion sans autorisation distincte du propriétaire.
Ne pas commencer de nouveau lot.
