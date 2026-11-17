# Inscription documentaire de `MEC-0001` : sous-décisions du 17 novembre 2026 (ARB-A à ARB-E, G1 à G4)

> **Inscription documentaire partielle.** `MEC-0001` reste une fiche incomplète, **« reportée »**, classe `MODIFICATION-PROPOSEE`, état « non commencé ». **Aucune implémentation n'est autorisée**, ni par l'inscription, ni par ce rapport. Les modifications sont commitées et poussées sur la seule branche `claude/new-session-mgfohp`, avec l'autorisation du propriétaire ; **aucune PR ni fusion dans `main`**.

| | |
|---|---|
| Date | 17 novembre 2026 (UTC) |
| Mandat | « BASTION — Mandat d'inscription documentaire MEC-0001 — v1.0 », statut « AUTORISÉ POUR MODIFICATIONS DOCUMENTAIRES UNIQUEMENT », fichier joint au message du propriétaire (`BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md`), 66 lignes, SHA-256 `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0`. **Non archivé** dans `docs/mandates/` : le mandat (§3) n'autorise aucun autre fichier que ceux qu'il liste. |
| Source de transcription | Consolidation documentaire `MEC-0001` v1.4.1 du 17 novembre 2026, jointe au même message (`bastion_mec0001_v141.md`), 273 lignes, SHA-256 `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc`. Le mandat la désigne sous le nom `BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md` ; le fichier reçu porte un autre nom, mais son titre et son contenu sont ceux de la v1.4.1. **Non archivée** dans le dépôt, pour la même raison. |
| Autorisation | Message du propriétaire du 17 novembre 2026, qui joint les deux documents : « Je valide l'exécution du mandat d'inscription documentaire MEC-0001 v1.0 joint, sur la base de la consolidation v1.4.1 également jointe. Exécute uniquement le périmètre autorisé par le mandat, conformément à CLAUDE.md. Travaille sur une branche dédiée […]. À cette étape, aucun commit, push, fusion ou publication n'est autorisé. » |
| Base | `git fetch origin main` (code 0) : `origin/main` = `35a5c3dbd15ea36a41bca46b887ec102a0d5081b`, fusion de la PR n° 13. Registre sur `main` : SHA-256 `519086ea6985bfb50484a724f04b394674023fcf9c0a654894f064e7d759c952`. |
| Branche | `claude/new-session-mgfohp`, créée depuis `origin/main` par `git switch --no-track -c` (code 0), donc sans suivi automatique : aucune publication ne peut viser `main` par défaut. Ce nom est celui que l'environnement de la session attribue au travail de Claude Code ; le mandat n'en fixait pas. |
| Publication | Pendant l'exécution du lot : aucune (mandat, §3, §4 et §6). Ensuite, second message du propriétaire du 17 novembre 2026 : « Je valide les compléments documentaires du lot d'inscription MEC-0001. Je t'autorise maintenant à créer un commit et à effectuer un push exclusivement sur la branche `claude/new-session-mgfohp`. » Périmètre limité aux quatre fichiers du lot ; « Ne crée pas de PR et ne fusionne pas dans `main`. » D'où **un commit et un push** sur cette branche, avec ces quatre fichiers et eux seuls. Le SHA du commit est donné dans la restitution au propriétaire, puisqu'il ne peut figurer dans le fichier qu'il contient. **Aucune PR, aucune fusion.** |

## 1. Résultat

- **Registre** (`docs/gameplay/GAMEPLAY-DECISIONS.md`, fiche `MEC-0001` seulement) :
  - un bloc daté « Sous-décisions de conception acceptées le 17 novembre 2026 (ARB-A à ARB-E, G1 à G4) », avec provenance, preuve, et les neuf sous-décisions, chacune avec ses points ouverts ;
  - les quatre interfaces historiques annotées : S4 et N2, S10, Z1, N14 ; le texte historique est conservé mot pour mot, l'annotation est ajoutée à sa suite ;
  - la liste « Encore ouvert » actualisée pour les seuls points tranchés en principe ; chaque sous-question encore non décidée reste écrite ;
  - le bandeau et quatre champs du tableau de la fiche complétés pour nommer les nouvelles sous-décisions (§4, interprétation 1).
- **Statut inchangé** : le champ « Décision du propriétaire » de `MEC-0001` commence toujours par « reportée » ; classe `MODIFICATION-PROPOSEE` ; « Aucun changement de gameplay » ; « non commencé ». La fiche `MEC-0002` et l'en-tête du registre sont inchangés octet pour octet.
- **Matrice du LOT-2F** : un bandeau « Document historique » de deux lignes, en tête ; le reste est intact.
- **`OXCE-BASELINE.md`** : la seule phrase périmée (« La seule fiche, `MEC-0001` ») est corrigée ; le commit figé et la politique de propriété intellectuelle (D4) sont intacts.
- **Ce rapport**, nouveau fichier de `docs/reviews/`.

## 2. Sources lues

Dans le dépôt, sur `origin/main` (`35a5c3d`) :
- `CLAUDE.md` ; `docs/gameplay/GAMEPLAY-DECISIONS.md` (en entier pour `MEC-0001`, et la structure de `MEC-0002`) ; l'en-tête et les conventions de `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md` ; `docs/references/OXCE-BASELINE.md` (§ Limites de vérification et Règles) ; `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md` (existence du §4, « Effet sur la matrice du LOT-2F ») ; `docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`, §2, lignes 3, 12 et 14 du tableau ; `docs/reviews/LOT-2J-INSCRIPTION-DOCUMENTAIRE.md`, comme modèle de rapport.
- Le harnais, sans le modifier : `.claude/settings.json`, `scripts/harness/pre-tool-use.sh`, `stop-report-check.sh`, `check-simulation-trace.sh`, `.github/workflows/ci.yml`.

Hors dépôt :
- le mandat et la consolidation v1.4.1, lus en entier (empreintes en tête) ;
- le code d'OXCE au commit figé `441cae1b071d249d40a223858cb6bd07fd5d791b`, clone local, lu sans exécution ni compilation. Il fonde l'étiquette d'ARB-C. Dans `src/Battlescape/UnitWalkBState.cpp:337-354`, le bloc commenté « now open doors » appelle `TileEngine::unitOpensDoor` pendant la marche, avant le pas, en mode non explicite (argument `rClick` à faux, ligne 340). Le commentaire de cette fonction (`src/Battlescape/TileEngine.cpp:4056-4068`) décrit l'ouverture « by rightclick, or by walking through it ». Le LOT-2A ne faisait que signaler cet emplacement (§6, « Portes ») ; cette lecture est donc propre à ce lot.

