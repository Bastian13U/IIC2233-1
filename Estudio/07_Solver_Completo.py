"""
MODULO 7 - Construccion completa del Sudoku Solver
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: integrar TODO lo visto en los modulos 1 a 6 en el programa
final. Esto es, en esencia, tu solver.py ya resuelto y comentado paso
a paso, en el orden en que conviene construirlo (de lo simple a lo
complejo).

Este archivo es autocontenido: si no encuentra una carpeta 'puzles' al
lado suyo, se crea una con un puzle de ejemplo para que puedas
ejecutarlo de inmediato.

Ejecuta:  python 07_solver_completo.py
"""

import os

CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_PUZLES = os.path.join(CARPETA_ACTUAL, "puzles")


def asegurar_puzle_de_ejemplo():
    """Crea la carpeta 'puzles' y un puzle de ejemplo si no existen,
    para que este archivo funcione apenas lo descargues."""
    os.makedirs(CARPETA_PUZLES, exist_ok=True)
    ruta_ejemplo = os.path.join(CARPETA_PUZLES, "puzle01.txt")
    if not os.path.exists(ruta_ejemplo):
        contenido = (
            "030000040\n"
            "290000057\n"
            "000002000\n"
            "006000000\n"
            "000010000\n"
            "000000900\n"
            "000900000\n"
            "960000074\n"
            "080000060\n"
        )
        with open(ruta_ejemplo, "w") as archivo:
            archivo.write(contenido)


# =====================================================================
# PASO 1 - Leer el puzle (repaso Modulo 5)
# =====================================================================

def leer_puzle(nombre_archivo):
    ruta = os.path.join(CARPETA_PUZLES, nombre_archivo)
    tablero = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                fila = [int(c) for c in linea]
                tablero.append(fila)
    return tablero


# =====================================================================
# PASO 2 - Imprimir el tablero (repaso Modulo 2)
# =====================================================================

def imprimir_tablero(tablero):
    for i, fila in enumerate(tablero):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        fila_str = ""
        for j, numero in enumerate(fila):
            if j % 3 == 0 and j != 0:
                fila_str += "| "
            fila_str += (str(numero) if numero != 0 else ".") + " "
        print(fila_str)


# =====================================================================
# PASO 3 - Encontrar la siguiente celda vacia (repaso Modulo 2)
# =====================================================================

