# BASTION — Mandat LOT-2H v1.0
## Préparer l'inscription des arbitrages DS1 à DS5 dans MEC-0001 — sans toucher au registre

**Statut : PRÉPARÉ POUR EXÉCUTION SUR AUTORISATION DU PROPRIÉTAIRE.**  
**Nature : documentaire uniquement, aucune décision nouvelle ni modification du registre protégé.**  
**Dépôt :** `mengpo1/bastion`.  
**Base de travail :** `main` au dernier état récupéré avec `git fetch origin main`.  
**Branche de travail suggérée :** `docs/lot-2h-preparation-inscription-mec-0001`.  
**Publication :** aucun `push`, PR ou fusion sans approbation explicite distincte du propriétaire.

## 1. Objectif

Préparer une **proposition complète, relisible et traçable d'inscription au registre de gameplay** des décisions **déjà prises** sur DS1 à DS5 après LOT-2G. Il ne s'agit pas d'approuver par défaut les propositions encore ouvertes ni de considérer MEC-0001 comme globalement acceptée.

**Le registre protégé ne doit pas être édité lors de LOT-2H.** Livrer le texte ou le diff **proposé**, dans un document non protégé, pour revue et validation ultérieure.

## 2. Sources obligatoires et priorité

1. `CLAUDE.md` sur `main` : rôles, protection du registre, Git, revue, arrêt de mandat.
2. `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` sur `orchestration/mandats` : **transcription de référence des arbitrages récents du propriétaire** ; vérifier le contenu et l'empreinte avant de l'archiver.
3. `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` : registre de référence à **lire sans écrire** ; statut global MEC-0001 encore « reportée ».
4. `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` et `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md` sur `main` : règles précédemment exprimées et tests.
5. `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md` et `docs/reviews/LOT-2G-IMPACTS-TESTS.md` sur la branche **`docs/lot-2g-mec-0001-arbitrages`** (PR n° 10, tant qu'elle n'est pas fusionnée). Lire cette branche **sans la fusionner** ; ses recommandations restent non validées sauf reprises explicitement dans le document du propriétaire.
6. `docs/references/OXCE-BASELINE.md` sur `main` si une affirmation technique à propos d'OXCE doit être citée.

**Règle de priorité :** décision explicite récente du propriétaire > proposition de Claude. Les décisions antérieures encore en vigueur ne doivent pas être réinterprétées silencieusement. Tout désaccord apparent devient un écart à expliquer, non une correction arbitraire.

## 3. Travail demandé

### A — Préparer la transcription, sans décision nouvelle

- Reconstituer précisément les décisions DS1, DS2, DS3, DS4 et DS5 figurant dans la consolidation, en gardant leurs restrictions.
- Établir une matrice de traçabilité : décision ; phrase/élément du document source ; ancienne règle touchée (S, N, J, P, D, K ou E) ; statut actuel dans le registre ; texte proposé ; statut (« accepté en conversation », « à définir », « conflit/écart »).
- Rédiger une **proposition de rédaction** pouvant être copiée plus tard dans la fiche MEC-0001, mais **sans l'y écrire**.
- Ne pas marquer MEC-0001 « acceptée » globalement, ne pas changer sa classe ni son état d'implémentation.
- Ne pas présenter les 13 points E1…E24 comme intégralement résolus : distinguer le choix de principe de la formule/valeur encore ouverte.
- Ne pas reprendre automatiquement les calculs du LOT-2G lorsqu'ils supposent une vitesse de décollage indépendante de la masse (DS2 rejeté par le propriétaire).

### B — Traiter explicitement les risques de contradiction

Vérifier au minimum :

1. **DS1 et P07 :** exception limitée au sol quitté par l'unité pendant son saut.
2. **DS2 et E11/P04/P05 :** poids qui réduit hauteur **et** distance ; masse de référence et formule non décidées ; ne pas adopter E11 tel que proposé dans LOT-2G.
3. **DS3 et D01/D03/N7/E18 :** pas de dégâts pour l'unité tombante après un étage **sans surcharge**, possibilité de dégâts chez une unité percutée ; chute de plusieurs étages non exonérée. Séparer « puissance de base » et « dégât réellement appliqué ».
4. **DS3 et E12 :** ne pas déclarer choisi le nombre exact de niveaux franchis ; la conversation n'a pas directement tranché ce point. Ne pas inventer de règle pour moins d'un étage.
5. **DS4 et E6/N9/N10/E24 :** masse relative protégeant la plus lourde en collision **entre unités**, sans écraser le rôle aggravant du poids lors d'une chute au sol.
6. **DS4 et E8 :** dépendance vitesse normale au carré, type « impact » et **tirage aléatoire commun** pour unité/obstacle ; distinguer les coefficients encore ouverts.
7. **DS5 et K07/S10 :** cible repoussée **après collision non esquivée** ; pas de déplacement d'esquive préalable ; attaquant sur la case cible si repoussement possible, sinon retombée à proximité (rayon et cas impossible non décidés).
8. **DS5 et E9/E13/E17 :** monde figé hors esquive/chutes, arrêt au premier choc, grandes unités exclues provisoirement, coût complet à l'engagement, esquive par TU restantes et huit voisines ; données de coûts et de visibilité non fixées.

