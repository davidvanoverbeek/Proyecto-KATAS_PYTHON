# Ejercicio 13:

def mayus_minus_letras(caracteres):
    caracteres_unicos = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))

if __name__ == "__main__":
    chars = ['a', 'b', 'a', 'c']
    print(mayus_minus_letras(chars))  # Salida: [('A','a'), ('B','b'), ('C','c')]
