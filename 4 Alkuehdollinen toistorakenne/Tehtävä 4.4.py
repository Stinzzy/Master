import random

v_luku = random.randint(1,10)
while True:
    arvaus = int(input("arvaa minkä luvun valitsin (1-10): "))

    if arvaus < v_luku:
        print("liian pieni arvaus")
    elif arvaus > v_luku:
        print("liian suuri arvaus")
    else:
        print("arvaus oikein!")
        break