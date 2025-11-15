# Ejercicio 38:

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota inválida"

if __name__ == "__main__":
    try:
        nota = int(input("Introduce la calificación (0-100): "))
        print(calificacion_texto(nota))
    except ValueError:
        print("Introduce un número válido")
