# BASTION — MEC-0001 — Consolidation Q1–Q4 pour revue indépendante

**Version de travail :** 0.2 — 19 novembre 2026  
**Statut :** dossier transmis pour *revue*, non inscription et non implémentation  
**MEC-0001 :** **reportée** ; aucun gameplay autorisé.  
**MEC-0002 :** décisions partielles seulement ; non acceptée globalement.  
**Branche de référence signalée par Claude Code :** `main` à `818c646` (à vérifier par le relecteur).  
**Restrictions :** lecture seule ; aucun code, test d'implémentation, commit, push, branche, PR ou modification documentaire.

## 0. Provenance et limites documentaires — LIRE AVANT TOUTE REVUE

Ce fichier est une **reconstruction documentaire par l'orchestrateur**, pas un enregistrement brut ou signé de la conversation entière. Il ne doit **pas** être utilisé comme preuve indépendante de ses propres décisions.

- **P4 / preuve directe incluse :** les validations Q4 des messages de l'utilisateur sont retranscrites textuellement au §12. Leurs formulations complètes d'options sont résumées dans les sections ci-dessous ; il convient de les comparer aux formulations du dialogue d'origine si celles-ci sont disponibles.
- **P1–P3 / provenance partielle :** les résumés Q1, Q2 et Q3 figurant ici proviennent de la consolidation de l'orchestrateur dans la conversation, **sans verbatim complet des validations d'origine dans cette pièce**. Pour une vérification de la preuve d'acceptation, les marquer « provenance non vérifiée » jusqu'à réception des échanges ou exports originaux.
- **H / sources du dépôt :** S1–S12, Z1, N1–N14, ARB-A–E, G1–G4, ainsi que PE, GE, ES et EN de MEC-0002 doivent être vérifiées **sur le dépôt**. Les règles historiques ne constituent pas une validation automatique de Q1–Q4.
- **D / déductions et critères :** les exemples de calcul et les scénarios Txx sont des **conséquences à vérifier**, pas des résultats de tests exécutés.
- Les textes présentés dans ce dossier comme « validés » désignent une validation dans la **conversation** et non une inscription dans GitHub.
- Toute incohérence, omission ou valeur non vérifiée doit être rapportée. **Ne rien rectifier tacitement.**

## 1. Périmètre et règles de priorité

MEC-0001 couvre marche ordinaire, recherche et exécution du chemin, coûts TU/énergie, visibilité du trajet, portes explicites, connexions spéciales de niveaux et leur transit. MEC-0002 fait autorité pour les sauts, chutes, collisions, esquives, repoussements et effets des impacts. Les effets de suppression de support passent immédiatement à MEC-0002. Cette séparation est à vérifier contre PE-01 à PE-03 de MEC-0002.

Règles d'antériorité : S5 (déplacement partiel en cas d'insuffisance) est supplantée par Z1 pour la sélection normale ; S4/N2 permissifs sont restreints par ARB-A/G1 et géométrie Q1 ; S10 comporte les exceptions ARB-B/G2 ; N5–N10 sont historiques pour les effets de chute ; ARB-E est étendue aux connexions par Q4.13. MEC-0002 garde son ordre spécialisé pour les chutes (EN-06/EN-07) sur le départage général Q3.5.

## 2. Q1 — Géométrie (reconstruction ; verbatim des validations NON joint)

