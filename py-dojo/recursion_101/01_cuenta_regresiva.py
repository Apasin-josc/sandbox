"""
NIVEL 0 - Ejercicio 01: cuenta regresiva

Dado un entero n >= 0, devuelve la lista [n, n-1, ..., 1].
    cuenta_regresiva(3) -> [3, 2, 1]
    cuenta_regresiva(0) -> []

REGLA: nada de bucles. Solo recursion. Es a proposito: aqui entrenas la plantilla,
no el algoritmo.

-------------------------------------------------------------------------------
LLENA LAS 3 PREGUNTAS ANTES DE CODEAR (escribelo, no lo pienses nomas):

1) CONTRATO   : recibe ___________ y devuelve ___________
2) CASO BASE  : cuando n == ___ la respuesta es ___ (sin recursion)
3) COMBINAR   : si cuenta_regresiva(n-1) YA me da la lista correcta,
                ¿como construyo la de n a partir de ella?
-------------------------------------------------------------------------------

PISTA (tapala si quieres): en Python, [n] + otra_lista concatena.
"""

from typing import List

from check import correr


def cuenta_regresiva(n: int) -> List[int]:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((3,), [3, 2, 1]),
    ((1,), [1]),
    ((0,), []),
    ((5,), [5, 4, 3, 2, 1]),
]

if __name__ == "__main__":
    correr("cuenta_regresiva", cuenta_regresiva, CASOS)
