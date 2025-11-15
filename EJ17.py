# Ejercicio 17:

from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

if __name__ == "__main__":
    digitos = [5, 7, 2]
    print(lista_a_numero(digitos))  # Salida: 572
