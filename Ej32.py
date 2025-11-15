# Ejercicio 32:

def buscar_empleado(nombre, empleados):
    for emp in empleados:
        if emp['nombre'] == nombre:
            return emp['puesto']
    return "La persona no trabaja aquí."

if __name__ == "__main__":
    empleados = [
        {"nombre": "Ana Perez", "puesto": "Developer"},
        {"nombre": "Luis Gomez", "puesto": "Designer"},
    ]
    print(buscar_empleado("Ana Perez", empleados))  # Salida: Developer
    print(buscar_empleado("Carlos", empleados))     # Salida: La persona no trabaja aquí.
