# Soluciones — Nivel 3 (estado global: dos contratos a la vez)

Este es **el nivel bisagra**. Si entiendes por qué el `return` y el `nonlocal` cargan cosas
distintas, ya eres otro programador.

---

## 14 — diámetro

```python
def diametro(root):
    res = 0

    def dfs(node):
        """CONTRATO: devuelve la ALTURA del subárbol de `node`.
           Efecto secundario: actualiza `res` con el mejor diámetro visto."""
        nonlocal res
        if not node:
            return 0
        izq = dfs(node.left)
        der = dfs(node.right)
        res = max(res, izq + der)      # ¿y si el camino más largo doblara en MÍ?
        return 1 + max(izq, der)       # lo que mi padre necesita de mí

    dfs(root)
    return res
```

### Las dos líneas que hay que entender de verdad

```python
res = max(res, izq + der)     # <- la RESPUESTA. Camino que baja por izq, sube, y baja por der.
return 1 + max(izq, der)      # <- el REPORTE al padre. Solo puede colgar de UNA rama.
```

Mi padre no puede usar un camino que baja por mis dos lados: si lo hiciera, tendría que pasar dos
veces por mí. Entonces al padre solo puedo ofrecerle **una** rama (`max`), pero para mi propia
respuesta sí puedo usar **las dos** (`izq + der`).

**La señal para reconocer este patrón en un problema nuevo:**

> Lo que quiero responder ≠ lo que mi padre necesita de mí.

Cuando eso pasa, son dos cosas: una va en el `return`, la otra en un `nonlocal`. Y el `nonlocal`
se actualiza **después** de las llamadas recursivas (necesitas los valores de los hijos primero).

**Sobre aristas vs nodos:** `izq + der` da aristas (lo que pide LeetCode 543). Si quisieras el
número de *nodos* del camino, sería `izq + der + 1`. Lee bien el enunciado; este off-by-one es
un clásico.

---

## 15 — está_balanceado

### Versión (a): devolver una tupla

```python
def esta_balanceado(root):
    def dfs(node):
        """CONTRATO: devuelve (esta_balanceado, altura) de este subárbol."""
        if not node:
            return True, 0
        bal_izq, h_izq = dfs(node.left)
        bal_der, h_der = dfs(node.right)
        balanceado = bal_izq and bal_der and abs(h_izq - h_der) <= 1
        return balanceado, 1 + max(h_izq, h_der)

    return dfs(root)[0]
```

### Versión (b): nonlocal, igualita al 14

```python
def esta_balanceado(root):
    ok = True

    def altura(node):
        nonlocal ok
        if not node:
            return 0
        izq, der = altura(node.left), altura(node.right)
        if abs(izq - der) > 1:
            ok = False
        return 1 + max(izq, der)

    altura(root)
    return ok
```

Las dos son O(n) porque **cada nodo se visita una sola vez**. La ingenua (llamar a `altura()`
dentro de `esta_balanceado()`) es O(n²): recalcula alturas que ya conocías.

**Guarda esto para la entrevista:** cuando notes que estás llamando a una función auxiliar
recursiva *dentro* de otra recursión, casi siempre puedes fusionarlas en un solo recorrido que
devuelva más información. Ese es el salto de O(n²) a O(n), y es un momento que los
entrevistadores buscan explícitamente.

*(Existe el truco de devolver `-1` como bandera de "no balanceado" mezclada con la altura.
Sábelo leer, pero rompe el "un contrato, una función" y por eso da más bugs.)*

---

## 16 — max_path_sum

```python
def max_path_sum(root):
    res = float("-inf")            # NO 0: el árbol puede ser todo negativo

    def dfs(node):
        """CONTRATO: devuelve la mejor suma de un camino que empieza en `node`
           y baja por UNA sola rama (lo que mi padre puede aprovechar)."""
        nonlocal res
        if not node:
            return 0
        izq = max(dfs(node.left), 0)    # si la rama resta, la ignoro
        der = max(dfs(node.right), 0)
        res = max(res, node.val + izq + der)   # el camino podría doblar en mí
        return node.val + max(izq, der)        # al padre solo le doy una rama

    dfs(root)
    return res
```

Compáralo lado a lado con el 14. **Es el mismo código**, cambiando `1 +` por `node.val +` y
agregando el `max(..., 0)`. Un LeetCode Hard que es un Medium que ya sabías.

### Los tres detalles que deciden si pasa o no

1. **`max(dfs(...), 0)`** — "si esta rama me perjudica, la corto y valgo 0 por ese lado".
   Es válido porque un camino puede empezar en mí: no estoy obligado a incluir a mis hijos.
2. **`res = float("-inf")`** — con `res = 0`, el árbol `[-3]` te daría 0, y la respuesta correcta
   es `-3` (un solo nodo también es un camino válido).
3. **`return 0` en el nodo nulo** — combinado con el `max(..., 0)` de arriba, hace que un hijo
   inexistente simplemente no aporte. Consistente.

---

## Cómo reconocer el Nivel 3 en la entrevista

Frases del enunciado que gritan "estado global":

- *"el camino **más largo** entre **dos nodos cualesquiera**"*
- *"la **máxima** suma de **cualquier** camino"*
- *"el subárbol **más grande** que cumpla X"*
- en general: **"el mejor de todos los nodos"**, sin que el "mejor" sea lo que le reportas
  a tu padre.
