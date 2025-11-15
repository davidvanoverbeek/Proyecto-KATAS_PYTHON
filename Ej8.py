# Ejercicio 8:

def dividir_numeros():
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = a / b
        print(f"Resultado de la división: {resultado}")
    except ValueError:
        print("Error: Debes ingresar números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

# Ejecución
if __name__ == "__main__":
    dividir_numeros()
