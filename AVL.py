def hauteur(noeud):
    if not noeud:
        return 0
    return noeud[3]

def rotation_droite(y):
    x = y[1]
    T2 = x[2]

    x[2] = y
    y[1] = T2

    y[3] = max(hauteur(y[1]), hauteur(y[2])) + 1
    x[3] = max(hauteur(x[1]), hauteur(x[2])) + 1

    return x

def rotation_gauche(x):
    y = x[2]
    T2 = y[1]

    y[1] = x
    x[2] = T2

    x[3] = max(hauteur(x[1]), hauteur(x[2])) + 1
    y[3] = max(hauteur(y[1]), hauteur(y[2])) + 1

    return y

def difference_hauteur(noeud):
    if not noeud:
        return 0
    return hauteur(noeud[1]) - hauteur(noeud[2])

def inserer_avl(racine, cle):
    if not racine:
        return [cle, None, None, 1]
    
    if cle < racine[0]:
        racine[1] = inserer_avl(racine[1], cle)
    elif cle > racine[0]:
        racine[2] = inserer_avl(racine[2], cle)
    else:
        return racine  # Les clés égales ne sont pas autorisées dans un arbre de recherche binaire

    racine[3] = 1 + max(hauteur(racine[1]), hauteur(racine[2]))

    difference = difference_hauteur(racine)

    # Cas de rotation à gauche
    if difference > 1 and cle < racine[1][0]:
        return rotation_droite(racine)

    # Cas de rotation à droite
    if difference < -1 and cle > racine[2][0]:
        return rotation_gauche(racine)

    # Cas de rotation gauche-droite
    if difference > 1 and cle > racine[1][0]:
        racine[1] = rotation_gauche(racine[1])
        return rotation_droite(racine)

    # Cas de rotation droite-gauche
    if difference < -1 and cle < racine[2][0]:
        racine[2] = rotation_droite(racine[2])
        return rotation_gauche(racine)

    return racine