Les revues des versions v1.1, v1.3 et v1.4 de la consolidation ont eu lieu dans la conversation du 17 novembre 2026 ; leurs rapports ne sont pas dans le dépôt.

## 3. Ce qui change (avant / après)

| # | Emplacement | Avant (`main`) | Après |
|---|---|---|---|
| 1 | Bandeau de `MEC-0001` | Sous-décisions acceptées : S1 à S12, Z1, N1 à N14 | Ajout : « puis ARB-A à ARB-E et G1 à G4 le 17 novembre 2026 » ; le reste inchangé |
| 2 | « Fonctionnement de référence et preuves » | Proposition, inscription, actualisation, surcharge | Ajout du renvoi à ce rapport |
| 3 | « Changement demandé » | S1 à S12, Z1 et N1 à N14 | S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 |
| 4 | « Décision du propriétaire » | « reportée — … » ; sous-décisions du 8 novembre et preuves | Inchangé, plus une phrase : sous-décisions acceptées en conversation le 17 novembre 2026, preuve et provenance dans le nouveau bloc |
| 5 | « Éléments exclus » | ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | ajout d'ARB-A à ARB-E et G1 à G4 |
| 6 | S4 | texte historique | conservé ; annotation : restreinte par ARB-A et G1 |
| 7 | S10 | texte historique | conservé ; annotation : exceptions ARB-B (corps) et G2 (réveil) |
| 8 | Z1 | texte historique et étiquette OXCE | conservés ; annotation : G3 ajoute l'énergie |
| 9 | N2 | texte historique et étiquette OXCE | conservés ; annotation : contrôle physique d'ARB-A et G1 après le contrôle topologique ; lecture de « S4 inchangée » |
| 10 | N14, deuxième puce | « seulement lorsque ses TU restantes… : aucune immobilisation liée à la charge » | conservé ; annotation : second motif, l'énergie insuffisante (G3) ; renvoi à ARB-D |
| 11 | Nouveau bloc | — | « Sous-décisions de conception acceptées le 17 novembre 2026 (ARB-A à ARB-E, G1 à G4) » : provenance, preuve, neuf sous-décisions |
| 12 | « Encore ouvert » | 7 points concernés (géométrie et portes, coûts, escaliers, surcharge, renouvellement, chemin, orientation-énergie-interruptions) | chaque point garde ses sous-questions ouvertes et indique ce qui est désormais décidé, avec la sous-décision qui le tranche |
| 13 | Phrase finale de « Encore ouvert » | ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | ajout d'ARB-A à ARB-E et G1 à G4, et renvoi aux points ouverts de chaque sous-décision |
| 14 | Matrice du LOT-2F | titre puis texte | bandeau « Document historique » après le titre ; texte conservé |
| 15 | `OXCE-BASELINE.md`, ligne 45 | « La seule fiche, `MEC-0001`, est une fiche documentaire incomplète et non approuvée » | « Deux fiches sont documentées, `MEC-0001` et `MEC-0002` : ce sont des fiches incomplètes, et aucune des deux mécaniques n'est acceptée dans son ensemble » |

Aucune sous-décision historique (S1 à S12, Z1, N1 à N14) n'est supprimée ni réécrite : leur texte d'origine reste en tête de ligne (contrôle 6). Le diff complet figure au §10.

## 4. Fidélité et interprétations

**Transcription.** Chaque sous-décision reprend le tableau du mandat (§2) et le texte de la consolidation v1.4.1 (§2 pour ARB-A à ARB-E, §3 pour G1 à G4), avec leurs points ouverts. La preuve reprend le §1.2 de la v1.4.1, présentée comme une **transcription** des échanges du 17 novembre 2026 : les messages d'origine ne sont pas dans le dépôt. Aucune citation n'est présentée comme figurant déjà au registre (mandat, §2). Aucune valeur des scénarios de test de la v1.4.1, toutes fictives, n'est inscrite (contrôle 9).

**Interprétations de l'exécutant** (la première, soumise au propriétaire, a été validée par lui, §9) :
1. **Bandeau et champs du tableau.** Le mandat (§3.1) demande le bloc daté, les annotations et l'actualisation de « Encore ouvert ». Le bandeau de la fiche, quatre champs du tableau et la phrase finale de « Encore ouvert » énumèrent les sous-décisions acceptées : ils ont été complétés pour nommer ARB-A à ARB-E et G1 à G4, sans rien retirer. Sans cela, le champ « Décision du propriétaire », où le gabarit place la preuve et la date, aurait ignoré les décisions du 17 novembre. Ces ajouts ne changent aucune règle ; ils se retirent sans effet sur le reste si le propriétaire les juge hors périmètre.
2. **Rapport à OXCE.** Les étiquettes [Écart établi] ne sont posées que là où la v1.4.1 signale un écart : ARB-A, ARB-C et G4. Aucune étiquette n'est ajoutée ailleurs, même là où le code lu concorde (ARB-D, par exemple), et aucune fidélité à OXCE n'est affirmée.
   - ARB-A et G4 : la référence est celle de la v1.4.1, les lignes 44 et 55 du fichier LOT-2A, écrite selon la convention du registre (« LOT-2A §2 ligne 3 » et « ligne 14 »). Pour G4, le LOT-2A classe « chemin le moins coûteux non garanti » comme une inférence, et l'étiquette le dit.
   - ARB-C : la v1.4.1 dit seulement « lu dans son code », sans référence. La référence de code et sa lecture sont celles de ce lot (§2), et l'étiquette renvoie à ce rapport. La source de transcription n'est donc pas la seule base de cette étiquette ; c'est pourquoi le bloc dit « transcrites depuis » et non « sans ajout ».
3. **Points ouverts.** Les points laissés ouverts par chaque sous-décision sont écrits à sa suite (« Ouvert : … ») plutôt que recopiés dans « Encore ouvert ». La phrase finale de cette liste y renvoie.

## 5. Ce qui reste ouvert

L'inscription ne tranche aucun point laissé ouvert par la v1.4.1 (§6). Ils restent écrits dans la fiche :

