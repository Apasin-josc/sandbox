"""
NIVEL 4 - Ejercicio 17: suma de camino  (LeetCode 112)

¿Existe un camino de la RAIZ a una HOJA cuyos valores sumen exactamente `target`?

    path_sum(build([5,4,8,11,None,13,4,7,2]), 22) -> True   (5+4+11+2)
    path_sum(build([1,2,3]), 5)                   -> False
    path_sum(build([]), 0)                        -> False  (sin nodos no hay camino)

>>> FLUJO B: la informacion BAJA. Primer problema donde el contexto viaja hacia
    abajo como PARAMETRO en vez de subir como return. <<<

-------------------------------------------------------------------------------
LA DIFERENCIA CON EL NIVEL 3:

En el nivel 3 los hijos le informaban al padre. Aqui es al reves: el padre le
dice al hijo "oye, hasta aqui llevamos acumulado X". Eso se hace agregando un
PARAMETRO:

    def dfs(node, restante):   # o (node, acumulado), como prefieras
        ...
        dfs(node.left, restante - node.val)

Dos formas equivalentes de plantearlo, elige una:
    - ir RESTANDO del target y preguntar si llegas a 0 en la hoja, o
    - ir SUMANDO y comparar contra target en la hoja.
-------------------------------------------------------------------------------
1) CONTRATO   : dfs(node, restante) devuelve _______________
2) CASO BASE  : aqui SI necesitas detectar la HOJA (not node.left and not node.right),
                porque el problema dice explicitamente "hasta una hoja".
                ¡Ojo! Sigue necesitando el caso `if not node: return False` para
                los nodos con un solo hijo. Piensa por que.
3) COMBINAR   : ¿basta con que UNO de los dos lados funcione? -> and / or
-------------------------------------------------------------------------------

REGLA PRACTICA que vale para todo trees:
    "desde la raiz hasta aqui"  -> la info BAJA (parametro)
    "desde aqui hacia abajo"    -> la info SUBE  (return)
Leer el enunciado buscando cual de las dos frases es, te dice como escribirlo.

BONUS (LeetCode 113): `todos_los_caminos(root, target)` que devuelva la LISTA de
caminos que suman target. Ahi vas a necesitar tambien el `camino.pop()` del
Nivel 5 -- es el puente natural a backtracking.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def path_sum(root: Optional[TreeNode], target: int) -> bool:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([5, 4, 8, 11, None, 13, 4, 7, 2]), 22), True),
    ((build([1, 2, 3]), 5), False),
    ((build([]), 0), False),
    ((build([1, 2]), 3), True),
    ((build([1, 2]), 1), False),  # 1 no es hoja, no cuenta
]

if __name__ == "__main__":
    correr("path_sum", path_sum, CASOS)
