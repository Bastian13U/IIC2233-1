"""
MODULO 8 - Examen simulado
IIC2233 - Preparacion intensiva para el ejercicio de Sudoku por Backtracking

Objetivo: ponerte a prueba con las mismas preguntas que cubren los
modulos 1 a 7. Respondelas en papel ANTES de ver las respuestas.

Ejecuta:  python 08_examen_simulado.py
El programa muestra las 10 preguntas, espera que presiones Enter
(si hay teclado disponible), y luego revela todas las respuestas
explicadas.
"""


PREGUNTAS = [
    "1) (concepto) Explica que son el 'caso base' y el 'caso recursivo' "
    "en una funcion recursiva, y da un ejemplo DISTINTO a los usados en "
    "la guia.",

    "2) (dry run) Que imprime este codigo?\n"
    "     tablero = [[1,2],[3,4]]\n"
    "     print(tablero[1][0])\n"
    "     print(tablero[0][1])",

    "3) (completar) Completa la funcion para que devuelva True si "
    "'numero' NO esta repetido en la columna 'columna' del tablero:\n"
    "     def columna_valida(tablero, columna, numero):\n"
    "         for fila in range(9):\n"
    "             if _______________:\n"
    "                 return False\n"
    "         return True",

    "4) (concepto) En el patron elegir/explorar/deshacer, que pasaria "
    "si tu funcion resolver() NO tuviera caso base (nunca hay un "
    "'return True' cuando el tablero esta completo)?",

    "5) (calculo) Dada la celda (fila=7, columna=4), calcula "
    "caja_fila_inicio y caja_columna_inicio.",

    "6) (escribir desde cero) Escribe una funcion contar_vacias(tablero) "
    "que devuelva cuantas celdas del tablero tienen valor 0.",

    "7) (archivos) Que hace .strip() sobre una linea leida de un "
    "archivo, y por que es necesario antes de convertirla en una lista "
    "de enteros?",

    "8) (orden) Ordena estos pasos segun el orden real en que ocurren "
    "cuando resolver(tablero) encuentra que NINGUN numero funciona en "
    "la celda actual:\n"
    "     a) Se prueba el numero 9 y es_valido devuelve False.\n"
    "     b) Se llega a la celda (fila, columna) actual.\n"
    "     c) La funcion devuelve False.\n"
    "     d) Se prueban los numeros 1 a 8 y ninguno es valido.",

    "9) (trace) Con esta funcion simplificada:\n"
    "     def resolver_mini(lista, indice):\n"
    "         if indice == len(lista):\n"
    "             return True\n"
    "         for numero in range(1, 4):\n"
    "             if numero not in lista[:indice]:\n"
    "                 lista[indice] = numero\n"
    "                 if resolver_mini(lista, indice + 1):\n"
    "                     return True\n"
    "                 lista[indice] = 0\n"
    "         return False\n"
    "     lista = [0, 0, 0]\n"
    "     resolver_mini(lista, 0)\n"
    "     print(lista)\n"
    "   Que imprime?",

    "10) (aplicada) Por que el enunciado dice que puedes asumir que el "
    "puzle tiene AL MENOS una solucion, y que pasaria en tu programa "
    "si un puzle no tuviera ninguna?",
]


