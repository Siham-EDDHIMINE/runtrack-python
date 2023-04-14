def arrondir_et_trier(liste):
    liste_arrondie = [round(x) for x in liste]
    liste_arrondie.sort()
    return liste_arrondie

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = arrondir_et_trier(ma_liste)
print(resultat) # affiche [4, 5, 9, 11, 12, 14, 16, 17, 22]