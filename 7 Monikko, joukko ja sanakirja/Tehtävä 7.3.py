lentokentät = {}

while True:
    print("valitse toiminto")
    print("1. syötä uusi lentokenttä")
    print("2. hae jo mainitun lentokentän tietoja")
    print("3. sammuta ohjelma")
    valinta = input("valintasi: ")

    if valinta == "1":
        koodi= input("anna lentokentän ICAO-koodi: ").upper()
        nimi = input("anna lentokentän nimi: ")
        lentokentät[koodi] = nimi
        print("lentokentttä {nimi} lisätty.")

    elif valinta == "2":
        koodi = input("anna lentokentän ICAO-koodi: ").upper()
        if koodi in lentokentät:
            print(f"{koodi} = {lentokentät[koodi]}")
        else:
            print("lentokenttää ei löytynyt")

    elif valinta == "3":
        print("ohjelma sammuu")
        break
