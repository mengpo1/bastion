# Bastion — Lot 1J : dossier de conception, plusieurs unités et alternance des camps

**Date :** 27 novembre 2026
**Mandat :** `docs/mandates/BASTION-MANDAT-LOT-1J-v1.0-transcription.md`. C'est la transcription du message du propriétaire du 2026-11-27T13:36:01Z, extraite mécaniquement du journal de session ; son identité avec un fichier original n'est pas vérifiée. Le texte se présente comme une « proposition de cadrage, non une autorisation d'exécution ».
**Autorisation :** 2026-11-27T13:40:13Z. En réponse à deux questions de Claude Code, le propriétaire a choisi :
- « Autoriser, dossier dans le dépôt (Recommandé) » : exécution locale, dossier dans `docs/reviews/`, mandat archivé et indexé, relecture indépendante ; aucun code ni test, registre intact, sans commit ni push ;
- « Non vérifiée, à qualifier (Recommandé) », pour la décision Q1-B (§3).

**Base :** `origin/main` = `364b46acc486fa723ba1787c6e4b01e9a3537678`, la référence du mandat, établie par `git fetch origin main`.
**Branche :** `claude/lot-1j-conception-camps`, créée localement à partir de cette base.
**État :** dossier préparatoire. **Rien n'est commité ni publié.**

> **Avertissement.** Ce dossier ne décide rien. Il n'autorise aucun gameplay et ne modifie ni le registre, ni le code, ni les tests. MEC-0003 et MEC-0004 restent inchangées ; MEC-0001 et MEC-0002 restent reportées. Toute règle marquée **[PROP]** est une proposition non validée ; toute question **[QO]** attend une décision du propriétaire. La validation des règles et l'autorisation d'implémentation feront l'objet de décisions distinctes.

**Étiquettes :**
- **[IMPL]** : règle acceptée, implémentée et intégrée à `main` (MEC-0003, MEC-0004) ;
- **[REG]** : sous-décision inscrite au registre dans une fiche reportée (MEC-0001, MEC-0002). Elle est acceptée comme principe, mais n'autorise aucune implémentation. Chaque sous-décision garde son propre niveau de preuve au registre ([TR], [CIT], [DÉC]…) : par exemple, Q4.14 n'y est qu'au niveau [CIT], sous forme de résumé ;
- **[NV]** : élément non vérifié : aucune preuve primaire de validation accessible ;
- **[DÉCL]** : déclaration du propriétaire transmise dans la conversation, dont la source primaire n'est pas accessible à Claude Code ;
- **[PROP]** : proposition de ce dossier, non validée ;
- **[QO]** : question ouverte, à trancher par le propriétaire ;
- **[INSP]** : constat fait par lecture du code ou des documents, sans exécution.

## 1. Résumé

- **Ce qui existe :** une seule unité, sans identité ni camp. La marche est celle de MEC-0003 (`Movement/`), et la fin de tour explicite avec récupération plafonnée est celle de MEC-0004 (`Turns/`). Le moteur de marche ignore les autres unités ; l'état de tour porte une seule unité.
- **Q1-B (trois camps, phases Joueur → Hostile → Neutre, phase neutre autonome) : déclarée validée, non vérifiable indépendamment.**
  - Aucune trace de la décision n'existe dans le dépôt, ni dans les journaux de session accessibles avant le 27 novembre. L'option (b) d'une question de l'étude LOT-2L, non publiée, est la seule trace écrite de l'option proposée, non de sa validation.
  - Le 27 novembre 2026, le propriétaire a déclaré l'avoir validée le 16 novembre 2026 à 14:49:17 UTC, dans une conversation avec l'orchestrateur que Claude Code ne peut pas consulter (§3).
- **Règles déjà acquises qui concernent plusieurs unités :** elles existent, mais dans des fiches reportées. Ce sont notamment :
  - S10, une case occupée étant infranchissable, Q5.2 et les exceptions ARB-B (corps morts ou inconscients) et G2 (réveil) ;
  - G1 et ARB-A, le volume d'une unité consciente pouvant bloquer un passage ;
  - G4, les chemins calculés sur les seules informations connues du camp ;
  - ES-09, l'usage des TU restantes « pendant le tour adverse ».

  Une gestion de plusieurs unités ne peut pas les ignorer sans les contredire (§4).
- **Décisions complémentaires nécessaires :** dix-sept questions ouvertes (§5). Les plus structurantes sont :
  - QO-01, les camps et leur ordre ;
  - QO-04, le moment de la récupération ;
  - QO-07, l'occupation des cases par les autres unités ;
  - QO-08, les unités incapables d'agir.
- **Proposition minimale [PROP] :** un état de bataille immuable, avec des camps ordonnés, des unités identifiées et une phase active (§6). La sélection est libre dans la phase du joueur, la fin de phase explicite, les phases sans unité apte sont passées automatiquement, et les phases non jouées le sont par un contrôleur « sans action » en attendant une IA.
- **Impacts, risques et matrice de tests prévisionnels :** §7 et §8.
- **Proposition de fiche :** sous l'identifiant **MEC-0005, à confirmer** (§9). La matrice compte 28 tests prévisionnels (§8).

## 2. Architecture actuelle de `Bastion.Simulation` [INSP]

Lecture du code à `364b46a`.

### 2.1 `Movement/` (MEC-0003)

- **`UnitState`** : un `record` immuable qui porte quatre valeurs, `Position`, `Orientation`, `Tu` et `Energy`. Son constructeur est interne ; un état se crée par `MovementModel.CreateState`, qui le valide.
  - Il n'a **ni identité, ni camp, ni statut** (vivant, conscient, apte).
  - Deux unités aux mêmes position, orientation et ressources seraient **égales** au sens du `record`.
  - Une expression `with` peut dériver d'un état valide un `UnitState` non validé, par exemple avec des ressources négatives ; les tests de `Turns/` s'en servent pour vérifier les refus (`TurnTests.cs`, `T09_NegativeResourcesAreRefused`).
- **`MovementModel`** : construit pour une carte (`TacticalMap`), des règles (`MovementRules`) et une emprise (`UnitBody`). Ses opérations prennent un seul `UnitState` :
  - `ComputeReachability(state)` ;
  - `EvaluateStep(state, direction)` ;
  - `ExecutePath(state, path)` ;
  - `ExecuteOrder(state, destination)`.
- **`TacticalMap`** : ne connaît que le terrain, les cases infranchissables et les murs. **Aucune notion d'occupation par une autre unité.** C'est conforme au hors-périmètre de MEC-0003 : « autres unités et corps, et donc S10, ARB-B et G2 ».
- **Emprise :** une seule `UnitBody` par modèle. Plusieurs modèles peuvent partager une même carte. Des unités d'emprises différentes demanderaient un modèle par type, ou une emprise portée par l'unité ; le registre prévoit déjà des dimensions « configurables par type d'unité et posture » (Q1.2).

### 2.2 `Turns/` (MEC-0004)

- **`TurnRules`** : quatre paramètres validés (`MaxTu`, `TuRecovery`, `MaxEnergy`, `EnergyRecovery`), avec le profil de test `Initial` (60, 60, 100, 20). Trois opérations :
  - `Start(UnitState)` rend le tour 1 ;
  - `WithUnit(TurnState, UnitState)` remplace l'unité sans changer de tour ;
  - `EndTurn(TurnState)` applique `min(courante + récupération, plafond)` à chaque ressource et incrémente le tour.
- **`TurnState`** : le numéro de tour et **une seule** `UnitState`.
- **`TurnOutcome`** : les états avant et après, les récupérations effectives et le compte rendu.
- **Les paramètres de récupération sont globaux** : un seul `TurnRules` pour l'unité, sans profil par unité ou par type.

### 2.3 Client Godot et tests

- **Scène :** `PrototypeScene` garde `State` et `Turns` en parallèle et les synchronise à la main (observation RG-08 du lot 1G).
- **Tests :** sur `main`, 65 tests xUnit et 120 contrôles fumée Godot, d'après la CI de la PR #28. Les 65 tests se répartissent ainsi :
  - 44 tests de la marche (`tests/Bastion.Simulation.Tests/Movement/`) ;
  - 2 tests techniques ;
  - 19 tests des tours (`tests/Bastion.Simulation.Tests/Turns/TurnTests.cs`).

### 2.4 Ce qui manque pour plusieurs unités

1. Une **identité** stable pour chaque unité, distincte de son état.
2. Un **camp** pour chaque unité, et une liste ordonnée de camps.
3. Un **statut d'aptitude** : apte, inconsciente, morte, éventuellement d'autres.
4. Un **état de bataille** : l'ensemble des unités, la phase active et le numéro de tour.
5. L'**occupation des cases** dans le calcul de la zone atteignable et dans l'exécution des pas (S10 et ses exceptions).
6. Une **fin de phase** distincte de la fin de tour de MEC-0004, et un enchaînement des phases.
7. Un **point d'entrée pour un contrôleur** de camp : le joueur, ou un contrôleur automatique.

## 3. Provenance de la décision Q1-B [NV]

**Libellé reçu dans le mandat :** « trois camps, phases Joueur → Hostile → Neutre, phase neutre autonome ».

**Recherches effectuées par l'auteur (commandes exécutées) :**
- **`main`** (`364b46a`) : `git grep` sur `docs/` pour « Q1-B », « trois camps », « Joueur → Hostile », « Hostile → Neutre », « phase neutre » et « camp neutre ». **Aucune occurrence.**
- **Branche `orchestration/mandats`** : `git grep` sur « Q1-B », « trois camps », « phase neutre » et « Hostile ». Aucune occurrence. Les autres branches distantes n'ont pas été fouillées par l'auteur.
- **Journaux de session :** les entrées du journal courant (`-home-user`) et de l'ancien journal (`-home-user-bastion`, du 8 au 16 novembre), pour les motifs « Q1-B », « Je valide Q1 » et « phase autonome ». Aucune occurrence n'est antérieure au 27 novembre. Celles du 27 novembre sont le mandat LOT-1J, le message de régularisation (ci-dessous) et les échanges du présent lot qui les citent. Le motif « trois camps », cherché par l'auteur seulement dans le texte des messages de type utilisateur (propriétaire et remises de sous-agents) du journal courant, figure dans le journal le 16 novembre à 10:54:21 UTC : c'est l'écriture du fichier LOT-2L lui-même, selon la relecture (§12).
- **16 novembre 2026, dans cette session :** le dernier message du propriétaire ce jour-là est la validation du mandat LOT-2L, à 10:27:29 UTC. Aucun message du propriétaire n'y figure vers 14:49 UTC.
- **Fichiers téléversés de la session :** aucune occurrence de « Q1-B », « phase autonome » ni « trois camps ».

**Recherches plus larges de la relecture indépendante** (§12) : tout l'historique Git, toutes branches confondues (`git log --all -S`), les deux journaux de session, les réponses du propriétaire aux questions et les fichiers téléversés. Elle ne trouve, elle non plus, aucune trace de la décision.

**Trace écrite de l'option proposée, et non de sa validation :** l'étude **LOT-2L** du 16 novembre 2026. C'est une étude documentaire comparée, en lecture seule, **non publiée**, remise dans la session et conservée hors du dépôt. Elle formule une question Q1, « Camps et contrôle des unités non jouées », avec trois options :
  - (a) deux camps alternés, avec des unités neutres sans phase propre ;
  - **(b) trois camps qui jouent chacun leur phase, comme dans OXCE** ;
  - (c) autre organisation.
- **Ce que LOT-2L rapporte d'OXCE** (code lu au commit `441cae1b071d249d40a223858cb6bd07fd5d791b`, sans exécution) :
  - les camps sont joués dans l'ordre Joueur, Hostile, Neutre ;
  - le compteur de tours avance au retour au Joueur ;
  - les camps hostile et neutre sont joués par l'IA ;
  - les TU sont renouvelées au début du tour de chaque camp.

  Ce rapport n'établit **aucune fidélité** d'une règle de Bastion à OXCE. Aucune reprise d'OXCE n'est envisagée (D4).

