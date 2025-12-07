# Définition des recettes sous forme de dictionnaires
# Chaque dictionnaire représente les ingrédients nécessaires pour un type de produit

# Recette pour les baguettes
bagguettes = {
    "farine": 250,  # grammes par baguette
    "levure": 8,    # grammes par baguette
    "sel": 5        # grammes par baguette
}

# Recette pour les pains au chocolat
pains = {
    "farine": 180,      # grammes par pain
    "beurre": 40,       # grammes par pain
    "chocolat": 15,     # grammes par pain
    "sucre": 10         # grammes par pain
}

# Recette pour les croissants
croissant = {
    "farine": 200,  # grammes par croissant
    "beurre": 50,   # grammes par croissant
    "sucre": 5      # grammes par croissant
}

# Liste qui contiendra toutes les recettes
recette = []

# Ajout des recettes à la liste dans un ordre spécifique :
# Index 0 : baguettes
# Index 1 : pains au chocolat
# Index 2 : croissants
recette.append(bagguettes)    # recette[0]
recette.append(pains)         # recette[1]
recette.append(croissant)     # recette[2]

# -------------------------------------------------------------------
# SECTION : SAISIE DES QUANTITÉS DE PRODUITS À FABRIQUER
# -------------------------------------------------------------------

# Demande à l'utilisateur le nombre de chaque produit à fabriquer
# et stocke les valeurs dans des variables

baguettes_user = try_user("Combien de Bagette allez vous preparer ? : ")
pains_user = try_user("Combien de Pains au chocolat allez vous preparer ? : ")
croissant_user = try_user("Combien de Croissant allez vous preparer ? : ")

# -------------------------------------------------------------------
# SECTION : CALCUL DES MATIÈRES PREMIÈRES NÉCESSAIRES
# -------------------------------------------------------------------

# Calcul de la farine totale nécessaire :
# (farine par baguette × nombre de baguettes) + 
# (farine par pain × nombre de pains) + 
# (farine par croissant × nombre de croissants)
farine = (recette[0]["farine"] * baguettes_user) + \
         (recette[1]["farine"] * pains_user) + \
         (recette[2]["farine"] * croissant_user)

# Calcul de la levure totale (seulement pour les baguettes)
levure = (recette[0]["levure"] * baguettes_user)

# Calcul du sel total (seulement pour les baguettes)
sel = (recette[0]["sel"] * baguettes_user)

# Calcul du beurre total :
# (beurre par pain × nombre de pains) + 
# (beurre par croissant × nombre de croissants)
beurre = (recette[1]["beurre"] * pains_user) + \
         (recette[2]["beurre"] * croissant_user)

# Calcul du chocolat total (seulement pour les pains au chocolat)
chocolat = (recette[1]["chocolat"] * pains_user)

# Calcul du sucre total :
# (sucre par pain × nombre de pains) + 
# (sucre par croissant × nombre de croissants)
sucre = (recette[1]["sucre"] * pains_user) + \
        (recette[2]["sucre"] * croissant_user)

# -------------------------------------------------------------------
# SECTION : AFFICHAGE DES RÉSULTATS
# -------------------------------------------------------------------

print(f"""
Nombre de matiere premier requit :
      Farine => {farine} g
      Levure => {levure} g
      Sel => {sel} g
      Beurre => {beurre} g
      Chocolat => {chocolat} g
      Sucre => {sucre} g
""")
