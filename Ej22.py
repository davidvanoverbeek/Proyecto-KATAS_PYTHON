# Ejercicio 22:

from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4]
    print(producto_total(numeros))  # Salida: 24