**Déclaration du propriétaire du 27 novembre 2026 [DÉCL]**, message « BASTION — Régularisation documentaire Q1-B » du 2026-11-27T13:58:24Z :
- le propriétaire y déclare avoir « explicitement validé Q1-B le 16 novembre 2026 à 14:49:17 UTC » ;
- texte cité : « Je valide Q1-B : trois camps avec une phase autonome pour les neutres, selon le modèle OXCE. » ;
- cette déclaration « a été retrouvée dans l'historique des conversations ChatGPT », mais « la conversation originale n'a pas été localisée sous une forme directement vérifiable par Claude Code ».

Ce message est une déclaration transmise : Claude Code ne peut vérifier ni le texte, ni l'heure, ni le contexte de la question posée. Sa traçabilité est analysée dans une note distincte (« Note de traçabilité Q1-B », remise avec ce dossier, hors dépôt). Ses principaux écarts avec les textes accessibles :
- l'option (b) de LOT-2L dit « trois camps qui jouent chacun leur phase, comme dans OXCE ». L'idée d'une phase **autonome** pour les neutres n'y figure pas ; elle ne correspond qu'à la description d'OXCE de la même étude, où les camps hostile et neutre sont joués par l'IA ;
- l'ordre Joueur → Hostile → Neutre n'est pas écrit dans le texte déclaré. Il ne s'en déduit que par « selon le modèle OXCE » : c'est une interprétation à confirmer ;
- « selon le modèle OXCE » ne peut valoir revendication de fidélité à OXCE (CLAUDE.md, §3).

**Ambiguïté de l'identifiant :** dans le registre, « Q1 » désigne déjà les questions de géométrie de MEC-0001 (Q1.1 à Q1.9), dont certaines ont des « options B ». « Q1-B » au sens de LOT-2L, la question Q1 de cette étude et son option (b), n'a aucun rapport avec elles. Un identifiant non ambigu sera nécessaire pour toute inscription.

**Qualification :**
- « Q1-B » correspond, d'après la déclaration du propriétaire, à l'option (b) de la question Q1 de LOT-2L.
- LOT-2L ne contient pas l'expression « phase neutre autonome ». Le fait que les camps non joués le soient par une IA y est seulement décrit pour OXCE.
- **Aucune preuve primaire de la validation n'est accessible.** La validation est seulement déclarée [DÉCL] ; elle n'est ni inscrite au registre, ni archivée dans le dépôt.
- Q1-B est donc traitée dans ce dossier comme une **décision déclarée, non vérifiable indépendamment**, et non comme une règle acquise. Toutes les règles qui en dépendent restent marquées en conséquence.

**Pour la régulariser :** une inscription au registre, par un mandat distinct, avec sa provenance déclarée. Le texte déclaré ne précise pas encore :
- ce que signifie « autonome » : joué par l'ordinateur, ou sans aucune action ;
- si l'ordre Joueur → Hostile → Neutre fait partie de la décision ou de son interprétation, « selon le modèle OXCE » ;
- la portée de « selon le modèle OXCE », qui ne peut valoir revendication de fidélité sans référence vérifiable et tests (CLAUDE.md, §3).

**Ce que dit déjà le registre :**
- **MEC-0004, §5 :** exclut « plusieurs unités », « adversaires ou intelligence artificielle » et « alternance entre camps ou phases ennemies ».
- **MEC-0001 et MEC-0002 :** emploient des notions qui supposent des camps, sans les définir. ES-09 parle du « tour adverse » ; SA-03 et SA-08 parlent d'« allié » et de « neutre » ; S6 à S12 parlent de la connaissance du joueur, et G4 des « informations connues du camp ».

## 4. Règles acquises qui concernent plusieurs unités ou les camps

| Réf. | Contenu | Étiquette | Conséquence pour plusieurs unités |
|---|---|---|---|
| MEC-0003 | Marche d'une seule unité : zone atteignable (Z1), coûts en TU et en énergie (G3), choix du chemin (G4), contrôle du volume, états immuables, refus sans modification (A9) | [IMPL] | À conserver telle quelle pour chaque unité. Ses tests restent la référence de non-régression |
| MEC-0004 | Fin de tour explicite ; `min(courante + récupération, plafond)` pour les TU et l'énergie ; tour initial 1 ; paramètres configurables et validés ; position et orientation conservées | [IMPL] | Formule de récupération réutilisable telle quelle. Le **moment** de la récupération dans un enchaînement de phases n'est pas décidé (QO-04) |
| S10 | Une case occupée par une autre unité est infranchissable, pour la traversée comme pour la destination | [REG] | Dès qu'il y a deux unités sur la carte, S10 s'applique, sauf décision contraire. Le moteur de marche ne le gère pas aujourd'hui (§2.1) |
| ARB-B | Pendant la marche ordinaire, un corps mort ou inconscient ne bloque ni la traversée ni la destination | [REG] | Exige un statut des unités (§2.4) |
| G2 | Réveil d'une unité inconsciente sur une case occupée : repositionnement sur une case voisine libre, ou reprise de conscience sur place, au sol | [REG] | Concerne la transition « inconscient → conscient », hors du présent cadrage minimal (QO-08) |
| S4, ARB-A, G1 | Une unité consciente voisine peut rendre physiquement impraticable le passage d'une diagonale ; le volume d'une unité ne peut pas traverser celui d'une autre unité consciente | [REG], ARB-A et G1 étant appliquées par MEC-0003 aux obstacles | Contrôle de volume entre unités, absent du moteur (QO-17) |
| ARB-D, Q3.6 | Récupération des TU par addition plafonnée (puis surcharge) ; énergie récupérée séparément | [REG], appliquées par renvoi dans MEC-0004 | Formule déjà implémentée pour une unité |
| ES-09 | L'esquive se paie « avec les TU restantes, même pendant le tour adverse » | [REG] (MEC-0002) | Suggère que les TU d'une unité ne sont pas renouvelées au début de la phase adverse. Indice pour QO-04, non décisif |
| ARB-E | Un tir de réaction effectivement tiré interrompt l'ordre de marche | [REG] | Suppose des unités adverses actives pendant la phase du joueur ; hors du présent cadrage |
| Q4.14 | Une incapacité interrompt l'action | [REG] | Suppose un statut « incapable » (QO-08) |
| ES-07 | Une unité inconsciente ou morte n'esquive pas | [REG] | Même statut |
| SA-03, SA-08 | Un allié ou un neutre identifié ne peut pas être ciblé intentionnellement ; un allié ou un neutre caché peut être percuté | [REG] | Suppose une relation entre camps (allié, neutre, ennemi) |
| S6 à S12 | Destinations et trajets limités au visible ou à l'exploré ; révélation et dissimulation des unités | [REG] | Une connaissance par camp est nécessaire pour une IA qui respecte la visibilité (QO-13) |
| Exclusion de MEC-0002 | « renouvellement des TU » exclu de MEC-0002 | [REG] | Le renouvellement relève d'une autre fiche, MEC-0004 ou la future |
| G4 | Chemin choisi parmi les chemins admissibles « avec les ressources disponibles et les informations connues du camp (S6 à S9, et non la vérité cachée) » | [REG], appliquée par MEC-0003 | Une occupation inconnue du camp ne peut pas entrer dans le calcul du chemin ; elle se découvre pendant la marche (S8, S11) |
| Q5.2 | Une connexion peut avoir une capacité supérieure à une unité, sans supprimer S10 ; « chaque unité consciente occupe un emplacement tactique stable distinct lorsqu'elle est en position stable » ; « aucune superposition volontaire de deux unités conscientes sur un même emplacement stable n'est autorisée » | [REG] ([DÉC]) | Confirme S10 pour les unités conscientes en position stable ; la coexistence involontaire de G2 reste une exception |
| Q1.2 | Dimensions « configurables par type d'unité et posture » ; les collisions restent obligatoires | [REG] | Touche QO-11 : une emprise par type est déjà prévue |
| SA-04 | Un ennemi actuellement visible peut être ciblé malgré S10 | [REG] | Suppose des camps ennemis |
| Q1-B | Trois camps, Joueur → Hostile → Neutre, phase neutre autonome | **[DÉCL], [NV]** | Décision déclarée, non vérifiable indépendamment ; non inscrite (§3) |

## 5. Décisions complémentaires nécessaires [QO]

| ID | Question | Options envisageables, non exhaustives | Dépendances |
|---|---|---|---|
| QO-01 | Quels camps, et dans quel ordre ? Le découpage se fait-il par camp ? | (a) Joueur → Hostile → Neutre, selon Q1-B déclarée, si le propriétaire décide de l'inscrire ; (b) deux camps alternés, neutres sans phase ; (c) liste de camps configurable par scénario, avec un ordre fixe. LOT-2L envisageait aussi un découpage par unité plutôt que par camp | Q1-B |
| QO-02 | Quand le numéro de tour augmente-t-il ? | (a) au retour au premier camp, une manche complète valant un tour ; (b) à chaque phase | QO-01 |
| QO-03 | Distinction entre tour, phase et activation | Le tour est une manche ; la phase est le temps d'un camp ; l'activation est le contrôle d'une unité. Faut-il une « fin d'activation » explicite, ou une simple sélection ? | — |
| QO-04 | **Moment de la récupération** des TU et de l'énergie | (a) au début de la phase du camp de l'unité ; (b) à la fin de la phase de ce camp, comme la fin de tour de MEC-0004 pour une unité seule ; (c) une fois par manche. ES-09 penche vers (a), sans le trancher | MEC-0004, ES-09 |
| QO-05 | Sélection des unités du joueur | Ordre libre ; changement d'unité à tout moment ; retour à une unité déjà déplacée ; limite d'activations. L'unité sélectionnée fait-elle partie de l'état de bataille, ou seulement de l'interface ? | — |
| QO-06 | Fin de la phase du joueur | Explicite seulement, comme MEC-0004 qui n'a « aucune fin de tour automatique » ; ou automatique quand plus aucune unité ne peut agir | MEC-0004 |
| QO-07 | **Occupation des cases** | (a) appliquer S10, avec ARB-B si les statuts existent ; (b) n'admettre que des scénarios où les unités ne se gênent pas. Cette option contourne S10 sans le modifier ; elle demande une décision explicite | S10, ARB-B, G1 |
| QO-08 | Unités incapables d'agir | Quels statuts (inconsciente, morte, autre) ? Sont-elles sélectionnables ? Récupèrent-elles leurs ressources ? Comptent-elles comme « occupant » une case (ARB-B) ? | Q4.14, ES-07, G2 |
| QO-09 | Camp sans unité apte | Phase passée automatiquement ; phase sautée sans être comptée ; ou fin de la bataille | QO-01, QO-02 |
| QO-10 | Paramètres de récupération | Communs à toutes les unités, comme le `TurnRules` actuel, ou propres à chaque unité ou type | MEC-0004 |
| QO-11 | Emprise des unités | Q1.2 prévoit déjà des dimensions « configurables par type d'unité et posture ». Reste à choisir : une emprise commune dans le premier incrément, comme aujourd'hui une par modèle, ou une emprise par type dès le départ | MEC-0003, Q1.2 |
| QO-12 | Phases des camps non joués **en l'absence d'IA** | Contrôleur « sans action » qui termine la phase ; ou jeu manuel de tous les camps pour les essais | Q1-B, QO-13 |
| QO-13 | Articulation avec une future IA | Interface de contrôleur par camp. L'IA respecte-t-elle la visibilité de son camp (S6 à S12) ? Doit-elle être déterministe, avec une graine ? | S6 à S12 |
| QO-14 | Relations entre camps | Ennemi, allié, neutre : table fixe ou configurable ? Nécessaire pour SA-03 et SA-08, pas pour le seul enchaînement des phases | SA-03, SA-08 |
| QO-15 | Devenir du scénario 4 et de `TurnState` | Conserver MEC-0004 telle quelle à côté du nouvel état de bataille ; ou la redéfinir plus tard comme un cas à un camp et une unité, ce qui demande une décision sur MEC-0004 | MEC-0004 |
| QO-16 | Occupants inconnus du camp | Le calcul de la zone et du chemin ne tient compte que des occupants connus du camp (G4, S6 à S9). Le registre répond déjà en partie à la rencontre d'une unité cachée : le pas non commencé n'est pas débité (Q3.4) ; la seule révélation n'interrompt pas la marche (Q4.20) ; l'arrêt se fait sans recalcul ni reprise automatique (Q4.21). Reste à décider si ces règles entrent dans le premier incrément | G4, S8, S11, Q3.4, Q4.20, Q4.21 |
| QO-17 | Volume entre unités | (a) Appliquer G1 et ARB-A entre unités conscientes dès le premier incrément. (b) Ne retenir d'abord que l'occupation des cases (S10), sans contrôle de volume entre unités : cette option **déroge à G1 et à ARB-A** entre unités et demande une décision explicite de dérogation. Une option qui refuserait toute diagonale longeant une unité consciente **dérogerait à S4 et à G1**, selon lesquelles une unité voisine n'interdit pas automatiquement la diagonale : elle demanderait une décision explicite de dérogation | G1, ARB-A, S4, Q5.2 |