- Repère : x vers l'est, y vers le sud, z vers le haut ; origine nord-ouest, indices de cases à partir de zéro. Centres horizontaux : `(i + 0,5) × L`, `(j + 0,5) × L` ; L = côté de case.
- Unités physiques de géométrie : mm entiers ; côté L configurable, initialement **1 500 mm**, nécessairement pair. Conversion des valeurs externes vers demi-entiers : arrondir la moitié en s'éloignant de zéro. Les données géométriques et tous leurs arrondis doivent être contrôlés.
- Références d'étage : **3 000 mm fixes entre sols de référence d'étages tactiques consécutifs**, rectification Q4.1 de la liberté initiale Q1.4 ; variations de hauteur locales des supports conservées. Les étages et les dénivelés locaux ne sont pas interchangeables.
- Profil humain initial : debout **600 × 600 × 1 800 mm**, agenouillé **600 × 600 × 1 200 mm**, couché **1 200 × 600 × 500 mm** ; orientations sur huit directions. AABB après rotation diagonale : arrondi vers l'extérieur au prochain entier pair. Pour couché à 45°, AABB horizontale initiale attendue **1 274 × 1 274 mm** (à recalculer).
- Mur type : **100 mm** d'épaisseur centré sur la séparation de cases, **±50 mm**.
- Support : pieds de l'unité sur un support physiquement uniforme et valide pour son volume horizontal ; unité stable au centre de case à l'arrivée.
- Ressaut pour humain **debout** : montée maximale **200 mm**, descente maximale **300 mm**. Au-delà, la marche ordinaire est refusée ; pas de chute ou saut automatique. Les seuils des autres postures ne sont pas décidés.
- Trajet physique d'un pas : montée d'abord verticale puis translation ; descente d'abord horizontale puis abaissement ; volume balayé vérifié. L'intérieur d'une unité consciente et des obstacles solides est bloquant ; tangent géométrique non bloquant pour marche mais contact détectable (précisé Q4.2).
- Diagonale : contrôle topologique N2 puis viabilité physique de l'un des itinéraires orthogonaux autour du coin. Si les deux sont valides, priorité au parcours X puis Y. Cela reste **un seul pas diagonal facturé une fois**. Un cheminement ne peut exploiter des cases jamais explorées.
- Corps morts ou inconscients : traversables **uniquement au titre de la marche** (ARB-B), sans suppression de leur volume physique pour MEC-0002.
- Réveil simultané : unités traitées par identifiant croissant, voisins dans l'ordre N, NE, E, SE, S, SW, W, NW, sans nouvelles tentatives en boucle après résolution ; voir Q4.19.
- Événements spatiaux : ordre du trajet physique et position exacte des rencontres doivent être représentés ; Q4.3 définit la perte de support immédiate.

## 3. Q2 — Connexions et passages (reconstruction ; verbatim NON joint)

- Escaliers : connexion explicite entre centres stables, avec admission physiquement vérifiée.
- Rampes : connexion spécifique transitoire ; ne présument pas une station debout permanente sur une pente.
- Échelles : points d'entrée et de sortie explicites ; pas de modification implicite de z lors de la marche ordinaire ; admissibilité des postures et volumes.
- Ascenseurs : plateforme physique à états, niveaux desservis ; les connexions disponibles dépendent de son état. **Aucune téléportation.**
- Les coûts universels par type de connexion ne sont **pas** décidés : coût **par instance** explicite (Q3.10).
- Les murs restent des barrières de cases avec épaisseur propre ; une porte fermée exige une action d'ouverture indépendante.
- Les connexions ne doivent pas faire passer des unités à travers un volume physiquement interdit ni exploiter d'informations cachées.

## 4. Q3 — Coûts, surcharge et événements (reconstruction ; verbatim NON joint)

### 4.1 Barème initial de marche

| Terrain | Orthogonal | Diagonal |
|---|---:|---:|
| Normal | 4 TU + 2 énergie | 6 TU + 3 énergie |
| Difficile (×1,5) | 6 TU + 3 énergie | 9 TU + 5 énergie |
| Très difficile (×2) | 8 TU + 4 énergie | 12 TU + 6 énergie |

Règle d'arrondis acceptée dans le résumé Q3 : multiplier séparément TU et énergie de base par le coefficient de terrain, arrondir **vers le haut** chaque ressource, puis appliquer pour le pas diagonal ×1,5, arrondir TU **vers le bas** et énergie **vers le haut**. Contrôler la cohérence, notamment le passage « difficile diagonal » 9 TU/5 énergie. Pas de coût universel de traversée de mur ; mur plein bloque, porte exige une action distincte.

### 4.2 Exécution et événements

- Chaque pas de marche ordinaire vérifie TU **et** énergie disponibles, un pas à la fois (G3).
- Pas refusé **avant engagement** : aucun débit. Pas déjà engagé : débit conservé ; un pas accompli n'est pas remboursé. Les réactions réelles tirées interrompent la marche (ARB-E) ; des événements spécifiques peuvent interrompre la connexion (Q4.13).
- Priorité aux règles spécialisées d'événement, puis identifiants stables croissants et revalidation après chaque événement. EN-06/EN-07 conservent leur FIFO spécifique pour les chutes ; voir Q4.4.
- Ressources maximales et récupération configurables ; récupération énergie distincte, limitée au maximum. Valeurs de base précisées par Q4.6.
- Recherche lexicographique des chemins : TU minimales, puis énergie minimales, puis départage déterministe ; détails Q4.16.

