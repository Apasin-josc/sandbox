"""
NIVEL 1 - Ejercicio 07: es palindromo

Un string es palindromo si se lee igual al derecho y al reves.
    es_palindromo("reconocer") -> True
    es_palindromo("hola")      -> False
    es_palindromo("")          -> True   (vacio y de 1 letra son palindromos)

Asume que ya viene limpio: solo minusculas, sin espacios ni acentos.

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : OJO, aqui hay DOS casos base. ¿Cuales? (len 0 y len 1)
3) COMBINAR   : compara los extremos. Si coinciden, ¿que subproblema queda?
                Si NO coinciden, ¿hace falta seguir?
-------------------------------------------------------------------------------

Este es tu primer problema con recursion BOOLEANA. El patron es:

    return condicion_local and f(subproblema)

Y ese `and` te da cortocircuito gratis: si la condicion local falla, Python ni
siquiera hace la llamada recursiva. Esa es exactamente la forma de tu isSameTree.
"""

from check import correr


def es_palindromo(s: str) -> bool:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    (("reconocer",), True),
    (("hola",), False),
    (("",), True),
    (("a",), True),
    (("abba",), True),
    (("abca",), False),
]

if __name__ == "__main__":
    correr("es_palindromo", es_palindromo, CASOS)
