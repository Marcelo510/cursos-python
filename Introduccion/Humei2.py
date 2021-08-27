### Pequeño Repaso

for i in range(1, 10):
    if i % 2 == 0:
        print(f"El número {i} es par")

## Control de flujo


base = {
    1: {"nombre":"Fernanda",
        "apellido":"Fernandez",
        "dni":333333331},
    2: {"nombre":"Gonzalo",
        "apellido":"Gonzalez",
        "dni":333333332},
    3: {"nombre":"Rodrigo",
        "apellido":"Rodriguez",
        "dni":333333333}
    }



dnis = [333333331, 333333336, 333333339, 333333332, None, 333333333]

n_encontrados = 0

for dni in dnis: # itero por todos los dnis

    if type(dni) == int: # si el tipo es entero
        dni_encontrado = False # inicializo una variable con valor False, ya van a ver para qué :-)
        
        # Ahora viene la parte complicada, ¿cómo sé si ese dni ya está en mi base?
        # 1- Recordemos que base es un diccionario y como tal tiene el método items(), pruébenlo afuera de esta celda
        # me devuelve una tupla, con la llave en el primer elemento y el valor en el segundo
        
        # itero por todos los elementos
        for i in base.items(): 
            valor = i[1] # guardo el valor en una variable
            if dni == valor["dni"]: # si el dni es el mismo que estoy buscando...
                dni_encontrado = True
                nombre_completo = valor["nombre"] + " " + valor["apellido"]
                n_encontrados += 1 # esto equivale a encontrados = encontrados + 1, agrega uno
                break # freno la búsqueda, ésto evita que siga buscando

        if dni_encontrado: # entra acá si es True
            print(f"{nombre_completo.title()} ingreso a nuestra web")

        elif not dni_encontrado: # noten el not
            print(f'El dni {dni} no se encuentra en la base...')
            continue # sigo con la búsqueda, NO paso a la siguiente línea
            
        print(f"Hasta el momento se encontraron {n_encontrados} casos")
    
    else:
        pass # si dni no es un entero entonces no hacemos nada, suponemos que hubo algún tipo de error

## Tuplas 



registro = ('Argentina', 112000, 'Bariloche')



registro[0] 

#### Unpacking



pais, poblacion, ciudad = registro

print("País:", pais)
print("Población:", poblacion)
print("Ciudad:", ciudad)

registros = [registro, ('Brasil', 477000, 'Florianópolis')]
registros[1]



# Una lista sí se puede modificar
lista = [1, 2, 3]

lista[0] = 4

lista



print(registro)
# registro[0] = 'Chile'

# tampoco se puede borrar ninguno de sus elementos
# del registro[0]

## Tipos de errores

# En el ejemplo de arriba vimos una pantalla de error. El **traceback** o **stack trace** nos muestra el camino del error: veremos más adelante que cuando tenemos funciones anidadas, vemos aquí como el error se propaga. 

# Las cosas a las que en principio les debemos prestar atención son:

#    1. El nombre del error, en este caso **TypeError**
#    2. La explicación dada en el último renglón: "'tuple' object doesn't support item deletion"
#    3. La flecha que nos indica la línea en la que ocurrió el error

# Existen distintos tipos de errores en Python, pueden consultar la lista de todas las excepciones básicas acá:
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions

# Sin embargo, las excepciones más frecuentes son:

# **AttributeError**: cuando tratamos de llamar a una referencia que no existe.

# **NameError**: cuando se llama a una variable u otro nombre que no está definido en el ambiente en que estamos trabajando.

# **KeyError**: cuando queremos llamar a una llave que no existe, por ejemplo, en un diccionario.

# **SyntaxError**: cuando hay un problema de sintaxis, errores muy comunes al comienzo pueden ser que no se cerró una llave o corchete, que falta alguna coma o dos puntos.

# **TypeError**: cuando el tipo de soporta una determinada operación.

# **IndexError**: cuando el índice al que se quiere acceder no existe, generalmente debido a que se llama a un índice mayor al largo de la lista.

# Veamos algunos ejemplos:

print(base) # recordamos base

# base['Gertrudis']

### Ejercicios

# Prueben y arreglen los siguientes errores de código:




a = 5
b = "3"
# a + b == 8



a = ["the beatles", "the rolling stones", "queen", "led zepellin"]

# print(a[4])

# a.appended(["cream"])

## Manejo de errores

# Para anticipar y manejar los errores, podemos usar la clausula **try** y **except**

#a = '20'
#b = 5

#try:
#    print(a+b)
#except:
#    print(int(a)+int(b)) # convierto a int ambas variables

## Si queremos ver qué excepción ocurrió, podemos usar la siguiente sintáxis:

#try:
#    print(a+b)
#except Exception as e:
#    print(f"El error fue {e}")

# También podemos especificar qué hacer para distintos tipos de error:

lista_tuplas = [('3', 8), 
                (5, 0), 
                (3, ), 
                (4, 6)]

