import mysql.connector
from geopy.distance import geodesic

def kordinaatit(kursori, icao):
    sql = """
    SELECT latitude_deg, longitude_deg
    From airport
    Where ident = %s
    """
    kursori.execute(sql, (icao,))
    x = kursori.fetchone()
    if x:
        lat, lon = x
        return (lat, lon)
    return None

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='-----',
    password='------',
    autocommit=True
    )
kursori = yhteys.cursor()

icao1 = input("anna 1. lontekentän ICAO-koodi: ").upper()
icao2 = input("anna 2. lentokentän ICAO-koodi: ").upper()

p1 = kordinaatit(kursori, icao1)
p2 = kordinaatit(kursori, icao2)

if p1 and p2:
    km = geodesic(p1, p2).kilometers
    print(f"etäisyys {icao1} ja {icao2} välillä on {km:.2f}km")

if not p1:
    print(f"lentokenttä '{icao1}' ei ole olemassa ")

if not p2:
    print(f"lentokenttä {icao2} ei ole olemassa ")
kursori.close()
yhteys.close()