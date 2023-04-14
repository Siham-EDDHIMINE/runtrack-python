# Création de la liste L
L = [8, 24, 48, 2, 16]

# Comptage du nombre de multiples de 3 dans la liste L
nombre_multiples_3 = 0
for element in L:
    if element % 3 == 0:
        nombre_multiples_3 += 1

# Affichage du résultat
print(nombre_multiples_3) # Affiche 2