"""
MODULO 6 - Input de usuario y menus por consola
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: aprender a pedir datos al usuario con input(), validar esos
datos, y construir un menu numerado -- exactamente lo que el enunciado
pide para elegir el archivo de puzle a resolver.

Ejecuta:  python 06_input_menus.py
(Si lo ejecutas en un entorno sin teclado interactivo, la parte final
que usa input() real se salta automaticamente y te avisa.)
"""

import os


# =====================================================================
# 6.1 input() basico
# =====================================================================
# Todo lo que devuelve input() es SIEMPRE string, incluso si el
# usuario escribe un numero -- tienes que convertirlo tu mismo con
# int() si lo necesitas como numero.
#
# Ejemplo (no lo ejecutamos aqui para no bloquear el demo):
#
#   nombre = input("Como te llamas? ")   # nombre es siempre str


# =====================================================================
# 6.2 Validar el input (evitar que el programa se caiga)
# =====================================================================
# Si el usuario escribe algo que no es un numero y tu intentas
# int(...) directamente, tu programa lanzara una excepcion y se
# detendra abruptamente. Para evitarlo, usa try/except.

def interpretar_opcion(texto_ingresado, cantidad_opciones):
    """
    Logica de validacion SEPARADA de input(), para poder probarla
    sin depender de teclado real (asi puedes ejecutar este archivo
    sin que se quede esperando que escribas algo).

    Devuelve una tupla (es_valida, resultado):
      - Si es valida: (True, indice_de_la_lista)   [ya restado el -1]
      - Si NO es valida: (False, mensaje_de_error)
    """
    try:
        opcion = int(texto_ingresado)
    except ValueError:
        return False, "Debes ingresar un numero."

    if 1 <= opcion <= cantidad_opciones:
        return True, opcion - 1  # -1 porque el menu se muestra desde 1

    return False, "Opcion fuera de rango."


def seccion_6_2():
    ejemplos = ["hola", "0", "2", "99", "3"]
    cantidad_opciones = 3
    print(f"Simulando distintas entradas con {cantidad_opciones} opciones disponibles:\n")
    for texto in ejemplos:
        es_valida, resultado = interpretar_opcion(texto, cantidad_opciones)
        if es_valida:
            print(f"  Entrada '{texto}' -> VALIDA, indice de lista = {resultado}")
        else:
            print(f"  Entrada '{texto}' -> INVALIDA ({resultado})")


# =====================================================================
# 6.3 Construir un menu numerado
# =====================================================================
# Patron tipico: listar opciones, pedir un numero, usar ese numero
# como indice (recordando que las listas parten en 0, pero al usuario
# normalmente le muestras desde 1).
#
# enumerate(lista, start=1) te da pares (indice, valor) empezando en 1
# en vez de 0 -- ideal para mostrar un menu "humano".

def mostrar_menu(opciones):
    print("=== Opciones disponibles ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")


def seccion_6_3():
    archivos_de_ejemplo = ["puzle01.txt", "puzle02.txt", "puzle03.txt"]
    mostrar_menu(archivos_de_ejemplo)


# =====================================================================
# 6.4 El menu REAL, usando input() de verdad
# =====================================================================
# Esta es la version completa que usarias en tu solver.py. Junta
# mostrar_menu() + interpretar_opcion() + un ciclo while que vuelve
# a preguntar si el usuario se equivoca.

def menu(carpeta_puzles="puzles"):
    if os.path.isdir(carpeta_puzles):
        archivos = sorted(f for f in os.listdir(carpeta_puzles) if f.endswith(".txt"))
    else:
        archivos = []

    if not archivos:
        print(f"(No se encontro la carpeta '{carpeta_puzles}' con archivos .txt; "
              f"usando una lista de ejemplo para la demo)")
        archivos = ["puzle01.txt", "puzle02.txt", "puzle03.txt"]

    mostrar_menu(archivos)

    while True:
        texto_ingresado = input("Elige un puzle (numero): ")
        es_valida, resultado = interpretar_opcion(texto_ingresado, len(archivos))
        if es_valida:
            return archivos[resultado]
        print(resultado)  # el mensaje de error


# =====================================================================
# EJERCICIO DEL MODULO 6
# =====================================================================
# Por que el menu usa 'while True' con un 'return' adentro, en vez de
# simplemente pedir el input UNA sola vez? Piensa tu respuesta, luego
# lee la explicacion abajo.

def ejercicio_modulo_6():
    respuesta = """
    Para permitir que el programa VUELVA A PREGUNTAR si el usuario se
    equivoca (escribe algo no numerico o un numero fuera de rango), en
    vez de fallar o continuar con un valor invalido. El 'return' dentro
    del ciclo es lo que efectivamente "rompe" el ciclo -- solo se llega
    ahi cuando el input es valido. Si usaras input() una sola vez sin
    ciclo, cualquier error del usuario haria fallar tu programa (o
    seguir con datos incorrectos).
    """
    print(respuesta)


# =====================================================================
# MAIN
# =====================================================================

if __name__ == "__main__":
    print("\n=== 6.2 Validar el input ===")
    seccion_6_2()

    print("\n=== 6.3 Construir un menu numerado ===")
    seccion_6_3()

    print("\n=== Ejercicio Modulo 6 ===")
    ejercicio_modulo_6()

    print("\n=== 6.4 Menu real con input() (interactivo) ===")
    try:
        elegido = menu()
        print("Elegiste:", elegido)
    except EOFError:
        print("(No hay teclado interactivo disponible en este entorno -- "
              "corre este archivo en tu propia terminal para probar el "
              "menu real escribiendo numeros de verdad.)")