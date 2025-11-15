# Ejercicio 5:

def evaluar_media(numeros, nota_aprobado=5):
    if not numeros:
        return (0, "suspenso")
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# Ejemplo de uso
if __name__ == "__main__":
    notas = [6, 7, 8, 5, 4]
    resultado = evaluar_media(notas)
    print(resultado)  # Salida: (6.0, "aprobado")
