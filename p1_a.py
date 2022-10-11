#Se importa la funcion encargada de realizar la multiplicacion
from producto import producto 
#Se importa la funcion encargada de la suma
from suma import suma

#9- función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.
def p1_a(num1, num2, num3):
    def p1_b(num1, num2, num3):
        try:
            ing2i(num1, num2)
            ing2i(num3)
            return suma(producto(num1, num2), num3)
        except:
            pass