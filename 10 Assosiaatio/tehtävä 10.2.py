class hissi:
    def __init__(self, alinkerros: int, ylinkerros: int):
        self.alin =alinkerros
        self.ylin = ylinkerros
        self.kerros = alinkerros

    def ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"hissi on {self.kerros} kerroksessa")
        else:
            print("Hissi on ylimmässä kerroksessa")

    def alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on {self.kerros} kerroksessa")
        else:
            print("Hissi on jo alimmassa kerroksessa")

    def siirtyminen(self, kohde: int):
        while self.kerros < kohde:
            self.ylös()
        while self.kerros > kohde:
            self.alas()

class talo:
    def __init__(self, alinkerros: int, ylinkerros: int, hissien_lukumäärä):
        self.alin = alinkerros
        self.ylin = ylinkerros
        self.hissit = [hissi(alinkerros, ylinkerros) for _ in range(hissien_lukumäärä)]

    def hissinajo(self, hissinumero: int, kerros: int):
        indeksi = hissinumero -1
        if indeksi < 0:
            print(f"hissinumero {hissinumero} ei ole käytettävissä")
            return
        print(f"ajetaan hissiä #{hissinumero} kerrokseen {kerros}:")
        self.hissit[indeksi].siirtyminen(kerros)


    def tilanne(self):
        print("hissien tilanne:")
        for i, h in enumerate(self.hissit, start = 1):
            print(f"hissi {i}: kerros {h.kerros}")


t = talo(1, 30, 3)
t.hissinajo(2, 8)
t.hissinajo(1, 3)
t.hissinajo(3, 30)
t.tilanne()
t.hissinajo(2, 4)
t.tilanne()