# BASTION — Mandat LOT-1A v1.0
## Identifier et figer une référence OXCE candidate

**Statut : PRÉPARÉ — NE PAS EXÉCUTER AVANT AUTORISATION EXPLICITE DU PROPRIÉTAIRE.**  
**Dépôt :** `mengpo1/bastion`  
**Document publié par ChatGPT :** branche `orchestration/mandats`, chemin `docs/mandates/BASTION-MANDAT-LOT-1A-v1.0.md`  
**Base de travail attendue :** `main`, commit `9e45c5db5daf3b13dd1e42dda8b50bb7f65567ca`  
**Branche de travail proposée à Claude Code :** `research/lot-1a-oxce-reference`

## 1. Objectif unique

**Identifier une version exacte, vérifiable et reproductible d'OpenXcom Extended (OXCE) à proposer comme référence pour Bastion**, sans choisir de mécanique de jeu et sans en implémenter.

Bastion doit pouvoir dire précisément de quelle version d'OXCE il parle. L'objectif est une **proposition argumentée au propriétaire**, et non une adoption automatique.

**Simplicité avant tout.** Aucune infrastructure ni automatisation nouvelle.

## 2. Conditions préalables

- L'autorisation de ce mandat doit être explicite et distincte de l'autorisation de fusion de la PR n° 2.
- Lire ce mandat **directement sur GitHub** à partir de la branche `orchestration/mandats`. **Ne pas le recopier ou l'archiver.**
- Exécuter `git fetch origin main` avant de commencer ; vérifier que la branche de travail part de la tête de `main`. Signaler tout écart matériel.
- Le lot 0D est accepté **avec réserves** ; consulter les limites conservées dans `docs/reviews/LOT-0C-QUALIFICATION.md` et `docs/reviews/LOT-0C-R1-EXECUTION.md`.
- Aucun push ou merge vers `main`. Ce mandat, s'il est autorisé, permet uniquement le push de `research/lot-1a-oxce-reference` et l'ouverture d'une PR **en brouillon** vers `main`.

## 3. Travaux demandés

1. Retrouver et vérifier le dépôt amont du projet **OpenXcom Extended (OXCE)**. Distinguer le dépôt officiel du moteur, les forks, les versions précompilées et les mods.
2. Identifier **un commit candidat précis** (SHA complet), sa branche, la date du commit et, si disponible, son tag/version. Fournir des liens GitHub directs permettant de vérifier ces données.
3. Clarifier la **portée** : moteur OXCE seul, ou moteur avec mod(s). **Ne choisir aucun mod implicitement** ; si un mod semble nécessaire, l'indiquer comme décision distincte à soumettre.
4. Vérifier les fichiers de licence et leurs versions pour le commit retenu. Donner des liens précis. Signaler les contraintes ou questions de redistribution, sans présenter cela comme un avis juridique définitif.
5. Noter ce qu'on pourra raisonnablement vérifier par la suite à partir de cette référence (sources, documentation, comportements observables) et ce qui reste inconnu. Ne **pas** déclarer des règles de jeu « conformes à OXCE » sans tests dédiés.
6. Formuler **une seule recommandation** de référence, avec justification simple et limites. Si les sources ne permettent pas de départager les candidats, le dire et soumettre l'arbitrage au propriétaire.

## 4. Périmètre strict

**Fichier de travail autorisé :**
- `docs/reviews/LOT-1A-OXCE-REFERENCE.md` : rapport de recherche et proposition.

**Ne pas modifier** `docs/references/OXCE-BASELINE.md`, `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/decisions/TECHNICAL-DECISIONS.md`, `CLAUDE.md`, le harnais, les projets C#, les tests ou le projet Godot. Le propriétaire doit d'abord valider la référence candidate avant son inscription dans le registre protégé.

Aucune création de mécanique `MEC-NNNN`, aucun code OXCE copié, aucun asset X-COM repris, aucune implémentation de gameplay.

## 5. Vérifications et preuves

- Chaque fait externe (dépôt, commit, licence, statut, date, portée) doit avoir une **source consultable** ; distinguer `vérifié`, `inférence` et `non vérifié`.
- Vérifier que le SHA candidat est accessible et pointe vers la version indiquée.
- Faire relire **en lecture seule** la proposition et les liens par un agent distinct, sans demander d'approuver à la place du propriétaire.
- Contrôler le diff : **un seul fichier de rapport** est autorisé. Les tests C# ne sont pas requis pour une étude documentaire seule ; mentionner les vérifications réellement exécutées et les éventuels contrôles non pertinents.
- Relever le résultat réel de la CI pour la PR documentaire si elle est ouverte ; ne pas promettre un état vert avant observation.

## 6. Livraison et arrêt

Une fois **autorisé** :
- Produire le rapport `docs/reviews/LOT-1A-OXCE-REFERENCE.md` contenant sources, SHA candidat, portée, licence, recommandation, revue indépendante et questions à arbitrer.
- Commiter/pousser **uniquement** `research/lot-1a-oxce-reference`, ouvrir une PR **en brouillon** ; ne pas fusionner.
- Informer le propriétaire avec le chemin du rapport, la branche, le dernier SHA, la PR et l'état observé de la CI, conformément à `CLAUDE.md`.

**Arrêt obligatoire :** attendre la décision explicite du propriétaire sur la référence. **Ne pas remplir** `OXCE-BASELINE.md` et ne pas commencer la première mécanique.
