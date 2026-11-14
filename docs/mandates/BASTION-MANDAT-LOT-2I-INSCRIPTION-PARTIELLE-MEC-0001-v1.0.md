# BASTION — Mandat LOT-2I v1.0
## Inscription partielle des décisions de conception dans le registre MEC-0001

**Statut : PRÉPARÉ — EXÉCUTION ET ÉCRITURE DANS LE REGISTRE NON AUTORISÉES.**  
**Nature :** opération documentaire contrôlée, avec modification envisagée du registre protégé **uniquement après validation explicite et datée du propriétaire**.  
**Dépôt :** `mengpo1/bastion`.  
**Branche de mandat :** `orchestration/mandats` (présent fichier uniquement).  
**Branche de travail proposée :** `docs/lot-2i-inscription-partielle-mec-0001`, depuis `origin/main` après `git fetch origin main`.  
**Publication de la branche de travail, PR et fusion :** permissions distinctes nécessaires.  
**Aucun code de gameplay, aucun test exécutable de gameplay dans ce lot.**

## 0. Condition absolue de démarrage

**Ne pas exécuter ce mandat sur la base du seul fait qu'il a été préparé ou publié.**

Avant toute écriture dans `docs/gameplay/GAMEPLAY-DECISIONS.md`, obtenir un message explicite et daté du propriétaire couvrant le **texte final** et le **périmètre de l'inscription**, et réglant les décisions de portée encore ouvertes ci-dessous :

1. **Confirmation de la transcription DS1 à DS5** : `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` et `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md`. La validation du *travail documentaire* de LOT-2H ne signifie pas, à elle seule, autorisation d'éditer le registre.
2. **LOT-2F et correctif du 9 novembre** : préciser si les décisions P/J/K/D/I et E14/E18/E23, citées mais pas encore inscrites dans le registre, doivent être inscrites dans ce lot, dans un autre lot ou simplement référencées sans changement de statut. Ne pas les déclarer inscrites automatiquement.
3. **Rattachement des mécaniques** : obtenir le choix entre conserver les sauts, chutes et collisions comme sous-partie de `MEC-0001 — Déplacement élémentaire à pied` et utiliser une fiche distincte. Ne pas inventer d'identifiant permanent `MEC-NNNN` sans décision.
4. **K07 versus DS5.3** : confirmer explicitement que « cible immobile » après esquive ratée signifie **absence de mouvement d'esquive**, sans empêcher un **repoussement postérieur à l'impact** lorsqu'une case voisine est libre ; sinon, suspendre l'inscription définitive de DS5.3.
5. **N7 et l'historique LOT-2F** : confirmer le traitement proposé : conserver la règle N7 existante, ajouter une annotation de précision par DS3.1–DS3.4, et laisser les anciennes formulations H01/E21 identifiées comme historiques/à requalifier, sans retoucher silencieusement LOT-2F.

**Si une confirmation manque**, demander l'arbitrage et s'arrêter pour le périmètre correspondant ; aucune présomption d'acceptation. Les 15 sujets chiffrés et algorithmiques du LOT-2H `5 ne sont **pas** tous des prérequis à une transcription *partielle* ; ils restent ouverts et ne doivent pas bloquer artificiellement l'inscription des principes non contestés.

## 1. Références à lire

