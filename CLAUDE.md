# Règles permanentes pour Claude Code — Bastion

Ces règles s'appliquent à chaque session. Elles ne changent que par un mandat distinct validé par le propriétaire.

## Rôles

- **Propriétaire** : valide les décisions.
- **ChatGPT** : orchestre et rédige les mandats.
- **Claude Code** : exécute un mandat à la fois.

## 1. Périmètre

- Travailler uniquement dans le périmètre du mandat en cours (`docs/mandates/`). Ce qui n'est pas demandé n'est pas fait.
- En cas d'ambiguïté, de doute sur le périmètre ou de changement destructif : s'arrêter et demander.
- Ne rien écraser, supprimer, déplacer ou migrer silencieusement.
- S'arrêter à la fin du lot. Ne pas enchaîner sur le lot suivant.

## 2. Simplicité

- Choisir la solution la plus simple, compréhensible et testable qui suffit.
- Pas de couche, framework, script, agent ou automatisation sans besoin démontré. Pour tout ajout complexe : justifier et demander un arbitrage avant.

## 3. Gameplay

- Aucune mécanique de jeu sans décision au statut « Validée » dans `docs/gameplay/GAMEPLAY-DECISIONS.md`.
- Aucune modification de mécanique, même présentée comme une simplification temporaire.
- Ne jamais inscrire ni modifier une décision dans les registres (`docs/gameplay/`, `docs/decisions/`, `docs/references/`) sans validation explicite du propriétaire.

## 4. Propriété intellectuelle

- Aucun asset X-COM original.
- Aucune copie de code OXCE sans audit de licence et décision enregistrée.

## 5. Git

- Ne jamais travailler directement sur `main`. Une branche dédiée par mandat.
- Pas de `git push`, fusion, rebase, publication ni effacement sans approbation explicite du propriétaire.

## 6. Preuves

- Toute réussite annoncée s'appuie sur les commandes réellement exécutées, leur sortie et leur code de sortie. Sans sortie observable, pas de succès déclaré.
- Fin de mandat : rapport dans `docs/reviews/` (résumé, fichiers, vérifications, limites, points à décider).

## 7. Architecture

- `Bastion.Simulation` ne dépend pas de Godot. L'interface Godot sera un projet distinct.

## 8. Harnais

- Ne pas modifier, neutraliser ni contourner le harnais (`.claude/`, `scripts/harness/`, `.github/workflows/`, ce fichier) sans mandat distinct.
- Les hooks ne détectent pas tout : ces règles s'appliquent même quand aucun hook ne bloque.

## Commandes

```bash
dotnet build
dotnet test
dotnet format --verify-no-changes
bash scripts/harness/test-hooks.sh
```
