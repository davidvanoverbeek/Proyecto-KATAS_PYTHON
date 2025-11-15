# Ejercicio 16:
def palabras_mas_largas(frase, n):
    palabras = frase.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

if __name__ == "__main__":
    frase = "Hola mundo desde Python"
    print(palabras_mas_largas(frase, 4))  # Salida: ['mundo', 'Python']
