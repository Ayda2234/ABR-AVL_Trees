# Les arbres binaires de recherche

import random
import time
import matplotlib as plt

"""
Dans un ABR 
  
  * chaque noeud possede un cle 
  * Chaque nœud du sous-arbre gauche possède une clé inférieure ou égale à celle du nœud considéré 
  * Les elements dun arbre sont stocke dans des dictionnaires tell que chaque "Noeud" est represente dans la facon suivante : 
      { cle : "12", gauche : "NONE", droite : "NONE"}

"""
# Remplir l'ABR aleatoirement 
def inserer_racine(racine, cle):
    if racine is None:
        return {"cle": cle, "gauche": None, "droit": None}
    else:
        if cle < racine["cle"]:
            racine["gauche"] = inserer_racine(racine["gauche"], cle)
        else:
            racine["droit"] = inserer_racine(racine["droit"], cle)
    return racine

def remplir_arbre_aleatoirement(taille, interval):
    valeurs = random.sample(range(1, interval + 1), taille)
    racine = None

    for val in valeurs:
        racine = inserer_racine(racine, val)

    return racine

"""
# definir une fonction qui recherche un element dans l'ABR 

"""

#ABR 

def ABR(racine, x):
    if racine is None:
        return None
    elif racine["val"] > x:
        return ABR(racine["gauche"], x)
    elif racine["val"] < x:
        return ABR(racine["droit"], x)
    else:
        return racine
    
#remplissage de AVL aleatoirement 

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

def remplir_avl_aleatoirement(taille, plage):
    valeurs = random.sample(range(1, plage + 1), taille)
    racine = None

    for valeur in valeurs:
        racine = inserer_avl(racine, valeur)

    return racine


"""
# definir une fonction qui recherche un element dans l'AVL

"""

#AVL 

def AVL(racine, x):
    if not racine:
        return None
    if x == racine[0]:
        return racine
    elif x < racine[0]:
        return AVL(racine[1], x)
    else:
        return AVL(racine[2], x)

# Exemple d'utilisation
x = 42
taille_arbre = 100
interval_vals = 100
ABR = remplir_arbre_aleatoirement(taille_arbre, interval_vals)
AVL = remplir_avl_aleatoirement(taille_arbre, interval_vals)

# L'affichage de l'ABR et L'AVL
print("L'ABR generer est  :\n", ABR)
print("====================================================\n====================================================")
print("L'AVL generer est  :\n", AVL)
print("====================================================\n====================================================")

# recherche si x est dans l'ABR
if ABR:
    print(f"L'élément {x} a été trouvé dans l'arbre ABR.")
else:
    print(f"L'élément {x} n'a pas été trouvé dans l'arbre ABR.")

# recheche si x est dans l'AVL
print("====================================================\n====================================================")

if AVL:
    print(f"L'élément {x} a été trouvé dans l'arbre AVL.")
else:
    print(f"L'élément {x} n'a pas été trouvé dans l'arbre AVL.")


################################

# Fonction de recherche pour ABR