for t in lista_tuplas:
    print(f"la tupla es {t}")
    
    try:
        print("intento dividir...")
        print(t[0] / t[1])
        print("éxito!")
    except IndexError as a:
        print(f'El largo está mal {a}')
    except TypeError:
        print('Error en el tipo de datos')
    except ZeroDivisionError:
        print("No se puede dividir por cero")

# Listas por comprensión (List Comprehension)

# Las **listas por comprensión** son una funcionalidad muy flexible de Python que permite crear listas de un modo más "descriptivo", basandose en la notación de definición de conjuntos.

# Supongamos que necesitamos obtener una lista con los elementos de una lista original elevados al cuadrado.

# Sin listas por comprensión haríamos...

lista = [1,2,3,4,5]

cuadrados = []

for x in lista:
    cuadrados.append(x**2)
    
cuadrados

# En cambio, con listas por comprensión usamos esta expresión:

cuadrados = [x**2 for x in lista]
cuadrados

# En las listas por comprensión también podemos incluir condicionales en una sola línea, vean la siguiente expresión:

x = 10
print(x if x > 15 else 0)

x = 16
print(x if x > 15 else 0)

# Ahora vamos a generar una lista por comprensión sólo con los números donde el cuadrado sea menor a 15

cuadrados = [x**2 for x in lista if x**2 < 15]
cuadrados

# La sintáxis para **filtrar** con condicionales es

# > [ (elemento) ( for x in (iterable) ) ( if condicion ) ]

# Donde "elemento" es lo que vayamos a guardar en la lista. Incluyendo un **else**:

# > [ (elemento) (if condicion else otro_elemento) ( for x in (iterable) ) ]

# Pueden hacerse loops anidados:

# > [i for i in range(x) for j in range(y)]

# Otra forma de pensar la sintaxis es a partir de teoría de conjuntos. Por ejemplo:
# Un conjunto S definido por todos los números X / 4 que pertenecen a los Naturales y cumplen que su cuadrado es menor a 20

# $$S=\{\,\frac{x}{4}\mid x \in \mathbb{N},\ x^2<60\,\}$$

# Con un loop for:

S = []

for x in range(1000):
    if x ** 2 < 60:
        S.append(x/4)
S

# Con listas por comprensión:

S = [x/4 for x in range(1000) if x**2 < 60]
S



for x in range(3):
    for y in 'abc':
        print(x,y)

[(x, y) for x in range(3) for y in 'abc']

# O comprensiones anidadas:

# > [ [i for i in range(x) ] for j in range(y) ]

[[l*n for l in 'abc'] for n in range(3)]

# Además, el elemento que se genera puede ser de otro tipo, en este caso una tupla:

animales = ['mantarraya', 'pandas', 'narval', 'unicornio']

[(a, len(a)) for a in animales]

### Ejercicios

# 1- Dado el siguiente grupo de palabras, crear otra lista que contenga sólo la primera letra de cada una

lista = ['a','ante','bajo','cabe','con']
print([(x[0]) for x in lista])

# 2- Dada la siguiente frase, crear una lista con el largo de cada palabra.
# Tip: Antes de aplicar listas por comprensión pueden usar la función split que vimos la clase pasada y la función replace para remover la puntuación.

frase = 'Cambiar el mundo, amigo Sancho, no es ni utopía ni locura, es justicia'
print([(len(x)) for x in frase.replace(',', '').split()])

# I/O

# Ahora veremos como abrir archivos usando Python base. Para hacerlo usaremos la sentencia **with** para definir un **contexto** del siguiente modo:

# with open('C:\Users\Marcelo\source\Python\CursoHumai\cursos-python\Introduccion\corpus.txt', 'r') as inp:
#     string_contenido = inp.read()
    
# Lo que significa: con el archivo "corpus.txt" abierto en **modo** lectura ("r" de read) con el **alias** _inp_, definimos la variable contenido usando el método **.read()** para leer el archivo. Algunas aclaraciones:

# - El método .read() es propio del objeto de input, que **en esta ocasión** llamamos _inp_. Otro método útil es **.readlines()** que nos permite iterar por renglones.
# - La ruta al archivo puede ser **relativa** como en este caso, donde el archivo se encontraría en la misma carpeta que la notebook. También se puede dar el path completo, como podría ser "C:/Usuarios/Matías/Documentos/corpus.txt"

# Existen varios modos de abrir un archivo, incluyendo:

#     - r: read, lectura
#     - w: write, escritura
#     - a: append, agregar al final del archivo
   
# Por ejemplo, para escribir en un archivo, haríamos:

# with open(outpath, 'w') as f:
#     f.write(string)

with open('nuevo.txt', 'w') as f:
    f.write('ejemplo de escritura 2aa')

with open('nuevo.txt', 'r') as f:
    contenido = f.read()

print(contenido)

# En Python se puede pedir un input del usuario de la siguiente manera:


while True:
    usuario_dijo = input('Ingrese un numero')

    try:
        num = int(usuario_dijo)
        break
    except:
        print('No anduvo, intente de nuevo')

