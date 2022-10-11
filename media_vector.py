#Se importa la funcion genrnd
from genrnd import genrnd

#16- función que calcule la media del vector obtenido en genrnd.
def media_vector(lista=[]):
    if len(lista)==0:
        lista = genrnd()#Se le asigna la lista a una variable ya que tendra que ser llamada msa de una vez
    return (sum(lista) / len(lista)) #Se devuelve el promedio (suma de todos su valores dividido la cantidad)