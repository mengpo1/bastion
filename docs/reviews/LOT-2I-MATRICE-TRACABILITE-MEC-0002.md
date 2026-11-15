# LOT-2I — Matrice de traçabilité de `MEC-0002`

Compagnon de `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md`, qui donne le texte de chaque règle. **Aucune décision nouvelle, rien d'inscrit au registre, aucun test exécutable.**

**Correctif v1.2** : la matrice intègre les arbitrages C3 (consolidation, §1 et §14). Les lignes des 23 règles modifiées citent C3 ; les critères de tests changés sont listés au §3.1, avec leur version v1.1.

**Sources** : comme dans la consolidation, §1.
- **C2** : consolidation provisoire de l'orchestrateur, `orchestration/mandats`, commit `d028c52`, SHA-256 `8e7c652b…dd83`.
- **D2** : déclaration du propriétaire du 14 novembre 2026 (29 propositions et arbitrages 1A à 6A acceptés).
- **C3** : arbitrages complémentaires du 14 novembre 2026, transcrits par l'orchestrateur dans le mandat v1.2 (§2) ; preuve déclarative. Libellés A3A, A4.1D à A4.3A et exception de surcharge (qui précisent le choix A4C, « Revoir le seuil et les exceptions »), A8A, D1C à D4A, et « oui » à A12, A18, A24, A25, A27 (consolidation, §1).
- **DS** : principes du 13 novembre 2026.
- **M** et **P** : décisions du 9 novembre 2026 et correctif, transcrits au LOT-2F (non inscrits).
- **R** : registre sur `main` (8 novembre 2026).

**Colonnes.**
- **Source primaire** : la décision d'origine, puis la section de C2 qui la reprend. Toutes les règles de C2 sont couvertes par D2. GE-09 et RP-09 viennent de DS1 à DS5 seuls : C2 ne les redit pas.
- **Date** : date de la décision d'origine. La reprise par C2 et D2 date, pour toutes les règles de C2, du 14 novembre 2026 ; la date de chaque proposition n'est pas plus précise (consolidation, §13).
- **Priorité** :
  - « concordant » : C2 reprend la règle sans changement de sens ;
  - « C2 précise » : C2 ajoute un détail compatible ;
  - « C2 prévaut » : C2 modifie ou remplace une règle plus ancienne, et la décision récente l'emporte ;
  - « C2 tranche » : C2 décide un point qui était ouvert ;
  - « nouveau » : règle sans antécédent ;
  - « maintenue » : décision antérieure que C2 ne redit pas, mais ne modifie pas (C2 §1 : une décision récente ne prévaut que si elle modifie une hypothèse ancienne) ;
  - « C3 prévaut » : un arbitrage du correctif v1.2 remplace une règle de C2 ou une décision plus ancienne ;
  - « C3 précise » : un arbitrage v1.2 ajoute un détail compatible ;
  - « C3 confirme » : un arbitrage v1.2 confirme un point laissé à confirmer par le v1.1, ou une règle déjà validée (CH-02).
- **Conflit** : renvoi à la consolidation (§11.1 point *n*, §11.2 X*n*, ou ambiguïté A*n* du §12) ; « réglée » signale une ambiguïté tranchée par C3.
- **Statut** : repris automatiquement de la consolidation.

## 1. Matrice de provenance des 105 règles

### 1.1 Périmètre

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| PE-01 | Marche dans MEC-0001 ; MEC-0002 fait autorité | C2 §2 ; D2 ; C3 (A24) | 14 nov. 2026 | LOT-2H : sauts, chutes, collisions dans MEC-0001 (proposé, non inscrit) | C2 prévaut ; C3 confirme | §11.2 X10 ; A24 (réglée) | validé en conception |
| PE-02 | Périmètre de MEC-0002 | C2 §2 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| PE-03 | Exclusions (escaliers, brouillard, TU, structure) | C2 §2 ; D2 | 14 nov. 2026 | N4 (R) : changements de niveau prévus | concordant (hors périmètre) | — | validé en conception |
| PE-04 | Pas d'autorisation par analogie | C2 §2 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |

