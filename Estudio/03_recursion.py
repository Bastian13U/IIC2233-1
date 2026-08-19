"""
MODULO 3 - Recursion (el motor del backtracking)
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: entender que es una funcion recursiva, que es el caso base
y el caso recursivo, y como funciona la pila de llamadas (call stack).
Esto es la base conceptual que necesitas ANTES de entender backtracking.

Ejecuta:  python 03_recursion.py
"""


# =====================================================================
# 3.1 Que es la recursion?
# =====================================================================
# Una funcion RECURSIVA es una funcion que se llama a si misma para
# resolver una version mas pequena del mismo problema, hasta llegar a
# un CASO BASE que se puede resolver directamente sin mas llamadas.
#
# Toda funcion recursiva necesita dos partes:
#   1. Caso base: la condicion que DETIENE la recursion. Si no existe,
#      la funcion se llama infinitamente hasta un RecursionError.
#   2. Caso recursivo: la llamada a si misma con un problema mas
#      pequeno, acercandose al caso base.


# =====================================================================
# 3.2 Ejemplo clasico: factorial
# =====================================================================

def factorial(n):
    if n == 0:                     # <-- CASO BASE
        return 1
    return n * factorial(n - 1)    # <-- CASO RECURSIVO


def seccion_3_2():
    print("factorial(4) ->", factorial(4))
    print("factorial(0) ->", factorial(0))
    print("factorial(6) ->", factorial(6))

    # Traza de factorial(4):
    #
    #   factorial(4) = 4 * factorial(3)
    #   factorial(3) = 3 * factorial(2)
    #   factorial(2) = 2 * factorial(1)
    #   factorial(1) = 1 * factorial(0)
    #   factorial(0) = 1                  <- caso base, "toca fondo" aqui
    #
    # Y luego se devuelve hacia arriba (la pila de llamadas):
    #
    #   factorial(1) = 1 * 1 = 1
    #   factorial(2) = 2 * 1 = 2
    #   factorial(3) = 3 * 2 = 6
    #   factorial(4) = 4 * 6 = 24
    print("\nVersion con print para VER la pila de llamadas en accion:")
    factorial_con_traza(4)


def factorial_con_traza(n, profundidad=0):
    """Misma logica que factorial(), pero imprime cada paso para que
    veas visualmente como se apilan y desapilan las llamadas."""
    sangria = "  " * profundidad
    print(f"{sangria}-> entrando a factorial_con_traza({n})")

    if n == 0:
        print(f"{sangria}<- caso base, devuelvo 1")
        return 1

    resultado_parcial = factorial_con_traza(n - 1, profundidad + 1)
    resultado = n * resultado_parcial
    print(f"{sangria}<- devuelvo {n} * {resultado_parcial} = {resultado}")
    return resultado


# =====================================================================
# 3.3 La pila de llamadas (call stack)
# =====================================================================
# Cada vez que una funcion se llama a si misma, Python "apila" una
# nueva instancia de esa funcion con sus propias variables locales, y
# NO continua la anterior hasta que la nueva termine (con return).
# Es como una pila de platos: el ultimo que se apila es el primero
# que se retira (LIFO: Last In, First Out).
#
# Esto explica por que en el sudoku solver, cuando resolver(tablero)
# "retrocede" (hace backtrack), en realidad esta VOLVIENDO a una
# llamada anterior en la pila, que sigue esperando con su propio
# numero candidato pendiente de probar.


# =====================================================================
# 3.4 Ejemplo con listas: suma recursiva
# =====================================================================

def suma(lista):
    if len(lista) == 0:                    # caso base: lista vacia -> 0
        return 0
    return lista[0] + suma(lista[1:])       # primer elemento + suma del resto


def seccion_3_4():
    print("suma([1,2,3,4]) ->", suma([1, 2, 3, 4]))
    print("suma([]) ->", suma([]))
    print("suma([10]) ->", suma([10]))


# =====================================================================
# EJERCICIO DEL MODULO 3
# =====================================================================
# Escribe (a mano, en papel) la traza completa de fibonacci(4) con
# esta funcion, mostrando cada llamada. Hazlo ANTES de correr
# ejercicio_modulo_3() abajo.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_con_traza(n, profundidad=0):
    sangria = "  " * profundidad
    print(f"{sangria}-> fibonacci({n})")
    if n <= 1:
        print(f"{sangria}<- caso base, devuelvo {n}")
        return n
    izquierda = fibonacci_con_traza(n - 1, profundidad + 1)
    derecha = fibonacci_con_traza(n - 2, profundidad + 1)
    resultado = izquierda + derecha
    print(f"{sangria}<- devuelvo {izquierda} + {derecha} = {resultado}")
    return resultado


def ejercicio_modulo_3():
    print("Tu respuesta esperada (revisala en papel primero):")
    print("""
    fibonacci(4) = fibonacci(3) + fibonacci(2)
    fibonacci(3) = fibonacci(2) + fibonacci(1) = (fib(1)+fib(0)) + 1 = (1+0)+1 = 2
    fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
    fibonacci(4) = 2 + 1 = 3
    """)
    print("Traza real ejecutada por Python:")
    resultado = fibonacci_con_traza(4)
    print("Resultado final:", resultado)


# =====================================================================
# MAIN
# =====================================================================

if __name__ == "__main__":
    print("\n=== 3.2 Ejemplo clasico: factorial ===")
    seccion_3_2()

    print("\n=== 3.4 Ejemplo con listas: suma recursiva ===")
    seccion_3_4()

    print("\n=== Ejercicio Modulo 3: fibonacci(4) ===")
    ejercicio_modulo_3()