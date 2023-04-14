def mot_suivant(mot: str) -> str:
    mot = list(mot)
    i = len(mot) - 2
    while i >= 0 and mot[i] >= mot[i + 1]:
        i -= 1
    if i == -1:
        return "Pas de mot suivant possible"
    j = len(mot) - 1
    while mot[j] <= mot[i]:
        j -= 1
    mot[i], mot[j] = mot[j], mot[i]
    mot[i + 1:] = reversed(mot[i + 1:])
    return "".join(mot)

mot = input("Entrez un mot: ")
mot_suivant = mot_suivant(mot)
print(f"Le mot suivant est: {mot_suivant}")

