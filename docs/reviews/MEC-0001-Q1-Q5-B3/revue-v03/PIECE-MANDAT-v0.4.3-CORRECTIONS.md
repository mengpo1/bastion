# Mandat de correction documentaire v0.4.2 → v0.4.3

Copie, par Claude Code, du message du propriétaire horodaté 2026-11-20T16:12:04.779Z dans le journal de session (JS-38, message 38 de l'extraction mécanique O-7). Le texte est extrait par script, puis reproduit **intégralement**, sans correction ni omission. Non archivé dans le dépôt, non authentifié de façon indépendante.

---

## Message K — Mandat v0.4.3

BASTION — Mandat de correction documentaire v0.4.2 → v0.4.3
Objet : corrections finales de la consolidation MEC-0001, sans modification des décisions de gameplay.
Documents de référence :

* Consolidation MEC-0001 v0.4.2, SHA-256 `a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808`.
* Rapport indépendant de la v0.4.2, SHA-256 `1476a060e449fda7816ccc74c060d3465096cb1e56a0ae134b5f699145a6eb69`.
* Pièces justificatives P1 à P6 et registre des décisions sur `main`.

1. Objectif
Produire une consolidation complète v0.4.3, corrigeant strictement les anomalies documentaires confirmées.
Conserver intégralement les décisions validées, notamment les six arbitrages M-04, M-05, R-5, R-6, R-7 et R-8.
Ne prendre aucune nouvelle décision de gameplay.
2. Corrections indispensables
AN-01 — Provenance B3-03
Ajouter le marqueur ⟨B3-03⟩ manquant dans T04. Vérifier que le journal des corrections décrit exactement les changements effectués.
AN-02 — Identifiants des messages
Lever l'ambiguïté du §0.1 entre les messages du 19 novembre à 20 h 36 UTC et à 20 h 54 UTC.
Employer des identifiants explicites et stables, associés à leurs horodatages et aux pièces correspondantes.
AN-03 — Scénario T47 (b)
Corriger les conditions initiales du scénario pour qu'elles respectent Z1 et G3.
Ne pas permettre la sélection initiale d'un trajet dont le coût connu excède les ressources disponibles.
Conserver le comportement validé par M-05=A : un pas devenu plus coûteux mais toujours payable et admissible est exécuté.
AN-04 — Citations
Corriger les expressions présentées abusivement comme des citations littérales.
Reprendre les termes exacts des sources ou retirer les guillemets lorsqu'il s'agit d'une reformulation.
Contrôler les trois occurrences signalées.
AN-05 — Classement de T45
Corriger le classement de T45 au §18 pour le rendre cohérent avec M-13 et avec son statut réel dans la matrice des scénarios.
AN-07 — Points ouverts
Corriger le §10 : R:166 et G3 ne doivent pas être marqués comme entièrement résolus si le repli d'une diagonale sur le passage Y et les coûts des connexions restent ouverts.
3. Corrections complémentaires
Examiner également :

* AN-06 : cohérence des dépendances PNV de T03, T42, T43 et T46 ;
* AN-08 : inventaire des scripts et précision des résultats de vérification ;
* OB-01 à OB-08 : observations rédactionnelles.

Intégrer les corrections qui améliorent la fidélité documentaire sans modifier les règles.
Pour toute observation non retenue, donner une justification concise.
Ne pas inventer le contenu d'une anomalie ou d'une observation absente des pièces disponibles.
4. Contrôles internes
Vérifier :

1. La présence des corrections indispensables.
2. La fidélité des citations.
3. La cohérence des scénarios modifiés.
4. L'absence de modifications des règles validées.
5. La cohérence des PNV et des points ouverts.
6. Les renvois et la matrice de traçabilité.
7. Les empreintes des pièces.

Produire un diff intégral v0.4.2 → v0.4.3 et une empreinte SHA-256 de la nouvelle consolidation.
5. Livrables
Fournir :

* la consolidation v0.4.3 complète ;
* le diff avec la v0.4.2 ;
* le tableau AN-01 à AN-08 et OB-01 à OB-08 avec le traitement de chaque point ;
* le bilan de vérification interne ;
* la liste des réserves documentaires restantes.

Ne pas déclarer la v0.4.3 conforme avant le contrôle indépendant du diff.
6. Restrictions
Travail documentaire uniquement.
Les fichiers temporaires nécessaires sont autorisés hors du dépôt.
Aucune modification du dépôt Bastion, aucun commit, push, branche ou PR.
Aucune inscription documentaire ni implémentation.
Aucune modification des tests du jeu.
MEC-0001 et MEC-0002 restent reportées.
Arrêter le travail après la remise des livrables. Le contrôle indépendant du diff et l'archivage feront l'objet d'autorisations distinctes.
