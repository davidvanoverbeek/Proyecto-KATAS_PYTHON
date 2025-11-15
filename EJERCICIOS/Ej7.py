# Ejercicio 7:

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: ''.join(map(str, t)), lista_tuplas))

# Ejemplo de uso
if __name__ == "__main__":
    lista = [(1, 2), (3, 4), (5, 6)]
    resultado = tuplas_a_strings(lista)
    print(resultado)  # Salida: ['12', '34', '56']
