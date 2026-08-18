"""
NIVEL 2 - Ejercicio 11: contar nodos y sumar valores

Dos funciones, mismo esqueleto. Hazlas seguidas a proposito: quiero que veas que
son LA MISMA recursion cambiando dos cosas (el neutro y la operacion).

    contar_nodos(build([1,2,3]))  -> 3
    suma_valores(build([1,2,3]))  -> 6

>>> FLUJO A: la informacion SUBE. <<<

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : ¿cual es el NEUTRO en cada caso? (para contar ___, para sumar ___)
3) COMBINAR   :
-------------------------------------------------------------------------------

Cuando termines, compara las dos funciones lado a lado. La plantilla es:

    if not root: return NEUTRO
    return OPERACION(algo_de_este_nodo, f(root.left), f(root.right))

Interiorizar esa plantilla vale mas que memorizar 50 problemas.

BONUS: escribe `altura_minima` (el camino MAS CORTO a una hoja). Ojo, no es
cambiar max por min sin pensar: un nodo con un solo hijo te daria 0 por el lado
nulo, y eso es incorrecto. Piensa por que.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def contar_nodos(root: Optional[TreeNode]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


def suma_valores(root: Optional[TreeNode]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS_CONTAR = [
    ((build([1, 2, 3]),), 3),
    ((build([]),), 0),
    ((build([1]),), 1),
    ((build([3, 9, 20, None, None, 15, 7]),), 5),
]

CASOS_SUMAR = [
    ((build([1, 2, 3]),), 6),
    ((build([]),), 0),
    ((build([5]),), 5),
    ((build([3, 9, 20, None, None, 15, 7]),), 54),
]

if __name__ == "__main__":
    correr("contar_nodos", contar_nodos, CASOS_CONTAR)
    correr("suma_valores", suma_valores, CASOS_SUMAR)
