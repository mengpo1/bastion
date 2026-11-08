# BASTION — Spécification du harnais de développement

**Version :** 0.2 (proposition à valider)  
**Date :** 8 novembre 2026  
**Phase :** Lot 0A — conception du harnais  
**Statut :** PROPOSÉ — aucune installation ni implémentation autorisée par ce seul document.

## 1. Mission

Créer un jeu de stratégie et de combat tactique inspiré d'OpenXcom Extended (OXCE), conservant la profondeur des systèmes de référence mais utilisant une interface et des graphismes modernisés. Certaines mécaniques feront l'objet de modifications profondes, **exclusivement après décision explicite du propriétaire du projet**.

Le harnais encadre les agents IA, le processus de développement, la preuve des comportements et la qualité du code. Il ne se substitue ni aux tests réels ni aux validations humaines.

## Règle fondamentale — Simplicité avant tout

**Rien d’alambiqué.** Dans la réflexion, les décisions, le code, l’architecture, les outils et le processus de développement, choisir **la solution la plus simple qui répond réellement au besoin**. Privilégier la clarté, la lisibilité et la facilité de maintenance ; refuser la suringénierie, les abstractions prématurées et les couches ou procédures sans utilité démontrée. Toute complexité jugée indispensable doit être expliquée simplement et justifiée avant sa mise en œuvre. **Cette règle s’impose à ChatGPT comme à Claude Code et aux relecteurs.**

## 2. Rôles et autorités

| Rôle | Titulaire | Autorité |
|---|---|---|
| Propriétaire / décideur | Utilisateur | Valide/refuse toute modification de mécanique et les jalons. Autorise intégration et publication. |
| Orchestrateur | ChatGPT | Analyse, rédige les mandats, définit critères, examine les preuves, prépare les arbitrages. Ne valide pas à la place du propriétaire. |
| Développeur | Claude Code | Exécute uniquement le mandat courant dans une branche dédiée, teste et rapporte les résultats. |
| Relecteur indépendant | Agent distinct du développeur, mandaté ponctuellement | Relit le diff, les risques, les tests et la conformité au mandat ; ne s'auto-accorde pas la validation finale. |
| Contrôles automatiques | Hooks + scripts + CI | Vérifient les règles contrôlables par machine ; leurs résultats sont des preuves partielles. |

### Interdictions permanentes

- Aucun changement intentionnel des mécaniques, aucune simplification de règles, aucun changement d'équilibrage sans décision explicite du propriétaire.
- Une idée figurant dans une conversation **n'est pas** une décision validée.
- Aucun commit direct sur `main`, aucune fusion, aucun push distant, aucune publication ni suppression destructive sans autorisation adaptée au mandat.
- Le développeur ne modifie pas les règles de gouvernance pour contourner un contrôle ; toute évolution du harnais fait l'objet d'un mandat distinct.
- Pas d'affirmation de « fidélité OXCE » sans référence vérifiable et tests comportementaux appropriés.
- Pas de copie automatique des assets originaux, ni de réutilisation de code OXCE sans analyse des licences et de leurs implications pour le projet.

## 3. Deux registres distincts

### 3.1 Registre des mécaniques : `docs/gameplay/GAMEPLAY-DECISIONS.md`

Une ligne par mécanique ou modification, avec :

- `ID` permanent (ex. `MEC-0001`)
- `Système` et `Description`
- `Classe` : `OXCE-REFERENCE`, `MODIFICATION-PROPOSEE`, `MODIFICATION-VALIDEE`, `A-VERIFIER`
- `Fonctionnement de référence` et preuves (commit OXCE, fichiers, documentation, reproduction expérimentale)
- `Changement demandé` ; raisons et impacts prévus
- `Décision du propriétaire` (acceptée/refusée/reportée), **preuve de validation explicite et date**
- `Périmètre autorisé` / éléments exclus
- `Tests de référence` et `Tests de modification`
- `État d'implémentation` : non commencé / en cours / testé / intégré

La **classe** d'une mécanique et son **état d'implémentation** ne doivent pas être confondus.

