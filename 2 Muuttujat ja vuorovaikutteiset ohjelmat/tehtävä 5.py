
leiviskä = int (input("leivisköjen määrä: "))
naula = int (input("naulan määrä: "))
luoti = int (input ("luotien määrä: "))

a = leiviskä * 20 * 32 * 13.3
b = naula * 32 * 13.3
c = luoti *13.3

vastaus = a+b+c
print( "Massa nykymittojen mukaan: ",
       str(vastaus)[0:2], "klogrammaa ja", str(vastaus)[3:6], "grammaa")

