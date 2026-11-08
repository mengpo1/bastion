# BASTION — Mandat LOT-1B v1.0
## Consigner la référence OXCE validée

**Statut : PRÉPARÉ — exécution soumise à autorisation distincte du propriétaire.**  
**Dépôt :** `mengpo1/bastion`  
**Mandat publié sur :** `orchestration/mandats`, `docs/mandates/BASTION-MANDAT-LOT-1B-v1.0.md`  
**Base vérifiée :** `main` au commit `9e45c5db5daf3b13dd1e42dda8b50bb7f65567ca`  
**Branche de travail proposée :** `research/lot-1a-oxce-reference`, PR n° 3 (déjà ouverte en brouillon), tête vérifiée `6984027f74fee05de4f1b5b63d33d17fd4f72714`.

## 1. But et autorité

Inscrire **les six arbitrages D1–D6** approuvés explicitement par le propriétaire le **8 novembre 2026** en réponse aux propositions de l'orchestrateur après revue du rapport LOT-1A. Ces décisions ne constituent **pas** une autorisation de développer le gameplay.

**Simplicité avant tout.** Il s'agit d'une clôture **exclusivement documentaire** de la même référence OXCE. Pour ne pas multiplier les PR, **dérogation de périmètre proposée** : poursuivre dans la branche de la PR n° 3 existante plutôt que créer une nouvelle branche. L'exécution de ce mandat nécessitera l'accord explicite du propriétaire sur cette organisation. Conserver la PR en brouillon, sans fusion.

Ne pas archiver ou recopier le présent mandat : le consulter directement dans `orchestration/mandats`.

## 2. Décisions du propriétaire à inscrire exactement

- **D1 — Version :** OpenXcom Extended (OXCE) **8.7.1**, dépôt `MeridianOXC/OpenXcom`, branche source `oxce-plus`, **commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b`**. Le SHA, et non une branche flottante ni une étiquette supposée, définit la référence.
- **D2 — Jeu de référence initial :** **UFO: Enemy Unknown**, jeu de règles `xcom1`. **Terror From the Deep (`xcom2`) n'est pas inclus** dans cette référence initiale.
- **D3 — Options :** valeurs **par défaut de cette version précise** pour toutes les options du moteur, sans recopier ni figer manuellement une liste de 362 options. Toute exception ultérieure doit être décidée séparément.
- **D4 — Politique de réutilisation :** étudier les comportements OXCE ; **ne reprendre ni code, ni données, ni assets** d'OXCE ou des jeux X-COM. Une mécanique peut être **réimplémentée indépendamment** après décision du propriétaire et tests de comportement. Ne pas présenter cette politique comme une conclusion juridique générale.
- **D5 — Registre :** consigner la référence approuvée dans `docs/references/OXCE-BASELINE.md` par le présent mandat distinct. Conserver les sources et les limites de vérification.
- **D6 — Mods :** **aucun mod**, standard ou externe. Toute éventuelle addition exige un nouvel arbitrage.

## 3. Travaux autorisés

1. Vérifier par `git fetch origin main` que `main`, la PR n° 3 et son état correspondent à ceux indiqués en tête. En cas de changement inattendu, arrêter et signaler sans écraser.
2. Modifier **uniquement** `docs/references/OXCE-BASELINE.md` pour remplacer les champs « à figer » et « à confirmer » par les décisions D1–D6. Ajouter :
   - les liens directs au dépôt et au **commit figé** ;
   - le choix du jeu `xcom1`, les options par défaut, l'absence de mods ;
   - la politique **aucune reprise de code, données ou assets** ;
   - la source de validation : décision explicite du propriétaire dans la conversation du **8 novembre 2026**, sur proposition D1–D6 après revue LOT-1A ;
   - un lien relatif vers `docs/reviews/LOT-1A-OXCE-REFERENCE.md` ;
   - les limites toujours ouvertes : aucun gameplay validé ou implémenté, binaires non reconstruits, compatibilité et licences tierces non auditées exhaustivement. Ne pas effacer les garde-fous existants.
3. Apporter une **correction minimale** à `docs/reviews/LOT-1A-OXCE-REFERENCE.md` : la mention ancienne « `main` sans protection technique » doit devenir une précision temporelle : ce risque existait lors de la qualification du harnais, mais **au 8 novembre 2026 GitHub affiche un ruleset actif ciblant `main` et imposant le job `build-test`**. Ne pas modifier les constats historiques de l'étude, les comptes rendus de tests, ni les autres limites. Ajouter éventuellement une courte note de décision D1–D6, **datée**, sans réécrire rétroactivement les propositions comme des validations antérieures.
4. Ne pas modifier le registre `GAMEPLAY-DECISIONS.md`, les décisions techniques, `CLAUDE.md`, la CI ou le code. Aucun fichier nouveau n'est nécessaire.

## 4. Vérification et livraison

- Examiner le diff et prouver qu'il ne porte que sur les **deux fichiers Markdown** ci-dessus. Faire une revue indépendante **en lecture seule** du texte, de la fidélité aux six décisions et de l'absence de déclarations non prouvées.
- Relever l'état réel des contrôles GitHub Actions après publication. Les tests C# ne sont pas nécessaires à cette correction documentaire ; ne prétendre exécuter que les commandes réellement lancées.
- Si le propriétaire autorise explicitement l'exécution : commiter et pousser **uniquement** `research/lot-1a-oxce-reference`, actualiser la **PR n° 3 en brouillon**, puis notifier le propriétaire (chemins, commit, PR, CI).
- **Ne pas fusionner la PR n° 3. Ne pas démarrer l'implémentation d'une mécanique ni créer de fiche MEC.** Attendre la revue de l'orchestrateur et la décision distincte du propriétaire sur la fusion.

**Critère de clôture :** les six décisions figurent fidèlement dans la référence figée ; le rapport historique n'indique plus à tort que `main` est actuellement non protégée ; aucun autre fichier n'a changé.
