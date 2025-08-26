aineet = []
aine = input("Anna nimi tai lopeta painamalla Enter: ")
while aine != "":
    aineet.append(aine)
    aine = input("Anna uusi nimi tai lopeta painamalla Enter:")

for aine in aineet:
    print(f"Moi, {aine}!")

nimet = []
