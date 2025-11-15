# Ejercicio 11:

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        print(f"Tu edad es {edad}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pedir_edad()
