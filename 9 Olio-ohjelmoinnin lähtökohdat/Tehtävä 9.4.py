import random

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self,kmh):
        self.nopeus += kmh
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self,tunnit):
        self.matka += self.nopeus * tunnit

autot = []
for x in range(1,11):
    huippu = random.randint(100,200)
    autot.append(Auto(f"ABC-{x}", huippu))

tunnit = 0
finish = 10_000

while True:
    tunnit += 1
    for auto in autot:
        muutos = random.randint(-10,15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    if any(a.matka >= finish for a in autot):
        break


print(f"\nkilpailu kesti {tunnit} tuntia.\n")
print("Rekisteri    Huippuopeus    Nopeus       Matka")
print("_"*50)

for a in autot:
    print(f"{a.rekkari}         {a.huippunopeus} km/h      {a.nopeus} km/h     {a.matka} km")
