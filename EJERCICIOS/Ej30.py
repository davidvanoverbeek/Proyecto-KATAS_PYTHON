# Ejercicio 30:

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

if __name__ == "__main__":
    print(son_anagramas("roma", "amor"))  # Salida: True
    print(son_anagramas("hola", "adios"))  # Salida: False
