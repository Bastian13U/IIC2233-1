"""
MODULO 2 - Listas y matrices anidadas (la grilla del sudoku)
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: dominar listas, indexacion, listas anidadas (matrices 9x9),
extraccion de filas/columnas/cajas 3x3, y comprension de listas.

Ejecuta:  python 02_listas_y_matrices.py
"""


# =====================================================================
# 2.1 Listas basicas
# =====================================================================

def seccion_2_1():
    fila = [0, 3, 0, 0, 0, 0, 0, 4, 0]

    print("fila[0] ->", fila[0])     # primer elemento, indice 0
    print("fila[1] ->", fila[1])
    print("fila[-1] ->", fila[-1])   # ultimo elemento
    print("len(fila) ->", len(fila))

    fila[2] = 7
    print("Tras fila[2] = 7:", fila)

    # 'in' para verificar pertenencia -- esto es oro para es_valido()
    print("5 in fila ->", 5 in fila)
    print("7 in fila ->", 7 in fila)


# =====================================================================
# 2.2 Listas anidadas = matrices
# =====================================================================
# Una grilla de sudoku 9x9 se representa como una lista de 9 listas,
# donde cada sublista es una fila.

TABLERO_EJEMPLO = [
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


def seccion_2_2():
    # Doble indexacion: tablero[fila][columna]
    print("tablero[0][1] ->", TABLERO_EJEMPLO[0][1])  # fila 0, columna 1 -> 3
    print("tablero[1][0] ->", TABLERO_EJEMPLO[1][0])  # fila 1, columna 0 -> 2

    # ERROR CLASICO: confundir el orden. Siempre es [fila][columna],
    # igual que en matematicas cuando hablas de una matriz A(i,j).

    # Para recorrer TODA la grilla necesitas un for anidado:
    print("\nRecorriendo toda la grilla:")
    for fila in range(9):
        for columna in range(9):
            valor = TABLERO_EJEMPLO[fila][columna]
            print(valor, end=" ")
        print()  # salto de linea al terminar cada fila


# =====================================================================
# 2.3 Extraer una fila, una columna o una caja 3x3
# =====================================================================

def obtener_columna(tablero, columna):
    """Columna completa -- no viene 'gratis', hay que construirla."""
    resultado = []
    for fila in range(9):
        resultado.append(tablero[fila][columna])
    return resultado


def obtener_columna_compacta(tablero, columna):
    """Misma funcion de arriba, con comprension de listas."""
    return [tablero[fila][columna] for fila in range(9)]


def obtener_caja(tablero, fila, columna):
    """
    Dada una celda (fila, columna), devuelve todos los valores de su
    caja 3x3. La parte clave: encontrar la esquina superior-izquierda
    de la caja con // (division entera).
    """
    caja_fila_inicio = (fila // 3) * 3
    caja_columna_inicio = (columna // 3) * 3

    valores = []
    for f in range(caja_fila_inicio, caja_fila_inicio + 3):
        for c in range(caja_columna_inicio, caja_columna_inicio + 3):
            valores.append(tablero[f][c])
    return valores


def seccion_2_3():
    print("Fila completa (ya viene gratis): tablero[0] ->", TABLERO_EJEMPLO[0])

    print("Columna 1 (con ciclo for):", obtener_columna(TABLERO_EJEMPLO, 1))
    print("Columna 1 (con comprension):", obtener_columna_compacta(TABLERO_EJEMPLO, 1))

    # Ejemplo: fila=4 -> 4 // 3 = 1 -> 1*3 = 3 -> la caja empieza en fila 3
    print("\nEjemplo del calculo de esquina de caja para fila=4:")
    print("4 // 3 =", 4 // 3, " -> caja_fila_inicio =", (4 // 3) * 3)

    print("\nCaja 3x3 que contiene a la celda (4, 4):", obtener_caja(TABLERO_EJEMPLO, 4, 4))


# =====================================================================
# 2.4 Comprension de listas (list comprehension)
# =====================================================================

def seccion_2_4():
    linea = "030000040"

    # Forma con ciclo for explicito
    resultado_for = []
    for c in linea:
        resultado_for.append(int(c))
    print("Con for explicito:", resultado_for)

    # Forma compacta equivalente (comprension de listas)
    resultado_comprension = [int(c) for c in linea]
    print("Con comprension de listas:", resultado_comprension)

    # Esto es EXACTAMENTE lo que necesitaras para convertir cada linea
    # del archivo de puzle en una fila de enteros (ver Modulo 5).


# =====================================================================
# EJERCICIO DEL MODULO 2
# =====================================================================
# Dado el siguiente tablero (un sudoku real, ya lo viste en el
# enunciado), responde SIN correr codigo: que caja 3x3 (esquina
# superior izquierda) le corresponde a la celda (5, 7)? Que valores
# contiene esa caja?

TABLERO_EJERCICIO = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def ejercicio_modulo_2():
    fila, columna = 5, 7
    caja_fila_inicio = (fila // 3) * 3
    caja_columna_inicio = (columna // 3) * 3
    print(f"5 // 3 = {5 // 3} -> caja_fila_inicio = {caja_fila_inicio}")
    print(f"7 // 3 = {7 // 3} -> caja_columna_inicio = {caja_columna_inicio}")
    print("Caja resultante (filas 3-5, columnas 6-8):",
          obtener_caja(TABLERO_EJERCICIO, fila, columna))
    print("Respuesta esperada: [0,0,3, 0,0,1, 0,0,6]")


# =====================================================================
# MAIN
# =====================================================================

if __name__ == "__main__":
    print("\n=== 2.1 Listas basicas ===")
    seccion_2_1()

    print("\n=== 2.2 Listas anidadas = matrices ===")
    seccion_2_2()

    print("\n=== 2.3 Extraer fila / columna / caja 3x3 ===")
    seccion_2_3()

    print("\n=== 2.4 Comprension de listas ===")
    seccion_2_4()

    print("\n=== Ejercicio Modulo 2 ===")
    ejercicio_modulo_2()