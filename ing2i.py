#Funcion encargada de almacenar y devolver numeros - #Autor: Yané, Ian
def ing2i(val1=0, val2=0):
    if not (type(val1) is int):
        print('La funcion "ing2i" admite solo valores numericos.')

    if not (type(val2) is int):
        print('La funcion "ing2i" admite solo valores numericos.')
    else:
        return(int(val1), int(val2))