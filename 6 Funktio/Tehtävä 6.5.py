
def parittomat(luvut):
    poistettu =[]
    for x in luvut:
        if x % 2 == 0:
            poistettu.append(x)

    return poistettu

lista = (1,2,7,2,8,2,9,2,32,52,65,)
pariton_lista = parittomat(lista)
print("alkuperäinen lista: ", lista)
print("parilliset luvut: ", pariton_lista)