### 4.3 Surcharge

Charge portée = masse des **armures + équipement + inventaire**, distincte de la masse physique totale avec le corps. Capacité kg strictement positive, issue d'une correspondance Force→kg commune à MEC-0001/MEC-0002 (Q4.5). Avec charge `W` :

```text
F = 1                         si W = 0
F = min(1, capacité_kg / W)   si W > 0
TU_après = floor(min(TU_restantes + TU_récupérées, TU_max) × F)
```

La surcharge ne majore pas le coût de chaque pas, n'introduit pas de seuil supplémentaire d'immobilisation et n'est pas appliquée à l'énergie. Les autres modificateurs de TU restent hors décision.

## 5. Q4.1–Q4.4 — Géométrie / événements (validés en conversation)

- **Q4.1=A** : 3 m fixes entre sols de référence des étages tactiques consécutifs, avec possibilité de dénivelés locaux. Cohérent avec GE-02 et CH-08.
- **Q4.2=A** : un contact de surfaces est détectable ; le seul contact ne bloque pas la marche, contrairement au chevauchement intérieur interdit. Les impacts et dégâts restent sous MEC-0002.
- **Q4.3=A** : destruction de support pendant un déplacement engagé = effet **immédiat**, interruption à la position physique courante et relais MEC-0002 ; pas engagé conservé en débit, pas non commencé non facturé. Pas de retour ou téléportation de convenance.
- **Q4.4=A** : chutes issues d'un même événement ordonnées de façon stable, **FIFO** par identifiant croissant ; chutes secondaires ajoutées en queue, revalidation EN-07 ; Q3.5 ne renverse pas les priorités spéciales. Ne pas confondre ordre de file et chronologie physique de plusieurs événements réellement distincts.

## 6. Q4.5–Q4.9 — Configurations et transferts (validés en conversation)

- **Q4.5=A** : correspondance Force→kg **configurable par type**, unique pour les deux mécaniques, capacités positives. **Aucune** formule Force×10 universelle acceptée. Valeurs encore ouvertes.
- **Q4.6=A** : profil initial de test **60 TU maximales**, **60 TU récupérées par tour**, **100 énergie maximale**, **20 énergie récupérée par tour**. Réduction de surcharge sur TU après récupération plafonnée, selon ARB-D et Q3.14. Pas des constantes universelles pour toutes les unités.
- **Q4.7=A** : ouverture d'une porte ordinaire manuelle action **explicite** initialement **4 TU / 0 énergie**, ouverture distincte sans pas automatique ensuite. Les portes particulières ont des règles propres.
- **Q4.8=A** : connexion avec **occupation physique** et capacité ; admission, collision et sortie vérifiées. Coûts TU/énergie par connexion, sans double débit des segments. Le rythme ne nécessite pas d'animation universelle. Aucun transfert par téléportation.
- **Q4.9=A** : interruption du transfert = conserver position/état physique atteints, sans arrivée automatiquement complétée. Perte de support vers Q4.3 et MEC-0002.

## 7. Q4.10–Q4.15 — Suspension, reprise, réaction, incapacité, partage (validés en conversation)

- **Q4.10=A** : transit interrompu et soutenu = **état suspendu** conservant position, orientation et association à la connexion ; reprise possible ; support perdu → MEC-0002. Cet état ne vaut pas une station tactique ordinaire.
- **Q4.11=A** : transfert = coût TU/énergie **intégral payé à l'engagement** ; vérification avant débit ; aucun remboursement en cas d'interruption ; pas de refacturation des segments engagés d'un même transfert ; une action nouvelle a un coût nouveau. Ne modifie pas le coût par pas de marche.
- **Q4.12=A** : reprise du **même transfert dans le même sens** sans nouveau paiement après vérification des conditions ; retour vers l'entrée = **nouvelle action**, coût propre, sans remboursement de l'action initiale.
- **Q4.13=A** : tir de réaction **effectivement tiré** contre une unité en transfert interrompt aussi l'action, même sans touche. Coût et position conservés ; les conséquences d'une éventuelle touche sont distinctes. Étend ARB-E seulement pour le périmètre de l'interruption, sans inventer les conditions générales d'Overwatch.
- **Q4.14=A** : incapacité interrompt l'action, puis contrôle de la validité du **support physique**. Maintien en place si soutenu ; sinon chute sous MEC-0002. Aucune chute automatique indépendante du support.
- **Q4.15=A** : chaque connexion définit sa **capacité** ; plusieurs utilisateurs possibles si capacité et volumes sans chevauchement intérieur interdit, accès et sortie physiquement valides.

