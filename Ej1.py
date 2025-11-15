# Ejercicio 1:

def contar_frecuencias(cadena):
    resultado = {}
    for letra in cadena.replace(" ", ""):
        resultado[letra] = resultado.get(letra, 0) + 1
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    texto = "hola mundo"
    print(contar_frecuencias(texto))
