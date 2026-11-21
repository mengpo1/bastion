# Pièces transmises par le propriétaire le 19 novembre 2026 — Q1 à Q3

Copie, par Claude Code, des deux messages du propriétaire qui contiennent les propositions et validations d'origine de Q1, Q2 et Q3. Le texte est reproduit tel que reçu dans la conversation, sans correction. Ces messages ne sont ni archivés dans le dépôt ni dotés d'une empreinte. L'ordre ci-dessous est celui de leur réception.

---

## Message 1 (reçu en premier) — Q1.5 à Q1.9, Q2.1 à Q2.6, Q3.1 à Q3.14

## **&#x20;Paramètres numériques initiaux**

**Q1.5 — Largeur initiale des cases**

**A — 1 000 mm** : grille compacte, espace de circulation plus contraint.

**B — 1 500 mm (recommandé)** : compromis initial pour les personnages et les obstacles.

**C — 2 000 mm** : cases plus spacieuses, grande échelle physique.

**Q1.6 — Profil initial d'une unité humaine standard**



Largeur × profondeur × hauteur, en millimètres. Ce sont des volumes de collision proposés, pas des dimensions anatomiques exactes.

**A — Profil indicatif (recommandé)** : debout 600 × 600 × 1 800 ; agenouillé 600 × 600 × 1 200 ; couché 1 200 × 600 × 500, orienté selon le corps.

**B — Profil plus compact** : debout 500 × 500 × 1 700 ; agenouillé 500 × 500 × 1 100 ; couché 1 000 × 500 × 400.

**C — Aucun profil humain chiffré pour l'instant** : valeurs à fixer après essais de géométrie.

**Q1.7 — Épaisseur initiale d'un mur standard**

**A — 100 mm (recommandé)** : mur standard relativement fin.

**B — 200 mm** : mur standard plus épais.

**C — Aucune épaisseur standard** : valeur obligatoire pour chaque type de mur.

**Q1.8 — Écart initial entre les références de deux niveaux**

**A — 3 000 mm (recommandé)** : hauteur de référence initiale entre étages.

**B — 4 000 mm** : hauteur initiale plus importante.

**C — Pas de valeur par défaut** : chaque niveau doit définir explicitement son altitude.

**Q1.9 — Seuils initiaux des ressauts pour un humain debout**

**A — Montée 200 mm, descente 300 mm (recommandé)** : valeurs initiales distinctes.

**B — Montée 300 mm, descente 400 mm** : franchissement plus permissif.

**C — Valeurs à déterminer par essais** : conserver les seuils configurables sans valeur numérique définitive.

Ces choix fixent uniquement les valeurs initiales de référence. Les autres types d'unités, postures, murs et cartes pourront utiliser des paramètres différents. Les profils seront soumis ensuite à des scénarios de cohérence géométrique, sans implémentation.

Valider les paramètres et vérifier Q1

Après cet arbitrage, la vérification portera notamment sur la compatibilité entre les volumes couchés, les diagonales, les passages étroits et les supports physiques. Les résultats permettront de distinguer les valeurs simplement configurables de celles nécessitant un ajustement.



**MEC-0001 reste en qualification.** Aucun fichier, test ou code n'a été modifié.



Pour Bastion MEC-0001, lot Q1 Géométrie, je valide les paramètres initiaux suivants : Q1.5 largeur de case=1500 mm ; Q1.6 profil humain=A ; Q1.7 mur standard=100 ; Q1.8 écart de référence des niveaux=3000 ; Q1.9 seuils de ressaut=A. Vérifie ensemble leur cohérence avec les décisions antérieures et les sources OpenXcomCE/Kowlting, puis termine Q1 sans implémentation.



**Q2.1 — Escaliers**

**A — Connexions explicites entre positions stables (recommandé).** Chaque escalier relie des positions et niveaux définis ; le trajet physique doit rester praticable, sans modifier implicitement le niveau tactique.

**B — Escaliers traités comme une succession de ressauts ordinaires.** Le niveau peut évoluer en suivant les marches, ce qui nécessiterait une exception à ARB-C.

