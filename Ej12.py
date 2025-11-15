# Ejercicio 12:

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

if __name__ == "__main__":
    frase = "Hola mundo desde Python"
    print(longitud_palabras(frase))  # Salida: [4, 5, 4, 6]
