# Proyecto 3: Katas Python (Ejercicios 1-40)

## Descripción del proyecto

Este proyecto consiste en resolver una serie de ejercicios de Python (Katas) con el objetivo de practicar y afianzar conocimientos en:

* Tipos de datos básicos y funciones incorporadas.
* Estructuras de datos (listas, diccionarios, tuplas, sets).
* Condicionales y estructuras de control de flujo.
* Iteraciones (`for`, `while`) y comprensión de listas.
* Funciones y programación orientada a objetos (POO).
* Manejo de excepciones y entradas del usuario.
* Uso de módulos estándar (`functools`, `math`, etc.).
* Buenas prácticas de codificación y comentarios explicativos.

Cada ejercicio está resuelto en un archivo `.py` independiente con su correspondiente comentario con el enunciado.

---

## Resumen de pasos y soluciones (Ejercicios 1-40)

### Ejercicio 1-5: Funciones básicas y manipulación de cadenas/listas

* Uso de diccionarios para contar frecuencias.
* `map()` para multiplicar valores y calcular diferencias.
* Filtrado de palabras que contengan ciertas subcadenas.
* Funciones con parámetros opcionales para calcular medias y estados.
* Recursión para calcular factoriales.

### Ejercicio 6-10: Manipulación de listas y manejo de excepciones

* Conversión de tuplas a listas de strings (`map()`).
* Gestión de excepciones para divisiones y validación de entradas del usuario.
* Filtrado de listas (`filter()`) para excluir elementos prohibidos.
* Funciones que manejan listas vacías y lanzan excepciones personalizadas.

### Ejercicio 11-15: Funciones de transformación de datos

* Uso de `map()` para calcular longitudes de palabras y generar combinaciones mayúsculas/minúsculas únicas.
* Filtrado basado en criterios específicos (letra inicial, longitud de palabra).
* Funciones lambda para operaciones simples como sumar un valor a cada elemento de una lista.

### Ejercicio 16-20: Reducción y agregación de datos

* Uso de `reduce()` para concatenar listas, calcular promedios, productos y diferencias totales.
* Filtrado y manipulación de listas de diccionarios.
* Funciones lambda para cálculos rápidos (cubo, resto de división).

### Ejercicio 21-30: Clases y POO

* Creación de la clase `Arbol` con métodos:

  * `crecer_tronco`, `nueva_rama`, `crecer_ramas`, `quitar_rama`, `info_arbol`.
* Creación de la clase `UsuarioBanco` con métodos:

  * `retirar_dinero`, `agregar_dinero`, `transferir_dinero`.
* Ejecución de casos de prueba para validar que la lógica de la clase funciona correctamente.

### Ejercicio 31-40: Funciones avanzadas de texto y cálculo

* Funciones `procesar_texto` para contar, reemplazar y eliminar palabras de un texto.
* Programas para determinar hora del día según entrada del usuario.
* Funciones para calcular áreas de figuras geométricas.
* Programas que aplican descuentos a compras y muestran resultados finales usando condicionales.
* Funciones que asignan calificación textual a los alumnos según su nota.

---

## Buenas prácticas seguidas

* Cada función está comentada para explicar su objetivo y funcionamiento.
* Manejo de errores con `try/except` donde fue necesario.
* Separación de ejercicios en archivos `.py` independientes para facilitar la revisión.
* Uso de funciones lambda y funciones integradas de Python (`map`, `filter`, `reduce`) para simplificar y optimizar el código.
* Validación de entradas del usuario y control de casos especiales (listas vacías, divisiones por cero, caracteres no numéricos, etc.).

---

## Cómo ejecutar los ejercicios

1. Clonar el repositorio.
2. Navegar a la carpeta del proyecto.
3. Ejecutar cualquier ejercicio con:

```bash
python ejercicioX.py
```

Reemplazando `X` por el número del ejercicio (1-40).

