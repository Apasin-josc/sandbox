"""
NIVEL 0 - Ejercicio 04: potencia

Calcula base^exp con exp >= 0, sin usar ** ni pow().
    potencia(2, 10) -> 1024
    potencia(5, 0)  -> 1

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : exp == 0 -> ___
3) COMBINAR   :
-------------------------------------------------------------------------------

BONUS FUERTE (este si aparece en entrevistas, LeetCode 50 "Pow(x, n)"):
tu version hace exp llamadas -> O(n). Se puede en O(log n) partiendo a la mitad:

    base^10 = (base^5)^2
    base^11 = (base^5)^2 * base

Implementa `potencia_rapida` abajo cuando termines la normal. Es el mismo salto
de fe, pero partiendo el problema en 2 en vez de restar 1 -- que es justo lo que
hace un arbol binario. No es coincidencia.
"""

from check import correr


def potencia(base: int, exp: int) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


def potencia_rapida(base: int, exp: int) -> int:
    """BONUS: O(log n). Deja el NotImplementedError si aun no llegas aqui."""
    raise NotImplementedError("bonus opcional")


CASOS = [
    ((2, 10), 1024),
    ((5, 0), 1),
    ((3, 3), 27),
    ((7, 1), 7),
]

if __name__ == "__main__":
    correr("potencia", potencia, CASOS)
    correr("potencia_rapida (bonus)", potencia_rapida, CASOS)
