def echanger_premiere_derniere(L):
    # Vérification que la liste n'est pas vide
    if len(L) > 0:
        # Échange des valeurs de la première et de la dernière case
        L[0], L[-1] = L[-1], L[0]
    return L

# Exemple d'utilisation de la fonction
ma_liste = [1, 2, 3, 4]
nouvelle_liste = echanger_premiere_derniere(ma_liste)
print(nouvelle_liste) # Affiche [4, 2, 3, 1]