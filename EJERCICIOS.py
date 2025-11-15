# Ejercicio 1
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    dic = {}
    for char in cadena.replace(" ", ""):
        dic[char] = dic.get(char, 0) + 1
    return dic

print(frecuencia_letras("hola mundo"))

# Ejercicio 2
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

numeros = [1,2,3,4,5]
doble = list(map(lambda x: x*2, numeros))
print(doble)

# Ejercicio 3
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

print(filtrar_palabras(["hola","mundo","holanda"], "hol"))

# Ejercicio 4
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

lista1 = [10,20,30]
lista2 = [1,2,3]
diferencias = list(map(lambda x, y: x-y, lista1, lista2))
print(diferencias)

# Ejercicio 5
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def estado_media(numeros, nota_aprobado=5):
    media = sum(numeros)/len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

print(estado_media([4,5,6]))

# Ejercicio 6
# Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Ejercicio 7
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

tuplas = [(1,2), (3,4), (5,6)]
strings = list(map(str, tuplas))
print(strings)

# Ejercicio 8
# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje.

try:
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    resultado = a/b
except ValueError:
    print("Debes ingresar números válidos")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print(f"Resultado: {resultado}")

# Ejercicio 9
# Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.

def filtrar_mascotas(lista):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda x: x not in prohibidas, lista))

print(filtrar_mascotas(["Perro", "Gato", "Tigre", "Oso"]))

# Ejercicio 10
# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error.

def promedio(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return sum(lista)/len(lista)

try:
    print(promedio([1,2,3,4]))
    print(promedio([]))
except ValueError as e:
    print(e)

# Ejercicio 11
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (0-120), maneja las excepciones.

try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("Edad fuera de rango")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Tienes {edad} años")

# Ejercicio 12
# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitudes(frase):
    return list(map(len, frase.split()))

print(longitudes("Hola mundo desde Python"))

# Ejercicio 13
# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def mayus_minus(conjunto):
    return list(map(lambda x: (x.upper(), x.lower()), set(conjunto)))

print(mayus_minus("abcABC"))

# Ejercicio 14
# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

def filtrar_por_letra(lista, letra):
    return list(filter(lambda x: x.startswith(letra), lista))

print(filtrar_por_letra(["Ana","Pedro","Alberto"], "A"))

# Ejercicio 15
#  Crea una función lambda que sume 3 a cada número de una lista dada.

nums = [1,2,3]
suma3 = list(map(lambda x: x+3, nums))
print(suma3)

# Ejercicio 16
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_largas(texto, n):
    return list(filter(lambda x: len(x)>n, texto.split()))

print(palabras_largas("Hola mundo desde Python", 4))

# Ejercicio 17
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Usa reduce().

from functools import reduce

def digitos_a_numero(lista):
    return reduce(lambda x,y: x*10+y, lista)

print(digitos_a_numero([5,7,2]))

# Ejercicio 18
# Escribe un programa que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [
    {"nombre":"Ana", "edad":20, "nota":95},
    {"nombre":"Luis", "edad":22, "nota":85}
]

aprobados = list(filter(lambda x: x["nota"]>=90, estudiantes))
print(aprobados)

# Ejercicio 19
# Crea una función lambda que filtre los números impares de una lista dada.

nums = [1,2,3,4,5]
impares = list(filter(lambda x: x%2!=0, nums))
print(impares)

# Ejercicio 20
# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa filter().

mezcla = [1,"a",2,"b",3]
solo_int = list(filter(lambda x: isinstance(x,int), mezcla))
print(solo_int)

# Ejercicio 21
# Crea una función que calcule el cubo de un número dado mediante una función lambda.

cubo = lambda x: x**3
print(cubo(3))

# Ejercicio 22
# Dada una lista numérica, obtén el producto total de los valores. Usa reduce().

nums = [1,2,3,4]
producto = reduce(lambda x,y: x*y, nums)
print(producto)

# Ejercicio 23
# Concatena una lista de palabras. Usa reduce().

palabras = ["Hola", "mundo", "Python"]
concatenado = reduce(lambda x,y: x + " " + y, palabras)
print(concatenado)

# Ejercicio 24
# Calcula la diferencia total en los valores de una lista. Usa reduce().

valores = [10,2,3]
diferencia = reduce(lambda x,y: x-y, valores)
print(diferencia)

# Ejercicio 25
# Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres("Hola mundo"))

# Ejercicio 26
# Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x,y: x % y
print(resto(10,3))

# Ejercicio 27
# Crea una función que calcule el promedio de una lista de números.