RESPUESTAS = [
    "R1) El caso base es la condicion que detiene la recursion sin "
    "hacer mas llamadas (evita recursion infinita); el caso recursivo "
    "es la parte donde la funcion se llama a si misma con una version "
    "mas pequena del problema. Ejemplo: contar los elementos de una "
    "lista recursivamente -- caso base: lista vacia devuelve 0; caso "
    "recursivo: 1 + contar(resto de la lista).",

    "R2) Imprime:\n     3\n     2\n"
    "   tablero[1][0] es la fila indice 1 ([3,4]), columna indice 0 -> 3.\n"
    "   tablero[0][1] es la fila indice 0 ([1,2]), columna indice 1 -> 2.",

    "R3) if tablero[fila][columna] == numero:",

    "R4) El programa nunca terminaria de forma exitosa aunque el "
    "tablero quedara completo -- seguiria intentando buscar una celda "
    "vacia con encontrar_celda_vacia, que devolveria None, pero como "
    "no hay ningun 'if celda_vacia is None: return True', el codigo "
    "probablemente lanzaria un TypeError al intentar desempaquetar "
    "None en (fila, columna).",

    "R5) fila=7 -> 7 // 3 = 2 -> caja_fila_inicio = 6.\n"
    "    columna=4 -> 4 // 3 = 1 -> caja_columna_inicio = 3.",

    "R6) def contar_vacias(tablero):\n"
    "        contador = 0\n"
    "        for fila in range(9):\n"
    "            for columna in range(9):\n"
    "                if tablero[fila][columna] == 0:\n"
    "                    contador += 1\n"
    "        return contador",

    "R7) .strip() elimina espacios en blanco y el caracter de salto de "
    "linea (\\n) al inicio y al final del string. Es necesario porque "
    "cada linea leida de un archivo de texto normalmente incluye un "
    "\\n al final, y si intentas convertir ese caracter con int(), "
    "lanzara un ValueError porque '\\n' no es un digito valido.",

    "R8) Orden correcto: b, d, a, c.\n"
    "    Primero se llega a la celda (b), se prueban los numeros 1 a 8 "
    "sin exito (d), se prueba el 9 y tambien falla (a), y finalmente "
    "se devuelve False porque se agotaron todas las opciones (c).",

    "R9) Imprime: [1, 2, 3]\n"
    "    El algoritmo siempre prueba desde el numero mas bajo "
    "disponible: coloca 1 en el indice 0; para el indice 1 prueba 1 "
    "(usado, se salta), prueba 2 (libre, lo coloca); para el indice 2 "
    "prueba 1 y 2 (usados), prueba 3 (libre, lo coloca). Como nunca "
    "hace falta retroceder, el resultado es simplemente los numeros en "
    "orden. (Puedes verificarlo abajo con codigo real.)",

    "R10) A diferencia de los sudokus disenados para humanos (que "
    "siempre tienen solucion unica), un algoritmo de backtracking "
    "'ingenuo' tambien debe poder manejar el caso sin solucion sin "
    "fallar. Si un puzle no tuviera solucion, resolver() recorreria "
    "exhaustivamente todas las combinaciones posibles, no encontraria "
    "ninguna valida, y terminaria devolviendo False en la primera "
    "llamada (la de main), por lo que el programa deberia simplemente "
    "informarlo (como hace el 'else' en main()), en vez de fallar con "
    "un error o quedar en un ciclo infinito.",
]


def resolver_mini(lista, indice):
    """Codigo real de la Pregunta 9, para verificar la respuesta en vivo."""
    if indice == len(lista):
        return True
    for numero in range(1, 4):
        if numero not in lista[:indice]:
            lista[indice] = numero
            if resolver_mini(lista, indice + 1):
                return True
            lista[indice] = 0
    return False


def verificar_pregunta_9():
    lista = [0, 0, 0]
    resolver_mini(lista, 0)
    print("Resultado real de ejecutar el codigo de la Pregunta 9:", lista)


def mostrar_examen():
    print("=" * 70)
    print(" EXAMEN SIMULADO -- responde en papel ANTES de ver las respuestas")
    print("=" * 70)
    for pregunta in PREGUNTAS:
        print("\n" + pregunta)


def mostrar_respuestas():
    print("\n" + "=" * 70)
    print(" RESPUESTAS")
    print("=" * 70)
    for respuesta in RESPUESTAS:
        print("\n" + respuesta)

    print("\n" + "-" * 70)
    verificar_pregunta_9()

    print("\nPuntaje sugerido: si respondiste 8/10 o mas SIN mirar la guia, "
          "estas listo. Si fallaste alguna, vuelve al modulo correspondiente "
          "(ver el numero de modulo entre parentesis en cada pregunta) y "
          "repite su ejercicio antes de seguir.")


if __name__ == "__main__":
    mostrar_examen()
    print("\n" + "=" * 70)
    try:
        input("\nPresiona Enter cuando hayas respondido todo en papel, "
              "para revelar las respuestas...")
    except EOFError:
        print("(Sin teclado interactivo: mostrando respuestas automaticamente. "
              "Corre este archivo en tu propia terminal para hacer la pausa real.)")
    mostrar_respuestas()