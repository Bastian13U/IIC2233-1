"""
MODULO 9 (EXTRA) - Thermo Sudoku, el desafio avanzado
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: mostrar como EXTENDER el solver del Modulo 7 para soportar
la variante Thermo Sudoku, sin reescribir el algoritmo de backtracking.
Este modulo es opcional (no forma parte del ejercicio base), pero es
una excelente prueba de que entendiste bien el diseno modular.

Ejecuta:  python 09_extra_thermo_sudoku.py
"""


# =====================================================================
# 9.1 Que cambia respecto al sudoku normal?
# =====================================================================
# Ademas de las reglas normales del sudoku, hay TERMOMETROS: secuencias
# de celdas conectadas donde los numeros deben ser ESTRICTAMENTE
# CRECIENTES desde el "bulbo" (el extremo redondo) hacia el otro
# extremo.
#
# Representamos cada termometro como una lista de coordenadas (fila,
# columna) EN ORDEN, desde el bulbo hasta la punta:
#
#   termometro_1 = [(0,1), (0,2), (1,2), (2,2)]   # el bulbo esta en (0,1)


# =====================================================================
# 9.2 Validacion extra para termometros
# =====================================================================

def cumple_termometro(tablero, termometro, posicion_en_termometro, numero):
    """
    Verifica que colocar 'numero' en la celda que ocupa la posicion
    'posicion_en_termometro' dentro de 'termometro' respete el orden
    creciente respecto a sus vecinos YA COLOCADOS en el termometro.
    """
    fila, columna = termometro[posicion_en_termometro]
    assert tablero[fila][columna] == 0 or tablero[fila][columna] == numero

    # revisar contra la celda anterior (mas cerca del bulbo)
    if posicion_en_termometro > 0:
        f_ant, c_ant = termometro[posicion_en_termometro - 1]
        valor_anterior = tablero[f_ant][c_ant]
        if valor_anterior != 0 and numero <= valor_anterior:
            return False

    # revisar contra la celda siguiente (mas lejos del bulbo)
    if posicion_en_termometro < len(termometro) - 1:
        f_sig, c_sig = termometro[posicion_en_termometro + 1]
        valor_siguiente = tablero[f_sig][c_sig]
        if valor_siguiente != 0 and numero >= valor_siguiente:
            return False

    return True


# =====================================================================
# 9.3 Integrandolo con es_valido() del Modulo 7
# =====================================================================
# La idea clave: el resto del algoritmo (resolver, encontrar_celda_vacia,
# la estructura de backtracking) NO CAMBIA -- solo agregas esta
# validacion extra dentro de tu chequeo de "es valido este numero aqui?".
# Esa es la belleza del diseno modular: como separaste bien las
# funciones en el Modulo 7, extender las reglas del juego no te obliga
# a reescribir el algoritmo central.