- `CLAUDE.md` (en particulier `3 : décision « acceptée », explicite et datée, obligatoire avant tout gameplay ; protection des registres).
- `docs/gameplay/GAMEPLAY-DECISIONS.md` sur `main` : fiche `MEC-0001` aujourd'hui « reportée », classe `MODIFICATION-PROPOSEE`, état « non commencé », aucun gameplay autorisé.
- `docs/reviews/LOT-2H-PROPOSITION-INSCRIPTION-MEC-0001.md` sur `main` : texte proposé pour le registre, **diff non appliqué** et 15 points ouverts.
- `docs/reviews/LOT-2H-TRACABILITE-ECARTS.md` et `docs/reviews/LOT-2H-EXECUTION.md` : 25 principes, écarts, limitations.
- `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` sur `main` : texte du propriétaire qui prime sur toute proposition de formule.
- `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` et matrice de tests ; `docs/reviews/LOT-2G-ARBITRAGES-MEC-0001.md` et impacts, tous intégrés dans `main`.
- `docs/references/OXCE-BASELINE.md` pour les comparaisons explicites ; aucun transfert de code ou d'assets OXCE.

Un texte contenu dans LOT-2F ou LOT-2G mais désigné « proposition », « ouvert », « à définir » ou « à confirmer » **ne devient pas accepté par reprise dans le registre**.

## 2. Travail envisagé après autorisation spécifique

### A — Inscription fidèle et limitée

- Vérifier les confirmations de la section 0 et leur provenance (date et formulation exacte).
- Recalculer le diff proposé par LOT-2H `4 contre le `main` réel (ne jamais forcer un patch si la base a changé).
- N'inscrire que les règles que le propriétaire a explicitement confirmées, en préservant leur statut **partiel**. Renvois à des décisions historiques non inscrites : les qualifier clairement, ne pas les présenter comme déjà présentes dans la fiche.
- Maintenir `MEC-0001` **« reportée » dans son ensemble** ; classe `MODIFICATION-PROPOSEE` ; état « non commencé » ; périmètre « aucun changement de gameplay ». Ne pas ajouter de champ `MODIFICATION-VALIDEE` pour le gameplay tant qu'une tranche d'implémentation n'a pas été approuvée dans un mandat distinct.
- Conserver les sous-décisions antérieures S1–S12, Z1, N1–N14 et leurs annotations ; ne pas réécrire leur historique.
- Signaler les paramètres ouverts (poids/portée, gravité, dégâts, choix des cases, TU, esquive). Aucun chiffre, formule de collision, paramètre ou comportement suppléé par l'agent.
- Pour toute règle nécessitant un arbitrage supplémentaire, **ne pas fabriquer de choix** ; conserver la mention ouverte, ou suspendre l'inscription du passage si elle serait trompeuse.

### B — Vérifications obligatoires

- S'assurer que **DS2** signifie « plus lourd = moins haut **et** moins loin » ; ne pas adopter l'hypothèse de vitesse égale du LOT-2G.
- S'assurer que **DS3** exonère l'unité tombante après **un étage sans surcharge**, mais non la cible percutée ; le mode de comptage des étages reste ouvert.
- S'assurer que **DS4** a un effet relatif des masses et un tirage **commun uniquement entre unité et obstacle**, sans extrapoler à une collision entre deux unités.
- S'assurer que **DS5** distingue l'esquive manquée de la poussée après collision et conserve le cas du repli de l'attaquant ; ne pas inventer le rayon ou une recherche de cases.
- Vérifier que les formules, seuils et autres valeurs non acceptés du LOT-2G ne se retrouvent pas dans le registre comme décisions.

### C — Préparer la transition vers le premier développement

Dans le rapport, ajouter **une page maximum** intitulée `MEC-0001 — tranche de développement initiale possible`, sans écrire de code ni modifier le registre davantage. Elle doit identifier :
- les règles de déplacement horizontal déjà **précises et approuvées** (notamment S1–S4, S10 et Z1) ;
- les dépendances vraiment indispensables à un premier test en C# (par exemple coûts de case, capital TU, sélection des destinations, tests minimaux), **en distinguant faits du registre et propositions** ;
- une **tranche minimale** cohérente de gameplay que le propriétaire pourrait accepter plus tard, sans reprendre les sauts, collisions, gravité ou dégâts non spécifiés ;
- les décisions d'autorisation et la trace de tests nécessaires pour ce futur développement.

Cette page n'autorise aucune mécanique ; elle sert au mandat de développement suivant. Ne pas ouvrir un nouveau chantier de recherche ni résoudre les 15 sujets ouverts pour produire cette page.

## 3. Fichiers autorisables lors de l'exécution

- `docs/mandates/BASTION-MANDAT-LOT-2I-INSCRIPTION-PARTIELLE-MEC-0001-v1.0.md` : archive **exacte** du mandat publié sur `orchestration/mandats`, avec empreinte.
- `docs/mandates/README.md` : ajout minimal d'une ligne d'index pour cette archive.
- `docs/gameplay/GAMEPLAY-DECISIONS.md` : **seul fichier de registre susceptible d'être modifié, et uniquement sur autorisation explicite de `0**.
- `docs/reviews/LOT-2I-INSCRIPTION-MEC-0001.md` : tableau avant/après, autorisation exacte, décisions inscrites/non inscrites, diff, réconciliation K07/N7, réserve.
- `docs/reviews/LOT-2I-EXECUTION.md` : commandes et codes de sortie, rapport de contrôle, revue indépendante et page de transition (`2 C).

Aucun autre fichier ; si un nom existe déjà, s'arrêter sans écrasement.

## 4. Contraintes techniques et contrôle de conformité

- Branche dédiée depuis `main` après `git fetch origin main` ; aucune écriture directe sur `main`.
- Aucune modification de `src/`, `tests/`, `.claude/`, `scripts/harness/`, `.github/`, `CLAUDE.md` ou des autres registres protégés.
- `git diff --check`, analyse des fichiers modifiés et de la traçabilité ; `dotnet build`, `dotnet test`, `dotnet format --verify-no-changes`, `bash scripts/harness/test-hooks.sh` si disponibles, sans annoncer de succès non observé.
- Relecteur indépendant en lecture seule : vérifier la preuve d'autorisation ; la conservation de « reportée » ; les 25 principes validés selon leur périmètre ; l'absence de nouveau comportement implicitement accepté ; l'absence de changement dans le code ; la page préparant une tranche réalisable sans règles non décidées.
- **Arrêt après le rapport**. Aucun `push`, aucune PR ou fusion sans autorisation distincte et ciblée.

## 5. Critère de sortie

Le propriétaire peut lire une fiche qui distingue sans ambiguïté **les principes inscrits, les hypothèses non acceptées et les sujets encore ouverts**. Le rapport précise les seuls choix indispensables avant d'autoriser un premier **lot de code C#**.

**Ce mandat est une préparation de la prochaine opération, pas son autorisation.**
