"""
NIVEL 3 - Ejercicio 16: maxima suma de camino  (LeetCode 124)  [HARD]

Un "camino" es cualquier secuencia de nodos conectados padre-hijo. NO tiene que
pasar por la raiz y NO puede repetir nodos (o sea: no puede bajar, subir y volver
a bajar por el mismo lado). Devuelve la suma maxima de un camino.

    build([1,2,3])                     -> 6    (2 -> 1 -> 3)
    build([-10,9,20,None,None,15,7])   -> 42   (15 -> 20 -> 7)
    build([-3])                        -> -3   (un solo nodo tambien es camino)

>>> Es el ejercicio 14 (diametro) con esteroides. Mismo esqueleto exacto. <<<

-------------------------------------------------------------------------------
LAS DOS IDEAS QUE TIENES QUE SEPARAR (identicas al 14):

  a) LO QUE REPORTO HACIA ARRIBA (el `return`):
     mi padre solo puede usarme si el camino SIGUE subiendo, asi que solo puede
     tomar UNA de mis dos ramas:
         return node.val + max(izq, der)

  b) LA RESPUESTA GLOBAL (el `nonlocal`):
     el mejor camino podria "doblar" justo en mi, usando MIS DOS ramas:
         res = max(res, node.val + izq + der)

LA VUELTA DE TUERCA -- los negativos:
Si una rama suma negativo, no la uso: mejor cortar ahi. Se maneja con

    izq = max(dfs(node.left), 0)     # "si me perjudica, la ignoro"
    der = max(dfs(node.right), 0)

Ese `max(..., 0)` es todo el truco del problema. Piensa por que funciona antes
de escribirlo.
-------------------------------------------------------------------------------
1) CONTRATO del dfs :
2) CASO BASE        : ¿que devuelve un nodo nulo aqui, y por que 0 y no -inf?
3) ¿Con que valor inicializas `res`? (ojo: 0 esta MAL si todos son negativos)
-------------------------------------------------------------------------------

Este es un HARD de LeetCode y lo vas a poder. Si hiciste el 14, ya lo sabes:
es literalmente el mismo codigo con otra operacion.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def max_path_sum(root: Optional[TreeNode]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([1, 2, 3]),), 6),
    ((build([-10, 9, 20, None, None, 15, 7]),), 42),
    ((build([-3]),), -3),
    ((build([2, -1]),), 2),
    ((build([-2, -1]),), -1),
]

if __name__ == "__main__":
    correr("max_path_sum", max_path_sum, CASOS)
