"""
NIVEL 5 - Ejercicio 21: subconjuntos  (LeetCode 78)

Dada una lista SIN duplicados, devuelve todos sus subconjuntos (el power set).
    subsets([1,2,3]) -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
El orden no importa (el test lo normaliza).

>>> BACKTRACKING: recursion + DESHACER. <<<

-------------------------------------------------------------------------------
LA IDEA: para cada elemento tomas una decision binaria -> lo incluyo o no.
Eso genera un ARBOL de decisiones. Recorrerlo es... DFS. Ya sabes hacerlo.

                    []
             /              \
          [1]                []            <- decido sobre el 1
        /     \            /    \
     [1,2]    [1]       [2]      []        <- decido sobre el 2
      / \      / \      / \      / \
   ...       ...      ...      ...         <- decido sobre el 3

Cada HOJA de ese arbol es una respuesta. Por eso backtracking se siente como
trees: es literalmente un DFS sobre un arbol que no existe en memoria, lo vas
construyendo con tus decisiones.

LA RECETA (memorizala, es la misma para los 3 ejercicios del nivel):

    def backtrack(i, camino):
        if i == len(nums):
            res.append(camino[:])   # <-- ¡COPIA!
            return
        camino.append(nums[i])      # decision 1: lo incluyo
        backtrack(i + 1, camino)
        camino.pop()                # DESHAGO  <-- esto es el backtracking
        backtrack(i + 1, camino)    # decision 2: no lo incluyo
-------------------------------------------------------------------------------
1) CONTRATO   : backtrack(i, camino) significa "ya decidi sobre los primeros i
                elementos y llevo `camino`; ahora explora el resto"
2) CASO BASE  : cuando ya no quedan elementos por decidir -> i == ___
3) ¿Por que `camino[:]` y no `camino`?  (SI no lo sabes, pruebalo sin la copia
   y mira que sale. Ese experimento vale mas que la explicacion.)
-------------------------------------------------------------------------------

EL `pop()` ES TODO. Sin el, `camino` se contamina entre ramas: te llevas basura
de una rama a la siguiente. Regla: "lo que agregas antes de bajar, lo quitas al
subir". Todo el estado compartido debe quedar como lo encontraste.
"""

from typing import List

from check import correr, ordenado


def subsets(nums: List[int]) -> List[List[int]]:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    (([1, 2, 3],), ordenado([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])),
    (([1],), ordenado([[], [1]])),
    (([],), ordenado([[]])),
    (([1, 2],), ordenado([[], [1], [2], [1, 2]])),
]

if __name__ == "__main__":
    correr("subsets", subsets, CASOS, normaliza=ordenado)
