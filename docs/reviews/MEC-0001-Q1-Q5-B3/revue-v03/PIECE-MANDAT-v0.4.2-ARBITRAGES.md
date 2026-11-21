# Mandat de consolidation documentaire v0.4.2 et six arbitrages du propriétaire

Copie, par Claude Code, du message du propriétaire horodaté 2026-11-20T14:44:23.468Z dans le journal de session (message 36 de l'extraction mécanique). Le texte est extrait par script, puis reproduit **intégralement**, sans correction ni omission. Non archivé dans le dépôt, non authentifié de façon indépendante.

---

## Message J — Mandat v0.4.2

BASTION — Mandat de consolidation documentaire v0.4.2
Projet : Bastion
Périmètre : MEC-0001 et interfaces documentaires avec MEC-0002
Base : consolidation MEC-0001 v0.4.1 et rapport de revue indépendante correspondant
Objet : intégrer les six arbitrages du propriétaire et corriger I-1 ainsi que M-01 à M-18
Statut : mandat de préparation documentaire exclusivement
1. Objectif
Produire une consolidation complète v0.4.2, à partir de la v0.4.1.
Cette version doit :

1. Intégrer exactement les six arbitrages ci-dessous.
2. Traiter l'anomalie importante I-1.
3. Corriger les dix-huit anomalies mineures M-01 à M-18.
4. Préserver les règles déjà validées.
5. Maintenir explicitement les paramètres et comportements non tranchés.
6. Actualiser la traçabilité, les scénarios et les réserves.
7. Préparer le dossier pour une nouvelle revue indépendante.

Ne pas rouvrir les décisions validées et ne pas introduire de nouvelles règles par déduction.
2. Arbitrages expressément validés par le propriétaire
Ces décisions constituent de nouvelles pièces justificatives. Leur formulation doit être conservée et leur provenance indiquée.
M-04=B — Surcharge et énergie
Décision validée :
« La surcharge peut également réduire l'énergie ; modalités à définir. »
Conséquences :

* Supprimer toute affirmation générale selon laquelle la surcharge ne réduit pas l'énergie.
* Conserver la formule validée de réduction des TU définie par Q3.14 et ARB-D.
* Conserver la récupération séparée de l'énergie prévue par ARB-D.
* Consigner que des effets énergétiques de surcharge sont possibles, mais que leur existence dans chaque situation, leur déclenchement, leur calcul et leurs valeurs ne sont pas encore spécifiés.
* Ne pas appliquer automatiquement à l'énergie la formule de surcharge des TU.
* Ne pas inventer de multiplicateur, d'arrondi ou de pénalité énergétique.

Statut : principe validé ; modalités ouvertes.
M-05=A — Augmentation imprévue du coût d'un pas
Décision validée :
« Si le coût augmente mais reste payable et que le passage est admissible, le pas est exécuté. »
Conséquences :

* Vérifier avant chaque pas son coût réel en TU et en énergie.
* Si les deux ressources suffisent et si le passage reste admissible, exécuter le pas avec son coût réel.
* Si le pas n'est plus payable ou devient physiquement inadmissible, interrompre l'ordre selon Q3.4 et Q4.21.
* Ne débiter aucun pas non commencé.
* Conserver le coût des pas déjà effectués.
* Ne pas créer de recalcul automatique de trajet.

Préciser que la simple augmentation du coût prévu ne suffit plus à interrompre l'ordre lorsque le pas reste admissible et payable.
Statut : règle validée.
R-5=A — Dimensions géométriques et précision numérique
Décision validée :
« Dimensions physiques configurées en millimètres entiers ; calculs physiques non limités systématiquement aux entiers. »
Conséquences :

* Les dimensions physiques configurées sont exprimées en millimètres entiers.
* Les calculs physiques intermédiaires ne sont pas soumis à un arrondi systématique au millimètre entier.
* Conserver les conventions d'arrondi déjà validées, notamment Q2.6, Q3.13 et Q3.14.
* Ne pas étendre ces conventions à d'autres calculs sans source.
* Mettre à jour PNV-2 : la question des millimètres entiers pour les dimensions configurées est désormais tranchée.
* Conserver ouverts les modalités de conversion, la précision numérique et les arrondis des autres grandeurs calculées lorsqu'ils ne sont pas spécifiés.

Cette décision est commune à MEC-0001 et MEC-0002 dans le cadre du référentiel physique B3.
Statut : règle validée ; modalités techniques restantes ouvertes.
R-6=A — Hauteur des étages
Décision validée :
« 3 000 mm fixes, sans réglage global ni par carte. »
Conséquences :

* La hauteur entre sols de référence de deux étages tactiques consécutifs est fixée à 3 000 mm.
* Elle n'est configurable ni globalement ni individuellement par carte.
* Les dénivelés locaux des supports demeurent possibles.
* Conserver la chronologie GE-02 → Q1.4 → Q1.8 → Q4.1 → W-01 → R-6.
* Ne pas présenter la hauteur d'étage comme une valeur initiale ajustable.

Statut : règle validée.
R-7=A — Portée résiduelle de Q1.4
Décision validée :
« Q1.4 reste historique pour l'altitude des niveaux de référence ; seules les variations locales de support demeurent. »
Conséquences :

* Conserver Q1.4 dans l'historique des décisions.
* Ne plus lui attribuer une faculté de configuration des altitudes de référence des étages.
* Maintenir les variations locales de hauteur des supports.
* Ne pas créer d'autre exception à la hauteur fixe de 3 000 mm.

Statut : clarification validée.
R-8=A — Articulation Q1.2 et GE-03
Décision validée :
« Q1.2 précise explicitement GE-03, avec géométrie commune aux deux mécaniques. »
Conséquences :

* Présenter Q1.2 comme une précision explicite de GE-03.
* Conserver les dimensions configurables par type d'unité et posture.
* Conserver la possibilité qu'un volume physique dépasse sa case.
* Maintenir les règles de collision applicables.
* Utiliser le même volume physique pour MEC-0001 et MEC-0002, conformément à B3.
* Identifier explicitement GE-03 parmi les règles à annoter lors d'une future inscription.

Cette validation ne modifie pas à elle seule le registre sur `main`.
Statut : articulation validée.
3. Correction de l'anomalie I-1 — Provenance Q1.1 à Q1.4
La provenance doit distinguer les messages effectivement transmis.
Le premier message fournit les options A et la validation de Q1.1 à Q1.4.
Un message ultérieur complète les propositions avec les options B.
Ces deux contributions constituent ensemble le dossier transmis de Q1.1 à Q1.4.
Travail demandé :

1. Identifier séparément les deux messages.
2. Reproduire fidèlement les huit options et la validation des quatre options A.
3. Conserver leur ordre chronologique réel.
4. Identifier toute section omise dans les copies de travail, notamment la partie « Mission ».
5. Actualiser la définition du statut [TR] afin qu'il distingue une proposition et une validation transmises ensemble d'un dossier constitué à partir de plusieurs messages.
6. Mettre à jour le §0.1, la matrice de traçabilité, l'inventaire des preuves et le journal des corrections.
7. Ne pas présenter une compilation comme un message original unique.

La transmission complète des propositions ne vaut pas authentification indépendante de la conversation d'origine.
Conserver les mentions de provenance et les exigences d'archivage applicables.
4. Corrections M-01 à M-18
Traiter intégralement les dix-huit anomalies à partir du rapport indépendant de la v0.4.1.
Pour chacune, relever son constat original, sa source, la correction apportée et les sections affectées.
Corrections particulièrement importantes
M-01 — Provenance B3-03
Compléter les cinq marqueurs manquants sur les valeurs dérivées de Q1.
M-02 — Scénario T21
Expliquer pourquoi un maximum fictif de 20 est utilisé pour exercer les différents cas de récupération et de plafonnement d'ARB-D.
M-03 — Traçabilité des scénarios
Corriger les dix rattachements insuffisamment justifiés dans la matrice. Ne pas attribuer un scénario à une décision qu'il ne vérifie pas réellement.
M-04 et M-05 — Arbitrages intégrés
Appliquer les décisions du §2. Vérifier leurs effets sur les descriptions des règles, les scénarios et la matrice de traçabilité.
M-08 — Citation PNV-4
Reprendre exactement la formulation de la source, sans guillemets autour d'une expression qui ne s'y trouve pas.
M-09 — Q5.2 et G2
Ne pas écrire une interdiction absolue de superposition de deux unités conscientes sans rappeler l'exception transitoire de G2.
M-10 — Q4.15
Corriger l'attribution de la citation au message source approprié.
M-11 — Q3.11 et Q4.6
Préciser que les valeurs énergétiques 100 et 20 de Q4.6 correspondent à l'option A précédemment écartée en Q3.11. Les valeurs de TU ne sont pas concernées par cette correspondance.
M-14 — Scénarios historiques
Clarifier le sort des trois cas de la v1.4.1 identifiés dans le rapport.
M-15 — Comparaison avec OXCE
Distinguer le calcul en nombres flottants et sa troncature dans OXCE du résultat mathématique exact requis par Q3.14 dans Bastion.
Conserver les références de code vérifiées. Ne pas affirmer une équivalence numérique universelle entre les deux systèmes.
M-16 — Fidélité des copies
Ne pas qualifier un texte de « reproduit tel que reçu » lorsqu'une section, même non décisionnelle, a été omise.
Pour M-06, M-07, M-12, M-13, M-17 et M-18 ainsi que les autres sous-points non reproduits ici, se référer exclusivement au rapport indépendant intégral. Ne pas inventer leur contenu.
5. Actualisation des décisions et réserves
Mettre à jour les sections suivantes :

* Décisions Q1 à Q5 et B3.
* Articulation GE-02 et GE-03.
* Ressources, surcharge et énergie.
* Exécution des pas et coûts imprévus.
* Géométrie et conventions numériques.
* Scénarios de vérification.
* Matrice de traçabilité.
* Liste des points ouverts.
* Inventaire des pièces justificatives.
* Journal des corrections.

Les six nouveaux arbitrages doivent apparaître dans une rubrique distincte, avec leur texte de validation et leur provenance.
Ne pas confondre une règle approuvée avec une modalité qui reste à définir.
6. Points restant ouverts
Maintenir les réserves qui ne sont pas directement tranchées par les six arbitrages.
En particulier :

* modalités d'une éventuelle réduction de l'énergie liée à la surcharge ;
* déclenchement exact du débit d'un pas engagé ;
* support pendant les phases physiques d'un pas ;
* cycles gratuits et terminaison de la recherche de chemin ;
* critères complets de repositionnement au réveil ;
* conventions d'orientation et de volume balayé ;
* tolérances de collision et précision des calculs ;
* règles détaillées des connexions et des transferts ;
* conditions de surveillance et de réaction.

Conserver les neuf formulations PNV, en ajustant uniquement celles que les décisions nouvelles permettent de clarifier.
Aucune proposition non validée ne doit être transformée en règle obligatoire.
7. Livrables attendus
Produire :

1. La consolidation v0.4.2 complète, et non uniquement un correctif.
2. La matrice de traçabilité actualisée.
3. Le tableau exhaustif I-1 et M-01 à M-18 : constat, correction, emplacement, source et statut.
4. L'inventaire des pièces et de leurs empreintes vérifiables.
5. La liste des réserves documentaires et des paramètres ouverts.
6. Le bilan de vérification interne.

Les éventuelles impossibilités de vérification doivent être signalées explicitement.
Ne pas annoncer un verdict de conformité avant la nouvelle revue indépendante.
8. Restrictions
Ce mandat autorise exclusivement la rédaction et les contrôles documentaires.
Les fichiers temporaires de travail sont autorisés uniquement hors du dépôt GitHub.
Interdictions :

* Modifier les fichiers du dépôt.
* Créer une branche, un commit, un push ou une PR.
* Inscrire les décisions dans le registre.
* Développer ou modifier le code du jeu.
* Implémenter ou modifier des tests.
* Engager une nouvelle mécanique de gameplay sans accord explicite.

MEC-0001 et MEC-0002 restent reportées dans leur ensemble.
9. Suite du processus
Après production de la v0.4.2 :

1. Vérifier la présence des pièces et la fidélité des corrections.
2. Soumettre la version complète à un relecteur distinct.
3. Examiner les éventuelles réserves restantes.
4. Préparer séparément, si la revue le permet, un mandat d'archivage et d'inscription documentaire.

Aucune étape ultérieure n'est autorisée par anticipation.