Une mécanique `MODIFICATION-PROPOSEE` ou `A-VERIFIER` n'autorise aucun changement de comportement. Une mécanique `MODIFICATION-VALIDEE` n'autorise que le périmètre décrit et approuvé.

### 3.2 Registre des décisions techniques : `docs/decisions/TECHNICAL-DECISIONS.md`

Documenter séparément : langage, moteur, bibliothèques, structures de données, formats d'échange, stockage et performances. Tout choix non validé reste une **proposition**, sans être présenté comme une décision définitive.

## 4. Référence OXCE et traçabilité

1. Identifier le dépôt et la branche de référence ; figer un **hash de commit** exact avant l'analyse des mécaniques.
2. Noter la version correspondante et la portée de la référence (OXCE seul ou avec un mod particulier).
3. Pour chaque règle à reproduire, conserver : source, hypothèse, niveau de preuve et scénario de comparaison.
4. Distinguer : **observé en jeu**, **déduit du code**, **documenté**, **non vérifié**.
5. Les tests de Bastion doivent viser des comportements observables, pas seulement recopier une implémentation interne.
6. Garder OXCE comme référence de comportement et non comme dépendance implicite du moteur Bastion.

**Point de vigilance juridique :** la consultation et la reprise éventuelle du code sous GPL peuvent avoir des implications pour la redistribution et les obligations de licence. Réaliser un audit des licences avant toute réutilisation de code ou de ressources. Aucun asset propriétaire d'X-COM n'est inclus dans le projet par défaut.

## 5. Architecture cible (à confirmer lors de l'audit 0B)

```text
bastion/
├── CLAUDE.md                        # Règles permanentes pour Claude Code
├── README.md
├── global.json                      # SDK .NET épinglé
├── Bastion.sln
├── src/
│   ├── Bastion.Domain/             # Entités, valeurs, événements — aucun Godot
│   ├── Bastion.Simulation/         # Règles tactiques et stratégiques — aucun Godot
│   ├── Bastion.Content/            # Chargement / validation des données
│   └── Bastion.Godot/              # Scènes, contrôleurs, rendu, UI
├── tests/
│   ├── Bastion.Domain.Tests/
│   ├── Bastion.Simulation.Tests/
│   ├── Bastion.Content.Tests/
│   └── Bastion.Integration.Tests/
├── docs/
│   ├── architecture/
│   ├── gameplay/GAMEPLAY-DECISIONS.md
│   ├── decisions/TECHNICAL-DECISIONS.md
│   ├── references/OXCE-BASELINE.md
│   ├── mandates/
│   └── reviews/
├── .claude/
│   ├── settings.json
│   ├── agents/
│   └── rules/
├── .github/workflows/
└── scripts/harness/
```

**Invariants d'architecture :**

- `Domain` et `Simulation` ne référencent ni Godot ni des classes de rendu.
- La simulation est pilotée par des commandes explicites et produit un état / des événements observables.
- Hasard injecté ou graine contrôlée ; horloge injectable ; résultats de tests reproductibles.
- Les données de contenu ne sont pas confondues avec le code de simulation.
- Le rendu peut changer sans modifier l'issue des calculs de combat.
- Interfaces entre systèmes documentées ; dépendances de projet dirigées vers le noyau et non l'inverse.
- Godot 4 .NET et .NET 10 LTS sont la **cible proposée** ; leurs versions exactes et la compatibilité des dépendances doivent être validées lors de l'installation.

## 6. Format obligatoire d'un mandat Claude Code

Chaque mandat possède :

1. Identifiant `LOT-NN` et titre.
2. **Objectif unique** et justification.
3. Préconditions, branche Git, références de décisions approuvées.
4. Liste précise des fichiers / couches autorisés.
5. Travaux à réaliser et **travaux explicitement exclus**.
6. Critères d'acceptation mesurables, dont tests négatifs.
7. Commandes de vérification et sortie attendue.
8. Conditions d'arrêt et cas nécessitant arbitrage humain.
9. Livrables : diff, tests, limites, risques, rapport de fin.