Les incertitudes doivent rester formulées sans valeurs fictives présentées comme finales.

### C — Préciser les validations encore nécessaires

Produire une courte table « **à arbitrer avant inscription exhaustive ou implémentation** » : loi masse/hauteur/portée ; surcharge et exemption d'un étage ; dimensions et gravités ; facteurs de dégâts ; cas de collision sans case libre ; tarif du saut ; calcul de la probabilité d'esquive ; valeur/côté d'armure et interactions avec le terrain.

Ne pas provoquer de nouveaux choix du propriétaire pendant ce lot : les regrouper dans la table pour une conversation ultérieure.

## 4. Livrables autorisés sur la branche locale

1. `docs/mandates/BASTION-MANDAT-LOT-2H-PREPARATION-INSCRIPTION-v1.0.md` — **copie exacte** du présent mandat depuis `orchestration/mandats`.
2. `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` — **copie exacte** de la consolidation depuis `orchestration/mandats`.
3. `docs/mandates/README.md` — ajout minimal pour indexer ces deux documents et leurs SHA-256 ; ne pas altérer les entrées historiques.
4. `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md` — texte proposé pour le registre, avec statut « PROPOSITION DOCUMENTAIRE — NON INSCRITE ».
5. `docs/reviews/LOT-2H-TRACABILITE-ECARTS.md` — matrice de correspondance décisions, sources, règles antérieures et questions ouvertes.
6. `docs/reviews/LOT-2H-EXECUTION.md` — rapport de contrôle, limites et revue indépendante.

Ne modifier **aucun autre fichier**. Si un livrable de même nom existe déjà, ne pas écraser sans demande préalable.

## 5. Interdictions

- Aucune écriture dans `docs/gameplay/GAMEPLAY-DECISIONS.md`, `docs/decisions/`, `docs/references/`, `CLAUDE.md`, `src/`, `tests/`, `scripts/harness/`, `.claude/` ou `.github/`.
- Aucun changement de gameplay, test exécutable, équilibrage, moteur ou configuration.
- Aucun nouveau seuil, coefficient ou choix d'algorithme déclaré « accepté » sans message explicite du propriétaire.
- Aucune fusion de PR n° 10, aucune PR créée, aucune publication, aucun rebase ou merge de branche sans autorisation distincte.
- Aucun enchaînement vers un autre lot.

## 6. Vérifications et revue

- `git fetch origin main` ; branche dédiée depuis la base courante ; contrôler le `diff` exact.
- Vérifier les deux copies documentaires **octet pour octet** contre `origin/orchestration/mandats` (via `cmp` et SHA-256), sans corriger les espaces ou la ponctuation du texte archivé.
- Vérifier que chaque décision de DS1 à DS5 a une source et un statut ; relever les contradictions et les paramètres indéterminés.
- Exécuter les contrôles documentaires et les tests de harnais applicables ; décrire commandes, résultats et limites. Les tests .NET ne seront déclarés réussis que s'ils sont réellement exécutés.
- Solliciter un relecteur indépendant **en lecture seule**, chargé en particulier de vérifier qu'aucune formule optionnelle du LOT-2G n'a été présentée comme validée.
- Remettre le rapport final et **s'arrêter**. Les actions de publication éventuelles nécessitent une autorisation supplémentaire, limitée à la branche LOT-2H.

## 7. Condition de réussite

Le propriétaire peut lire le texte d'inscription proposé et identifier immédiatement :
- ce qu'il a effectivement validé ;
- ce qui reste à arbitrer ;
- les modifications qu'une future écriture au registre nécessiterait ;
- ce qui **n'a pas été modifié**.

**Fin impérative à la remise de la proposition documentaire. Pas d'inscription automatique au registre, ni d'implémentation.**
