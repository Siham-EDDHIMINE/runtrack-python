def tri_croissant(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    return liste
ma_liste = [3, 1, 4, 2]
ma_liste_triee = tri_croissant(ma_liste)
print(ma_liste_triee) # affiche [1, 2, 3, 4]