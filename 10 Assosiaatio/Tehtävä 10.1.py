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


h = hissi(1, 10)
h.siirtyminen(8)
h.siirtyminen(1)