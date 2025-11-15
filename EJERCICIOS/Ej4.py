# Ejercicio 4:

def diferencia_listas(lista1, lista2):
    # Asumimos que ambas listas tienen la misma longitud
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo de uso
if __name__ == "__main__":
    lista_a = [10, 20, 30, 40]
    lista_b = [1, 2, 3, 4]
    resultado = diferencia_listas(lista_a, lista_b)
    print(resultado)  # Salida: [9, 18, 27, 36]