| Point ouvert | Où dans la fiche |
|---|---|
| Dimensions, volumes, murs, tolérance, trajectoire et sous-segments du pas diagonal | G1 « Ouvert » ; « Encore ouvert », géométrie |
| Coût en énergie du pas diagonal, barèmes TU et énergie, arrondis, murs | G1 et G3 « Ouvert » ; « Encore ouvert », coûts |
| Choix entre plusieurs cases voisines, « accessible », case portant un corps, état « au sol » et GE-03 | G2 « Ouvert » |
| Corps et esquives, repoussements, sauts | G2 « Hors de G2 » (relève de `MEC-0002`) |
| Formule du facteur de surcharge, Force et kg, arrondi, autres pénalités, indicateur « encombré » | ARB-D « Ouvert » ; « Encore ouvert », surcharge |
| Capital initial, quantités récupérées, TU et énergie maximales | « Encore ouvert », renouvellement et énergie |
| Clé du départage final, algorithme de recherche | G4 « Ouvert » ; « Encore ouvert », calcul de chemin |
| Système de surveillance (Overwatch), interruption sur simple découverte | ARB-E « Ouvert » ; « Encore ouvert », interruptions |
| Coûts et états des portes, escaliers, échelles, ascenseurs | ARB-C « Ouvert » ; « Encore ouvert », géométrie et escaliers |
| Hausse imprévue d'un coût pendant un ordre | G3 « Ouvert » ; « Encore ouvert », trajet devenu non payable (inchangé) |

## 6. Contrôles exécutés

Toutes les commandes sont en lecture seule, sauf les écritures des trois fichiers par l'outil Edit (chacune soumise à la demande d'accord du harnais pour les fichiers protégés) et l'ajout de ce rapport. Les résultats sont ceux de la dernière exécution, sur l'état final des trois fichiers, avant l'ajout de ce rapport.

| # | Contrôle | Commande ou méthode | Résultat |
|---|---|---|---|
| 1 | Base | `git fetch origin main` ; `git rev-parse HEAD origin/main` | code 0 ; `HEAD` = `origin/main` = `35a5c3d` (aucun commit sur la branche) |
| 2 | Branche | `git switch --no-track -c claude/new-session-mgfohp origin/main` ; `git rev-parse --abbrev-ref @{u}` | code 0 ; aucun suivi configuré |
| 3 | Chemins modifiés | `git status --porcelain` ; `git diff --numstat origin/main` | les trois fichiers autorisés : registre (54 insertions, 18 suppressions), `OXCE-BASELINE.md` (1, 1), matrice du LOT-2F (2, 0) ; aucun autre, hors ce rapport |
| 4 | Chemins interdits | `git diff --quiet origin/main -- CLAUDE.md .claude scripts .github src tests docs/decisions docs/mandates` | code 0 : aucun code, test, harnais ni mandat touché |
| 5 | Espaces et fins de ligne | `git diff --check origin/main` | code 0 |
| 6 | Texte historique conservé | Python (`python3 -I`), registre de `main` comparé au registre modifié | S1 à S12, Z1, N1 à N11 et N12 à N14 : texte d'origine en tête de ligne ; S5 inchangée ; deuxième puce de N14 conservée en tête |
| 7 | Annotations | même script | S4, S10, Z1, N2 et N14 portent chacune une annotation datée du 17 novembre 2026 |
| 8 | Définitions | même script | ARB-A à ARB-E et G1 à G4 : une définition chacune |
| 9 | Valeurs fictives | même script, recherche de valeurs en TU, énergie, kg, facteurs | aucune dans les lignes ajoutées ; les seuls nombres du bloc sont des numéros de version, de paragraphe ou de ligne, et la date |
| 10 | `MEC-0002` et en-tête du registre | `cmp` avec `main` | code 0 pour les deux : inchangés octet pour octet |
| 11 | Décisions lues comme le harnais | extraction de `scripts/harness/check-simulation-trace.sh` (`awk`, `grep`, `cut`) | `MEC-0001` : « reportée » ; `MEC-0002` : « reportée » |
| 12 | Champs de `MEC-0001` | `grep` | `MODIFICATION-PROPOSEE` ; « Aucun changement de gameplay » ; « non commencé » ; `MODIFICATION-VALIDEE` : 3 occurrences, comme sur `main` (règles et gabarit) |
| 13 | Identifiant de modèle | `grep` sur le diff | aucun |
| 14 | Harnais | `bash scripts/harness/test-hooks.sh` | « 75 tests, 0 échec(s) », code 0 |
| 15 | Tests .NET | `command -v dotnet` | code 1 : outil absent ; `dotnet build`, `dotnet test` et `dotnet format --verify-no-changes` **non exécutés**. Aucun fichier de code n'est modifié |

Empreintes SHA-256 des trois fichiers après modification :
- `docs/gameplay/GAMEPLAY-DECISIONS.md` : `9117d20c45aa95abbc218ce5cdcc2a095106eb86c64a342be76d8521ef14d39e` ;
- `docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md` : `febf600b8e9fb414d3e763497b67fce7733a2b003a2c05a690bb65c78afbe35f` ;
- `docs/references/OXCE-BASELINE.md` : `f1b1db1a9b03a828b21a19c504597b086f297396a29a4923b68fdc4a4de699cd`.

**Aucun test de mécanique n'est écrit ni exécuté.** Les scénarios de la consolidation v1.4.1 restent des critères futurs : aucun n'est réputé réussi.

## 7. Revue indépendante

Revue du 17 novembre 2026, par un agent distinct de l'exécutant, **en lecture seule**, sur le diff non commité comparé à `origin/main` (`35a5c3d`), contre le mandat et la consolidation v1.4.1. Il n'a rien modifié et ne valide rien. Verdict : inscription fidèle sur le fond et dans le périmètre ; **aucun constat bloquant**, 2 importants, 7 mineurs, tous corrigés avant ce rapport.

Il a vérifié sans constat : les empreintes ; que le fichier reçu est bien la v1.4.1 ; le texte historique conservé et `MEC-0002` identique (`cmp`) ; le statut, y compris par l'extraction du harnais ; la substance des neuf sous-décisions ; l'absence de valeur fictive ; l'exactitude des citations et leur attribution ; les rapports à OXCE d'ARB-A et d'ARB-D ; « Encore ouvert » ligne à ligne ; le bandeau du LOT-2F ; la ligne d'`OXCE-BASELINE.md` ; le rendu Markdown (pandoc, GFM).

