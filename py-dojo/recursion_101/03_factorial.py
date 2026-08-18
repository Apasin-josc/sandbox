"""
NIVEL 0 - Ejercicio 03: factorial

factorial(n) = n * (n-1) * ... * 1, y factorial(0) = 1 por definicion.
    factorial(5) -> 120

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : ¿por que el caso base devuelve 1 y no 0?
                (pista: 1 es el "neutro" de la multiplicacion, como 0 lo es de la suma.
                 Elegir mal el neutro es un bug clasico: todo te daria 0.)
3) COMBINAR   :
-------------------------------------------------------------------------------

BONUS (opcional, ya que te salga): implementa factorial_iterativo(n) con un for
y compara los dos. Verlos lado a lado ayuda a ver que la recursion solo esta
"escondiendo" el acumulador en la pila de llamadas.
"""

from check import correr


def factorial(n: int) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


CASOS = [
    ((5,), 120),
    ((1,), 1),
    ((0,), 1),
    ((7,), 5040),
]

if __name__ == "__main__":
    correr("factorial", factorial, CASOS)
