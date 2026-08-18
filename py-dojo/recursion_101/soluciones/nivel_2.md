# Soluciones — Nivel 2 (árboles: la info SUBE)

Todo este nivel es **una sola plantilla**. Míralas juntas al final del archivo.

---

## 10 — max_depth

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Contrato:** *"recibe un nodo y devuelve la profundidad del subárbol que cuelga de él"*.

El `1 +` es **yo mismo**: el camino más largo desde mí es "el camino más largo desde mi mejor
hijo, más un escalón para llegar a él".

**Por qué `if not root` y no `if es_hoja`:** con un árbol como `1 -> 2` (solo hijo izquierdo),
el caso "hoja" no cubre bien al nodo 1, que tiene un hijo nulo. Usar el nodo nulo como base hace
que ese caso se resuelva solo: `max_depth(None) = 0`. **Regla general en árboles: el caso base
es el nodo nulo, salvo que el enunciado hable explícitamente de hojas** (como el ejercicio 17).

---

## 11 — contar_nodos y suma_valores

```python
def contar_nodos(root):
    if not root:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)

def suma_valores(root):
    if not root:
        return 0
    return root.val + suma_valores(root.left) + suma_valores(root.right)
```

Diferencia: `1 +` vs `root.val +`. Nada más. Cuando veas dos problemas que se resuelven con el
mismo esqueleto, no memorices dos soluciones — memoriza el esqueleto.

### Bonus: altura_minima

```python
def altura_minima(root):
    if not root:
        return 0
    if not root.left:                                  # solo tengo hijo derecho
        return 1 + altura_minima(root.right)
    if not root.right:                                 # solo tengo hijo izquierdo
        return 1 + altura_minima(root.left)
    return 1 + min(altura_minima(root.left), altura_minima(root.right))
```

**Por qué NO basta cambiar `max` por `min`:** en el árbol `1 -> 2` (solo izquierdo), el lado
derecho devuelve 0 y `min(1, 0) = 0`, así que dirías que la altura mínima es 1. Falso: el camino
mínimo a una **hoja** es 1→2, o sea 2. Un lado nulo no es un camino a una hoja.

Ese detalle es un favorito de entrevistadores: prueba que entiendes tu propio caso base y no
copiaste el patrón a ciegas.

---

## 12 — invertir

```python
def invertir(root):
    if not root:
        return None
    root.left, root.right = invertir(root.right), invertir(root.left)
    return root
```

**Contrato:** devuelve la raíz del subárbol **ya invertido**.

La asignación simultánea de Python evalúa primero todo el lado derecho y después asigna, así que
no hay pisada. Sin ella:

```python
root.left = invertir(root.right)   # root.left ya cambió
root.right = invertir(root.left)   # ...y aquí invertimos lo que acabamos de poner  ✗
```

Versión con temporal, si prefieres que sea explícito:

```python
izq = invertir(root.left)
der = invertir(root.right)
root.left, root.right = der, izq
return root
```

**No se te olvide el `return root`.** Es el error #1 aquí: mutas el árbol correctamente pero
devuelves `None`, y el llamador se queda sin nada.

---

## 13 — same_tree

```python
def same_tree(p, q):
    if not p and not q:      # ambos vacíos: iguales
        return True
    if not p or not q:       # uno sí, el otro no: estructura distinta
        return False
    return (p.val == q.val
            and same_tree(p.left, q.left)
            and same_tree(p.right, q.right))
```

**El orden de los tres casos es obligatorio.** Si preguntaras `p.val == q.val` antes de descartar
los nulos, revientas con `AttributeError`. Patrón mental: *primero descarto lo nulo, luego ya
puedo tocar `.val` con confianza.*

Este es el que ya tenías en el repo. Nota que es la **misma forma** del palíndromo (07):
`condición_local and recursión`.

### Bonus: es_simetrico (LeetCode 101)

```python
def es_simetrico(root):
    def espejo(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (a.val == b.val
                and espejo(a.left, b.right)     # <- EN CRUZ
                and espejo(a.right, b.left))    # <- EN CRUZ
    return espejo(root, root) if root else True
```

Es `same_tree` con los hijos cruzados. Ese es el ejercicio real: **reconocer un patrón conocido
bajo un enunciado nuevo**. Eso es exactamente lo que evalúa una entrevista.

---

## La plantilla del nivel

```python
def dfs(node):
    if not node:
        return NEUTRO                       # 0, True, None, []...
    izq = dfs(node.left)
    der = dfs(node.right)
    return COMBINA(node.val, izq, der)      # 1+max, val+suma, and, ...
```

| Problema | NEUTRO | COMBINA |
|---|---|---|
| max_depth | `0` | `1 + max(izq, der)` |
| contar_nodos | `0` | `1 + izq + der` |
| suma_valores | `0` | `val + izq + der` |
| invertir | `None` | intercambia y devuelve `node` |
| same_tree | `True` | `val_igual and izq and der` |

Cuando te enfrentes a un problema nuevo de árboles, tu primera pregunta debe ser:
**"¿cuál es mi neutro y cuál es mi combinación?"**