## 6. Proposition de spécification minimale [PROP, non validée]

Elle ne retient que ce qui est nécessaire pour enchaîner des phases et activer plusieurs unités. **Aucune règle de combat, de réaction, de visibilité ni d'IA.** Chaque point indique la question dont il dépend.

**Concepts :**
- **Camp :** un identifiant et un contrôleur (`joueur` ou `automatique`). La liste ordonnée des camps est un paramètre du scénario (QO-01).
- **Unité :** un identifiant stable, un camp, un statut et un état de marche `UnitState` de MEC-0003. L'identité est distincte de l'état : deux unités aux états égaux restent deux unités.
- **Statut :** dans ce dossier, « apte » désigne une unité consciente capable d'agir ; « inapte », une unité qui ne peut pas agir. Les statuts exacts relèvent de QO-08. Seuls les **corps morts ou inconscients** relèvent d'ARB-B : une unité consciente, même incapable d'agir pour une autre raison, reste soumise à S10.
- **État de bataille :** le numéro de tour, l'indice du camp actif et l'ensemble des unités ; éventuellement l'unité sélectionnée (QO-05). Il est immuable : chaque transition rend un nouvel état, comme `TurnRules` et `MovementModel`.

**Règles proposées :**

| ID | Proposition | Dépend de |
|---|---|---|
| P-01 | L'ordre des camps est fixe pendant une bataille. Par défaut : Joueur → Hostile → Neutre, **si Q1-B, déclarée, est inscrite et que son interprétation est confirmée** | QO-01, Q1-B |
| P-02 | La bataille commence au tour 1, phase du premier camp. Le numéro de tour augmente de 1 quand la phase du dernier camp se termine, au retour au premier | QO-02 |
| P-03 | La récupération applique la formule de MEC-0004, sans la modifier, aux unités d'un camp, une fois par manche, au moment fixé par QO-04 : au moins aux unités aptes ; le cas des unités inaptes relève de QO-08. Les unités des autres camps ne sont pas modifiées | QO-04, QO-08, QO-10 |
| P-04 | Pendant la phase d'un camp `joueur`, le joueur sélectionne librement une unité apte de ce camp. Il la déplace selon MEC-0003, peut changer d'unité à tout moment et revenir à une unité déjà déplacée tant que ses ressources le permettent | QO-05 |
| P-05 | Une unité d'un autre camp, ou inapte, n'est pas sélectionnable ; une demande de sélection est refusée sans modifier l'état | QO-08 |
| P-06 | Quand le camp du joueur a au moins une unité apte, sa phase se termine **explicitement**, comme la fin de tour de MEC-0004. Aucune fin automatique dans ce cas | QO-06 |
| P-07 | Un camp sans unité apte voit sa phase passée automatiquement, sans action. Elle compte dans l'ordre des phases. Pour le camp du joueur, c'est une **exception à P-06**, à valider en tant que telle | QO-06, QO-09 |
| P-08 | En l'absence d'IA validée, la phase d'un camp `automatique` est jouée par un contrôleur **sans action**, qui la termine immédiatement. Ce n'est pas une IA ; mais ce contrôleur est **lui-même un comportement provisoire, non validé**, à décider comme tel | QO-12, QO-13 |
| P-09 | Occupation des cases : une unité ne peut ni traverser ni atteindre une case occupée par une autre unité consciente (S10, Q5.2) ; un corps mort ou inconscient ne bloque pas (ARB-B). Le calcul ne tient compte que des occupants **connus du camp** (G4) ; la rencontre d'un occupant inconnu relève de QO-16. Le contrôle de volume entre unités (G1, ARB-A) n'est **pas** couvert par cette proposition (QO-17). **À valider explicitement**, car cela fait entrer dans le périmètre des sous-décisions d'une fiche reportée | QO-07, QO-16, QO-17, S10, ARB-B, G4 |
| P-10 | Une unité seule, sans autre unité sur la carte, obtient exactement les mêmes zones, chemins et coûts que MEC-0003 | MEC-0003 |
| P-11 | La logique des camps, des phases et de la récupération appartient à `Bastion.Simulation`. Le client Godot ne fait qu'afficher et transmettre les commandes | MEC-0004 §7 |

**Hors de cette proposition :** combat, réactions et surveillance (ARB-E), visibilité par camp, IA, initiative, conditions de fin de bataille, statuts détaillés et réveil (G2), interactions physiques de MEC-0002, contrôle de volume entre unités (G1, ARB-A ; QO-17), rencontre d'occupants inconnus (QO-16), et emprises différentes par unité (QO-11).

## 7. Impacts techniques et risques

**Impacts [INSP et PROP] :**
- **Nouveau modèle :** un espace de noms dédié, par exemple `Bastion.Simulation.Battle`. Il porterait des types immuables pour l'identité d'unité, le camp, l'unité, l'état de bataille et les règles de bataille, ces dernières réutilisant `TurnRules`. L'existant n'est pas changé : `TurnState` et le scénario 4 restent ceux de MEC-0004 (QO-15).
- **Récupération :** réutiliser la formule de `TurnRules` sans la dupliquer. Aujourd'hui, `CappedSum` est privée et `EndTurn` prend un `TurnState`. Une méthode de récupération pour un `UnitState` serait à ajouter **sans changer le comportement** de MEC-0004, et à justifier dans le mandat d'implémentation.
- **Marche et occupation (P-09) :** `ComputeReachability` et `ExecuteOrder` ne connaissent que la carte. Il faudrait leur fournir les cases occupées, par exemple par une surcharge qui accepte un ensemble d'occupants, en gardant les signatures actuelles pour MEC-0003 (P-10). Le contrôle de volume entre unités (G1) est un chantier distinct et plus lourd.
- **Client Godot :** sélection d'une unité par clic, affichage du camp et de la phase, commande de fin de phase, et probablement un scénario 5. La scène ne devrait plus garder deux sources d'état synchronisées à la main (RG-08).

**Risques de régression :**

| Risque | Garde proposée |
|---|---|
| Changement du comportement de la marche pour une unité seule | Les 44 tests de `Movement/`, qui sont ceux de MEC-0003, inchangés ; tests d'équivalence P-10 |
| Changement de MEC-0004 : formule, compteur, scénario 4 | Les 19 tests de `Turns/` et les contrôles fumée du scénario 4, inchangés |
| Confusion d'identité : `UnitState` est un `record`, et deux états égaux paraissent la même unité | Identité séparée ; test de deux unités aux états égaux |
| États non validés dérivés par `with` | Validation de l'état de bataille à sa création et à chaque transition (TJ-22) |
| Récupération appliquée au mauvais camp, ou deux fois | Tests par camp et par manche |
| Coût du calcul de zone avec occupants | Mesure sur une carte de test ; pas d'optimisation prématurée |
| Divergence entre l'état affiché et l'état du moteur | Une seule source d'état dans la scène |
| Introduction implicite de règles non validées (IA, réactions) | Relecture du diff contre la fiche. Le contrôleur « sans action » (P-08) ne protège que s'il est lui-même validé : à défaut, les phases non jouées ne doivent pas être implémentées |

## 8. Matrice de tests prévisionnels

Ces tests ne sont **ni écrits ni validés**. Leurs résultats attendus dépendent des décisions indiquées.

| ID | Situation | Résultat attendu (si la proposition est retenue) | Dépend de |
|---|---|---|---|
| TJ-01 | Trois camps, Joueur → Hostile → Neutre ; trois fins de phase | Phases dans l'ordre ; retour au Joueur au tour 2 | P-01, P-02, Q1-B (déclarée) |
| TJ-02 | Fins de phase successives sur plusieurs manches | Le tour n'augmente qu'au retour au premier camp | P-02 |
| TJ-03 | Camp sans unité apte | Phase passée automatiquement, comptée dans l'ordre | P-07 |
| TJ-04 | Phase d'un camp `automatique`, sans IA | Phase terminée sans aucun changement d'unité, hors récupération éventuelle | P-08 |
| TJ-05 | Sélection d'une unité apte du camp actif | Acceptée | P-04 |
| TJ-06 | Sélection d'une unité d'un autre camp ou inapte | Refusée, état inchangé | P-05 |
| TJ-07 | Déplacer A, sélectionner B, déplacer B, revenir à A | Ressources de A conservées ; A peut encore se déplacer dans la limite de ses ressources | P-04 |
| TJ-08 | Récupération | Formule de MEC-0004 appliquée à chaque unité apte du camp concerné, une seule fois par manche, au moment fixé | P-03, QO-04 |
| TJ-09 | Récupération d'un camp | Les unités des autres camps sont inchangées | P-03 |
| TJ-10 | Unité inapte | Récupération ou non, selon la décision ; P-03 ne la fixe pas | QO-08 |
| TJ-11 | Destination occupée par une unité consciente connue du camp | Ordre refusé, état inchangé | P-09, S10 |
| TJ-12 | Chemin passant par une case occupée par une unité consciente connue du camp | Chemin contournant, ou refus si aucun chemin | P-09, S10, G4 |
| TJ-13 | Case occupée par un corps mort ou inconscient | Traversable et atteignable | P-09, ARB-B |
| TJ-14 | Une seule unité sur la carte | Zones, chemins et coûts identiques à MEC-0003 | P-10 |
| TJ-15 | Deux unités aux états égaux | Restent deux unités distinctes | identité |
| TJ-16 | Toute transition | Rend un nouvel état ; l'état d'entrée est inchangé | immutabilité |
| TJ-17 | Paramètres invalides : liste de camps vide, camp en double, unité sans camp connu | Refus explicite | — |
| TJ-18 | Même suite d'entrées, deux fois | Même suite d'états | déterminisme |
| TJ-19 | Pas de fin de phase demandée | La phase ne se termine pas d'elle-même | P-06 |
| TJ-20 | Non-régression | 65 tests .NET, 120 contrôles fumée et scénarios 1 à 4 inchangés | — |
| TJ-21 | Unité dont il reste des TU à la fin de sa phase, puis phase adverse | Si QO-04 retient (a) ou (c) : TU restantes conservées pendant la phase adverse (ES-09). Si QO-04 retient (b) : TU déjà récupérées à la fin de la phase du joueur, et l'articulation avec ES-09 est à réexaminer | QO-04, ES-09 |
| TJ-22 | État initial de bataille invalide : ressources hors plafond, deux unités conscientes sur une même case, unité sur une case infranchissable ou hors carte | Refus explicite, sans état créé | P-09, MEC-0004 §3.2 |
| TJ-23 | Ordre de déplacement donné à une unité hors du camp actif | Refusé, état inchangé | P-04, P-05 |
| TJ-24 | Demande de fin de phase pendant la phase d'un camp `automatique` | Refusée ou sans effet, selon la décision sur les phases non jouées | P-06, P-08, QO-12 |
| TJ-25 | Chemin qui rencontre une unité cachée, inconnue du camp | Selon QO-16 : interruption, révélation, pas non commencé non débité | QO-16, S8, S11 |
| TJ-26 | Diagonale qui longe une unité consciente voisine | Selon QO-17 : avec (a), admise si le volume passe et refusée sinon (G1) ; avec (b), aucun contrôle de volume entre unités, ce qui suppose la dérogation à G1 et à ARB-A décidée explicitement. Jamais de refus automatique au seul motif de la voisine (S4, G1) | QO-17, G1, ARB-A, S4 |
| TJ-27 | État initial avec deux unités de même identifiant | Refus explicite | identité |
| TJ-28 | Camp du joueur sans unité apte au début de sa phase | Phase passée automatiquement, si l'exception P-07 est retenue ; sinon selon la décision | P-06, P-07, QO-06, QO-09 |

