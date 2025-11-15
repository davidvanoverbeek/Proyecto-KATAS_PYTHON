# Ejercicio 31:

def buscar_nombre():
    nombres = input("Introduce una lista de nombres separados por coma: ").split(",")
    nombre_buscar = input("Introduce un nombre a buscar: ")
    if nombre_buscar in nombres:
        print(f"{nombre_buscar} fue encontrado en la lista.")
    else:
        raise ValueError(f"{nombre_buscar} no está en la lista.")

if __name__ == "__main__":
    try:
        buscar_nombre()
    except ValueError as e:
        print(e)
