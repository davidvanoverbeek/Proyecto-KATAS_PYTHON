# Ejercicio 39:

import math

def area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no reconocida")

if __name__ == "__main__":
    print(area("rectangulo", (5, 3)))  # Salida: 15
    print(area("circulo", (4,)))       # Salida: ~50.27
    print(area("triangulo", (6, 2)))   # Salida: 6
