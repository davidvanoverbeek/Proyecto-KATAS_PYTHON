# Ejercicio 15:

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

if __name__ == "__main__":
    numeros = [1, 2, 3]
    print(sumar_tres(numeros))  # Salida: [4, 5, 6]
