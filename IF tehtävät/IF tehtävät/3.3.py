sukupuoli = input("Sukupuoli: ")
hemo = int(input("Hemoglobiinin määrä (g/): "))

if sukupuoli == "nainen":
    if hemo < 117:
        print(" Hemoglobiiniarvo on alhainen")
    elif hemo <= 175:
        print(" Hemoglobiiniarvo on normaali")
    else:
        print(" Hemoglobiiniarvo on korkea")
elif sukupuoli == "mies":
    if hemo < 134:
        print(" Hemoglobiiniarvo on alhainen")
    elif hemo <= 195:
        print(" Hemoglobiiniarvo on normaali")
    else:
        print(" Hemoglobiiniarvo on korkea")