| Constat | Traitement |
|---|---|
| **I-1** — Chronologie de la preuve : certaines formulations de G2 et de G4 ont été présentées après les choix, non avant ; « fixent » allait plus loin que la v1.4.1 | Corrigé : « Le même §1.2 reprend les formulations qui précisent G2 et G4 : soumises avant ces choix, ou présentées après eux et dans le récapitulatif approuvé par « Je valide ». » |
| **I-2** — G3 posait au présent une règle sur les esquives de `MEC-0002` | Corrigé, d'après la v1.4.1 (§1.3 et G3, point 5) : « G3 n'ajoute aucun coût d'énergie aux esquives de `MEC-0002` […] ; une telle extension exigerait une décision distincte. » |
| m-1 — Réserve « pendant la marche ordinaire » omise dans G1 et G2 | Ajoutée aux deux endroits |
| m-2 — Annotation de N14 ambiguë | Reformulée d'après la v1.4.1 : « le pas n'est payable que si les TU et l'énergie suffisent. Aucune immobilisation liée à la charge n'est ajoutée. » |
| m-3 — Étiquette d'ARB-C fondée sur une lecture propre au lot ; « transcrites sans ajout » excessif | « transcrites depuis » ; l'étiquette renvoie au LOT-2A §6 et à ce rapport ; la lecture du code est décrite au §2 ; l'introduction des crochets le dit |
| m-4 — G4 : le LOT-2A classe le chemin non minimal comme une inférence | Étiquette reformulée : « le chemin le moins coûteux n'est donc pas garanti (inférence, LOT-2A §2 ligne 14) » |
| m-5 — Contacts avec les murs absents des points ouverts de G1 | Ajoutés |
| m-6 — « Encore ouvert » : le point « énergie » semblait rétréci | « énergie, notamment : … » |
| m-7 — Redondance dans ARB-B | Phrase réduite à « ne bloquent ni la traversée ni la destination » |
| Option — « acceptées en conversation » à côté de la règle « Une idée évoquée dans une conversation n'est pas une décision validée » | Appliquée : « acceptées explicitement par le propriétaire, en conversation » (champ « Décision du propriétaire ») ; « Validées explicitement par le propriétaire, en conversation » (bloc) |
| Limite — « rédigée par l'orchestrateur » ne figure pas dans la v1.4.1 | Retiré du registre et de ce rapport |
| Interprétation 1 (§4) jugée dans le périmètre, à déclarer | Déclarée au §4 |

## 8. Limites de preuve

- **Preuve déclarative.** Les validations du 17 novembre 2026 sont connues par le §1.2 de la consolidation v1.4.1 et par le mandat. Les messages d'origine n'ont pas été fournis, et leur transcription n'a pu être contrôlée que contre ces documents.
- **Documents cités mais absents du dépôt.** Le registre cite la consolidation v1.4.1 et le mandat par leur seule empreinte SHA-256 : le mandat (§3) n'autorisait pas à les archiver.
- **Revues.** La consolidation v1.4.1 elle-même n'a pas été relue par un agent distinct (elle le dit au §9). Le relecteur de cette inscription est un agent du même type que l'exécutant, lancé par lui sans ses conclusions : c'est une revue interne, pas un audit externe.
- **OXCE** : code lu, ni compilé ni exécuté ; aucune fidélité démontrée.
- **Outils** : `dotnet` absent, donc compilation, format et tests .NET non exécutés ; aucun fichier de code n'est touché. Le rendu Markdown a été contrôlé avec pandoc, pas sur GitHub.
- **Nom de branche** : il est celui de l'environnement de la session, et non un nom de lot du projet (en-tête).

## 9. Points à décider par le propriétaire

