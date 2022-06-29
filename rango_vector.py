#Se importa funcion encargada de generar 50 numeros aleatorios
from genrnd import genrnd

def rango_vector(lista=[]):
    if len(lista)==0:
        lista = genrnd()#Asigna a la variable una lista
    return (max(lista) - min(lista)) #Se resta el valor maximo de los numeros con el valor minimo de los numeros