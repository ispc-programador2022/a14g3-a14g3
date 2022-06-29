#Se importa funcion encargada del promedio
from media_vector import media_vector
#Se importa funcion encargada de la creacion de la lista con numeros aleatorios
from genrnd import genrnd

def varianza_vector(lista=[], media=[]):
    if len(lista) == 0:
        lista = genrnd() #Se asigna el valor a la lista
        media = media_vector(lista) #Se asigna el valor a la media
    #Se crea que contiene cada uno de los valores de la lista menos la media de la misma
    valores_menos_media = list(map(lambda a: a - media, lista))
    #Se devuele la varianza (suma de valores menos su media dividido la cantidad de valores)
    return (sum(valores_menos_media) / len(lista))

""" 
Formula utilizada:

Var (X) = (x1 – x’)2 + (x2 – x’)2 + … + (xn – x’) / N

Donde:

N representa el número total de observaciones o de datos utilizados para el cálculo de la varianza.
x representa los datos utilizados para el cálculo de la varianza.
x’ representa la media aritmética calculada con los datos utilizados para el cálculo de la varianza

#Fuente de donde se obtuvo la info: https://www.sdelsol.com/glosario/varianza/ 
"""