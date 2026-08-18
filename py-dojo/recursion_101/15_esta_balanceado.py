"""
NIVEL 3 - Ejercicio 15: arbol balanceado  (LeetCode 110)

Un arbol esta balanceado si para CADA nodo, las alturas de sus dos subarboles
difieren en a lo mas 1.

    build([3,9,20,None,None,15,7])   -> True
    build([1,2,2,3,3,None,None,4,4]) -> False

-------------------------------------------------------------------------------
INTENTO INGENUO (hazlo primero, en serio):

    def esta_balanceado(root):
        if not root: return True
        return (abs(altura(root.left) - altura(root.right)) <= 1
                and esta_balanceado(root.left)
                and esta_balanceado(root.right))

Funciona, pero es O(n^2): recalculas alturas una y otra vez. En una entrevista
esto te lo aceptan y luego te dicen "¿lo puedes hacer en O(n)?".

LA VERSION O(n) -- el patron que quiero que aprendas:
Un solo recorrido que devuelve DOS cosas a la vez. Dos formas de lograrlo:

    a) devolver una tupla:   return (esta_balanceado, altura)
    b) usar un nonlocal para el bool y devolver solo la altura  (como el 14)
    c) truco: devolver la altura, pero -1 como "bandera de que ya no balancea"

Implementa la (a) o la (b). La (c) es elegante pero mezcla dos significados en
un mismo valor de retorno: rompe el principio de "un contrato, una funcion", y
por eso es mas facil de arruinar. Sabela leer, no la uses como default.
-------------------------------------------------------------------------------
1) CONTRATO del helper : devuelve ___________________
2) CASO BASE           :
3) COMBINAR            :
-------------------------------------------------------------------------------

Idea clave: "devolver mas de una cosa desde la recursion" es una tecnica que vas
a reusar muchisimo (validar BST, contar subarboles, etc.).
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def esta_balanceado(root: Optional[TreeNode]) -> bool:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([3, 9, 20, None, None, 15, 7]),), True),
    ((build([1, 2, 2, 3, 3, None, None, 4, 4]),), False),
    ((build([]),), True),
    ((build([1]),), True),
    ((build([1, 2, None, 3]),), False),
]

if __name__ == "__main__":
    correr("esta_balanceado", esta_balanceado, CASOS)
