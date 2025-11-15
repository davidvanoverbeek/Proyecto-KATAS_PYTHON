# Ejercicio 18:

def estudiantes_aprobados(estudiantes):
    return list(filter(lambda est: est['calificacion'] >= 90, estudiantes))

if __name__ == "__main__":
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 21, "calificacion": 85},
        {"nombre": "Pedro", "edad": 22, "calificacion": 92},
    ]
    print(estudiantes_aprobados(estudiantes))  
    # Salida: [{'nombre': 'Ana', 'edad': 20, 'calificacion': 95}, {'nombre': 'Pedro', 'edad': 22, 'calificacion': 92}]
