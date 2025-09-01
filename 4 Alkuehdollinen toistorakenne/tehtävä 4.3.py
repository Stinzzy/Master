luvut =[]
while True:
    numero = input("anna jokin numero: ")
    if numero == "":
        if luvut:
            print("suurin: ", max(luvut))
            print("pienin: ", min(luvut))
            break
    x = float(numero)
    luvut.append(x)
