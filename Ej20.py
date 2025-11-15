# Ejercicio 20:

def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

if __name__ == "__main__":
    lista_mixta = [1, "a", 2, "b", 3]
    print(solo_enteros(lista_mixta))  # Salida: [1, 2, 3]
