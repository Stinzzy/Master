import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='tozzy',
    password='Marianhomeboy23',
    autocommit=True
)
kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi: ").upper()

sql = """
SELECT country.name, airport.type, COUNT(*)
FROM airport
JOIN country ON airport.iso_country = country.iso_country
WHERE airport.iso_country = %s
GROUP BY airport.type, country.name
"""

kursori.execute(sql, (maakoodi,))
tulos = kursori.fetchall()

if tulos:
    maan_nimi = tulos[0][0]  # kaikissa riveissä sama maan nimi
    print(f"Lentokenttien lukumäärät maassa {maan_nimi} ({maakoodi}):")
    for _, tyyppi, määrä in tulos:
        print(f"{tyyppi}: {määrä} kpl")
else:
    print(f"Maakoodilla {maakoodi} ei löytynyt lentokenttiä.")

kursori.close()
yhteys.close()
