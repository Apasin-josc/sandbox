"""
NIVEL 2 - Ejercicio 13: mismo arbol  (LeetCode 100)

Dos arboles son iguales si tienen la misma estructura Y los mismos valores.
    same_tree(build([1,2,3]), build([1,2,3])) -> True
    same_tree(build([1,2]),   build([1,None,2])) -> False

>>> FLUJO A con DOS arboles a la vez. Bajas por los dos en paralelo. <<<

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : aqui hay TRES situaciones. Ordenalas bien o te truena:
                  a) los dos son None -> ___
                  b) solo uno es None -> ___   (estructura distinta)
                  c) los dos existen pero p.val != q.val -> ___
                El orden importa: si preguntas p.val antes de descartar los None,
                te da AttributeError.
3) COMBINAR   : ¿deben coincidir AMBOS lados o basta uno? -> and / or
-------------------------------------------------------------------------------

BONUS FUERTE (LeetCode 101, "Symmetric Tree"): escribe `es_simetrico(root)`, que
dice si un arbol es espejo de si mismo. Pista: es casi este mismo codigo, pero
comparando izq contra der en cruz. Es un ejercicio buenisimo de "adaptar un patron
que ya conoces", que es literalmente lo que hace un senior en la entrevista.
"""

from typing import Optional

from check import correr
from tree_node import TreeNode, build


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


def es_simetrico(root: Optional[TreeNode]) -> bool:
    """BONUS. Deja el NotImplementedError si aun no llegas aqui."""
    raise NotImplementedError("bonus opcional")


CASOS = [
    ((build([1, 2, 3]), build([1, 2, 3])), True),
    ((build([1, 2]), build([1, None, 2])), False),
    ((build([]), build([])), True),
    ((build([1]), build([])), False),
    ((build([1, 2, 1]), build([1, 1, 2])), False),
]

CASOS_SIMETRICO = [
    ((build([1, 2, 2, 3, 4, 4, 3]),), True),
    ((build([1, 2, 2, None, 3, None, 3]),), False),
    ((build([]),), True),
]

if __name__ == "__main__":
    correr("same_tree", same_tree, CASOS)
    correr("es_simetrico (bonus)", es_simetrico, CASOS_SIMETRICO)
