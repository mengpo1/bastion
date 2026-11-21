"""Vérifie les renvois au code d'OXCE de la nouvelle phrase du §5 (AR-01).
Lecture seule : uniquement `git show HEAD:<fichier>` dans le clone.
Usage : python3 -I citations_oxce.py <clone OXCE>
Code de sortie 0 si tous les contrôles réussissent, 1 sinon."""
import sys, subprocess
C = sys.argv[1]
def git(*a): return subprocess.run(["git", "-C", C, *a], capture_output=True, text=True, check=True).stdout
ok = True
def t(nom, cond):
    global ok
    ok &= bool(cond)
    print(("OK    " if cond else "ECHEC ") + nom)
t("commit du clone = 441cae1b071d249d40a223858cb6bd07fd5d791b", git("rev-parse", "HEAD").strip() == "441cae1b071d249d40a223858cb6bd07fd5d791b")
F = {f: git("show", "HEAD:" + f).splitlines() for f in ("src/Savegame/BattleUnit.cpp", "src/Mod/Armor.cpp", "src/Mod/RuleStatBonus.cpp", "src/Mod/RuleStatBonus.h", "src/Mod/RuleSoldierBonus.cpp")}
def L(f, a, b=None): return F[f][a - 1:(b or a)]
BU, AR, RS = "src/Savegame/BattleUnit.cpp", "src/Mod/Armor.cpp", "src/Mod/RuleStatBonus.cpp"

pe = L(BU, 2733, 2742)
t("BU:2733 ouvre prepareEnergy", pe[0].strip() == "[code OXCE retiré — D4]")
t("BU:2742 ferme prepareEnergy", pe[-1] == "}" and L(BU, 2743)[0].strip() == "")
t("BU:2738 seule soustraction : blessures mortelles au torse", [l.strip() for l in pe if "-=" in l] == ["[code OXCE retiré — D4]"])
t("BU:2733-2742 sans terme de poids ni de charge", not any(k in "".join(pe) for k in ("Weight", "weight", "encumbrance")))
t("BU:2946 appelle [code OXCE retiré — D4]", L(BU, 2946)[0].strip() == "[code OXCE retiré — D4]")
sb = L(BU, 2902, 2909)
t("BU:2902-2909 additionne les bonus du soldat dans ENRecovery", sb[0].strip() == "[code OXCE retiré — D4]" and "[code OXCE retiré — D4]" in [l.strip() for l in sb])
t("BU:2910 ne contient que l'accolade fermante du if", L(BU, 2910)[0].strip() == "}")
t("BU:2717 : getCarriedWeight dans prepareTimeUnits (BU:2709-2727)", "getCarriedWeight()" in L(BU, 2717)[0] and L(BU, 2709)[0].strip() == "[code OXCE retiré — D4]")
uu = L(BU, 2894, 2948)
t("BU:2894-2948 (updateUnitStats) sans getCarriedWeight", uu[0].strip().startswith("[code OXCE retiré — D4]") and not any("getCarriedWeight" in l for l in uu))
occ = [i + 1 for i, l in enumerate(F[BU]) if "getCarriedWeight" in l]
t("BattleUnit.cpp : getCarriedWeight seulement l.2717, 3110 (addItem) et 4852 (définition) : %s" % occ, occ == [2717, 3110, 4852])

t("Armor.cpp:60 : [code OXCE retiré — D4]", L(AR, 60)[0].strip() == "[code OXCE retiré — D4]")
t("Armor.cpp:234 : chargement depuis la clé recovery, avec analyseur de script", L(AR, 234)[0].strip() == '[code OXCE retiré — D4]')
ge = [i + 1 for i, l in enumerate(F[AR]) if "[code OXCE retiré — D4]" in l]
t("Armor.cpp:789-791 : getEnergyRecovery = [code OXCE retiré — D4] (non cité)", ge == [789] and L(AR, 791)[0].strip() == "[code OXCE retiré — D4]")

t("RuleStatBonus.cpp:537-544 : setEnergyRecovery = energyRegen x 1.0", L(RS, 537)[0].strip() == "[code OXCE retiré — D4]" and '[code OXCE retiré — D4]' in [l.strip() for l in L(RS, 537, 544)] and L(RS, 544)[0] == "}")
t("RuleStatBonus.cpp:292 : energyRegen -> basicEnergyRegeneration", L(RS, 292)[0].strip() == '[code OXCE retiré — D4]')
br = [l.strip() for l in L(RS, 144, 155)]
t("RuleStatBonus.cpp:144-155 : TU initiales / 3 pour un soldat, sinon récupération de la règle de l'unité",
  br[0] == "[code OXCE retiré — D4]" and "[code OXCE retiré — D4]" in br and "[code OXCE retiré — D4]" in br and L(RS, 155)[0] == "}")
t("RuleStatBonus.cpp:144-155 sans terme de poids", not any("eight" in l for l in br))
t("RuleStatBonus.cpp:579 : la sortie part de externalBonuses (non cité)", L(RS, 579)[0].strip() == "[code OXCE retiré — D4]")
t("RuleStatBonus.cpp:382 : le script par défaut part de « bonus » (non cité)", L(RS, 382)[0].strip() == '[code OXCE retiré — D4]')
t("RuleStatBonus.cpp:363-366 : une chaîne sous la clé est chargée comme script (non cité)", "[code OXCE retiré — D4]" in L(RS, 363)[0] and "loadContainer" in L(RS, 365)[0])
noms = [l.split('"')[1] for l in L(RS, 235, 293) if l.strip().startswith('{ "')]
t("liste des termes de bonus (%d) sans terme de poids ni de charge" % len(noms), noms and not any(k in n.lower() for n in noms for k in ("weight", "carr", "encumb")))
t("RuleStatBonus.h : [code OXCE retiré — D4] et _bonusOrig vide par défaut", "[code OXCE retiré — D4]" in [l.strip() for l in F["src/Mod/RuleStatBonus.h"]])
t("RuleSoldierBonus.cpp:57-60 : récupération d'énergie du bonus de soldat chargée depuis sa propre clé recovery (non cité)",
  L("src/Mod/RuleSoldierBonus.cpp", 57)[0].strip() == '[code OXCE retiré — D4]' and "[code OXCE retiré — D4]" in L("src/Mod/RuleSoldierBonus.cpp", 60)[0])
print("TOUS_OK", ok)
sys.exit(0 if ok else 1)