## 9. Proposition de fiche de mécanique — identifiant à confirmer

**Identifiant proposé : `MEC-0005`.** Il est libre au registre à `364b46a` : seules MEC-0001 à MEC-0004 existent. **Cette fiche n'est pas inscrite**, et ce dossier ne l'inscrit pas.

```markdown
### MEC-0005 — Plusieurs unités et alternance des camps (proposition)

| Champ | Valeur |
|---|---|
| Système | Combat tactique : enchaînement des phases des camps et activation de plusieurs unités. |
| Description | Plusieurs unités, chacune rattachée à un camp, sur une carte. Les camps jouent tour à tour leur phase ; le joueur active ses unités pendant sa phase ; les ressources sont récupérées selon MEC-0004. |
| Classe | `MODIFICATION-PROPOSEE`. |
| Fonctionnement de référence et preuves | Règles propres à Bastion. Q1-B déclarée validée par le propriétaire, non vérifiable indépendamment ; si le propriétaire décide de l'inscrire, avec sa provenance (dossier LOT-1J, §3). Description d'OXCE par l'étude LOT-2L, non publiée et hors dépôt : information seulement, aucune fidélité revendiquée. |
| Changement demandé | Proposition P-01 à P-11 du dossier LOT-1J, après décision sur QO-01 à QO-17. |
| Décision du propriétaire | non encore soumise : ni acceptée, ni refusée, ni reportée. |
| Périmètre autorisé | Aucun, tant que la fiche n'est pas acceptée. |
| Éléments exclus | Combat, réactions, surveillance, visibilité par camp, IA, initiative, fin de bataille, réveil (G2), volume entre unités (G1, ARB-A), occupants inconnus, MEC-0002, et toute règle non décrite. |
| Tests de référence | Aucun : aucune fidélité à OXCE revendiquée. |
| Tests de modification | TJ-01 à TJ-28 du dossier LOT-1J, prévisionnels. |
| État d'implémentation | non commencé |
```

## 10. Limites et réserves

- **Q1-B est déclarée, non vérifiable indépendamment, et non inscrite.** Son interprétation (ordre, sens d'« autonome », portée de « selon le modèle OXCE ») reste à confirmer. Si une autre organisation des camps était retenue, P-01, P-02 et TJ-01 changeraient.
- **LOT-2L n'est pas dans le dépôt.** C'est un fichier de la session : `scratchpad/lot2l/LOT-2L-FONDATIONS-TACTIQUES.md`, de SHA-256 `419ec107f493285467eba0419ed1b69f786dc2a3dc523a6a58e61bd86c5f5702`. Ses descriptions d'OXCE viennent d'une lecture du code, sans exécution.
- **P-09, l'occupation, fait entrer S10 et ARB-B dans un périmètre d'implémentation.** Ces sous-décisions appartiennent à MEC-0001, reportée. Il faut une décision explicite pour les appliquer dans une nouvelle fiche sans valider MEC-0001.
- **Les impacts techniques sont des estimations**, établies par lecture du code ; aucun prototype n'a été écrit.
- **Aucun test n'est écrit ni exécuté** pour ces propositions.
- **CI :** rien n'est poussé.

## 11. Vérifications

Commandes lancées dans le dépôt de travail ; toutes renvoient le code 0.

| Vérification | Résultat |
|---|---|
| `git fetch origin main` ; `git rev-parse origin/main HEAD` | `364b46acc486fa723ba1787c6e4b01e9a3537678` deux fois ; arbre propre avant le lot |
| `git status --short -uall` | `M docs/mandates/README.md` ; `?? docs/mandates/BASTION-MANDAT-LOT-1J-v1.0-transcription.md` ; `?? docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md` |
| `git diff --stat origin/main -- src tests docs/gameplay docs/decisions docs/references .github scripts .claude CLAUDE.md README.md` | aucune sortie : ni code, ni test, ni registre, ni harnais modifiés |
| Empreintes de l'index, recalculées pour chaque entrée | 24 concordantes, 0 écart ; aucun fichier de `docs/mandates/` absent de l'index |
| `bash scripts/harness/test-hooks.sh` | « == 75 tests, 0 échec(s) == » |
| `dotnet format --verify-no-changes` | aucune sortie |
| `dotnet build` ; `dotnet test --no-build` | 0 Warning(s), 0 Error(s) ; « Passed! - Failed: 0, Passed: 65 » |
| `dotnet test --no-build --list-tests` | 65 tests ; la répartition 44 + 2 + 19 vient de la relecture (§12) |

**Archive du mandat (RJ-19).** Le fichier est le texte du message du propriétaire du 2026-11-27T13:36:01Z, extrait mécaniquement du journal de session, auquel un saut de ligne final est ajouté, comme pour les transcriptions précédentes. Il compte 2 064 octets. Son SHA-256 est `747c402c344dcbc68eec13f9e262e75decb20055e716e559ff2b85795e3920b3`, et `c0cccbd64521dbe35289725884796ab03e305e0e75e40244612cc6bc9caa9b23` sans ce saut de ligne final.

**Fichiers du lot :**
- `docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md`, nouveau : ce dossier ;
- `docs/mandates/BASTION-MANDAT-LOT-1J-v1.0-transcription.md`, nouveau : le mandat ;
- `docs/mandates/README.md` : une ligne d'index ajoutée.

Le contrôle de traçabilité de la CI (`check-simulation-trace.sh`) ne s'applique pas, puisqu'aucun fichier de `src/Bastion.Simulation/` n'est modifié. Le contrôle fumée Godot n'est pas relancé, puisqu'aucun code n'est modifié.

## 12. Relecture indépendante ciblée

Un agent distinct de l'auteur a relu le dossier en lecture seule, en trois temps :
1. une relecture complète (RJ-01 à RJ-19) ;
2. la vérification des corrections et de la note de traçabilité Q1-B (RJ-20 à RJ-30) ;
3. la vérification des corrections RJ-20 à RJ-30 (RJ-31, RJ-32).

Il a refait lui-même les recherches sur Q1-B, plus largement que l'auteur, et lancé les contrôles dans une copie neuve. Son rapport est reproduit ci-dessous sans modification, entre deux filets : c'est une **version intermédiaire** du fichier `relecture-1j/relecture.md` du dossier temporaire de la session, de SHA-256 `882798f7560309e775e09acac3c7f99948c143d1ed4bf53f9caebc1b51f004b0`, conservée telle quelle dans `relecture-1j/relecture-882798f7.md`. Le rapport s'est poursuivi ensuite par une relecture finale ciblée (voir l'annexe). Les numéros de ligne qu'il cite renvoient aux versions successives qu'il a relues.

---

# Relecture indépendante : dossier de conception LOT-1J (plusieurs unités et alternance des camps)

- **Date :** 2026-11-27, terminée à 13:56 UTC.
- **Objet :** `docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md` (désigné « D » ci-dessous), l'archive du mandat et son entrée d'index. §11, §12 et l'annexe (marqueurs `<<…>>`) ne sont pas relus.
- **Relecteur :** agent distinct de l'auteur, en lecture seule. Il ne s'accorde pas la validation finale, qui appartient au propriétaire.
- **Base :** branche `claude/lot-1j-conception-camps`, HEAD = `origin/main` = `364b46acc486fa723ba1787c6e4b01e9a3537678`.
- **Abréviations :** R = `docs/gameplay/GAMEPLAY-DECISIONS.md` ; L = `scratchpad/lot2l/LOT-2L-FONDATIONS-TACTIQUES.md` ; J = journal `/root/.claude/projects/-home-user/7361641c-….jsonl`.

**État relu (SHA-256), identique au début et à la fin de la relecture :**

