#Se importa la funcion encargada de generar lista con 50 numeros aleatorios
from genrnd import genrnd

#20- función que calcule devuelva el mínimo del vector obtenido en genrnd.
def minimo_vector(lista=[]):
    if len(lista)==0:#Si no se recive lista por argumento se crea
        lista = genrnd()
    return min(lista) #Se retorna el minimo valor del vector