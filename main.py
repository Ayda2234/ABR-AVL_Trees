# Les arbres binaires de recherche


import random
import timeit
import matplotlib.pyplot as plt

"""
Dans un ABR 
  
  * chaque noeud possede un cle 
  * Chaque nœud du sous-arbre gauche possède une clé inférieure ou égale à celle du nœud considéré 
  * Les elements dun arbre sont stocke dans des dictionnaires tell que chaque "Noeud" est represente dans la facon suivante : 
      { cle : "12", gauche : "NONE", droite : "NONE"}

""" 

# Fonction pour remplir un arbre avec une taille donnée aleatoirement
def remplir_arbre(taille, interval_vals, remplissage_func):
    # Assurez-vous que interval_vals est suffisamment grand pour éviter une erreur
    if interval_vals < taille:
        raise ValueError("La taille de l'échantillon doit être inférieure ou égale à interval_vals.")
    
    valeurs = random.sample(range(1, interval_vals + 1), taille)
    racine = None

    for val in valeurs:
        racine = remplissage_func(racine, val)
    return racine

"""
Racine : represente le noeud actuel 
cle : la valeur associer a ce noeud 

"""

# Remplir l'ABR 
def inserer_racine(racine, cle): 
    if racine is None:
        return {"cle": cle, "gauche": None, "droit": None}
    else:
        if cle < racine["cle"]:
            racine["gauche"] = inserer_racine(racine["gauche"], cle)
        else:
            racine["droit"] = inserer_racine(racine["droit"], cle)
    return racine

# Remplissage de AVL 
def hauteur(noeud):
    if not noeud:
        return 0 # hauteur = 0 
    return noeud[3]  # chaque noeud est represente de cette facon : [vlaeur , sous arbre gauche , sous arbre droite , hauteur]

"""
rééquilibrer l'arbre lorsque le sous-arbre gauche de y est devenu trop grand par rapport à son sous-arbre droit.
 La fonction renvoie le nouveau nœud qui devient la racine du sous-arbre rééquilibré.

"""

def rotation_droite(y):
    x = y[1]
    T2 = x[2]

    x[2] = y
    y[1] = T2

    y[3] = max(hauteur(y[1]), hauteur(y[2])) + 1
    x[3] = max(hauteur(x[1]), hauteur(x[2])) + 1

    return x
"""
rééquilibrer l'arbre lorsque le sous-arbre gauche de y est devenu trop petit par rapport à son sous-arbre droit.
 La fonction renvoie le nouveau nœud qui devient la racine du sous-arbre rééquilibré.

"""
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

# Fonction de recherche pour ABR
def recherche_abr(racine, x):
    if racine is None:
        return None
    elif racine["cle"] > x:
        return recherche_abr(racine["gauche"], x)
    elif racine["cle"] < x:
        return recherche_abr(racine["droit"], x)
    else:
        return racine

# Fonction de recherche pour AVL
def recherche_avl(racine, x):
    if not racine:
        return None
    if x == racine[0]:
        return racine
    elif x < racine[0]:
        return recherche_avl(racine[1], x)
    else:
        return recherche_avl(racine[2], x)

# Exemple d'utilisation
x = 42
tailles_arbres = [10, 100, 1000]
interval_vals = max(tailles_arbres)

temps_execution_abr_liste = []
temps_execution_avl_liste = []

for taille in tailles_arbres:
    ABR = remplir_arbre(taille, interval_vals, inserer_racine)
    AVL = remplir_arbre(taille, interval_vals, inserer_avl)

    debut_abr = timeit.default_timer()
    recherche_abr(ABR, x)
    fin_abr = timeit.default_timer()
    temps_execution_abr = fin_abr - debut_abr
    temps_execution_abr_liste.append(temps_execution_abr)

    debut_avl = timeit.default_timer()
    recherche_avl(AVL, x)
    fin_avl = timeit.default_timer()
    temps_execution_avl = fin_avl - debut_avl
    temps_execution_avl_liste.append(temps_execution_avl)

        # Ajustez interval_vals pour chaque taille d'arbre spécifique
    interval_vals = max(taille, interval_vals)
    ABR = remplir_arbre(taille, interval_vals, inserer_racine)
    AVL = remplir_arbre(taille, interval_vals, inserer_avl)

    # L'affichage de l'ABR et de l'AVL
    print(f"Taille de l'arbre : {taille}")
    print("L'ABR généré est :\n", ABR)
    print("====================================================\n====================================================")
    print("L'AVL généré est :\n", AVL)
    print("====================================================\n====================================================")

    # L'affichage de l'ABR et de l'AVL
    print(f"Taille de l'arbre : {taille}")
    print("L'ABR généré est :\n", ABR)
    print("====================================================\n====================================================")
    print("L'AVL généré est :\n", AVL)
    print("====================================================\n====================================================")

    ABR = remplir_arbre(taille, interval_vals, inserer_racine)
    AVL = remplir_arbre(taille, interval_vals, inserer_avl)

    resultat_abr = recherche_abr(ABR, x)
    resultat_avl = recherche_avl(AVL, x)

    # Affichage des résultats
    print(f"\nTaille de l'arbre : {taille}")
    print(f"Temps d'exécution pour ABR :{temps_execution_abr:.6f} secondes")
    if resultat_abr:
        print(f"L'élément {x} a été trouvé dans l'arbre ABR.")
    else:
        print(f"L'élément {x} n'a pas été trouvé dans l'arbre ABR ")

    print(f"Temps d'exécution pour AVL :{temps_execution_avl:.6f} secondes")
    if resultat_avl:
        print(f"L'élément {x} a été trouvé dans l'arbre AVL avec un temps d'execution : {temps_execution_avl:.6f}")
    else:
        print(f"L'élément {x} n'a pas été trouvé dans l'arbre AVL.")

# Affichage des résultats
plt.plot(tailles_arbres, temps_execution_abr_liste, marker='o', linestyle='-', color='b', label='ABR')
plt.plot(tailles_arbres, temps_execution_avl_liste, marker='o', linestyle='-', color='r', label='AVL')

plt.title('Temps d\'exécution pour ABR et AVL')
plt.xlabel('Taille de l\'arbre')
plt.ylabel('Temps d\'exécution (secondes)')
plt.legend()

plt.show()

