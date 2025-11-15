# Ejercicio 9:

def filtrar_mascotas(mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in mascotas_prohibidas, mascotas))

# Ejemplo de uso
if __name__ == "__main__":
    lista_mascotas = ["Perro", "Gato", "Tigre", "Pez", "Mapache"]
    resultado = filtrar_mascotas(lista_mascotas)
    print(resultado)  # Salida: ['Perro', 'Gato', 'Pez']
