# BASTION — Mandat LOT-2B v1.0
## Préparation des arbitrages de MEC-0001 — déplacement élémentaire à pied

**Statut : PRÉPARÉ — la publication ne vaut pas autorisation d'exécution.**  
**Dépôt :** `mengpo1/bastion`  
**Branche de publication du mandat :** `orchestration/mandats`  
**Base de travail attendue :** `main`, commit `e3dfd41ab43dcc17f1cbf79afce1fe0828a0821f` (à revérifier au démarrage).  
**Branche de travail proposée :** `design/lot-2b-mec-0001-proposition`.

## 1. Objet et limite

Préparer **une proposition courte et compréhensible** pour permettre au propriétaire d'arbitrer la future fiche `MEC-0001 — Déplacement élémentaire à pied`, à partir du rapport déjà fusionné `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`.

**Ne décider aucune règle à la place du propriétaire.** Les propositions faites lors de la revue ChatGPT du LOT-2A ne sont pas des décisions acceptées. Ce mandat ne crée pas de fiche MEC, n'autorise aucune implémentation et ne demande pas une nouvelle étude exhaustive d'OXCE.

**Principe impératif : simplicité avant tout.** Pas de nouveau mécanisme de gouvernance, d'agent, d'outil ou de couche technique.

## 2. Travail demandé

1. Lire `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/references/OXCE-BASELINE.md`, `CLAUDE.md` et le rapport LOT-2A depuis `main`. S'appuyer sur la référence OXCE figée `441cae1b071d249d40a223858cb6bd07fd5d791b` **uniquement si une vérification ciblée est indispensable** ; citer le fichier et les lignes. Ne pas présenter une lecture de code comme une observation d'exécution.
2. Proposer un **périmètre élémentaire cohérent**, sans ajouter de mécanique absente du LOT-2A : carte plane à un niveau, unité à pied de taille 1, déplacement de case en case, obstacles, occupation, coûts propres à Bastion, chemin, paiement en TU et destination invalide. Distinguer clairement **option proposée** et **décision acceptée**.
3. Regrouper les arbitrages `P1` à `P14` du LOT-2A en :
   - **choix structurants à soumettre maintenant**, notamment coût de la diagonale (P3), passage diagonal près des obstacles (P7) et TU insuffisantes (P9) ;
   - **options de simplification proposées**, non approuvées (P1, P2, P4, P5, P6, P8, P12, P14) ;
   - **sujets explicitement reportés**, notamment orientation/rotation (P10), énergie (P11), interruptions (P13), et interface. Justifier toute dépendance qui rendrait un report incohérent.
4. Donner **au plus trois questions prioritaires** à poser au propriétaire, avec options courtes, conséquences concrètes sur le jeu et indication de ce qu'OXCE fait d'après le LOT-2A. Ne pas inventer les réponses.
5. Fournir quelques **exemples sur petite grille** avec coûts TU **fictifs et explicitement indiqués**, pour expliquer les différences entre options (diagonale, angle d'obstacle, TU insuffisantes). Ne pas reprendre les données d'OXCE ou de X-COM.
6. Proposer des **critères de tests futurs**, sans écrire de tests ni de code. Signaler les inconnues qui empêchent une fiche MEC complète, plutôt que les combler silencieusement.

## 3. Livrable unique

Créer `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`, lisible par le propriétaire, avec :

- un résumé du périmètre proposé, en quelques lignes ;
- une table compacte `P1` à `P14` : référence, option proposée ou report, **statut non décidé**, raison courte ;
- les **trois arbitrages prioritaires maximum** et leurs exemples ;
- les limites, les critères de tests futurs et les décisions encore nécessaires ;
- un compte rendu des contrôles, du diff et de la revue indépendante.

**Ne pas modifier `docs/gameplay/GAMEPLAY-DECISIONS.md`** et ne pas créer de `MEC-0001` ailleurs. La future inscription dans le registre exigera une décision explicite, datée et prouvée du propriétaire, dans un mandat distinct.

## 4. Périmètre strict

**Seul fichier modifiable :** `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` (nouveau).

Aucune modification de code C#, tests, Godot, CI, hooks, `CLAUDE.md`, registres, références, autres rapports ou outils. Aucun gameplay. Aucune copie de code, données ou assets d'OXCE/X-COM (D4). Les observations reformulées et références de code sont permises.

Ne pas corriger dans ce lot les mentions anciennes de `main` non protégée ni les formulations de licence : sujets hors périmètre.

## 5. Exécution, revue et publication

- **Attendre l'autorisation explicite du propriétaire d'exécuter LOT-2B.** Ce mandat publié ne suffit pas.
- Au démarrage, `git fetch origin main` ; vérifier le SHA et signaler tout avancement inattendu avant de commencer.
- Travailler sur `design/lot-2b-mec-0001-proposition`, créée depuis `main`, jamais directement sur `main`.
- Faire relire le livrable en lecture seule par un agent distinct : vérifier fidélité au LOT-2A, absence de décision implicite, cohérence des options, D4 et périmètre du diff. Cette revue ne remplace pas l'accord du propriétaire.
- Vérifier `git diff --check` et le seul fichier autorisé. Les tests C# ne sont pas obligatoires pour ce lot documentaire ; indiquer exactement les vérifications exécutées. Relever la CI sans annoncer de réussite avant observation.
- **Si l'exécution et la publication sont autorisées**, pousser uniquement la branche de travail, ouvrir une **PR en brouillon** vers `main`, sans fusion. Le rapport est le canal de transmission à ChatGPT via GitHub ; il n'est pas nécessaire de rédiger un compte rendu à copier dans une conversation.
- Informer brièvement le propriétaire que la PR est publiée. Celui-ci pourra dire à ChatGPT « Claude a terminé » ; ChatGPT consultera GitHub directement.

## 6. Arrêt

S'arrêter après publication du dossier de proposition et de la PR en brouillon. **Aucune règle MEC-0001 n'est acceptée par ce lot.** Attendre les arbitrages du propriétaire avant toute rédaction validée ou implémentation.
