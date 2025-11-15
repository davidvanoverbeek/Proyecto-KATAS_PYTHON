# Ejercicio 3:

def filtrar_palabras(lista, palabra_objetivo):
    return [palabra for palabra in lista if palabra_objetivo in palabra]

# Ejemplo de uso
if __name__ == "__main__":
    palabras = ["manzana", "banana", "cereza", "platano", "mango"]
    objetivo = "an"
    resultado = filtrar_palabras(palabras, objetivo)
    print(resultado)  # Salida: ['manzana', 'banana', 'platano', 'mango']
