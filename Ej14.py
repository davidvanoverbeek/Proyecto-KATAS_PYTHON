# Ejercicio 14:

def palabras_con_inicial(lista, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista))

if __name__ == "__main__":
    palabras = ["Ana", "Alberto", "Pedro", "Amanda"]
    print(palabras_con_inicial(palabras, "A"))  # Salida: ['Ana', 'Alberto', 'Amanda']
