def inserer_racine(racine, cle):
    if racine is None:
        return {"cle": cle, "gauche": None, "droit": None}
    else:
        if cle < racine["cle"]:
            racine["gauche"] = inserer_racine(racine["gauche"], cle)
        else:
            racine["droit"] = inserer_racine(racine["droit"], cle)
    return racine