Proyecto: Katas de Python (v0)

Este repositorio/proyecto recopila una serie de katas (ejercicios) en Python orientadas a practicar:
- Estructuras de datos (listas, tuplas, sets y diccionarios)
- Programación funcional (map, filter, reduce)
- Excepciones (try/except, raise)
- Programación orientada a objetos (clases ARBOL y UsuarioBanco)
- Entrada por teclado y pequeños menús interactivos

Fuente de los ejercicios: archivo Proyecto Katas de Python v.0-Python.txt.

------------------------------------------------------------

#Pasos seguidos durante el proyecto

1. Arranque del proyecto  
   Creación de un archivo único con ejercicios, organizado en bloques tipo notebook mediante separadores %% (compatible con VS Code/Jupyter).

2. Implementación incremental por ejercicios  
   Para cada ejercicio:
   - lectura del enunciado
   - implementación de una primera versión
   - ejecución/pruebas (con print y casos simples)
   - ajustes: manejo de errores, refactor de funciones, y variantes usando map/filter/reduce

3. Introducción de validaciones  
   A partir de los ejercicios con input(), se añade control de:
   - conversión de tipos (int, float)
   - rangos válidos (edad, calificaciones, hora, etc.)
   - reintentos mediante while True cuando procede

4. OOP y casos de uso  
   Se implementan clases (ARBOL, UsuarioBanco) y se añaden casos de prueba para comprobar comportamiento.

5. Consolidación  
   Se agrupan ejercicios relacionados (p.ej. el bloque del ejercicio 37 de procesamiento de texto) y se documentan mejoras/pendientes.

------------------------------------------------------------

#Requisitos

- Python 3.10+ recomendado (por tipado moderno).
- Librerías estándar utilizadas:
  - functools (reduce)
  - math (pi, factorial)
  - datetime (hora del día)

No se requieren dependencias externas.

------------------------------------------------------------

#Cómo ejecutar

##Opción A: VS Code / Jupyter (recomendado)
El archivo está en formato “celdas” (%%). En VS Code puedes ejecutar cada celda por separado.

