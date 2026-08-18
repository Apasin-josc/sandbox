"""
NIVEL 5 - Ejercicio 23: combination sum  (LeetCode 39)  [el jefe final]

Dada una lista de candidatos distintos y un target, devuelve todas las
combinaciones UNICAS que suman exactamente target. Puedes usar el mismo numero
las veces que quieras.

    combination_sum([2,3,6,7], 7) -> [[2,2,3], [7]]
    combination_sum([2,3,5], 8)   -> [[2,2,2,2], [2,3,3], [3,5]]

-------------------------------------------------------------------------------
AQUI SE JUNTA TODO LO DE LA CARPETA:

  - backtracking con append/pop            (nivel 5)
  - contexto que BAJA: cuanto falta        (nivel 4, flujo B)
  - dos casos base, uno bueno y uno malo   (nivel 0)
  - PODA: cortar ramas que ya no sirven    (nuevo)

LOS DOS CASOS BASE:
    if restante == 0:  guardo camino[:] y regreso     <- exito
    if restante < 0:   regreso sin guardar             <- me pase, PODA

LA PARTE FINA -- evitar duplicados:
[2,2,3] y [2,3,2] son la MISMA combinacion, no la quieres dos veces. El truco es
pasar un indice `start` y en el for empezar SIEMPRE en `start`, nunca en 0:

    for i in range(start, len(candidatos)):
        camino.append(candidatos[i])
        backtrack(i, restante - candidatos[i], camino)   # <- i, NO i+1
        camino.pop()

  - `i` (no `i+1`) porque SI puedo repetir el mismo numero
  - empezar en `start` (no en 0) porque asi solo genero combinaciones en orden
    no-decreciente, y cada combinacion aparece una sola vez

Esas dos decisiones de una letra son la diferencia entre este problema y sus
primos (LeetCode 40 usa i+1, LeetCode 46 empieza en 0). Entiende POR QUE cada
una, y ya te llevaste toda la familia de problemas de combinaciones.
-------------------------------------------------------------------------------
1) CONTRATO   : backtrack(start, restante, camino) =
2) CASO BASE  :
3) ¿Que deshaces?
-------------------------------------------------------------------------------

Si terminas este ejercicio entendiendolo: ya puedes con la seccion de Trees y de
Backtracking de NeetCode completas, y estas listo para graphs. Neta.
"""

from typing import List

from check import correr, ordenado


def combination_sum(candidatos: List[int], target: int) -> List[List[int]]:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    (([2, 3, 6, 7], 7), ordenado([[2, 2, 3], [7]])),
    (([2, 3, 5], 8), ordenado([[2, 2, 2, 2], [2, 3, 3], [3, 5]])),
    (([2], 1), ordenado([])),
    (([1, 2], 4), ordenado([[1, 1, 1, 1], [1, 1, 2], [2, 2]])),
]

if __name__ == "__main__":
    correr("combination_sum", combination_sum, CASOS, normaliza=ordenado)
