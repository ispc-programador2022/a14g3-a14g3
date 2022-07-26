from genrnd2 import genrnd2

#28- función que calcule devuelva el máximo del vector obtenido en genrnd.
def maximo_del_vector(lista=[]):
    if len(lista)==0:             #Si no se recive lista por argumento se crea
        lista = genrnd2()
    return max(lista)     #Se retorna el máximo valor del vector
