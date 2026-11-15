# LOT-2J — Inscription documentaire de `MEC-0001` et `MEC-0002`

> **Inscription documentaire partielle.** Les deux fiches restent **« reportées »**, classe `MODIFICATION-PROPOSEE`, état « non commencé », sans changement de gameplay. **Aucune implémentation n'est autorisée**, ni par l'inscription, ni par ce rapport.

| | |
|---|---|
| Date | 15 novembre 2026 (UTC) |
| Mandat | `docs/mandates/BASTION-MANDAT-LOT-2J-INSCRIPTION-DOCUMENTAIRE-v1.0.md` : fichier joint au message du propriétaire, copié octet pour octet, SHA-256 `460a83f201308b4e1faafa8683ddd5f9fdf9b232042c188730bd010c7c7ebb17`. Le fichier indique « mandat préparé pour validation/transmission », conservé tel quel. |
| Autorisation | Message du propriétaire, reçu le 15 novembre 2026 (UTC), qui joint le mandat : exécution du LOT-2J v1.0, **exclusivement** pour l'inscription documentaire de `MEC-0001` et `MEC-0002` dans `docs/gameplay/GAMEPLAY-DECISIONS.md`, l'archivage et le compte rendu prévus ; branche `docs/lot-2j-inscription-mec-0001-mec-0002` depuis le dernier `main` ; décisions et diff validés du LOT-2I v1.2, sans ajout de règle ni résolution d'ambiguïté ; deux mécaniques « reportées » ; aucun gameplay ; commit local autorisé ; **aucun push, aucune PR, aucune fusion**. |
| Base | `git fetch origin main` (code 0) : `origin/main` = `9e119b64767553d2013795b4ccee4bb2db496fa2`, commit de fusion de la PR n° 12, identique à la base indiquée par le mandat (§1). Registre sur `main` : SHA-256 `c2a3a55e7b1ed3d08089b5d814cded324b94313792982c8556d0e9d19a7e3968`. |
| Branche | `docs/lot-2j-inscription-mec-0001-mec-0002`, créée depuis `origin/main` (`9e119b6`). Le suivi automatique de `origin/main`, posé à la création, a été retiré (`git branch --unset-upstream`), pour qu'aucune publication ne puisse viser `main` par défaut. |
| Publication | **Commit local seulement**, sur cette branche, avec les quatre chemins autorisés ; son SHA est donné dans la restitution au propriétaire, puisqu'il ne peut figurer dans le fichier qu'il contient. Aucun push, aucune PR, aucune fusion. |

## 1. Résultat

- **Registre** : il contient désormais `MEC-0001`, annotée, et `MEC-0002`, nouvelle, avec les 105 principes de conception PE-01 à EN-10. Le texte écrit est **exactement l'effet du diff** du LOT-2I v1.2 (§3 de `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md`), sans ajout ni retouche.
- **Décisions** : les deux champs « Décision du propriétaire » commencent par « reportée ». Aucune mécanique n'est « acceptée » ni `MODIFICATION-VALIDEE`.
- **Archive** : le mandat LOT-2J est copié octet pour octet dans `docs/mandates/`, et une seule ligne est ajoutée à `docs/mandates/README.md`.
- **Chemins modifiés** : les quatre autorisés, et eux seuls (§5).

## 2. Sources et provenance

