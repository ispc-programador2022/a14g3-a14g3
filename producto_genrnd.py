#Se importa la funcion genrnd
from genrnd import genrnd
#Se importa funcion encargada del producto
from producto import producto

#13- función que devuelva la suma de las combinaciones posibles de los números generados 
# por la función genrnd tomados de a dos.
def producto_genrnd(lista=[]):
    if len(lista)==0:
        lista = genrnd()#Asigna a la variable una lista
    x = []#Se inicializa la lista de los resultados en 0
    for i in lista:#Toma los primeros valores
        for j in lista:#Toma los segundos valores
            if (i != j):#Comprueba que los numeros sean distintos
                #Agrega el resultado a una lista
                x.append(producto(lista[lista.index(i)], lista[lista.index(j)]))
    return sum(x) #Retorna la suma de todos los valores almacenados