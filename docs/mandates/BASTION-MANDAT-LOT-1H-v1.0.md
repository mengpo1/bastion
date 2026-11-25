BASTION — Mandat LOT-1H v1.0
Clôture documentaire de MEC-0004
Statut : PRÉPARÉ — exécution soumise à autorisation
Dépôt : `mengpo1/bastion`
Base : `main`, commit `b4e2a4793dd1101ff4b81e6ad404613ec7671838`
Branche proposée : `claude/lot-1h-cloture-mec-0004`
1. Objectif
Mettre la documentation de Bastion en cohérence avec l'intégration de MEC-0004.
Références vérifiées :

* PR #26, fusionnée dans `main`.
* Commit de fusion `b4e2a4793dd1101ff4b81e6ad404613ec7671838`.
* CI push et PR réussies : 65 tests .NET, 75 contrôles du harnais et 120 contrôles fumée Godot.
* Essais manuels macOS : sept contrôles déclarés satisfaisants par le propriétaire.
* Rapport `docs/reviews/LOT-1G-IMPLEMENTATION-MEC-0004.md`.

Cette opération est strictement documentaire.
2. Modifications du registre
Dans `docs/gameplay/GAMEPLAY-DECISIONS.md`, modifier uniquement les champs suivants de MEC-0004.
A. Tests de modification
Conserver intégralement le texte historique :
`T01 à T16, définis à la section 6, non encore implémentés.`
Lui ajouter une annotation datée du 25 novembre 2026 indiquant :

* Les seize scénarios T01 à T16 sont désormais couverts.
* Le moteur dispose de 19 tests xUnit.
* Le contrôle fumée Godot comprend 54 nouveaux contrôles.
* La CI de la PR #26 a exécuté avec succès 65 tests .NET et 120 contrôles fumée.
* Les détails se trouvent dans le rapport du LOT-1G.

Ne pas présenter les tests comme réalisés à la date de l'inscription initiale.
B. État d'implémentation
Remplacer :
`non commencé`
par :
`intégré — dans main par la PR #26, commit de fusion b4e2a4793dd1101ff4b81e6ad404613ec7671838 (25 novembre 2026). État à la date de l'inscription : non commencé.`
Préciser les essais manuels macOS : sept contrôles déclarés satisfaisants par le propriétaire, sans prétendre à une reproduction indépendante.
Conserver la distinction entre les vérifications automatisées et les essais déclarés.
C. Préservation de la fiche

* Ne modifier aucune décision de gameplay.
* Ne modifier aucun résultat attendu T01 à T16.
* Préserver intégralement les sections 2 à 7.
* Préserver les mentions historiques et leur provenance.
* Ne modifier ni MEC-0001, ni MEC-0002, ni MEC-0003.
* Ne pas élargir le périmètre accepté de MEC-0004.

3. Actualisation du README principal
Dans `README.md` :

* Mentionner MEC-0003 et MEC-0004 comme deux incréments implémentés et intégrés.
* Mentionner `Bastion.Simulation.Turns`.
* Décrire brièvement la gestion élémentaire des tours et la récupération des ressources.
* Actualiser la description du prototype Godot pour indiquer qu'il dispose de quatre scénarios.
* Conserver les restrictions de portée de MEC-0001 et MEC-0002.

Ne pas présenter le prototype comme un jeu complet ou une interface définitive.
4. Archivage et rapport
Archiver le présent mandat dans `docs/mandates/` et actualiser l'index existant.
Produire `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md` contenant :

* Le périmètre exact des modifications.
* La référence à la PR #26 et au commit de fusion.
* Les preuves de tests.
* La distinction entre contrôles automatisés et essais manuels.
* Le diff final.
* Les résultats des contrôles.
* Les limitations et éventuelles réserves.
* Les empreintes des fichiers documentaires modifiés.

5. Vérifications
Avant toute modification :

1. Exécuter `git fetch origin main`.
2. Vérifier le commit de base et l'état de la branche.
3. Vérifier qu'aucune modification locale étrangère au lot ne risque d'être écrasée.

Après modification :

1. Inspecter le diff du registre, ligne par ligne.
2. Confirmer que seules les deux lignes autorisées de MEC-0004 ont changé.
3. Vérifier l'absence de modification des sections normatives.
4. Vérifier le README et l'index.
5. Exécuter les contrôles applicables : compilation, tests, format et harnais.
6. Faire relire indépendamment le diff documentaire et les preuves.

Ne pas annoncer de succès sans résultat observable.
6. Restrictions

* Aucun changement de code C# ou Godot.
* Aucun changement des tests.
* Aucun changement de CI, hooks, scripts ou harnais.
* Aucune nouvelle règle de gameplay.
* Aucun refactoring.
* Aucun changement hors des cinq fichiers documentaires autorisés.
* Aucune fusion dans `main`.

7. Conditions d'exécution
L'autorisation demandée porte sur la préparation et l'exécution locale de ces modifications documentaires précises, y compris celles des deux champs de MEC-0004 décrits au §2.
Elle n'autorise pas le commit, le push ou l'ouverture d'une PR.
À la fin :

* Fournir le diff complet.
* Fournir le rapport de clôture.
* Présenter les conclusions de la relecture indépendante.
* Arrêter le travail et attendre la décision du propriétaire sur la publication.

Ne commencer aucun autre lot.
