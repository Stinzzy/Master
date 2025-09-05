import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='tozzy',
    password='Marianhomeboy23',
    autocommit=True
    )
kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi: ").upper()

sql ="""
SELECT  type, COUNT(*)
FROM airport
WHERE iso_country =%s
Group by type
"""

kursori.execute(sql, (maakoodi,))

tulos = kursori.fetchall()

if tulos:
    print(f"lentokenttia lukumäärä maassa {maakoodi}")
    for tyyppi, määrä in tulos:
        print(f"{tyyppi}: {määrä} kpl")
else:
    print (f"maakoodilla {maakoodi} ei löytynyt lentokenttiä")
kursori.close()
yhteys.close()
