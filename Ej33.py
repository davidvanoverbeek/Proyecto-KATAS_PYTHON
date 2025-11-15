# Ejercicio 33:

suma_listas = lambda l1, l2: [x + y for x, y in zip(l1, l2)]

if __name__ == "__main__":
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    print(suma_listas(lista1, lista2))  # Salida: [5, 7, 9]
