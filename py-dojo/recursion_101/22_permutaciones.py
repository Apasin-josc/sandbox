"""
NIVEL 5 - Ejercicio 22: permutaciones  (LeetCode 46)

Todas las ordenaciones posibles de una lista sin duplicados.
    permutaciones([1,2,3]) -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
El orden de las permutaciones entre si no importa.

-------------------------------------------------------------------------------
LA DIFERENCIA CON SUBSETS (y por que este va despues):

En subsets la decision era "¿incluyo nums[i]?" -> avanzabas con un indice.
Aqui la decision es "¿cual pongo AHORA?" -> tienes que recorrer TODOS los que
aun no has usado. Por eso el esqueleto lleva un for:

    def backtrack(camino, disponibles):
        if not disponibles:
            res.append(camino[:])
            return
        for x in disponibles:
            camino.append(x)
            backtrack(camino, disponibles - {x})   # o una lista sin x
            camino.pop()                            # DESHAGO

Dos formas de llevar "los que faltan", elige una:
    a) un set `usados` que agregas y quitas (mismo patron de deshacer)
    b) pasar una lista nueva sin el elegido: disponibles[:i] + disponibles[i+1:]

La (a) es mas eficiente, la (b) mas facil de razonar. Intenta las dos si te da
tiempo: comparar es donde se aprende.
-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : ¿cuando esta completa una permutacion?
3) ¿Que agregas y que deshaces en cada iteracion del for?
-------------------------------------------------------------------------------

CUANTAS SON: n! permutaciones. Con n=10 son 3.6 millones. Backtracking es
exponencial por naturaleza -- eso esta bien, el punto es no explorar ramas que
ya sabes que no sirven ("podar"). Eso lo ves en el 23.
"""

from typing import List

from check import correr


def permutaciones(nums: List[int]) -> List[List[int]]:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    (([1, 2, 3],), sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])),
    (([0, 1],), sorted([[0, 1], [1, 0]])),
    (([1],), [[1]]),
]

if __name__ == "__main__":
    # aqui NO usamos `ordenado`: ordenar por dentro destruiria las permutaciones
    correr("permutaciones", permutaciones, CASOS, normaliza=sorted)
