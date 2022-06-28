#Se importa mosulo random
import random
#12- función genrnd que retorna una lista con 50 números aleatorios.
def genrnd():
    lista = []
    for i in range(50):
        #Se escoge un numero suficientemente grande para aumentar relacion de aletoriedad
        lista.append(random.randint(0, 100000)) 
    return lista