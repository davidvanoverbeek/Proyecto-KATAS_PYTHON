# Ejercicio 36:

def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    return ' '.join([p for p in palabras if p != palabra])

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción inválida o argumentos incorrectos")

if __name__ == "__main__":
    texto = "hola mundo hola python"
    print(procesar_texto(texto, "contar"))
    print(procesar_texto(texto, "reemplazar", "python", "java"))
    print(procesar_texto(texto, "eliminar", "hola"))
