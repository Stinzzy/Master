nimet = set()

print("syötä nimiä. (jätä kenttä tyhjäksi sammuttaaksesi ohjelma)")
while True:
    nimi = input("anna jokin nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("nimi on jo syötetty!")
    else:
        nimet.add(nimi)
        print("uusi nimi lisätty")

print("tässä antamasi nimet: ")
for nimi in nimet:
    print(nimi)