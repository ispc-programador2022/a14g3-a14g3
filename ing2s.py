#Funcion encargada de almacenar y devolver letras - #Autor: Yané, Ian
def ing2s(letras1, letras2):
    if not (type(letras1) is str):
        print('La funcion "ing2s" admite solo valores en letras.')

    while not (type (letras2) is str):
        if not letras1.isalpha():
            print('La funcion "ing2s" admite solo valores en letras.')

    return((letras1), (letras2))