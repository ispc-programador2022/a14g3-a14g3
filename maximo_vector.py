from genrnd import genrnd #Se importa la funcion encargada de generar lista con 50 numeros aleatorios
#20- función que calcule devuelva el maximo del vector obtenido en genrnd.
def maximo_vector(lista=[]):
    if len(lista)==0: #Si no se recive lista por argumento se crea...
        lista = genrnd()
    return max(lista) #Se retorna el maximo valor del vector.
