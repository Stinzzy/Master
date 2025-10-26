class julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi

class kirja(julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumäärä: int):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta(self):
        print(f"Kirjasi: {self.nimi}")
        print(f"kirjoittaja: {self.kirjoittaja}")
        print(f"sivumäärä {self.sivumäärä}")

class lehti(julkaisu):
    def __init__(self, nimi: str, toimittaja: str):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta(self):
        print(f"Lehti: {self.nimi}")
        print(f"toimittaja: {self.toimittaja}")

if __name__ == "__main__":
    aku_ankka = lehti("Aku Ankka", "Aki Hyyppä")
    hytti6 = kirja("Hytti N. 6", "Rosa Liksom", 200)

    aku_ankka.tulosta()
    print()
    hytti6.tulosta()