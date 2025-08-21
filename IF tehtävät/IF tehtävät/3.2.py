hytti = (input("Onko teillä käytössä LUX, A, B vai C hytti? "))

hytti = hytti.upper()

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella. ")

elif hytti == "A":
    print("Hytti A on ikkunallinen hytti yläkannella.")
elif hytti == "B":
    print("Hytti B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("Hytti C on ikkunaton hytti autokannen alapuolella.")
else:
    print("virheellinen hyttiluokka")
