# Déclarations et addenda du propriétaire, 19 novembre 2026 — Q4.6, Q4.7, Q5.1, Q5.2, B3

Copie, par Claude Code, de cinq messages du propriétaire reçus dans la conversation du 19 novembre 2026, dans l'ordre de réception, tels que reçus, sans correction. Ils ne sont ni archivés dans le dépôt ni dotés d'une empreinte. Les textes des propositions d'origine (options) de Q5.1, Q5.2 et B3, et les propositions d'origine de Q4.6 et Q4.7, n'ont pas été transmis.

---

## Message A — Provenance Q1–Q3 (repères horaires) et valeurs de Q4.6 et Q4.7

J'ai examiné ton rapport de revue indépendante.
La réserve de provenance Q1–Q3 est fondée pour le dossier transmis. Toutefois, les validations historiques ont eu lieu le 19 novembre 2026 et leurs traces ont été retrouvées :

* Q1 : vers 14 h 26–14 h 29 UTC, notamment validation de Q1.4 puis Q1.5–Q1.9.
* Q2 : vers 14 h 38 UTC, validation des options A pour Q2.1–Q2.6.
* Q3 : vers 14 h 43–14 h 47 UTC, validations successives de Q3.1–Q3.14.

Ces indications servent à identifier les échanges d'origine ; elles ne constituent pas encore un verbatim intégral ni une preuve documentaire suffisante.
Maintiens donc la réserve de traçabilité jusqu'à disponibilité des messages sources. Ne transforme pas ces informations en preuve indépendante.
Pour Q4.6 et Q4.7, les valeurs 60/60/100/20 et 4 TU/0 énergie figuraient expressément dans les propositions acceptées par option A. Elles constituent des valeurs initiales configurables de test, et non des constantes universelles.
Conserve les autres anomalies pertinentes et distingue les corrections purement documentaires des arbitrages qui exigent une nouvelle décision.
N'effectue aucune modification du dépôt, aucun commit ni aucune implémentation.

---

## Message B — Q5.1 et Q5.2

Pour Bastion MEC-0001, prends en compte les précisions suivantes dans ton rapport documentaire.

**1. B1 est déjà tranchée : Q5.1=A, validée le 19 novembre 2026.**

Lorsqu'un tir de réaction interrompt la marche, le pas déjà engagé est achevé avant la résolution du tir, sauf événement physique prioritaire comme une perte de support. Le pas est débité une seule fois et l'ordre est interrompu, même si le tir manque.

Conserve les conditions de détection et de déclenchement d'Overwatch hors de cet arbitrage.

**2. B2 est déjà tranchée : Q5.2=A, validée le 19 novembre 2026.**

Une plateforme peut accueillir plusieurs unités si sa capacité, sa géométrie et ses emplacements tactiques distincts le permettent.

Deux unités conscientes ne peuvent pas partager le même emplacement tactique stable. Q5.2 ne crée donc aucune exception supplémentaire à S10.

**3. B3 reste ouverte.**

Ne considère pas que Q1 a automatiquement modifié GE-02 et GE-03 de MEC-0002. Signale cette articulation comme nécessitant une précision explicite.

**4. Provenance Q1–Q3.**

Maintiens la réserve bloquante tant que les messages originaux ne sont pas disponibles. Les dates et heures indiquées ne constituent pas des preuves suffisantes.

**5. Coûts nuls.**

Corrige l'anomalie 8 : sur un graphe fini à coûts non négatifs, les chemins à coût nul n'empêchent pas l'existence d'un minimum lexicographique. La réserve concerne les cycles gratuits, la terminaison de la recherche et le départage déterministe.

**6. Statut.**

Actualise le tableau des anomalies et la matrice de traçabilité en distinguant les décisions du propriétaire des corrections documentaires proposées.

Cette demande ne constitue pas une nouvelle revue indépendante ni une autorisation d'inscription.

Aucun fichier modifié, aucun commit, push, branche, PR ou implémentation.

---

## Message C — Addendum documentaire Q5.1–Q5.2

BASTION — MEC-0001
Addendum documentaire Q5.1–Q5.2 et rectifications de la revue
Date : 19 novembre 2026
Statut : Projet de rectification documentaire
Portée : Consolidation Q1–Q4 et rapport de revue indépendante
Implémentation : Interdite
A. Décision Q5.1 — Tir de réaction pendant un pas
Validation du propriétaire : Q5.1=A.
Un tir de réaction qui interrompt une marche ordinaire est résolu à la frontière du pas tactique engagé, une fois ce pas achevé.