1. **Commit et publication** : *décidé.* Le propriétaire a autorisé, le 17 novembre 2026, un commit et un push sur la seule branche `claude/new-session-mgfohp`, pour les quatre fichiers du lot, sans PR ni fusion (en-tête).
2. **Archivage** du mandat et de la consolidation v1.4.1 dans le dépôt (`docs/mandates/` et son index), pour que le registre ne renvoie pas qu'à des empreintes : *ouvert*, mandat distinct.
3. **Interprétation 1** (§4) : *décidé.* Le propriétaire a validé les compléments du bandeau et des quatre champs du tableau de `MEC-0001` le 17 novembre 2026 (« Je valide les compléments documentaires du lot d'inscription MEC-0001 »).

La qualification globale de `MEC-0001`, l'équilibrage et l'implémentation restent des étapes distinctes, chacune soumise à son propre accord (mandat, §6).

## 10. Diff

Diff des trois fichiers modifiés, par rapport à `origin/main` (`git diff origin/main`), hors ce rapport. Ses 17 lignes de contexte vides commencent par une espace, comme le veut le format : `git diff --check` les signalerait dans ce rapport, et elles sont conservées pour que le diff reste exact.

````diff
diff --git a/docs/gameplay/GAMEPLAY-DECISIONS.md b/docs/gameplay/GAMEPLAY-DECISIONS.md
index 0fd477e..10fc3a5 100644
--- a/docs/gameplay/GAMEPLAY-DECISIONS.md
+++ b/docs/gameplay/GAMEPLAY-DECISIONS.md
@@ -48,18 +48,18 @@ L'identifiant `MEC-NNNN` est permanent : il n'est jamais réattribué.
 
 ### MEC-0001 — Déplacement élémentaire à pied
 
-**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé. Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`.**
+**Fiche de conception incomplète. Des sous-décisions sont acceptées (S1 à S12, Z1, N1 à N14, N12 et N13 étant fusionnées dans N14, puis ARB-A à ARB-E et G1 à G4 le 17 novembre 2026), mais la mécanique n'est pas acceptée dans son ensemble et aucun gameplay n'est autorisé. Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`.**
 
 | Champ | Valeur |
 |---|---|
 | Système | Combat tactique : déplacement d'une unité à pied. |
 | Description | Une unité se déplace de case en case vers une destination choisie, en payant des unités de temps (TU). Règles partielles ci-dessous. |
 | Classe | `MODIFICATION-PROPOSEE`, tant que la mécanique globale n'est pas acceptée. |
-| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. Actualisation : `docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`. Surcharge, même commit, lecture du code : `src/Savegame/BattleUnit.cpp:2709-2726` et `:4852-4861`, `src/Battlescape/UnitWalkBState.cpp:295-323`. |
-| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12, Z1 et N1 à N14 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
-| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception acceptées le 8 novembre 2026 : S1 à S12 (LOT-2C), puis Z1 et N1 à N14 (LOT-2D ; N12 et N13 fusionnées dans N14). Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par les mandats `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`) et `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md` (commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`), branche `orchestration/mandats`, confirmées par les autorisations d'exécution de ces lots données par le propriétaire le 8 novembre 2026. |
+| Fonctionnement de référence et preuves | OXCE 8.7.1, `MeridianOXC/OpenXcom`, commit `441cae1b071d249d40a223858cb6bd07fd5d791b` : **lecture du code, sans exécution d'OXCE** (`docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md`). Proposition : `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md`. Inscription : `docs/reviews/LOT-2C-INSCRIPTION-MEC-0001.md`. Actualisation : `docs/reviews/LOT-2D-ACTUALISATION-MEC-0001.md`. Inscription des sous-décisions du 17 novembre 2026 : `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md`. Surcharge, même commit, lecture du code : `src/Savegame/BattleUnit.cpp:2709-2726` et `:4852-4861`, `src/Battlescape/UnitWalkBState.cpp:295-323`. |
+| Changement demandé | Fixer le déplacement élémentaire de Bastion à partir des sous-décisions S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 ci-dessous. Raisons et impacts : voir `docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §2 et §3. Les points encore ouverts sont listés plus bas. |
+| Décision du propriétaire | reportée — arbitrages complémentaires requis. Sous-décisions de conception acceptées le 8 novembre 2026 : S1 à S12 (LOT-2C), puis Z1 et N1 à N14 (LOT-2D ; N12 et N13 fusionnées dans N14). Preuve : transcriptions des messages du propriétaire du 8 novembre 2026 portées par les mandats `docs/mandates/BASTION-MANDAT-LOT-2C-v1.0.md` (commit `d8c5335c4e19c374726f06430c31f7db77cbcc77`) et `docs/mandates/BASTION-MANDAT-LOT-2D-v1.0.md` (commit `d71fbcc98d1e073ce09a436624f59339b7835c0b`), branche `orchestration/mandats`, confirmées par les autorisations d'exécution de ces lots données par le propriétaire le 8 novembre 2026. Sous-décisions de conception acceptées explicitement par le propriétaire, en conversation, le 17 novembre 2026 : ARB-A à ARB-E et G1 à G4 ; preuve et provenance : bloc « Sous-décisions de conception acceptées le 17 novembre 2026 » ci-dessous. |
 | Périmètre autorisé | **Aucun changement de gameplay.** La fiche documente des arbitrages ; elle n'autorise aucune implémentation. |
-| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas ; les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002`. |
+| Éléments exclus | Tous les points listés sous « Encore ouvert », et tout ce que S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 ne couvrent pas ; les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002`. |
 | Tests de référence | Critères futurs seulement (`docs/reviews/LOT-2B-PROPOSITION-MEC-0001.md` §4, à adapter). Aucun test écrit ni exécuté ; aucune fidélité à OXCE démontrée. |
 | Tests de modification | Critères futurs seulement, un par écart retenu. Aucun test écrit ni exécuté. |
 | État d'implémentation | non commencé |
@@ -71,13 +71,13 @@ Elles n'autorisent, seules, aucun gameplay. Chaque sous-décision S*n* transcrit
 - **S1** — Huit directions, diagonales incluses.
 - **S2** — Coût d'un pas en diagonale : coût de la case d'arrivée × 1,5, arrondi à l'entier inférieur (comme OXCE, selon la lecture du code : LOT-2A §2 ligne 4).
 - **S3** — Diagonale interdite uniquement lorsque les deux cases orthogonales voisines sont bloquées.
-- **S4** — Une unité voisine ne compte pas comme obstacle pour la règle des diagonales.
+- **S4** — Une unité voisine ne compte pas comme obstacle pour la règle des diagonales. *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé ; restreinte postérieurement par ARB-A et G1. Une unité voisine ne compte toujours pas comme un mur pour le contrôle topologique, mais une unité consciente peut rendre physiquement impraticable le passage emprunté par la diagonale ; voir le bloc du 17 novembre 2026.)*
 - **S5** — TU insuffisantes : déplacement partiel, comme dans OXCE (selon la lecture du code : LOT-2A §2 ligne 9). Décision initiale, conservée comme historique : **supplantée par Z1 pour la sélection normale d'une destination**. Une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. *(Annotation ajoutée au LOT-2D.)*
 - **S6** — Destinations autorisées : cases actuellement visibles ou déjà explorées.
 - **S7** — Le trajet reste entièrement dans des cases actuellement visibles ou déjà explorées.
 - **S8** — Le trajet est calculé selon le dernier état connu du terrain ; le déplacement est interrompu lorsqu'un obstacle inconnu est rencontré.
 - **S9** — Un obstacle inconnu rencontré pendant un déplacement devient connu du joueur et met à jour sa connaissance du terrain.
-- **S10** — Une case occupée par une autre unité est infranchissable, pour la traversée comme pour la destination.
+- **S10** — Une case occupée par une autre unité est infranchissable, pour la traversée comme pour la destination. *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé ; deux exceptions postérieures. Pour la marche ordinaire, un corps mort ou inconscient ne bloque ni la traversée ni la destination (ARB-B). Lors d'un réveil sans case voisine disponible, deux unités conscientes occupent transitoirement la même case (G2). Voir le bloc du 17 novembre 2026.)*
 - **S11** — Une unité cachée rencontrée pendant un déplacement est révélée au joueur.
 - **S12** — Une unité révélée redevient cachée lorsqu'elle n'est plus observable, sans indication persistante de sa position.
 
@@ -87,9 +87,9 @@ Elles n'autorisent, seules, aucun gameplay. Les références Z1 et N*n* reprenne
 
 Entre crochets, le rapport à OXCE, établi par lecture du code (sans exécution) ; le détail figure dans le rapport LOT-2D. « Vérifié » : comportement d'OXCE lu dans le code, concordant dans son principe avec la décision ; aucune fidélité n'est démontrée. « Écart établi » : la décision s'écarte de ce comportement lu. « À vérifier » : point seulement signalé au LOT-2A (§6), sans étude.
 
-- **Z1** — Afficher la zone atteignable selon les TU et les informations connues ; interdire la sélection d'une destination hors de cette zone. Proposée au LOT-2C, acceptée ensuite. Z1 supplante S5 pour la sélection normale ; une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. [Écart établi : OXCE calcule le chemin sans regarder les TU, puis déplace partiellement l'unité (LOT-2A §2 ligne 9).]
+- **Z1** — Afficher la zone atteignable selon les TU et les informations connues ; interdire la sélection d'une destination hors de cette zone. Proposée au LOT-2C, acceptée ensuite. Z1 supplante S5 pour la sélection normale ; une interruption imprévue reste possible (S8, S11), selon la portée de Z1 donnée par le mandat LOT-2D. [Écart établi : OXCE calcule le chemin sans regarder les TU, puis déplace partiellement l'unité (LOT-2A §2 ligne 9).] *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé ; G3 ajoute postérieurement l'énergie. La zone atteignable est calculée avec les TU, l'énergie et les informations connues ; une destination qui ne peut être atteinte avec les deux ressources n'est pas sélectionnable. Voir le bloc du 17 novembre 2026.)*
 - **N1** — Terrain en « modèle B » : des cases et des murs séparant les cases ; huit directions maintenues (S1). [Vérifié : dans OXCE, une case a un sol, un mur ouest, un mur nord et un objet (LOT-2A §2 ligne 11).]
