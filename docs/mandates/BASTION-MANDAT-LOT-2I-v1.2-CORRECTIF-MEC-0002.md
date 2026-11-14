# BASTION — Mandat LOT-2I v1.2 — Correctif documentaire de MEC-0002

**Date :** 14 novembre 2026.  
**Statut : PRÉPARÉ ET PUBLIÉ — EXÉCUTION NON AUTORISÉE.**  
**Dépôt :** `mengpo1/bastion`.  
**Branche du présent mandat :** `orchestration/mandats`.  
**Cible documentaire éventuelle :** les quatre livrables du LOT-2I de la branche `docs/lot-2i-consolidation-mec-0002`, PR brouillon n°12 vers `main`.  
**Autorisation obtenue :** le propriétaire a autorisé la **préparation et publication de ce mandat** sur `orchestration/mandats` le 14 novembre 2026. **Cela n'autorise ni l'exécution du correctif, ni un push sur la branche LOT-2I, ni une modification de PR, ni une fusion, ni l'inscription au registre, ni du gameplay.**

## 0. Gouvernance et périmètre

1. Lire `CLAUDE.md` sur `main` et les mandats LOT-2I v1.0 et v1.1, **conservés à l'identique**. Le présent mandat est une proposition corrective versionnée, sans effacer les preuves antérieures.
2. **Avant toute exécution**, obtenir une autorisation distincte du propriétaire couvrant le présent v1.2, les fichiers modifiables et la branche de travail. Sans cet accord, s'arrêter.
3. Les corrections ne concernent que **quatre documents** de `docs/reviews/`, énumérés au §1, et uniquement après autorisation d'exécution. Préférer travailler localement sur la branche existante `docs/lot-2i-consolidation-mec-0002` après vérification de son état ; ne pas supposer qu'elle est inchangée.
4. **Ne pas modifier** le registre protégé `docs/gameplay/GAMEPLAY-DECISIONS.md`, ni `docs/decisions/`, `docs/references/`, `docs/mandates/`, `docs/mandates/README.md`, `CLAUDE.md`, `src/`, `tests/`, `.claude/`, `scripts/harness/`, `.github/`. Aucun code, test exécutable, mécanique ou équilibrage.
5. **Push, mise à jour de la PR n°12 et fusion** nécessitent chacun une autorisation distincte, explicite et vérifiable. Ne pas considérer l'existence de la PR comme une autorisation de la modifier.
6. Dans toute **proposition** de registre, maintenir `MEC-0001` et `MEC-0002` au statut **« reportée »**, classe `MODIFICATION-PROPOSEE`, sans autoriser d'implémentation.

## 1. Sources à relire

Sur `main` : `CLAUDE.md`, `docs/gameplay/GAMEPLAY-DECISIONS.md`, spécification et matrice du LOT-2F, décisions DS1–DS5, documents LOT-2G et LOT-2H.

Sur `orchestration/mandats` :
- `docs/mandates/BASTION-MANDAT-LOT-2I-v1.1.md` ;
- `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md` (copie provisoire publiée au commit `d028c52`).

