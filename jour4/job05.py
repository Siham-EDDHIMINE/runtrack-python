# Création de la liste L
L = [1, 2, 3, 4, 5]

# Affichage de la valeur de L[1]
print(L[1])

# Définition de la fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_L3():
    L[3] = L[2] + L[4]

# Appel de la fonction pour remplacer L[3]
remplacer_L3()

# Affichage de la valeur du dernier terme de la liste
print(L[-1])