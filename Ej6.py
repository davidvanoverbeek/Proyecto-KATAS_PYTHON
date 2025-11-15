# Ejercicio 6:

def factorial(n):
    if n < 0:
        raise ValueError("No se puede calcular factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejemplo de uso
if __name__ == "__main__":
    numero = 5
    print(f"Factorial de {numero} es {factorial(numero)}")  # Salida: 120
