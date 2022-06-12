def   radicación(a, b):
    return pow(a, 1/b)

a = int(input('Ingrese valor de radicando: '))
b = int(input('Ingrese valor de indice de raiz: '))

print(f'La   raiz de {a} respecto de {b} es {  radicación(a, b)}')