## 8. Q4.16–Q4.21 — Départage, orientation, posture, réveil, découverte, imprévus (validés en conversation)

- **Q4.16=A** : après coûts TU puis énergie, départage lexicographique déterministe des séquences de directions **N, NE, E, SE, S, SW, W, NW** ; connexions spéciales départagées par identifiant stable ; si deux cheminements physiques sont possibles pour une diagonale, règle **X d'abord** Q1. Le calcul ne doit pas exploiter d'information cachée.
- **Q4.17=A** : unité orientée vers le pas engagé, sans supplément de TU ou d'énergie pour cette orientation automatique ; **volume balayé de la rotation** et mouvement contrôlé. Les rotations autonomes constituent un autre sujet.
- **Q4.18=A** : se coucher, s'agenouiller, se relever = **actions distinctes**, soumises à des coûts configurables et à la validité physique ; aucun changement automatique de posture provoqué par la recherche ou l'exécution d'une marche.
- **Q4.19=A** : réveil sur case occupée applique G2. Chercher la **première** case adjacente admissible dans l'ordre N, NE, E, SE, S, SW, W, NW, au **même niveau**, avec support, volume admissible et sans chevauchement intérieur interdit avec une unité consciente. Un corps inerte n'interdit pas le repositionnement ordinaire. Sinon réveil **sur place, couché**, sans relèvement implicite ni nouvelle recherche automatique. Les règles de collision pour esquive/repoussement restent MEC-0002.
- **Q4.20=A** : la seule **révélation** d'une unité cachée, sans obstacle au trajet ni tir de réaction effectivement déclenché, **n'interrompt pas** la marche. Si elle bloque réellement, S8–S11 déterminent l'interruption ; aucune révélation anticipée sans cause.
- **Q4.21=A** : prochain pas devenu non exécutable (coût réel supérieur, occupation ou obstacle inattendu) : arrêt **sans débiter ce pas non commencé**, actualisation de la connaissance et de la zone atteignable ; **pas de recalcul/reprise automatique** vers l'ancienne destination. Le joueur choisit une nouvelle commande.

## 9. Matrice de traçabilité destinée au relecteur

| Groupe | Source historique à contrôler | Validations conversationnelles | Vérification attendue |
|---|---|---|---|
| Grille, axes, étages | N1, N3, GE-01–GE-03, CH-08 | Q1, Q4.1 | 3 000 mm entre étages ; dénivelé local distinct |
| Collision de marche | S3–S4, S10, ARB-A/B, G1, GE-05 | Q1, Q2, Q4.2, Q4.17 | blocage par chevauchement interdit ; contact tangent toléré pour marche |
| Passages diagonaux | S1–S3, N2, G1 | Q1, Q3, Q4.16 | passage orthogonal physiquement praticable ; une seule charge diagonale |
| Terrain et TU | S2, Z1, G3 | Q3, Q4.6 | arrondis et montants ; éligibilité TU + énergie |
| Optimisation | G4, S6–S9 | Q3, Q4.16 | priorité TU puis énergie, départage stable |
| Surcharge | N11–N14, ARB-D, GE-07, CH-14 | Q3.14, Q4.5 | même capacité Force→kg ; effet distinct sur chutes |
| Portes | ARB-C | Q3, Q4.7 | action distincte 4 TU / 0 énergie en profil de test |
| Connexions | N4, ARB-C, PE-03 | Q2, Q3.10, Q4.8–Q4.15 | admission, occupation physique, paiement, suspension, reprise |
| Réaction | ARB-E | Q3.4, Q4.13 | tir réellement effectué interrompt marche/transfert |
| Perte de support | EN-03, EN-06, EN-07 | Q4.3–Q4.4, Q4.14 | effet immédiat ; chute FIFO après perte, états réévalués |
| Réveil | G2, ARB-B | Q1, Q4.19 | choix voisin déterministe ; état couché si bloqué |
| Visibilité | S6–S12, Z1 | Q4.20–Q4.21 | découverte ne bloque que pour motif défini ; pas de fuite d'information |
| Esquive | ES-08–ES-12, G3 | Q3 et interfaces Q4 | aucune extension d'énergie implicite à ES-09/ES-10 |

