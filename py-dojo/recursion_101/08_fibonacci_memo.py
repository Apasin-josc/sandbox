"""
NIVEL 1 - Ejercicio 08: fibonacci (+ memoizacion)

fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)
    fib(10) -> 55

Tu PRIMER problema con DOS llamadas recursivas -- igual que un arbol binario
(izquierda y derecha). No es casualidad: el arbol de llamadas de fib ES un arbol
binario. Este ejercicio es el puente al Nivel 2.

-------------------------------------------------------------------------------
1) CONTRATO   :
2) CASO BASE  : hay dos. ¿Cuales y por que no basta uno?
3) COMBINAR   :
-------------------------------------------------------------------------------

PARTE 1: escribe `fib` ingenuo. Corre el archivo. Vas a ver que fib(35) tarda
        una eternidad -> es O(2^n), porque recalcula fib(20) miles de veces.

PARTE 2: escribe `fib_memo` guardando resultados ya calculados en un dict.
        Pasa de O(2^n) a O(n) cambiando ~3 lineas.

        def fib_memo(n, memo=None):
            if memo is None: memo = {}
            if n in memo: return memo[n]      # <- ya lo calcule, lo reuso
            ...
            memo[n] = resultado
            return resultado

Esa idea (recursion + cache) se llama DP top-down. Es media entrevista de FAANG.
"""

from check import correr


def fib(n: int) -> int:
    raise NotImplementedError("borra esta linea y escribe tu solucion")


def fib_memo(n: int, memo=None) -> int:
    raise NotImplementedError("parte 2: la version con cache")


CASOS = [
    ((0,), 0),
    ((1,), 1),
    ((10,), 55),
    ((20,), 6765),
]

CASOS_MEMO = CASOS + [((60,), 1548008755920)]  # imposible sin memo

if __name__ == "__main__":
    correr("fib (ingenuo)", fib, CASOS)
    correr("fib_memo", fib_memo, CASOS_MEMO)
