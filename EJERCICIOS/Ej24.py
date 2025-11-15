# Ejercicio 24:

from functools import reduce

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

if __name__ == "__main__":
    numeros = [10, 2, 3]
    print(diferencia_total(numeros))  # Salida: 5 (10-2-3)
