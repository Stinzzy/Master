kuhan_pituus = int(input("Mikä on kuhan pituus?  "))

alimitta = 37

if kuhan_pituus < alimitta:
    puuttuu = alimitta - kuhan_pituus
    print ("kuha on alimittainen. Laske kuha takaisin järveen")
    print(f"Kuhan pituudesta puuttuu {puuttuu} cm")

else:
    print("kuhan voi ottaa messiin!")