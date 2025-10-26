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

class sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akku_kwh):
        super().__init__(rekkari, huippunopeus)
        self.akk_kwh = akku_kwh

class bensa_auto(Auto):
    def __init__(self, rekkari, huippunopeus, tankkiL):
        super().__init__(rekkari, huippunopeus)
        self.tankkiL = tankkiL

if __name__ == "__main__":
    s = sähköauto("ABC-15", 180, 52.5)
    b = bensa_auto("ACD-123", 165, 32.5)

    s.kiihdytä(34)
    b.kiihdytä(127)

    s.kulje(3)
    b.kulje(3)

    print(f"{s.rekkari} matka: {s.matka} km")
    print(f"{b.rekkari} matka: {b.matka} km")
