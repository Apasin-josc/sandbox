"""
NIVEL 1 - Ejercicio 09: subir la escalera  (LeetCode 70, Climbing Stairs)

Una escalera de n escalones. Puedes subir de 1 en 1 o de 2 en 2.
¿De cuantas formas distintas puedes llegar hasta arriba?

    subir(2) -> 2   (1+1, 2)
    subir(3) -> 3   (1+1+1, 1+2, 2+1)
    subir(4) -> 5

-------------------------------------------------------------------------------
LA PREGUNTA CLAVE (asi se piensan estos problemas):

    Estoy parado en el escalon n. ¿De donde pude haber venido?
    Solo de dos lugares: del n-1 (di un paso) o del n-2 (di dos pasos).
    Entonces las formas de llegar a n = formas de llegar a n-1 + formas de llegar a n-2.

Si eso te sono a fibonacci... es fibonacci. Muchisimos problemas "de conteo" son
fibonacci disfrazado. Reconocerlo es una habilidad de entrevista real.
-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : ¿cuantas formas hay de subir 1 escalon? ¿y 0 escalones?
                (ojo con el de 0: la respuesta es 1, "no moverse" cuenta como
                 una forma valida. Si pones 0, todo te da 0.)
3) COMBINAR   :
-------------------------------------------------------------------------------

Hazlo con memo desde el principio. Sin memo, subir(45) no termina.
"""

from check import correr


def subir(n: int, memo=None) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((2,), 2),
    ((3,), 3),
    ((4,), 5),
    ((5,), 8),
    ((45,), 1836311903),  # este solo pasa si memoizaste
]

if __name__ == "__main__":
    correr("subir", subir, CASOS)
