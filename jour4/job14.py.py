def my_long_word(n, chaine):
    mots = chaine.split()
    mots_long = []
    for mot in mots:
        if len(mot) > n:
            mots_long.append(mot)
    return " ".join(mots_long)

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")
print(resultat) # affiche "peur chemin vers côté obscur peur mène colère colère mène haine haine mène souffrance"