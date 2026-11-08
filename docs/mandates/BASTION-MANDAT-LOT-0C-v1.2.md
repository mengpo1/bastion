# BASTION — Mandat LOT-0C v1.2
## Qualification du harnais

**Statut : préparé — en attente d'autorisation du propriétaire**  
**Dépôt :** `mengpo1/bastion`  
**Branche de départ :** `main` — commit `9ece89df9acd88bcf8c8c2eb8215ffd5937a04b4`  
**Branche de travail :** `chore/lot-0c-qualification`

**Remplace la version préparatoire v1.1.** Le périmètre technique est inchangé ; la v1.2 clarifie la transmission et l'archivage à l'identique des mandats.

## 1. Objectif

Qualifier le harnais installé au lot 0B, conformément aux exigences de la spécification v0.2.

Identifier les contrôles efficaces, leurs limites et les risques résiduels.

**Règle fondamentale : simplicité avant tout.**

Aucun développement de gameplay.

## 2. Préparation documentaire

Au début du lot :

1. Le propriétaire transmet **ce fichier `.md`**, qui constitue le document de référence. Claude Code l'archive **octet pour octet**, sans reformulation ni changement de mise en forme, dans `docs/mandates/` ; il vérifie et consigne son empreinte SHA-256.
2. Archiver également le mandat `LOT-0B-FUSION` à partir de son original **si celui-ci est disponible**. S'il ne reste que le texte de la conversation, l'archiver comme **transcription**, en l'indiquant expressément dans `docs/mandates/README.md`, sans prétendre à l'identité avec un fichier original indisponible.
3. Compléter l'index documentaire avec les empreintes SHA-256 et la provenance de chaque document (original `.md` ou transcription de conversation).
4. Ajouter une seule ligne dans `CLAUDE.md` renvoyant au protocole d'échange de la section 3.
5. Compléter `docs/decisions/TECHNICAL-DECISIONS.md` pour retracer les arbitrages déjà approuvés le 8 novembre 2026 :
   - .NET 10 conservé à titre provisoire, avec `latestFeature`.
   - Format `.slnx` conservé.
   - Architecture C# avec simulation indépendante de Godot.
   - Avertissements NuGet conservés comme erreurs.
   - Deux limites des hooks acceptées provisoirement : faux positif sur `rm -rf` cité et détection incomplète d'une dépendance Godot déclarée mais inutilisée.
   - Compatibilité Godot toujours non vérifiée.

Ne pas transformer un choix provisoire en validation définitive. Conserver les autres choix techniques à leur statut actuel, sauf autorisation explicite.

Les fichiers protégés restent soumis aux demandes d'accord des hooks.

## 3. Protocole d'échange GitHub

- **Mandats :** l'orchestrateur fournit un fichier Markdown `.md` au propriétaire, qui le joint à la conversation Claude Code. Claude Code archive le fichier reçu sans modification, vérifie et consigne son SHA-256 et demande les autorisations exigées par les hooks.
- **Repli si texte collé :** l'archiver tel que reçu, et noter explicitement **« transcription depuis la conversation ; identité avec le fichier original non vérifiée »** dans `docs/mandates/README.md`. Le SHA-256 porte alors sur la transcription, et non sur un original supposé.
- **Rapports :** Claude Code les rédige et les commite dans `docs/reviews/`.
- **Publication autorisée pour ce seul lot :** pousser exclusivement `chore/lot-0c-qualification`, une fois le présent mandat explicitement autorisé, et ouvrir une PR en brouillon vers `main`.
- **Interdictions :** ne jamais pousser vers `main`, effectuer de force push, ni fusionner une PR sans autorisation distincte.
- **Revue :** l'orchestrateur consulte les commits, rapports et résultats de CI directement via GitHub, sur la branche du lot tant que celle-ci n'est pas fusionnée.

Aucun nouveau dossier ni outil de synchronisation.

## 4. Qualification technique

Exécuter les dix scénarios H-Q01 à H-Q10 définis dans la spécification v0.2 :

| ID | Vérification |
|---|---|
| H-Q01 | Erreur de compilation intentionnelle |
| H-Q02 | Test volontairement faux |
| H-Q03 | Divergence avec une règle OXCE de référence |
| H-Q04 | Écriture dans un registre protégé |
| H-Q05 | Modification de gameplay sans décision approuvée |
| H-Q06 | Rapport absent ou incomplet |
| H-Q07 | Modification hors mandat détectée en revue indépendante |
| H-Q08 | Tentative de modification non autorisée du harnais |
| H-Q09 | Reproductibilité d'un scénario déterministe |
| H-Q10 | Démarrage de Godot en mode headless |

**Contraintes :**

- Utiliser des copies jetables pour les essais destructifs et les injections de défauts.
- Ne jamais introduire volontairement un test cassé dans `main`.
- Ne pas inventer de mécaniques pour H-Q03, H-Q05 et H-Q09. Utiliser une démonstration technique lorsque possible, en la qualifiant de preuve partielle.
- Si Godot est indisponible pour H-Q10, documenter le report.
- Ne pas masquer un échec pour obtenir artificiellement dix résultats positifs.

Chaque scénario doit produire un résultat vérifiable, avec ses limites.

## 5. Revue indépendante

Mandater un agent distinct, en lecture seule, pour examiner :

- Les essais réalisés.
- Les preuves de réussite ou d'échec.
- Les limites non couvertes.
- Les risques résiduels.
- Les éventuelles modifications hors mandat.

Le relecteur ne doit pas modifier le code ni autoriser sa propre validation.

## 6. Livrables

Créer `docs/reviews/LOT-0C-QUALIFICATION.md`.

Le rapport doit contenir :

- Le résultat de chacun des dix essais : réussi, échoué, partiel ou reporté.
- Les commandes exécutées, codes de sortie et preuves.
- Les modifications apportées au dépôt.
- Les observations de la revue indépendante.
- Les risques résiduels.
- Les points nécessitant un arbitrage.

Exécuter les vérifications C# et les tests des hooks.

Pousser la branche autorisée et ouvrir une PR en brouillon. Fournir le lien de la PR, le SHA du dernier commit et le résultat de la CI.

## 7. Interdictions et arrêt

- Aucun développement de mécanique de jeu.
- Aucune refonte de l'architecture.
- Aucun ajout de complexité sans besoin démontré.
- Aucun nouveau dossier.
- Aucune suppression ou neutralisation de protection.
- Aucune modification directe de `main`.
- Aucune fusion de PR.

Si une correction importante du harnais devient nécessaire, la documenter et demander un arbitrage avant de l'implémenter.

**S'arrêter à la fin du lot 0C. Ne pas commencer le lot 0D.**
