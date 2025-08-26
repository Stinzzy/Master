while True:
    tuumat = float(input("syötä tuumien määrä: "))
    if tuumat < 0:
        print("Annoit negatiivisen määrän tuumia, ohjelma sammuu.")
        break
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} Tuumaa on {senttimetrit:.2f} senttimetriä.")