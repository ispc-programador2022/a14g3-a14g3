#Se importa funcion encargada de comprobar que se ingresen numeros
from ing2i import ing2i
#Se importa funcion encargada de la suma
from suma import suma
#Se importa funcion  encargada de la multiplicacion
from producto import producto

#10- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las funciones anteriores.
def p1_b(num1, num2, num3):
    try:
        ing2i(num1, num2)
        ing2i(num3)
        return producto(suma(num1, num2), num3)
    except:
        pass

