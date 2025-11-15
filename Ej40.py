# Ejercicio 40:

def calcular_precio_final():
    try:
        precio = float(input("Introduce el precio original: "))
        cupón = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        if cupón == "sí":
            valor_cupon = float(input("Introduce el valor del cupón: "))
            if valor_cupon > 0:
                precio -= valor_cupon
        print(f"Precio final: {precio}")
    except ValueError:
        print("Entrada inválida, asegúrate de introducir números válidos.")

if __name__ == "__main__":
    calcular_precio_final()
