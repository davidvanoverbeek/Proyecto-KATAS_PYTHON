# Ejercicio 29:

def enmascarar(valor):
    s = str(valor)
    return '#' * (len(s) - 4) + s[-4:]

if __name__ == "__main__":
    print(enmascarar(123456789))  # Salida: #####6789
