# Ejercicio 10:

class ListaVaciaError(Exception):
    pass

def promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(lista) / len(lista)

# Ejemplo de uso
if __name__ == "__main__":
    try:
        numeros = [5, 10, 15]
        print(promedio(numeros))  # Salida: 10.0
        print(promedio([]))       # Esto generará la excepción
    except ListaVaciaError as e:
        print(f"Error: {e}")
