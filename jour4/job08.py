# Création de la liste L
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Calcul de la somme des valeurs paires de la liste L
somme_paires = 0
for element in L:
    if element % 2 == 0:
        somme_paires += element

# Affichage du résultat
print(somme_paires) # Affiche 182