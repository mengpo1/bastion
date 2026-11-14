# BASTION — Mandat LOT-2I v1.1
## Consolidation et préparation du diff de MEC-0002, sans écriture dans le registre

**Date de proposition et de publication :** 14 novembre 2026.  
**Statut :** **PUBLIÉ POUR PRÉPARATION — EXÉCUTION NON AUTORISÉE.**  
**Dépôt :** `mengpo1/bastion`.  
**Branche de publication :** `orchestration/mandats`.  
**Auteur du mandat :** orchestrateur ChatGPT.  
**Développeur documentaire envisagé :** Claude Code.  
**Objet :** mettre à jour le périmètre initial du mandat LOT-2I v1.0 après les arbitrages du propriétaire, **sans écraser le mandat v1.0 déjà publié**.

**Portée de la publication :** le propriétaire a autorisé le 14 novembre 2026 la publication du seul mandat v1.1 sur `orchestration/mandats`. Cette autorisation ne porte ni sur son exécution, ni sur la modification du registre, ni sur du code de gameplay, ni sur la création d'une PR ou une fusion.

## 0. Conditions préalables

- Lire `CLAUDE.md`, notamment la protection du registre et les règles d'autorisation d'exécution, publication, PR et fusion.
- Ne pas déduire de l'accord sur les mécaniques une autorisation d'écriture du registre ou de développement.
- Obtenir **un accord distinct du propriétaire** avant d'exécuter ce mandat sur une branche de travail ; obtenir des autorisations distinctes pour push, PR et fusion.
- Le v1.1 précise et remplace le **périmètre proposé** du v1.0 pour une éventuelle exécution future, mais le v1.0 reste intact comme archive historique. Si une incompatibilité dépasse ce périmètre, la signaler et demander un arbitrage.

## 1. Sources obligatoires

- `docs/gameplay/GAMEPLAY-DECISIONS.md` (`main`) ; statut de MEC-0001 « reportée » ; ne pas modifier.
- `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` et sa matrice de tests.
- `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md`.
- `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md`.
- `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md` et `LOT-2H-TRACABILITE-ECARTS.md`.
- Ancien mandat LOT-2I v1.0 sur `orchestration/mandats`.
- Consolidation provisoire de l'orchestrateur : `BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md`, **document local remis au propriétaire, non joint à cette publication GitHub**. Une copie exacte devra être fournie à l'exécutant avant le début du lot. La faire relire et vérifier contre les échanges du propriétaire ; ne pas la traiter comme une transcription infaillible.
- Messages d'arbitrage du propriétaire dans la conversation, y compris acceptation des 29 propositions et QCM 1A à 6A. Si ces messages ne sont pas accessibles à Claude Code, conserver la limite de preuve et demander une copie approuvée ; ne pas inventer une provenance.

## 2. Périmètre du lot

### Autorisé **après autorisation d'exécution**

1. Préparer la séparation documentaire :
   - MEC-0001 pour la marche, conservée « reportée » ;
   - MEC-0002 pour sauts, chutes, collisions, esquives associées et environnement physique lié.
2. Construire une **matrice de traçabilité exhaustive** des sous-règles : source primaire, date de la décision, formulation ancienne, règle courante, priorité, éventuel conflit, statut « validé en conception » ou « ouvert ».
3. Vérifier notamment les contradictions N7 / DS3, ancienne portée descendante P05 / nouvelle portée au même niveau, DS5 simultané / chutes FIFO, K07 / repoussement forcé, D12 / résistance cumulable, multi-cases DS5.5, coût saut simple / offensif, tirages communs et arrondis.
4. Proposer **un diff non appliqué** à `docs/gameplay/GAMEPLAY-DECISIONS.md` : annotation historique de MEC-0001 et nouvelle fiche MEC-0002, avec clauses « gameplay non autorisé », paramètres ouverts et références aux preuves. Ne pas faire passer une acceptation de conception pour une autorisation d'implémentation.
5. Rédiger les critères de tests futurs et un registre des ambiguïtés indispensables à arbitrer avant une implémentation déterministe.
6. Soumettre le tout à un relecteur indépendant **en lecture seule** et reporter ses conclusions, corrections et limites.

### Formellement interdit

- **Modifier** `docs/gameplay/GAMEPLAY-DECISIONS.md` ou tout autre registre protégé `docs/decisions/`, `docs/references/`.
- Modifier `src/`, `tests/`, `.claude/`, `scripts/harness/`, `.github/`, `CLAUDE.md`.
- Programmer, paramétrer ou équilibrer une mécanique ; créer des données provisoires présentant de nouvelles valeurs comme validées.
- Écraser / renommer le mandat LOT-2I v1.0 publié sur `orchestration/mandats`.
- Push, PR, fusion, suppression, rebase sans autorisations ciblées et vérifiables.

## 3. Livrables proposés

- `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` : spécification consolidée, états et sources.
- `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` : provenance, écarts, inventaire des règles et des tests futurs.
- `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md` : texte **proposé et non appliqué** pour le registre protégé, annotations historiques.
- `docs/reviews/LOT-2I-EXECUTION.md` : commandes, résultats réels, revue indépendante, limites, points à décider et absence d'autorisation d'implémentation.
- Une archive de ce mandat v1.1 dans `docs/mandates/` et mise à jour minimale de `docs/mandates/README.md`, **seulement si ce périmètre de fichiers est explicitement autorisé**.

Ne pas écraser un fichier existant. Nom de branche dédié à fixer par le mandat accepté. `git fetch origin main` en début de lot, jamais travailler directement sur `main`.

## 4. Contrôles de sortie

- Registre et sources protégées inchangés octet pour octet.
- Aucune modification du gameplay, de l'architecture ou du harnais.
- Chaque règle consolidée a une provenance et un statut clair ; aucune proposition numérique non validée glissée dans la fiche.
- Tous les écarts majeurs sont explicitement recensés ; N7 reste historiquement traçable.
- Revue indépendante et commandes réellement exécutées, sans déclarer des tests non lancés.
- Arrêt à la livraison documentaire et demande d'autorisation **distincte** avant toute inscription ou implémentation.

**Ce mandat publié est une préparation, pas une autorisation d'exécution.**
