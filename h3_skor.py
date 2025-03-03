import random


fb_gol = random.randint(0, 5)  
gs_gol = random.randint(0, 5)  


print(f"Fenerbahçe {fb_gol} - {gs_gol} Galatasaray")


if fb_gol > gs_gol:
    print("Kazanan: Fenerbahçe")
elif gs_gol > fb_gol:
    print("Kazanan: Galatasaray")
else:
    print("Maç berabere!")
