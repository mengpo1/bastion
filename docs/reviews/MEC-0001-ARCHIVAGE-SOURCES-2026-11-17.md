# Bastion — Archivage des sources documentaires MEC-0001

**Date d'exécution :** 18 novembre 2026  
**Nature :** archivage documentaire, sans modification des décisions de gameplay.  
**Mandat :** « BASTION — Projet de mandat d'archivage des sources MEC-0001 — v1.0 », validé explicitement par le propriétaire le 18 novembre 2026, incluant commit, push sur branche dédiée et ouverture d'une PR, sans fusion.

## Provenance et base

- Source : archive `BASTION-LOT-ARCHIVAGE-MEC-0001-SOURCES-ET-MANDAT.zip` fournie dans la conversation, contenant les deux documents historiques du 17 novembre 2026 et le mandat d'archivage.
- Base : `main` au commit `af832cf2aa1c13bdf00f44ecdd71b3543a2ffc70` (PR n° 14 déjà fusionnée).
- Branche : `docs/archive-mec-0001-sources-2026-11-18`.
- Opération : un commit documentaire unique, puis PR vers `main` ; **aucune fusion autorisée**.

## Documents archivés, sans modification de contenu

| Chemin dans le dépôt | Taille | SHA-256 de la source |
|---|---:|---|
| `docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md` | 8 927 octets | `90e049c751aa797c79cf8202439f723f1278449af0d3abe58467f07b3a5885e0` |
| `docs/reviews/BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md` | 39 919 octets | `b7874c48169c8c4a8af38fb5b52d56516d90114fb1dae23cd1a621694ae1b3cc` |

Les deux empreintes ont été recalculées sur les originaux de l'archive avant l'écriture. La vérification des objets Git publiés permet de confirmer ensuite leur identité octet pour octet.

## Contrôles, limites

- Les trois chemins cibles étaient absents sur `main` au démarrage ; aucune réécriture de fichier existant.
- Les documents historiques restent intacts, y compris les formulations et statuts datés.
- Vérification locale équivalente à `git diff --check` sur l'ajout des deux sources : cinq avertissements de blancs de fin de ligne dans la consolidation (lignes 3 à 7) correspondant aux **doubles espaces Markdown d'origine** ; ils sont conservés pour respecter l'égalité des empreintes. Le mandat historique ne produit aucun avertissement.
- Aucun test applicatif ou harnais n'a été exécuté localement lors de cet archivage par l'orchestrateur ; l'état de la CI doit être rapporté séparément après publication.
- Aucune modification des règles, de MEC-0001/MEC-0002, du code, des tests, de la CI, des références ou de l'équilibrage ; trois fichiers ajoutés uniquement.

**Statut :** MEC-0001 reste `reportée`, `MODIFICATION-PROPOSEE`, `non commencé` ; archivage seul, aucune autorisation de gameplay.
