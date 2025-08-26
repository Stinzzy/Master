kaupungit = []

for x in range(5):
    kaupunki = input(f"Kerro ({x+1}) kaupungin nimi:")
    kaupungit.append(kaupunki)

print("\nKaupungit sinun antamassasi järjestyksessä:")
for kaupunki in kaupungit:
    print(kaupunki)