def promedio_lista(lista):
    return sum(lista)/len(lista)

print(promedio_lista([1,2,3,4,5]))

# Ejercicio 28
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for x in lista:
        if x in vistos:
            return x
        vistos.add(x)
    return None

print(primer_duplicado([1,2,3,2,4]))

# Ejercicio 29
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con '#' excepto los últimos cuatro.

def enmascarar(valor):
    s = str(valor)
    return '#'*(len(s)-4) + s[-4:]

print(enmascarar("123456789"))

# Ejercicio 30
# Crea una función que determine si dos palabras son anagramas.

def anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(anagramas("amor","roma"))

# Ejercicio 31
# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista.

def buscar_nombre():
    lista = input("Introduce nombres separados por coma: ").split(",")
    nombre = input("Nombre a buscar: ")
    if nombre in lista:
        print(f"{nombre} fue encontrado")
    else:
        raise ValueError("Nombre no encontrado")

# Ejercicio 32
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre y devuelva el puesto si se encuentra.

def buscar_empleado(nombre, empleados):
    for emp in empleados:
        if emp["nombre"] == nombre:
            return emp["puesto"]
    return "La persona no trabaja aquí"

empleados = [{"nombre":"Ana","puesto":"Manager"},{"nombre":"Luis","puesto":"Developer"}]
print(buscar_empleado("Ana", empleados))

# Ejercicio 33
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1,2,3]
lista2 = [4,5,6]
suma = list(map(lambda x,y: x+y, lista1, lista2))
print(suma)

# Ejercicio 34
# Crea la clase Arbol con los métodos indicados.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        self.tronco += 1
    
    def nueva_rama(self):
        self.ramas.append(1)
    
    def crecer_ramas(self):
        self.ramas = [r+1 for r in self.ramas]
    
    def quitar_rama(self, pos):
        if 0 <= pos < len(self.ramas):
            self.ramas.pop(pos)
    
    def info_arbol(self):
        return {"tronco": self.tronco, "numero_ramas": len(self.ramas), "longitud_ramas": self.ramas}

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print(arbol.info_arbol())

# Ejercicio 35
# Crea la clase UsuarioBanco con los métodos indicados.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
    
    def transferir_dinero(self, otro, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para transferir")
        self.saldo -= cantidad
        otro.saldo += cantidad
    
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
print(alicia.saldo, bob.saldo)

# Ejercicio 36
# Crea la función procesar_texto con las opciones indicadas.

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        palabras = texto.split()
        from collections import Counter
        return dict(Counter(palabras))
    elif opcion == "reemplazar":
        original, nuevo = args
        return texto.replace(original, nuevo)
    elif opcion == "eliminar":
        palabra = args[0]
        return ' '.join(filter(lambda x: x != palabra, texto.split()))
    else:
        raise ValueError("Opción inválida")

print(procesar_texto("hola hola mundo", "contar"))
print(procesar_texto("hola mundo", "reemplazar", "mundo", "Python"))
print(procesar_texto("hola mundo Python", "eliminar", "mundo"))

# Ejercicio 37
# Genera un programa que nos indique si es de noche, día o tarde según la hora proporcionada por el usuario.

hora = int(input("Introduce la hora (0-23): "))
if 6 <= hora < 12:
    print("Es de mañana")
elif 12 <= hora < 20:
    print("Es de tarde")
else:
    print("Es de noche")

# Ejercicio 38
# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.

nota = int(input("Introduce tu calificación (0-100): "))
if nota <= 69:
    print("Insuficiente")
elif nota <= 79:
    print("Bien")
elif nota <= 89:
    print("Muy bien")
else:
    print("Excelente")

# Ejercicio 39
# Escribe una función que tome dos parámetros: figura y datos para calcular el área.

import math

def area(figura, datos):
    if figura == "rectangulo":
        return datos[0]*datos[1]
    elif figura == "circulo":
        return math.pi * datos[0]**2
    elif figura == "triangulo":
        return (datos[0]*datos[1])/2
    else:
        return None

print(area("rectangulo",(5,3)))
print(area("circulo",(4,)))
print(area("triangulo",(4,5)))

# Ejercicio 40
# Escribe un programa que determine el monto final de una compra después de aplicar un descuento.

precio = float(input("Precio original: "))
tiene_cupon = input("Tienes cupón? (sí/no): ").lower()
if tiene_cupon == "sí":
    descuento = float(input("Valor del cupón: "))
    if descuento > 0:
        precio_final = precio - descuento
    else:
        precio_final = precio
else:
    precio_final = precio

print(f"Precio final: {precio_final}")
