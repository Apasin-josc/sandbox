"""
NIVEL 3 - Ejercicio 14: diametro del arbol  (LeetCode 543)

El diametro es la longitud (en ARISTAS) del camino mas largo entre dos nodos
cualesquiera. Ese camino NO tiene por que pasar por la raiz.

    build([1,2,3,4,5]) -> 3     (4 -> 2 -> 1 -> 3)
    build([1,2])       -> 1
    build([1])         -> 0

>>> FLUJO C: aparece el ESTADO GLOBAL. Aqui esta el salto conceptual del nivel. <<<

-------------------------------------------------------------------------------
EL PROBLEMA DE FONDO, y es EL concepto de este nivel:

Tu padre necesita saber tu ALTURA (para calcular su propio camino).
Pero la respuesta que buscas es el DIAMETRO.
Son dos cosas distintas y una sola funcion no puede devolver las dos... a menos
que las separes:

    - lo que le devuelvo a mi padre  -> va en el `return`   (la altura)
    - la respuesta que voy juntando  -> va en un `nonlocal` (el diametro)

En CADA nodo te preguntas: "si el camino mas largo pasara justo por MI, ¿cuanto
mediria?" -> altura_izq + altura_der. Guardas el maximo de todos. Ya.
-------------------------------------------------------------------------------
1) CONTRATO del dfs :
2) CASO BASE        :
3) COMBINAR         :
4) ¿Que actualizo en el nonlocal y en que momento?
-------------------------------------------------------------------------------

Cuando este te salga y entiendas POR QUE, ya desbloqueaste el 70% de los
"medium" de arboles. En serio. Este es el problema bisagra de toda la carpeta.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def diametro(root: Optional[TreeNode]) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((build([1, 2, 3, 4, 5]),), 3),
    ((build([1, 2]),), 1),
    ((build([1]),), 0),
    ((build([]),), 0),
    ((build([1, None, 2, None, 3]),), 2),
]

if __name__ == "__main__":
    correr("diametro", diametro, CASOS)