print(f'Su numero fue {num}! :D')

# Funciones

# Las funciones nos permiten estandarizar y reutilizar un proceso en múltiples ocasiones.

# Como patrón de diseño, las funciones tienen que ser lo más atómicas posibles, es decir, resolver un problema lo más pequeño posible y bien definido.

# Los nombres también son importantes, el nombre de la función tiene que reflejar lo mejor posible lo que hace. 


# Las funciones se definen de la siguiente manera:

def nombre_de_funcion(argumentos):
    """docstring opcional"""
    resultado = procedimiento(argumentos)
    return resultado
        
# Las variables definidias en el contexto de una función son locales, es decir, sólo viven dentro de esa función. Por otra parte, si desde una función se llama a una variable que no está definida en la función tratará de buscarla afuera. En general, es buena práctica usar sólo variables definidas dentro de la función o argumentos.

# Los argumentos son variables que le pasamos a la función para que *haga algo*.

# Las funciones emplean dos términos reservados:

# - def: que indica el comienzo de la definición de la función

# - return: establece la variable o variables que devuelve la función

# En este punto vale la pena mencionar que en Python los nombres (de variables, funciones, etc.) se almacenan y ordenan en NameSpaces. En este punto, la información definida dentro de la función no es compartida con el exterior de la función (salvo algunas excepciones que no vienen al caso), por lo tanto, para compartirla, la función debe enviar desde el NameSpace local (el de la función) al NameSpace global (donde está el resto del programa). Para ello, el término return indica qué se devolverá al ambiente global. Para que efectivamente esa/s variable/s que la función devuelve se guarden una variable en el ambiente global debemos asignar el resultado a una variable. Esto va a quedar más claro con el código.

# Por último, vale la pena mencionar que *print* sólo nos muestra el contenido de una variable pero no envía la información desde la función hacia afuera.

def promedio(lista):
    return sum(lista) / len(lista)

resultado = promedio([0,1,2,3]) # asigno el resultado
print(resultado)

def suma(a,b):
    """Esta función recibe dos numeros y devuelve la suma"""
    return a+b

r = suma(3,5) # asigno el resultado
print(r)

def rango(lista):
    return max(lista) - min(lista)

lista = [89, -24, 9, 2]
rango(lista)

### Ejercicios: 

# 1- Escribir una función que reciba una lista con números y devuelva la suma de todos los pares

# 2- Escribir una función que tome una lista con distintos elementos (de cualquier tipo) y devuelva una lista sólo con los últimos tres números que aparecen.

# En las funciones existen argumentos se pueden pasar por posición o por su nombre. Algunos de los argumentos tienen un valor por default.

def unir_lista(lista, conector=' '):
    """Esta funcion recibe dos argumentos, una lista y un conector
    y devuelve la lista unida usando el conector."""
    
    unida = conector.join([str(e) for e in lista])
    
    return unida

unir_lista(['unir',3,'cosas'])

unir_lista(['probando', 'unir', 'lista', 123], conector = ',')

# Lo que no podemos hacer es pasar el argumento nombrado antes de el o los posicionales

# unir_lista(conector = ',',['probando', 'unir', 'lista', 123])

# Cuando uso los argumentos por su nombre, puedo pasarlos en cualquier orden

# unir_lista(conector = ',',lista = ['probando', 'unir', 'lista', 123])

# Existen distintos tipos de argumentos, principalmente los llamados "args" y "kwargs", o argumentos y "keyword arguments" es decir argumentos nombrados. 

# También podemos tener un numero variable de argumentos, usando el symbolo *, por conveción al parámetro se le llama 'args'

# Internamente, los elementos de *args se tratan como una tupla

def suma_todos(*args):
    print(type(args))
    return sum(args)

suma_todos(9,1,4,2,9)

# En cambio los elementos de **kwargs se tratan como un diccionario

def consulta(**kwargs):
    print(type(kwargs))
    texto = f"Su consulta es {kwargs['fecha']} a las {kwargs['hora']}"
    return texto

consulta(fecha='hoy',hora='4PM')

# Finalmente, podemos juntar todo lo visto en una misma función, es decir, tener argumentos sin nombre sin valor default, argumentos con valores default, args y kwargs. Esto es especialmente útil cuando necesitamos enviar args o kwargs a otras funciones usadas dentro de una función.

valor_consulta = {"consulta":10, "arreglos_caries":20, "flúor":15}

costos = list(valor_consulta.values())
costos

def emitir_factura(nombre, dni, tipo="DNI", *args, **kwargs):
    factura = ""
    factura += f"Gracias por su visita Nombre:{nombre} \n"
    factura += f"{tipo} {dni} \n"
    costo = suma_todos(*args) # hago unpacking de args
    factura += f"El costo es {costo} \n"
    factura += consulta(**kwargs) # hago unpacking de kwargs
    return factura

factura = emitir_factura("Obi Wan", 370310455, "DNI", *costos, fecha="hoy", hora="5PM")

print(factura)

