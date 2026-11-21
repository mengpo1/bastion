# Messages du propriétaire — consignes v0.3, mandat de revue v0.3, mandat de correction v0.4

Copie, par Claude Code, de trois messages du propriétaire reçus dans la conversation, dans l'ordre de réception, tels que reçus, sans correction. Ils ne sont ni archivés dans le dépôt ni authentifiés indépendamment. Le troisième contient les confirmations W-01 et W-12, reçues le 20 novembre 2026 (date de la session).

---

## Message F — Consignes de préparation de la v0.3

Pour Bastion MEC-0001, j'ai pris connaissance de ta réévaluation de provenance.
Je valide la poursuite de la préparation documentaire uniquement, sans modification du dépôt.
Prépare une consolidation complète révisée v0.3 dans ta réponse, destinée à une nouvelle revue indépendante.
Consignes :

1. Intègre les 29 décisions Q1–Q3 dont les propositions et validations sont désormais fournies.
2. Corrige la chronologie GE-02 → Q1.4 → Q1.8 → Q4.1. La hauteur entre sols de référence reste fixée à 3 000 mm.
3. Intègre Q5.1=A, Q5.2=A et B3=A, ainsi que leurs rectificatifs, en conservant leur provenance exacte.
4. Reprends les neuf formulations sans source de ta section 3. Pour chacune, cherche une décision explicite existante. Si aucune preuve suffisante n'est disponible, inscris « proposé, non validé ». N'ajoute aucune règle tacitement.
5. Intègre toutes les corrections documentaires recensées dans la section 4 de ton rapport et dans les revues précédentes.
6. Actualise la matrice de traçabilité, les scénarios de vérification et la liste des réserves.
7. Fournis la liste précise des pièces justificatives à archiver, en distinguant les textes transmis, les validations citées et les déclarations non accompagnées de leur proposition originale.
8. Vérifie que les modifications concernant GE-02 et GE-03 de MEC-0002 sont explicitement identifiées.

Ne réalise pas encore de nouvelle revue de conformité : prépare d'abord un document complet, qui pourra être soumis à un relecteur distinct.
Interdictions : aucune modification de fichier du dépôt, aucun commit, push, branche, PR, test ou implémentation.
MEC-0001 et MEC-0002 restent reportées. Aucune autorisation de gameplay.

---

## Message G — Mandat de revue indépendante de la v0.3

BASTION — Mandat de revue indépendante MEC-0001 v0.3
La consolidation Q1–Q5 et B3 v0.3 est maintenant rédigée.
Confie sa vérification à un relecteur distinct de celui qui l'a préparée.
Objectif
Vérifier sa fidélité aux décisions validées, sa cohérence avec le registre Bastion et sa capacité à constituer un dossier documentaire fiable.
Contrôles prioritaires

1. Vérifier les 29 décisions Q1–Q3 à partir des propositions et validations transmises.
2. Vérifier la hiérarchie GE-02 → Q1.4 → Q1.8 → Q4.1.
3. Vérifier les formulations Q4, Q5.1, Q5.2 et B3 selon les preuves effectivement disponibles.
4. Vérifier que les neuf formulations PNV ne sont jamais présentées comme des règles acceptées.
5. Vérifier la cohérence entre Q5.2, S10 et la correspondance « emplacement tactique stable / case ».
6. Vérifier toutes les formules et tous les résultats des scénarios T01 à T36.
7. Vérifier les modifications documentaires prévues dans MEC-0002, notamment GE-02, GE-03 et la ligne « Géométrie » des points ouverts.
8. Vérifier le journal C-01 à C-31 et la liste des preuves à archiver.
9. Distinguer les contradictions réelles, les anomalies documentaires et les paramètres explicitement reportés.

Livrable
Rendre un rapport comprenant :

* Un verdict : conforme, conforme sous réserves ou non conforme.
* Les anomalies, classées par gravité.
* La matrice de traçabilité des décisions et des preuves.
* Les éventuelles règles insuffisamment justifiées.
* Les corrections strictement nécessaires avant archivage et inscription.

Ne prends aucune décision de gameplay à la place du propriétaire.
Restrictions
Travail en lecture seule.
Aucune modification du dépôt, aucun commit, push, branche, PR, test d'implémentation ou développement.
MEC-0001 et MEC-0002 demeurent reportées. Aucune autorisation d'inscription ou de gameplay.

---

## Message H — Mandat de correction documentaire v0.3 → v0.4 (contient les confirmations W-01 et W-12)

BASTION — Mandat de correction documentaire MEC-0001 v0.3 → v0.4
Nature : correction groupée de la consolidation documentaire
Base : consolidation MEC-0001 Q1–Q5 et B3 v0.3 ; rapport de revue indépendante W-01 à W-14
Livrable : consolidation v0.4 complète, accompagnée de sa matrice de traçabilité et de son journal des corrections
Statut : préparation documentaire uniquement
1. Objectif
Produire une version v0.4 de la consolidation MEC-0001 corrigeant les anomalies W-01 à W-14.
Conserver strictement les décisions existantes. Ne modifier aucune règle de gameplay sans validation explicite du propriétaire.
La v0.4 doit distinguer :

