#Se importa la funcion genrnd
from genrnd import genrnd
#Se importa funcion encargada de la suma
from suma import suma

#13- función que devuelva la suma de las combinaciones posibles de los números generados 
# por la función genrnd tomados de a dos.
def suma_genrnd():
    x = []
    lista = genrnd()
    for i in lista:
        for j in lista:
            if (i != j):
                x.append(suma(lista[lista.index(i)], lista[lista.index(j)]))
    return x
