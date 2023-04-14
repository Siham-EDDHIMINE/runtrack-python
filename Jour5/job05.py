def distance_parcourue(nbre_marches: int, hauteur_marche: int) -> str:
    distance = nbre_marches * hauteur_marche * 2 * 5 * 7 / 100
    return f"Pour {nbre_marches} marches de {hauteur_marche} cm, le gardien parcours {distance:.2f} m par semaine."
# Définir les paramètres d'entrée
nbre_marches = 300
hauteur_marche = 20

# Appeler la fonction avec les paramètres définis
resultat = distance_parcourue(nbre_marches, hauteur_marche)

# Afficher le résultat
print(resultat)