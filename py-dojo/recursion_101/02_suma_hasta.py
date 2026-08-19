"""
NIVEL 0 - Ejercicio 02: suma hasta n

Devuelve 1 + 2 + ... + n. Con n = 0 la suma es 0.
    suma_hasta(4) -> 10

Sin bucles, sin la formula n*(n+1)/2. Solo recursion.

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  :
3) COMBINAR   : si suma_hasta(n-1) ya vale 1+...+(n-1), ¿que le falta?
-------------------------------------------------------------------------------

Esta es la Receta 1 del README en su forma mas pura. Si esta te sale sola,
ya tienes el esqueleto que reusaras en los 22 ejercicios restantes.
"""

from check import correr


def suma_hasta(n: int) -> int:
    if n == 0:
        return 0
    
    sum = n
    return sum + suma_hasta(n - 1)


CASOS = [
    ((4,), 10),
    ((1,), 1),
    ((0,), 0),
    ((10,), 55),
]

if __name__ == "__main__":
    correr("suma_hasta", suma_hasta, CASOS)
