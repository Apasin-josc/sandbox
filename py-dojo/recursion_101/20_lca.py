"""
NIVEL 4 - Ejercicio 20: ancestro comun mas bajo  (LeetCode 236, arbol general)

Dado un arbol y dos nodos p y q, devuelve el nodo mas profundo que es ancestro de
ambos. (Un nodo puede ser ancestro de si mismo.)

           3
         /   \
        5     1
       / \   / \
      6   2 0   8
         / \
        7   4

    lca(root, 5, 1) -> 3
    lca(root, 5, 4) -> 5   (5 es ancestro de si mismo)

-------------------------------------------------------------------------------
LA FORMA DE PENSARLO (es preciosa y da 6 lineas):

Que devuelva dfs(node):
    - None            si ni p ni q estan en este subarbol
    - p (o q)         si encontro uno de ellos aqui abajo
    - el LCA          si ya lo encontro

Con ese contrato, en cada nodo te preguntas:
    izq = dfs(node.left)
    der = dfs(node.right)
    - si AMBOS lados devolvieron algo -> p esta de un lado y q del otro
                                      -> ¡YO soy el LCA!
    - si solo uno devolvio algo       -> paso ese hacia arriba
    - si yo mismo soy p o q           -> me devuelvo a mi mismo

Nota que este es FLUJO A (todo sube), pero con un contrato de retorno mas rico
que un simple numero. Esa es la lección del ejercicio: el `return` puede llevar
lo que tu quieras, mientras el CONTRATO sea claro.
-------------------------------------------------------------------------------
1) CONTRATO   : (ya te lo di arriba -- reescribelo con tus palabras, en serio)
2) CASO BASE  : ¿que devuelve un nodo nulo? ¿y si node es p o node es q?
3) COMBINAR   :
-------------------------------------------------------------------------------

BONUS (LeetCode 235): si el arbol es un BST, se resuelve MUCHO mas facil sin ni
siquiera explorar los dos lados. Piensa que te dice la propiedad del BST sobre
donde estan p y q respecto al nodo actual.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def buscar(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Helper YA RESUELTO (para armar los casos). Leelo: tambien es Flujo A."""
    if not root:
        return None
    if root.val == val:
        return root
    return buscar(root.left, val) or buscar(root.right, val)


def lca(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


_t = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
_s = build([2, 1, 3])

CASOS = [
    ((_t, buscar(_t, 5), buscar(_t, 1)), 3),
    ((_t, buscar(_t, 5), buscar(_t, 4)), 5),
    ((_t, buscar(_t, 7), buscar(_t, 4)), 2),
    ((_t, buscar(_t, 6), buscar(_t, 8)), 3),
    ((_s, buscar(_s, 1), buscar(_s, 3)), 2),
]

if __name__ == "__main__":
    correr("lca", lca, CASOS, normaliza=lambda n: n.val if n else None)
