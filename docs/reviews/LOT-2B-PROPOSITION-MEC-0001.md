# LOT-2B — Proposition pour `MEC-0001` : déplacement élémentaire à pied

| | |
|---|---|
| Mandat | `docs/mandates/BASTION-MANDAT-LOT-2B-v1.0.md`, branche `orchestration/mandats`, commit `4b08e7d9706e9e18b775db170173b39b716f1bca`. Lu sur GitHub avec l'outil GitHub de la session, ni recopié ni archivé. |
| Autorisation | Propriétaire, 8 novembre 2026. |
| Branche | `design/lot-2b-mec-0001-proposition`, créée depuis `origin/main` = `e3dfd41ab43dcc17f1cbf79afce1fe0828a0821f` (base attendue par le mandat, revérifiée après `git fetch origin main`). |
| Source | `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md` (fusionné dans `main`). Aucune nouvelle lecture du code OXCE n'a été nécessaire. |
| Nature | **Proposition. Rien n'est décidé.** Aucune fiche `MEC-0001` n'est créée, aucun registre n'est modifié, aucun gameplay n'est implémenté. |

## 0. En bref

**Périmètre proposé**, à arbitrer :
- une unité à pied de taille 1 se déplace de case en case, sur une carte plane à un seul niveau, vers une case choisie ;
- chaque case est franchissable ou bloquée et porte un coût d'entrée en unités de temps (TU) propre à Bastion ;
- une case occupée par une autre unité est infranchissable ;
- le chemin retenu est le moins coûteux ;
- chaque pas est payé en TU avant d'être fait ;
- une destination invalide ou inaccessible ne coûte rien.

**Trois questions prioritaires** sont soumises au propriétaire (§3) ; les autres décisions nécessaires sont listées au §5 :
1. le coût d'un pas en diagonale ;
2. le passage en diagonale le long d'un obstacle ;
3. ce qui se passe quand les TU ne suffisent pas.

Dans ce document :
- **option proposée** = suggestion du rapport, à accepter, modifier ou refuser ;
- **décision acceptée** = choix explicite, daté et prouvé du propriétaire. **Il n'y en a aucune ici.**

## 1. Périmètre proposé

Chaque point renvoie, entre crochets, au choix correspondant du LOT-2A (son §5, repris au §2 ci-dessous).

1. **Carte** : rectangle de cases repérées par deux entiers (x, y), à un seul niveau ; hors carte = invalide. [P1]
2. **Unité** : à pied, occupant une seule case.
3. **Voisinage** : 8 cases voisines ; la numérotation des directions est un détail interne, à documenter. [P2]
4. **Cases** : franchissable ou bloquée ; coût d'entrée en TU, entier ≥ 1, fixé par Bastion. [P4, P5, P6]
5. **Coût d'un pas** : coût d'entrée de la case d'arrivée. Diagonale : question 1 [P3] ; diagonale le long d'un obstacle : question 2 [P7].
6. **Occupation** : la case d'une autre unité ne peut être ni traversée ni choisie comme destination ; toutes les unités sont connues. [P12]
7. **Chemin** : coût total minimal ; en cas d'égalité, une règle de départage fixe, encore à définir. [P8]
8. **Paiement** : les TU sont dépensées pas à pas, avant chaque pas. TU insuffisantes : question 3. [P9]
9. **Ordre impossible** (hors carte, case bloquée ou occupée, destination inaccessible) : aucun déplacement, aucune TU dépensée. Le message éventuel relève de l'interface, dont le report est proposé. [P14]
10. **Mode de déplacement** : la marche seule, comme le proposait le LOT-2A (§2 ligne 7) ; course, pas de côté et marche furtive restent hors périmètre.

Aucune mécanique absente du LOT-2A n'est ajoutée. Restent aussi hors périmètre, comme le proposait le LOT-2A (§6) : niveaux et escaliers, vol, grandes unités, portes, réserve de TU, agenouillement, visibilité, tir de réaction, IA, animation. L'origine des TU de l'unité (capital initial, récupération à chaque tour) n'est pas couverte : le déplacement ne fait que les consommer (§5).

## 2. Les 14 choix du LOT-2A, regroupés