-- **N2** — Règle permissive dans le modèle B : diagonale permise si au moins un des deux passages orthogonaux autour du coin est ouvert ; interdite si les deux sont bloqués. N2 étend aux murs du modèle B le principe permissif de S3 ; S4 inchangée. [Écart établi : OXCE refuse la diagonale dès qu'un des murs concernés bloque, sur l'un ou l'autre passage (LOT-2A §2 ligne 3 ; `src/Battlescape/Pathfinding.cpp:959-966` pour le nord-est).]
+- **N2** — Règle permissive dans le modèle B : diagonale permise si au moins un des deux passages orthogonaux autour du coin est ouvert ; interdite si les deux sont bloqués. N2 étend aux murs du modèle B le principe permissif de S3 ; S4 inchangée. [Écart établi : OXCE refuse la diagonale dès qu'un des murs concernés bloque, sur l'un ou l'autre passage (LOT-2A §2 ligne 3 ; `src/Battlescape/Pathfinding.cpp:959-966` pour le nord-est).] *(Annotation ajoutée le 17 novembre 2026 : texte historique conservé. N2 reste le premier contrôle, topologique ; ARB-A et G1 y ajoutent postérieurement un contrôle physique : une diagonale permise par N2 est refusée si aucun passage orthogonal n'est physiquement praticable. La mention « S4 inchangée » se lit avec l'annotation de S4.)*
 - **N3** — Plusieurs niveaux dès `MEC-0001`, avec des positions de principe (x, y, z). [Vérifié : positions en x, y, z dans OXCE (LOT-2A §2 ligne 1).]
 - **N4** — Changements de niveau prévus dès la conception : escaliers, échelles et ascenseurs. [À vérifier.]
 - **N5** — Chutes volontaires et involontaires autorisées. [À vérifier.]
@@ -102,7 +102,7 @@ Entre crochets, le rapport à OXCE, établi par lecture du code (sans exécution
 - **N11** — Le poids total porté affecte aussi le déplacement normal. [Vérifié : dans OXCE, l'effet est indirect, par la réduction des TU, qui touche toutes les actions ; voir N12 à N14.]
 - **N12 à N14** — Surcharge, décision finale N14 (la plus récente) :
   - principe d'OXCE, sans seuil d'immobilisation supplémentaire ;
-  - l'unité est empêchée d'avancer seulement lorsque ses TU restantes ne permettent pas de payer le pas suivant : aucune immobilisation liée à la charge ;
+  - l'unité est empêchée d'avancer seulement lorsque ses TU restantes ne permettent pas de payer le pas suivant : aucune immobilisation liée à la charge ; *(annotation ajoutée le 17 novembre 2026 : texte historique conservé ; G3 ajoute postérieurement un second motif de non-exécution du pas, l'énergie insuffisante : le pas n'est payable que si les TU et l'énergie suffisent. Aucune immobilisation liée à la charge n'est ajoutée. Pour l'ordre de la récupération et de la réduction due à la surcharge, voir ARB-D, bloc du 17 novembre 2026.)*
   - « encombré » peut rester un simple indicateur informatif, sans nouveau modificateur ni statut technique décidé ;
   - la Force détermine l'effet de la surcharge (N13).
 
@@ -110,27 +110,63 @@ Entre crochets, le rapport à OXCE, établi par lecture du code (sans exécution
 
   [Vérifié : dans OXCE, à la récupération des TU, si le rapport Force / poids porté est inférieur à 1, les TU sont multipliées par ce rapport et tronquées, avant d'autres pénalités ; ce n'est pas un surcoût des pas (`src/Savegame/BattleUnit.cpp:2709-2726`). L'unité s'arrête quand le pas suivant dépasse ses TU restantes (`src/Battlescape/UnitWalkBState.cpp:295-323`).]
 
+#### Sous-décisions de conception acceptées le 17 novembre 2026 (ARB-A à ARB-E, G1 à G4)
+
+Elles n'autorisent, seules, aucun gameplay : `MEC-0001` reste reportée dans son ensemble. Validées explicitement par le propriétaire, en conversation, le 17 novembre 2026, elles sont inscrites par le mandat d'inscription documentaire `MEC-0001` v1.0, validé par le propriétaire le même jour, et transcrites depuis la consolidation documentaire `MEC-0001` v1.4.1 du 17 novembre 2026. Ces deux documents, transmis par le propriétaire, ne sont pas archivés dans le dépôt : consolidation, SHA-256 `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc` ; mandat, SHA-256 `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0`. Détail de l'inscription : `docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md`.
+
+Preuve de validation : transcription des échanges du 17 novembre 2026, reprise au §1.2 de la consolidation v1.4.1 ; les messages d'origine ne sont pas dans le dépôt. « parfait. je valide les deux » valide ARB-B et ARB-E ; « Je valide tout le reste », après le récapitulatif des cinq arbitrages, valide ARB-A, ARB-C et ARB-D. Pour G1 à G4, le propriétaire a répondu « B » (G1 : trajet par un passage ouvert), « B » puis « A » (G2 : repositionnement automatique, puis réveil sur place faute de case voisine libre), « B » (G3 : TU et énergie) et « A » (G4 : priorité aux TU), puis « Je valide » après le récapitulatif de G1 à G4. Le même §1.2 reprend les formulations qui précisent G2 et G4 : soumises avant ces choix, ou présentées après eux et dans le récapitulatif approuvé par « Je valide ».
+
+Les valeurs numériques des scénarios de test de la consolidation sont fictives : aucune n'est inscrite ici. Entre crochets, le rapport à OXCE que la consolidation signale, selon les conventions du bloc précédent ; les lectures du code qui le fondent sont détaillées dans le rapport d'inscription.
+
+- **ARB-A** — Une diagonale admise par le contrôle topologique (S4, N2) peut néanmoins être inexécutable si le volume de l'unité ne peut pas passer sans collision. Restriction postérieure explicite de S4 et N2 (voir leurs annotations), précisée par G1. Ouvert : géométrie détaillée. [Écart établi : dans OXCE, une unité voisine n'empêche pas la diagonale (LOT-2A §2 ligne 3).]
+- **ARB-B** — Pendant la marche ordinaire, les corps morts ou inconscients ne bloquent ni la traversée ni la destination. Exception postérieure à la formulation historique de S10 (voir son annotation). Le simple chevauchement lié à la marche n'est pas un impact de `MEC-0002` ; le corps garde sa masse et son volume pour `MEC-0002` (RP-04, EN-08). Précisée par G2 pour le réveil.
+- **ARB-C** — Une porte demande une ouverture explicite : la marche ne l'ouvre pas automatiquement. Les escaliers et les échelles s'empruntent par des connexions définies ; les ascenseurs ont des états et des connexions définis. La marche ordinaire ne change pas de niveau de façon implicite ; les sauts et les chutes relèvent de `MEC-0002`. Ouvert : coûts, états et détails d'interaction. [Écart établi : dans OXCE, la marche ouvre les portes au passage (`src/Battlescape/UnitWalkBState.cpp:337-354`, emplacement signalé au LOT-2A §6 ; lecture du code, sans exécution, rapportée dans le rapport d'inscription).]
+- **ARB-D** — Après récupération, les TU disponibles valent min(solde restant + TU récupérées, TU maximales) ; la réduction due à la surcharge s'applique ensuite à ce total plafonné, et non au seul incrément récupéré. L'énergie est récupérée séparément. La surcharge ne majore pas le prix des pas. Ouvert : formule exacte du facteur, conversion de la Force en capacité en kg, arrondis, valeurs.
+- **ARB-E** — Un tir de réaction effectivement tiré contre une unité qui marche interrompt son ordre de marche, même s'il manque, ne blesse pas ou ne met pas hors de combat. Le pas déjà effectué reste débité une seule fois, sans remboursement. Un surveillant qui pivote sans tirer n'interrompt pas la marche au titre d'ARB-E. Ouvert : conditions, ordre et coûts du système de surveillance (Overwatch), hors de cette fiche. Aucune conversion des UT de kowlting en TU de Bastion.
+- **G1** — Le pas diagonal ne suit pas obligatoirement la droite entre les centres des cases : il passe par l'un des passages orthogonaux praticables autour du coin.
+  - N2 reste le premier contrôle : au moins un des deux passages orthogonaux doit être ouvert.
+  - Le volume de l'unité doit pouvoir emprunter un passage sans traverser celui d'une autre unité consciente ou d'un obstacle ; pendant la marche ordinaire, un corps mort ou inconscient reste traversable (ARB-B).
+  - Une unité voisine n'interdit pas automatiquement la diagonale au titre de S4, mais peut rendre le passage physiquement impraticable.
+  - Le trajet physique respecte S7 : il n'exploite pas de terrain jamais exploré.
+  - Le déplacement reste un seul pas diagonal : le coût en TU de S2 est facturé une fois, et il ne devient pas deux pas orthogonaux.
+  - Sans passage physiquement praticable, la diagonale est refusée.
+
+  Ouvert : dimensions des volumes, largeur des cases, épaisseur des murs, tolérance géométrique, trajectoire et sous-segments (dont l'application de S7 et les contacts avec les murs), événements détectés pendant la traversée, coût éventuel des murs, coût en énergie du pas diagonal (G3).
+- **G2** — Réveil d'une unité inconsciente dont la case est occupée par une autre unité :
+  - si une case voisine libre et accessible existe, l'unité réveillée y est automatiquement repositionnée ; ce repositionnement n'est ni un déplacement volontaire ni un pas de marche ordinaire, et ne coûte pas de TU de marche ; aucun autre coût n'est fixé ;
+  - si aucune case voisine n'est disponible, l'unité reprend conscience sur place et reste au sol ; elle ne peut pas se relever tant que sa case reste occupée. Ce chevauchement de deux unités conscientes est une exception transitoire à S10 ; la reprise de conscience n'est pas différée faute de place ;
+  - ARB-B demeure : pendant la marche ordinaire, un corps inconscient reste traversable jusqu'au réveil, un corps mort reste traversable.
+
+  Ouvert : choix entre plusieurs cases voisines libres ; sens précis d'« accessible » (terrain, niveau, visibilité, support, volumes) ; statut d'une case portant déjà un corps (compte-t-elle comme « libre » ?) ; correspondance technique de l'état « au sol » avec les postures de GE-03, sans relèvement implicite ; contacts et interactions pendant la coexistence ; événements consécutifs ; coûts des autres actions de posture. Hors de G2 : admissibilité des cases portant un corps pour les esquives (ES-08, ES-11, ES-12), les repoussements (RP-03, RP-05) et les sauts, qui relève de `MEC-0002`.
+- **G3** — Chaque pas de marche ordinaire coûte des TU et de l'énergie ; il n'est réalisable que si les deux ressources suffisent pour ce pas. La zone atteignable (Z1) se calcule avec les TU disponibles, l'énergie disponible et les informations connues ; une destination qui ne peut pas être atteinte avec les deux ressources n'est pas sélectionnable. Les coûts sont propres à Bastion : ni conversion des UT de kowlting, ni reprise automatique des valeurs d'OXCE. G3 n'ajoute aucun coût d'énergie aux esquives de `MEC-0002` : ES-09 et ES-10 ne prévoient que le débit de TU ; une telle extension exigerait une décision distincte. G3 modifie la portée de Z1 et de N14 (voir leurs annotations), sans ajouter d'immobilisation liée à la surcharge. Ouvert : barèmes de terrain, coûts en énergie des diagonales et des passages, arrondis, coûts des murs, récupération et plafond d'énergie, hausse imprévue d'un coût pendant un ordre.
+- **G4** — Parmi les chemins admissibles avec les ressources disponibles et les informations connues du camp (S6 à S9, et non la vérité cachée) :
+  - choisir celui qui dépense le moins de TU ;
+  - à égalité de TU, celui qui dépense le moins d'énergie ;
+  - s'il reste une égalité, appliquer un départage déterministe, identique pour un même état et une même destination.
+
+  Un chemin moins cher en TU mais irréalisable en énergie n'est pas admissible ; la priorité est lexicographique, sans mélange pondéré des deux ressources. Ouvert : clé exacte du départage final, algorithme de recherche. [Écart établi : OXCE retient une ligne droite à coût homogène sans la comparer à un détour ; le chemin le moins coûteux n'est donc pas garanti (inférence, LOT-2A §2 ligne 14).]
+
 #### Encore ouvert
 
-- Géométrie précise des murs et des angles, dont ce qu'est un passage orthogonal « bloqué » pour N2 ; portes ; taille des unités.
-- Modèle et valeurs des coûts : terrain, murs éventuels, changements de niveau. S2 suppose un coût d'entrée par case d'arrivée : le modèle B (N1) peut obliger à la revoir, notamment pour un coût éventuel des murs (dans OXCE, ce coût s'ajoute après le facteur 1,5 : LOT-2A §2 lignes 4 et 5).
-- Règles précises des escaliers, échelles et ascenseurs.
+- Géométrie précise des murs et des angles, dont ce qu'est un passage orthogonal « bloqué » pour N2 ; trajectoire physique du pas diagonal (G1) ; portes : l'ouverture explicite est décidée (ARB-C), leurs coûts et leurs détails restent ouverts ; taille des unités.
+- Modèle et valeurs des coûts, en TU et en énergie (G3) : terrain, murs éventuels, changements de niveau. S2 suppose un coût d'entrée par case d'arrivée : le modèle B (N1) peut obliger à la revoir, notamment pour un coût éventuel des murs (dans OXCE, ce coût s'ajoute après le facteur 1,5 : LOT-2A §2 lignes 4 et 5).
+- Règles précises des escaliers, échelles et ascenseurs ; le principe des connexions définies et des états d'ascenseur est décidé (ARB-C).
 - Chutes :
   - règles des chutes volontaires et involontaires ;
   - formule et valeurs des dégâts ;
   - hauteur de chute sans dégâts ;
   - effet précis des caractéristiques, équipements, armure et charge ;
   - ces points sont précisés ou tranchés en partie par `MEC-0002`, qui fait autorité (seuil sans dégâts : 3 m inclus, CH-09) ; les points qui restent ouverts y sont listés.
-- Surcharge : transposition exacte du principe d'OXCE (formule, arrondi, ordre avec les autres pénalités) ; présentation de l'indicateur « encombré ».
-- Capital initial et renouvellement des TU.
-- Calcul de chemin garantissant le coût minimal ; départage déterministe des chemins de même coût.
-- Orientation et rotation ; énergie ; interruptions non encore spécifiées.
+- Surcharge : l'ordre de la récupération est décidé (ARB-D : solde plus récupération, plafond aux TU maximales, puis réduction sur le total plafonné) ; restent ouverts la formule exacte du facteur, la conversion de la Force en capacité en kg, l'arrondi, l'ordre avec les autres pénalités et la présentation de l'indicateur « encombré ».
+- Capital initial et quantités de TU récupérées, TU maximales ; le principe du renouvellement est décidé (ARB-D).
+- Calcul de chemin : le critère est décidé (G4 : TU minimales, puis énergie minimale, puis départage déterministe) ; restent ouverts la clé exacte du départage final et l'algorithme de recherche.
+- Orientation et rotation ; énergie, notamment : barèmes, énergie maximale, récupération et plafond (le double coût en TU et en énergie est décidé, G3) ; interruptions autres que le tir de réaction (ARB-E), dont la simple découverte d'un ennemi sans tir ; conditions et coûts du système de surveillance (Overwatch).
 - Conditions détaillées de visibilité ; règles de brouillard de guerre hors du déplacement.
 - Interface de la zone atteignable : présentation et sélection.
 - Trajet devenu non payable ou non réalisable en cours de route, à cause d'un coût réel, d'une occupation ou d'un obstacle jusque-là inconnus. Au-delà de l'interruption (S8, S11), ce cas n'est pas entièrement défini, notamment en cas d'augmentation imprévue du coût.
 - Autres propositions du LOT-2B non arbitrées, notamment : ordre impossible sans TU dépensée (P14), paiement de chaque pas avant de le faire, marche seule ; classe définitive de la fiche.
 
-Cette liste n'est pas exhaustive : tout ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté.
+Cette liste n'est pas exhaustive : tout ce que S1 à S12, Z1, N1 à N14, ARB-A à ARB-E et G1 à G4 ne couvrent pas reste non décidé, comme tout paramètre non explicitement accepté. Les points laissés ouverts par ARB-A à ARB-E et G1 à G4 sont aussi indiqués dans chacune de ces sous-décisions.
 
 L'hypothèse provisoire du LOT-2B « toutes les unités sont connues » n'est pas retenue : S6 à S9 introduisent les cases explorées et le terrain mémorisé, S11 et S12 les unités cachées.
 
diff --git a/docs/references/OXCE-BASELINE.md b/docs/references/OXCE-BASELINE.md
index 38a19bb..ae1bf40 100644
--- a/docs/references/OXCE-BASELINE.md
+++ b/docs/references/OXCE-BASELINE.md
@@ -42,7 +42,7 @@ Registre protégé. OXCE (OpenXcom Extended) sert de référence de comportement
 
 ## Limites de vérification (toujours ouvertes)
 
-- **Aucun gameplay n'est validé ni implémenté** sur la base de cette référence. La seule fiche, `MEC-0001`, est une fiche documentaire incomplète et non approuvée (`docs/gameplay/GAMEPLAY-DECISIONS.md`).
+- **Aucun gameplay n'est validé ni implémenté** sur la base de cette référence. Deux fiches sont documentées, `MEC-0001` et `MEC-0002` : ce sont des fiches incomplètes, et aucune des deux mécaniques n'est acceptée dans son ensemble (`docs/gameplay/GAMEPLAY-DECISIONS.md`).
 - **Binaires non reconstruits :** le rattachement des binaires officiels au commit figé repose sur leur nom (hash `441cae1b0`, nommage par `git describe`). C'est une inférence solide, non vérifiée par recompilation.
 - **Compatibilité non vérifiée, dans les deux sens du terme :**
   - **licences :** la compatibilité des licences tierces avec Bastion n'est pas auditée exhaustivement (code tiers de `src/`, bibliothèques de `deps/`, shaders, ressources) ;
diff --git a/docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md b/docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md
index 6bbd096..f1e0c80 100644
--- a/docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md
+++ b/docs/reviews/LOT-2F-MATRICE-TESTS-MEC-0001.md
@@ -1,5 +1,7 @@
 # LOT-2F — Matrice de tests futurs de `MEC-0001`
 
+> **Document historique** *(avertissement ajouté le 17 novembre 2026)*. Cette matrice précède `MEC-0002` et les sous-décisions de `MEC-0001` du 17 novembre 2026 (ARB-A à ARB-E, G1 à G4), inscrites dans `docs/gameplay/GAMEPLAY-DECISIONS.md`. Certains attendus ne sont plus des oracles actuels, notamment T-M05 (diagonale près d'une unité : contrôle physique, ARB-A et G1), T-M09 (corps non bloquants pour la marche : ARB-B), T-M11 (récupération des TU : ARB-D) et les tests relatifs aux sauts, chutes, esquives et impacts, qui relèvent de `MEC-0002` (voir `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`, §4). La matrice candidate à jour figure au §5 de la consolidation documentaire `MEC-0001` v1.4.1, hors dépôt (SHA-256 `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc`). Le texte ci-dessous est conservé sans modification.
+
 Compagnon de `docs/reviews/LOT-2F-SPECIFICATION-MEC-0001.md` : les identifiants de règles (M, J, P, K, D, I) et de points ouverts (E) y sont définis.
 
 **Aucun test n'est écrit ni exécuté.** Ce document décrit des scénarios ; il n'autorise aucune implémentation.
````
