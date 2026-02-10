# %%
##################################################################
######### Archivo de Katas de Python - Ejercicio 001 #############
##################################################################

# %%
# EJERCICIO 1: Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados

cadena_de_texto = "hola mundo"
print (f"la cadena de texto es: {cadena_de_texto}")
contador = len (cadena_de_texto)
print (f"el numero de caracteres es: {contador}")

#vamos a recorrer la cadena de texto y contar las letras

for c in cadena_de_texto:
    print (c)

# vamos a crear el diccionario para contar las letras

def contar_letras (cadena_de_texto):  

    "Definimos el diccionario "
    frecuencias = {}
    "y contamos las letras"
    for letra in cadena_de_texto:
        if letra != ' ':
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

print (contar_letras (cadena_de_texto))


# %%
# EJERCICIO 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

#Primero definimos un bucle
numeros = list[int]

def doble (numeros):
    dobles = []
    for n in numeros: 
         dobles.append(n*2)
    return dobles

numeros = [1, 2, 3, 4, 5]
print (doble (numeros))

# ahora usamos map
def doble_map (numeros):
    "lambda x: recorre la lista y x*2 la multiplica por 2"
    return list (map (lambda x: x*2, numeros))
print (doble_map (numeros))

# Se puede hacer de las 2 maneras.

# %%
# EJERCICIO 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista 
# con todas las palabras de la lista original que contengan la palabra objetivo.

def palabras_objetivo (palabras, objetivo):
    lista_resultado = []
    for palabra in palabras:
        if objetivo in palabra:
            lista_resultado.append(palabra)
    return lista_resultado

palabras = ["pedro", "drones", "cabeza", "padron", "manos", "curvado"]
objetivo = "dro"
print (palabras_objetivo (palabras, objetivo))

# %%
# EJERCICIO 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función MAP ()

def diferencia_listas (lista1, lista2):
    return list (map (lambda x, y: x - y, lista1, lista2))

lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]

print (diferencia_listas (lista1, lista2))

# %%
# EJERCICIO 4-BIS. Genera una función que calcule la SUMA entre los valores de dos listas. SI UN VALOR SUPERA 40, LO DEVUELVE A 0. Usa la función MAP ()

def suma_listas (lista1, lista2):
    "Se puede incorporar un if dentro del lambda"
    return list (map (lambda x, y: x + y if x + y <= 40 else 0, lista1, lista2))
lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]

print (suma_listas (lista1, lista2))


# %%
# EJERCICIO 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
# una tupla que contenga la media y el estado.

notas = [6, 5, 5, 4, 5]
nota_corte = 5

def evaluar_nota (notas, nota_corte):
    suma = sum(notas)
    cantidad = len(notas)
    media = suma / cantidad
  
    if media >= nota_corte:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

print (evaluar_nota (notas, nota_corte))

# %%
# Cambiamos las notas para probar el otro caso

notas = [5, 4, 5, 4, 5]
nota_corte = 5

# %%
# la nueva nota es:
print (evaluar_nota (notas, nota_corte))

# %%
# EJERCICIO 6.  Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        "aqui está la versión recursiva, la llamada a la función dentro de sí misma"
        return n * factorial (n - 1)

# se llama a la función dentro del Print
print (factorial (5))

# otra forma es usar la librería math
import math
print (math.factorial (5))

# %%
# EJERCICIO 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usar la función MAP ()

# la sintaxis de las tuplas es con paréntesis
# la sintaxis de los strings es con comillas

lista_de_tuplas = [("Pepe", "Juan"), ("Peras", "Manzanas"), ("Alto", "Bajo")]
lista_de_strings = list (map (lambda x: ' '.join (x), lista_de_tuplas))
print (lista_de_strings)

# %%
# EJERCICIO 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
# indicando si la división fue exitosa o no.

