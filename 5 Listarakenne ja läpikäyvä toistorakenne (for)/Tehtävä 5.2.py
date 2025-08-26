luku = []

vastaus = input("Anna luku: \n(Tai jos haluat päättää niin jätä kenttä tyhjäksi) ")

while vastaus != "":
    luku.append(int(vastaus))
    vastaus = input("anna toinen luku: ")

luku.sort(reverse=True)

viis_suurinta = luku[:5]

print("suurimmat luvut ovat:", viis_suurinta)
