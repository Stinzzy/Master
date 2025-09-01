import random

def nopan_heitto():
    return random.randint(1,6)

silmaluku = 0
while silmaluku !=6:
    silmaluku = nopan_heitto()
    print("tulos: ", silmaluku)