* les règles déjà inscrites au registre ;
* les propositions et validations d'origine transmises ;
* les décisions attestées uniquement par des citations ou déclarations ;
* les conséquences déduites de règles validées ;
* les propositions non validées ;
* les points laissés ouverts.

Ne pas transformer une correction rédactionnelle en arbitrage implicite.
2. Confirmations du propriétaire
W-01 — Hauteur d'étage
Le propriétaire confirme expressément :
« La hauteur entre les sols de référence de deux étages tactiques consécutifs est fixée à 3 000 mm, non configurable par carte. Les dénivelés locaux restent possibles. »
Cette confirmation fait autorité pour la rédaction de la v0.4.
Corriger les formulations contradictoires de B3-02 sans modifier le texte historique de la pièce d'origine.
Présenter clairement la chronologie :

1. GE-02 fixe la hauteur d'étage à 3 m.
2. Q1.4=A introduit historiquement une altitude configurable pour chaque niveau.
3. Q1.8=A propose une valeur initiale de 3 000 mm.
4. Q4.1=A précise la règle applicable des 3 m fixes entre sols de référence.
5. La présente confirmation explicite définitivement sa portée non configurable par carte.

Conserver Q1.4 et Q1.8 dans l'historique, sans les effacer.
W-12 — Validation du rectificatif B3
Le propriétaire valide expressément le rectificatif B3 comme référence documentaire.
Inscrire sa validation dans la traçabilité de la v0.4.
Conserver la mention « proposition de rectification documentaire » dans la pièce historique si elle est reproduite, puis ajouter séparément la validation ultérieure du propriétaire.
Ne pas présenter cette confirmation comme une autorisation de modifier le dépôt.
3. Provenance de Q1.1 à Q1.4 — correction de W-05
Le relecteur a classé Q1.1 à Q1.4 en « RV — restitution », au motif que les options écartées seraient absentes.
Ce constat est à corriger à partir des textes effectivement transmis.
Les pièces comprennent, pour chacune de ces décisions, les deux options A et B, puis la validation explicite de l'option A.
Vérifier et conserver :

* Q1.1=A : largeur uniforme par carte, configurable et paire en millimètres.
* Q1.2=A : dimensions physiques configurables par type et posture ; volume pouvant dépasser sa case.
* Q1.3=A : épaisseur physique configurable par type de mur.
* Q1.4=A : altitude initialement configurable par niveau, règle historique ensuite supplantée pour la hauteur d'étage.

Reclasser ces quatre décisions dans la catégorie « proposition et validation transmises », sous réserve que les textes complets soient effectivement joints au dossier de travail.
La distinction à maintenir est celle entre une copie transmise par le propriétaire et une pièce originale indépendamment authentifiée.
Ne pas inventer de date, d'empreinte ou de provenance supplémentaire.
4. Corrections W-02 à W-14
W-02 — Provenance des valeurs Q1
Rétablir les mentions de provenance exigées par B3-03 jusqu'à l'archivage des validations.
Distinguer les valeurs dont le texte a été transmis de celles qui n'ont aucune source vérifiable.
W-03 — Scénario T21
Corriger l'explication du plafond de TU.
Avec le profil Q4.6, min(solde + 60, 60) vaut 60 pour tout solde non négatif.
Le plafond est donc atteint et ne permet pas de distinguer ARB-D d'une remise au maximum. Conserver les résultats numériques corrects des scénarios.
W-04 — MEC-0002
Rédiger explicitement les mises à jour documentaires envisagées pour :

* GE-02 et sa liste de points ouverts ;
* GE-03 et ses dimensions configurables ;
* la ligne « Géométrie » de la section « Encore ouvert » (R:336).

Distinguer le principe métrique commun décidé par B3, les valeurs initiales Q1 transmises, et les paramètres restant ouverts : dimensions minimales, tolérances, arrondis, précision des calculs et autres types d'unités.
Ne pas modifier GE-05, CO-01 ou les règles de dégâts.
W-05 — Archivage et inventaire
Compléter l'inventaire des pièces avec :

* les copies de travail identifiées par leurs empreintes ;
* les propositions et validations Q1–Q3 ;
* les messages de validation Q4 ;
* les déclarations Q5.1, Q5.2 et B3 ;
* les addenda et rectificatifs ;
* le message de consignes ayant demandé la v0.3 ;
* les deux confirmations W-01 et W-12 ;
* le mandat, le rapport et les observations complémentaires de la revue indépendante ;
* la consolidation v0.4 et, ultérieurement, son rapport de revue.

