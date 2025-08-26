import random

n = int(input("Anna jokin määrä arpakuutioita: "))

#kysyn käyttäjältä arpakuutioiden määrän

summa = 0

#aloitetaan lasku nollasta

for i in range(n):
    numero = random.randint(1, 6)
    summa += numero

#heitetään noppia (n) kertaa eli käyttäjän valitseman verran ja summataan luvut yhteen

print(f"Arpakuutioiden yhteenlaskettu summa: {summa}")