Si une ambiguïté touche une mécanique de jeu : **arrêter cette partie du mandat** et demander un arbitrage, sans inventer un comportement provisoire qui se retrouverait implicitement validé.

## 7. Cycles de travail

1. ChatGPT rédige et circonscrit le mandat.
2. Le propriétaire approuve le périmètre lorsqu'une décision de gameplay ou un jalon sensible l'exige.
3. Claude Code réalise une branche dédiée ; tests et vérifications locales.
4. Un relecteur indépendant examine le diff et les preuves, sans réécrire le code pendant la revue.
5. ChatGPT confronte les résultats aux critères et signale les écarts.
6. Le propriétaire décide des arbitrages et de l'intégration.
7. Les documents d'architecture, de décisions et de tests sont actualisés dans la même demande que le code concerné.

**Aucune preuve de conformité par la simple déclaration « tests OK ».** Exiger les commandes exécutées, codes de sortie, nombres de tests et, si nécessaire, scénario reproduit.

## 8. Contrôles prévus

### 8.1 Hooks Claude Code (exécutés localement, configurés dans `.claude/settings.json`)

| Hook | Rôle | Comportement voulu |
|---|---|---|
| `SessionStart` | Charger contexte du mandat, branche, décisions pertinentes et statut Git | Informatif, en lecture seule |
| `PreToolUse` | Inspecter les écritures ou commandes sensibles | Bloquer les chemins interdits, actions destructives ou écritures sur fichiers protégés selon règles explicites |
| `PostToolUse` | Signaler les fichiers changés et vérifier rapidement formats / règles simples | Rapide, non destructif, sortie claire |
| `Stop` | Vérifier la présence d'un rapport de mandat et rappeler les contrôles non exécutés | Ne doit pas provoquer une boucle infinie ni masquer les échecs |
| `SubagentStop` | Vérifier qu'une revue attendue a produit son rapport | Signaler l'absence de preuve, pas auto-approuver |

Les hooks utilisent des scripts versionnés dans `scripts/harness/`, analysent le JSON reçu sur stdin, traitent les chemins et arguments comme non fiables et disposent de tests unitaires. **Pas de secrets dans leurs sorties.**

Ne pas lancer une compilation complète après chaque édition : les tests coûteux sont exécutés aux points de contrôle et dans la CI.

**Limite explicite :** ni un hook `PreToolUse` ni un contrôle de diff ne prouvent l'absence de changement sémantique de gameplay. Les règles critiques reposent aussi sur tests, revue et approbation. Les hooks ne constituent pas à eux seuls une barrière de sécurité contre un agent délibérément malveillant.

### 8.2 Qualité C# et tests

- Compilation avec warnings traités selon politique documentée (idéalement `WarningsAsErrors` pour le code maîtrisé).
- Formattage vérifié, analyse statique et compilation Release.
- Tests unitaires déterministes de chaque règle métier ; tests de propriétés et cas limites quand adaptés.
- Tests d'intégration des interactions entre systèmes.
- Tests de non-régression basés sur scénarios / « golden cases » validés.
- Tests Godot (scènes, entrée, affichage minimal) dans un dispositif séparé du noyau ; ne pas prétendre qu'ils sont couverts par `dotnet test` si ce n'est pas vrai.
- Toute correction de bug comporte un test qui échouait avant correction, lorsque possible.
- Mesure de couverture éventuelle **indicative**, jamais substitut à l'examen des comportements.

### 8.3 Git et CI

- Travail par branches courtes et fusion par revue ; `main` protégée dès qu'un dépôt distant est disponible.
- Pipeline CI : restauration épinglée, compilation, vérification de format, analyse statique, tests, contrôle des dépendances, validation du registre des décisions.
- Relever les versions SDK / moteur et verrouiller les dépendances lorsque possible.
- Aucun secret commité ; vérification explicite des fichiers sensibles / des secrets.
- CI verte nécessaire, mais **insuffisante seule** pour autoriser une fusion.
- Tests et hooks ne peuvent pas être supprimés ou neutralisés discrètement dans un mandat de développement.

## 9. Qualification du harnais : essais de défaillance

