# BASTION — Mandat d'inscription documentaire MEC-0001 — v1.0

**Statut : AUTORISÉ POUR MODIFICATIONS DOCUMENTAIRES UNIQUEMENT**, le 17 novembre 2026, par la réponse explicite du propriétaire « Je valide » à la demande de validation du présent mandat. Cette autorisation porte sur la préparation de modifications locales, sur une branche dédiée, dans les seuls fichiers du §3, avec rapport d’exécution. Elle **n’autorise ni commit, ni push, ni publication, ni fusion**, et n’autorise aucun gameplay.

**Date de préparation et de validation :** 17 novembre 2026.

**Pièces à fournir à Claude Code :** le présent mandat intégral **et** `BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md` dans son intégralité. Le mandat ne remplace pas la source détaillée des décisions.

**Priorité de gouvernance :** si `CLAUDE.md` ou les fichiers effectivement lus révèlent une incompatibilité, ne pas la résoudre en élargissant le mandat ; signaler le blocage au propriétaire.

## 1. Objectif

Inscrire dans les documents de gouvernance de Bastion les **sous-décisions de conception** ARB-A à ARB-E et G1 à G4, déjà validées **en conversation**, sans transformer `MEC-0001` en mécanique globalement acceptée et sans implémenter de gameplay.

**Source de transcription :** `BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md`, intégrale ; ce document indique la provenance, les arbitrages et les paramètres laissés ouverts. Il succède à la v1.4, dont la vérification interne a déclaré V-01 à V-07 corrigées, avec deux réserves mineures levées dans la v1.4.1. **La v1.4.1 n'a pas été revue par un agent distinct.**

**Autres sources :** `CLAUDE.md`, `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md`, `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`, `docs/references/OXCE-BASELINE.md`, sur le commit réellement lu au début du mandat.

## 2. Décisions à inscrire, sans extrapolation

| Identifiant | Contenu accepté | Réserve à préserver |
|---|---|---|
| ARB-A | La collision physique peut empêcher une diagonale admise par le contrôle topologique S4/N2. | Il s'agit d'une **restriction postérieure explicite** à S4/N2 ; géométrie détaillée ouverte. |
| ARB-B | Les corps morts ou inconscients ne bloquent ni le passage ni la destination de la marche ordinaire. | Exception à la formulation historique S10 ; volumes conservés pour MEC-0002. |
| ARB-C | Ouverture explicite des portes ; accès entre niveaux par connexions définies pour escaliers/échelles, états/connexions pour ascenseurs. | Coûts et détails d'interaction ouverts ; sauts et chutes relèvent de MEC-0002. |
| ARB-D | Reprise de TU : **min(solde + récupération, TU max)**, puis application du facteur de surcharge au **total plafonné** ; énergie récupérée séparément. | Formule exacte du facteur, Force→kg, arrondis et valeurs ouverts ; aucun surcoût par pas lié à la charge. |
| ARB-E | Un tir de réaction effectivement tiré pendant une marche interrompt l'ordre, même manqué ou non incapacitant ; pas achevé payé une seule fois ; pivot sans tir insuffisant. | Système Overwatch complet encore ouvert ; aucune conversion des UT de kowlting. |
| G1 | La diagonale physique passe par un passage orthogonal praticable, en **un seul pas diagonal**. | Une unité consciente voisine peut bloquer réellement le passage mais pas automatiquement en tant que mur ; dimensions/trajectoires détaillées ouvertes. |
| G2 | Réveil sur case occupée : repositionnement automatique vers une case voisine libre et accessible, **sans TU de marche** ; sans case disponible, conscience retrouvée sur place, **au sol**, sans relèvement tant que case occupée. | Choix parmi plusieurs cases, corps sur case candidate, posture technique et contacts transitoires ouverts. |
| G3 | Chaque pas de marche ordinaire demande des TU **et** de l'énergie ; zone atteignable Z1 et paiement du pas vérifient les deux ressources. | Modification postérieure explicite de Z1 et de la portée de N14 ; barèmes ouverts ; pas de coût d'énergie ajouté aux esquives ES-09/10. |
| G4 | Parmi les chemins réalisables, minimiser d'abord les TU, ensuite l'énergie, puis appliquer un départage déterministe. | Clé exacte de départage et algorithme de recherche sur grille ouverts. |

