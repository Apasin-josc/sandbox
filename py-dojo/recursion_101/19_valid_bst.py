"""
NIVEL 4 - Ejercicio 19: validar arbol binario de busqueda  (LeetCode 98)

Un BST valido cumple, para CADA nodo:
    - TODO el subarbol izquierdo tiene valores < node.val
    - TODO el subarbol derecho tiene valores > node.val
    (estrictamente; sin duplicados)

    build([2,1,3])              -> True
    build([5,1,4,None,None,3,6]) -> False

>>> FLUJO B en su forma mas elegante: bajan LIMITES (min, max). <<<

-------------------------------------------------------------------------------
LA TRAMPA #1 DE TODA LA CARPETA -- casi todo mundo escribe esto:

    return (root.left.val < root.val and root.right.val > root.val
            and valid(root.left) and valid(root.right))

y esta MAL. Mira este arbol:

         5
        / \
       1   4        <- 4 < 5, invalido... pero comparando solo padre-hijo,
          / \          el 3 se ve bien respecto a su padre 4
         3   6

El 3 es menor que su padre 4, pero esta a la DERECHA del 5, o sea deberia ser
mayor que 5. Comparar solo con el padre no basta: cada nodo tiene que respetar a
TODOS sus ancestros.

LA SOLUCION: cada nodo baja un RANGO permitido a sus hijos.

    dfs(node, lo, hi)  ->  "¿es valido este subarbol sabiendo que todos sus
                            valores deben estar estrictamente entre lo y hi?"

    - al ir a la IZQUIERDA: el techo se aprieta  -> dfs(node.left,  lo, node.val)
    - al ir a la DERECHA:   el piso se aprieta   -> dfs(node.right, node.val, hi)
    - la raiz arranca sin limites -> float("-inf"), float("inf")
-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : un subarbol vacio, ¿es un BST valido?
3) COMBINAR   :
-------------------------------------------------------------------------------

Este problema es EL ejemplo canonico de "la informacion baja". Si lo entiendes,
entendiste el Flujo B para siempre.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def valid_bst(root: Optional[TreeNode]) -> bool:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([2, 1, 3]),), True),
    ((build([5, 1, 4, None, None, 3, 6]),), False),
    ((build([]),), True),
    ((build([1]),), True),
    ((build([1, 1]),), False),           # duplicados no valen
    ((build([5, 4, 6, None, None, 3, 7]),), False),  # el caso del dibujo
]

if __name__ == "__main__":
    correr("valid_bst", valid_bst, CASOS)
