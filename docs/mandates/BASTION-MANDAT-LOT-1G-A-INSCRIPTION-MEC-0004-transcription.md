# BASTION — Mandat d'inscription MEC-0004 v1.2

**Statut : PRÉPARÉ — exécution non encore autorisée**

**Dépôt :** `mengpo1/bastion`  
**Objet :** inscrire une décision de gameplay validée, sans implémentation.

## 1. Décision du propriétaire

Le 23 novembre 2026, le propriétaire a explicitement validé MEC-0004 v1.2 par la réponse « oui » à la question :

« Validez-vous MEC-0004 v1.2 dans son ensemble ? »

La version validée correspond à MEC-0004 v1.1, complétée par les trois précisions de la v1.2.

Ne pas interpréter cette validation comme une autorisation d'implémentation.

## 2. Travail demandé

Inscrire MEC-0004 dans :

`docs/gameplay/GAMEPLAY-DECISIONS.md`

Respecter le gabarit du registre et renseigner :

| Champ | Valeur |
|---|---|
| Identifiant | MEC-0004 |
| Classe | `MODIFICATION-VALIDEE` |
| Décision | Acceptée le 23 novembre 2026 |
| Fonctionnement de référence | Règles Bastion, renvois à ARB-D, Q3.6 et Q4.6 ; aucune fidélité à OXCE revendiquée |
| État d'implémentation | `non commencé` |
| Tests | T01 à T16, prévus et non exécutés |

## 3. Contenu fonctionnel à inscrire

Reprendre intégralement les règles validées :

- Une seule unité et une commande explicite de fin de tour.
- Tour initial numéroté 1.
- TU maximales 60, récupération 60.
- Énergie maximale 100, récupération 20.
- Paramètres configurables.
- TU : addition du solde et de la récupération, plafonnée.
- Énergie : addition du solde et de la récupération, plafonnée ; formule nouvellement validée par MEC-0004.
- Plafonds strictement positifs ; récupérations nulles admises ; valeurs négatives refusées.
- Récupération supérieure au plafond autorisée ; état initial supérieur au plafond refusé.
- Aucune fin de tour automatique.
- Position et orientation conservées.
- Chemin du dernier déplacement conservé après la fin de tour ; dernier résultat remplacé par le compte rendu de fin de tour.
- Exclusion de la surcharge ; facteur neutre égal à 1 conformément à Q3.14.
- Scénario Godot 4 : touche 4 (AZERTY compris), touche T pour finir le tour, touche R pour réinitialiser ; état initial 12 TU et 35 énergie ; les scénarios 1 à 3 restent inchangés.

Reprendre également les exclusions, les règles d'architecture et les seize tests de la fiche v1.2 validée.

Ne pas inventer de règles complémentaires.

## 4. Contraintes

- Ne pas modifier les décisions MEC-0001, MEC-0002 et MEC-0003.
- Ne pas modifier la simulation ni le client Godot.
- Ne pas écrire de tests ni de code applicatif.
- Ne pas modifier la CI ou le harnais.
- Vérifier que l'inscription correspond exactement aux décisions validées.
- Effectuer une relecture indépendante ciblée du registre.

## 5. Livrables

- Fiche MEC-0004 intégrée au registre.
- Ajustement de l'en-tête du registre pour mentionner quatre fiches.
- Rapport d'inscription et de conformité dans `docs/reviews/`.
- Archivage du mandat selon les conventions du dépôt.

## 6. Autorisations et arrêt

L'exécution de ce mandat nécessite une autorisation distincte.

Aucun commit, push ou ouverture de PR sans autorisation explicite du propriétaire.

Aucune fusion sans autorisation supplémentaire.

Arrêter le travail après l'inscription et sa vérification. Ne pas commencer l'implémentation du lot 1G.