**Q2.2 — Rampes et sols inclinés**

**A — Passages spéciaux entre supports horizontaux (recommandé).** Une rampe est un trajet de connexion défini ; ses extrémités sont des positions stables horizontales. Les collisions du trajet sont contrôlées.

**B — Supports inclinés permanents.** Une unité peut occuper une position stable inclinée, ce qui exige de compléter les règles de support et d'ancrage.

**Q2.3 — Échelles**

**A — Action spécifique avec connexion définie (recommandé).** Accès réservé aux unités compatibles, points d'entrée et de sortie explicites et volume de passage contrôlé. Aucun déplacement vertical ordinaire implicite.

**B — Déplacement vertical ordinaire.** L'échelle fonctionne comme une extension de la grille de marche.

**Q2.4 — Ascenseurs**

**A — Plateforme à états explicites (recommandé).** L'ascenseur possède un niveau courant et des connexions d'accès disponibles seulement lorsque les conditions de son état le permettent.

**B — Téléportation entre étages desservis.** Une interaction transfère directement l'unité entre deux positions, sans représenter les états physiques de la plateforme.

**Deux conventions géométriques reportées de Q1**

**Q2.5 — Positionnement des murs**

**A — Mur centré sur la frontière commune (recommandé).** Son épaisseur se répartit de part et d'autre ; un mur de 100 mm occupe 50 mm dans chaque case.

**B — Mur intégralement dans une des deux cases.** Nécessite une convention d'attribution de côté pour chaque mur.

**Q2.6 — Arrondi des volumes AABB orientés**

**A — Multiple pair supérieur (recommandé).** L'enveloppe calculée est agrandie au plus petit nombre pair de millimètres qui la contient intégralement.

**B — Multiple pair le plus proche.** La dimension pourrait être légèrement inférieure à l'enveloppe théorique.



Pour Bastion MEC-0001, lot Q2, je valide Q2.1=A (escaliers), Q2.2=A (rampes), Q2.3=A (échelles), Q2.4=A (ascenseurs), Q2.5=A (ancrage murs), Q2.6=A (arrondi AABB). Vérifie ensemble leur cohérence avec Q1, G1, ARB-C et MEC-0002, et termine le lot Q2 ou identifie uniquement les arbitrages réellement bloquants, sans implémentation.



**Q3.1 — Coûts des terrains**

**A — Barème par type de terrain (recommandé).** Chaque terrain définit un coût d'entrée en TU et en énergie. Les règles existantes déterminent ensuite les coûts des pas diagonaux.

**B — Coût universel.** Tous les terrains possèdent les mêmes coûts de base ; seules les actions spéciales peuvent les modifier.

**Q3.2 — Énergie des déplacements diagonaux**

**A — Multiplicateur configurable indépendant (recommandé).** L'énergie d'une diagonale possède son propre facteur. Le multiplicateur TU de S2 reste inchangé.

**B — Même coût énergétique qu'un pas orthogonal.** Seules les TU bénéficient du traitement diagonal de S2.

**C — Même multiplicateur que les TU.** L'énergie suit également le facteur 1,5, avec un arrondi à définir.

**Q3.3 — Coûts des connexions spéciales**

**A — Coût défini par connexion (recommandé).** Escaliers, rampes, échelles et ascenseurs possèdent des coûts TU/énergie configurables. Aucun double débit automatique des segments géométriques.

**B — Coût calculé selon la distance et le dénivelé.** Une formule commune détermine toutes les dépenses.

**Q3.4 — Obstacle inconnu et coût devenu imprévu**

**A — Vérifier avant chaque pas et interrompre si nécessaire (recommandé).** Le pas non commencé n'est pas débité. Les pas déjà accomplis conservent leurs coûts. Les découvertes actualisent la connaissance conformément à S8–S11.

**B — Autoriser un débit partiel pour un pas refusé.** Un coût peut être engagé même si l'unité n'a pas effectué le pas.

