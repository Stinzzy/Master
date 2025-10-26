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

auto = Auto("ABC-123",142)
print(f"auton rekkari on {auto.rekkari}")
print(f"auton huippunopeus on {auto.huippunopeus}")
print(f"auton tämänhetkinen nopeus on {auto.nopeus}")
print(f"autolla ajettu matka on {auto.matka}")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"kiihdytettiin kolme kertaa ja tämän hetkinen nopeus on {auto.nopeus} km/h")

auto.kiihdytä(-200)

print(f"hätäjarrutuksen jälkeen nopeus on {auto.nopeus} km/h")