## 10. Scénarios futurs (NON EXÉCUTÉS)

| ID | Situation | Attente documentaire, à vérifier |
|---|---|---|
| T01 | Orthogonal normal | 4 TU et 2 énergie |
| T02 | Diagonale difficile, passage praticable | 9 TU et 5 énergie |
| T03 | Diagonale topologiquement permise mais volume bloqué | refus sans débit du pas non engagé |
| T04 | Ressaut humain debout +200 mm / descente −300 mm | admissible si volumes et support valides ; au-delà marche refusée |
| T05 | Deux itinéraires admissibles de mêmes TU et énergie | même chemin déterministe |
| T06 | Porte ordinaire fermée | action distincte 4 TU/0 énergie ; pas de marche automatique |
| T07 | Ennemi caché révélé hors trajet et sans tir | marche poursuivie si autre événement ne l'interrompt pas |
| T08 | Obstacle inconnu rencontré | arrêt, révélation, prochain pas non commencé non débité |
| T09 | Corps inconscient au sol | traversable pour marche, reste physique pour MEC-0002 |
| T10 | Réveil dans une case occupée | voisin admissible déterministe, sinon réveil sur place couché |
| T11 | Tir de réaction manqué pendant marche ou transfert | ordre interrompu ; coût du pas engagé ou du transfert conservé |
| T12 | Connexion payée et interrompue | état exact conservé ; reprise du même transfert non refacturée |
| T13 | Revenir dans une connexion suspendue | nouvelle action et nouveau coût |
| T14 | Plateforme soutenant une unité inconsciente | support conservé : pas de chute automatique |
| T15 | Support détruit pendant une marche engagée | relais immédiat à MEC-0002, sans téléportation |
| T16 | Plusieurs chutes du même événement | FIFO stable, réévaluation EN-07 |
| T17 | Esquive MEC-0002 | TU de marche applicable, pas d'énergie ajoutée par G3 |

## 11. Réserves et limites à qualifier lors de la revue

### Nécessaires à la spécification exécutable complète

