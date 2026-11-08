# LOT-2C — Inscription des décisions partielles de `MEC-0001`

| | |
|---|---|
| Mandat | `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md`, branche `orchestration/mandats`, commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`. Lu sur GitHub avec l'outil GitHub de la session, ni recopié ni archivé. |
| Autorisation | Propriétaire, 8 novembre 2026 : exécution du LOT-2C, inscription au registre des « décisions partielles de MEC-0001, en respectant exactement leur statut ». |
| Branche | `docs/lot-2c-mec-0001-decisions`, créée depuis `origin/main` = `a2418df007b486431dc25895dd4aca5230e58dc6` (base attendue, revérifiée après `git fetch origin main`). |
| Nature | Documentaire. **`MEC-0001` reste une proposition incomplète, sans décision globale « acceptée ». Aucun gameplay, aucun test de gameplay.** |

## 0. En bref

- Le registre `docs/gameplay/GAMEPLAY-DECISIONS.md` contient désormais la fiche `MEC-0001 — Déplacement élémentaire à pied`.
- **Statut global** :
  - classe `MODIFICATION-PROPOSEE` ;
  - décision « reportée — arbitrages complémentaires requis » ;
  - périmètre autorisé : **aucun changement de gameplay** ;
  - état : non commencé.
- La fiche distingue :
  - **12 sous-décisions de conception acceptées** le 8 novembre 2026 (S1 à S12 ; S*n* transcrit la déclaration A.*n* du mandat) ;
  - **1 proposition du propriétaire à confirmer** (Z1, zone atteignable) ;
  - **9 groupes de points encore ouverts** (O1 à O9), liste non exhaustive.

## 1. Changements

1. **`docs/gameplay/GAMEPLAY-DECISIONS.md`** :
   - l'en-tête « Aucune mécanique n'est enregistrée » est remplacé par la mention d'une seule fiche, proposée et incomplète. La conséquence est conservée : aucune mécanique ne peut être implémentée ;
   - « _Aucune._ » est remplacé par la fiche `MEC-0001`, au gabarit du registre, suivie de trois listes : sous-décisions acceptées, proposition à confirmer, points ouverts ;
   - les règles du registre et le gabarit ne sont pas modifiés.
2. **`docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`** : ce rapport, nouveau.

## 2. Accepté, proposé, ouvert

La dernière colonne résume le LOT-2A, qui repose sur une **lecture du code, sans exécution**. « Non étudié » signifie que le LOT-2A ne l'a pas examiné.

| # | Règle (résumé) | Statut | Origine dans le LOT-2B | Rapport à OXCE (LOT-2A) |
|---|---|---|---|---|
| S1 | Huit directions, diagonales incluses | **Acceptée** | P2 | Identique : 8 directions (§2 ligne 2) |
| S2 | Diagonale : coût de la case d'arrivée × 1,5, arrondi à l'inférieur | **Acceptée** | Question 1, option A | Identique (§2 ligne 4) |
| S3 | Diagonale interdite seulement si les deux cases orthogonales voisines sont bloquées | **Acceptée** | Question 2, option B | Écart : option sans équivalent dans OXCE, dont la règle dépend des murs et « grands murs » (§2 ligne 3) |
| S4 | Une unité voisine n'est pas un obstacle pour la diagonale | **Acceptée** | Question 2, sous-question | Identique : une unité voisine ne gêne pas (§2 ligne 3) |
| S5 | TU insuffisantes : déplacement partiel | **Acceptée** (décision initiale, nuancée par Z1) | Question 3, option A | Identique (§2 ligne 9) |
| S6 | Destinations : cases visibles ou déjà explorées | **Acceptée** | Nouveau ; la visibilité était hors périmètre au LOT-2B (§1) | Non étudié |
| S7 | Trajet entièrement dans des cases visibles ou déjà explorées | **Acceptée** | Nouveau | Non étudié |
| S8 | Trajet calculé sur le dernier état connu du terrain ; interruption devant un obstacle inconnu | **Acceptée** | Nouveau | Non établi. Le LOT-2A note seulement que chaque pas recalcule son coût sur l'état courant et que la marche s'arrête si le pas suivant devient impossible (§2 lignes 15 et 16) |
| S9 | Un obstacle inconnu rencontré devient connu du joueur | **Acceptée** | Nouveau | Non étudié |
| S10 | Case occupée par une autre unité : infranchissable, en traversée comme en destination | **Acceptée** | §1 point 6 | Proche : les unités connues bloquent le calcul (§2 lignes 12 et 13) |
| S11 | Une unité cachée rencontrée en marchant est révélée au joueur | **Acceptée** | Nouveau ; remplace l'hypothèse P12 | Partiel : la marche s'arrête avant sa case (§2 ligne 12) ; repérage à cet instant non vérifié (NV) |
| S12 | Une unité révélée redevient cachée quand elle n'est plus observable, sans trace de sa position | **Acceptée** | Nouveau | Non étudié |
| Z1 | Afficher la zone atteignable ; interdire une destination hors zone. Remplacerait S5 pour une sélection normale ; S8 demeurerait | **Proposée, à confirmer** | Troisième voie de la question 3 | Écart : OXCE calcule le chemin sans regarder les TU (§2 ligne 9) |
| O1 | Carte à un niveau ; taille des unités ; coût d'entrée par case ; murs et obstacles. S2 et S3 en dépendent | **Ouvert** | P1, P4, P6 | — |
| O2 | Valeurs des coûts de terrain ; capital et renouvellement des TU | **Ouvert** | P5, §5 | — |
| O3 | Calcul de chemin garantissant le coût minimal ; départage déterministe des égalités | **Ouvert** | P8 | — |
| O4 | Orientation, rotation ; énergie ; interruptions non spécifiées | **Ouvert** | P10, P11, P13 | — |
| O5 | Conditions de visibilité ; brouillard de guerre hors déplacement | **Ouvert** | Nouveau | — |
| O6 | Interface de la zone atteignable | **Ouvert** | Interface | — |
| O7 | Trajet devenu non payable ou non réalisable (coût réel ou occupation jusque-là inconnus) | **Ouvert** | Nouveau | — |
| O8 | Confirmation de Z1 et rôle restant de S5 | **Ouvert** | — | — |
| O9 | Autres propositions du LOT-2B non arbitrées : ordre impossible sans TU dépensée, paiement de chaque pas avant de le faire, marche seule ; classe définitive de la fiche | **Ouvert** | P14, §1 points 8 et 10, §5 point 6 | — |

O1 à O7 reprennent la liste du mandat (§3). O8 et O9 sont ajoutés par Claude Code, sans rien décider, pour que la liste ne paraisse pas complète.

Ne sont pas retenues comme décisions :
- les autres propositions du LOT-2B ;
- l'hypothèse « toutes les unités connues » (P12), que S6 à S12 remplacent.

## 3. Preuve et limites

- **Source des décisions.** Ce sont des transcriptions des messages du propriétaire du 8 novembre 2026, **portées par le mandat LOT-2C**. Claude Code n'a pas consulté cette conversation. Selon le mandat (§5.1), l'autorisation d'exécution du propriétaire valide ces transcriptions comme base de l'inscription. Elle ne vaut ni acceptation globale de `MEC-0001`, ni autorisation de développer.
- **Statuts.**
  - Les déclarations que le mandat classe comme « explicitement validantes » (§2.A) sont inscrites comme sous-décisions acceptées.
  - La phrase « je souhaite proposer », suivie de « Ok », est inscrite comme proposition à confirmer (Z1), selon le mandat (§2.B).
  - S5 n'est pas présentée sans sa nuance ultérieure.
  - Aucune décision n'a été ajoutée par déduction. Exemple : la rencontre d'une unité cachée (S10, S11) arrête-t-elle le déplacement ? La question est rangée sous O7, sans réponse.
- **OXCE.** Commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b`, lecture du code seulement (LOT-2A). **Aucune exécution d'OXCE**, aucune fidélité démontrée. Aucune nouvelle lecture du code pour ce lot.
- **Tests.** Seulement des critères futurs ; aucun test écrit ni exécuté.
- **Effet sur la CI.** Le contrôle de traçabilité de la CI (`scripts/harness/check-simulation-trace.sh`) rejette toute fiche dont la décision contient « reportée ». Une PR qui toucherait `src/Bastion.Simulation/` en déclarant `MEC-0001` serait donc refusée (§5). Ce contrôle est seulement syntaxique : il n'arrête pas une déclaration `TECHNIQUE`, et il lit le registre de la PR elle-même. La protection repose aussi sur les règles et sur la revue.
- **« Comme OXCE ».** Dans S2 et S5, ce sont les mots du propriétaire. La fiche précise qu'il s'agit de la lecture du code (LOT-2A), pas d'une fidélité démontrée.

