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

while True:
    icao = input("anna lentoaseman ICAO-koodi: ").upper()

    if icao == "":
        print("ohjelma sammuu")
        break

    sql = "SELECT name, municipality FROM airport WHERE ident =%s"
    kursori.execute(sql,(icao,))

    tulos = kursori.fetchone()
    if tulos:
        nimi, kunta = tulos
        print(f"lentoasema: {nimi}")
        print(f"kunta: {kunta}")
    else:
        print("lento asemaa ei löytynyt")

