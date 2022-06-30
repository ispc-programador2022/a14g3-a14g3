#Se importa funcion encargada de generar 50 numeros aleatorios
from genrnd import genrnd

#18- función que calcule el rango del vector obtenido en genrnd.
def rango_vector(lista=[]):
    if len(lista)==0:#Comprueba que se reciva una lista
        lista = genrnd()#Asigna a la variable una lista en caso de que no se reciva
    return (max(lista) - min(lista)) #Se resta el valor maximo de los numeros con el valor minimo de los numeros