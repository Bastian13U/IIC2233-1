"""
MODULO 5 - Manejo de archivos de texto
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: aprender a abrir, leer y parsear archivos de texto -- asi es
como tu programa cargara los puzles desde la carpeta 'puzles'.

Este archivo es autocontenido: crea su propio archivo de ejemplo
('ejemplo_puzle.txt', al lado de este script) para que puedas ejecutarlo
sin depender de otras carpetas.

Ejecuta:  python 05_archivos.py
"""

import os

# Carpeta donde vive este script (para que el archivo de ejemplo se
# cree siempre al lado de 05_archivos.py, sin importar desde donde lo
# ejecutes).
CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_EJEMPLO = os.path.join(CARPETA_ACTUAL, "ejemplo_puzle.txt")


def crear_archivo_de_ejemplo():
    """Genera un archivo de puzle de ejemplo (igual al del enunciado)."""
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
    with open(RUTA_EJEMPLO, "w") as archivo:
        archivo.write(contenido)


# =====================================================================
# 5.1 Abrir y leer archivos con 'with'
# =====================================================================

def seccion_5_1():
    with open(RUTA_EJEMPLO, "r") as archivo:
        contenido = archivo.read()  # todo el archivo como un solo string
    print("Contenido completo (repr para ver los \\n):")
    print(repr(contenido))

    # 'with' es la forma recomendada: garantiza que el archivo se
    # CIERRE automaticamente al salir del bloque, incluso si ocurre
    # un error dentro.


# =====================================================================
# 5.2 Leer linea por linea
# =====================================================================

def seccion_5_2():
    with open(RUTA_EJEMPLO, "r") as archivo:
        for linea in archivo:
            print(repr(linea))  # "030000040\n"  <- OJO el \n al final

    # Cada linea trae al final un salto de linea (\n) que DEBES quitar
    # con .strip() antes de procesarla, o tendras bugs raros al
    # convertir a numeros.
    with open(RUTA_EJEMPLO, "r") as archivo:
        primera_linea = archivo.readline()
    print("\nSin limpiar:", repr(primera_linea))
    print("Con .strip():", repr(primera_linea.strip()))


# =====================================================================
# 5.3 De linea de texto a lista de enteros
# =====================================================================

def seccion_5_3():
    linea = "030000040"
    fila = [int(caracter) for caracter in linea]
    print(f"'{linea}' -> {fila}")


# =====================================================================
# 5.4 Juntando todo: leer el puzle completo
# =====================================================================

def leer_puzle(ruta):
    tablero = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:  # evita procesar lineas vacias al final
                fila = [int(c) for c in linea]
                tablero.append(fila)
    return tablero


def seccion_5_4():
    tablero = leer_puzle(RUTA_EJEMPLO)
    print(f"Tablero leido tiene {len(tablero)} filas.")
    for fila in tablero:
        print(fila)


# =====================================================================
# 5.5 Rutas de archivo con os.path.join
# =====================================================================

def seccion_5_5():
    # Buena practica: construir rutas de forma portable (funciona
    # igual en Windows, Mac o Linux).
    ruta = os.path.join("puzles", "puzle01.txt")
    print("os.path.join('puzles', 'puzle01.txt') ->", ruta)


# =====================================================================
# 5.6 Listar archivos de una carpeta
# =====================================================================

def seccion_5_6():
    archivos = os.listdir(CARPETA_ACTUAL)
    print("Todo lo que hay en esta carpeta:", archivos)

    archivos_txt = [f for f in archivos if f.endswith(".txt")]
    print("Solo los .txt:", archivos_txt)

    # Esto es lo que usaras para construir el MENU DINAMICO (Modulo 6),
    # en vez de escribir los nombres de los puzles "a mano" en el codigo.


# =====================================================================
# EJERCICIO DEL MODULO 5
# =====================================================================
# Que error ocurre (y por que) si olvidas el .strip() al leer cada
# linea, e intentas hacer int(c) sobre el caracter '\n' dentro de una
# lista de comprension? Piensa tu respuesta, luego ejecuta la funcion
# de abajo para comprobarlo EN VIVO (esta disenada para fallar).

def ejercicio_modulo_5():
    print("Respuesta esperada: ValueError, porque '\\n' no es un digito.\n")
    print("Comprobandolo en vivo (se capturara el error para que no truene el programa):")
    linea_sucia = "030000040\n"  # con el \n, a proposito, SIN strip()
    try:
        fila = [int(c) for c in linea_sucia]
        print("No debería llegar aqui:", fila)
    except ValueError as error:
        print(f"Error capturado, tal como se esperaba: {error}")


# =====================================================================
# MAIN
# =====================================================================

if __name__ == "__main__":
    crear_archivo_de_ejemplo()

    print("\n=== 5.1 Abrir y leer archivos con 'with' ===")
    seccion_5_1()

    print("\n=== 5.2 Leer linea por linea ===")
    seccion_5_2()

    print("\n=== 5.3 De linea de texto a lista de enteros ===")
    seccion_5_3()

    print("\n=== 5.4 Leer el puzle completo ===")
    seccion_5_4()

    print("\n=== 5.5 Rutas de archivo con os.path.join ===")
    seccion_5_5()

    print("\n=== 5.6 Listar archivos de una carpeta ===")
    seccion_5_6()

    print("\n=== Ejercicio Modulo 5 ===")
    ejercicio_modulo_5()