Tous les statuts sont **non décidé**. La colonne « Référence OXCE » résume le LOT-2A (§2 et §5), issu d'une lecture du code, sans exécution.

| # | Sujet | Référence OXCE (LOT-2A) | Groupe : option proposée ou report | Statut | Raison courte |
|---|---|---|---|---|---|
| P1 | Niveaux | Grille 3D, escaliers, chutes | Simplification : un seul niveau | Non décidé | Suffit au déplacement élémentaire |
| P2 | Directions | 0 = nord, sens horaire | Simplification : 8 directions, convention interne documentée | Non décidé | Sans effet visible en jeu |
| P3 | Coût de la diagonale | × 1,5, tronqué | **Structurant : question 1** | Non décidé | Change les trajets et les distances parcourues |
| P4 | Modèle de coût | Sol + objet, murs franchis, + 1 en montée, plafond 100 | Simplification : un coût d'entrée unique par case | Non décidé | Pas de murs ni d'objets distincts dans ce périmètre |
| P5 | Valeurs de coût | Données de terrain, non relevées | Simplification : valeurs propres à Bastion | Non décidé | Un relevé des valeurs d'origine est incompatible avec D4 en l'état |
| P6 | Obstacles | Murs minces et objets | Simplification : case franchissable ou bloquée | Non décidé | Plus simple ; murs minces reportés |
| P7 | Diagonale le long d'un obstacle | Dépend du type de mur ou d'objet ; une unité voisine ne gêne pas | **Structurant : question 2** | Non décidé | La règle d'OXCE ne se transpose pas au modèle simplifié de P6 |
| P8 | Calcul du chemin | Ligne droite, sinon recherche du chemin le moins coûteux (algorithme A*) ; coût minimal non garanti | Simplification : coût minimal garanti, départage fixe à définir | Non décidé | Résultat prévisible et testable |
| P9 | TU insuffisantes | Déplacement partiel jusqu'au dernier pas payable | **Structurant : question 3** | Non décidé | Change ce que le joueur obtient d'un ordre |
| P10 | Orientation, rotation | Rotation gratuite en marchant, et par défaut avant le 1er pas | **Reporté** | Non décidé | Sans effet sur les TU dans ce périmètre |
| P11 | Énergie | Marche = moitié du coût en TU ; arrêt si elle manque | **Reporté** | Non décidé | Aucune énergie dans ce périmètre |
| P12 | Unités non vues | Découvertes en marchant | Simplification : toutes les unités connues | Non décidé | La visibilité est reportée |
| P13 | Interruptions | Repérage, tir de réaction, annulation | **Reporté** | Non décidé | Dépendent de la visibilité, du tir et de l'interface |
| P14 | Ordre impossible | Aucun mouvement ni message trouvé | Simplification : aucun mouvement, aucune TU dépensée ; message reporté | Non décidé | Le message relève de l'interface |

