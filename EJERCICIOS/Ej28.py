# Ejercicio 28:

def primer_duplicado(lista):
    vistos = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return None

if __name__ == "__main__":
    numeros = [1, 2, 3, 2, 5]
    print(primer_duplicado(numeros))  # Salida: 2
