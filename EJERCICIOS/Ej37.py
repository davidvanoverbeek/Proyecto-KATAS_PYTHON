# Ejercicio 37:

def determinar_momento(hora):
    if 6 <= hora < 12:
        return "Mañana"
    elif 12 <= hora < 20:
        return "Tarde"
    else:
        return "Noche"

if __name__ == "__main__":
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if 0 <= hora <= 23:
            print(determinar_momento(hora))
        else:
            print("Hora fuera de rango")
    except ValueError:
        print("Introduce un número válido")

