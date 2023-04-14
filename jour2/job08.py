def check_type_saison(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire,fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, andive")
    elif type == "légumes" and "été":
        print("artichaut, aubergine, navet")

    else:
         ("nul")
check_type_saison("fruits", "hiver")
check_type_saison("fruits", "été")
check_type_saison("légumes", "hiver")
check_type_saison("légumes", "été")