### 1.2 Géométrie, masse et posture

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| GE-01 | Positions (x, y, z) | R : N3 ; C2 §3 | 8 nov. 2026 | N3 : plusieurs niveaux, positions (x, y, z) | concordant | — | validé en conception |
| GE-02 | Proportions ; étage de 3 m | DS1.1 ; C2 §3 ; C3 (A3A) | 13 et 14 nov. 2026 | DS1.1 et C2 §3 : proportions, sans échelle en mètres | C3 précise (hauteur d'étage) | §11.2 X13 ; A1 | validé en conception, paramètre ouvert |
| GE-03 | Pavés par type ; postures | DS1.2 ; C2 §3 ; D2 | 13 et 14 nov. 2026 | DS1.2 : pavés, collisions sur le volume | C2 précise (postures) | — | validé en conception, paramètre ouvert |
| GE-04 | Posture et orientation figées en vol | C2 §3 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| GE-05 | Contact, vitesse normale, agrégation | D11 (M) ; C2 §3 ; D2 | 9 et 14 nov. 2026 | D11 : vitesse normale distincte de la tangentielle | C2 précise | — | validé en conception, paramètre ouvert |
| GE-06 | Masse totale M | E23 (P) ; C2 §3 | 9 nov. 2026 | E23 : poids total = corps + armure + équipement + inventaire | concordant | — | validé en conception, paramètre ouvert |
| GE-07 | Charge portée en kg ; Force → capacité | N10, N14 (R) ; C2 §3 ; D2 | 8 et 14 nov. 2026 | N14 : rapport Force / poids porté (OXCE) ; E20 : unité de la charge ouverte | C2 précise (kg) | — | validé en conception, paramètre ouvert |
| GE-08 | Grandes unités : aucun saut volontaire | DS5.5 ; C2 §3 ; D2 (proposition 8/29) | 13 et 14 nov. 2026 | DS5.5 : pas d'attaque sautée par une grande unité, ni contre elle | C2 prévaut (extension) | §11.1 point 6 | validé en conception |
| GE-09 | Grande unité non ciblée par une attaque sautée | DS5.5 (C2 ne la redit pas) ; C3 (A12) | 13 et 14 nov. 2026 | DS5.5 : pas choisie comme cible d'une attaque sautée | maintenue ; C3 confirme | §11.1 point 6 ; A12 (réglée) | validé en conception |

### 1.3 Sauts

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| SA-01 | Saut simple, même niveau ou plus bas | C2 §4.1 ; D2 | 14 nov. 2026 | N5 (R) : chutes volontaires autorisées | nouveau | §11.2 X16 ; A30 | validé en conception |
| SA-02 | Attaque : au moins un étage plus bas | J01 (M) ; C2 §4.1 | 9 nov. 2026 | J01 : au moins un étage de dénivelé vers le bas | concordant | — | validé en conception |
| SA-03 | Allié ou neutre identifié non ciblable | J06 (M) ; C2 §4.1 | 9 nov. 2026 | J06 | concordant | — | validé en conception |
| SA-04 | Ennemi visible ciblable malgré S10 | J13, E14 (P) ; DS1.4 ; C2 §4.1 | 9 et 13 nov. 2026 | J13 : exception explicite à S10 | concordant | — | validé en conception |
| SA-05 | Destination visible ou explorée | J03, J04 (M) ; S6 (R) ; C2 §4.1 | 8 et 9 nov. 2026 | J03, J04 ; S6 | concordant | — | validé en conception |
| SA-06 | Cases survolées : non explorées permises | C2 §4.1 ; D2 | 14 nov. 2026 | E15 (LOT-2F) : ouvert | C2 tranche | — | validé en conception |
| SA-07 | Révélation à la rencontre | P08, I01 (M) ; DS5.2 ; C2 §4.1 | 9 et 13 nov. 2026 | P08 ; I01 ; DS5.2 | concordant | — | validé en conception |
| SA-08 | Cible cachée percutée, avec bonus | J05, J07, J08 (M) ; C2 §4.1 | 9 nov. 2026 | J05, J07, J08 | concordant | — | validé en conception |
| SA-09 | Saut simple percutant : pas de bonus | C2 §4.1 ; D2 | 14 nov. 2026 | D08 (M) : bonus en collision volontaire | C2 précise | — | validé en conception |
| SA-10 | Arc continu ; portée Manhattan ; volumes | P07 (M) ; DS1.2 ; C2 §4.2 | 9 et 13 nov. 2026 | P07 : arc sans contournement, volume entier | concordant | — | validé en conception |
| SA-11 | Sol de départ ignoré | DS1.3 ; C2 §4.2 | 13 nov. 2026 | DS1.3 | concordant | — | validé en conception |
| SA-12 | Obstacle connu / inconnu | P08 (M) ; C2 §4.2 | 9 nov. 2026 | P08 | concordant | — | validé en conception |
| SA-13 | Vol sans correction ; réception stable | C2 §4.2 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| SA-14 | Arrêt au premier choc ; événements distincts | DS5.2 ; D13 (M) ; C2 §4.2 | 9 et 13 nov. 2026 | DS5.2 ; D13 | concordant | §11.2 X16 ; A30 | validé en conception |
| SA-15 | Impulsions verticale et horizontale par type | P02, P03 (M) ; C2 §4.3 ; D2 | 9 et 14 nov. 2026 | P02 : impulsion verticale constante pour une unité et une action | C2 précise | — | validé en conception, paramètre ouvert |
| SA-16 | Impulsion constante : v ∝ 1/M | DS2.1 ; C2 §4.3 ; D2 | 13 et 14 nov. 2026 | DS2.1 : plus lourd = moins haut et moins loin ; loi non choisie. G (E11) : même vitesse pour toutes les masses (écartée) | C2 tranche (quantité de mouvement) | §11.2 X2 | validé en conception, paramètre ouvert |
| SA-17 | Gravité ; plage par type | P01 (M) ; DS2.4 ; C2 §4.3 | 9, 13 et 14 nov. 2026 | DS2.4 : une plage de gravité | C2 précise (par type) | A11 | validé en conception, paramètre ouvert |
| SA-18 | Pas de saut à 0 g ; gravité négative invalide | DS2.4 ; C2 §4.3 | 13 et 14 nov. 2026 | DS2.4 : indisponible en apesanteur | concordant | — | validé en conception |
| SA-19 | Référence : 2 cases au même niveau ; sommet 0,75 m | P04, P05 (M) ; DS2.3 ; C2 §4.3 ; D2 ; C3 (A3A) | 9, 13 et 14 nov. 2026 | P05 et DS2.3 : 2 cases pour une descente d'un étage | C2 prévaut (remplace P05) ; C3 précise (mètres) | §11.1 point 2 ; X1 ; X13 | validé en conception, paramètre ouvert |
| SA-20 | Même niveau : vol plus court | C2 §4.3 | 14 nov. 2026 | — | nouveau (conséquence de SA-16 à SA-19) | — | validé en conception |
| SA-21 | Portée : arrondi vers le bas | P05 (M) ; DS2.2 ; C2 §4.3 | 9, 13 et 14 nov. 2026 | P05, DS2.2 : Manhattan ; E2 : conversion ouverte | C2 tranche | — | validé en conception |
| SA-22 | Distance 3D pour les TU | DS5.6 ; C2 §4.4 ; D2 | 13 et 14 nov. 2026 | DS5.6 : coût proportionnel à la distance de Manhattan | C2 précise (3D) | §11.1 point 7 | validé en conception |
| SA-23 | Coût du saut simple | C2 §4.4 ; D2 | 14 nov. 2026 | — | nouveau | A10 | validé en conception, paramètre ouvert |
| SA-24 | Coût de l'attaque sautée | J09 (M) ; DS5.6 ; C2 §4.4 | 9, 13 et 14 nov. 2026 | J09 : max(1, ⌊0,20 × TU_max⌋) en plus du déplacement | concordant | A10 | validé en conception, paramètre ouvert |
| SA-25 | C_saut propre aux sauts | C2 §4.4 ; D2 | 14 nov. 2026 | E13 (LOT-2F) : ouvert | C2 tranche le principe | — | validé en conception, paramètre ouvert |
| SA-26 | Paiement à l'engagement, sans remboursement | J09 (M) ; DS5.6 ; C2 §4.4 | 9 et 13 nov. 2026 | J09 ; DS5.6 (attaque sautée seulement) | C2 précise (étend au saut simple) | — | validé en conception |
| SA-27 | TU insuffisantes ; prévisualisation | J10, I02 (M) ; C2 §4.4 | 9 nov. 2026 | J10 ; I02 | concordant | — | validé en conception |

### 1.4 Chutes et réception

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| CH-01 | Saut volontaire sans surcharge, au même niveau ou d'un étage : pas de dégât de réception ; un étage compté sur 3 m entre les sols | DS3.1 ; C2 §5.1 ; D2 ; C3 (A3A, A4.2A, A4.3A, exception de surcharge, A25) | 13 et 14 nov. 2026 | DS3.1 : chute d'un étage sans surcharge, sans préciser « volontaire » ; C2 : « un étage » non défini, saut au même niveau non couvert, exemption perdue en cas de collision | C2 précise ; C3 précise | §11.1 point 1 ; X3, X4, X12, X16 ; A3, A4, A25 (réglées) ; A30 | validé en conception |
| CH-02 | Surcharge : dégâts possibles | DS3.1, DS3.2 ; C2 §5.1 ; C3 (exception de surcharge) | 13 et 14 nov. 2026 | DS3.1 | concordant ; C3 confirme | — | validé en conception |
| CH-03 | Chute involontaire : seuil de 3 m | D01 (M) ; C2 §5.1 ; D2 ; C3 (A4.1D, D3A) | 9 et 14 nov. 2026 | D01 et C2 : chute blessante possible dès un étage, même sans surcharge | C3 prévaut (remplace D01 et C2) | §11.1 point 1 ; X14 | validé en conception |
| CH-04 | Réception sur une unité = collision calculée à part | DS3.4 ; K01, K02 (M) ; C2 §5.1 ; C3 (A25) | 9, 13 et 14 nov. 2026 | DS3.1 : l'unité qui tombe d'un étage sans surcharge est exemptée ; DS3.4 : l'unité percutée peut être blessée « indépendamment de l'exemption qui concerne l'unité tombante » | C2 prévaut (restreint DS3.1 et DS3.4) ; C3 confirme | §11.2 X12, X16 ; A25 (réglée) ; A30 | validé en conception |
| CH-05 | Attaquant après esquive : saut volontaire, mesure entre les sols | E18 (P) ; DS3.1 ; C2 §5.1 ; C3 (A4.3A) | 9, 13 et 14 nov. 2026 | E18 : chute au sol, plafond 70 | concordant ; C3 précise | — | validé en conception |
| CH-06 | Chute après obstacle : involontaire | D13 (M) ; C2 §5.1 ; D2 | 9 et 14 nov. 2026 | D13 : chute verticale depuis le contact | C2 précise | §11.2 X16 ; A28, A30 | validé en conception |
| CH-07 | Courbe à recalibrer ; B(n) historique | D03, D04 (M) ; C2 §5.2 ; C3 (D1C) | 9 et 14 nov. 2026 | D03, D04 et C2 : courbe B(n) du LOT-2F (historique) | C3 prévaut (barème remplacé) | §11.2 X15 ; A29 | validé en conception, paramètre ouvert |
| CH-08 | Hauteurs en mètres ; trois grandeurs distinctes | C2 §5.2 ; D2 ; C3 (A3A, A4.3A, D1C) | 14 nov. 2026 | E12 (LOT-2F) : comptage ouvert ; DS3 : comptage non confirmé ; C2 : interpolation linéaire entre les points B(n) | C2 tranche (dégâts) ; C3 précise | §11.2 X16 ; A30 | validé en conception, paramètre ouvert |
| CH-09 | Seuil de 3 m inclus | C2 §5.2 ; D2 ; C3 (A4.1D, D1C, D3A) | 14 nov. 2026 | N7 (R) : seuil à décider ; C2 : 0,25 étage et interpolation jusqu'à 8 (historique) | C3 prévaut (remplace le seuil de C2) ; précise N7 | §11.1 point 1 ; X4 ; A4 (réglée) ; A29 | validé en conception |
| CH-10 | Gravité : au-delà du seuil seulement | C2 §5.2 ; D2 ; C3 (D3A) | 14 nov. 2026 | D03 : base selon le nombre d'étages, sans gravité ; C2 : g/g0 sur la puissance de référence | C2 prévaut (modifie D03) ; C3 précise | §11.2 X5 ; A5 | validé en conception, paramètre ouvert |
| CH-11 | Vitesse héritée dans H_eq ; montée non comptée pour les sauts de CH-01 | C2 §5.2 ; D2 ; C3 (D4A, A4.2A, A4.3A, exception de surcharge) | 14 nov. 2026 | C2 : seuil de 0,25 sur H_eq (historique) | nouveau ; C3 précise | §11.2 X3, X4, X16 ; A4 (réglée) ; A5, A29, A30 | validé en conception, paramètre ouvert |
| CH-12 | Sol horizontal : vitesse verticale seule | D11 (M) ; C2 §5.2 | 9 nov. 2026 | D11 | concordant | — | validé en conception |
| CH-13 | Plafond 70 ; surcharge hors de la puissance | D05 (M) ; C2 §5.2 ; D2 ; C3 (D2A) | 9 et 14 nov. 2026 | D05 : plafonds avant le tirage ; D09 : facteurs de poids après le tirage ; C2 : surcharge après le plafond, au-delà de 70 | C2 prévaut (déroge à D09) ; C3 prévaut (surcharge sur H_eq) | §11.2 X6, X15 ; A6, A29 | validé en conception, paramètre ouvert |
| CH-14 | Capacité de portage ; seuil de N14 | DS3.2 ; N14 (R) ; C2 §5.3 | 8 et 13 nov. 2026 | DS3.2 : même seuil que la réduction des TU | concordant | A13 | validé en conception, paramètre ouvert |
| CH-15 | Dépassement relatif S | C2 §5.3 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| CH-16 | F_surcharge sur la hauteur équivalente | C2 §5.3 ; D2 ; C3 (D2A) | 14 nov. 2026 | E24 (LOT-2F) : ouvert ; C2 : multiplicateur de la puissance | C2 tranche ; C3 prévaut (point d'application) | §11.2 X6, X15 ; A5, A29 | validé en conception, paramètre ouvert |
| CH-17 | Chute : surcharge non réappliquée à la puissance | N9, N10 (R) ; C2 §5.3 ; C3 (D2A) | 8 et 14 nov. 2026 | N9, N10 : le poids peut aggraver une chute ; C2 : la surcharge aggrave la puissance | C3 prévaut (chute) | A6 (collisions) | validé en conception |
| CH-18 | Surcharge : seuil maintenu, dégâts possibles dès 3 m | C2 §5.3 ; D2 ; C3 (exception de surcharge, D2A) | 14 nov. 2026 | C2 : seuil de 0,25 non supprimé par la surcharge (historique) | nouveau ; C3 prévaut (seuil) | §11.2 X16 ; A30 | validé en conception |
| CH-19 | Nature du sol sans effet | D02 (M) ; C2 §5.4 | 9 nov. 2026 | D02 | concordant | — | validé en conception |
| CH-20 | Support détruit : la chute continue | D12, D13 (M) ; C2 §5.4 | 9 et 14 nov. 2026 | D13 ; D12 | C2 précise | §11.2 X16 ; A30 | validé en conception |
| CH-21 | Traversée : perte d'énergie | C2 §5.4 ; D2 | 14 nov. 2026 | — | nouveau | A14 | validé en conception, paramètre ouvert |

### 1.5 Collisions et dégâts

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| CO-01 | Contacts sur volumes réels | DS1.2 ; C2 §6 | 13 et 14 nov. 2026 | DS1.2 | concordant | — | validé en conception |
| CO-02 | P = K × v_n² ; deux coefficients | DS4.2 ; D10 (M) ; C2 §6 ; D2 | 9, 13 et 14 nov. 2026 | DS4.2 : carré de la vitesse normale contre un obstacle | C2 prévaut (étend aux unités) | A7, A14 | validé en conception, paramètre ouvert |
| CO-03 | Facteur de masse entre unités | DS4.1 ; K08 (M) ; C2 §6 ; D2 ; C3 (A8A) | 9, 13 et 14 nov. 2026 | DS4.1 : la masse tend à protéger la plus lourde, sans décider seule | C2 tranche la formule ; C3 confirme le tirage commun | §11.1 point 8 ; A8 (réglée) | validé en conception |
| CO-04 | Décor : min(M/80, 3), plafond 70 | D10, D05 (M) ; C2 §6 | 9 nov. 2026 | D10 | concordant | A7 | validé en conception, paramètre ouvert |
| CO-05 | Type « impact » | DS4.4 ; D07 (LOT-2F, ouverte) ; C2 §6 | 13 nov. 2026 | DS4.4 | concordant | A21 | validé en conception, paramètre ouvert |
| CO-06 | Blessures et étourdissement séparés | K02 (M) ; C2 §6 ; D2 | 9 et 14 nov. 2026 | K02 : dégâts et étourdissement distincts | C2 précise | A21 | validé en conception, paramètre ouvert |
| CO-07 | Sensibilité à l'étourdissement | C2 §6 ; D2 | 14 nov. 2026 | — | nouveau | A16 | validé en conception, paramètre ouvert |
| CO-08 | Tirage commun par événement, confirmé | D06 (M) ; DS4.5 ; C2 §6 ; D2 ; C3 (A8A) | 9, 13 et 14 nov. 2026 | DS4.5 : même tirage pour l'unité et l'obstacle ; mandat v1.0 : ne pas étendre aux unités | C2 prévaut (étend aux unités) ; C3 confirme | §11.1 point 8 ; A8 (réglée) ; A26 | validé en conception, paramètre ouvert |
| CO-09 | Ordre de la chaîne de calcul ; chute : surcharge sur H_eq ; collisions : A6 | DS3.5 ; D09, D10 (M) ; C2 §6 ; C3 (D2A, D3A) | 9, 13 et 14 nov. 2026 | DS3.5 : deux arrondis ; D09 : poids et armure après le tirage ; C2 : bonus de surcharge sur la puissance | C2 prévaut (déroge à D09) ; C3 prévaut (surcharge d'une chute, gravité) | §11.2 X6 ; A5 à A7, A26 | validé en conception, paramètre ouvert |
| CO-10 | Bonus × 1,25 de l'attaque sautée | J08, J11, J12, D08 (M) ; C2 §6 | 9 nov. 2026 | J11 ; J12 | concordant | — | validé en conception |
| CO-11 | Contacts multiples d'un même choc | C2 §6 ; D2 | 14 nov. 2026 | — | nouveau | A23 | validé en conception, paramètre ouvert |

### 1.6 Esquives réactives

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| ES-01 | Tentative automatique, réussite probabiliste | K03, K05 (M) ; DS5.7 ; C2 §7.1 ; D2 | 9, 13 et 14 nov. 2026 | K03 : esquive « automatique » | D2 précise | — | validé en conception |
| ES-02 | Menace vue juste avant l'impact | K03 (M) ; DS5.7 ; C2 §7.1 | 9, 13 et 14 nov. 2026 | DS5.7 : la cible doit voir l'unité qui tombe (instant non précisé) | C2 précise | A15 | validé en conception, paramètre ouvert |
| ES-03 | Bonus de visibilité + 10 | C2 §7.1 ; D2 | 14 nov. 2026 | — | nouveau | A15 | validé en conception |
| ES-04 | + 5 points par étage | K05 (M) ; DS5.7 ; C2 §7.1 | 9 et 13 nov. 2026 | K05 : + 5 par niveau traversé, formulation provisoire (E12) | C2 tranche (formulation provisoire confirmée) | A16 | validé en conception, paramètre ouvert |
| ES-05 | Probabilité P | K05 (M) ; C2 §7.1 ; D2 | 9 et 14 nov. 2026 | K05 : clamp(Réactions + 5n, 0, 100) | C2 précise | A16 | validé en conception, paramètre ouvert |
| ES-06 | Tirage 1 à 100 | C2 §7.1 ; D2 | 14 nov. 2026 | — | nouveau | A16 | validé en conception, paramètre ouvert |
| ES-07 | Inconscient : pas d'esquive | C2 §7.1 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| ES-08 | Huit voisines du même niveau | DS5.7 ; C2 §7.2 | 13 nov. 2026 | DS5.7 | concordant | — | validé en conception |
| ES-09 | Coût de la marche, TU restantes | DS5.7 ; S2 (R) ; C2 §7.2 | 8 et 13 nov. 2026 | DS5.7 | concordant | — | validé en conception, paramètre ouvert |
| ES-10 | Débit seulement si réussite exécutée | K06, K07 (M) ; DS5.7 ; C2 §7.2 | 9 et 13 nov. 2026 | K06 ; K07 | concordant | — | validé en conception |
| ES-11 | Choix uniforme ; pas d'information cachée | K04 (M) ; C2 §7.2 ; D2 | 9 et 14 nov. 2026 | K04 : choix aléatoire ; E22 : loi ouverte | C2 tranche | — | validé en conception |
| ES-12 | Esquives en conflit | C2 §7.2 ; D2 | 14 nov. 2026 | — | nouveau | A17 | validé en conception, paramètre ouvert |
| ES-13 | Menaces simultanées : une tentative | C2 §7.2 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| ES-14 | Dangers successifs : nouvelle tentative | C2 §7.2 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |

### 1.7 Repoussement et retombées

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| RP-01 | Esquive réussie ≠ repoussement | K07 (M) ; DS5.3 ; C2 §8 ; D2 ; C3 (A27) | 9, 13 et 14 nov. 2026 | K07 : cible immobile ; DS5.3 : à vérifier | C2 tranche ; C3 confirme | §11.1 point 4 ; A27 (réglée) | validé en conception |
| RP-02 | Direction du repoussement ; vide admis | DS5.3 ; C2 §8 ; D2 | 13 et 14 nov. 2026 | DS5.3 : case voisine libre ; choix à définir | C2 précise | A18 (réglée) | validé en conception |
| RP-03 | Pas de repoussement en chaîne | S10 (R) ; C2 §8 | 8 et 14 nov. 2026 | S10 | concordant | — | validé en conception |
| RP-04 | Cible hors de combat repoussable | C2 §8 ; D2 | 14 nov. 2026 | Consolidation DS : devenir d'une cible hors de combat à définir | C2 tranche | — | validé en conception |
| RP-05 | Retombée de l'attaquant : case adjacente | DS5.4 ; C2 §8 ; D2 | 13 et 14 nov. 2026 | DS5.4 : « à proximité », rayon non décidé | C2 précise | — | validé en conception |
| RP-06 | Impossibilité connue ou révélée en vol | C2 §8 ; D2 | 14 nov. 2026 | — | nouveau | A19 | validé en conception, paramètre ouvert |
| RP-07 | Repoussement sans intention | C2 §8 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| RP-08 | Impacts simultanés : direction combinée | C2 §8 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| RP-09 | Attaquant sur la case de la cible repoussée | DS5.3 (C2 ne la redit pas) ; C3 (A18) | 13 et 14 nov. 2026 | DS5.3 : l'attaquant prend la case initiale de la cible | maintenue ; C3 confirme | §11.2 X8 ; A18 (réglée) | validé en conception |

### 1.8 Environnement et événements

| ID | Règle courante | Source primaire | Date | Formulation ancienne | Priorité | Conflit | Statut |
|---|---|---|---|---|---|---|---|
| EN-01 | Résistance cumulative | D12 (M) ; C2 §9 ; D2 | 9 et 14 nov. 2026 | D12 : règles de résistance du terrain d'OXCE (seuil, sans cumul) | C2 prévaut (modifie D12) | §11.1 point 5 ; A22 | validé en conception, paramètre ouvert |
| EN-02 | Blocage conservé tant que résistance > 0 | C2 §9 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| EN-03 | Destruction immédiate ; pas d'effondrement | D12 (M) ; C2 §9 | 9 et 14 nov. 2026 | D12 | C2 précise | — | validé en conception |
| EN-04 | Impacts simultanés : dégâts cumulés | C2 §9 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| EN-05 | Action offensive résolue jusqu'au bout | DS5.1 ; C2 §9 | 13 nov. 2026 | DS5.1 : monde figé pendant un saut | concordant | — | validé en conception |
| EN-06 | Chutes en file FIFO stable | DS5.1, DS5.2 ; I03 (M) ; C2 §9 ; D2 | 9, 13 et 14 nov. 2026 | I03, DS5.2 : résolution chronologique | C2 prévaut (file FIFO pour les chutes) | §11.1 point 3 ; A20 | validé en conception, paramètre ouvert |
| EN-07 | Réévaluation ; une chute en attente par unité | C2 §9 ; D2 | 14 nov. 2026 | — | nouveau | A20 | validé en conception |
| EN-08 | Corps qui tombent | C2 §9 ; D2 | 14 nov. 2026 | — | nouveau | A23 | validé en conception |
| EN-09 | Pas d'actions offensives simultanées | C2 §9 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |
| EN-10 | Graine ; ordre déterministe | C2 §9 ; D2 | 14 nov. 2026 | — | nouveau | — | validé en conception |

## 2. Écarts à l'historique : vérification du tableau de C2 (§10)

Chaque ligne du tableau des écarts de C2 est comparée aux textes d'origine.

| Référence (C2) | Ce que dit C2 de l'historique | Vérification sur les textes d'origine | Statut récent (C2) | Règles |
|---|---|---|---|---|
| `MEC-0001` | Marche et verticalité mêlées | Exact : le registre ne contient que `MEC-0001` ; le LOT-2H y proposait DS1 à DS5 (proposition non inscrite) | Séparation en `MEC-0002` | PE-01, PE-02 |
| N7 / H01 / E21 | Petite chute sans dégâts, puis « contradictoire » | Exact (registre N7 ; LOT-2F H01, E21) | Annoter N7, sans l'effacer | CH-01, CH-03, CH-09 |
| DS3.1 | Exemption d'un étage, sans préciser « volontaire » | Exact (consolidation DS, §4 item 1) | Exemption du seul saut volontaire | CH-01, CH-03 |
| P05 / DS2.3 | 2 cases pour une descente d'un étage | Exact (LOT-2F P05 ; DS2.3) | 2 cases au même niveau | SA-19 |
| P02 / E11 | Ambiguïté vitesse ou impulsion | Exact (LOT-2F E11 ; G E11) | Quantité de mouvement à effort égal | SA-15, SA-16 |
| K05 / DS5.7 | « Réactions + 5 par étage ; visibilité juste avant le choc » | **Inexact en partie** : DS5.7 dit « la cible doit voir l'unité qui tombe », sans préciser l'instant | + 10 si menace vue au départ ; vue juste avant l'impact nécessaire ; tirage 1 à 100 | ES-02 à ES-06 |
| K07 / DS5.3 | « Cible immobile » contre poussée après le choc | Exact (LOT-2F K07 ; DS5.3, avec la mention « à vérifier ») | Pas de déplacement d'esquive ; repoussement forcé possible | RP-01, RP-02 |
| D02 | Nature du sol sans effet | Exact | Gardé pour les dégâts corporels ; destruction et perte de vitesse distinctes | CH-19, CH-20, CH-21 |
| D12 / OXCE | Destruction par seuil, sans accumulation | Exact (LOT-2F §4, lecture du code) | Résistance cumulative | EN-01 |
| D13 | Collision puis chute depuis le contact | Exact | Chute consécutive involontaire | CH-06 |
| DS5.1 | « Chutes supposées simultanées » | **Inexact** : DS5.1 fige le monde, sauf esquives et chutes provoquées ; il ne dit pas que les chutes sont simultanées | Chutes en file FIFO stable | EN-06, EN-07 |
| DS5.5 | Exclusion des grandes unités des seules attaques sautées | Exact pour le sauteur ; DS5.5 les excluait aussi comme **cibles**, ce que C2 ne redit pas sans le modifier | Aucun saut volontaire ; chutes involontaires permises ; exclusion comme cible maintenue | GE-08, GE-09 |
| DS5.6 | « Coût de saut offensif + 20 % » | **Inexact** : le supplément vaut `max(1, ⌊0,20 × TU_max⌋)`, pas 20 % du coût | Saut simple sans supplément ; attaque avec ; distance 3D pour les TU | SA-22 à SA-24 |
| DS4.5 | Tirage commun entre unité et obstacle | Exact ; le mandat v1.0 (§2 B) demandait de ne pas l'étendre aux unités | Étendu aux collisions entre unités | CO-08 |

La colonne « Statut récent (C2) » décrit C2. Pour N7 et DS3.1, le correctif v1.2 modifie ce statut, comme pour D03, qui figure dans la liste des écarts non mentionnés ci-dessous : voir la liste des écarts v1.2.

**Écarts que le tableau de C2 ne mentionne pas** (consolidation, §11) :
- D03 devient dépendant de la gravité (CH-10) ; **v1.2** : au-delà du seuil de 3 m seulement (D3A) ;
- D09 plaçait les facteurs de poids après le tirage ; la surcharge, facteur lié au poids, vient avant (CH-13, CO-09 ; §11.2, X6) ; **v1.2** : elle majore désormais la hauteur équivalente (D2A) ;
- l'extension du tirage commun (CO-08) entre en conflit avec DS4.1 (§11.1, point 8) ; **v1.2** : écart assumé par le propriétaire (A8A) ;
- l'exemption d'un étage ne vaut plus en cas de collision avec une unité, ce qui restreint DS3.1 et DS3.4 (CH-01, CH-04 ; §11.2, X12) ; **v1.2** : confirmé (A25) : la collision est calculée à part ;
- N5 à N10 de `MEC-0001` changent de fiche de référence (§11.2, X10) ; **v1.2** : confirmé (A24) ;
- la part de DS5.3 où l'attaquant prend la case de la cible n'est plus redite ; elle est maintenue (RP-09 ; §11.2, X8) ; **v1.2** : confirmé (A18).

**Écarts introduits par le correctif v1.2** (C3 ; consolidation, §14) :
- le seuil de 0,25 étage de C2 et son interpolation sont remplacés par un seuil de **3 m inclus**, quelle que soit la gravité (CH-09) ;
- la courbe `B(n)` de D03 et D04, reprise par C2, devient historique ; la courbe est à recalibrer lors des tests, sans valeur fixée, et sans décalage d'un étage (CH-07) ;
- D01 et la règle de C2 selon laquelle une chute involontaire peut blesser dès un étage sont remplacés : une chute ordinaire d'un étage ne blesse plus (CH-03 ; §11.2, X14) ;
- pour une chute, le coefficient de surcharge passe de la puissance à la hauteur équivalente, sans double application (CH-16, CH-17) ; son effet dans les collisions reste ouvert (CO-09 ; A6) ;
- la hauteur d'étage est fixée à 3 m, alors que C2 (§3) ne fixait pas de mètres pour la grille (GE-02 ; §11.2, X13) ;
- un saut volontaire au même niveau sans surcharge, que C2 ne couvrait pas, ne blesse pas à la réception (A4.2A) ; pour un saut d'un étage vers le bas, avec ou sans surcharge, la hauteur comptée est l'écart de 3 m entre les sols, sans la montée, alors que C2 résolvait physiquement la montée et le sommet (A4.3A ; CH-01, CH-11 ; §11.2, X3, X4, X16).

## 3. Critères de tests futurs

**Aucun test n'est écrit ni exécuté.** Les valeurs notées « fictif » sont des valeurs d'essai, pas des valeurs de jeu.
- **Spécifiable** : l'attendu découle des règles validées en conception et de données fictives déclarées.
- **Partiel** : une partie de l'attendu dépend d'une ambiguïté A*n*.
- **Bloqué** : l'attendu exact dépend d'une ambiguïté A*n*.

| ID | Règles | Scénario | Attendu | Exécutabilité |
|---|---|---|---|---|
| T2-01 | CH-01, CH-11 | Sauts volontaires sans surcharge ni collision : au même niveau, à 1 g puis à une gravité plus faible dans la plage du type (sommet plus haut) ; d'un étage vers le bas, soit 3 m entre les sols | Aucun dégât de réception dans tous les cas ; la montée au sommet n'est pas comptée | Spécifiable |
| T2-02 | CH-03, CH-09, CH-10 | Chutes involontaires ordinaires de 2,99 m et de 3,00 m, sans surcharge, sans vitesse héritée et sans collision, à 1 g, 0,5 g et 2 g | 0 dégât de chute dans les six cas : le seuil de 3 m est inclus et ne dépend pas de la gravité. Hauteurs données directement, sans vitesse ; la tolérance d'une `H_eq` calculée relève d'A29 | Spécifiable |
| T2-03 | CH-01, CH-02, CH-16 à CH-18 | Chute de 3 m, puis saut volontaire d'un étage vers le bas, avec `S` = 1 (fictif, soit `F_surcharge` = 1,5) | Hauteur équivalente majorée, donc supérieure à 3 m : dégâts possibles, sans garantie de perte de santé après protections ; `F_surcharge` n'est pas réappliqué à la puissance | Partiel (A5 : combinaison ; A29 : courbe) |
| T2-04 | CH-15, CH-16 | `S` = 0 ; 0,5 ; 1 ; 3 | `F_surcharge` = 1 ; 1,25 ; 1,5 ; 2 | Spécifiable |
| T2-05 | CO-03 | Collision entre unités de 120 et 60 kg (fictif) | Facteurs 0,75 (la plus lourde) et √2 ≈ 1,414 (la plus légère) | Spécifiable (facteur) |
| T2-06 | CO-08 | Collision entre deux unités, graine fixée ; puis deux collisions distinctes | Même tirage pour les deux unités d'une collision, puis protections propres à chacune ; tirages distincts pour des collisions distinctes | Partiel (A26 : nature du tirage) |
| T2-07 | CO-03, CO-08 ; DS4.1 | Même collision répétée avec plusieurs graines, armures égales, masses différentes | Avec le tirage commun, et `P_i` la puissance de chaque unité arrondie juste avant le tirage (premier arrondi de CO-09), l'ordre des dégâts avant protections suit `P_i × F_i` pour toutes les graines : le tirage ne l'inverse jamais, et le second arrondi peut au plus créer une égalité ; à puissances arrondies égales avant tirage, la plus légère reçoit des dégâts supérieurs ou égaux. Le premier arrondi peut, lui, changer l'ordre des produits non arrondis | Spécifiable (ordre seulement) |
| T2-08 | CO-06, CO-07 | Unité de sensibilité 0 à l'étourdissement (fictif) percutée | Aucun étourdissement ; santé selon l'armure | Partiel (A21) |
| T2-09 | CO-10, SA-09 | Attaque sautée, saut simple et collision accidentelle sur un allié caché | Bonus × 1,25 pour la seule attaque sautée | Partiel (A14 : `K_unités`) |
| T2-10 | ES-03 à ES-06 | Unité non étourdie, Réactions 40 (fictif), 2 étages ; menace vue au départ, puis vue seulement avant le contact | P = 60, puis 50 ; réussite si `t ≤ P`, avec `t` tiré dans {1, …, 100} et une graine fixée | Spécifiable |
| T2-11 | ES-07 | Unité inconsciente sous un corps qui tombe ; unité consciente sous un cadavre qui tombe | Aucune esquive ; esquive possible | Spécifiable |
| T2-12 | ES-08 à ES-11 | Esquive sans TU suffisantes ; esquive réussie vers une case de coût fictif | Pas d'esquive, aucun débit ; débit du coût de la marche | Partiel (coûts de terrain : `MEC-0001`) |
| T2-13 | ES-12, ES-13 | Deux esquives en conflit ; deux menaces visibles simultanées | — | Bloqué (A17) |
| T2-14 | SA-22 à SA-26 | Saut simple de `Δx = 2`, `Δz = −1` ; attaque sautée de même géométrie, `TU_max` = 54 ; `C_saut` fictif ; la cible esquive | `3 × C_saut`, puis `3 × C_saut + 10`, payés en entier, sans remboursement | Partiel (A10 si coût non entier) |
| T2-15 | SA-19, SA-21 | Unité de référence à 1 g, même niveau, cases à distance 2 et 3 | 2 permis ; 3 refusé | Partiel (A9 : calibrage) |
| T2-16 | SA-16 | Unité plus lourde que la référence, mêmes capacités | Sommet plus bas (rapport `(M_ref/M)²`) et portée plus courte | Partiel (A2 : `M_ref`) |
| T2-17 | SA-18 | `g` = 0 ; puis `g` > 0 hors de la plage de saut ; puis `g` < 0 | Pas de saut ; chute involontaire encore possible ; gravité refusée | Partiel (A11 : plage) |
| T2-18 | GE-08 | Grande unité qui veut sauter ; grande unité dont le sol est détruit | Saut refusé ; chute involontaire | Spécifiable |
| T2-19 | CH-05 | La cible esquive une attaque sautée d'un étage, sans surcharge | L'attaquant retombe au sol ; sa réception est comptée sur 3 m entre les sols, reste volontaire et ne cause aucun dégât de réception | Spécifiable |
| T2-20 | SA-05, SA-06 | Saut au-dessus de cases jamais explorées ; destination jamais explorée | Permis ; refusé | Spécifiable |
| T2-21 | EN-01 à EN-04, CH-20, CH-21 | Obstacle destructible de résistance fictive, deux impacts successifs ; plancher détruit sous l'unité | Résistance réduite deux fois, destruction à 0 ; la chute continue avec une vitesse réduite, puis un deuxième impact est résolu à part | Partiel (A14, A22, A28 : résistances, énergie, vitesse résiduelle) |
| T2-22 | EN-06, EN-07 | Trois unités A, B, C perdent leur support dans un même événement ; la chute de B devient caduque | Traitement dans l'ordre stable ; B annulée ; une seule chute en attente par unité | Partiel (A20 : clé d'ordre) |
| T2-23 | RP-02, RP-03, RP-05, RP-06, RP-09 | Cible repoussée vers le vide ; cible sans case libre ; aucune case adjacente pour l'attaquant | Chute involontaire de la cible ; l'attaquant prend une case adjacente ; refus avant engagement si tout est connu | Partiel (A19) |
| T2-24 | SA-07, PE-01 | Prévisualisation avec obstacle ou unité cachés ; marche ordinaire après inscription | Aucune information révélée avant contact ; la marche de `MEC-0001` reste inchangée | Spécifiable |
| T2-25 | CH-01, CH-04 | Attaque sautée d'un étage, sans surcharge ; la cible n'esquive pas | Collision distincte : dégâts possibles pour les deux unités, même si la réception de l'attaquant est exemptée | Partiel (A14 : `K_unités`) |
| T2-26 | GE-09 | Attaque sautée visant une grande unité | Sélection refusée | Spécifiable |
| T2-27 | CH-11, CH-20, CH-21 | Chute de 3 m avec une vitesse descendante héritée fictive, par exemple après la traversée d'un plancher | `H_eq` supérieure à 3 m : dégâts possibles, sans garantie | Partiel (A5, A28 : combinaison et vitesse résiduelle ; A29 : courbe) |
| T2-28 | CH-07, CH-09, CH-10 | Chutes ordinaires de plus de 3 m, sans surcharge (fictif : 3,01 m et 6 m), à 1 g, 0,5 g et 2 g | Dégâts possibles ; valeurs à calibrer lors des tests ; la gravité module les dégâts sans déplacer le seuil | Bloqué (A29 : courbe ; A5 : gravité) |
| T2-29 | CH-01, CH-04, CH-08, CH-11, CH-20 | Saut volontaire de deux étages vers le bas ; saut au même niveau en surcharge ; saut exempté d'un étage dont le support de réception cède ; attaque sautée d'un étage, sans surcharge, qui heurte sa cible : fin de la descente de l'attaquant | — | Bloqué (A30) |

Décompte après le correctif v1.2 : 29 critères ; 12 spécifiables, 14 partiels, 3 bloqués. Avant (v1.1) : 26 critères ; 8 spécifiables, 16 partiels, 2 bloqués.

**Aucun critère ne transforme « dégâts possibles » en « dégâts garantis »** : au-dessus du seuil, ou en surcharge, l'attendu est une possibilité de dégâts, sans valeur ni perte de santé assurée après protections.

### 3.1 Critères modifiés par le correctif v1.2

Version v1.1 citée telle quelle (historique).

| ID | Version v1.1 (historique) | Raison du changement |
|---|---|---|
| T2-01 | CH-01, CH-03 — Saut volontaire d'un étage, sans surcharge ni obstacle ; puis chute involontaire d'un étage, de hauteur équivalente 1 — Saut : aucun dégât de chute. Chute : puissance 8 avant plafond (à 1 g), tirage dans [4, 12] — Partiel (A3 : définition d'« un étage ») | Seuil de 3 m et saut au même niveau (A3A, A4.1D, A4.2A, A4.3A) : la chute involontaire d'un étage ne blesse plus ; la base 8 est historique (D1C) |
| T2-02 | CH-09, CH-10 — Chutes involontaires de hauteur équivalente 0,25 ; 0,625 ; 1,5 étage, à 1 g ; puis 1,5 étage à 0,5 g et à 2 g — 0 ; 4 ; 11 ; puis 5,5 et 22 (avant plafond) — Partiel (A4, A5 : seuil et pondération) | Seuil de 0,25 et courbe `B(n)` historiques (A4.1D, D1C, D3A) |
| T2-03 | CH-13, CH-16 — Chute au sol à 1 g, de puissance de base supérieure à 70 ; surcharge `S` = 2 (fictif) — Plafond 70, puis × 2 : 140 avant arrondi et tirage — Spécifiable | La surcharge majore la hauteur équivalente, et non plus la puissance après le plafond (D2A) |
| T2-06 | CO-08 — Collision entre deux unités, graine fixée ; puis deux collisions distinctes — Même tirage pour les deux unités d'une collision ; tirages distincts pour des collisions distinctes — Partiel (A8 : tirage commun à confirmer ; A26) | Tirage commun confirmé (A8A) |
| T2-07 | CO-03, CO-08 ; DS4.1 — Même collision répétée, armures égales, masses différentes — Avec un tirage commun, l'ordre des blessures avant armure est fixe, déterminé par `P_i × F_i` ; à puissances avant tirage égales, la plus légère est toujours la plus blessée — Bloqué (A8 : contradiction à trancher) | Contradiction tranchée : tirage commun gardé (A8A) |
| T2-19 | CH-05 — La cible esquive une attaque sautée d'un étage, sans surcharge — L'attaquant retombe au sol sans dégâts de chute — Partiel (A3) | Mesure entre les sols (A4.3A) ; A3 réglée |
| T2-23 | RP-02, RP-03, RP-05, RP-06, RP-09 — Cible repoussée vers le vide ; cible sans case libre ; aucune case adjacente pour l'attaquant — Chute involontaire de la cible ; l'attaquant prend une case adjacente ; refus avant engagement si tout est connu — Partiel (A19 ; A18) | Maintien de RP-09 confirmé (A18) |
| T2-25 | CH-01, CH-04 — Attaque sautée d'un étage, sans surcharge ; la cible n'esquive pas — Collision : l'attaquant peut être blessé (plafond 60), contrairement à DS3.1 — Partiel (A25 : changement à confirmer ; A14 : `K_unités`) | Collision calculée à part, confirmée (A25) ; le plafond 60 n'est plus cité (X15) |
| T2-26 | GE-09 — Attaque sautée visant une grande unité — Sélection refusée — Partiel (A12 : maintien à confirmer) | Maintien de GE-09 confirmé (A12) |
| T2-27 à T2-29 | — (nouveaux) | Cas du mandat v1.2 (§2.3) : vitesse héritée, chute au-delà de 3 m ; sauts non couverts, saut exempté suivi d'une chute, réception de l'attaquant après un choc (A30) |

## 4. Effet sur la matrice du LOT-2F

La matrice du LOT-2F n'est pas modifiée. Les tests ci-dessous seraient à reprendre si `MEC-0002` était inscrite.

| Test LOT-2F | Effet | Règles |
|---|---|---|
| T-J02, T-J03, T-J04, T-J11 | À recalculer : la référence de 2 cases vaut désormais au même niveau, et une descente d'un étage porte plus loin | SA-19, SA-21 |
| T-J05 | Valable pour l'unité de référence seulement ; dépend de la masse. A3A donne une valeur métrique à `H` (E1, pour la hauteur seulement) : à 1 g, le sommet de l'unité de référence est à 0,75 m (SA-19). *(v1.1 : « Valable pour l'unité de référence seulement ; dépend de la masse ».)* | SA-16, SA-19, GE-02 |
| T-J15, T-J18, T-J19 | Coût total : `d_3D × C_saut` + supplément ; seuil complet | SA-22 à SA-27 |
| T-J17 | Inchangé (supplément offensif) | SA-24 |
| T-K02, T-K06 | Formule changée : + 10 si menace vue au départ ; tirage dans {1, …, 100} | ES-03 à ES-06 |
| T-K03 | L'attaquant qui retombe après une esquive, d'un étage et sans surcharge, ne subit plus de dégâts ; réception comptée sur 3 m entre les sols. *(v1.1 : « L'attaquant qui retombe après une esquive, d'un étage et sans surcharge, ne subit plus de dégâts ».)* | CH-05 |
| T-K04 | Tirage commun aux deux unités ; repoussement possible de la cible après l'impact ; tous deux confirmés (A8A, A27). *(v1.1 : « Tirage commun aux deux unités ; repoussement possible de la cible après l'impact », règles CO-08, RP-01 ; A8.)* | CO-08, RP-01 |
| T-D01 | Remplacé : ni le saut volontaire d'un étage, ni la chute involontaire ordinaire d'un étage (3 m) ne blessent, le seuil de 3 m étant inclus ; la base 8 est historique. *(v1.1 : « À séparer : saut volontaire d'un étage (aucun dégât) ; chute involontaire (puissance 8) ».)* | CH-01, CH-03, CH-09 |
| T-D02 | Valeurs historiques : la courbe `B(n)` n'est plus un barème ; elle n'est pas décalée d'un étage ; nouvelles valeurs à calibrer lors des tests. *(v1.1, avec T-D04 : « Valeurs inchangées ; interpolation entre les points ».)* | CH-07, CH-08 ; A29 |
| T-D04 | Bornes du tirage inchangées pour une puissance fictive ; la puissance 8 n'est plus celle d'une chute d'un étage | CO-08, CH-07 ; A26 |
| T-D03 | Plafonds à revoir : ses valeurs `B(6)` à `B(8)` sont historiques ; la surcharge majore la hauteur équivalente et n'agit plus après le plafond ; la valeur des plafonds, gardée comme limite validée, pourrait être recalibrée selon la portée de D1C (A29). *(v1.1 : « Sens des plafonds à revoir (surcharge après le plafond au sol) ».)* | CH-13, CH-16, CH-17 ; A6, A29 |
| T-D05, T-D06, T-D07 | La base d'une collision entre unités devient `K_unités × v_n²`, et non `B(n)` | CO-02 |
| T-D09 | Place de `min(M/80, 3)` à fixer | CO-04 ; A7 |
| T-D10 | Remplacé : résistance cumulative | EN-01 |
| T-D12 | La chute après l'obstacle est involontaire | CH-06 |
| T-D14 | Remplacé : avec le tirage commun confirmé (A8A), l'ordre des dégâts avant protections suit `P_i × F_i`, avec `P_i` arrondie juste avant le tirage ; à puissances égales, la plus légère reçoit des dégâts supérieurs ou égaux ; seules les protections départagent ensuite. *(v1.1 : « Avec un tirage commun, l'ordre des blessures avant armure est fixe ; à puissances égales, la plus légère est toujours la plus blessée », règle A8.)* | CO-03, CO-08 |
| T-X02, T-X03, T-X04, T-X05 | En partie tranchés : premier contact (SA-14), chute jusqu'au support (SA-01), grandes unités (GE-08), apesanteur (SA-18) | — |
| T-X01 | Destination devenue occupée en vol : toujours non tranché ; RP-06 couvre seulement l'impossibilité révélée en vol | RP-06 |
