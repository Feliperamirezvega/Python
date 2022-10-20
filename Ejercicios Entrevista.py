"""
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max(a, b):
    if a > b:
        print(f"El valor mas grande es {a}")
    else:
        print(f"El valor mas grande es {b}")


print(max(10, 13))

"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def max_de_tres(a, b, c):
    if a > b and a > c:
        print(f"El valor mas grande es {a}")
    elif b > a and b > c:
        print(f"El valor mas grande es {b}")
    else:
        print(f"El valor mas grande es {c}")

print(max_de_tres(30, 25, 50))

"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def ejercicio(vocal):
    vocales = ["a", "e", "i", "o", "u"]
    if vocal in vocales:
        return True
    else:
        return False

print(ejercicio("d"))

"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def suma(lista):
    sumas = 0
    for i in lista:
        sumas += i
    print(sumas)

def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion = i * multiplicacion
    print(multiplicacion)


mi_lista = [2, 2, 2, ]

print(suma(mi_lista))
print(multip(mi_lista))

"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def cadena(texto):
    texto2 = texto[::-1]
    print(texto2)

print(cadena("estoy probando"))

"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def palindromo(cadena):
    cadena = cadena.lower()
    nueva_cadena = cadena[::-1]
    if nueva_cadena == cadena:
        return True
    else:
        return False

print(palindromo("Otto"))

"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return True
    return False

print(superposicion([2, 2, 1], [1, 1, 1]))

"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, b):
    print(n * b)

print(generar_n_caracteres(5, "x"))

"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
"""

def procedimiento(lista):
    valor = 0
    for n in lista:
        valor = n
        print(valor * '*')

lista1 = [60, 2, 3, 8, 10]
print(procedimiento(lista1))