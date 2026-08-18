"""
NIVEL 1 - Ejercicio 05: suma de una lista

Suma todos los elementos de una lista, recursivamente.
    suma_lista([1, 2, 3, 4]) -> 10
    suma_lista([])           -> 0

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : la lista vacia. ¿Cuanto suma una lista vacia?
3) COMBINAR   : nums[0] es el primero, nums[1:] es "todo lo demas".
                Si suma_lista(nums[1:]) ya funciona, ¿que le falta?
-------------------------------------------------------------------------------

NOTA DE EFICIENCIA (no cambia tu solucion, pero que lo sepas): nums[1:] copia la
lista, asi que esto es O(n^2) en memoria. La version "de verdad" pasa un indice:

    def helper(i): ...   # trabaja sobre nums[i:] sin copiar

Intenta las dos. La del indice es la que usaras en problemas reales, y es el
mismo patron con el que "bajaras" contexto en los arboles del Nivel 4.
"""

from typing import List

from check import correr


def suma_lista(nums: List[int]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    (([1, 2, 3, 4],), 10),
    (([],), 0),
    (([7],), 7),
    (([-1, 1, -1, 1],), 0),
]

if __name__ == "__main__":
    correr("suma_lista", suma_lista, CASOS)
