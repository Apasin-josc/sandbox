"""
NIVEL 2 - Ejercicio 10: profundidad maxima  (LeetCode 104)

Devuelve la cantidad de nodos del camino mas largo desde la raiz hasta una hoja.
    build([3,9,20,None,None,15,7]) -> 3
    build([])                      -> 0

>>> FLUJO A: la informacion SUBE. Cada nodo pregunta a sus hijos y devuelve. <<<

-------------------------------------------------------------------------------
1) CONTRATO   : recibe un nodo y devuelve _______________ del subarbol que
                cuelga de ESE nodo (no del arbol completo -- esto importa)
2) CASO BASE  : if not root -> ___
                (usa el nodo NULO como caso base, no la hoja. Con la hoja te
                 vas a tropezar con los nodos que solo tienen un hijo.)
3) COMBINAR   : SALTO DE FE: ya tengo la profundidad de izquierda y de derecha.
                ¿Que hago con esas dos para dar la mia?
-------------------------------------------------------------------------------

Este es el "hola mundo" de los arboles. Sale en 3 lineas. Si te sale sin ver la
solucion, ya tienes la Receta 2 -- y con ella resuelves los siguientes tres.

Nota: ya lo tienes resuelto en neetcode/trees/max_depth.py. Hazlo aqui SIN verlo.
La meta no es tener la respuesta, es poder llegar a ella otra vez.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def max_depth(root: Optional[TreeNode]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([3, 9, 20, None, None, 15, 7]),), 3),
    ((build([]),), 0),
    ((build([1]),), 1),
    ((build([1, 2, None, 3, None, 4]),), 4),  # arbol totalmente chueco
]

if __name__ == "__main__":
    correr("max_depth", max_depth, CASOS)