**Q3.5 — Événements simultanés sur le trajet**

**A — Priorités spécifiques puis identifiant stable (recommandé).** Les règles déjà décidées ont priorité. En cas d'égalité restante, les événements sont départagés par leur identifiant unique croissant. Leur applicabilité est réévaluée après chaque résolution.

**B — Ordre de détection.** La résolution suit l'ordre dans lequel le moteur a trouvé les événements.

**Q3.6 — Plafond et récupération d'énergie**

**A — Réserve plafonnée et récupération configurable (recommandé).** L'énergie possède un maximum et une règle de récupération distincts de ceux des TU. Les valeurs seront fixées séparément.

**B — Réserve entièrement restaurée à chaque tour.** L'énergie revient systématiquement à son maximum au début du tour, sans récupération partielle.

**Portée de cette validation**



Ces six décisions ne fixeront pas encore les barèmes chiffrés de TU et d'énergie. Elles ne modifieront pas S2, G4, ARB-E ni les règles de MEC-0002 concernant les esquives, sauts et chutes.



Les coûts des portes et des interactions distinctes resteront à distinguer des coûts de marche afin d'éviter toute facturation implicite.



Pour Bastion MEC-0001, lot Q3 Ressources et événements, je valide Q3.1=A, Q3.2=A, Q3.3=A, Q3.4=A, Q3.5=A, Q3.6=A. Vérifie leur cohérence avec S2, Z1, G3, G4, ARB-E, Q1, Q2 et MEC-0002. Regroupe ensuite les seuls barèmes et arbitrages restants, sans implémentation.





**Q3.7 — Coût initial du pas orthogonal sur terrain normal**

**A — 4 TU et 2 énergie (recommandé).** Une diagonale coûte alors 6 TU, selon S2.

**B — 6 TU et 3 énergie.** Échelle de coûts plus élevée.

**C — Pas de valeur chiffrée définitive.** Valeur de référence à établir par tests.

**Q3.8 — Différences entre types de terrains**

**A — Trois catégories initiales (recommandé)** : normal = coût de base ; difficile = +50 % de TU et d'énergie ; très difficile = +100 %, avec arrondi entier à définir.

**B — Terrain normal uniquement au départ.** Le système accepte d'autres terrains configurables, mais aucun autre barème n'est encore fixé.

**Q3.9 — Énergie d'une diagonale**

**A — Facteur initial 1,5 avec arrondi supérieur (recommandé).** Un coût énergétique de 3 devient 5 en diagonale.

**B — Facteur initial 1,5 avec arrondi inférieur.** Un coût énergétique de 3 devient 4 en diagonale.

**C — Facteur à régler ultérieurement.** Conserver uniquement le principe du multiplicateur indépendant.

**Q3.10 — Barèmes des connexions spéciales**

**A — Profil chiffré initial.** Rampe et escalier : 6 TU / 3 énergie ; échelle : 8 TU / 4 énergie ; transfert d'ascenseur : 2 TU / 0 énergie. Coûts de commande de l'ascenseur non inclus.

**B — Coûts obligatoirement définis par connexion (recommandé).** Aucun barème universel pour l'instant ; des valeurs de test seront définies pour chaque scénario.

**Q3.11 — Réserve énergétique initiale**

**A — Maximum 100 ; récupération 20 par tour.** Profil initial configurable, sans dépendance aux valeurs de TU.

**B — Valeurs à déterminer après calibration (recommandé).** La réserve et sa récupération restent configurables, sans valeurs définitives avant les essais de rythme de jeu.

**Q3.12 — Coût supplémentaire des murs et des passages**

**A — Aucun surcoût universel lié au mur (recommandé).** Un mur infranchissable bloque ; un passage ouvert est traité selon les coûts du terrain ou de sa connexion. L'ouverture d'une porte est une action distincte.

**B — Surcoût configurable par type de passage.** Le franchissement d'un passage peut ajouter un coût spécifique au coût d'entrée sur le terrain.