Le lot 0C ne sera accepté que si les essais suivants sont **effectivement exécutés** et consignés.

| ID | Injection volontaire (branche de test jetable) | Résultat attendu |
|---|---|---|
| H-Q01 | C# qui ne compile pas | Build/CI rouge ; intégration interdite |
| H-Q02 | Assertion de test volontairement fausse | Pipeline rouge ; test signalé |
| H-Q03 | Écart sur une règle avec scénario de référence connu | Test de comparaison en échec |
| H-Q04 | Tentative d'écriture sur registre de décisions protégé ou hors périmètre | Hook / droits signalent ou bloquent selon chemin ; contrôle CI en seconde ligne |
| H-Q05 | Modification de gameplay sans ID de décision approuvée | Rejet par vérification de traçabilité **et revue humaine** ; pas de garantie purement automatique |
| H-Q06 | Rapport de fin absent / sans commandes de test | Mandat déclaré incomplet |
| H-Q07 | Relecteur repère une modification hors mandat | Rejet documenté avant intégration |
| H-Q08 | Tentative de contournement de la configuration du harnais | Contrôles de fichiers sensibles et revue déclenchés |
| H-Q09 | Réexécution d'un scénario déterministe à graine fixe | Résultats identiques sur environnement de référence |
| H-Q10 | Vérification du lancement headless du projet Godot lorsque disponible | Démarrage sans erreur bloquante ou limitation documentée |

## 10. Critères de sortie des lots

**Lot 0A — Conception :**

- Spécification présente, limites et exigences explicites.
- Arbitrages techniques non vérifiés marqués « à confirmer ».
- Accord du propriétaire pour passer à 0B.

**Lot 0B — Installation :**

- Dépôt et fichiers de gouvernance créés.
- Hooks installés et testables, scripts versionnés.
- Solution C# minimale compilable, projets de tests vides ou tests fumée sans gameplay.
- CI configurée avec preuve d'exécution.
- Aucune mécanique de combat implémentée.

**Lot 0C — Qualification :**

- Essais H-Q01 à H-Q10 exécutés ou reportés avec justification et risque explicite.
- Rapports d'exécution et artefacts conservés.
- Failles du dispositif listées, corrigées ou acceptées par décision.

**Lot 0D — Acceptation :**

- ChatGPT synthétise les résultats et les limites.
- Propriétaire autorise explicitement le premier mandat de développement.

## 11. Points à confirmer, sans blocage du lot 0A

1. Environnement cible de développement : système d'exploitation principal de la machine hébergeant Claude Code et Godot.
2. Dépôt Git distant : GitHub ou autre ; réglages de protection et permissions.
3. Version précise de Godot .NET compatible avec le SDK cible et les extensions de tests.
4. Source OXCE exacte (branche + hash), politique de mods et licence de Bastion.
5. Choix final du framework de tests C# et des tests de scènes Godot.
6. Politique de revue indépendante : outil / modèle, accès en lecture seule et périmètre.

Ces choix doivent être clarifiés ou investigués pendant le lot 0B. En cas d'incertitude, ils ne doivent pas être présentés comme des faits acquis.

## 12. Premier mandat prévu, **non encore autorisé**

**LOT-0B — Installation technique du harnais**

À rédiger en version exécutable **seulement après validation de cette spécification**. Il comportera : inventaire de l'environnement, création du dépôt sans gameplay, configurations et scripts vérifiés, tests de fumée, première CI et rapport des limites. Exclure explicitement toute implémentation des mouvements, tirs, dégâts, IA et contenu d'OXCE.

---

### Sources consultées pour la faisabilité (documentation éditeur)

- Anthropic, hooks de Claude Code : <https://code.claude.com/docs/en/hooks>
- Anthropic, fichiers de configuration : <https://code.claude.com/docs/en/settings>
- Anthropic, agents spécialisés : <https://claude.com/blog/subagents-in-claude-code>
- Microsoft, politique de support .NET : <https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core>
- Godot, documentation officielle : <https://docs.godotengine.org/>

*Cette spécification est une proposition d'organisation, et non une preuve que les contrôles ont déjà été installés ou exécutés.*