def dividir_numeros ():
    try:
        num1 = float (input ("Introduce el primer número: "))
        num2 = float (input ("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        return "Error: Debes ingresar valores numéricos."
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    else:
        return f"La división fue exitosa. El resultado es: {resultado}"

print (dividir_numeros ())

# %%
# EJERCICIO 9. Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excuir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Usar la función FILTER ()

# Definimos la lista de exclusión
Lista_exclusión = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def filtrar_mascotas (lista_mascotas):
    "usamos la función filter y el método lambda para filtrar las mascotas, recorriendo la lista y excluyendo las que están en la lista de exclusión"
    return list (filter (lambda x: x not in Lista_exclusión, lista_mascotas))
# Probamos la llamada a la función imnprimiendo el resultado
print (filtrar_mascotas (["Perro", "Gato", "Tigre", "Loro", "Oso", "Hamster", "Mapache", "Leon"]))

# %%
# EJERCICIO 10. Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

números = [35, 42, 27, 50, 18]
lista_números = números

def promedio (números):
    if len(números) == 0:
        raise ValueError("La lista está vacía. No se puede calcular el promedio.")
    return sum(números) / len(números)

print (f"la lista de números es: {lista_números}")
print (f"el promedio es {promedio (lista_números)}")

# %%
# EJERCICIO 10-1. AHORA PROBAMOS LA EXCEPCIÓN PERSONALIZADA CON UNA LISTA VACÍA

números = []
lista_números = números

def promedio (números):
    if len(números) == 0:
        raise ValueError("La lista está vacía. No se puede calcular el promedio.")
    return sum(números) / len(números)

print (f"la lista de números es: {lista_números}")
print (f"el promedio es {promedio (lista_números)}")

# %%
# EJERCICIO 10-2. AHORA INTRODUCIMOS LOS NÚMEROS DE LA LISTA DESDE EL TECLADO

números = []
cantidad_números = int (input ("¿Cuántos números quieres introducir en la lista? "))

for i in range (cantidad_números):
    número = float (input (f"Introduce el número {i + 1}: "))
    números.append (número)

print (f"la lista de números es: {números}")
def promedio (números):
    if len(números) == 0:
        raise ValueError("La lista está vacía. No se puede calcular el promedio.")
    return sum(números) / len(números)

print (f"el promedio es {promedio (números)}")

# %%
# EJERCICIO 11.  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

edad_usuario = input ("Introduce tu edad: ")

try:
    edad = int (edad_usuario)
    if edad < 0 or edad > 120:
        raise ValueError ("La edad debe estar entre 0 y 120.")
except ValueError as ve:
    print (f"Error: {ve}")
else:
    print (f"Tienes {edad} años.")


# %%
# EJERCICIO 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usar la función MAP ()

def longitud_palabras (frase):
    "Separamos la frase en palabras usando split"
    palabras = frase.split()
    "Usamos map para aplicar la función len a cada palabra y devolver la longitud"
    return list (map (len, palabras))

frase = "Todos estos recuerdos se perderán como lágrimas en la lluvia, es hora de morir (Blade Runner)" # Los paréntesis son parte de la palabra, ojo.
print (longitud_palabras (frase))


# %%
# EJERCICIO 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
# Mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus (conjunto_caracteres):
    "Usamos set para eliminar las letras repetidas"
    conjunto_unico = set (conjunto_caracteres)
    "Usamos map para crear las tuplas de mayúsculas y minúsculas"
    return list (map (lambda x: (x.upper(), x.lower()), conjunto_unico))

conjunto_caracteres = "Costantinopla"
print (letras_mayus_minus (conjunto_caracteres))


# %%
# EJERCICIO 14. Crea una función que retome las palabras de una lista de palabras que comience con una letra en especifico. Usa la función FILTER ()

lista_de_palabras = ["Manzana", "Pera", "Plátano", "Melocotón", "Mango", "Cereza", "Papaya"]
print (lista_de_palabras[1:6])
filtered_words1 = list (filter (lambda x: x.startswith ("P"), lista_de_palabras))
print (filtered_words1)


# %%
# EJERCICIO 14-1. Ahora con map ()

def filter_map (lista_de_palabras):
    return list (map (lambda x: x if x.startswith ("P") else None, lista_de_palabras))
print (lista_de_palabras)
lista_con_none=filter_map (lista_de_palabras)
print (lista_con_none)

# Ahora defino una función para elimnar los None de la lista pero sin utilizar filter

def eliminar_none (lista_con_none):
    lista_sin_none = []
    for item in lista_con_none:
        if item != None:
            lista_sin_none.append(item)
    return lista_sin_none

print (eliminar_none (lista_con_none))


# %%
#EJERCICIO 15. Crea una función lambda que  sume 3 a cada número de una lista dada
lista_números = [1, 2, 3, 4, 5]
def suma_tres (lista_números):
    return list (map (lambda x: x + 3, lista_números))
print (suma_tres (lista_números))


# %%
#EJERCICIO 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
#todas las palabras que sean más largas que n. Usa la función FILTER ()

cadena_de_texto = "El rápido zorro marrón salta sobre el perro perezoso"
n = 4

######## Pruebas previas
# palabras = cadena_de_texto.split()
# print (palabras)
# palabras_largas = list (filter (lambda x: len(x) > n, palabras))
# print (palabras_largas)

def palabras_mas_largas (cadena_de_texto, n):
    palabras = cadena_de_texto.split()
    return list (filter (lambda x: len(x) > n, palabras))

print (palabras_mas_largas (cadena_de_texto, n))

# %%
# EJERCICIO 17. Crea una función que tome una lista de dígigos y devuelva el número correspondiente. Por ejemplo, 5,7,2 
# corresponde al número quinientos setenta y dos 572. Usa la función reduce()

from functools import reduce


######## Pruebas previas
# lista_de_digitos = [5, 7, 2]
# número = reduce (lambda x, y: str(x) + str(y), lista_de_digitos)         
# print (número)

def lista_a_número (lista_de_digitos):
    return int (reduce (lambda x, y: str(x) + str(y), lista_de_digitos))
lista_de_digitos = [5, 7, 2, 45, 32]
print (lista_a_número (lista_de_digitos))

# %%
#EJERCICIO 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
#90. Usa la función filter()

# Primero ver cómo funciona una lista de diccionarios

alumnos = [ {"nombre": "Ana", "edad": 20, "calificación": 95},
            {"nombre": "Luis", "edad": 22, "calificación": 85},
            {"nombre": "Marta", "edad": 19, "calificación": 92},
            {"nombre": "Carlos", "edad": 21, "calificación": 78}]

print (alumnos[0])  # Imprime el primer diccionario
print (alumnos[0]["nombre"])  # Imprime el nombre del primer estudiante

def estudiantes_aprobados (alumnos):
    return list (filter (lambda x: x["calificación"] >= 90, alumnos))
print (estudiantes_aprobados (alumnos))


# %%
#EJERCICIO 19. Crea una función lambda que filtre los números impares de una lista dada. 

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

######## Pruebas previas
# numeros_impares = list (filter (lambda x: x % 2 != 0, lista_numeros))
# print (numeros_impares)

def filter_impares (lista_numeros):
    return list (filter (lambda x: x % 2 != 0, lista_numeros))
print (filter_impares (lista_numeros))

# %%
# EJERCICIO 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
# filter()

lista_elementos = [1, "dos", 3, "cuatro", 5, "seis"]

def filtrar_elementos_int (lista_elementos):
    return list (filter (lambda x: isinstance(x, int), lista_elementos))
print (filtrar_elementos_int (lista_elementos))

# ahora hacemos lo mismo pero con str

def filtrar_elementos_str (lista_elementos):
    return list (filter (lambda x: isinstance(x, str), lista_elementos))
print (filtrar_elementos_str (lista_elementos))

# %%
# EJERCICIO 21. Crea una función que calcule el cubo de un número dado MEDIANTE LA FUNCIÓN LAMBDA

número = 3
cubo = lambda x: x ** 3
print (cubo (número))

# %%
# EJERCICIO 22. DADA una lista numérica, obtener el producto total de valores de dicha lista, usando la función reduce ()
# Pruebas previas
from functools import reduce

lista_números = [1, 2, 3, 4, 5]
producto_total = int (reduce(lambda x, y: x * y, lista_números))
print (producto_total)

# %%
# EJERCICIO 23. CONCATENA UNA LISTA DE PALABRAS, USANDO LA FUNCIÓN REDUCE ()
from functools import reduce
Lista_palabras = ["Ahora", "estoy", "aquí", "y", "mañana", "allí"]
# la función lambda recorre la lista y cuenta con 3 agrumentos: (qué variables, qué se hace con ellas y dónde se aplica)
frase_concatenada = reduce (lambda x, y: x + ' ' + y, Lista_palabras)
print (frase_concatenada)

# %%
# EJERCICIO 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce ()
# Entendemos como tal el cálculo de las diferencias sucesivas tomando como restandos 2 a 2
from functools import reduce
lista_números = [20, 5, 15, 100]
diferencia_total = int (reduce (lambda x, y: x - y, lista_números))
print (diferencia_total)

# %%
# EJERCICIO 25. Crea una función que cuente el número de caracteres en una cadena de texto dada

# Pruebas Previas
cadena_texto = "Hola, ¿cómo estás?"
length_cadena = len (cadena_texto)
print ( length_cadena )

# Ahora la función
def contar_caracteres (cadena_texto):
    return len (cadena_texto)
print (contar_caracteres (cadena_texto))

# %%
# EJERCICIO 26. Crea una función lambda que calcule el resto de la división entre dos números dados

número1 = 10
número2 = 3

resto_división = lambda x, y: x % y
print (resto_división (número1, número2))


# %%
#EJERCICIO 27. Crea una función que calcule el promedio de una lsita de números

números = [35, 42, 27, 50, 18]
def promedio (números):
    return sum(números) / len(números)
print (promedio(números))

# %%
#EJERCICIO 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada. 

lista_elementos = [1, 2, 3, 4, 2, 5, 3]
sets = set (lista_elementos)
print (sets)

def primer_duplicado (lista_elementos):
    vistos = set()
    for elemento in lista_elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # Si no hay duplicados

print (primer_duplicado (lista_elementos))


# %%
# EJERCICIO 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro. 
# Por ejemplo, utilziamos los 16 digitos de una tarjeta de crédito "1234567812345678" y el resultado sería "############5678".

tarjeta = 1234567812345678
tarjeta_str = str (tarjeta)
print (tarjeta_str)
 
for i in range (len(tarjeta_str) - 4):
    tarjeta_str = tarjeta_str.replace (tarjeta_str[i], '#', 1)
print (tarjeta_str)


# %%
#EJERCICIO 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

palabra_1="primark"
palabra_2="krampri"

def anagramas (palabra_1, palabra_2):
    set_1= set (palabra_1)
    set_2= set (palabra_2)
    "transformamos las palabras en sets para eliminar letras repetidas y comparar"
    if set_1 == set_2:
        return print ("Son anagramas") 
    else:
         return print ("No son anagramas")

anagramas (palabra_1, palabra_2)

# %%
#EJERCICIO 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
# lanza una excepción. Hay que quitar los espacios antes y después de las comas al introducir la lista de nombres.

def buscar_nombre_en_lista ():
    lista_nombres = input ("Introduce una lista de nombres separados por comas: ").split (',')
    lista_nombres_limpia = [nombre.strip() for nombre in lista_nombres]
    lista_nombres = lista_nombres_limpia
    nombre_a_buscar = input ("Introduce el nombre a buscar en la lista: ")
    
    if nombre_a_buscar in lista_nombres: 
        return print (f"el nombre {nombre_a_buscar} esta en la lista")
    else:
        raise ValueError(f"{nombre_a_buscar} no está en la lista: {lista_nombres}")           


# %%
#EJERCICIO 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
#no trabaja aquí.

def obtener_puesto(nombre_completo: str, empleados: list[dict]):
    nombre_completo = nombre_completo.strip()

    for emp in empleados:
        if emp.get("nombre", "").strip() == nombre_completo:
            return emp.get("puesto", "Puesto no disponible")

    return f"{nombre_completo} no trabaja aquí"

empleados = [
    {"nombre": "Ana García", "puesto": "Analista"},
    {"nombre": "Luis Pérez", "puesto": "Desarrollador"},
]

print(obtener_puesto("Luis Pérez", empleados))      # Desarrollador
print(obtener_puesto("Marta López", empleados))     # Marta López no trabaja aquí


# %%
# EJERCICIO 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista_1 = [10,20,30,40,50]
lista_2 = [50,40,30,20,10]

def suma_listas (lista_1, lista_2):
    return list (map (lambda x, y: x + y, lista_1, lista_2))

print (suma_listas (lista_1, lista_2))  # return [60, 60, 60, 60, 60]

# %%
# EJERCICIO 34. Crea la clase de objetos 'ARBOL', define un árbol genérico con un tronco y ramas como atributos. 
# Los métodos disponibles son: Crecer Tronco, Nueva Rama, Crecer Ramas, Quitar Rama e Info_arbol. El objetivo es implementar estos 
# métodos para manipular la estructura del árbol.

class ARBOL:
     def __init__(self, tronco, ramas):
        if tronco < 0:
            raise ValueError("El tronco no puede ser negativo.")
        self.tronco: int = int(tronco)
        self.ramas: list[int] = list(ramas) if ramas is not None else []

        if any(r < 0 for r in self.ramas):
            raise ValueError("Las ramas no pueden tener longitudes negativas.")
        
     # Método 2 - Crecer el Tronco   
     def crecer_tronco(self):
        self.tronco += 1

     # Método 3 - Nueva Rama para añadir Ramas
     def anadir_rama(self):
        self.ramas.append(1)

     # Método 4 - Crecer ramas para aumentar en una unidad la longitud de todas las ramas existentes.
     def crecer_ramas(self,long_ramas):
       self.ramas = [r+long_ramas for r in self.ramas]
   
    # Método 5 - Quitar una rama de una posición específica.
     def quitar_rama(self, posicion):
       if posicion < 0 or posicion >= len(self.ramas):
          raise IndexError("Posición de rama fuera de rango.")
       return self.ramas.pop(posicion)  

    # Método 5 - Dar la información de la longitud del tronco, número de ramas y longitudes de las mismas, de forma estructurada.
     def info_arbol(self):
       print(f"Longitud del Tronco {arbol.tronco} m")
       print(f"Número de ramas {len(self.ramas)}")
       print(f"Longitud de las ramas {self.ramas} m")



# %%
# EJERCICIO 35 - 1. Check y caso de Uso ARBOL

# 1. Crear un árbol. 2. Hacer crecer el tronco del árbol una unidad. 3. Añadir una nueva rama al árbol. 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol. 6. Retirar la rama situada en la posición 2. 7. Obtener información sobre el árbol

arbol=ARBOL (tronco=1, ramas=[])
arbol.crecer_tronco()
arbol.anadir_rama()
arbol.anadir_rama()
arbol.anadir_rama()
arbol.crecer_ramas(1)
arbol.anadir_rama()
arbol.quitar_rama(1)
arbol.info_arbol()



# %%
# EJERCICIO 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, 
# transferir dinero desde otro usuario y agregar dinero al saldo. 

class UsuarioBanco:
     def __init__(self, saldo, cuenta_corriente):    
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self.saldo: float = float(tronco)
        self.cuenta_corriente: bool = bool (cuenta_corriente) 

print ()


# %%
# EJERCICIO 36 -1 CASO DE USO BANCO

class UsuarioBanco: 
    def __init__(self, nombre, saldo, cc):
        if saldo < 0:
          raise ValueError("El saldo NO PUEDE SER NEGATIVO")
        self.nombre = str (nombre)
        self.saldo = int(saldo)
        self.cc = bool(cc) 

    # Método 2 - Retirar Dinero
    def retirar_dinero(self, cuantia):
        self.saldo_restante=self.saldo-cuantia
        print (f"La posición inicial de {self.nombre} es {self.saldo}")
        print (f"La posición inicial de {self.nombre} es {self.saldo_restante}")
        self.saldo=self.saldo_restante

    # Método 3 - Aportar Dinero
    def retirar_dinero(self, cuantia):
        self.saldo_restante=self.saldo-cuantia
        print (f"La posición inicial de {self.nombre} es {self.saldo}")
        print (f"La posición inicial de {self.nombre} es {self.saldo_restante}")
        self.saldo=self.saldo_restante

    

# Método 1 - Inicializar y Probar

Usuario1=UsuarioBanco("Alicia", 100, True)
Usuario2=UsuarioBanco("Bob", 50, True)
print(Usuario1.nombre, Usuario1.saldo, Usuario1.cc)
print(Usuario2.nombre, Usuario2.saldo, Usuario2.cc)
Usuario1.retirar_dinero(50)


# %%
# EJERCICIO 37 - CREA una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, 
# eliminar palabra. Estas opciones son otras funciones que tenemso que definir primero y llamar dentro de la función procesar_texto. 

# Ejercicio 37-1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario. 

def contar_palabras(lista):
    dicc={}
    for p in lista:
        dicc[p] = dicc.get(p,0) + 1
    return dicc  

# Ejercicio 37-2. Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva. 
# Tiene que devolver el texto con el reemplazo de palabras

def reemplazar_palabras(texto,reemplazo, reemplazar): 
    lista = texto.split()
    lista1=list(map(lambda s: reemplazo if s == reemplazar else s, lista))
    texto1=" ".join(lista1)
    return texto1
   
# Ejercicio 37-3. Eliminar_palabras. para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada. 
# Utilizamos la palabra de reemplazo anterior.

def eliminar_palabras (texto, eliminar):
    lista= texto.split()
    lista1=list(map(lambda s: "" if s == eliminar else s, lista))
    lista2=list(filter(None, lista1))
    texto2=" ".join(lista2)
    return texto2

# Ejercicio 37-4. Crear la función procesar_terxto que tome un texto, una opción entre "contar", "reemplazar", "eliminar"
# y un número de argumentos variable según la opción indicada.

def procesar_texto() :
    texto = input("Introduce el texto: ")

    print("\nElige una opción:")
    print("1) contar")
    print("2) reemplazar")
    print("3) eliminar")
    opcion = input("Opción (1/2/3): ").strip()
    dicc={}

    if opcion == "1":
        # Contar palabras
        dicc=contar_palabras (texto.split())
        print("Recuento de palabras:", dicc)

    elif opcion == "2":
        # Reemplazar palabra
        palabra_original = input("Palabra a reemplazar: ").strip()
        palabra_nueva = input("Palabra nueva: ").strip()
        texto_resultado = reemplazar_palabras(texto, palabra_nueva, palabra_original)
        print("Texto resultante:", texto_resultado)

    elif opcion == "3":
        # Eliminar palabra
        palabra_eliminar = input("Palabra a eliminar: ").strip()
        texto_resultado = eliminar_palabras(texto, palabra_eliminar)
        print("Texto resultante:", texto_resultado)

    else:
        raise ValueError("Opción no válida. Debe ser 1, 2 o 3.")


# %%
# EJERCICIO 37-5 Caso de Uso. Comprobación de la función. 

procesar_texto()

# %%
# EJERCICIO 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario
# Consideramos el dia/mañana entre 06:00 y 11:59, tarde desde las 12:00 - 19:59,  noche 20:00 - 5:59. 

from datetime import datetime

def momento_dia():

    hora= int(input ("Introduce la hora (0-24): ").strip())

    # Creamos un objeto time con la hora
    ahora = datetime.now().replace(hour=hora, minute=0, second=0, microsecond=0)
    print("La hora es: ", ahora.hour)

    h = ahora.hour
    if 6 <= h < 12:
        print("Es de día (mañana).")
    elif 12 <= h < 20:
        print("Es tarde.")
    else:
        print("Es de noche.")

momento_dia()


# %%
# EJERCICIO 39. Escribe un Programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son (0-69) - Suficiente, 
# (70-79) Bien, (80-89) Muy Bien, (90-100) Excelente. 



# %%
# EJERCICIO 40 Escribe una función QUE TOME dos parámetros: figura (cadena qeu puede ser "rectángulo", "círculo", "triángulo") y datos 
# (una tupla con los datos necesarios para calcular el área de la figura)

def areas():

   while True:
   
    figura = int(input ("Introduce la puntuación >=0:"))
  
    if puntuación <0:
        print ("La puntuación no puede ser menor que 0")
        continue
    if puntuación >100:
        print ("La puntuación no puede ser mayor que 100")
        continue

    if 0 <= puntuación <=69:
        calificación = "Insuficiente"
    elif 70 <= puntuación <= 79:
        calificación = "Bien"
    elif 80 <= puntuación <= 89:
        calificación = "Muy Bien"
    else:  
        calificación = "Excelente" 
       
    print (calificación)
    return calificación

notas()

# %%
# EJERCICIO 40. 
# scribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo") y datos 
# (una tupla con los datos necesarios para calcular el área de la figura).

# def area_rectangulo (base, altura):
#    return area_r=base,altura

def area_rectangulo (base, altura):
    return base * altura

def area_triangulo (base, altura):
    return base * altura / 2

def area_circulo (radio):
    import math
    radio=float (radio)
    return math.pi * (radio ** 2)

def area_poligono () :

    while True:
        print("\nElige una opción:")
        print("1) rectángulo")
        print("2) triangulo")
        print("3) circulo")
        
        try:
            opcion = int(input("Opción (1/2/3): "))
            if opcion not in (1, 2, 3):
                raise ValueError("Opción no válida. Debe ser 1, 2 o 3.")
            break
        except ValueError as e:
            print("Error:", e)

    if opcion == 1:
        # rectángulo
        base= float(input("Introduce la base del rectángulo"))
        altura= float(input("Introduce la altura del rectángulo"))
        tupla_formulas=(base,altura)
        print (area_rectangulo(tupla_formulas[0], tupla_formulas[1]))

    elif opcion == 2:
        base= float(input("Introduce la base del triangulo"))
        altura= float(input("Introduce la altura del triangulo"))
        tupla_formulas=(base,altura)
        print (area_triangulo(tupla_formulas[0], tupla_formulas[1]))

    else: 
        rad= float(input("Introduce el radio del circulo"))
        tupla_formulas=(rad,)
        print (area_circulo(tupla_formulas[0]))
   

area_poligono()

# %%
# EJERCICIO 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, 
# después de aplicar un descuento. Utilizar estructuras de control de flujo como if, elif y else. El programa debe hacer lo siguiente:
    # 1. Solicita al usuario que ingrese el precio original de un artículo.
    # 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    # 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    # 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
    # 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 

def descuento () :

    while True:
        try:
            precio = float(input("Introduce el precio del artículo: ").strip())
            if precio <0:
                raise ValueError ("El precio no puede ser negativo.")
            break  # es número -> salimos del bucle
        except ValueError as e:
            print("Error:", e)

    while True:
        print ("Tienes cupon de descuento?")
        print("1) Si")
        print("2) No")
        try:
            opcion = int(input("Opción (1/2): "))
            if opcion not in (1, 2):
                raise ValueError("Opción no válida. Debe ser 1 o 2.")
            
            if opcion == 1 :
                while True:
                    try:
                        descuento = float(input("Introduce el descuento del artículo (mayor que 0): ").strip())
                        if descuento < 0:
                            raise ValueError ("El descuento no puede ser menor que 0.")
                        if descuento > precio: 
                            raise ValueError ("El descuento no puede ser mayor que el precio")
                        valor_articulo=precio-descuento
                        break
                    except ValueError as e:
                        print("Error:", e)
            else: 
                descuento=0
                valor_articulo=precio
            break
        except ValueError as e:
            print("Error:", e)
       
    return print(f"el precio del articulo es {precio}, el descuento es de {descuento}, con lo que el precio final es {valor_articulo}")

descuento()


