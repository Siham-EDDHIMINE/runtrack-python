L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
result = 1
for value in L:
    if 25 <= value <= 90:
        result *= value
print(f"Le produit des valeurs de la liste comprises dans l'intervalle [25, 90] est {result}")
