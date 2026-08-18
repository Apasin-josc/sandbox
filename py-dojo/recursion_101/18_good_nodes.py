"""
NIVEL 4 - Ejercicio 18: nodos buenos  (LeetCode 1448)

Un nodo X es "bueno" si en el camino de la raiz hasta X no hay ningun nodo con
valor MAYOR que X. Cuenta cuantos nodos buenos hay.

    build([3,1,4,3,None,1,5]) -> 4
    build([3,3,None,4,2])     -> 3
    build([1])                -> 1   (la raiz siempre es buena)

>>> FLUJO B + FLUJO C juntos: el maximo del camino BAJA, el contador es GLOBAL. <<<

-------------------------------------------------------------------------------
Este ejercicio existe para que veas que los flujos se COMBINAN. Se ve dificil y
son 8 lineas:

    - lo que baja  : el maximo visto en el camino desde la raiz hasta mi padre
    - lo que sube  : nada, no necesito nada de mis hijos
    - lo global    : el contador

(Tambien se puede resolver haciendo que el conteo SUBA como return, sumando
izq + der + (1 si soy bueno). Las dos son validas -- intenta las dos, es el
mejor ejercicio de la carpeta para sentir la diferencia entre flujos.)
-------------------------------------------------------------------------------
1) CONTRATO del dfs :
2) CASO BASE        :
3) ¿Con que valor arranca el "maximo del camino" en la raiz?
   (pista: si usas 0, un arbol de puros negativos te da mal. Usa root.val o -inf)
-------------------------------------------------------------------------------
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def good_nodes(root: Optional[TreeNode]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([3, 1, 4, 3, None, 1, 5]),), 4),
    ((build([3, 3, None, 4, 2]),), 3),
    ((build([1]),), 1),
    ((build([]),), 0),
    # solo la raiz es buena. Si inicializas el maximo en 0, este te da 0 en vez de 1
    ((build([-1, -2, -3]),), 1),
]

if __name__ == "__main__":
    correr("good_nodes", good_nodes, CASOS)