def es_valido_normal(tablero, fila, columna, numero):
    """Copiada tal cual del Modulo 7 (reglas normales de sudoku)."""
    if numero in tablero[fila]:
        return False
    for f in range(len(tablero)):
        if tablero[f][columna] == numero:
            return False
    caja_fila_inicio = (fila // 3) * 3
    caja_columna_inicio = (columna // 3) * 3
    for f in range(caja_fila_inicio, caja_fila_inicio + 3):
        for c in range(caja_columna_inicio, caja_columna_inicio + 3):
            if tablero[f][c] == numero:
                return False
    return True


def construir_mapa_de_termometros(termometros):
    """
    Convierte la lista de termometros en un diccionario que permite
    buscar rapido: dada una celda (fila, columna), a que termometro
    pertenece y en que posicion de el.
    Estructura resultante: {(fila, columna): (termometro, posicion)}
    """
    mapa = {}
    for termometro in termometros:
        for posicion, celda in enumerate(termometro):
            mapa[celda] = (termometro, posicion)
    return mapa


def es_valido_thermo(tablero, fila, columna, numero, mapa_termometros):
    """es_valido() extendida: reglas normales + regla de termometro."""
    if not es_valido_normal(tablero, fila, columna, numero):
        return False

    if (fila, columna) in mapa_termometros:
        termometro, posicion = mapa_termometros[(fila, columna)]
        if not cumple_termometro(tablero, termometro, posicion, numero):
            return False

    return True


# =====================================================================
# 9.4 Demo con un mini-tablero (4x4, para que la demo corra rapido)
# =====================================================================
# NOTA: para simplificar la demo usamos un tablero 4x4 con "cajas" de
# 2x2 en vez de 9x9 con cajas 3x3, para que el ejemplo sea legible y
# rapido de ejecutar. La logica es identica, solo cambia el tamano.

def encontrar_celda_vacia_nxn(tablero):
    n = len(tablero)
    for fila in range(n):
        for columna in range(n):
            if tablero[fila][columna] == 0:
                return (fila, columna)
    return None


def es_valido_normal_nxn(tablero, fila, columna, numero, tam_caja):
    n = len(tablero)
    if numero in tablero[fila]:
        return False
    for f in range(n):
        if tablero[f][columna] == numero:
            return False
    caja_fila_inicio = (fila // tam_caja) * tam_caja
    caja_columna_inicio = (columna // tam_caja) * tam_caja
    for f in range(caja_fila_inicio, caja_fila_inicio + tam_caja):
        for c in range(caja_columna_inicio, caja_columna_inicio + tam_caja):
            if tablero[f][c] == numero:
                return False
    return True


def es_valido_thermo_nxn(tablero, fila, columna, numero, tam_caja, mapa_termometros):
    if not es_valido_normal_nxn(tablero, fila, columna, numero, tam_caja):
        return False
    if (fila, columna) in mapa_termometros:
        termometro, posicion = mapa_termometros[(fila, columna)]
        if not cumple_termometro(tablero, termometro, posicion, numero):
            return False
    return True


def resolver_thermo_nxn(tablero, tam_caja, mapa_termometros):
    n = len(tablero)
    celda_vacia = encontrar_celda_vacia_nxn(tablero)
    if celda_vacia is None:
        return True

    fila, columna = celda_vacia
    for numero in range(1, n + 1):
        if es_valido_thermo_nxn(tablero, fila, columna, numero, tam_caja, mapa_termometros):
            tablero[fila][columna] = numero
            if resolver_thermo_nxn(tablero, tam_caja, mapa_termometros):
                return True
            tablero[fila][columna] = 0
    return False


def imprimir_tablero_nxn(tablero):
    for fila in tablero:
        print(" ".join(str(x) if x != 0 else "." for x in fila))


def seccion_9_4():
    # Tablero 4x4 (valores 1-4, cajas de 2x2). Un termometro que sube
    # en diagonal-escalera desde (0,0) hasta (1,1).
    tablero = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    termometro_1 = [(0, 0), (0, 1), (1, 1)]  # bulbo en (0,0), creciente hacia (1,1)
    mapa_termometros = construir_mapa_de_termometros([termometro_1])

    print("Tablero inicial (vacio) con un termometro en (0,0)->(0,1)->(1,1):")
    imprimir_tablero_nxn(tablero)

    exito = resolver_thermo_nxn(tablero, tam_caja=2, mapa_termometros=mapa_termometros)
    print("\nSe encontro solucion?", exito)
    if exito:
        imprimir_tablero_nxn(tablero)
        f0, c0 = termometro_1[0]
        f1, c1 = termometro_1[1]
        f2, c2 = termometro_1[2]
        print(f"\nVerificando el termometro: {tablero[f0][c0]} < {tablero[f1][c1]} < {tablero[f2][c2]}"
              f"  -> {tablero[f0][c0] < tablero[f1][c1] < tablero[f2][c2]}")


# =====================================================================
# NOTA FINAL
# =====================================================================
# Para adaptar esto a un sudoku 9x9 de verdad, usarias
# es_valido_thermo() (la version de 9.3, ya pensada para tableros 9x9
# con cajas 3x3) en vez de resolver() del Modulo 7, agregando el
# parametro extra 'mapa_termometros' a lo largo de tu funcion
# resolver(). El patron de backtracking en si -- elegir, explorar,
# deshacer -- se mantiene EXACTAMENTE igual.


if __name__ == "__main__":
    print("=== 9.4 Demo: mini Thermo Sudoku 4x4 resuelto con backtracking ===")
    seccion_9_4()