**Interface** (aperçu du trajet, confirmation, messages, sélection d'une unité par clic) : **report proposé**.

Dans ce tableau, « reporté » signifie toujours « report proposé, non décidé ».

**Les reports sont-ils cohérents ?**
- **P10, orientation.** Dans OXCE, tourner ne coûte rien en marchant ni, par défaut, avant le premier pas. Seule exception : une unité repérée pendant la rotation initiale, ce qui suppose la visibilité, hors périmètre. L'ignorer ne change donc aucun coût dans ce périmètre. L'orientation comptera avec la vision et le tir de réaction, reportés eux aussi.
- **P11, énergie.** Sans énergie, une unité ne s'arrête jamais faute d'énergie, alors qu'OXCE le prévoit. Le report est cohérent tant que Bastion n'a pas d'énergie. Quand elle arrivera, la règle d'arrêt de la question 3 devra être étendue.
- **P13, interruptions.** Elles supposent la visibilité, le tir de réaction et une interface, tous absents du périmètre. P12 (toutes les unités connues) va dans le même sens.
- **Interface.** La simulation ne dépend pas de Godot (`CLAUDE.md` §7). Les règles du déplacement peuvent être fixées sans l'interface.
- **Dépendance à signaler : P7 dépend de P6.** OXCE distingue murs minces, « grands murs » et objets ordinaires. Avec des cases simplement bloquées, ces distinctions disparaissent : la règle d'OXCE ne peut pas être reproduite telle quelle, et un choix explicite est nécessaire (question 2).

## 3. Trois questions prioritaires

Les exemples utilisent des **coûts fictifs**, indiqués à chaque fois. Ils ne viennent ni d'OXCE ni de X-COM.

Notation des grilles :
- `.` case franchissable, `#` case bloquée ;
- `U` l'unité, `D` la destination ;
- x croît vers la droite, y vers le bas.

### Question 1 — Combien coûte un pas en diagonale ? (P3)

**OXCE** (LOT-2A, §2 ligne 4) : le coût du pas est multiplié par 1,5, puis tronqué à l'entier inférieur.

| Option | Règle | Conséquence en jeu |
|---|---|---|
| A | Comme OXCE : × 1,5, arrondi à l'inférieur | Les diagonales coûtent plus cher. Avec de petits coûts, l'arrondi compte : une case à 1 TU donne une diagonale à 1 TU. |
| B | Même coût qu'un pas droit | Avancer en diagonale est un raccourci : on couvre plus de terrain pour le même prix. |
| C | × 1,5, arrondi au supérieur | Comme A, mais la diagonale coûte toujours plus qu'un pas droit (1 → 2 ; 3 → 5). Avec des cases à 1 TU, une diagonale coûte autant que deux pas droits : les égalités entre chemins sont plus fréquentes, et la règle de départage (P8) compte davantage. |

Coût d'un pas en diagonale selon le coût fictif `c` de la case d'arrivée :

| `c` (fictif) | A | B | C |
|---|---|---|---|
| 1 | 1 | 1 | 2 |
| 2 | 3 | 2 | 3 |
| 3 | 4 | 3 | 5 |
| 4 | 6 | 4 | 6 |

**Exemple 1** : de `U` (0, 0) à `D` (2, 2), toutes les cases à 3 TU (fictif).

```
U . .
. . .
. . D
```

| Trajet | A | B | C |
|---|---|---|---|
| 2 pas en diagonale | 8 TU | 6 TU | 10 TU |
| 4 pas droits | 12 TU | 12 TU | 12 TU |

Dans les trois options, le chemin le moins coûteux passe en diagonale. Seul son prix change.

### Question 2 — Peut-on passer en diagonale le long d'une case bloquée ? (P7)

**OXCE** (LOT-2A, §2 ligne 3) : la diagonale est refusée par certains murs, et par certains objets « grand mur » (plein, ou diagonal en travers du pas) dans une case voisine. Un objet infranchissable ordinaire ou une unité voisine ne l'empêche pas.

**Ces options supposent la simplification P6 acceptée** (obstacles = cases bloquées). Avec de simples cases bloquées, les distinctions d'OXCE disparaissent. Si P6 est refusée (murs minces et objets distincts), reproduire la règle d'OXCE redevient une option.

| Option | Règle | Conséquence en jeu |
|---|---|---|
| A | Interdite si **au moins une** des deux cases voisines du pas est bloquée | Pas de « coupe d'angle » : contourner un coin coûte un pas de plus. |
| B | Interdite seulement si **les deux** cases voisines sont bloquées. *Option ajoutée par ce rapport, sans équivalent dans OXCE.* | On frôle un coin, mais on ne passe pas entre deux obstacles en diagonale. |
| C | Toujours permise | Seules la case de départ et la case d'arrivée comptent ; on peut passer « entre » deux obstacles. |

**Rapprochement avec OXCE** (inférence tirée du LOT-2A, §2 ligne 3, non observée) : une seule case voisine portant un « grand mur » plein suffit à refuser la diagonale. Une case bloquée assimilée à un « grand mur » plein donnerait donc l'option A ; assimilée à un objet ordinaire, l'option C.

**Sous-question** : une case voisine **occupée par une unité** compte-t-elle comme bloquée pour cette règle ? Dans OXCE, non.

**Exemple 2** : toutes les cases franchissables à 2 TU (fictif). Pour la diagonale, l'option A de la question 1 est prise à titre d'illustration : 3 TU.

```
Cas 1            Cas 2
# D              # D
U .              U #
```

| Cas | A | B | C |
|---|---|---|---|
| Cas 1 : un coin bloqué | Diagonale refusée : 2 pas droits par (1, 1), 4 TU | Diagonale permise : 3 TU | Diagonale permise : 3 TU |
| Cas 2 : deux coins bloqués | Refusée : pas de chemin sur cette petite grille | Refusée : pas de chemin | Permise : 3 TU |

### Question 3 — Que se passe-t-il si les TU ne suffisent pas pour tout le trajet ? (P9)

**OXCE** (LOT-2A, §2 ligne 9) : le chemin est calculé sans regarder les TU. L'unité avance pas à pas et s'arrête dès que le pas suivant coûte plus que ses TU restantes. Les pas faits restent payés, et un message s'affiche.

| Option | Règle | Conséquence en jeu |
|---|---|---|
| A | Comme OXCE : déplacement partiel jusqu'au dernier pas payable | L'ordre est toujours suivi au mieux ; l'unité peut s'arrêter en chemin, loin de la destination choisie. |
| B | Refus de l'ordre entier si le trajet coûte plus que les TU disponibles ; rien n'est dépensé | Le joueur doit choisir une destination atteignable. |

Telles qu'elles sont formulées, les deux options permettent un pas dont le coût **égale exactement** les TU restantes. C'est aussi le cas dans OXCE, où l'unité ne s'arrête que si le coût **dépasse** ses TU.

Le LOT-2A citait une troisième voie : ne permettre de choisir que des cases atteignables. Côté règles, elle revient à l'option B ; la différence relève de l'interface, reportée.

**Exemple 3** : `D` est à 5 cases à l'est de `U` ; chaque case coûte 2 TU (fictif). L'unité dispose de 7 TU ; le trajet complet coûte 10 TU.

```
U . . . . D
```

| Option | Résultat |
|---|---|
| A | 3 pas faits (6 TU), arrêt sur la 3e case, 1 TU restante |
| B | Ordre refusé, l'unité ne bouge pas, 7 TU restantes |

## 4. Critères de tests futurs

Aucun test ni code n'est écrit dans ce lot. Les tests de la future fiche devraient au moins vérifier les points suivants, avec des coûts fictifs déclarés comme tels.

1. **Déterminisme** : même carte, même état et même ordre donnent le même chemin et le même coût.
2. **Pas droit** : il coûte le coût d'entrée de la case d'arrivée.
3. **Diagonale** : coût conforme à la question 1, pour des coûts de case pairs, impairs et égaux à 1.
4. **Coins** : les deux cas de l'exemple 2, conformes à la question 2, plus un cas où une case voisine porte une unité (sous-question).
5. **Obstacles et occupation** : une case bloquée ou occupée n'est jamais traversée ni acceptée comme destination.
6. **Hors carte et destination inaccessible** : ordre refusé, TU inchangées.
7. **Coût minimal** : sur une carte où un détour coûte moins que la ligne droite, le détour est choisi.
8. **Égalité** : quand plusieurs chemins ont le même coût, la règle de départage fixée donne le chemin attendu.
9. **TU insuffisantes** : l'exemple 3, conforme à la question 3 (arrêt et TU restantes exactes, ou refus et TU inchangées), plus le cas limite où le dernier pas coûte exactement les TU restantes (pas permis).
10. **Paiement** : les TU dépensées égalent la somme des pas réellement faits.

Ces tests vérifieraient les règles de Bastion. Comme OXCE n'a pas été exécuté, aucun ne pourrait prouver une fidélité observée à OXCE.

## 5. Inconnues et décisions encore nécessaires

Avant une fiche `MEC-0001` complète, il manque :

1. **Les réponses aux questions 1 à 3.**
2. **L'acceptation ou le refus des simplifications** P1, P2, P4, P5, P6, P8, P12 et P14, et des reports P10, P11, P13 et interface.
3. **La règle de départage des égalités** (P8). Elle n'est pas proposée ici, faute de référence établie : le LOT-2A la note « non vérifiée » dans OXCE.
4. **Les coûts de case du jeu.** Les tests peuvent utiliser des valeurs fictives. Les valeurs réelles relèvent de l'équilibrage, qui exige l'accord explicite du propriétaire (`CLAUDE.md` §3).
5. **L'origine des TU de l'unité** (capital, récupération à chaque tour) : hors de ce périmètre, elle devra être fixée ailleurs ou supposée donnée.
6. **La classe de la fiche.** Elle dépend des réponses. Plusieurs simplifications (P4, P6, P8, P12) s'écarteraient du modèle d'OXCE si elles étaient acceptées : une classe `OXCE-REFERENCE` pure paraîtrait alors difficile. C'est une observation, pas une décision.

## 6. Limites

- Les comportements d'OXCE cités viennent du LOT-2A : **lecture du code, sans exécution**. Aucune nouvelle lecture du code n'a été faite pour ce lot.
- Les valeurs des exemples sont **fictives** et ne préjugent pas de l'équilibrage.
- Les options listées ne sont pas exhaustives : le propriétaire peut en retenir une autre.
- Ce document ne crée aucune règle. La fiche `MEC-0001` exigera une décision explicite, datée et prouvée du propriétaire, puis un mandat distinct.

## 7. Contrôles, diff et revue indépendante

**Lectures.**
- Mandat : lu avec l'outil GitHub de la session, au commit `4b08e7d`.
- Depuis `origin/main` (`e3dfd41`) : `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`, `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/references/OXCE-BASELINE.md` et `CLAUDE.md`. Les trois derniers ont aussi été comparés à la branche du LOT-2A : `git diff` vide.
- Code OXCE : aucune nouvelle lecture par le développeur. Le relecteur a fait deux lectures ciblées, sans exécution : `Pathfinding.cpp:573-577` et `:940-1003`.

**Diff.** Un seul fichier, nouveau : ce rapport. Aucun autre fichier modifié (`git status --short`). Aucune fiche `MEC`, aucun registre touché.

| Contrôle | Résultat | Code de sortie |
|---|---|---|
| `git fetch origin main` au démarrage | `origin/main` = `e3dfd41ab43dcc17f1cbf79afce1fe0828a0821f`, base attendue | 0 |
| `git diff --check` (fichiers suivis) | Aucune sortie | 0 |
| `git diff --no-index --check /dev/null` sur ce rapport | Aucune erreur d'espacement signalée | 1 (attendu : le fichier diffère de `/dev/null`) |
| Recherche d'espaces en fin de ligne (`grep -nP "[ \t]+$"`) | Aucune ligne | 1 (aucune correspondance) |

**Non lancés** : `dotnet build`, `dotnet test`, `dotnet format` et les tests des hooks. Ils ne sont pas obligatoires pour ce lot documentaire, et aucun code n'est modifié. L'état de la CI GitHub est relevé après publication, dans la PR.

**Revue indépendante.**
- **Relecteur** : agent distinct du développeur, en lecture seule (aucune écriture, aucun commit). Il a relu ce rapport avant commit, avec le mandat, le LOT-2A et les registres.
- **Résultat** : 11 constats, dont 0 bloquant, 1 important et 10 mineurs. Il a recalculé tous les exemples et les a trouvés justes. Il a jugé conformes au mandat le regroupement P1 à P14, la fidélité au LOT-2A, D4 et le périmètre du diff.
- **Tous intégrés** :
  - constat important : les options de la question 2 supposent P6 acceptée ; « reproduire OXCE » redevient possible si P6 est refusée. S'y ajoute le rapprochement entre options et OXCE, marqué comme inférence ;
  - constats mineurs :
    - option B de la question 2 signalée comme ajoutée ;
    - conséquence de l'option C de la question 1 corrigée ;
    - « certains » grands murs ;
    - exception de la rotation (P10) ;
    - formulations « report proposé » et « s'écarteraient » ;
    - marche seule et sujets hors périmètre du LOT-2A rappelés ;
    - cas limite des TU exactes et cas d'une unité voisine ajoutés aux tests ;
    - « TU » et « A* » expliqués ;
    - libellé de l'exemple 3 et accords corrigés ;
    - base `origin/main` et lectures précisées.
- **Limites de la revue** : le relecteur a lu le mandat avec l'outil GitHub, sans vérifier que le commit `4b08e7d` appartient à la branche `orchestration/mandats`. Il est du même type que le développeur. Sa revue ne remplace pas l'accord du propriétaire.
