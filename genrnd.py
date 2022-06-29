#Se importa modulo random
import random

#12- función genrnd que retorna una lista con 50 números aleatorios.
def genrnd():
    lista = [] #Se inicializa la lista que se retornara
    for i in range(50):#Se recorre un rango de los 50 valores
        lista.append(random.randint(0, 100)) #Se toma un valor aleatorio entre 0 y 100
    return lista #Se devuelve la lista