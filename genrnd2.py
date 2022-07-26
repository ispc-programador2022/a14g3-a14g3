import random #Modulo Random

def genrnd2():
    lista=[]      
    #En este caso for i in range(500000000000000000): No se usa por desbordamiento de memoria
    for i in range(5000000): #Para pruebas 5.000,000 numeros
        lista.append(random.randint(-256,+256))
    return lista #Devuelve
