# BASTION — Mandat LOT-1I v1.0
## Correction des incohérences documentaires RH-02 et RH-08

**Statut : PRÉPARÉ — exécution non encore autorisée**

**Dépôt :** `mengpo1/bastion`  
**Base vérifiée :** `main` — `10f4a0a51d2b3f2296a13cd1aeff46d7a5a8e8c5`  
**Branche proposée :** `claude/lot-1i-corrections-documentaires`

### 1. Objectif

Résoudre les deux observations documentaires RH-02 et RH-08 du rapport `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`.

Le travail est exclusivement documentaire. Il ne doit introduire aucune règle ou fonctionnalité.

### 2. RH-02 — Actualisation de la notice Godot

**Fichier :** `src/Bastion.Client.Godot/README.md`

Conserver le compte rendu historique des six essais macOS du 23 novembre 2026 concernant le lot 1D.

Ajouter séparément le compte rendu du propriétaire du 25 novembre 2026, concernant LOT-1G :

| Essai | Résultat déclaré |
|---|---|
| Charger le scénario 4 | Satisfaisant |
| Terminer le premier tour | Satisfaisant |
| Terminer le deuxième tour | Satisfaisant |
| Déplacer puis terminer le tour | Satisfaisant |
| Réinitialiser | Satisfaisant |
| Vérifier les anciens scénarios | Satisfaisant |
| Vérifier la fenêtre | Satisfaisant |

**Source documentaire :** annexe A de `docs/reviews/LOT-1H-CLOTURE-MEC-0004.md`.

Ces sept résultats sont des déclarations du propriétaire, sans reproduction indépendante.

La version exacte du commit testé, les modalités d'affichage et les périphériques physiques utilisés ne sont pas établis par ce compte rendu. Ne pas les inventer.

Corriger toutes les mentions de la notice devenues inexactes, notamment :

- Le titre de la section macOS, ligne 96.
- L'affirmation selon laquelle les scénarios 2 à 4 n'ont pas été testés, ligne 107.
- La réserve macOS, ligne 175.
- L'affirmation générale concernant l'absence d'essais sur écran réel, ligne 176, à reformuler sans supposer des modalités matérielles non documentées.
- Le récapitulatif des vérifications macOS, ligne 197.

Préserver les informations concernant les tests Linux, la CI, les captures Xvfb et les commandes d'installation.

### 3. RH-08 — Mandat absent de l'index

**Fichier :** `docs/mandates/README.md`

Ajouter une entrée pour le document existant :

`BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md`

Ce document est déjà présent dans le dépôt.

Pour cette entrée :

1. Lire le document original intégralement.
2. Reprendre son titre exact.
3. Indiquer sa provenance et son statut tels qu'ils sont documentés.
4. Calculer son empreinte SHA-256 à partir du fichier réellement présent.
5. Vérifier la cohérence avec le format des entrées existantes.

Ne pas modifier le mandat original.

Ne pas transformer son autorisation de modifications documentaires locales en autorisation de publication ou d'implémentation.

### 4. Archivage et traçabilité

Archiver le présent mandat sous :

`docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md`

Ajouter son entrée à `docs/mandates/README.md`.

Créer un rapport :

`docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md`

Il doit contenir :

- Le contexte des observations RH-02 et RH-08.
- Les modifications exactes.
- Les sources documentaires utilisées.
- Les résultats de vérification.
- Une relecture indépendante ciblée.
- Les éventuelles réserves non résolues.
- Le diff final et les empreintes.

### 5. Fichiers autorisés

Quatre fichiers uniquement :

1. `src/Bastion.Client.Godot/README.md`
2. `docs/mandates/README.md`
3. `docs/mandates/BASTION-MANDAT-LOT-1I-v1.0.md`
4. `docs/reviews/LOT-1I-CORRECTIONS-DOCUMENTAIRES.md`

Les deux derniers sont nouveaux.

### 6. Vérifications

- Vérifier la base Git et l'absence de modifications locales étrangères au lot.
- Comparer le diff à ce mandat.
- Contrôler que toutes les mentions obsolètes de la notice Godot ont été traitées.
- Vérifier les empreintes des mandats indexés.
- Exécuter les contrôles applicables du harnais.
- Effectuer une relecture indépendante ciblée sur l'exactitude documentaire et le respect du périmètre.

### 7. Restrictions

- Aucun changement du code C# ou Godot.
- Aucun changement des tests.
- Aucun changement du registre de gameplay.
- Aucun changement des documents historiques.
- Aucun changement de CI, hooks ou harnais.
- Aucune nouvelle mécanique.
- Aucun travail sur MEC-0001 ou MEC-0002 au-delà de l'indexation du document déjà existant.

### 8. Publication

L'exécution proposée est **locale uniquement**.

Aucun commit, push, PR ou fusion n'est autorisé par ce mandat.

Après les vérifications, transmettre le rapport et le diff complet à l'orchestrateur, puis arrêter le travail en attendant une autorisation de publication distincte.
