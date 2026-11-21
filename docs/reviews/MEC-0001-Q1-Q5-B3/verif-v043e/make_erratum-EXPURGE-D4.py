import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
def rep(old, new):
    global t
    n = t.count(old)
    if n != 1: sys.exit("ECHEC: %d occurrence(s) de: %r" % (n, old[:100]))
    t = t.replace(old, new)

# Métadonnées strictement nécessaires
rep("# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.3\n",
    "# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4.3 (erratum AR-01/AR-02)\n")
rep("sans modifier les décisions. Non revu, non inscrit.\n",
    "sans modifier les décisions. Non revu, non inscrit.\n"
    "**Erratum AR-01/AR-02** (mandat d'erratum du propriétaire, JS-40, 2026-11-20T17:09:00Z) : seules deux corrections sont faites, au §5 (comparaison avec OXCE, AR-01) et dans l'introduction du §17 (nature des contrôles, AR-02). Le reste du texte est celui de la v0.4.3 initiale (SHA-256 `cd1c808b10dbcf39f96e557f9d6ef994b232bdcacc44e696122edd4dbee76602`), conservée intacte. Pour limiter l'erratum à ces deux corrections, le mandat d'erratum et le rapport de contrôle indépendant de la v0.4.3 initiale (SHA-256 `427e0736235ad1eb5340cfb028eb19c24c315b030399e899fb41421a5ca902c2`) ne sont pas ajoutés au §15, et la phrase finale n'est pas actualisée.\n")

# AR-01 : §5, point d'articulation (OB-06)
rep("Or OXCE ne réduit pas la récupération d'énergie selon la charge : `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`, commit `441cae1b`) ne tient compte que des blessures mortelles au torse.",
    "Côté OXCE, le code lu au commit `441cae1b`, sans exécution, montre ceci. La fonction `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`) ne retranche du gain d'énergie qu'elle reçoit que l'effet des blessures mortelles au torse ; elle ne fait pas intervenir la charge. Ce gain est calculé ailleurs, par l'armure ([code OXCE retiré — D4], l.2946), qui y ajoute les bonus du soldat (l.2902-2909). Il est paramétrable par la clé `recovery` de l'armure, éventuellement par script (`src/Mod/Armor.cpp:234`). Sans ce paramétrage, il vaut le bonus `energyRegen` (`Armor.cpp:60` ; `src/Mod/RuleStatBonus.cpp:537-544`) : le tiers des TU initiales d'un soldat, ou la récupération d'énergie fixée par la règle de l'unité (`RuleStatBonus.cpp:292` et `144-155`), sans terme de charge. Dans la récupération, la charge (`getCarriedWeight`) n'intervient qu'au calcul des TU (l.2717). Les paramétrages possibles de la clé `recovery` n'ont pas été étudiés : le constat ne vaut que pour la configuration par défaut.")

# AR-02 : introduction du §17
rep("Cette vérification est de Claude Code. Elle **n'est pas une revue indépendante**. Chaque contrôle a été exécuté avec `python3 -I` ou une commande du shell, avec le code de sortie 0. Les scripts sont inventoriés au §15 (S-1 à S-13).",
    """Cette vérification est de Claude Code. Elle **n'est pas une revue indépendante**. Elle comprend deux sortes de contrôles :
- **contrôles automatisés**, exécutés par un script (`python3 -I`) ou une commande du shell, dont le code de sortie est connu et vaut 0 : contrôles 1, 2, 5, 7, 8, 10, 12 et 13. Pour le contrôle 7, l'interprétation de la sortie relative à JS-22 est une lecture ;
- **vérifications documentaires par relecture** : contrôles 3, 4 et 6 entièrement ; contrôles 9 et 11 en partie. Pour le 9, la relecture du §3.5 et du §13 complète S-8. Pour le 11, le diff (O-8) et la comparaison des sections sont automatisés, mais leur rapprochement avec le §21 est une relecture. Une relecture n'a pas de code de sortie : sa conclusion repose sur l'examen décrit dans la colonne « Méthode ».

Les scripts sont inventoriés au §15 (S-1 à S-13).""")

open(dst, "w", encoding="utf-8").write(t)
print("OK")