- **RF-01** : profils complets des connexions effectivement utilisées : géométrie, support pendant transit et en cas d'inconscience, accès, sortie, capacité, état de l'ascenseur, coûts par instance.
- **RF-02** : coût, conditions et géométrie des changements de posture et rotations autonomes ; aucune transformation implicite des règles de marche.
- **RF-03** : table Force→kg, données physiques des unités et ressources particulières nécessaires aux scénarios, sans fixer de faux paramètres universels.
- **RF-04** : gestion déterministe des cas limites de coûts (coût nul, non entier, invalide, cycle), arrondi et départage, sans modifier silencieusement G4.
- **RF-05** : conditions aux interfaces de MEC-0002 (chutes physiques, esquives, réactions, enchaînements d'événements). Ne pas confondre cette réserve avec une obligation de terminer toute MEC-0002 avant une consolidation documentaire de MEC-0001.

### Hors périmètre ou explicitement reportables

Équilibrage des autres unités, textes/UI précis, animations, système Overwatch détaillé, dégâts de chute et collisions complètes, tolérance numérique GE-05 non déjà décidée, stabilité des bâtiments hors événements EN, valeurs des objets ou type d'armure non employés dans les scénarios.

### Points de vigilance supplémentaires

- **P1** : coût minimal autorisé (notamment zéro) et validité du calcul de chemin ; aucune valeur inventée.
- **P2** : trajectoire balayée d'une rotation sans pénétration physique ; définition mathématique manquante si elle influence un cas de test.
- **P3** : correspondance entre « pas engagé », « pas achevé » et interruption à un instant intermédiaire ; séparation des cas Q4.3 et ARB-E.
- **P4** : Q4.19 autorise le corps inerte pour une relocalisation ordinaire, mais cela ne doit pas déroger par accident aux exclusions physiques MEC-0002.
- **P5** : Q4.12 retour comme nouvelle action ne définit pas automatiquement le chemin et coût du retour partiel : profil de connexion requis.

## 12. Verbatim des validations utilisateur Q4 accessibles dans le dialogue

> « Pour Bastion MEC-0001, audit Q4, je valide Q4.1=A concernant la hauteur des étages et Q4.2=A concernant les contacts physiques. Poursuis l'audit transversal avec vérification des règles OpenXcomCE, Kowlting et MEC-0002, identifie les autres contradictions réelles puis prépare la matrice de traçabilité, sans implémentation ni modification de dépôt. »

> « Pour Bastion MEC-0001, audit Q4, je valide Q4.3=A concernant la perte de support pendant un déplacement et Q4.4=A concernant l'ordre des chutes et événements simultanés. Vérifie la cohérence avec EN-03, EN-06, EN-07, ARB-E et Q3.5, puis poursuis Q4 avec les paramètres opérationnels encore indispensables, sans implémentation ni modification de dépôt. »

> « Pour Bastion MEC-0001, audit Q4, je valide Q4.5=A (capacité de portage), Q4.6=A (ressources), Q4.7=A (portes), Q4.8=A (occupation des connexions), Q4.9=A (interruptions de transit). Vérifie leur cohérence avec ARB-C, ARB-D, ARB-E, G3, Q3, Q4.3, MEC-0002 et la simplicité du système. Identifie ensuite uniquement les arbitrages qui bloquent encore la consolidation, sans implémentation ni modification du dépôt. »

> « Pour Bastion MEC-0001, audit Q4, je valide Q4.10=A pour les interruptions au milieu d'une connexion et Q4.11=A pour son paiement. Vérifie leur cohérence avec Q4.3, Q4.8, Q4.9, ARB-C, ARB-E, G3 et MEC-0002. Puis établis le bilan des seules réserves encore bloquantes avant la consolidation documentaire, sans implémentation ni modification du dépôt. »

> « Pour Bastion MEC-0001, audit Q4-A, je valide Q4.12=A (reprise/retour), Q4.13=A (tir de réaction en transfert), Q4.14=A (incapacité et support), Q4.15=A (occupation des connexions). Vérifie la cohérence avec les décisions précédentes, ARB-C, ARB-E, G3 et MEC-0002 ; termine Q4-A ou signale seulement les contradictions réellement bloquantes, puis poursuis vers Q4-B sans implémentation ni modification de dépôt. »

> « Pour Bastion MEC-0001, audit Q4-B, je valide Q4.16=A (départage des chemins), Q4.17=A (orientation), Q4.18=A (postures), Q4.19=A (réveil), Q4.20=A (révélation), Q4.21=A (imprévu). Vérifie leur cohérence avec S2, S6-S11, G1-G4, Q1-Q4-A et MEC-0002. Établis ensuite le bilan final des réserves, la matrice de traçabilité et le statut de MEC-0001, sans implémentation ni modification de dépôt. »

**Important :** ces validations confirment les **identifiants et options A**. Leur signification exacte doit être vérifiée contre les propositions correspondantes de la conversation, dont les formulaires détaillés ne sont pas reproduits mot pour mot ici. Le présent document est donc une source de *texte à auditer*, et non une preuve indépendante de formulation intégrale.

## 13. Rapport de relecture attendu

1. Verdict : conforme / conforme sous réserves / non conforme.
2. Anomalies : gravité, texte contesté, source opposable, correction documentaire proposée, sans correction effectuée.
3. Matrice de traçabilité avec une colonne « preuve confirmée / preuve insuffisante / non vérifiable ».
4. Provenance non vérifiée, explicitement, en particulier validations Q1–Q3 non jointes en verbatim.
5. Seules questions nécessitant une décision du propriétaire, sans proposer des arbitrages déjà validés comme s'ils étaient ouverts.

**Interdit de modifier le dépôt ou de mettre en œuvre la mécanique.**
