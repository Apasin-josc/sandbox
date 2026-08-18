"""
NIVEL 2 - Ejercicio 12: invertir arbol binario  (LeetCode 226)

Espeja el arbol: cada nodo intercambia su hijo izquierdo con el derecho.

        4                 4
      /   \             /   \
     2     7    ->     7     2
    / \   / \         / \   / \
   1   3 6   9       9   6 3   1

    invertir(build([4,2,7,1,3,6,9])) -> [4,7,2,9,6,3,1]

>>> FLUJO A, pero ahora el return NO es un numero: es un NODO. <<<

-------------------------------------------------------------------------------
1) CONTRATO   : recibe un nodo y devuelve _______________
                (dilo completo: "devuelve la raiz del subarbol YA invertido")
2) CASO BASE  : un arbol vacio invertido es ___
3) COMBINAR   : SALTO DE FE: invertir(root.left) me devuelve el subarbol izquierdo
                ya invertido, igual el derecho. Ahora solo me falta... ¿que?
-------------------------------------------------------------------------------

TRAMPA CLASICA: si haces
        root.left = invertir(root.right)
        root.right = invertir(root.left)   # <-- root.left YA cambio!
te sale mal. En Python se arregla con asignacion simultanea:
        root.left, root.right = invertir(root.right), invertir(root.left)
o guardando en variables temporales primero. Este bug es MUY comun, tenlo presente.

Fun fact: este es el problema por el que rechazaron al creador de Homebrew en
Google. Ahora ya lo sabes hacer.
"""

from typing import Optional

from check import correr, arbol
from tree_node import TreeNode, build


def invertir(root: Optional[TreeNode]) -> Optional[TreeNode]:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([4, 2, 7, 1, 3, 6, 9]),), "[4, 7, 2, 9, 6, 3, 1]"),
    ((build([2, 1, 3]),), "[2, 3, 1]"),
    ((build([]),), "None"),
    ((build([1, 2]),), "[1, None, 2]"),
]

if __name__ == "__main__":
    correr("invertir", invertir, CASOS, normaliza=arbol)