## 4. Points à arbitrer

1. Les points ouverts O1 à O9, dont la confirmation de Z1. Cette liste n'est pas exhaustive : tout ce que S1 à S12 ne couvrent pas reste non décidé.
2. **Dépendance à surveiller** : S2 et S3 supposent un coût par case et des obstacles en cases bloquées (simplifications P4 et P6 du LOT-2B, encore ouvertes en O1). Si O1 retient un autre modèle (murs minces, objets distincts), S2 et S3 pourraient devoir être revues.
3. La décision globale de `MEC-0001` (acceptée, refusée ou reportée), une fois ces points tranchés. Seule une décision globale « acceptée » pourra autoriser une implémentation, dans un mandat distinct.
4. **Hors périmètre de ce lot** : `docs/references/OXCE-BASELINE.md` (ligne 45) indique encore « Aucune fiche `MEC`. », ce qui n'est plus exact. Le mandat interdit de toucher ce fichier ; à corriger dans un mandat ultérieur.

## 5. Vérifications

| Vérification | Résultat | Code de sortie |
|---|---|---|
| `git fetch origin main` au démarrage | `origin/main` = `a2418df`, base attendue ; aucune fiche `MEC-0001` sur `main` | 0 |
| `git status --short` et `git diff --name-only` | Les 2 fichiers autorisés, et eux seuls | 0 |
| `git diff --check` (fichiers suivis) | Aucune sortie | 0 |
| `git diff --no-index --check /dev/null` sur ce rapport | Aucune erreur d'espacement | 1 (attendu : le fichier diffère de `/dev/null`) |
| Recherche d'espaces en fin de ligne dans les 2 fichiers | Aucune ligne | 1 (aucune correspondance) |
| Extraction de la décision de `MEC-0001`, comme le fait le contrôle de la CI (`awk` et `grep`, rejoués à part) | La fiche est trouvée (53 lignes, version finale) ; une seule ligne « Décision du propriétaire », lue « reportée — … » ; résultat : rejetée comme non « acceptée » | 0 |