* Le pas engagé est débité une seule fois.
* L'unité atteint la destination tactique admissible du pas avant la résolution du tir.
* Le tir effectivement effectué interrompt l'ordre, même s'il manque.
* Un simple pivot sans tir n'entraîne pas l'interruption prévue par ARB-E.
* La perte de support et les autres événements physiques prioritaires restent immédiatement applicables conformément à Q4.3 et MEC-0002.
* Les conditions de détection, de déclenchement et les coûts d'Overwatch demeurent hors de cet arbitrage.

Références : ARB-E, Q3.4, Q4.3, Q4.20, Q4.21, EN-03.
Rectification demandée : distinguer explicitement un pas non commencé, un pas engagé, un pas achevé et un événement physique prioritaire.
B. Décision Q5.2 — Occupation d'une plateforme
Validation du propriétaire : Q5.2=A.
Une connexion peut avoir une capacité supérieure à une unité. Cette capacité ne supprime pas les règles d'occupation de S10.

* Chaque unité consciente occupe un emplacement tactique stable distinct lorsqu'elle est en position stable.
* Aucune superposition volontaire de deux unités conscientes sur un même emplacement stable n'est autorisée.
* Une plateforme comportant plusieurs emplacements peut accueillir plusieurs unités si la capacité et les volumes physiques le permettent.
* Une plateforme ne comportant qu'un emplacement tactique stable ne peut pas accueillir deux unités conscientes à cet emplacement.
* Le transit physique reste soumis aux contrôles de volume et d'occupation de Q4.8 et Q4.15.
* L'exception transitoire au réveil prévue par G2 reste inchangée.

Références : S10, ARB-B, ARB-C, G2, Q4.8, Q4.15.
Rectification demandée : expliciter que Q4.15 ne constitue pas une exception supplémentaire à S10.
C. Corrections documentaires à préparer
Le rapport indépendant relève plusieurs rectifications nécessaires :

1. Ajouter Q5.1 et Q5.2 à la matrice de traçabilité et aux scénarios de vérification.
2. Distinguer les valeurs initiales configurables des données fictives des anciennes consolidations.
3. Documenter les règles historiques précisées ou supplantées par Q1–Q4.
4. Réconcilier explicitement les dimensions métriques proposées par Q1 avec GE-02 et GE-03 de MEC-0002, sans modifier tacitement cette dernière fiche.
5. Définir les critères de test manquants pour les dimensions, la surcharge, les connexions, les rotations et le réveil.
6. Conserver les questions non résolues : rotation balayée, dénivelés locaux, coûts nuls, géométrie intermédiaire, autres postures et paramètres de MEC-0002.
7. Conserver les remarques sur l'arithmétique exacte et les arrondis pour les futurs tests.

Ces corrections ne doivent pas introduire de décision supplémentaire.
D. Provenance
La validation explicite de Q5.1=A et Q5.2=A figure dans le message du propriétaire du 19 novembre 2026.
La revue indépendante a déclaré Q1–Q3 « provenance non vérifiée », faute de verbatim accessible dans son dossier.
Cette réserve reste ouverte tant que les échanges d'origine ou une attestation documentaire suffisante ne sont pas fournis.
Aucune validation supplémentaire de Q1–Q3 ne doit être déduite de Q5.1 ou Q5.2.
E. Conditions de clôture
La revue ne pourra être déclarée pleinement conforme qu'après traitement documenté des anomalies, vérification des preuves de validation et nouvelle appréciation indépendante.
MEC-0001 reste reportée dans son ensemble. Aucun gameplay ni développement autorisé.

---

## Message D — Addendum B3

# BASTION — Addendum B3
## Géométrie physique commune à MEC-0001 et MEC-0002

**Décision :** B3=A  
**Validation :** propriétaire, 19 novembre 2026  
**Statut :** formulation documentaire préparée, non inscrite  
**Implémentation :** non autorisée

### B3-01 — Référentiel géométrique unique

MEC-0001 et MEC-0002 utilisent le même référentiel physique : coordonnées spatiales, dimensions des cases, niveaux, surfaces, volumes de collision, postures et orientations.

Les distances et dimensions physiques sont exprimées en millimètres. Les paramètres géométriques sont configurables et partagés par les deux mécaniques.

Il ne doit pas exister de dimensions concurrentes d'une même unité selon qu'elle marche, saute ou tombe.

### B3-02 — Précision apportée à GE-02

La clause historique « largeur de case et volumes des unités en proportions, sans mètres fixés » est modifiée par B3.

Les dimensions disposent désormais de valeurs métriques configurables communes à MEC-0001 et MEC-0002.

Sous réserve de confirmation documentaire des décisions Q1, les valeurs initiales prévues sont notamment :

- largeur de case : 1 500 mm ;
- hauteur entre sols de référence de deux étages consécutifs : 3 000 mm ;
- murs standards : épaisseur initiale de 100 mm.

