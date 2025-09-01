def lista_num(kokonaisluvut):
    summa = 0
    for kokonaisluku in kokonaisluvut:
        summa += kokonaisluku
    return summa


lista = (3, 8, 2, 2, 3)
tulos = lista_num(lista)
print("listan: ", lista)
print("summa:", tulos)
