BASTION — Autorisation d'avenant n° 1 à MEC-0003 / T13

Je valide la correction proposée pour T13.

J'autorise exclusivement les deux modifications suivantes :

1. Registre "docs/gameplay/GAMEPLAY-DECISIONS.md"

Dans le résultat attendu de T13, remplacer uniquement la dernière phrase :

« La case (2,2) n'est pas non plus dans la zone atteignable »

par :

« La case (2,2) reste toutefois dans la zone atteignable : le chemin retenu est [NE, NW], pour 12 TU et 6 d'énergie ; l'unité y arrive orientée NW, et son emprise ne chevauche alors pas la case (3,1). »

Toutes les autres phrases de T13, notamment le refus du deuxième pas N et la conservation de l'état après ce refus, doivent rester inchangées.

2. Test C# correspondant

Remplacer exclusivement l'assertion erronée sur l'absence de (2,2) dans la zone atteignable par des assertions couvrant :

- la présence de (2,2) dans la zone ;
- le chemin [NE, NW] ;
- son coût de 12 TU et 6 d'énergie ;
- l'orientation finale NW.

Conserver les vérifications existantes sur le refus du deuxième pas N et l'absence de débit lors de ce refus.

Après correction :

1. Vérifier que le diff est strictement limité à ces deux modifications.
2. Relancer la compilation, les tests, le formatage et le harnais.
3. Faire contrôler l'ensemble du lot par un relecteur indépendant, avec une attention particulière à la géométrie, aux rotations, aux volumes balayés et à la conformité aux règles inscrites.
4. Préparer le rapport d'exécution et la revue.

Restrictions :

- Aucune modification supplémentaire du moteur C#.
- Aucune modification des autres tests ou règles.
- Aucun changement de MEC-0001 ou MEC-0002.
- Aucun changement du harnais.
- Aucun ajout à "docs/mandates/README.md" dans cet avenant.
- Aucun commit, push ou PR sans autorisation de publication distincte.

Cette autorisation ne porte que sur l'avenant n° 1 à T13.

À l'issue des vérifications, présente le bilan et le diff avant toute publication.
