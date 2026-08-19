"""
MODULO 1 - Fundamentos de Python
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo de este modulo: repasar variables, tipos de datos, operadores,
condicionales, ciclos y funciones -- todo lo que usaras como "ladrillos"
para construir el sudoku solver.

Como usar este archivo:
    Ejecutalo directo con:  python 01_fundamentos_python.py
    Cada seccion imprime resultados en consola para que veas el
    comportamiento real, no solo la teoria. Lee los comentarios primero,
    luego mira que imprime cada bloque.
"""


# =====================================================================
# 1.1 Variables y tipos de datos
# =====================================================================
# En Python no declaras el tipo explicitamente; se infiere del valor.

def seccion_1_1():
    numero = 5             # int
    texto = "hola"          # str
    decimal = 3.14           # float
    es_valido = True          # bool

    print("numero:", numero, type(numero))
    print("texto:", texto, type(texto))
    print("decimal:", decimal, type(decimal))
    print("es_valido:", es_valido, type(es_valido))

    # Para este ejercicio usaras casi exclusivamente int, str y bool.

    # Conversion entre tipos: la usaras constantemente al leer el
    # archivo de texto del puzle.
    texto_numero = "7"
    numero_convertido = int(texto_numero)
    de_vuelta_a_texto = str(numero_convertido)
    print("int('7') ->", numero_convertido, type(numero_convertido))
    print("str(7) ->", repr(de_vuelta_a_texto), type(de_vuelta_a_texto))

    # Detalle clave: convertir un string de UN SOLO caracter te da el
    # numero que representa. Esto es exactamente lo que haras para
    # transformar "030000040" en una lista de enteros.
    print("int('0') ->", int("0"))
    print("int('9') ->", int("9"))


# =====================================================================
# 1.2 Operadores relevantes
# =====================================================================
# ==, !=, in, not in, %  (modulo/resto), //  (division entera)
#
# Los dos ultimos son CRUCIALES para el sudoku: sirven para saber en
# que "caja" 3x3 esta una celda, y para separar visualmente filas y
# columnas cada 3 elementos al imprimir el tablero.

def seccion_1_2():
    fila = [0, 3, 0, 0, 0, 0, 0, 4, 0]

    print("3 in fila ->", 3 in fila)
    print("5 in fila ->", 5 in fila)
    print("5 not in fila ->", 5 not in fila)

    # // y % -- piensa en // como "cuantos grupos completos de 3 caben"
    # y en % como "cuanto sobra".
    for n in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print(f"{n} // 3 = {n // 3}   |   {n} % 3 = {n % 3}")


# =====================================================================
# 1.3 Estructuras condicionales
# =====================================================================

def clasificar_celda(numero):
    """Ejemplo de if/elif/else combinados con and/or/not."""
    if numero == 0:
        return "celda vacia"
    elif numero > 9:
        return "numero invalido"
    elif 1 <= numero <= 9:
        return "celda ocupada con un digito valido"
    else:
        return "caso raro (numero negativo)"


def seccion_1_3():
    for n in [0, 5, 9, 12, -1]:
        print(f"clasificar_celda({n}) -> {clasificar_celda(n)}")


# =====================================================================
# 1.4 Ciclos: for y while
# =====================================================================

def seccion_1_4():
    # for -- cuando sabes cuantas veces vas a iterar (o sobre que
    # coleccion). Lo usaras para recorrer las 9 filas, columnas, y
    # las 9 posibilidades (1-9) al resolver el sudoku.
    print("range(9) ->", list(range(9)))         # 0..8  (9 elementos)
    print("range(1, 10) ->", list(range(1, 10)))  # 1..9  (para probar digitos)

    # Ojo: range(9) NO incluye el 9. Como los indices de listas parten
    # en 0, esto calza perfecto con una grilla de 9 elementos.

    # while -- cuando no sabes de antemano cuantas iteraciones
    # necesitas, o quieres repetir "hasta que algo se cumpla".
    # Ejemplo simulado (sin pedir input real, para que el demo corra solo):
    entradas_simuladas = ["hola", "12", "abc", "3"]
    i = 0
    numero_valido = None
    while numero_valido is None and i < len(entradas_simuladas):
        candidato = entradas_simuladas[i]
        if candidato.isdigit():
            numero_valido = int(candidato)
        else:
            print(f"'{candidato}' no es un numero, sigo buscando...")
        i += 1
    print("Primer numero valido encontrado:", numero_valido)


# =====================================================================
# 1.5 Funciones
# =====================================================================

def es_par(numero):
    """Devuelve True si numero es par."""
    return numero % 2 == 0


def vaciar_celda(tablero, fila, columna):
    """
    Ejemplo de funcion que modifica una lista "in-place" (sin necesidad
    de devolverla), porque las listas son MUTABLES y se pasan por
    referencia. Esto es exactamente lo que hace resolver() en el
    sudoku solver: modifica el tablero directamente.
    """
    tablero[fila][columna] = 0


def seccion_1_5():
    print("es_par(4) ->", es_par(4))
    print("es_par(7) ->", es_par(7))

    tablero_ejemplo = [[1, 2], [3, 4]]
    print("Antes de vaciar_celda:", tablero_ejemplo)
    vaciar_celda(tablero_ejemplo, 0, 1)
    print("Despues de vaciar_celda(tablero, 0, 1):", tablero_ejemplo)
    # Nota que NO hicimos "tablero_ejemplo = vaciar_celda(...)".
    # El cambio ya quedo reflejado porque listas anidadas se modifican
    # por referencia.


# =====================================================================
# EJERCICIO DEL MODULO 1
# =====================================================================
# Sin ejecutar el codigo, responde: que imprime esto?
#
#   def misterio(n):
#       if n % 3 == 0:
#           return "fizz"
#       return n
#
#   for i in range(1, 5):
#       print(misterio(i))
#
# Piensa tu respuesta ANTES de correr ejercicio_modulo_1() abajo.

def misterio(n):
    if n % 3 == 0:
        return "fizz"
    return n


def ejercicio_modulo_1():
    print("Resultado real (compara con lo que anotaste en papel):")
    for i in range(1, 5):
        print(misterio(i))
    print("Respuesta esperada: 1, 2, fizz, 4")


# =====================================================================
# MAIN: ejecuta todo el modulo en orden
# =====================================================================

if __name__ == "__main__":
    print("\n=== 1.1 Variables y tipos de datos ===")
    seccion_1_1()

    print("\n=== 1.2 Operadores relevantes ===")
    seccion_1_2()

    print("\n=== 1.3 Estructuras condicionales ===")
    seccion_1_3()

    print("\n=== 1.4 Ciclos (for / while) ===")
    seccion_1_4()

    print("\n=== 1.5 Funciones ===")
    seccion_1_5()

    print("\n=== Ejercicio Modulo 1 ===")
    ejercicio_modulo_1()