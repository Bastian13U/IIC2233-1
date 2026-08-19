"""
MODULO 4 - Backtracking a fondo
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: internalizar el patron ELEGIR / EXPLORAR / DESHACER a traves
de dos ejemplos clasicos (permutaciones y N-Reinas) antes de aplicarlo
al sudoku en el Modulo 7. Si entiendes este modulo, el solver del
sudoku es solo "el mismo patron con reglas distintas".

Ejecuta:  python 04_backtracking.py
"""


# =====================================================================
# 4.1 La idea central
# =====================================================================
# Backtracking es una tecnica para resolver problemas por PRUEBA Y
# ERROR SISTEMATICO: eliges una opcion, avanzas, y si en algun punto
# futuro descubres que esa eleccion no lleva a ninguna solucion,
# RETROCEDES (deshaces la eleccion) y pruebas la siguiente opcion
# disponible.
#
# Patron general (pseudocodigo) -- SIEMPRE es el mismo:
#
#   funcion resolver(estado):
#       si el estado esta completo:
#           devolver True (exito)
#
#       para cada opcion posible en este punto:
#           si la opcion es valida:
#               ELEGIR la opcion (aplicar el cambio al estado)
#               si resolver(estado) es True:      # EXPLORAR
#                   devolver True
#               DESHACER la opcion (revertir el cambio)   # BACKTRACK
#
#       devolver False   # ninguna opcion funciono desde aqui
#
# Tres verbos que debes memorizar: ELEGIR, EXPLORAR, DESHACER.


# =====================================================================
# 4.2 Por que "deshacer" es necesario?
# =====================================================================
# Porque el estado (el tablero, en nuestro caso) es COMPARTIDO y
# MUTABLE: si colocas un numero y la rama no funciona, tienes que
# dejar el estado EXACTAMENTE como estaba antes de intentar esa rama,
# para que la siguiente opcion se pruebe sobre un estado "limpio".
# Si no deshaces, arrastras un error a las siguientes ramas.


# =====================================================================
# 4.3 Ejemplo clasico #1: generar todas las permutaciones
# =====================================================================

def permutaciones(elementos, actual=None, resultados=None):
    if actual is None:
        actual = []
    if resultados is None:
        resultados = []

    if len(elementos) == 0:
        resultados.append(actual)
        return resultados

    for i in range(len(elementos)):
        elegido = elementos[i]                          # ELEGIR
        restantes = elementos[:i] + elementos[i + 1:]     # sin el elegido
        permutaciones(restantes, actual + [elegido], resultados)  # EXPLORAR
        # DESHACER es implicito aqui: 'actual + [elegido]' crea una
        # lista NUEVA (no modifica 'actual'), asi que al volver de la
        # recursion, 'actual' sigue intacto para probar el siguiente i.

    return resultados


def seccion_4_3():
    todas = permutaciones([1, 2, 3])
    print("Todas las permutaciones de [1,2,3]:")
    for p in todas:
        print(" ", p)
    print(f"Total: {len(todas)} permutaciones (deberian ser 3! = 6)")


# =====================================================================
# 4.4 Ejemplo clasico #2: N-Reinas (muy similar en espiritu al sudoku)
# =====================================================================
# Colocar N reinas en un tablero de NxN sin que se ataquen entre si.
# tablero_reinas[fila] = columna donde esta la reina de esa fila
# (o -1 si esa fila aun no tiene reina asignada).

def es_seguro(tablero_reinas, fila, columna):
    for f in range(fila):
        c = tablero_reinas[f]
        if c == -1:
            continue
        # misma columna, o misma diagonal
        if c == columna or abs(c - columna) == abs(f - fila):
            return False
    return True


def resolver_reinas(tablero_reinas, fila):
    if fila == len(tablero_reinas):
        return True  # se colocaron reinas en todas las filas

    for columna in range(len(tablero_reinas)):
        if es_seguro(tablero_reinas, fila, columna):
            tablero_reinas[fila] = columna              # ELEGIR

            if resolver_reinas(tablero_reinas, fila + 1):  # EXPLORAR
                return True

            tablero_reinas[fila] = -1                    # DESHACER

    return False


def imprimir_reinas(tablero_reinas):
    n = len(tablero_reinas)
    for fila in range(n):
        linea = ""
        for columna in range(n):
            linea += "Q " if tablero_reinas[fila] == columna else ". "
        print(linea)


def seccion_4_4():
    n = 6
    tablero_reinas = [-1] * n
    if resolver_reinas(tablero_reinas, 0):
        print(f"Solucion encontrada para {n}-Reinas:")
        imprimir_reinas(tablero_reinas)
    else:
        print(f"No se encontro solucion para {n}-Reinas.")

    # Compara la ESTRUCTURA de resolver_reinas() con la que veras en
    # resolver() del sudoku (Modulo 7): son PRACTICAMENTE IDENTICAS.
    # Esa es la senal de que entendiste el patron.


# =====================================================================
# 4.5 Aplicando el patron al Sudoku (tabla de equivalencias)
# =====================================================================
#
#   Verbo del patron        | En el Sudoku
#   -------------------------|--------------------------------------
#   Estado completo?         | No queda ninguna celda vacia
#   Opciones posibles        | Numeros del 1 al 9
#   Opcion valida?           | es_valido(): no se repite en fila/columna/caja
#   Elegir                   | tablero[fila][columna] = numero
#   Explorar                 | Llamada recursiva resolver(tablero)
#   Deshacer                 | tablero[fila][columna] = 0
#
# La diferencia con N-Reinas es solo el criterio de "opcion valida" y
# como se identifica el "siguiente lugar a llenar".