**Preuve de validation :** les échanges du 17 novembre et leurs citations reprises dans le §1.2 du dossier v1.4.1, notamment la validation globale « Je valide » après la présentation G1 à G4. Ne jamais présenter une citation du dossier comme si elle figurait déjà dans le registre.

## 3. Fichiers autorisés à modifier par le présent mandat

1. **`docs/gameplay/GAMEPLAY-DECISIONS.md`** : dans MEC-0001 seulement, ajouter un bloc daté des décisions ARB-A…E et G1…G4 ; **annoter S4/N2, S10, Z1 et N14** en distinguant rédaction historique et décisions postérieures ; actualiser uniquement les points « Encore ouvert » désormais tranchés, conserver chaque sous-question non décidée. Préserver le statut « fiche incomplète / mécanique globale reportée / aucune implémentation autorisée ». Ne pas modifier les décisions de MEC-0002 ni leurs effets.
2. **`docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md`** : ajouter **un court bandeau d'avertissement historique** pointant vers la consolidation v1.4.1, en précisant que certains attendus ne sont plus des oracles actuels (notamment T-M05, T-M09, T-M11 et tests relatifs à MEC-0002). Ne pas réécrire ni supprimer la matrice ancienne.
3. **`docs/references/OXCE-BASELINE.md`** : corriger **uniquement** l'énoncé obsolète selon lequel MEC-0001 serait la seule fiche : MEC-0002 est également documentée, sans que les deux mécaniques soient globalement acceptées. Préserver le commit de référence figé et la politique de propriété intellectuelle.
4. **`docs/reviews/`** : livrer le rapport d'exécution documentaire requis par `CLAUDE.md` (chemins modifiés, références vérifiées, diff, contrôles effectués avec sorties et codes de retour, limites). Le nom du rapport est à choisir sans écraser un ancien rapport.

Aucun autre fichier à modifier sans mandat complémentaire. En particulier **aucun fichier de code, test exécutable, asset ou donnée d'équilibrage**.

## 4. Conditions d’exécution de ce lot validé

Avant toute écriture :

- **Autorisation reçue** pour les seules modifications locales du §3 par « Je valide » du 17 novembre 2026 ; tout élargissement du périmètre requiert une nouvelle autorisation.
- Appliquer `CLAUDE.md` ; faire `git fetch origin main` au démarrage du lot si autorisé ; travailler sur **une branche dédiée**, jamais sur `main`.
- **Aucun commit, push ou publication dans ce lot.** Une approbation séparée précisant la branche et les opérations Git sera nécessaire. Aucune fusion vers `main` n'est autorisée.
- Lire les versions réelles du dépôt avant de préparer le diff ; si elles divergent du dossier, signaler les écarts et s'arrêter sur ce qui changerait la substance.
- Ne pas réinterpréter les règles ouvertes, ne pas compléter les paramètres numériques, ne pas déduire la validation globale de MEC-0001.

## 5. Vérifications attendues

- Les neuf décisions sont présentes, datées, traçables et correctement qualifiées comme **sous-décisions acceptées**, sans autorisation de gameplay.
- Les quatre interfaces historiques **S4/N2, S10, Z1, N14** sont expressément annotées ; S5 reste historique et supplantée par Z1.
- Aucun montant de TU ou d'énergie issu des jeux de référence n'est inscrit comme équilibrage de Bastion ; exemples de tests restent fictifs.
- Les corps restent physiquement pertinents pour MEC-0002 et non bloquants pour la marche ; la distinction marche/esquive/repoussement/saut est maintenue.
- Les changements de niveau par marche n'interdisent pas les chutes et sauts MEC-0002 ; portes explicites correctement identifiées comme écart à OXCE.
- Les points ouverts restent ouverts (valeurs, géométrie détaillée, case portant un corps pour G2, Overwatch complet, algorithme G4, etc.).
- Le diff ne contient que les fichiers autorisés ; rapport de travail vérifiable ; aucun gameplay exécuté ou revendiqué comme testé.

## 6. Livrable et fin de lot

Produire un seul jeu de changements documentaires locaux, sur branche dédiée, avec un rapport de vérification dans `docs/reviews/`. Fournir le nom de la branche, la liste des fichiers modifiés, le diff et les sorties/codes de retour réellement observés. **Ne pas annoncer de rapport publié ni de PR créée**, car aucun commit ou push n’est autorisé. **Stop à la fin du lot.** La qualification globale de MEC-0001, l’équilibrage, l’implémentation, le commit, la publication et la fusion restent des étapes distinctes, chacune nécessitant son propre accord.