Ces valeurs ne sont pas des constantes universelles. Le moteur doit pouvoir utiliser d'autres configurations admissibles.

La hauteur d'étage de 3 000 mm demeure la règle explicitement validée par Q4.1.

### B3-03 — Précision apportée à GE-03

Chaque type d'unité possède des dimensions physiques configurables, dépendant de sa posture.

Le profil humain initial proposé par Q1 est :

| Posture | Dimensions |
|---|---|
| Debout | 600 × 600 × 1 800 mm |
| Agenouillé | 600 × 600 × 1 200 mm |
| Couché | 1 200 × 600 × 500 mm |

Les dimensions et orientations pertinentes sont communes aux deux mécaniques.

La conservation de la posture et de l'orientation pendant le vol, prévue par GE-04, reste applicable.

Ces valeurs Q1 doivent conserver une mention de provenance non vérifiée jusqu'à l'archivage de leur validation originale.

### B3-04 — GE-05 et CO-01 inchangées

Une géométrie commune ne modifie pas les règles de contact et d'impact.

GE-05 conserve la distinction entre contact détecté et dommage d'impact.

CO-01 conserve la détection des contacts à partir des volumes physiques réels au moment du contact.

Les enveloppes englobantes éventuellement utilisées pour les calculs ne doivent pas être confondues, sans justification, avec les volumes réels exigés par CO-01.

Le traitement exact des rotations, des arrondis et des enveloppes de calcul reste soumis aux conventions géométriques à qualifier.

### B3-05 — Responsabilités inchangées

MEC-0001 demeure responsable de la marche ordinaire, de son cheminement, de ses coûts et de ses connexions spéciales.

MEC-0002 demeure responsable des sauts, chutes, contacts et collisions relevant de son périmètre.

B3 n'autorise aucune nouvelle mécanique et ne modifie pas les règles de dégâts.

### B3-06 — Statut documentaire

B3=A est validée.

La compatibilité de principe est établie par lecture des règles existantes ; elle ne constitue pas une validation de code ou de tests.

Les preuves de validation détaillées de Q1 à Q3 demeurent à réunir.

MEC-0001 et MEC-0002 restent reportées dans leur ensemble.

Aucune inscription ni implémentation n'est autorisée par cet addendum.

---

## Message E — Rectificatif de l'addendum B3

# BASTION — Rectificatif de l'addendum B3

**Statut :** proposition de rectification documentaire  
**Date :** 19 novembre 2026  
**Implémentation :** non autorisée

### 1. Unités physiques et précision des calculs

B3 établit un référentiel géométrique commun à MEC-0001 et MEC-0002.

Les dimensions physiques configurées peuvent être exprimées en millimètres. Les hauteurs exprimées en mètres dans CH-08 restent compatibles par conversion d'unités : 3 m correspondent à 3 000 mm.

La contrainte Q1 des millimètres entiers ne doit pas être étendue implicitement aux grandeurs physiques intermédiaires calculées par MEC-0002.

La précision et les arrondis des trajectoires, vitesses, hauteurs équivalentes et autres calculs physiques restent à qualifier.

### 2. Hauteur des étages

La hauteur de 3 m entre deux sols d'étages consécutifs provient de GE-02, précisée historiquement par A3A et reprise dans CH-08.

Q4.1 précise son application aux sols de référence des étages tactiques et la distinction avec les dénivelés locaux.

B3 conserve cette hauteur et n'introduit aucune nouvelle valeur.

### 3. Paramètres géométriques ouverts

B3 tranche le principe des dimensions métriques configurables et partagées.

GE-02 et GE-03 doivent être annotées pour rendre explicite cette évolution.

Les valeurs initiales attribuées à Q1 conservent le statut « provenance non vérifiée » jusqu'à l'obtention des messages d'origine.

Sous réserve de leur confirmation, une case de 1 500 mm et une hauteur d'étage de 3 000 mm donnent un rapport case/étage de 0,5.

Les profils et dimensions des autres types d'unités restent configurables.

### 4. Configurations admissibles

B3 n'établit pas à lui seul l'ensemble des contraintes de validité des configurations.

La parité de la largeur des cases, les dimensions minimales, les tolérances géométriques et les conventions d'arrondi doivent être rattachées à leurs décisions sources ou laissées explicitement ouvertes.

Aucune contrainte supplémentaire n'est créée par le présent rectificatif.

### 5. Portée de l'inscription future

B3 modifie explicitement la formulation de GE-02 et précise GE-03 dans MEC-0002.

Une éventuelle inscription devra donc être autorisée pour les sections concernées de MEC-0001 **et de MEC-0002**, tout en conservant leur statut reporté.

Aucune inscription n'est actuellement autorisée.