**Non lancés** : `dotnet build`, `dotnet test`, `dotnet format` et les tests des hooks. Ils ne sont pas requis pour ce lot documentaire, et aucun code n'est modifié. L'état de la CI GitHub est relevé après publication, dans la PR.

## 6. Revue indépendante

- **Relecteur** : agent distinct du développeur, en lecture seule (aucune écriture dans le dépôt, aucun commit). Il a lu le mandat avec l'outil GitHub et relu le diff non commité, le LOT-2A, le LOT-2B, les règles et le script de la CI.
- **Résultat** : 12 constats, dont 0 bloquant, 2 importants et 10 mineurs. Il a jugé exactes :
  - les 12 transcriptions (S*n* = A.*n*) et leurs statuts ;
  - la portée de Z1 ;
  - la reprise des points ouverts du mandat.

  Il a rejoué la lecture de la CI : une déclaration `MEC-0001` serait rejetée.
- **Tous intégrés** :
  - **constats importants :**
    - liste des points ouverts non exhaustive, d'où l'ajout d'O9 et de la mention « liste non exhaustive » ;
    - dépendance de S2 et S3 envers O1, signalée dans la fiche et au §4 ;
  - **constats mineurs :**
    - formulation « explicitement validantes » ;
    - colonne OXCE pour S8, S10 et S11 ;
    - précision « selon la lecture du code » pour S2 et S5 ;
    - libellé d'O3 ;
    - correspondance S*n* = A.*n* ;
    - Z1 attribuée au propriétaire et chemin du mandat dans la preuve ;
    - renvoi « raisons et impacts » ;
    - mention périmée d'`OXCE-BASELINE.md` signalée ;
    - portée du contrôle de la CI ;
    - formulations sur S6 et sur S6 à S12.
- **Limites de la revue** :
  - l'autorisation du propriétaire et la conversation du 8 novembre ne sont pas vérifiables par le relecteur : les transcriptions ont été contrôlées contre le mandat seul ;
  - le code OXCE n'a pas été relu ;
  - le relecteur est du même type que le développeur ; sa revue ne vaut pas validation.