##Opción B: Convertir a .py y ejecutar
1. Convierte el notebook/celdas a script si lo tienes como .ipynb (nbconvert) o copia el contenido a katas.py.
2. Ejecuta:
   ``bash
   python katas.py
   `
   Nota: algunos ejercicios piden datos por teclado; ejecútalos de forma individual o comenta los input() si quieres ejecución completa sin interacción.

------------------------------------------------------------

#Comentarios por ejercicio

- Ejercicio 1. : Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
  - Frecuencias de letras en una cadena ignorando espacios. Se practica el bucle for, diccionarios y la comprobación de ' '.
Mejora: normalizar mayúsculas/minúsculas y usar collections.Counter si se quiere simplificar.
- Ejercicio 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
  - Doble de cada número con bucle y con map. Se comparan enfoques imperativo vs funcional.
Nota: numeros = list[int] es un *tipo*, no una lista; conviene usar numeros: list[int] = [...].
- Ejercicio 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista
  - Filtrado por subcadena (objetivo in palabra). Útil para búsquedas simples.
Mejora: normalizar a minúsculas si se quiere búsqueda sin distinguir mayúsculas.
- Ejercicio 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función MAP ()
  - Diferencia elemento a elemento con map(lambda x,y: x-y, ...).
Nota: map se detiene al acabar la lista más corta.
- Ejercicio 4-BIS. Genera una función que calcule la SUMA entre los valores de dos listas. SI UN VALOR SUPERA 40, LO DEVUELVE A 0. Usa la función MAP ()
  - Suma elemento a elemento con condicional dentro de lambda (si supera 40, devuelve 0).
- Ejercicio 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
  - Cálculo de media y estado (aprobado/suspenso) devolviendo una tupla (media, estado).
Mejora: definir nota_corte como parámetro con valor por defecto.
- Ejercicio 6. Escribe una función que calcule el factorial de un número de manera recursiva.
  - Factorial recursivo (casos base 0 y 1) y alternativa con math.factorial.
- Ejercicio 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usar la función MAP ()
  - Convertir lista de tuplas a lista de strings usando ' '.join(tupla) con map.
- Ejercicio 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
  - División con manejo de excepciones (ValueError, ZeroDivisionError) y bloque else si todo va bien.
- Ejercicio 9. Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
  - Filtrado de mascotas prohibidas con filter y una lista de exclusión. Buen ejemplo de listas + lambda.
- Ejercicio 10. Escribe una función que reciba una lista de números y calcule su promedio.
  - Promedio con validación de lista vacía (lanza ValueError). Se prueba también con lista vacía y con entrada por teclado (10-1, 10-2).
- Ejercicio 10-1. AHORA PROBAMOS LA EXCEPCIÓN PERSONALIZADA CON UNA LISTA VACÍA
  - Caso de prueba de lista vacía para forzar la excepción del ejercicio 10.
- Ejercicio 10-2. AHORA INTRODUCIMOS LOS NÚMEROS DE LA LISTA DESDE EL TECLADO
  - Construcción de lista desde teclado y reutilización de la función promedio.
- Ejercicio 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
  - Validación de edad (tipo entero y rango 0–120) con try/except/else y raise ValueError.
- Ejercicio 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usar la función MAP ()
  - Longitud de cada palabra en una frase usando split() + map(len, ...).
- Ejercicio 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
  - Generación de tuplas (mayúscula, minúscula) a partir de un conjunto de caracteres. Se usa set para eliminar repetidos.
Nota: el orden de un set no es determinista; si se quiere orden fijo, usar sorted(set(...)).
- Ejercicio 14. Crea una función que retome las palabras de una lista de palabras que comience con una letra en especifico. Usa la función FILTER ()
  - Filtrado de palabras por letra inicial con filter + startswith.
- Ejercicio 14-1. Ahora con map ()
  - Alternativa con map que inserta None y luego se elimina con un bucle (sin filter).
- Ejercicio 15. Crea una función lambda que  sume 3 a cada número de una lista dada
  - Lambda/map para sumar 3 a cada número de una lista.
- Ejercicio 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
  - Filtro de palabras más largas que n con filter y len.
- Ejercicio 17. Crea una función que tome una lista de dígigos y devuelva el número correspondiente. Por ejemplo, 5,7,2
  - Construcción de un número a partir de una lista usando reduce (concatenación).
- Ejercicio 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
  - Lista de diccionarios de alumnos y filtrado por calificación ≥ 90 con filter.
- Ejercicio 19. Crea una función lambda que filtre los números impares de una lista dada.
  - Filtrado de impares con filter(lambda x: x % 2 != 0, ...).
- Ejercicio 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
  - Filtrado por tipo (int y str) usando isinstance.
- Ejercicio 21. Crea una función que calcule el cubo de un número dado MEDIANTE LA FUNCIÓN LAMBDA
  - Cálculo del cubo con lambda x: x3.
- Ejercicio 22. DADA una lista numérica, obtener el producto total de valores de dicha lista, usando la función reduce ()
  - Producto total con reduce. Mejora: usar inicializador (reduce(..., lista, 1)) para listas vacías.
- Ejercicio 23. CONCATENA UNA LISTA DE PALABRAS, USANDO LA FUNCIÓN REDUCE ()
  - Concatenación de palabras con reduce. Mejora: normalmente se usa ' '.join(lista).
- Ejercicio 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce ()
  - Diferencia sucesiva con reduce (el orden importa).
- Ejercicio 25. Crea una función que cuente el número de caracteres en una cadena de texto dada
  - Conteo de caracteres con len (función simple).
- Ejercicio 26. Crea una función lambda que calcule el resto de la división entre dos números dados
  - Resto de división con lambda y operador %.
- Ejercicio 27. Crea una función que calcule el promedio de una lsita de números
  - Promedio sin validación de lista vacía (mejora: reutilizar validación del ejercicio 10).
- Ejercicio 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
  - Primer duplicado usando un set de vistos; patrón clásico de detección en O(n).
- Ejercicio 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
  - Enmascarado de tarjeta dejando 4 últimos.
Ojo: el enfoque con replace(tarjeta_str[i], '#', 1) reemplaza la *primera ocurrencia del carácter*, no la posición i; puede fallar si hay dígitos repetidos. Mejor: '#'*12 + tarjeta_str[-4:].
- Ejercicio 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
  - Anagramas comparando set de letras.
Ojo: set ignora repeticiones, así que puede dar falsos positivos (p.ej. 'aab' y 'ab'). Mejor: sorted(p1)==sorted(p2) o Counter.
- Ejercicio 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
  - Entrada de lista de nombres por comas, limpieza con strip() y búsqueda. Si no está, lanza ValueError.
- Ejercicio 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
  - Búsqueda de empleado por nombre completo en lista de diccionarios; uso de .get() para evitar KeyError.
- Ejercicio 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
  - Suma elemento a elemento de dos listas con map y lambda.
- Ejercicio 34. Crea la clase de objetos 'ARBOL', define un árbol genérico con un tronco y ramas como atributos.
  - Clase ARBOL con atributos tronco y ramas y métodos de crecimiento/gestión.
Mejoras: revisar indentación, tipado y que info_arbol use self.tronco (no arbol.tronco).
- Ejercicio 35. - 1. Check y caso de Uso ARBOL
  - Caso de uso del árbol: crecimiento de tronco/ramas, añadir y quitar ramas, e imprimir info.
- Ejercicio 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
  - Primera versión de UsuarioBanco (incompleta/errónea en el archivo: referencia a variables no definidas).
La versión 36-1 es la base recomendable.
- Ejercicio 37. - CREA una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras,
  - Bloque de procesamiento de texto: contar, reemplazar y eliminar palabras mediante funciones auxiliares y un menú interactivo.
- Ejercicio 37-1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
  - contar_palabras: devuelve diccionario con frecuencias de palabras.
- Ejercicio 37-2. Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva.
  - reemplazar_palabras: reemplaza palabra exacta usando map.
- Ejercicio 37-3. Eliminar_palabras. para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
  - eliminar_palabras: elimina una palabra exacta (marca con '' y filtra).
- Ejercicio 37-4. Crear la función procesar_terxto que tome un texto, una opción entre "contar", "reemplazar", "eliminar"
  - procesar_texto: pide texto y opción, solicita parámetros extra según la opción.
- Ejercicio 37-5. Caso de Uso. Comprobación de la función.
  - Caso de uso: ejecución interactiva de procesar_texto().
- Ejercicio 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario
  - Clasificación del momento del día usando datetime y rangos horarios.
Mejora: validar hora 0–23 (24 no es válida para datetime.replace).
- Ejercicio 39. Escribe un Programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son (0-69) - Suficiente,
  - En el archivo queda el enunciado, pero no hay implementación (pendiente).
- Ejercicio 40. Escribe una función QUE TOME dos parámetros: figura (cadena qeu puede ser "rectángulo", "círculo", "triángulo") y datos
  - Hay dos intentos: uno erróneo (mezcla variables de 'puntuación') y la versión funcional area_poligono con menú para rectángulo/triángulo/círculo.
- Ejercicio 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
  - Programa de descuento con validaciones de entrada, opción de cupón y control de rangos. Mejora: devolver el valor final (no return print(...)).

------------------------------------------------------------

#Recomendaciones y mejoras (técnicas)

- Evitar variables con acentos en código (puntuación, calificación) si se prevé compatibilidad o colaboración (no es “error”, pero puede dar guerra en algunos entornos).
- Preferir while a recursión para reintentar entradas del usuario (evita profundidad de recursión).
- Para anagramas: usar sorted() o collections.Counter para respetar repeticiones.
- Para enmascarado de tarjetas: usar slicing, no replace por carácter.
- Para clases: mantener nombres de métodos únicos (en UsuarioBanco hay un método duplicado con el mismo nombre en el archivo).

------------------------------------------------------------

#Estado del proyecto

- ✅ Ejercicios implementados: 1–38, 40–41 (con observaciones).
- ⏳ Pendiente: ejercicio 39 (solo enunciado en el archivo).
- 🧹 Pendiente de refactor: primera versión de UsuarioBanco (36) y el primer intento del 40 (función areas()`).

Fecha de generación del README: 2026-02-10
