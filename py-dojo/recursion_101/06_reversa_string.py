"""
NIVEL 1 - Ejercicio 06: reversa de un string

    reversa("hola") -> "aloh"
    reversa("")     -> ""

Sin s[::-1], sin reversed(), sin bucles. Recursion pura.

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  :
3) COMBINAR   : si reversa(s[1:]) ya me devuelve el resto al reves,
                ¿donde va s[0] en el resultado final?
-------------------------------------------------------------------------------

Este ejercicio se ve trivial y es el que mas gente rompe: la trampa es poner
s[0] al principio por costumbre. Piensa en el CONTRATO, no en el recorrido.
"""

from check import correr


def reversa(s: str) -> str:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    (("hola",), "aloh"),
    (("",), ""),
    (("a",), "a"),
    (("recursion",), "noisrucer"),
]

if __name__ == "__main__":
    correr("reversa", reversa, CASOS)