Vérifier chaque empreinte sur le fichier correspondant. Ne pas déclarer une pièce archivée simplement parce qu'elle figure dans la liste.
W-06 — Scénarios historiques
Réexaminer P0-10, E-04, E-05, C-02, G1-01, G1-04 et G1-05.
Pour chacun, indiquer s'il est repris, adapté, remplacé, exclu ou conservé comme historique.
Corriger G1-05 : avec un seul passage orthogonal ouvert, sa dépendance concerne la géométrie et la praticabilité du trajet, et non la priorité X puis Y.
W-07 — Q3.11
Reprendre la formulation originale : les valeurs de réserve et de récupération restent configurables, sans valeurs définitives avant les essais de rythme de jeu.
Rappeler leur fixation ultérieure comme valeurs initiales de test en Q4.6.
W-08 — Fidélité rédactionnelle
Corriger l'ensemble des écarts identifiés, notamment :

* Q5.1 : restaurer la notion de destination tactique admissible ;
* B3 : conserver « peuvent être exprimées en millimètres » lorsque cette formulation correspond à la source ;
* GE-02 : distinguer modification et remplacement d'une clause ;
* GE-03 : attribuer explicitement à Q1.2 ce qui ne figure pas dans B3-03 ;
* ARB-A et G1 : ne pas étendre aux autres pas une restriction démontrée seulement pour les diagonales ;
* Q4.19 : corriger le nombre de points effectivement tranchés ;
* arithmétique exacte : distinguer exigence validée, nécessité technique démontrée et recommandation non arbitrée.

Corriger également les autres écarts rédactionnels signalés dans W-08.
W-09 — Formulations PNV
Mettre PNV-2 en cohérence avec les sources qui fixent les millimètres entiers.
Ne pas étendre tacitement cette contrainte aux calculs physiques de MEC-0002.
Signaler la dépendance éventuelle du §3.6 à PNV-4.
Conserver les formulations non suffisamment justifiées comme proposées et non validées, même lorsqu'elles semblent raisonnables.
W-10 — Attendus de scénarios
Réviser les statuts et résultats attendus de T04, T18, T30, T33 et T36.
En particulier :

* ne pas supposer l'inclusion des bornes de ressaut si elle n'est pas justifiée ;
* ne pas attribuer arbitrairement un sens de classement aux identifiants de connexion ;
* rendre explicites les conditions physiques des tests ;
* distinguer les cas exécutables en théorie de ceux dépendant d'une convention encore ouverte.

W-11 — Renvois
Corriger tous les renvois aux PNV, aux addenda et aux observations de revue.
Distinguer les points numérotés de l'addendum Q5 des remarques ultérieures formulées à son sujet.
Reclasser correctement les questions « emplacement stable / case ».
W-12 — Rectificatif B3
Reporter la validation expresse du propriétaire, sans réécrire rétroactivement le statut de la pièce historique.
W-13 — Rapport à OpenXcomCE
Ne pas étendre les constats du LOT-2A à des comportements qu'il ne vérifie pas.
Limiter les comparaisons aux éléments effectivement documentés.
Corriger le traitement de G4 et Q4.16.
Ajouter la référence BattleUnit.cpp:2714-2720 pour ARB-D si elle est confirmée dans la source disponible.
W-14 — Q5.2 et S10
Distinguer les règles validées des interprétations documentaires.
Conserver le principe : Q5.2 ne crée pas d'exception supplémentaire à S10.
Ne pas autoriser implicitement deux unités conscientes sur une même case tactique stable.
Si la correspondance exacte entre emplacement stable et case, ou les conditions d'occupation pendant un transit partagé, ne sont pas couvertes par les décisions disponibles, les maintenir explicitement ouvertes.
5. Matrice de traçabilité
Produire une matrice actualisée indiquant, pour chaque décision :

* son identifiant ;
* sa formulation retenue ;
* sa source exacte ;
* le niveau de preuve ;
* son statut actuel ;
* les règles du registre concernées ;
* les scénarios associés ;
* les réserves éventuelles.

Identifier séparément les modifications documentaires futures concernant MEC-0002.
6. Vérification finale de la v0.4
Effectuer une vérification de cohérence documentaire interne, distincte d'une revue indépendante.
Vérifier notamment :

1. La fidélité aux 29 décisions Q1–Q3.
2. Les confirmations W-01 et W-12.
3. L'absence de décision nouvelle.
4. Les calculs et scénarios.
5. L'exhaustivité de W-01 à W-14.
6. Les neuf formulations PNV et leurs dépendances.
7. Les écarts restants avec les sources.
8. L'exactitude de l'inventaire des preuves.

Fournir la v0.4 complète, et non une simple liste de modifications.
Terminer par un tableau « anomalie → correction → section → preuve → statut ».
Ne pas déclarer la v0.4 conforme avant une nouvelle revue indépendante.
7. Restrictions absolues
Le mandat autorise exclusivement la rédaction et la vérification documentaire dans la réponse de Claude Code.
Aucune modification du dépôt GitHub.
Aucune création de branche, aucun commit, push ou PR.
Aucun développement, aucune modification de code ou de test.
Aucune inscription dans les registres de décisions.
Aucune décision nouvelle sans accord explicite du propriétaire.
MEC-0001 et MEC-0002 restent reportées dans leur ensemble.
