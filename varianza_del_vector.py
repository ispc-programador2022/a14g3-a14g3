from media_del_vector import media_del_vector     #Se importa funcion encargada del promedio
from genrnd2 import genrnd2     #Se importa funcion encargada de la creacion de la lista con numeros aleatorios

def varianza_del_vector(lista=[], media=[]):
    if len(lista) == 0:
        lista = genrnd2() #Se asigna el valor a la lista
        media = media_del_vector(lista) #Se asigna el valor a la media
    #Se crea que contiene cada uno de los valores de la lista menos la media de la misma
    valores_menos_media = list(map(lambda a: a - media, lista))
    #Se devuele la varianza (suma de valores menos su media dividido la cantidad de valores)
    return (sum(valores_menos_media) / len(lista))