| Fichier | SHA-256 |
|---|---|
| `docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md` | `cd652a352d2c2f792d15128087a542ae070421c7b75dff83f9bf20681b86044e` |
| `docs/mandates/BASTION-MANDAT-LOT-1J-v1.0-transcription.md` | `747c402c344dcbc68eec13f9e262e75decb20055e716e559ff2b85795e3920b3` |
| `docs/mandates/README.md` (de travail ; sur `main` : `c34e6718…`) | `c8c8cedef0b15de0523df0becdf0ccf65b3339a87c0941cee58ad06d1bf6724a` |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` (identique à `main`) | `6e5d13cccb07c9b0bd67e520868f85e33057f4b02c5ce9f42df7323423abf16d` |
| LOT-2L (hors dépôt) | `419ec107f493285467eba0419ed1b69f786dc2a3dc523a6a58e61bd86c5f5702` |

## 1. Méthode

1. J'ai lu `CLAUDE.md`, le mandat, l'index, D, les fiches MEC-0001 à MEC-0004, le code de `Movement/` et de `Turns/`, les tests et LOT-2L.
2. J'ai refait seul les recherches sur Q1-B, plus largement que l'auteur : toutes les références distantes, tout l'historique, les deux journaux de la session, les réponses aux questions posées au propriétaire, et les fichiers téléversés.
3. J'ai confronté chaque affirmation de D §2 et §4 au code et au registre, ligne par ligne.
4. J'ai recalculé mécaniquement l'archive et les empreintes de l'index.
5. J'ai lancé les contrôles dans une copie neuve, sans `.git`, `bin`, `obj` ni `.godot`.

Je n'ai lancé aucun `git fetch`. `git ls-remote` montre que les 59 références distantes, têtes de PR comprises, étaient déjà présentes localement. Le dépôt réel n'a pas été modifié.

## 2. Commandes exécutées

| # | Commande (résumé) | Résultat | Code |
|---|---|---|---|
| C1 | `git status --porcelain -uall` (début et fin) | 3 entrées seulement : ` M docs/mandates/README.md`, `?? …LOT-1J-v1.0-transcription.md`, `?? docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md` | 0 |
| C2 | `git diff --quiet 364b46a -- docs/gameplay docs/decisions docs/references src tests .claude scripts .github CLAUDE.md` ; `git diff --stat 364b46a` | aucune différence ; seul `README.md` change, d'une ligne ajoutée | 0 |
| C3 | `git ls-remote origin`, puis comparaison avec les références locales | 59 références ; toutes les têtes et toutes les PR sont présentes localement | 0 |
| C4 | `git grep -I -i -E` sur les 31 commits distincts (têtes et PR). Motifs : `Q1-B`, `Q1B`, `Q1 B`, `trois camps`, `Joueur → Hostile`, `Hostile → Neutre`, `phase neutre`, `camp neutre`, `neutre autonome`, `Joueur -> Hostile`, `Player.*Hostile.*Neutral` | 0 fichier pour chaque motif | 0 |
| C5 | `git log --all -S` pour cinq de ces motifs ; `git grep` sur les branches locales | aucun commit, aucune occurrence | 0 |
| C6 | `grep` de Q1-B dans tous les `*.jsonl` de `/root/.claude/projects/` | J seulement, à partir de la ligne 9366 (le mandat), et mon propre journal de sous-agent. L'ancien journal `-home-user-bastion` (8 au 16 novembre) : 0 occurrence de « Q1-B », « trois camps » ou « LOT-2L » | 0 |
| C7 | Réponses du propriétaire aux questions de Claude Code (`toolUseResult.answers`) dans les deux journaux | 14 + 4 réponses ; aucune ne tranche les camps. Seules J:7465 (texte de MEC-0004 v1.2) et J:9396 (autorisation LOT-1J) mentionnent les camps | 0 |
| C8 | `grep -E 'Q1-B\|trois camps\|phase neutre\|…'` dans `/root/.claude/uploads/` | aucune correspondance | 1 (aucune ligne trouvée) |
| C9 | Extraction Python de J:9366 et J:9368 ; `sha256` ; `cmp` de l'archive avec le message suivi d'un LF | message de 2 063 octets, SHA `c0cccbd6…9b23` ; message + LF = `747c402c…20b3` ; archive identique | 0 |
| C10 | Autorisation dans J:9396 | 2026-11-27T13:40:13.287Z ; options « Autoriser, dossier dans le dépôt (Recommandé) » et « Non vérifiée, à qualifier (Recommandé) » | — |
| C11 | Empreintes de toutes les lignes de l'index | 24 lignes, 24 concordantes ; aucun fichier non indexé | 0 |
| C12 | Décompte de `[Fact]`, `[Theory]` et `[InlineData]` à `364b46a` | `Movement/` : 4 + 5 + (14 + 10) + 11 = **44** ; `SmokeTests.cs` : 2 ; `Turns/TurnTests.cs` : 19 ; total 65 | 0 |
| C13 | `gh api` : PR #28, ses exécutions de CI et les journaux des jobs 140532218210 (PR) et 140535135416 (push sur `main`) | PR fusionnée, tête `5b8905c`, fusion `364b46a`. Chaque job : `Passed: 65, Failed: 0`, 120 lignes `SMOKE OK`, 0 échec, `SMOKE : RÉUSSITE` | 0 |
| C14 | Copie neuve par `tar` | 199 fichiers | 0 |
| C15 | Copie neuve : `bash scripts/harness/test-hooks.sh` | `== 75 tests, 0 échec(s) ==` | 0 |
| C16 | Copie neuve : `dotnet format --verify-no-changes` (SDK 10.0.115) | aucune sortie | 0 |
| C17 | Copie neuve : `dotnet test` (en plus de ce qui était demandé) | `Passed: 65, Failed: 0, Total: 65` | 0 |
| C18 | Fichiers relus : BOM, CR, espaces finaux (`grep -P '[ \t]$'`), dernier octet ; `git diff --check` | ni BOM ni CR ; aucun espace final ; LF final | 0 |
| C19 | `git grep MEC-0005` sur `main` et sur les 31 commits distants | aucune occurrence ; seul D l'emploie | 0 |

Note sur C18 : un premier essai avec `grep -E '[ \t]+$'` signalait à tort « Objet ». En ERE, `\t` entre crochets désigne `\` et `t`. Le contrôle avec `-P` fait foi.

## 3. Points vérifiés conformes

**Mandat, sept points.** Tous les points sont couverts :

| Point | Où dans D | Vérification |
|---|---|---|
| 1. Architecture | §2 | inspecté seulement |
| 2. Provenance de Q1-B | §3 | exécuté et réussi (C4 à C8) |
| 3. Règles acquises et décisions nécessaires | §4 et §5 | couverture incomplète, voir RJ-10 |
| 4. Points d'étude | voir ci-dessous | inspecté seulement |
| 5. Spécification minimale | §6 | inspecté seulement |
| 6. Tests et risques | §7 et §8 | inspecté seulement |
| 7. Fiche à identifiant à confirmer | §9 | inspecté seulement |

Pour le point 4 :
- sélection et activation : QO-05, P-04, P-05 ;
- tour, phase et activation : QO-03 ;
- passage d'une unité à une autre : P-04, TJ-07 ;
- récupération : QO-04, QO-10, P-03 ;
- unités incapables d'agir : QO-08, P-05 ;
- phases des camps sans unité active : QO-09, P-07 ;
- articulation avec une IA : QO-12, QO-13, P-08.

**Contraintes.** Toutes sont respectées (exécuté et réussi, C1, C2, C19) :
- aucun code ni test ;
- registre identique à `main` ;
- MEC-0003 et MEC-0004 non modifiées ;
- MEC-0001 et MEC-0002 non implémentées ;
- rien n'est commité.

**Q1-B.** La qualification « non vérifiée » est justifiée (exécuté et réussi, C4 à C8) : aucune trace dans Git, dans les deux journaux, dans les réponses du propriétaire ni dans les fichiers téléversés.

D ne présente Q1-B comme acquise nulle part (inspecté) :
- D:26, D:79-105 et D:129 la marquent [NV] ;
- D:135 (« à valider »), D:164 (« si Q1-B est validée »), D:204, D:238 et D:250 la traitent comme conditionnelle.

Les descriptions de LOT-2L reprises en D:87-95 sont exactes (L:26, L:85-88, L:177-184, L:189). L'absence de « phase neutre autonome » et de « autonome » dans L est exacte.

**Code (§2), inspecté seulement sauf mention contraire.** Les points suivants sont exacts :
- `UnitState` est un `record` scellé, au constructeur interne (`UnitState.cs:7`, `:9`).
- L'égalité de `record` porte sur des types à valeur (`GridPosition` est un `record struct`, `Direction` une énumération). Elle est même utilisée par un test qui passe (`SearchAndExecutionTests.cs:157-163`, exécuté et réussi par C17).
- La signature de `MovementModel` et ses quatre opérations sont celles décrites (`MovementModel.cs:15`, `:65`, `:96`, `:107`, `:132`).
- `TacticalMap` ne connaît que le terrain, les cases bloquées et les murs ; aucune occupation (`TacticalMap.cs:15`).
- `TurnRules` : profil `Initial` (60, 60, 100, 20) en `:30`, `Start`, `WithUnit` et `EndTurn` en `:44`, `:50`, `:61`, `CappedSum` privée en `:74`.
- `TurnState` porte une seule unité (`TurnState.cs:9-20`) ; `TurnOutcome` est en `:24`.
- La double source d'état de la scène est exacte (`PrototypeScene.cs:59`, `:68`, `:287-310`) ; RG-08 figure dans `LOT-1G-IMPLEMENTATION-MEC-0004.md:525`.

Les chiffres « 65 = 46 + 19 » et « 120 contrôles » sont exacts (exécuté et réussi, C12, C13, C17).

**Registre (§4), inspecté.** Les citations suivantes sont exactes :

| Règle | Ligne de R |
|---|---|
| S10 | 80 |
| ARB-B | 122 |
| G2 | 135-138 |
| S4, ARB-A, G1 | 74, 121, 128-129 |
| ARB-D | 124 |
| Q3.6 | 213 |
| renvoi par MEC-0004 | 643, 658-659 |
| ARB-E | 125 |
| Q4.14 | 229 |
| ES-07 | 376 |
| ES-09 | 378 |
| SA-03, SA-08 | 307, 312 |
| S6 à S12 | 76-82 |
| exclusion « renouvellement des TU » de MEC-0002 | 278 |
| MEC-0004 §5 | 798-800 |
| « Aucune fin de tour automatique » | 726 |
| hors périmètre de MEC-0003 | 578 |

MEC-0005 est libre (exécuté et réussi, C19).

**OXCE.** D n'affirme aucune fidélité (D:97, D:238, D:243). Le commit cité est celui de `docs/references/OXCE-BASELINE.md:13`.

**Archive et index.** Exécuté et réussi (C9 à C11) :
- l'archive est mécaniquement égale au message suivi d'un LF, convention des lots 1H et 1I ;
- les horodatages 13:36:01 et 13:40:13 UTC, l'option citée, la citation finale « Ce mandat est une proposition de cadrage… » et l'empreinte de l'index sont exacts ;
- les 24 empreintes de l'index concordent.

## 4. Constats

Aucun constat n'est bloquant. Les constats RJ-01 à RJ-12 sont à corriger ; RJ-13 à RJ-19 sont des observations.

### RJ-01 — À corriger — Le dossier décrit des recherches plus larges que celles réellement faites

**Preuve.** D:83-86 annonce « Branches distantes, dont `orchestration/mandats` : aucune occurrence » et « Journal de session : la seule occurrence est le mandat ». Les commandes de l'auteur, dans le journal, montrent une couverture plus étroite :
- J:9371 et J:9375 : `git grep` sur `origin/main -- docs` ;
- J:9382 : `git grep` sur la seule branche `origin/orchestration/mandats`, avec quatre motifs ;
- J:9391 : messages texte de J seulement, sans les résultats d'outils (réponses du propriétaire), sans l'ancien journal `-home-user-bastion` et sans les fichiers téléversés.

L'étiquette « [INSP, commandes exécutées] » mêle deux états. La conclusion reste juste : C4 à C8 couvrent tout cela, sans trace.

**Correction.** Décrire exactement l'étendue des recherches, ou citer celle de C4 à C8. Mettre les commandes et leur sortie au §11.

### RJ-02 — À corriger — L'homonymie de « Q1 » n'est pas signalée

**Preuve.** Dans le registre, « Q1 » désigne la géométrie de MEC-0001 (Q1.1 à Q1.9, R:164 et suivantes). Les « options B » de Q1.1 à Q1.4 existent (R:154 ; pièce `PIECE-Q1.1-Q1.4-OPTIONS-B.md`), et « Q1.5 (option B) » figure dans la consolidation v0.3, à la ligne 82. LOT-2L, lui, note ses options en minuscules, « (b) » (L:182).

La déduction de D:100 est plausible par le contenu, mais l'identifiant « Q1-B » est ambigu.

**Correction.** Ajouter au §3 une phrase qui signale cette homonymie et dit pourquoi elle est écartée par le contenu (la géométrie, non les camps).

### RJ-03 — À corriger — P-09 suppose que toute l'occupation est connue, sans le dire

**Preuve.** P-09 (D:172) et TJ-11 à TJ-13 (D:214-216) rendent une case occupée infranchissable dans le calcul de la zone et du chemin. Or :
- G4 impose de choisir le chemin selon « les informations connues du camp (S6 à S9, et non la vérité cachée) » (R:142) ;
- S8 et S11 interrompent ou révèlent en cours de marche (R:78, R:81).

Avec une unité cachée, P-09 calculerait donc sur la vérité cachée. La visibilité est exclue (D:153, D:176), mais l'hypothèse « toutes les unités sont connues du camp actif » n'est écrite nulle part.

**Correction.** L'écrire comme hypothèse explicite à valider, avec une restriction des scénarios ou une nouvelle question, et l'ajouter aux limites.

### RJ-04 — À corriger — P-09 ne dit rien de G1 et d'ARB-A entre unités

**Preuve.** MEC-0003 applique déjà ARB-A et G1 par renvoi (R:493). G1 exige que le volume « puisse emprunter un passage sans traverser celui d'une autre unité consciente » (R:128-129).

D:183 qualifie ce contrôle de « chantier distinct ». Pourtant ni le hors-périmètre du §6 (D:176) ni les exclusions de la fiche (D:242) ne citent G1 ou ARB-A. Implémenter S10 sans ce contrôle admettrait des diagonales que G1 refuse.

**Correction.** Le traiter explicitement : l'appliquer, ou poser une question ou une exclusion qui demande une décision, comme le fait QO-07 (b).

### RJ-05 — À corriger — P-09 et TJ-13 n'emploient pas le vocabulaire d'ARB-B

**Preuve.** D:172 et D:216 parlent d'unités « apte » ou « inapte ». S10 et ARB-B parlent d'une « autre unité » et d'un « corps mort ou inconscient » (R:80, R:122). Or le statut « inapte » reste « à préciser par QO-08 » (D:157) : il pourrait couvrir des états conscients, et P-09 exempterait alors de S10 une unité consciente.

**Correction.** Écrire « bloquée par toute autre unité, sauf un corps mort ou inconscient (ARB-B) ».

### RJ-06 — À corriger — P-08 est présenté comme une garde alors qu'il est lui-même un comportement non validé

**Preuve.** D:171 affirme qu'« aucune règle de comportement n'est proposée ». Pourtant des camps qui n'agissent jamais forment un comportement de jeu provisoire. Le tableau des risques en fait une « garde » contre l'introduction de règles non validées (D:196), ce qui est circulaire. `CLAUDE.md` §3 rappelle qu'une simplification temporaire n'échappe pas à la décision.

**Correction.** Présenter P-08 comme un comportement provisoire soumis à QO-12, et retirer P-08 de la colonne « Garde ».

### RJ-07 — À corriger — P-06 et P-07 se contredisent pour le camp du joueur

**Preuve.** P-06 dit « Aucune fin automatique » (D:169). P-07 passe automatiquement la phase d'un camp sans unité apte (D:170), ce qui inclut le joueur. TJ-19 et TJ-03 sont touchés de la même façon.

**Correction.** Restreindre P-07, ou en faire une exception explicite à P-06, liée à QO-06 et QO-09.

### RJ-08 — À corriger — TJ-21 préjuge de QO-04

**Preuve.** TJ-21 attend des « TU conservées pendant la phase adverse » (D:224). Avec l'option (b) de QO-04, une récupération à la fin de la phase du camp de l'unité, ses TU seraient déjà augmentées au début de la phase adverse.

**Correction.** Rendre le résultat conditionnel à QO-04, en écartant l'option (b), ou le formuler de façon neutre.

### RJ-09 — À corriger — Le décompte des tests de `Movement/` est faux

**Preuve.** D:190 parle des « 46 tests de `Movement/` ». `Movement/` compte 44 cas ; les 2 autres sont les tests techniques de `SmokeTests.cs:12` et `:20` (C12). D:67 donne le bon décompte.

**Correction.** Écrire « les 44 tests de `Movement/` et les 2 tests techniques ».

### RJ-10 — À corriger — Le §4 omet des règles déjà décidées

**Preuve.** Le §4 ne cite pas :
- **G4** (R:142) : « informations connues du camp ». C'est la seule règle qui fait déjà du camp le détenteur de la connaissance ; elle concerne QO-13. D:109 l'omet aussi.
- **SA-04** (R:308) : « Un ennemi actuellement visible peut être ciblé malgré S10 ». Elle concerne QO-14 et S10.
- **Q5.2** (R:203) : chaque unité consciente occupe un emplacement distinct, et « aucune superposition volontaire » n'est admise. Elle concerne P-09 et TJ-17.
- **Q1.2** (R:166) : « Dimensions configurables par type d'unité et posture », appliquée par MEC-0003 (R:498). QO-11 (D:145) propose pourtant une « emprise commune » sans la citer.

**Correction.** Ajouter ces lignes au §4 et reformuler QO-11.

### RJ-11 — À corriger — Une phrase du §1 attribue les corps à G1

**Preuve.** D:27 écrit « G1, des corps inconscients ou morts ». G1 porte sur le passage diagonal près d'unités conscientes (R:126-133) ; les corps relèvent d'ARB-B.

**Correction.** Reformuler la phrase.

### RJ-12 — À corriger — La matrice de tests a des manques et une incohérence

**Manques :**
- (a) la validation de l'état initial : deux unités conscientes sur une même case (S10, Q5.2), un identifiant d'unité en double, une unité sur une case bloquée ou hors de la carte ;
- (b) un ordre de marche donné à une unité hors du camp actif ou non sélectionnée (TJ-06 ne couvre que la sélection) ;
- (c) une fin de phase demandée pendant la phase d'un camp automatique ;
- (d) P-07 appliqué au camp du joueur, voir RJ-07 ;
- (e) un occupant caché, à placer au moins en cas exclu, voir RJ-03 ;
- (f) une diagonale près d'une unité consciente, voir RJ-04.

**Incohérence :** P-03 limite la récupération aux unités aptes (D:166), alors que TJ-10 dit « selon la décision » (D:213).

### RJ-13 — Observation — `UnitState` peut être dérivé sans validation

**Preuve.** Les propriétés `init` sont publiques (`UnitState.cs:17-23`). Une expression `with` crée donc, hors de l'assembly, un état non validé ; les tests le font eux-mêmes (`TurnTests.cs:163-164`). « Un état se crée par `CreateState` » (D:43) est incomplet.

**Correction.** Le signaler : l'état de bataille devra valider lui-même les unités qu'il reçoit (TJ-17).

### RJ-14 — Observation — « donc par carte » est inexact

**Preuve.** D:52 écrit « une seule `UnitBody` par modèle, donc par carte ». Plusieurs modèles peuvent partager une même carte, car la carte est un argument du constructeur (`MovementModel.cs:15`). La conclusion « un modèle par type » reste juste.

### RJ-15 — Observation — L'état de bataille n'a pas d'unité sélectionnée

**Preuve.** L'état de bataille ne porte ni « unité sélectionnée » ni « unité active » (D:158). Pourtant P-04, P-05 et TJ-05 à TJ-07 parlent d'une sélection qui change, ou ne change pas, l'état.

### RJ-16 — Observation — Le découpage par phase de camp est présupposé

**Preuve.** QO-01 et la description de la fiche (D:236) supposent des phases par camp. LOT-2L Q2 posait aussi la question du « découpage (par camp, par unité, autre) » (L:188-192). Une option est à ajouter dans QO-03 ou QO-01.

### RJ-17 — Observation — Fiche proposée : décision hors gabarit et source non publiée

**Preuve.** « Décision du propriétaire | aucune — proposition à examiner » (D:240) sort des valeurs du gabarit : acceptée, refusée ou reportée (R:37). La fiche cite aussi LOT-2L, non publiée (D:238) : il faudrait l'archiver avant toute inscription.

### RJ-18 — Observation — L'étiquette [REG] masque des niveaux de preuve

**Preuve.** Q4.14 est au niveau [CIT], une formulation résumée par l'orchestrateur (R:155, R:229). Les principes de MEC-0002 reposent sur une preuve déclarative (R:276). L'étiquette [REG] ne montre pas ces nuances.

### RJ-19 — Observation — Ce que §11 et l'annexe devront contenir

Pour être conforme à `CLAUDE.md` §6 (« fichiers, vérifications »), le §11 et l'annexe devraient donner :
- la liste des trois fichiers ;
- la convention de l'archive : message de 2 063 octets, SHA sans LF `c0cccbd64521dbe35289725884796ab03e305e0e75e40244612cc6bc9caa9b23`, archive = message + LF ;
- les commandes exactes et leur code de sortie.

## 5. Non vérifié

- L'existence d'une décision Q1-B hors du dépôt et de la session, par exemple dans un échange avec l'orchestrateur.
- L'identité de la transcription avec un fichier original.
- Les comportements d'OXCE rapportés par LOT-2L : le code d'OXCE n'a pas été relu, l'information est prise de L seulement.
- Les impacts techniques du §7 : aucun prototype n'existe.
- Les contrôles fumée Godot en local : seuls les journaux de CI ont été lus (C13).
- L'exhaustivité des journaux de session.
- Le contenu à venir des §11, §12 et de l'annexe.

## 6. Verdict

**Conforme au mandat et aux contraintes, sous réserve des corrections RJ-01 à RJ-12.** Aucun constat bloquant.

- La qualification de Q1-B est justifiée (exécuté et réussi) ; Q1-B n'est présentée comme acquise nulle part.
- L'archive, l'index et les empreintes sont exacts (exécuté et réussi).
- Les contrôles réussissent (exécuté et réussi) : `test-hooks.sh` (75 tests, 0 échec), `dotnet format --verify-no-changes` (code 0) et `dotnet test` (65 réussis).

Les propositions P-08 et P-09 et les tests qui en dépendent appellent les corrections les plus importantes (RJ-03 à RJ-06) : en l'état, ils s'écartent implicitement de G4, G1 et ARB-B. La validation finale appartient au propriétaire.

## Vérification des corrections et de la note Q1-B

- **Date :** 2026-11-27, terminée à 14:08 UTC.
- **Nature :** vérification ciblée, en lecture seule, et non nouvelle relecture générale. Le relecteur ne s'accorde pas la validation finale.
- **Abréviations :** D = dossier actuel ; Dr = version relue (`scratchpad/lot1j/dossier-relu.md`) ; N = note (`scratchpad/q1b/NOTE-TRACABILITE-Q1-B.md`) ; R = registre ; L = LOT-2L ; J = journal `-home-user`.

**Empreintes (SHA-256) :**

| Fichier | SHA-256 |
|---|---|
| Dr, identique à la version relue plus haut | `cd652a352d2c2f792d15128087a542ae070421c7b75dff83f9bf20681b86044e` |
| D, 309 lignes | `840486f19dfe6e2b5519ba181db356b7b6da3d290402962e90a03d85f2cade42` |
| N, 98 lignes | `ced28d47c19c2027f911848eeb4615fd9e30d63a9e53bea95940d196a4d5ecd0` |
| Archive, inchangée | `747c402c344dcbc68eec13f9e262e75decb20055e716e559ff2b85795e3920b3` |
| Index, inchangé | `c8c8cedef0b15de0523df0becdf0ccf65b3339a87c0941cee58ad06d1bf6724a` |
| Registre, identique à `main` | `6e5d13cccb07c9b0bd67e520868f85e33057f4b02c5ce9f42df7323423abf16d` |
| Message de régularisation du propriétaire (1 940 octets) | `a4507da673bf4876e928d845054d5e8441421ba13516fb700c8d91ae99308ea3` |

### Commandes exécutées

| # | Commande (résumé) | Résultat | Code |
|---|---|---|---|
| V1 | Extraction Python du message « Régularisation documentaire Q1-B » de J | Mis en file à 13:58:24.291Z (J:9487) et remis en cours de tour à 13:58:24.290Z (J:9494, `queued_command`). Origine `{'kind': 'human'}` ; texte identique en J:9493 | 0 |
| V2 | `sha256sum` de Dr et D ; `diff Dr D` | Dr correspond à la version relue ; 33 blocs modifiés, tous examinés | 0 |
| V3 | Comptage mécanique des lignes de tableau de D | 17 lignes QO (QO-01 à QO-17), 26 lignes TJ (TJ-01 à TJ-26), 11 lignes P ; aucun renvoi vers un identifiant inexistant | 0 |
| V4 | Événements du 16 novembre dans les deux journaux | Derniers messages d'origine humaine : 10:24:36, 10:27:06 (refus d'un outil) et 10:27:29.256Z (J:870, validation du mandat LOT-2L). Ensuite, seulement des remises de sous-agents. Dernier événement du jour : 10:54:55 ; reprise le 17 novembre à 13:02:46 | 0 |
| V5 | Dernier message de Claude Code mentionnant LOT-2L le 16 novembre | J:995, 10:54:52.568Z : le rapport LOT-2L, qui annonce « huit questions » | 0 |
| V6 | `grep` de « trois camps », « phase autonome » et « Q1-B » dans les deux journaux | « trois camps » figure en **J:976-977, le 16 novembre à 10:54:21Z** : écriture du fichier LOT-2L et son résultat. « phase autonome » et « Q1-B » n'apparaissent qu'à partir du 27 novembre. Ancien journal : 0 pour les trois motifs | 0 |
| V7 | Commandes de l'auteur dans J (9498, 9504, 9511, 9534) | Journaux : motifs « Q1-B », « Je valide Q1 » et « phase autonome » seulement, **sans « trois camps »**. Fichiers téléversés : « trois camps » inclus | — |
| V8 | Lignes R:117, R:455, R:645 et R:165-169 ; `TurnTests.cs:161-164` ; `MovementModel.cs:35-43` | Citations des précédents exactes. Q1 couvre Q1.1 à **Q1.9**. `T09_NegativeResourcesAreRefused` emploie `with`. `CreateState` refuse les cases hors carte et bloquées | 0 |
| V9 | `git status --porcelain -uall` | ` M docs/mandates/README.md`, `?? …LOT-1J-v1.0-transcription.md`, `?? docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md` | 0 |
| V10 | `git diff --quiet 364b46a --` sur les chemins protégés, puis `git diff --stat` | aucune différence ; seul `README.md` change, d'une ligne | 0 |
| V11 | Copie neuve (`tar`, 199 fichiers), puis `bash scripts/harness/test-hooks.sh` | `== 75 tests, 0 échec(s) ==` | 0 |
| V12 | Contrôle de D : BOM, CR, espaces finaux, LF final | ni BOM ni CR ; aucun espace final ; LF final | 0 |

### Corrections de RJ-01 à RJ-18 (inspecté)

| RJ | État | Preuve dans D |
|---|---|---|
| 01 | corrigé, avec un reste (RJ-27) | D:96-103 : étendue des recherches de l'auteur et de la relecture |
| 02 | corrigé, mais avec une nouvelle inexactitude (RJ-21) | D:123 |
| 03 | corrigé | P-09 limité aux occupants connus (D:208) ; G4 (D:158) ; QO-16 (D:183) ; TJ-11 et TJ-12 (D:251-252) ; TJ-25 ; exclusions (D:212, D:284) |
| 04 | corrigé, mais l'option ajoutée pose problème (RJ-23) | QO-17 (D:184) ; D:149, D:208, D:212, D:284 ; TJ-26 |
| 05 | corrigé | définition du statut (D:193) ; P-09 « consciente » ou « corps mort ou inconscient » ; TJ-13 (D:253) |
| 06 | corrigé | D:207, D:233 |
| 07 | corrigé | P-06 conditionné ; P-07 posé comme exception (D:205-206) |
| 08 | corrigé | TJ-21 conditionnel (D:261) |
| 09 | corrigé | D:77-80, D:226 (44 + 2 + 19) |
| 10 | corrigé en grande partie | G4, Q5.2, Q1.2 et SA-04 ajoutés (D:158-161), mais voir RJ-24 et RJ-27 |
| 11 | corrigé | D:30-34 |
| 12 | corrigé en grande partie | TJ-22 à TJ-26 ; P-03 et TJ-10 rendus cohérents (D:202, D:250) ; restes en RJ-27 |
| 13 | corrigé | D:55, D:229 |
| 14 | corrigé | D:62 |
| 15 | corrigé | D:172, D:194 |
| 16 | corrigé | D:168 |
| 17 | corrigé | D:280, D:282 |
| 18 | corrigé | D:17 |

**Compteurs : exacts** (exécuté et réussi, V3 et C12) :
- dix-sept QO (D:37) ;
- 26 TJ (D:44, D:286) ;
- 44 + 2 + 19 = 65 tests (D:77-80) ;
- « QO-01 à QO-17 » dans la fiche (D:281).

**Traitement de la déclaration : conforme aux consignes** (inspecté, V1). Le message est bien d'origine humaine.

Citations exactes de ce message :
- D:117-119 ;
- N S-7.

Aucune validation présumée dans le dossier :
- l'étiquette [DÉCL] est définie (D:19) ;
- Q1-B est « non vérifiable indépendamment, et non comme une règle acquise » (D:129) ;
- D note l'absence de « preuve primaire » (D:128) ;
- P-01 est subordonnée à l'inscription et à l'interprétation (D:200).

L'option (b) n'est présentée nulle part comme une preuve suffisante :
- D:128 ;
- N l.48.

Deux formulations restent toutefois à resserrer : RJ-22 et RJ-25.

**Note, sources S-1 à S-8 :**

| Source | Résultat | Preuve |
|---|---|---|
| S-1 | exact | |
| S-2 | exact | |
| S-3 | exact | |
| S-4 | exact | |
| S-5 | exact | V4 : 10:27:29 UTC ; rien vers 14:49 UTC, la session était inactive de 10:54:55 au lendemain |
| S-6 | **inexact** | RJ-20 |
| S-7 | exact | V1 |
| S-8 | exact | |

L'heure de 10:54:52 UTC pour le dernier message de Claude Code présentant LOT-2L est exacte (V5).

Écarts du §3 de N :
- 3.1 à 3.4 sont exacts (L:177-185) ;
- 3.5 est inexact (RJ-21).

Précédents du §1 de N : citations exactes (R:117, R:645, R:455), avec une réserve (RJ-29).

Aucune règle n'est inventée. Une seule présomption est formulée comme un fait (RJ-22).

### Constats

**RJ-20 — À corriger (N S-6 ; D:99) — « trois camps » figure dans le journal avant le 27 novembre**
- **Preuve.** N affirme qu'aucune occurrence de « trois camps » n'existe dans les journaux avant le 27 novembre. Or le motif figure en J:976-977, le 16 novembre à 10:54:21Z : c'est l'écriture du fichier LOT-2L lui-même, c'est-à-dire la source S-4. La recherche de l'auteur sur les journaux ne portait pas sur ce motif (V7).
- D:99 se limite au « texte des messages » sans nommer les motifs ni les auteurs. Il omet aussi les autres occurrences du 27 novembre : J:9396, J:9472 et J:9478.
- **Correction.**
  - Dans N : écrire « hors du texte de LOT-2L lui-même (J:976-977) ».
  - Dans D : écrire « messages du propriétaire », en nommant les motifs.

**RJ-21 — À corriger (D:123 ; N §3.5) — La plage des questions Q1 est fausse**
- **Preuve.** Les deux textes écrivent « Q1.1 à Q1.5 ». Le registre porte Q1.1 à Q1.4, puis « Q1.5 à Q1.9 » (R:165-169).
- **Correction.** Écrire « Q1.1 à Q1.9 ».

**RJ-22 — À corriger (N §4, l.56) — Une présomption est présentée comme un fait**
- **Preuve.** N écrit « L'option validée est l'option (b) de la question Q1 de l'étude LOT-2L ». Cette phrase n'est pas attribuée à la déclaration. Elle contredit aussi le §3.1 de N : le texte déclaré, avec sa « phase autonome pour les neutres », n'est pas celui de l'option (b).
- **Correction.** Écrire « que la déclaration rattache à l'option (b), dont le texte diffère (§3) ».

**RJ-23 — À corriger (D:184 QO-17 ; D:266 TJ-26) — Une option contredit S4 et G1 sans le signaler**
- **Preuve.** La seconde option de QO-17 propose de « refuser toute diagonale qui longe une unité consciente ». Elle contredit deux sous-décisions inscrites :
  - S4 : « Une unité voisine ne compte pas comme obstacle pour la règle des diagonales » (R:74) ;
  - G1 : une unité voisine « n'interdit pas automatiquement la diagonale au titre de S4 » (R:129).

  Le dossier présente donc une règle plus stricte que le registre, non inscrite, sans dire qu'elle y déroge.
- **Correction.** Signaler explicitement cette dérogation, qui demande une décision, ou retirer l'option. Adapter TJ-26 en conséquence.

**RJ-24 — À corriger (D:159) — La ligne Q5.2 généralise trop**
- **Preuve.** D écrit « aucune superposition ». Le registre dit « Aucune superposition **volontaire** de deux unités conscientes sur un même emplacement stable », et « lorsqu'elle est en position stable » (R:203). G2 reste une superposition involontaire admise.
- **Correction.** Reprendre la formulation du registre.

**RJ-25 — À corriger, mineur (D:28 ; D:104) — « seule trace » est ambigu**
- **Preuve.** D écrit « la seule trace écrite est l'option (b) » et « Seule trace retrouvée : l'étude LOT-2L ». Ces phrases peuvent laisser croire que l'option (b) est une trace de la décision. Elles sont aussi dépassées : le journal contient désormais la déclaration du 27 novembre. Enfin, la puce de D:104 est rattachée par erreur au paragraphe sur les recherches de la relecture (D:103).
- **Correction.** Écrire « seule trace écrite de l'option proposée, et non de sa validation ».

**RJ-26 — Observation (D:168 ; D:280) — « à inscrire » présume un choix du propriétaire**
- **Preuve.** D écrit « à inscrire » pour Q1-B. Or N §6.4 laisse au propriétaire le choix d'accepter une source seulement déclarée.
- **Correction.** Écrire « si le propriétaire décide de l'inscrire ».

**RJ-27 — Observation — Restes des constats précédents**
- D:96 garde l'étiquette mixte « [INSP, commandes exécutées] ».
- D:98 dit « sur les mêmes motifs » pour `orchestration/mandats`. L'auteur n'y a cherché que quatre motifs (J:9382), sans « camp neutre ».
- D:138 n'a toujours pas G4.
- QO-11 (D:178) n'est pas reformulée au regard de Q1.2.
- Il manque un test d'identifiant d'unité en double.
- Il manque un test de P-07 appliqué au camp du joueur.
- TJ-24 dit « selon la décision » sans renvoyer à aucune QO.

**RJ-28 — Observation (D:183, QO-16) — Des renvois manquent**
QO-16 devrait citer Q3.4, Q4.20 et Q4.21. Ces sous-décisions y répondent déjà en partie :
- un pas non commencé n'est pas débité ;
- la seule révélation n'interrompt pas la marche ;
- l'arrêt se fait sans recalcul.

**RJ-29 — Observation (N §1, l.23) — « la source et ses limites » est trop fort**
- **Preuve.** N écrit « Dans chaque cas, la source et ses limites sont écrites ». C'est vrai pour MEC-0001 et MEC-0004. Pour MEC-0003 (R:455), la source est donnée, « conversation Bastion du 21 novembre 2026 », mais aucune limite n'est écrite.

**RJ-30 — Observation (D:121) — Les écarts ne vivent que hors du dépôt**
- **Preuve.** Les écarts entre la déclaration et LOT-2L (N §3.1 à §3.3) ne figurent que dans N, hors dépôt. D, destiné au dépôt, se contente d'y renvoyer.
- **Correction.** Résumer ces écarts au §3 de D, ou prévoir l'archivage de N.

### Verdict

**Corrections de RJ-01 à RJ-18 : correctement traitées dans l'ensemble** (inspecté). Les compteurs sont exacts (exécuté et réussi).

**Déclaration du propriétaire : traitement conforme aux consignes.** Le dossier ne présume aucune validation et ne présente pas l'option (b) comme une preuve.

**Points à corriger :**
- trois nouvelles inexactitudes : RJ-20 (S-6), RJ-21 (plage Q1) et RJ-24 (Q5.2) ;
- une présomption formulée comme un fait dans la note : RJ-22 ;
- une option qui contredit S4 et G1 sans le dire : RJ-23 ;
- une formulation ambiguë : RJ-25.

Aucun constat n'est bloquant. Les contrôles réussissent : `git status --porcelain -uall` ne montre que les trois fichiers ; `test-hooks.sh` passe (75 tests, 0 échec, code 0). La validation finale appartient au propriétaire.

## Vérification des corrections RJ-20 à RJ-30

- **Date :** 2026-11-27, terminée à 14:12 UTC.
- **Nature :** vérification ciblée, en lecture seule, limitée aux corrections de RJ-20 à RJ-30 et aux erreurs qu'elles auraient introduites. Le relecteur ne s'accorde pas la validation finale.
- **Abréviations :** D = dossier actuel ; D2 = `scratchpad/lot1j/dossier-relu-2.md` ; N = note actuelle ; N1 = `scratchpad/q1b/note-relue.md` ; R = registre ; J = journal `-home-user`.

**Empreintes (SHA-256) :**

| Fichier | SHA-256 |
|---|---|
| D2, identique à la version vérifiée précédemment | `840486f19dfe6e2b5519ba181db356b7b6da3d290402962e90a03d85f2cade42` |
| D, 315 lignes | `68371fd53a95bb2080bab2ad871ccbee43d140a044d1c6cf52010185b21c9fb1` |
| N1, identique à la version vérifiée précédemment | `ced28d47c19c2027f911848eeb4615fd9e30d63a9e53bea95940d196a4d5ecd0` |
| N, 98 lignes | `5da9de503f88fefb644cb07e0829d759f865dc7c8514fd1ce08ef134b3b5d0fa` |
| Archive, inchangée | `747c402c…20b3` |
| Index, inchangé | `c8c8cede…724a` |
| Registre, identique à `main` | `6e5d13cc…f16d` |

### Commandes exécutées

| # | Commande (résumé) | Résultat | Code |
|---|---|---|---|
| W1 | `sha256sum` de D2, D, N1 et N | D2 et N1 correspondent aux versions vérifiées | 0 |
| W2 | `diff D2 D` ; `diff N1 N` | 18 blocs dans D et 4 dans N, tous examinés | 1 (différences attendues) |
| W3 | `grep -F` des deux citations de Q5.2 dans R ; lecture de Q3.4 (R:221), Q4.21 (R:223), Q4.20 (R:230), G1 (R:128-129) | Les deux citations figurent mot pour mot. Résumés de Q3.4, Q4.20 et Q4.21 exacts | 0 |
| W4 | `grep` de « Je valide Q1 » dans les deux journaux | Première occurrence en J:9487, le 27 novembre ; ancien journal : 0. « Q1-B » apparaît dès J:9366 ; « phase autonome » dès J:9487 ; « trois camps » en J:976-977 avant le 27 novembre (vérification précédente, V6) | 0 |
| W5 | Comptage mécanique des tableaux de D ; recherche de renvois au-delà de QO-17 ou TJ-28 ; recherche de « à inscrire » | 28 TJ, 17 QO et 11 P ; aucun renvoi invalide ; plus aucun « à inscrire » | 0 |
| W6 | Contrôle de D et N : BOM, CR, espaces finaux, LF final | ni BOM ni CR ; aucun espace final ; LF final | 0 |
| W7 | `git diff --quiet 364b46a --` sur les chemins protégés | aucune différence | 0 |
| W8 | `git status --porcelain -uall` | ` M docs/mandates/README.md`, `?? …LOT-1J-v1.0-transcription.md`, `?? docs/reviews/LOT-1J-CONCEPTION-UNITES-CAMPS.md` | 0 |

### Résultats (inspecté, sauf W3 à W8, exécutés)

| RJ | État | Preuve |
|---|---|---|
| 20 | corrigé | N S-6 est exact : « Trois camps » n'apparaît que dans l'écriture de LOT-2L à 10:54:21 UTC. D:99 nomme les motifs et les occurrences du 27 novembre. Une imprécision résiduelle est relevée en RJ-32 |
| 21 | corrigé | D:127 ; N §3.5 : « Q1.1 à Q1.9 » |
| 22 | corrigé | N l.56 : « La déclaration rattache la décision à l'option (b)… dont le texte diffère du texte déclaré (§3) » |
| 23 | corrigé pour S4, mais avec une nouvelle omission (RJ-31) | D:188, D:270 |
| 24 | corrigé | D:163 : citations exactes de R:203 ; l'exception G2 est mentionnée |
| 25 | corrigé | D:28, D:105 : « trace écrite de l'option proposée, non de sa validation » ; la puce mal rattachée est devenue un paragraphe |
| 26 | corrigé | D:172, D:286 ; aucun « à inscrire » ne reste |
| 27 | corrigé | étiquette (D:96) ; quatre motifs exacts selon J:9382 (D:98) ; G4 (D:142) ; QO-11 (D:182) ; TJ-24 renvoie à QO-12 (D:268) ; TJ-27 et TJ-28 ajoutés (D:271-272) |
| 28 | corrigé | QO-16 (D:187), Q3.4, Q4.20 et Q4.21 fidèlement résumées |
| 29 | corrigé | N l.23 |
| 30 | corrigé | D:122-125 résume fidèlement les écarts 1, 3 et 4 du §3 de N |

**Compteurs : exacts** (exécuté et réussi, W5) :
- 28 TJ (D:44, D:292) ;
- dix-sept QO ;
- onze P.

### Constats

**RJ-31 — À corriger (D:188 QO-17 (b) ; D:270 TJ-26) — La nouvelle option (b) déroge à G1 sans le dire**
- **Preuve.** La correction a remplacé l'ancienne option (b) par « Ne retenir d'abord que l'occupation des cases (S10), sans contrôle de volume entre unités ». Or G1 exige que « le volume de l'unité [puisse] emprunter un passage sans traverser celui d'une autre unité consciente » (R:128), et MEC-0003 l'applique déjà par renvoi (R:493).

  Avec l'option (b), et pour TJ-26 « aucun contrôle de volume entre unités », une diagonale qui traverse le volume d'une unité consciente voisine serait admise. QO-17 signale la dérogation seulement pour la variante de refus automatique, qui déroge à S4. Elle ne la signale pas pour (b), qui déroge à G1.
- **Correction.** Ajouter à (b), comme pour QO-07 (b) : « cette option déroge à G1 (et ARB-A) entre unités ; elle demande une décision explicite ». Ajouter la même précision à TJ-26.

**RJ-32 — Observation (D:99) — « non cherché par l'auteur dans les journaux » est inexact**
- **Preuve.** D:99 dit de « trois camps » qu'il n'a pas été cherché par l'auteur dans les journaux. Or l'auteur l'a cherché en J:9391, mais seulement dans le texte des messages utilisateur du journal courant ; il ne l'a cherché ni dans les autres entrées ni dans l'ancien journal. Ma propre formule de RJ-20 (« ne portait pas sur ce motif », V7) visait les seules commandes J:9498 à J:9511 et était trop large.
- **Correction.** Écrire « cherché par l'auteur seulement dans le texte des messages utilisateur du journal courant ».

Aucune autre erreur introduite par les corrections. Aucune validation présumée : D:28, D:105, D:122-125, D:172, D:286 et N l.56 attribuent tout à la déclaration et ne présentent pas l'option (b) comme une preuve.

### Verdict

**Corrections RJ-20 à RJ-30 : traitées.** Les compteurs sont exacts. Le registre, l'archive et l'index sont inchangés. `git status --porcelain -uall` ne montre que les trois fichiers attendus.

**Un point reste à corriger, RJ-31.** La nouvelle formulation de QO-17 (b) et de TJ-26 déroge à G1 sans le signaler.

**Une observation, RJ-32.** Elle porte sur une formulation, sans incidence sur les conclusions.

Aucun constat n'est bloquant. La validation finale appartient au propriétaire.

---

**Traitement des constats :**

| Constats | Traitement |
|---|---|
| RJ-01 à RJ-12 (à corriger) | **Corrigés**, et vérifiés par le relecteur (« Corrections de RJ-01 à RJ-18 : correctement traitées dans l'ensemble »). Les restes relevés ensuite sont regroupés en RJ-27 |
| RJ-13 à RJ-18 (observations) | **Appliquées** (vérifiées par le relecteur) |
| RJ-19 (contenu du §11 et de l'annexe) | **Appliquée** au §11 et dans l'annexe |
| RJ-20 à RJ-25 (à corriger) | **Corrigés**, et vérifiés par le relecteur (« Corrections RJ-20 à RJ-30 : traitées ») |
| RJ-26 à RJ-30 (observations) | **Appliquées**, et vérifiées par le relecteur |
| RJ-31 (à corriger) : l'option (b) de QO-17 déroge à G1 sans le dire | **Corrigé** : QO-17 (b) et TJ-26 signalent la dérogation à G1 et à ARB-A, qui demande une décision explicite. Vérifié lors de la relecture finale ciblée |
| RJ-32 (observation) : étendue de la recherche de « trois camps » | **Appliquée**, puis précisée par RJ-33 : « cherché par l'auteur seulement dans le texte des messages de type utilisateur (propriétaire et remises de sous-agents) du journal courant ». Vérifiée lors de la relecture finale ciblée |
| RJ-33 et RJ-34 (observations de la relecture finale ciblée) | **Appliquées** sur autorisation du propriétaire du 27 novembre 2026 : étendue exacte de la recherche (RJ-33) ; mention obsolète corrigée et empreintes des versions du rapport précisées (RJ-34). Leur vérification indépendante fait l'objet d'un compte rendu distinct, hors dépôt (`relecture-1j/verification-rj33-rj34.md`) |

Les corrections de RJ-31 et RJ-32 ont été revues lors de la relecture finale ciblée du 27 novembre 2026, achevée à 14:22 UTC, dont le verdict est : « Le LOT-1J est conforme au mandat, aux contraintes et aux consignes du propriétaire, sans réserve bloquante. » Cette relecture est ajoutée à la fin du rapport du relecteur, après la version intermédiaire reproduite ci-dessus.

**Note de traçabilité Q1-B.** Elle est relue dans les mêmes sections du rapport : sources S-1 à S-8, écarts et précédents. Ses constats (RJ-20, RJ-21, RJ-22 et RJ-29) sont corrigés et vérifiés. La note reste hors du dépôt.

## Annexe — Empreintes SHA-256

| Fichier | Sur `origin/main` (`364b46a`) | Dans l'arbre de travail du lot |
|---|---|---|
| `docs/mandates/BASTION-MANDAT-LOT-1J-v1.0-transcription.md` | absent | `747c402c344dcbc68eec13f9e262e75decb20055e716e559ff2b85795e3920b3` |
| `docs/mandates/README.md` | `c34e6718d754ccdd243fe311323279dad052006f95b760edb53ac801f404d3fc` | `c8c8cedef0b15de0523df0becdf0ccf65b3339a87c0941cee58ad06d1bf6724a` |
| `docs/gameplay/GAMEPLAY-DECISIONS.md` (registre, inchangé) | `6e5d13cccb07c9b0bd67e520868f85e33057f4b02c5ce9f42df7323423abf16d` | `6e5d13cccb07c9b0bd67e520868f85e33057f4b02c5ce9f42df7323423abf16d` |

**Documents hors dépôt** (dossier temporaire de la session) :

| Fichier | SHA-256 |
|---|---|
| `scratchpad/lot2l/LOT-2L-FONDATIONS-TACTIQUES.md` (étude LOT-2L, 16 novembre 2026) | `419ec107f493285467eba0419ed1b69f786dc2a3dc523a6a58e61bd86c5f5702` |
| `scratchpad/q1b/NOTE-TRACABILITE-Q1-B.md` (note de traçabilité Q1-B) | `5da9de503f88fefb644cb07e0829d759f865dc7c8514fd1ce08ef134b3b5d0fa` |
| `scratchpad/relecture-1j/relecture-882798f7.md` (rapport du relecteur, version intermédiaire reproduite au §12) | `882798f7560309e775e09acac3c7f99948c143d1ed4bf53f9caebc1b51f004b0` |
| `scratchpad/relecture-1j/relecture.md` (rapport du relecteur, version finale, avec la relecture finale ciblée) | `fdf47781699579705796927c8ec955f0b343fb49f9d8013fd24365a4bb9193b9` |

Ce dossier ne peut pas porter sa propre empreinte.
