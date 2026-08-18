"""Mini test-runner para los ejercicios.

Uso dentro de cada ejercicio:

    CASOS = [
        ((3,), [3, 2, 1]),     # (args_como_tupla, resultado_esperado)
        ((1,), [1]),
    ]

    if __name__ == "__main__":
        correr("cuenta_regresiva", cuenta_regresiva, CASOS)

Ojo: los args SIEMPRE son tupla. Un solo argumento se escribe (3,) con coma.
"""

from typing import Any, Callable, List, Tuple


def correr(
    nombre: str,
    fn: Callable,
    casos: List[Tuple[tuple, Any]],
    normaliza: Callable[[Any], Any] = lambda x: x,
) -> bool:
    """Corre `fn` contra los casos. `normaliza` sirve para comparar arboles como str."""
    print(f"\n== {nombre} ==")
    ok = 0
    pendientes = 0

    for i, (args, esperado) in enumerate(casos, 1):
        try:
            obtenido = normaliza(fn(*args))
        except NotImplementedError:
            pendientes += 1
            print(f"  [ ] caso {i}: todavia no lo implementas")
            continue
        except RecursionError:
            print(f"  [X] caso {i}: RecursionError -> tu caso base nunca se alcanza")
            continue
        except Exception as exc:  # noqa: BLE001 - queremos ver cualquier explosion
            print(f"  [X] caso {i}: reventó -> {type(exc).__name__}: {exc}")
            continue

        if obtenido == esperado:
            ok += 1
            print(f"  [OK] caso {i}: args={args} -> {obtenido}")
        else:
            print(f"  [X] caso {i}: args={args} esperaba {esperado}, obtuve {obtenido}")

    total = len(casos)
    print(f"  --> {ok}/{total} correctos" + (f" ({pendientes} sin implementar)" if pendientes else ""))
    return ok == total


def arbol(nodo) -> str:
    """Normalizador para ejercicios que devuelven un TreeNode."""
    return str(nodo) if nodo is not None else "None"


def ordenado(listas):
    """Normalizador para backtracking: el orden de las respuestas no importa."""
    return sorted(sorted(x) for x in listas)
