import math

def hinta(cm_halkaisia, hinta):
    säde = cm_halkaisia / 2
    pinta_ala = math.pi * säde * säde / 10000
    return hinta / pinta_ala

hl1 = float(input("Anna 1. pizzan halkaisija (cm): "))
hi1 = float(input("anna 1. pizzan hinta euroina: "))

hl2 = float(input("anna 2. pizzan halkaisija (cm): "))
hi2 = float(input("anna 2. pizzan hinta euroina: "))

hinta1 = hinta(hl1,hi1)
hinta2 = hinta(hl2,hi2)

print(f"1. pizzan yksikkohinta: {hinta1:.2f}€/m2")
print(f"2. pizzan yksikkohinta: {hinta2:.2f}€/m2")

if hinta1 < hinta2:
    print("1. pizza on halvempi")
else:
    print("2. pizza on halvempi")