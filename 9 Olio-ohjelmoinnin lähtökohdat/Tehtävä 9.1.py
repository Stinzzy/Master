class auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = auto("ABC-123",142)
print(f"auton rekkari on {auto.rekkari}")
print(f"auton huippunopeus on {auto.huippunopeus}")
print(f"auton tämänhetkinen nopeus on {auto.nopeus}")
print(f"autolla ajettu matka on {auto.matka}")