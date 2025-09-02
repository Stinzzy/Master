talvi = (12,1,2)
kevät = (3,4,5)
kesä = (6,7,8)
syksy = (9,10,11)

x = int(input("anna kuukauden numero: "))
if x in talvi:
    print("vuoden aika on talvi")
elif x in kevät:
    print("vuoden aika on kevät")
elif x in kesä:
    print("vuodenaika on kesä")
elif x in syksy:
    print("vuodenaika on syksy")
else:
    print("virheellinen kuukausi")