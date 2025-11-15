# Ejercicio 19:

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6]
    print(filtrar_impares(numeros))  # Salida: [1, 3, 5]
