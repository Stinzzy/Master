import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='ankkalinna',
    user='tozzy',
    password='Marianhomeboy23',
    autocommit=True
    )


sql = "SELECT * FROM ankkalinnalainen"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print("kaikki tiedot:")
for rivi in tulos:
    print(", ".join(str(sarake)for sarake in rivi))