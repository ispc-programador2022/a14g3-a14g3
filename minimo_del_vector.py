from genrnd2 import genrnd2

#27- función que calcule devuelva el mínimo del vector obtenido en genrnd2.
def minimo_del_vector(lista=[]):
    if len(lista)==0:        #Si no se recive lista por argumento se crea
        lista = genrnd2()
    return min(lista)            #Se retorna el minimo valor del vector
