def gl_l(gallona):
    return gallona * 3.785

while True:
    gallona = float(input("(negatiivisen arvon antaminen sammuttaa ohjelman)\n anna bensan määrä gallonina: "))
    if gallona < 0:
        print("ohjelma sammuu")
        break
    litrat = gl_l(gallona)
    print(f"{gallona} galloonaa on {litrat:.2f} litraa")