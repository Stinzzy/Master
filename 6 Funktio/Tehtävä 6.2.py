import random

def nopan_heitto(tahkot):
    return random.randint(1,tahkot)

tahkot = int(input("Anna tahkojen määrä: "))

silmaluku = 0
while silmaluku != tahkot:
    silmaluku = nopan_heitto(tahkot)
    print("tulos: ", silmaluku)
