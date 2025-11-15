# Ejercicio 27:

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

if __name__ == "__main__":
    numeros = [2, 4, 6]
    print(promedio(numeros))  # Salida: 4.0
