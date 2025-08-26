x = int(input("anna kokonaisluku: "))

if x < 1:
    print(f"{x} ei ole alkuluku")
else:
    x_alkuluku = True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            print(f"{x} ei ole alkuluku, koska sen voi jakaa luvulla {i}.")
            x_alkuluku = False
            break

    if x_alkuluku:
        print(f"{x} on alkuluku")
