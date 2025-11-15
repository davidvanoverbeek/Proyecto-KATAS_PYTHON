# Ejercicio 23:

from functools import reduce

def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

if __name__ == "__main__":
    palabras = ["Hola", " ", "mundo"]
    print(concatenar_palabras(palabras))  # Salida: "Hola mundo"
