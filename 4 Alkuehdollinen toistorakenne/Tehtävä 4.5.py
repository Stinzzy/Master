o_tunnus = "python"
o_salis = "rules"

yritykset = 0
max = 5

while yritykset < max:
    tunnus = input("käyttäjätunnus: ")
    salis = input("salasana: ")

    if tunnus == o_tunnus and salis == o_salis:
        print("Tervetuloa")
        break
    else:
        print("tarkista käyttäjätunnus / salasana")
        yritykset += 1

if yritykset == max:
    print("Pääsy evätty")