Sur `docs/lot-2i-consolidation-mec-0002` : lire les quatre **livrables existants**, qui constituent le seul périmètre de correction envisagé :
1. `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` ;
2. `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` ;
3. `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md` (**diff jamais appliqué**) ;
4. `docs/reviews/LOT-2I-EXECUTION.md` (**conserver ses preuves et y ajouter un compte rendu correctif**, sans réécrire silencieusement l'historique).

La preuve des nouveaux arbitrages provient de déclarations explicites du propriétaire dans sa conversation du 14 novembre 2026, **transcrites ci-dessous**. Si Claude Code n'a pas accès aux messages originaux, qualifier la transcription comme preuve déclarative fournie par l'orchestrateur, et signaler la limite. **Ne jamais fabriquer de source primaire.**

## 2. Nouveaux arbitrages acceptés pour la conception (non encore inscrits)

### 2.1 Confirmations des huit points du LOT-2I

| ID | Paroles / choix du propriétaire | Conséquence documentaire |
|---|---|---|
| **A3A** | « 3 mètres fixes par étage » | L'écart vertical entre deux sols d'étages consécutifs est **3 m** ; distinguer cette hauteur de la montée initiale d'un saut. |
| **A8A** | « Un tirage commun aux deux personnages (décision précédente) » | Conserver le tirage de choc commun à deux unités (`CO-08`) ; annoter l'écart vis-à-vis de DS4.1 et les conséquences sur les blessures relatives avant protections. |
| **A12** | « oui » | Conserver l'interdiction d'attaque sautée visant une unité de plusieurs cases (`GE-09`, DS5.5). |
| **A18** | « oui » | L'attaquant occupe l'ancienne case de sa cible repoussée (`RP-09`, DS5.3). |
| **A24** | « oui » | `MEC-0002` fait autorité pour sauts, chutes et collisions ; N5–N10 restent historiques dans `MEC-0001`. |
| **A25** | « oui » | Les dégâts d'une collision avec une unité sont séparés des dégâts de réception au sol : les deux participants peuvent être blessés malgré une exemption de réception. |
| **A27** | « oui » | Une esquive échouée ne produit pas de déplacement d'esquive ; un repoussement peut survenir **après** le choc (`RP-01`, K07/DS5.3). |

**A4C** (« Revoir le seuil et les exceptions ») a été précisé par les décisions suivantes :
- **A4.1D** : « Autre règle, à préciser » ; précision textuelle du propriétaire : **« Une chute sans dommage se fera d'une unité d'étage soit 3m »**.
- **A4.2A** : « Aucun dégât de réception, même si la trajectoire monte puis redescend » pour un saut volontaire **au même niveau**, dans le cas normal sans surcharge ni collision.
- **A4.3A** : pour un saut volontaire descendant d'un étage, mesurer les **3 m entre le sol de départ et le sol d'arrivée**, sans ajouter la montée au sommet de la trajectoire.
- **Exception surcharge A** : « La surcharge peut provoquer des dégâts même à 3 mètres. »
- Le propriétaire a confirmé la synthèse de ces choix par « Je valid[e] ».

### 2.2 Recalibrage validé après le choix A4

| ID | Formulation acceptée par le propriétaire |
|---|---|
| **D1C** | « Conserver uniquement le seuil de 3 m et recalibrer toutes les valeurs lors des tests (proposé) » |
| **D2A** | « La surcharge augmente la hauteur équivalente utilisée dans le calcul, avec le coefficient existant (proposé) » |
| **D3A** | « Le seuil reste 3 mètres quelle que soit la gravité ; la gravité module les dégâts au-delà du seuil (proposé pour respecter ton choix initial) » |
| **D4A** | « Sa vitesse descendante initiale augmente la hauteur équivalente de chute, donc les dégâts possibles (proposé) » |

Après lecture de la synthèse, le propriétaire a répondu explicitement **« Je valide »**. La synthèse retenait en particulier :
- seuil de **3 m inclus** pour les dégâts de chute ordinaires sans surcharge ni vitesse descendante héritée, quelle que soit la gravité ;
- courbe de dégâts **à recalibrer lors des tests**, sans fixer de nouvelles puissances ;
- coefficient de surcharge déjà accepté : `S = max(0, charge/capacité − 1)` et `F_surcharge = min(2, 1 + 0,5 × S)` ; l'appliquer à la **hauteur équivalente**, **sans le réappliquer ensuite à la puissance des dégâts** ;
- une vitesse verticale descendante **héritée** (notamment après traversée d'un support) accroît la hauteur équivalente ;
- la gravité module **les dégâts au-delà** du seuil fixe de 3 m ;
- conserver les exemptions de réception volontaire et calculer les collisions séparément.

**Ne pas inventer** la chaîne numérique définitive de combinaison vitesse héritée–surcharge–gravité, les valeurs de la courbe, des protections, des plafonds, des arrondis ou des coefficients. Le principe est décidé ; l'algorithme précis reste **ouvert**.

### 2.3 Cas de comportement pour les tests futurs (non exécutables dans ce mandat)

| Situation | Résultat à spécifier |
|---|---|
| Chute ordinaire de 2,99 m ou exactement 3,00 m ; pas de surcharge ni de vitesse descendante héritée ; gravité positive | **0 dégât ordinaire de chute**, sous réserve d'une collision distincte. |
| Chute ordinaire de 3 m, surcharge | **Dégâts possibles** via la hauteur équivalente majorée, sans garantir une perte de PV après protections. |
| Chute de 3 m avec vitesse descendante héritée | **Dégâts possibles** par hauteur équivalente accrue. |
| Chute de plus de 3 m sans surcharge | **Dégâts possibles** ; valeur à calibrer. |
| Saut volontaire au même niveau, sans surcharge ni collision | **0 dégât de réception** lié à la montée puis redescente normale. |
| Saut volontaire d'un étage vers le bas, sans surcharge ni collision | Exemption de dégâts ordinaires de réception ; une cible qui esquive ne transforme pas cette réception en chute involontaire. |
| Choc contre une unité pendant la réception | Collision **distincte** : dégâts possibles pour les deux, même en présence d'une exemption de réception. |
| Collision entre deux unités | **Un même tirage d'intensité** pour le même choc ; protections ensuite individuelles. |

Ne pas transformer « dégâts possibles » en « dégâts garantis ».

## 3. Corrections imposées par les nouveaux choix

Les textes passés restent **historiquement citables**, mais ne doivent plus être présentés comme des règles actives inchangées :

- `CH-03` : ancienne blessure possible dès un étage involontaire **sans surcharge** ; remplacée pour une chute ordinaire de 3 m sans vitesse héritée ni collision.
- `CH-07`, `D03/D04` : ancienne courbe `B(1)=8; B(2)=14; B(3)=22,1; B(4)=33,035` désormais **historique**. Ne pas la reprendre comme barème retenu, ni la décaler automatiquement d'un étage. Nouvelles valeurs **ouvertes**.
- `CH-08`, `CH-01`, `CH-05` : distinguer les **sols départ/arrivée** (écart d'étage) de la trajectoire et de la hauteur équivalente ; préserver l'exemption d'un saut normal et celle d'un étage sans surcharge ni collision.
- `CH-09`, `N7` : ancien seuil `0,25 étage` (0,75 m) **remplacé** pour les dégâts ordinaires par **3 m** ; annoter N7 sans altérer le registre.
- `CH-10` : gravité modifiant les dégâts **au-delà** du seuil sans modifier le seuil fixe ; point d'application de `g/g0` et absence de double comptage à vérifier.
- `CH-11` : vitesse descendante **héritée** prise en compte dans la hauteur équivalente ; supprimer les renvois actifs au seuil de 0,25 ; résoudre les exemptions de saut normal sans inventer un algorithme.
- `CH-13`, `CH-15`, `CH-16`, `CH-17`, `CH-18` : le coefficient de surcharge **majore la hauteur équivalente**, et **ne multiplie pas de nouveau** la puissance. Conserver les paramètres et limites précédemment validés, signaler les interactions ouvertes avec les plafonds et les arrondis.
- `CO-09` et `D09` : chaîne de calcul **à réconcilier**, aucune double application de surcharge, gravité ou masse.
- `CO-08`, `CO-03`, `DS4.1` : confirmation explicite du tirage commun ; documenter qu'il ne peut pas à lui seul inverser le rapport des puissances avant protections, tout en distinguant protections individuelles.
- `GE-09`, `RP-01`, `RP-09`, `PE-01` : fond des confirmations réglé ; ne pas confondre **validation en conception** et **autorisation d'inscription**.
- `SA-19` : le sommet de référence d'un saut reste **1/4 étage**, soit **0,75 m** avec 3 m/étage. Ce **sommet de saut** ne doit pas être confondu avec l'ancien **seuil de blessure** de 1/4 étage.
- Corriger la matrice des sources, les futurs tests, la synthèse, les ambiguïtés A1–A28, et la **proposition de diff**, sans changer le vrai registre. Vérifier chaque occurrence de `0,25`, `75 cm`, `B(1)`, `un étage`, `surcharge`, `gravité`, y compris dans les analyses, sans remplacement aveugle des citations historiques.

## 4. Exécution envisagée — après mandat distinctement autorisé

1. Exécuter `git fetch origin main orchestration/mandats` et vérifier l'état de la branche LOT-2I et de la PR n°12. Si de nouveaux commits sont apparus, établir un diff et signaler les conflits.
2. Travailler sur une branche **explicitement validée** ; par défaut, proposer `docs/lot-2i-consolidation-mec-0002`, sans la modifier à distance sans autorisation.
3. Modifier **uniquement** les quatre livrables du §1 ; conserver leur historique et documenter les changements **avant/après** par règle et source. Conserver les 105 identifiants existants autant que possible ; justifier tout besoin de nouvelle règle permanente.
4. Réviser le **texte proposé** et le **patch non appliqué** du registre ; laisser `MEC-0001` et `MEC-0002` « reportées », aucun gameplay. Faire `git apply --check` ou équivalent sur copie du registre, **pas dans le registre réel**.
5. Recalculer les statuts, ambiguïtés ouvertes et futurs tests. Ne pas inscrire comme validés les coefficients, seuils additionnels, lois numériques ou valeurs de dégâts encore **reportés aux tests**.
6. Revue indépendante **en lecture seule** sur le diff ; corriger ses constats dans le périmètre. Produire un rapport de correction appendu au rapport existant, avec commandes, sorties, codes de retour, fichiers touchés, points ouverts et limites de preuve.
7. Arrêt. **Pas de push, pas de PR, pas de fusion** sans autorisation séparée du propriétaire ; pas de modification de registre ni de code.

## 5. Critères de sortie

- Concordance entre consolidation, matrice, proposition de fiche, patch et cas de tests futurs.
- Arbitrages datés, formulés sans ajout de règles ; décisions obsolètes tracées historiquement.
- Aucun ancien seuil de 0,25 ou barème B(1) actif présenté comme la règle actuelle ; pas de nouvelle courbe de dégâts inventée.
- Aucune extrapolation d'un accord de conception en autorisation de modification du registre ou d'implémentation.
- Vérifications et revue indépendante réellement effectuées et documentées ; tout contrôle non exécuté signalé.

**La publication de ce document ne donne aucune permission de commencer le correctif.**