def encontrar_celda_vacia(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return (fila, columna)
    return None


# =====================================================================
# PASO 4 - Validar un numero en una celda (repaso Modulo 2 + Modulo 1)
# =====================================================================

def es_valido(tablero, fila, columna, numero):
    if numero in tablero[fila]:                        # fila
        return False

    for f in range(9):                                   # columna
        if tablero[f][columna] == numero:
            return False

    caja_fila_inicio = (fila // 3) * 3                    # caja 3x3
    caja_columna_inicio = (columna // 3) * 3
    for f in range(caja_fila_inicio, caja_fila_inicio + 3):
        for c in range(caja_columna_inicio, caja_columna_inicio + 3):
            if tablero[f][c] == numero:
                return False

    return True


# =====================================================================
# PASO 5 - Resolver con backtracking (repaso Modulo 4 + Modulo 3)
# =====================================================================

def resolver(tablero):
    celda_vacia = encontrar_celda_vacia(tablero)

    if celda_vacia is None:
        return True                          # caso base: tablero completo

    fila, columna = celda_vacia

    for numero in range(1, 10):
        if es_valido(tablero, fila, columna, numero):
            tablero[fila][columna] = numero          # ELEGIR

            if resolver(tablero):                      # EXPLORAR
                return True

            tablero[fila][columna] = 0                  # DESHACER

    return False


# =====================================================================
# PASO 6 - Menu y programa principal (repaso Modulo 6)
# =====================================================================

def menu():
    archivos = sorted(f for f in os.listdir(CARPETA_PUZLES) if f.endswith(".txt"))
    print("=== Puzles disponibles ===")
    for i, archivo in enumerate(archivos, start=1):
        print(f"{i}. {archivo}")
    while True:
        try:
            opcion = int(input("Elige un puzle (numero): "))
            if 1 <= opcion <= len(archivos):
                return archivos[opcion - 1]
            print("Opcion fuera de rango.")
        except ValueError:
            print("Debes ingresar un numero.")


def main():
    try:
        nombre_archivo = menu()
    except EOFError:
        # Sin teclado interactivo disponible (por ejemplo, al correr
        # este archivo en un entorno automatizado): se auto-selecciona
        # el primer puzle disponible para que igual veas el resultado.
        archivos = sorted(f for f in os.listdir(CARPETA_PUZLES) if f.endswith(".txt"))
        nombre_archivo = archivos[0]
        print(f"(Sin input interactivo: usando '{nombre_archivo}' automaticamente. "
              f"Corre este archivo en tu propia terminal para elegir a mano.)")

    tablero = leer_puzle(nombre_archivo)

    print("\nPuzle inicial:")
    imprimir_tablero(tablero)

    if resolver(tablero):
        print("\nPuzle resuelto:")
        imprimir_tablero(tablero)
    else:
        print("\nEste puzle no tiene solucion.")


# El bloque if __name__ == "__main__" asegura que main() solo se
# ejecute cuando corres el archivo directamente (python solver.py), y
# no si alguien lo importa como modulo. Es buena practica estandar en
# Python.


# =====================================================================
# 7.1 Traza mental de una ejecucion corta (para repasar el flujo)
# =====================================================================
#
#  1. main() llama a resolver(tablero).
#  2. resolver busca la primera celda vacia -> la encuentra en (0,0).
#  3. Prueba numero=1. Si es_valido dice que si, lo coloca y se llama
#     a si misma de nuevo.
#  4. La nueva llamada busca la SIGUIENTE celda vacia, y repite.
#  5. Si en algun punto NINGUN numero de 1 a 9 es valido para la celda
#     actual, esa llamada devuelve False.
#  6. La llamada ANTERIOR (que sigue esperando en la pila) recibe ese
#     False, deshace su numero, y prueba el siguiente.
#  7. Esto continua hasta que encontrar_celda_vacia devuelve None
#     (tablero lleno) -> se propaga True hasta main().
#
#  Esta es la esencia de TODO backtracking: una cadena de llamadas que
#  avanza mientras puede, y retrocede EXACTAMENTE un paso cuando se
#  atasca -- nunca "salta" varios pasos atras de una vez.


# =====================================================================
# EJERCICIO DEL MODULO 7
# =====================================================================
# Una optimizacion comun es "elegir la celda vacia con MENOS
# candidatos posibles" en vez de "la primera celda vacia que
# aparece". Por que crees que eso reduciria el numero de intentos
# fallidos? (Piensa en terminos de poda del arbol de busqueda.)

def contar_candidatos(tablero, fila, columna):
    """Funcion de apoyo para la version optimizada (opcional)."""
    return sum(1 for numero in range(1, 10) if es_valido(tablero, fila, columna, numero))


def ejercicio_modulo_7():
    respuesta = """
    Porque si eliges la celda con menos opciones validas, hay menos
    ramas que explorar en ese punto, y las contradicciones (celdas
    sin ningun candidato valido) se detectan mas temprano en el arbol
    de busqueda, evitando construir ramas largas que de todas formas
    iban a fallar mas adelante. Esto se conoce como heuristica de
    "most constrained variable" -- es un concepto avanzado, no
    necesario para aprobar el ejercicio, pero bueno para entender por
    que el backtracking "ingenuo" a veces es lento en puzles dificiles.
    """
    print(respuesta)


if __name__ == "__main__":
    asegurar_puzle_de_ejemplo()
    main()

    print("\n=== Ejercicio Modulo 7 ===")
    ejercicio_modulo_7()