# =====================================================================
# EJERCICIO DEL MODULO 4
# =====================================================================
# Que pasaria si en resolver() del sudoku OLVIDAS la linea de
# "deshacer" (tablero[fila][columna] = 0) despues de un intento
# fallido? Piensa tu respuesta, luego lee la funcion de abajo.

def ejercicio_modulo_4():
    respuesta = """
    El tablero quedaria con numeros "fantasma" de intentos fallidos
    que nunca se limpiaron. Cuando el algoritmo retroceda a probar
    otra opcion en una celda anterior, se encontrara con celdas que
    aparentan estar ocupadas con valores incorrectos, lo que puede
    hacer que es_valido() rechace opciones que en realidad si eran
    validas, o -peor- que el algoritmo "resuelva" el tablero con
    numeros que no corresponden a una solucion real, porque el
    estado ya no refleja fielmente las decisiones vigentes.
    """
    print(respuesta)

    # IMPORTANTE: en N-Reinas, es_seguro() solo compara la fila actual
    # contra las filas ANTERIORES (fila 0 .. fila-1), asi que un valor
    # "fantasma" que quede en una fila mas profunda casi nunca se
    # vuelve a leer antes de ser sobreescrito -- por eso, si probaras
    # el mismo experimento con resolver_reinas(), el bug puede pasar
    # desapercibido (por suerte, no porque este bien hecho).
    #
    # En el Sudoku el problema SI se nota, porque es_valido() revisa
    # la fila, columna Y caja COMPLETAS en cada llamada, sin importar
    # el orden en que se fueron llenando. Un valor que quedo pegado de
    # un intento fallido anterior contamina esas revisiones. Veamos la
    # diferencia en un mini-sudoku real:
    print("Demo: mismo bug, pero en un sudoku real (donde SI se nota):")

    def encontrar_celda_vacia_demo(tablero):
        for fila in range(9):
            for columna in range(9):
                if tablero[fila][columna] == 0:
                    return (fila, columna)
        return None

    def es_valido_demo(tablero, fila, columna, numero):
        if numero in tablero[fila]:
            return False
        for f in range(9):
            if tablero[f][columna] == numero:
                return False
        cfi, cci = (fila // 3) * 3, (columna // 3) * 3
        for f in range(cfi, cfi + 3):
            for c in range(cci, cci + 3):
                if tablero[f][c] == numero:
                    return False
        return True

    def resolver_sudoku_correcto(tablero):
        celda = encontrar_celda_vacia_demo(tablero)
        if celda is None:
            return True
        fila, columna = celda
        for numero in range(1, 10):
            if es_valido_demo(tablero, fila, columna, numero):
                tablero[fila][columna] = numero
                if resolver_sudoku_correcto(tablero):
                    return True
                tablero[fila][columna] = 0  # <-- el deshacer, presente
        return False

    def resolver_sudoku_roto(tablero, contador):
        contador[0] += 1
        if contador[0] > 500:  # limite de seguridad para el demo
            return False
        celda = encontrar_celda_vacia_demo(tablero)
        if celda is None:
            return True
        fila, columna = celda
        for numero in range(1, 10):
            if es_valido_demo(tablero, fila, columna, numero):
                tablero[fila][columna] = numero
                if resolver_sudoku_roto(tablero, contador):
                    return True
                # <-- FALTA: tablero[fila][columna] = 0
        return False

    puzle_de_ejemplo = [
        [0, 3, 0, 0, 0, 0, 0, 4, 0],
        [2, 9, 0, 0, 0, 0, 0, 5, 7],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [9, 6, 0, 0, 0, 0, 0, 7, 4],
        [0, 8, 0, 0, 0, 0, 0, 6, 0],
    ]

    tablero_correcto = [fila[:] for fila in puzle_de_ejemplo]  # copia independiente
    exito_correcto = resolver_sudoku_correcto(tablero_correcto)
    print(f"\nVersion CORRECTA (con deshacer)  -> resuelto: {exito_correcto}")

    tablero_roto = [fila[:] for fila in puzle_de_ejemplo]  # otra copia independiente
    contador = [0]
    exito_roto = resolver_sudoku_roto(tablero_roto, contador)
    print(f"Version ROTA (sin deshacer)       -> resuelto: {exito_roto} "
          f"(se dio por vencida tras {contador[0]} llamadas)")
    print("Tablero que dejo la version rota (a medio contaminar, no es una solucion):")
    for fila in tablero_roto:
        print(" ", fila)
    print("\nEsto confirma la explicacion: sin 'deshacer', el algoritmo se "
          "atasca mucho antes y deja el tablero en un estado invalido, en vez "
          "de encontrar la solucion real.")


# =====================================================================
# MAIN
# =====================================================================

if __name__ == "__main__":
    print("\n=== 4.3 Permutaciones ===")
    seccion_4_3()

    print("\n=== 4.4 N-Reinas ===")
    seccion_4_4()

    print("\n=== Ejercicio Modulo 4 ===")
    ejercicio_modulo_4()