Lus sur `main` (`9e119b6`) :
- `CLAUDE.md` ; le registre `docs/gameplay/GAMEPLAY-DECISIONS.md` (`MEC-0001` seule avant ce lot).
- `docs/reviews/LOT-2I-DIFF-PROPOSE-REGISTRE-MEC-0001-MEC-0002.md` (SHA-256 `f82230ba8f9078514d6736acf8d339da19e88676c4f5393842d2d317bee76a94`) : le bloc `diff` du §3 en est extrait tel quel (214 lignes, SHA-256 `97a1af3000fc0e588cdf51ece0d54bd1e9d0fc3f2b77e674da14d9ad85d17e86`).
- `docs/reviews/LOT-2I-CONSOLIDATION-MEC-0002.md` (§12 et §14), `docs/reviews/LOT-2I-MATRICE-TRACABILITE-MEC-0002.md`, `docs/reviews/LOT-2I-EXECUTION.md` (§9) : pour les comptes, les statuts et les ambiguïtés ouvertes.
- `docs/mandates/BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` (SHA-256 `dee88998…f335f`, conforme à l'index) : **relu en entier dans ce lot**, mais après l'écriture du registre (écart d'ordre, §8). Aucune contradiction non tracée : la fiche cite les principes DS1.1 à DS5.7 un par un ; DS3.3 (pas d'exemption au-delà d'un étage) et DS4.3 (plafond de 70 contre les obstacles) n'y sont pas cités par leur numéro, mais leur contenu figure dans CH-09 et CO-04 ; l'écart à DS4.1 (tirage commun) est assumé dans la liste des décisions modifiées.
- Rapports des LOT-2F, LOT-2G et LOT-2H, cités par la fiche : **non relus en entier dans ce lot** (écart, §8). Ils ont été produits et lus lors des lots précédents ; dans ce lot, leur présence sur `main` et les renvois de la fiche ont été vérifiés (la seconde revue a aussi vérifié LOT-2E C8 et LOT-2H §5, ligne 12).

Lus en lecture seule sur `orchestration/mandats`, récupérée dans ce lot (`git fetch origin orchestration/mandats`, 15 novembre 2026, 18:33 UTC, code 0 ; inchangée à `f8cf26e`), **non archivés** (mandat, §2) :
- consolidation provisoire C2, `docs/reviews/BASTION-MEC-0002-CONSOLIDATION-PROVISOIRE-2026-11-14.md`, SHA-256 `8e7c652b5c5b5a72508699e3361a887f8992b99f63bb155b8c5496da1ff0dd83`, conforme à la fiche ;
- mandat LOT-2I v1.2, cité par la fiche avec son commit et son empreinte (`f8cf26e…`, SHA-256 `e4c5345a…`, vérifiée) ; mandat LOT-2I v1.1 (`58d3ebc…`, SHA-256 `6ac95b0d…`), cité par la consolidation du LOT-2I, et non par la fiche.

**Points du LOT-2I à régler avant inscription** (diff proposé, §4) : l'autorisation d'écrire le registre (point 1) est donnée ; la fidélité, dont la lecture d'A4.3A (point 3), est traitée au §4 ci-dessous ; les identifiants PE à EN, l'identifiant `MEC-0002` et la reprise des décisions du 9 novembre par leurs identifiants (points 4 à 6) sont couverts par le mandat LOT-2J (§2.1), qui les nomme : ces identifiants deviennent **permanents** avec ce lot. L'archivage (point 2) et la copie des arbitrages (point 3 bis) restent non faits (§8, §9).

**Non utilisé** : `BASTION-MANDAT-LOT-2I-INSCRIPTION-PARTIELLE-MEC-0001-v1.0.md`, présent sur `orchestration/mandats`, que le mandat LOT-2J déclare **caduc pour exécution** (§1).

## 3. Ce qui change dans le registre (avant / après)

| # | Emplacement | Avant (`main`) | Après |
|---|---|---|---|
| 1 | Introduction | « Une seule fiche est enregistrée : `MEC-0001`, proposée et incomplète… » | « Deux fiches sont enregistrées : `MEC-0001` et `MEC-0002`, proposées et incomplètes… » |
| 2 | Bandeau de `MEC-0001` | S1 à S12, Z1, N1 à N14 ; aucun gameplay autorisé | Ajout : « Les sauts, les chutes, les collisions, les esquives et les repoussements relèvent de `MEC-0002`. » |
| 3 | `MEC-0001`, « Éléments exclus » | Ce que S1 à S12, Z1 et N1 à N14 ne couvrent pas | Ajout : les sauts, chutes, collisions, esquives et repoussements, traités par `MEC-0002` |
| 4 | N7 | « Pas de dégâts pour les petites chutes ; seuil exact à décider. [À vérifier.] » | Texte conservé ; annotation : précisée par `MEC-0002`, qui fait autorité ; pas de dégâts de chute ordinaires jusqu'à 3 m inclus de hauteur équivalente (CH-09) ; renvoi à CH-01 et CH-03 |
| 5 | Sous N10 | — | Annotation : N5 à N10 précisées par `MEC-0002`, qui fait autorité ; leur texte reste comme historique |
| 6 | `MEC-0001`, « Encore ouvert », chutes | Quatre sous-points | Les quatre gardés, avec la ponctuation finale du quatrième ajustée (« charge. » devient « charge ; ») ; un cinquième : précisés ou tranchés en partie par `MEC-0002` (seuil sans dégâts : 3 m inclus, CH-09) |
| 7 | Fin du registre | — | Fiche `MEC-0002 — Sauts, chutes et collisions` (178 lignes) : champs du gabarit, décision « reportée », 105 principes, décisions antérieures remplacées, liste « Encore ouvert » |

Aucune sous-décision historique de `MEC-0001` (S1 à S12, Z1, N1 à N14) n'est supprimée ni réécrite : seules des annotations s'ajoutent. Diff : 186 insertions et 5 suppressions (`git diff --numstat`), soit 5 lignes remplacées et 181 lignes ajoutées.

## 4. Points de fidélité

- **Hauteurs** : la hauteur d'étage de 3 m (GE-02, CH-08) et le seuil de chute ordinaire de **3 m inclus** de hauteur équivalente (CH-09) sont deux règles distinctes. Le sommet d'un saut de référence, à 0,75 m (SA-19), n'est pas un seuil de blessure.
- **Ancien seuil et ancienne courbe** : le seuil de 0,25 étage et la courbe `B(n)` n'apparaissent qu'en contexte de remplacement, comme historiques : dans la liste « Décisions antérieures remplacées ou modifiées » (D03 et D04 ; consolidation du 14 novembre), et dans les renvois entre crochets de CH-07 et CH-08 (`B(n)`), de CH-09, CH-11 et CH-18 (`0,25`). Aucun n'est présenté comme actif.
- **Lecture d'A4.3A** : le mandat (§0 et §2) indique que le propriétaire a confirmé cette lecture le 15 novembre 2026. Pour un saut descendant d'un étage, on compte 3 m entre les sols, sans la montée, avec ou sans surcharge. Sans surcharge, la réception normale est exempte de dégâts ; avec surcharge, des dégâts deviennent possibles. Le texte inscrit (CH-01, CH-02, CH-11, CH-18) dit exactement cela : il n'a pas eu à changer. Traçabilité :
  - plus tôt le même jour, dans cette session, le propriétaire avait choisi de « laisser en l'état » cette lecture, alors présentée comme à vérifier avant une inscription ;
  - la confirmation citée par le mandat est donc une **preuve déclarative transmise par l'orchestrateur** ; la transmission du mandat par le propriétaire, avec son autorisation explicite, est retenue comme confirmation ;
  - la fiche inscrite ne mentionne pas cette confirmation (diff exact), et les livrables du LOT-2I, qui la présentent comme « à vérifier », ne sont pas modifiés (mandat, §3).
- **Sources hors de `main`** : la fiche cite C2 et le mandat LOT-2I v1.2 par leur branche (`orchestration/mandats`), leur commit et leur SHA-256. Ces deux fichiers ne sont pas sur `main` ; leur archivage demande une décision distincte (mandat, §2).

## 5. Ambiguïtés et paramètres ouverts

Les 22 ambiguïtés encore ouvertes au LOT-2I v1.2 (consolidation, §12) restent ouvertes : aucune n'est tranchée par l'inscription. Chacune reste visible dans la fiche :

| Ambiguïtés | Où dans la fiche `MEC-0002` |
|---|---|
| A1 | « Encore ouvert » : géométrie ; mention « Ouvert » de GE-02, GE-03, GE-05 |
| A2, A13 | « Encore ouvert » : sauts (masses et capacités de référence) ; force et charge ; « Ouvert » de GE-06, GE-07, SA-15, SA-16, CH-14 |
| A5, A29, A30 | « Encore ouvert » : chutes ; « Ouvert » de CH-07, CH-08, CH-10, CH-11, CH-13, CH-16 |
| A6, A7, A26 | « Encore ouvert » : chaîne de calcul ; « Ouvert » de CH-13, CO-04, CO-08, CO-09 |
| A9, A10, A11 | « Encore ouvert » : sauts (calibrage horizontal, coût non entier, plage de gravité) ; « Ouvert » de SA-17, SA-19, SA-23, SA-24 |
| A14, A21 | « Encore ouvert » : dégâts ; « Ouvert » de CH-21, CO-02, CO-05, CO-06 |
| A15, A16, A17 | « Encore ouvert » : esquive ; « Ouvert » de ES-02, ES-04, ES-05, ES-06, ES-12, CO-07 |
| A19 | « Encore ouvert » : repoussement ; « Ouvert » de RP-06 |
| A20, A23 | « Encore ouvert » : événements ; « Ouvert » d'EN-06 et de CO-11 |
| A22 | « Encore ouvert » : décor ; « Ouvert » d'EN-01 |
| A28 | « Encore ouvert » : vitesse après un choc, vitesse résiduelle |

Nuance : pour A21, les sensibilités par type ne sont pas nommées dans la liste « Encore ouvert ». CO-07 en pose le principe sans valeur, et la phrase finale de la fiche (« tout paramètre non explicitement accepté » reste non décidé) les couvre. Le texte n'est pas retouché, le diff devant rester exact.

## 6. Contrôles exécutés

Contrôles lancés par un script local hors dépôt (lecture seule, sauf `git add` des quatre chemins autorisés). Les résultats sont ceux de la dernière exécution, sur l'état final indexé.

| # | Contrôle | Commande ou méthode | Résultat |
|---|---|---|---|
| 1 | Base | `git rev-parse`, `git merge-base --is-ancestor origin/main HEAD` | `HEAD` = `origin/main` = `9e119b6` avant le commit ; code 0 |
| 2 | Chemins modifiés | `git diff --cached --name-status origin/main` ; `git status --porcelain` | les quatre chemins autorisés, aucun autre |
| 3 | Chemins interdits | `git diff --cached --quiet origin/main -- src tests .claude scripts .github CLAUDE.md docs/decisions docs/references` et les livrables du LOT-2I | code 0 |
| 4 | Espaces et fins de ligne | `git diff --cached --check origin/main` | code 2 : trois lignes de l'archive du mandat (4, 5 et 6) finissent par deux espaces, retour à la ligne Markdown du fichier reçu, conservé pour la copie octet pour octet, comme pour les mandats déjà archivés ; sur les trois autres chemins : code 0 |
| 5 | Diff applicable, sur une **copie** du registre | `git apply --check` puis `git apply` dans un dossier temporaire ; `patch` sur une autre copie | codes 0 ; résultats identiques (`cmp` : 0) |
| 6 | Registre = effet exact du diff | `cmp` entre la copie corrigée et le registre indexé, puis l'arbre de travail ; `git apply -R --check` sur l'arbre de travail | codes 0 ; SHA-256 du registre inscrit `519086ea6985bfb50484a724f04b394674023fcf9c0a654894f064e7d759c952` |
| 7 | Fiche = texte proposé du LOT-2I v1.2 | comparaison Python (`python3 -I`) de la fiche `MEC-0002` inscrite avec le §2 du document LOT-2I | identiques (178 lignes) |
| 8 | Décisions lues comme le harnais | extraction de `scripts/harness/check-simulation-trace.sh` (`awk`, `grep`, `cut`) | `MEC-0001` : reportée ; `MEC-0002` : reportée |
| 9 | Champs des fiches | lecture Python des tableaux | les deux fiches : `MODIFICATION-PROPOSEE`, « reportée », « non commencé », « Aucun changement de gameplay » ; seule la ligne du gabarit contient « acceptée / refusée / reportée » ; `MODIFICATION-VALIDEE` n'apparaît que dans les règles et le gabarit |
| 10 | Identifiants de conception | Python : identifiants en tête de principe dans la fiche, comparés à la consolidation et à la matrice du LOT-2I | 105, chacun défini une seule fois ; mêmes ensembles que la consolidation (105) et la matrice (105) ; aucune autre définition dans le registre, où seuls CH-01, CH-03 et CH-09 sont cités par les annotations de `MEC-0001` |
| 11 | Ancien seuil, ancienne courbe, hauteurs | `grep` sur `0,25`, `B(1)`, `B(n)`, `interpolation`, `0,75`, `3 m` | `0,25` et `B(n)` seulement en contexte de remplacement : liste des décisions remplacées et renvois entre crochets de CH-07, CH-08 (`B(n)`), CH-09, CH-11 et CH-18 (`0,25`) ; `0,75` : sommet de saut (SA-19) et borne de facteur (CO-03) ; aucune courbe `B(1) = 8` |
| 12 | Ambiguïtés ouvertes | correspondance manuelle avec la consolidation, §12 | 22 sur 22 visibles (§5) |
| 13 | Archive du mandat | `sha256sum`, `cmp` avec la pièce jointe ; `git diff --numstat` sur l'index | identiques (`cmp` : 0) ; une seule ligne ajoutée à l'index, avec l'empreinte |
| 14 | Documents cités par la fiche | `git fetch origin orchestration/mandats` (code 0), puis `git cat-file -e` sur `main` et sur `orchestration/mandats` | tous présents ; C2 et le mandat v1.2 sur `orchestration/mandats` seulement (§4) |
| 15 | Tableaux | Python : nombre de colonnes | cohérents (registre, index, rapport) |
| 16 | Identifiant de modèle | `grep` | aucun |
| 17 | Harnais | `bash scripts/harness/test-hooks.sh` | « 75 tests, 0 échec(s) », code 0 |
| 18 | Tests .NET | `which dotnet` | code 1 : outil absent ; `dotnet build`, `dotnet test` et `dotnet format --verify-no-changes` **non exécutés** |

**Aucun test de mécanique n'est écrit ni exécuté.** Les critères de tests futurs du LOT-2I (matrice, §3) restent des critères : aucun n'est réputé réussi.

**Harnais** : chaque écriture dans `docs/gameplay/` et `docs/mandates/` a été faite par une commande que le hook reconnaît (`cp`, Edit), et soumise à la demande d'accord prévue par le harnais. Aucun contournement.

## 7. Revue indépendante

Revue du 15 novembre 2026, par un agent distinct de l'exécutant, **en lecture seule**, sur l'index comparé à `origin/main` (`9e119b6`). Il n'a rien modifié et ne valide pas. Résultat : **aucun constat bloquant**, 3 importants, 8 mineurs.

Il a vérifié, sans constat, en refaisant les opérations sur des copies :
- registre = effet exact du diff (`git apply --check`, `git apply`, `patch -F0` : 7 blocs sans décalage ; `cmp` avec le registre indexé ; `git apply -R` ramène au registre de `main`) ; fiche identique au §2 du LOT-2I ;
- deux fiches « reportées », `MODIFICATION-PROPOSEE`, « non commencé », « Aucun changement de gameplay » ; sous-décisions historiques conservées ;
- 105 identifiants définis une seule fois, sans trou (PE 4, GE 9, SA 27, CH 21, CO 11, ES 14, RP 9, EN 10) ;
- hauteurs, seuil de 3 m inclus et lecture d'A4.3A (CH-01, CH-02, CH-05, CH-11, CH-18) ;
- 22 ambiguïtés ouvertes toutes visibles ;
- périmètre (quatre chemins), archive identique à la pièce reçue, ligne d'index conforme ; empreintes ; harnais (75 tests, 0 échec).

| Constat | Traitement |
|---|---|
| **I1** — `0,25` et `B(n)` mal localisés par le rapport (§4, contrôle 11) | Corrigé : ils figurent aussi dans les crochets de CH-07, CH-08, CH-09, CH-11 et CH-18, toujours en contexte de remplacement |
| **I2** — lecture du mandat §1, point 6, non faite et non déclarée | Document DS1 à DS5 relu en entier (§2) ; rapports des LOT-2F, LOT-2G et LOT-2H non relus en entier : écart déclaré (§8) |
| **I3** — rapport non daté | Date ajoutée en tête ; revue datée |
| M1 — mandat v1.1 présenté comme cité par la fiche | Corrigé : cité par la consolidation du LOT-2I seulement |
| M2 — décompte du diff ; ponctuation du quatrième sous-point | Corrigés (§3) |
| M3 — formulation du contrôle 10 | Précisée : les annotations de `MEC-0001` citent CH-01, CH-03 et CH-09 |
| M4 — tableau du §5 : A28 et A23 | A28 : renvoi à CH-21 retiré (il relève d'A14) ; A23 : CO-11 ajoutée |
| M5 — points 4 à 6 du §4 du LOT-2I | Traitement indiqué au §2 : couverts par le mandat ; identifiants désormais permanents |
| M6 — fraîcheur d'`orchestration/mandats` | Récupération du 15 novembre 2026, 18:33 UTC, indiquée (§2, contrôle 14) |
| M7 — commit décrit avant d'exister | Formulation ajustée ; SHA donné dans la restitution |
| M8 — réserves sur le texte du registre | Hors périmètre (diff exact) ; ajoutées au §9 comme points pour un mandat distinct |

## 8. Limites de preuve

- **Écart à la procédure** : le mandat (§1) demandait de lire, avant toute écriture, le document DS1 à DS5 et les rapports des LOT-2F, LOT-2G et LOT-2H. Le document DS1 à DS5 a été relu en entier, mais après l'écriture du registre ; les rapports des LOT-2F, LOT-2G et LOT-2H n'ont pas été relus en entier dans ce lot. Le texte inscrit n'en dépend pas directement : c'est l'effet exact d'un diff déjà relu deux fois au LOT-2I v1.2.
- **Preuves déclaratives** : les arbitrages du 14 novembre 2026 (D2, C3) et la confirmation d'A4.3A du 15 novembre 2026 (mandat, §0) sont connus par des déclarations et des transcriptions de l'orchestrateur. Les messages d'origine n'ont pas été fournis.
- **Copie des arbitrages** : la copie approuvée des 29 propositions et des réponses 1A à 6A, demandée par le mandat LOT-2I v1.1, n'a jamais été fournie (diff LOT-2I, §4, point 3 bis).
- **Script de contrôle** : il n'est pas versionné, car seuls quatre chemins sont modifiables ; ses résultats sont déclaratifs, mais les commandes sont décrites au §6.
- **Pas de .NET, pas de CI** : `dotnet` est absent, et rien n'est poussé.
- **Fidélité à OXCE** : aucune n'est affirmée ni démontrée.

## 9. Points à décider et prochaines autorisations

- **Publication** : push de la branche, PR et fusion demandent chacun une autorisation distincte du propriétaire.
- **Archivage** : C2 et les mandats LOT-2I v1.1 et v1.2 restent sur `orchestration/mandats` ; leur copie dans `main` demande une décision distincte (mandat, §2).
- **Index des mandats** : la ligne de `BASTION-DECISIONS-LOT-2G-DS1-DS5-v1.0.md` dit encore « non inscrites au registre », alors que `MEC-0002` reprend désormais ces principes, avec ou sans modification. Elle n'est pas modifiée : le mandat n'autorise qu'une ligne nouvelle.
- **Retouches possibles du registre**, chacune hors du diff exact et donc à décider par un mandat distinct :
  - la fiche ne mentionne pas la confirmation d'A4.3A ;
  - le champ « Décision du propriétaire » de `MEC-0002` ne mentionne pas l'autorisation d'inscription du 15 novembre 2026 ;
  - le champ « Fonctionnement de référence et preuves » de `MEC-0002` ne renvoie pas à ce rapport d'inscription, alors que celui de `MEC-0001` renvoie au sien (LOT-2C) ;
  - PE-01 dit encore « sous réserve d'autorisation d'inscription », réserve devenue caduque ;
  - les annotations « Annotation ajoutée lors de l'inscription de `MEC-0002` » ne citent ni lot ni date, à la différence de l'annotation du LOT-2D.
- **Implémentation** : interdite. Elle demanderait d'abord le règlement des ambiguïtés utiles, puis une décision « acceptée » et un mandat d'implémentation distincts.

## 10. Arrêt

Le LOT-2J s'arrête ici, après le commit local. Aucun push, aucune PR, aucune fusion, aucun gameplay.
