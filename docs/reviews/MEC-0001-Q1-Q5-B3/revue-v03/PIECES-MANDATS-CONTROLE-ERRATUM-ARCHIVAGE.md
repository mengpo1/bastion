# Mandats de contrôle de la v0.4.3, d'erratum, et de préparation de l'archivage

Copie, par Claude Code, de trois messages du propriétaire extraits mécaniquement du journal de session (JS-39, JS-40 et JS-41 de l'extraction). Chaque texte est reproduit **intégralement**, sans correction ni omission. Non archivé dans le dépôt, non authentifié de façon indépendante.

---

## Message L — JS-39, horodatage du journal : 2026-11-20T16:36:50.909Z

BASTION — Mandat de contrôle indépendant de la consolidation v0.4.3
Objet : contrôler les corrections documentaires apportées à la consolidation MEC-0001 v0.4.3.
Nature : revue indépendante ciblée, en lecture seule.
1. Documents

* Consolidation v0.4.2 — SHA-256 `a6ad63e9b1659b917fcf1aae25e04a39c75030eaded4d72f45e381219e269808`.
* Consolidation v0.4.3 — SHA-256 `cd1c808b10dbcf39f96e557f9d6ef994b232bdcacc44e696122edd4dbee76602`.
* Diff v0.4.2 → v0.4.3 — SHA-256 `d15f305467744f5e874daea772cb544faf16e813aad3b71bdbc29e0b78485787`.
* Rapport de revue indépendante v0.4.2 — SHA-256 `1476a060e449fda7816ccc74c060d3465096cb1e56a0ae134b5f699145a6eb69`.
* Pièces justificatives P1 à P7, registre Bastion et références citées.

2. Travail demandé
Confier le contrôle à un relecteur distinct du rédacteur de la v0.4.3.
Vérifier indépendamment :

1. La correction effective des anomalies AN-01 à AN-08.
2. Le traitement des observations OB-01 à OB-08, notamment la justification du rejet d'OB-08.
3. L'exactitude des références et citations modifiées.
4. La cohérence de T47(b), en particulier la sélection initiale du trajet, les débits et l'arrêt avant le troisième pas.
5. Les calculs de T48 et les conventions d'arrondi.
6. La matrice de traçabilité et les dépendances aux PNV.
7. La présence des points ouverts qui ne doivent pas disparaître.
8. La conservation exacte des six arbitrages M-04, M-05, R-5, R-6, R-7 et R-8.
9. L'absence de modification des autres décisions de gameplay.
10. Les empreintes, l'inventaire et les fichiers de preuve.
11. L'absence de changements hors du périmètre annoncé par le diff.

Ne pas considérer les scripts ou les résultats des contrôles internes comme des preuves suffisantes : effectuer des vérifications indépendantes sur les sources.
3. Livrable
Remettre un rapport comprenant :

* Verdict : conforme, conforme sous réserves ou non conforme.
* Tableau des anomalies restantes, avec gravité et preuve.
* Vérification explicite de chacune des huit anomalies AN.
* Vérification de la conservation des six arbitrages.
* Confirmation ou infirmation de l'absence de nouvelle règle implicite.
* Conclusion sur l'aptitude de la v0.4.3 à être archivée.

Distinguer les défauts du document des réserves structurelles déjà connues : sources non authentifiées, archivage non effectué et paramètres volontairement ouverts.
Ne pas exiger la résolution de mécaniques reportées comme condition de conformité documentaire.
4. Restrictions
Lecture seule sur le dépôt Bastion et sur le clone d'OXCE.
Les fichiers de travail du relecteur sont autorisés uniquement dans un dossier distinct du scratchpad.
Aucune modification de la consolidation v0.4.3 pendant sa revue.
Aucun commit, push, branche, PR ou inscription documentaire.
Aucun développement, aucune modification du code ni des tests du jeu.
Aucune nouvelle décision prise à la place du propriétaire.
MEC-0001 et MEC-0002 restent reportées.
Arrêter le travail après remise du rapport. L'archivage nécessitera une autorisation distincte.

---

## Message M — JS-40, horodatage du journal : 2026-11-20T17:09:00.014Z

BASTION — Mandat d'erratum documentaire v0.4.3
Objet : corriger exclusivement AR-01 et AR-02, avant archivage.
Base : consolidation MEC-0001 v0.4.3 et rapport de contrôle indépendant correspondant.
1. Corrections autorisées
AR-01 — Comparaison avec OXCE
Corriger uniquement la phrase concernée au §5.
La nouvelle rédaction doit :

* limiter le constat à ce que démontre effectivement le code d'OXCE ;
* distinguer le comportement de la fonction examinée des paramètres de récupération calculés ailleurs ;
* tenir compte des paramètres éventuels de l'armure ;
* conserver les références au code vérifié ;
* ne modifier aucune règle de Bastion.

AR-02 — Nature des contrôles
Corriger uniquement l'introduction du §17.
Distinguer explicitement :

* les contrôles automatisés effectivement exécutés, dont le code de sortie est connu ;
* les vérifications documentaires réalisées par relecture.

Les contrôles 3, 4, 9 et 11 ne doivent plus être présentés comme entièrement automatisés.
2. Travail demandé

1. Produire une version corrigée de la consolidation v0.4.3, identifiée comme v0.4.3 avec erratum AR-01/AR-02.
2. Conserver une copie intacte de la v0.4.3 initiale.
3. Produire un diff contenant uniquement les deux corrections et les métadonnées strictement nécessaires.
4. Calculer les empreintes SHA-256 des deux versions et du diff.
5. Faire vérifier ce diff par un relecteur distinct.
6. Remettre le résultat du contrôle indépendant.

Ne pas corriger les observations facultatives OC-01 à OC-07.
3. Restrictions
Travail documentaire exclusivement, hors du dépôt.
Aucune modification des décisions, valeurs, scénarios ou matrices.
Aucune modification du dépôt GitHub, aucun commit, push, branche ou PR.
Aucun archivage ni inscription documentaire.
Aucune implémentation.
MEC-0001 et MEC-0002 restent reportées.
Arrêter le travail après remise du contrôle indépendant.

---

## Message N — JS-41, horodatage du journal : 2026-11-20T18:08:14.609Z

BASTION — Préparation de l'archivage documentaire MEC-0001
Objet : préparer l'archivage de la consolidation Q1 à Q5 et B3, sans inscription des règles ni implémentation.
Statut : préparation uniquement. Aucune opération d'écriture dans le dépôt n'est autorisée.
1. Documents de référence
La consolidation v0.4.3 originale, son erratum AR-01/AR-02 et les rapports de contrôle indépendant constituent le dossier documentaire de référence.
Le dernier rapport indépendant conclut à une aptitude à l'archivage, sous deux réserves mineures AE-01 et AE-02.
La décision du propriétaire est de conserver l'erratum en l'état, accompagné du rapport signalant ces deux réserves. Aucun second erratum n'est demandé.
2. Inventaire à préparer
Recenser les pièces nécessaires :

* Consolidation v0.4.3 originale, inchangée.
* Erratum AR-01/AR-02, inchangé.
* Consolidations antérieures utiles à la traçabilité.
* Pièces justificatives P1 à P7.
* Validations et arbitrages du propriétaire.
* Rapports de revue et de contrôle indépendant.
* Scripts de vérification et leurs résultats, lorsqu'ils sont disponibles.
* Mandats associés.
* Empreintes SHA-256 vérifiées.

Distinguer les pièces déjà archivées, celles qui restent dans le scratchpad et celles qui sont seulement citées mais indisponibles.
Ne pas inventer de document manquant.
3. Réserves obligatoires
Préparer une notice de provenance mentionnant explicitement :
AE-01 : l'explication de la récupération énergétique d'OXCE dans l'erratum est incomplète. Elle doit être lue avec le rapport indépendant, qui précise le rôle des bonus du soldat.
AE-02 : la comparaison section par section du contrôle 11 n'est pas étayée par un script conservé. Elle doit être considérée comme une vérification documentaire par relecture.
Conserver également les limites d'authentification des sources, les formulations Q4 résumées, les neuf PNV et les paramètres volontairement ouverts.
Ne pas transformer une réserve documentaire en décision de gameplay.
4. Organisation proposée
Proposer une arborescence simple dans `docs/`, réutilisant autant que possible les dossiers existants.
Éviter les copies inutiles, les fichiers redondants et les mécanismes de gouvernance supplémentaires.
Prévoir un inventaire permettant de retrouver chaque pièce, sa provenance, son statut et son empreinte.
5. Contrôles préalables
Avant toute demande d'inscription ou d'archivage effectif :

1. Vérifier l'état actuel de `main`.
2. Identifier précisément les fichiers à ajouter.
3. Vérifier les empreintes.
4. Détecter les doublons avec les documents déjà archivés.
5. Contrôler que la v0.4.3 et son erratum restent intacts.
6. Présenter la liste exhaustive des opérations Git envisagées.
7. Signaler toute pièce manquante ou dont la provenance est insuffisante.

6. Livrable attendu
Remettre un plan d'archivage documentaire comprenant :

* l'inventaire des pièces ;
* les chemins de destination proposés ;
* les fichiers déjà présents dans le dépôt ;
* les fichiers nouveaux ;
* les réserves à conserver ;
* les contrôles prévus après archivage ;
* la liste exacte des opérations Git nécessaires.

Terminer par une demande d'autorisation explicite au propriétaire avant toute modification du dépôt.
7. Restrictions
Pour ce mandat :

* lecture seule sur le dépôt ;
* travail préparatoire uniquement hors dépôt ;
* aucun commit, push, branche ou PR ;
* aucune modification des registres de décisions ;
* aucune correction supplémentaire de la consolidation ;
* aucune implémentation.

MEC-0001 et MEC-0002 restent reportées.
L'archivage effectif et l'inscription des décisions feront l'objet d'autorisations distinctes.
