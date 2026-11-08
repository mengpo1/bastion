# LOT-2D — Actualisation de `MEC-0001` après le LOT-2C

| | |
|---|---|
| Mandat | `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md`, branche `orchestration/mandats`, commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`. Lu sur GitHub avec l'outil GitHub de la session, ni recopié ni archivé. |
| Autorisation | Propriétaire, 8 novembre 2026 : actualiser la fiche avec les décisions validées depuis le LOT-2C, corriger la mention obsolète d'`OXCE-BASELINE.md`, publier une PR en brouillon. |
| Branche | `docs/lot-2d-mec-0001-actualisation`, créée depuis `origin/main` = `6497e6b4c12b2804bc6b7c99a49fc645a820983e` (base attendue, revérifiée après `git fetch origin main` ; fiche `MEC-0001` inchangée depuis le LOT-2C). |
| Nature | Documentaire. **`MEC-0001` reste une proposition incomplète, sans décision globale « acceptée ». Aucun gameplay.** |

## 0. En bref

- **Z1 est acceptée** : la zone atteignable est affichée, et choisir une destination hors de cette zone est interdit. Elle supplante S5 (déplacement partiel) pour la sélection normale ; une interruption imprévue reste possible (S8, S11).
- **Décisions N1 à N14 inscrites** sur :
  - le terrain en cases et murs (modèle B) ;
  - la diagonale permissive ;
  - plusieurs niveaux ;
  - les escaliers, échelles et ascenseurs ;
  - les chutes et leurs dégâts ;
  - la surcharge.

  Les étapes N12 à N14 sur la surcharge sont fusionnées dans la décision finale N14.
- **Statut global inchangé** :
  - classe `MODIFICATION-PROPOSEE` ;
  - décision « reportée — arbitrages complémentaires requis » ;
  - aucun changement de gameplay autorisé ;
  - état non commencé.
- **`OXCE-BASELINE.md`** : la mention « Aucune fiche `MEC` » est corrigée, sans toucher à la référence OXCE.

## 1. Décisions et statuts

Sources des décisions : transcriptions des messages du propriétaire du 8 novembre 2026, **portées par le mandat LOT-2D** (§2). Claude Code n'a pas consulté cette conversation. L'autorisation d'exécution du propriétaire confirme ces transcriptions comme base de l'inscription. Elle ne vaut pas approbation globale de `MEC-0001`.

Colonne OXCE :
- **vérifié** = comportement lu dans le code au commit `441cae1`, concordant dans son principe avec la décision, sans fidélité démontrée ;
- **écart établi** = la décision s'écarte de ce comportement lu ;
- **à vérifier** = point seulement signalé au LOT-2A (§6), sans étude.

Aucune exécution d'OXCE.

| Réf. | Décision (résumé) | Statut | OXCE | Preuve OXCE |
|---|---|---|---|---|
| Z1 | Zone atteignable selon les TU et les informations connues ; destination hors zone interdite | **Acceptée** (auparavant proposée) | Écart établi | OXCE calcule le chemin sans regarder les TU, puis déplace partiellement : LOT-2A §2 ligne 9 |
| S5 | Déplacement partiel si TU insuffisantes | **Historique**, supplantée par Z1 pour la sélection normale | Vérifié (LOT-2A) | LOT-2A §2 ligne 9 |
| N1 | Modèle B : cases et murs séparant les cases ; 8 directions | **Acceptée** | Vérifié | Case à sol, mur ouest, mur nord et objet : LOT-2A §2 ligne 11 |
| N2 | Diagonale permise si au moins un des deux passages orthogonaux est ouvert ; interdite si les deux sont bloqués | **Acceptée** | Écart établi | OXCE refuse la diagonale dès qu'un des murs concernés bloque, sur l'un ou l'autre passage : LOT-2A §2 ligne 3 ; `src/Battlescape/Pathfinding.cpp:959-966` (nord-est) |
| N3 | Plusieurs niveaux dès `MEC-0001` ; positions (x, y, z) | **Acceptée** | Vérifié | Positions x, y, z : LOT-2A §2 ligne 1 |
| N4 | Escaliers, échelles et ascenseurs prévus dès la conception | **Acceptée** | À vérifier | — |
| N5 | Chutes volontaires et involontaires autorisées | **Acceptée** | À vérifier | — |
| N6 | Dégâts de chute croissants avec la hauteur | **Acceptée** | À vérifier | — |
| N7 | Pas de dégâts pour les petites chutes ; seuil à décider | **Acceptée** (seuil ouvert) | À vérifier | — |
| N8 | Caractéristiques et équipements peuvent modifier les conséquences d'une chute | **Acceptée** | À vérifier | — |
| N9 | L'armure peut protéger, mais son poids peut aussi aggraver une chute | **Acceptée** | À vérifier | — |
| N10 | Le poids de l'inventaire contribue à l'effet de la charge lors d'une chute | **Acceptée** | Chute : à vérifier. Poids porté : vérifié | Poids porté = armure + objets de l'inventaire : `src/Savegame/BattleUnit.cpp:4852-4861` |
| N11 | Le poids total porté affecte aussi le déplacement normal | **Acceptée** | Vérifié | Effet indirect dans OXCE : réduction des TU, qui touche toutes les actions ; voir N12 à N14 |
| N12 à N14 | Surcharge, décision finale N14 : principe d'OXCE, sans seuil d'immobilisation ; l'unité est empêchée d'avancer seulement quand ses TU restantes ne paient pas le pas suivant ; « encombré » peut rester un indicateur informatif, sans nouveau modificateur ni statut technique ; la Force détermine l'effet (N13) | **Acceptée** (N14 remplace la pénalité et l'immobilisation de N12) | Vérifié | TU multipliées par Force / poids si ce rapport est inférieur à 1, à leur récupération, puis tronquées, avant d'autres pénalités : `src/Savegame/BattleUnit.cpp:2709-2726`. Arrêt si le pas dépasse les TU restantes : `src/Battlescape/UnitWalkBState.cpp:295-323` |

**Non retenu comme décision**, conformément au mandat :
- une augmentation du coût des pas liée au poids : la question « progressif ou par paliers sur le coût d'un pas » est abandonnée ;
- une immobilisation automatique au-delà d'un seuil de charge : proposition écartée, non consignée au registre.

**Rapport entre S3 et N2.** N2 étend aux murs du modèle B le principe permissif de S3 (cases bloquées). S3 n'est pas modifiée ; le renvoi figure dans N2. Ce qu'est un passage « bloqué » (mur, case bloquée, ou les deux) reste ouvert, sous « géométrie des murs et des angles ». S4 (unité voisine) n'est pas modifiée.

## 2. Passages OXCE établis et non vérifiés

**Établis par lecture du code**, au commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, sans exécution. Les quatre passages cités ont été relus pour ce lot :
- `src/Savegame/BattleUnit.cpp:2709-2726` : récupération des TU, réduction selon le rapport Force / poids porté, puis pénalité des blessures aux jambes ;
- `src/Savegame/BattleUnit.cpp:4852-4861` : poids porté = poids de l'armure + poids des objets de l'inventaire ;
- `src/Battlescape/UnitWalkBState.cpp:295-323` : arrêt si le prochain pas dépasse les TU restantes ;
- `src/Battlescape/Pathfinding.cpp:959-966` : diagonale nord-est refusée dès qu'un des quatre murs concernés, ou un « grand mur » voisin, bloque.

Les autres comparaisons s'appuient sur le LOT-2A (§2 lignes 1, 3, 9 et 11).

**Non vérifiés** : le fonctionnement d'OXCE pour les escaliers, échelles et ascenseurs, les chutes, les dégâts de chute, et l'influence de la charge sur les chutes. Aucune fidélité à OXCE n'est affirmée sur ces points. Une comparaison exigerait un lot de recherche distinct.

## 3. Changements effectifs

1. **`docs/gameplay/GAMEPLAY-DECISIONS.md`**, fiche `MEC-0001` :
   - en-tête de la fiche, preuves (mandat LOT-2D, rapport LOT-2D, passages OXCE), « Changement demandé », « Décision du propriétaire » (qui commence toujours par « reportée ») et « Éléments exclus » mis à jour ;
   - section S1 à S12 datée « (LOT-2C) » ; S5 seule est annotée, comme demandé par le mandat : historique, supplantée par Z1 pour la sélection normale (annotation signalée comme ajoutée au LOT-2D) ;
   - la section « Proposition à confirmer » est remplacée par une section datée « Décisions acceptées le 8 novembre 2026, après le LOT-2C (LOT-2D) » : Z1 (origine rappelée), N1 à N11, N12 à N14 fusionnées, chacune avec son rapport à OXCE ;
   - « Encore ouvert » est révisé : le modèle B, la verticalité, les chutes et Z1 n'y figurent plus comme non décidés. La réserve sur S2 est maintenue : le modèle B peut obliger à la revoir (coût éventuel des murs).

   Les règles du registre, le gabarit, la classe, le périmètre autorisé et l'état sont inchangés.
2. **`docs/references/OXCE-BASELINE.md`** (ligne 45) : « Aucune fiche `MEC`. » est remplacé par la mention de `MEC-0001`, fiche documentaire incomplète et non approuvée ; la même puce dit déjà qu'aucun gameplay n'est implémenté. Rien d'autre n'est modifié.
3. **`docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`** : ce rapport, nouveau.

## 4. Limites

- Aucune exécution d'OXCE ; aucun test écrit ni exécuté.
- Les transcriptions viennent du mandat ; la conversation du propriétaire n'a pas été consultée.
- Aucun paramètre (seuil, formule, valeur) n'est ajouté comme décision.
- La transposition exacte du principe d'OXCE pour la surcharge (formule, arrondi, ordre avec les autres pénalités) reste ouverte.

## 5. Points encore ouverts (rappel de la fiche)

- géométrie des murs et des angles, portes, taille des unités ;
- coûts du terrain, des murs éventuels et des changements de niveau ;
- règles précises des escaliers, échelles et ascenseurs ;
- chutes : règles des chutes volontaires et involontaires, formule et valeurs des dégâts, hauteur sans dégâts, effets des caractéristiques, équipements, armure et charge ;
- transposition de la surcharge et présentation de l'indicateur « encombré » ;
- capital initial et renouvellement des TU ;
- coût minimal et départage ;
- orientation, énergie, interruptions ;
- visibilité détaillée et brouillard de guerre ;
- interface de la zone atteignable ;
- coût imprévu en cours de trajet ;
- autres propositions du LOT-2B ; classe définitive.

La liste n'est pas exhaustive.

## 6. Contrôles

| Contrôle | Résultat | Code de sortie |
|---|---|---|
| `git fetch origin main` au démarrage | `origin/main` = `6497e6b`, base attendue | 0 |
| Comparaison des registres de `main` avec la branche du LOT-2C (`git diff --stat`) | Aucune différence : `MEC-0001` n'a pas été modifiée par un autre lot | 0 |
| `git status --short` | Les 3 fichiers autorisés, et eux seuls | 0 |
| `git diff --check` (fichiers suivis) | Aucune sortie | 0 |
| Recherche d'espaces en fin de ligne dans les 3 fichiers | Aucune ligne | 1 (aucune correspondance) |
| Lecture de la décision de `MEC-0001`, comme la fait la CI (`awk` et `grep`, rejoués à part) | Une seule ligne « Décision du propriétaire », lue « reportée — … » : rejetée comme non « acceptée » | 0 |
| Recherche de « à confirmer » dans le registre | Aucune occurrence | 1 (aucune correspondance) |

**Non lancés** : `dotnet build`, `dotnet test`, `dotnet format` et les tests des hooks. Ils ne sont pas requis pour ce lot documentaire, et aucun code n'est modifié. L'état de la CI GitHub est relevé après publication, dans la PR.

## 7. Revue indépendante

- **Relecteur** : agent distinct du développeur, en lecture seule (aucune écriture dans le dépôt ni dans git). Il a lu le mandat sur GitHub au commit `d71fbcc` et relu le diff non commité, le LOT-2A, le LOT-2B, le LOT-2C, le script de la CI et le code OXCE aux lignes citées.
- **Résultat** : 10 constats, dont 1 bloquant, 1 important et 8 mineurs ou cosmétiques. Il a confirmé :
  - les passages OXCE cités, dont l'écart établi de N2 ;
  - qu'aucun seuil, aucune immobilisation et aucun surcoût des pas n'est présenté comme décidé ;
  - que la fiche reste « reportée » pour la CI ;
  - que la liste des points ouverts est complète au regard du mandat ;
  - que le diff porte sur 3 fichiers.
- **Tous intégrés**, après vérification :
  - **bloquant** : le sens de N14 était inversé. « L'unité ne peut plus avancer que lorsque… » est devenu « l'unité est empêchée d'avancer seulement lorsque ses TU restantes ne permettent pas de payer le pas suivant », dans la fiche et dans le rapport ;
  - **important** : la réserve sur S2 est rétablie, car le modèle B peut obliger à la revoir (coût éventuel des murs) ;
  - **mineurs** :
    - « sans nouveau modificateur » ;
    - légende « vérifié » précisée (concordance de principe, sans fidélité démontrée ; « à vérifier » = signalé au LOT-2A §6) ;
    - effet indirect du poids pour N11 ;
    - formulation de la fusion N12 à N14 ;
    - renvoi S3 → N2 déplacé dans N2 ;
    - annotation de S5 signalée comme ajoutée au LOT-2D ;
    - portée de Z1 attribuée au mandat ;
    - « peut protéger » pour N9 ;
    - origine de Z1 rappelée ;
    - redite d'`OXCE-BASELINE.md` supprimée.
- **Limites de la revue** :
  - l'autorisation du propriétaire et la conversation du 8 novembre ne sont pas vérifiables par le relecteur ;
  - le rendu Markdown est jugé selon CommonMark, sans rendu GitHub ;
  - OXCE n'a été ni compilé ni exécuté ;
  - le relecteur est du même type que le développeur, et sa revue ne vaut pas validation.
