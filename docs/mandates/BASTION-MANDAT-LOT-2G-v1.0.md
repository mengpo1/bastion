# BASTION — Mandat LOT-2G v1.0
## Préparation des arbitrages techniques bloquants de MEC-0001

**Statut : PRÉPARÉ — EXÉCUTION NON AUTORISÉE**  
**Dépôt :** `mengpo1/bastion`  
**Référence de départ :** `main`, contenant la fusion de la PR n° 9 (commit de fusion `72908389ea99f7267f7f723c57b488f640bfe441`), à revérifier par `git fetch origin main` avant tout travail.  
**Branche proposée :** `docs/lot-2g-mec-0001-arbitrages` (à créer seulement après mandat d'exécution explicite).  
**Nature :** étude, propositions et préparation des choix du propriétaire ; **aucun code et aucune décision nouvelle présumée validée**.  
**Référence OXCE :** `MeridianOXC/OpenXcom`, commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b` (référence 8.7.1).  
**Provenance :** décisions antérieures de la conversation Bastion, registre et documents du LOT-2F ; le mandat LOT-2G est un projet préparatoire, pas une nouvelle acceptation de gameplay.

## 1. Objectif

Produire un **dossier de décisions techniques** permettant au propriétaire de trancher les **13 points bloquants** recensés après correction du LOT-2F, sans reprendre les règles de gameplay déjà validées.

Le LOT-2G ne vise **ni à implémenter MEC-0001, ni à déclarer MEC-0001 acceptée globalement, ni à combler silencieusement des lacunes**. Un point est « résolu » seulement si le propriétaire accepte explicitement une solution, ou si une démonstration établit qu'il découle mécaniquement d'une décision déjà acceptée. Sinon, il reste ouvert.

## 2. Sources obligatoires

1. `CLAUDE.md` et `docs/mandates/README.md` ;
2. `docs/gameplay/GAMEPLAY-DECISIONS.md`, notamment S1 à S12, Z1 et N1 à N14 ;
3. `docs/reviews/LOT-2E-VERTICALITE-OXCE.md` ;
4. `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` ;
5. `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md` ;
6. `docs/references/OXCE-BASELINE.md` ;
7. si nécessaire, fichiers sources OXCE au commit figé ; distinguer toujours **lecture du code**, **observation en exécution**, **inférence** et **proposition Bastion**.

La PR n° 9 et son correctif documentaire sont fusionnés dans `main`. Les décisions E14, E18 et E23 sont **déjà confirmées et ne doivent pas être remises en question** : un ennemi actuellement visible peut être ciblé par un saut offensif ; après esquive réussie, l'attaquant subit les règles de chute au sol avec plafond 70 avant l'aléatoire ; le poids total de collision comprend le corps, l'armure, l'équipement et l'inventaire, distinct de la charge portée.

## 3. Périmètre exact : 13 points

Traiter les points ci-dessous avec les **identifiants du LOT-2F inchangés**.

| ID | Question à formaliser | Exigence à préserver |
|---|---|---|
| **E1** | Dimensions des cases et des étages, repère physique, volume occupé par une unité, position du premier contact | Collision du **volume**, pas seulement du centre ; gravité de référence 1 g. Ne pas choisir une échelle métrique sans arbitrage. |
| **E2** | Compatibilité entre trajectoire physique continue, vitesse horizontale ajustable et portée en distance de Manhattan ; conversion de la portée en cases | À 1 g et pour un étage de descente : **2 cases Manhattan** ; gravité et dénivelé modifient la portée. Ne pas remplacer cette règle par une portée euclidienne non décidée. |
| **E3** | Gravité nulle et gravités extrêmes ; domaine autorisé et résultat d'un saut lorsque le vol ne se termine pas | Gravité configurable ; aucune règle de gravité zéro n'est encore acceptée. |
| **E5** | Arrondis et ordre numérique des étapes, y compris `B(n)`, plafonds, bonus, tirage 50–150 %, coefficients et valeurs extrêmes | Préserver les paramètres initiaux acceptés ; aucun arrondi implicite. |
| **E6** | Formule **atténuée** du rapport de poids entre deux unités ; effets sur les deux unités | Les deux peuvent subir des dégâts asymétriques ; formule distincte de `min(M/80,3)` pour les obstacles ; poids total E23 validé. |
| **E7** | Type de dégâts, interaction avec les protections d'OXCE, côté d'armure, santé, étourdissement et mise hors de combat | Ne pas attribuer une mécanique propre à Bastion à OXCE ; exposer les écarts et compatibilités réellement établis. |
| **E8** | Conversion de la vitesse normale au contact en puissance d'impact ; articulation avec `B(n)` et les collisions entre unités ; éviter de compter deux fois une contribution | Début/milieu/fin de course : **diagnostic seulement**, pas de multiplicateur arbitraire ; plafond obstacle 70, unité tombante 60, cible 80, sol 70. |
| **E9** | Ordre des collisions multiples, destination devenue occupée/libre, tailles d'unités, perte de support, chaîne de chutes | Résolution chronologique ; arrêt sur obstacle même s'il est détruit ; chute verticale distincte si plus de support ; ne pas révéler l'inconnu à l'avance. |
| **E11** | Sens de l'« impulsion verticale constante » : vitesse initiale ou quantité de mouvement, notamment sous différentes charges | À 1 g, montée maximale initiale : **un quart d'étage** ; gravité plus faible = montée plus haute pour une même action. |
| **E12** | Définition du nombre d'étages traversés ; hauteurs partielles, impacts entre niveaux, chutes de moins d'un étage ; probabilité d'esquive aux bornes | Bonus de **5 points** par niveau traversé, probabilités bornées 0–100 % ; dommages possibles dès un étage. |
| **E13** | Coût en TU du déplacement composant un saut et moment de paiement | Supplément offensif `max(1, floor(0,20 × TU_max))`, payé à l'engagement et jamais remboursé ; coût total et prévisualisation doivent rester cohérents. |
| **E17** | Esquive pendant le tour adverse ; réserve de TU utilisée ; cases voisines valides, diagonales, niveau et visibilité | Esquive seulement si la cible voit l'unité tombante, possède les TU requises et une case accessible ; choix aléatoire ; paiement uniquement en cas de réussite. |
| **E24** | Effets du poids total, de l'armure, des caractéristiques et équipements sur une chute au sol | Aucun double comptage ; dégâts de base fixes selon la hauteur puis protections et effets prévus, à préciser ; N8–N10 à respecter. |

Les autres points du LOT-2F (**E4, E10, E15, E16, E19, E20, E21, E22**) restent visibles dans le registre des questions, mais ne doivent **pas** être présentés comme faisant partie des 13 blocages à résoudre dans ce lot. Relever toute dépendance directe sans étendre silencieusement le périmètre.

## 4. Méthode de travail

### A — Regrouper les problèmes en quatre paquets cohérents

1. **Géométrie et physique :** E1, E2, E3, E11, E12.
2. **Dégâts et masses :** E5, E6, E7, E8, E24.
3. **Règles d'action et résolution :** E9, E13, E17.
4. **Vérification transversale :** cohérence entre les trois paquets, références OXCE et impacts sur la matrice de tests.

Les paquets servent à organiser le rapport ; **ils ne constituent pas des validations collectives**. Toute proposition de lotissement supplémentaire doit être signalée.

### B — Pour chacun des 13 points

Présenter dans un tableau homogène :

- **Énoncé exact du problème** et référence des règles concernées ;
- **Ce qui est déjà décidé** (avec source) et ce qui ne l'est pas ;
- **Une solution recommandée**, si possible, clairement marquée **PROPOSITION NON VALIDÉE** ;
- **Une alternative réellement différente**, si utile, avec avantages/inconvénients, complexité et conséquences visibles pour le joueur ;
- **Équations et exemples numériques**, uniquement lorsque les hypothèses sont explicitement déclarées ;
- **Compatibilité avec les paramètres validés** ;
- **Risques techniques**, cas limites et dépendances envers d'autres points ;
- **Critère de test** et tests du LOT-2F concernés ;
- **Question d'arbitrage** formulée simplement pour le propriétaire, sans lui demander de comprendre le code source.

Lorsqu'il existe une incompatibilité logique entre des règles acceptées, **ne pas la masquer** : apporter une démonstration, identifier les règles en conflit et proposer des solutions **sans en adopter une**.

### C — Préférence pour les solutions simples

Favoriser un modèle cohérent, calculable de manière déterministe et facilement testable, sous réserve du respect des décisions du propriétaire. Ne pas créer de nouvelles caractéristiques, mécanismes ou systèmes de dégâts pour résoudre un problème de calcul sans justification explicite. Une valeur « illustrative » ne devient jamais une valeur retenue.

### D — Préparer les arbitrages sans les présumer

Le livrable doit comporter une **synthèse pour le propriétaire**, en français, de taille raisonnable : d'abord les 3 à 5 décisions structurantes, puis les décisions dépendantes. Regrouper les choix interdépendants pour éviter 13 questions isolées. Séparer les éléments **dérivables** de ceux qui exigent un choix de conception. Les 13 points sont **ouverts jusqu'à validation explicite**.

## 5. Livrables proposés

À produire **uniquement après mandat d'exécution explicite** :

1. `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md` : matrice des 13 points, propositions non validées, variantes, conséquences, questions au propriétaire et ordre d'arbitrage.
2. `docs/reviews/LOT-2G-IMPACTS-TESTS.md` : correspondance entre chaque solution proposée et les scénarios du LOT-2F qui deviendraient spécifiables ; aucun test exécutable.
3. Mise à jour de `docs/mandates/README.md` pour archiver et indexer **ce mandat exact**, transmis par le propriétaire et vérifié au SHA-256 ; ne pas modifier le fichier original.

Ne pas réécrire les livrables du LOT-2F : ils sont le **point de départ vérifiable**. Le statut des décisions du propriétaire ne change pas pendant LOT-2G.

## 6. Interdictions et protection du dépôt

- **Aucun gameplay, aucun code C#, aucune scène Godot, aucun test exécutable.**
- **Aucune écriture** dans `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/decisions/TECHNICAL-DECISIONS.md`, `docs/references/`, `CLAUDE.md`, les scripts du harnais, les workflows CI, les fichiers `src/` ou `tests/`.
- Ne pas modifier ni réinterpréter les valeurs validées au LOT-2F, ni les trois corrections E14/E18/E23.
- Ne pas copier de code ou d'assets X-COM/OXCE ; seulement citer et analyser la référence figée, conformément à D4.
- Travail sur **branche dédiée**, jamais sur `main`.
- **Aucun push, aucune PR, aucun merge, aucun force push sans autorisation explicite distincte et limitée au lot**. L'approbation de préparation exprimée dans cette conversation ne constitue pas une autorisation de publication.
- Ne pas enchaîner sur LOT-2H ou sur une implémentation.

## 7. Vérifications et revue indépendante

- Démarrer par `git fetch origin main`, vérifier le point de départ et l'état de la branche.
- Faire un contrôle de complétude : exactement 13 identifiants E1, E2, E3, E5, E6, E7, E8, E9, E11, E12, E13, E17, E24, sans doublon ni oubli.
- Vérifier l'identité octet pour octet de l'archive du mandat (SHA-256), les références croisées et les hypothèses des équations.
- Distinguer les valeurs calculées des valeurs de conception proposées ; aucune équation ne doit modifier implicitement la règle de Manhattan ou les quatre plafonds.
- Exécuter les contrôles documentaires adaptés, consigner les commandes, sorties et codes de retour.
- Charger un relecteur indépendant en **lecture seule** : cohérence des formules, conformité au LOT-2F, traçabilité OXCE, absence de décision inventée, limites de test, diff exact.
- Remettre un rapport final dans `docs/reviews/` avec état réel de la revue et des contrôles. N'affirmer aucune exécution de test .NET ou d'OXCE sans preuve.

## 8. Condition de clôture

Le LOT-2G documentaire est clos quand les 13 blocages sont **exposés avec des propositions arbitrables**, leurs dépendances et leurs effets sur les tests, et quand les décisions restant à prendre sont clairement séparées des règles acquises.

**Le lot ne clôt pas les 13 décisions par lui-même.** Seul le propriétaire peut les valider lors d'une étape suivante. La fiche globale MEC-0001 demeure à son statut documentaire courant jusqu'à un mandat distinct, expressément autorisé, d'actualisation du registre.

**Arrêt impératif après livraison et revue documentaire du LOT-2G.**