Pour Bastion MEC-0001, lot Q3, je valide Q3.7=A, Q3.8=A, Q3.9=A, Q3.10=B, Q3.11=B, Q3.12=A. Vérifie la cohérence numérique et les éventuels paramètres encore bloquants de Q3, notamment les interactions avec S2, G3, ARB-D et MEC-0002. Termine Q3 si possible, sans implémentation.





**Q3.13 — Ordre des multiplicateurs et des arrondis**

**A — Arrondir le terrain, puis la diagonale (recommandé)**



Le coût de base est multiplié par le facteur de terrain, puis arrondi à l'entier supérieur pour chaque ressource.



Ensuite, la diagonale applique ses propres règles : TU ×1,5 arrondi inférieur (S2) ; énergie ×1,5 arrondi supérieur (Q3.9).



Chaque coût final est entier et calculé une seule fois avant le pas.

**B — Combiner tous les facteurs, puis arrondir à la fin**



Les multiplicateurs de terrain et de diagonale sont appliqués à la valeur initiale avant un arrondi final selon la ressource.



Le résultat peut différer de l'option A pour des paramètres personnalisés.

**Q3.14 — Formule de surcharge ARB-D**

**A — Rapport capacité/charge plafonné à 1 (recommandé)**



La capacité de portage est une donnée exprimée en kg, déterminée par la Force selon une conversion configurable.



Le facteur de surcharge est `min(1, capacité / charge)`, avec facteur 1 lorsque la charge est nulle.



Ce facteur s'applique au total de TU déjà récupérées et plafonnées, conformément à ARB-D. Le résultat est arrondi à l'entier inférieur.

**B — Facteur configurable par tranches de charge**



Le rapport charge/capacité sélectionne une tranche configurée associée à un facteur de réduction des TU.



Cette option nécessite un barème supplémentaire.

**C — Différer la formule de surcharge**



ARB-D conserve son ordre de calcul validé, mais sa formule et ses valeurs restent explicitement ouvertes pour l'audit final.

**Exemple de l'option A pour Q3.14**



Exemple fictif, non un paramètre de jeu validé : capacité 30 kg, charge 40 kg, total de TU récupérées et plafonnées à 60.

\\[ 60 \times \min(1,\frac{30}{40})=45\ \text{TU} \\]

Ce calcul illustre la réduction sur le total plafonné, et non uniquement sur les TU récupérées pendant le tour.



La conversion Force → kg et les autres pénalités resteraient à calibrer. L'option A fixe la formule générale, pas leurs valeurs.



Pour Bastion MEC-0001, lot Q3, je valide Q3.13=A concernant les arrondis et Q3.14=A concernant la formule de surcharge ARB-D. Vérifie leur cohérence, identifie les seules réserves restantes et établis le bilan final de Q3 avant l'audit Q4, sans implémentation.

---

## Message 2 (reçu ensuite) — Q1.1 à Q1.4

Pour Bastion MEC-0001, voici les quatre dernières propositions et validations originales manquantes : Q1.1 à Q1.4.
Q1.1 — Largeur des cases : option A.
Largeur uniforme par carte, configurable et paire en millimètres.
Q1.2 — Dimensions physiques des unités : option A.
Dimensions configurables par type d'unité et posture. Le volume peut dépasser sa case ; les collisions restent obligatoires.
Q1.3 — Épaisseur physique des murs : option A.
Épaisseur configurable par type de mur ; les murs possèdent un volume physique défini.
Q1.4 — Hauteur de référence des niveaux : option A.
Altitude configurable pour chaque niveau ; les étages pouvaient initialement être séparés par des hauteurs différentes.
Ma validation originale était :
« Pour Bastion MEC-0001, lot Q1 Géométrie, je valide Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A. Poursuis le lot Q1 en regroupant les paramètres numériques restants, avec comparaison vérifiée d'OpenXcomCE et de Kowlting, sans implémentation. »
Les propositions intégrales et validations Q1.5–Q1.9, Q2.1–Q2.6 et Q3.1–Q3.14 ont déjà été transmises.
