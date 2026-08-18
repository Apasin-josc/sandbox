# Soluciones — Nivel 4 (la info BAJA)

Regla que resume todo el nivel:

> **"desde la raíz hasta aquí"** → parámetro que baja
> **"desde aquí hacia abajo"** → valor que sube

---

## 17 — path_sum

```python
def path_sum(root, target):
    if not root:
        return False                                  # árbol vacío: no hay camino
    if not root.left and not root.right:              # soy hoja
        return target == root.val
    restante = target - root.val
    return path_sum(root.left, restante) or path_sum(root.right, restante)
```

**Por qué necesitas los DOS casos base:**

- `if not root` cubre a los nodos con **un solo hijo**: cuando bajas por el lado nulo, esa rama
  simplemente responde `False` en vez de reventar.
- `if es_hoja` es obligatorio porque el enunciado dice *"raíz a **hoja**"*. Sin él, `[1,2]` con
  target 1 devolvería `True` (parándose en el nodo 1), y eso está mal: 1 no es hoja.

**Por qué `or` y no `and`:** basta que **exista** un camino. `or` además corta en cuanto el lado
izquierdo dice `True` — no explora el derecho. Gratis.

### Bonus: todos_los_caminos (LeetCode 113) — ya es backtracking

```python
def todos_los_caminos(root, target):
    res, camino = [], []

    def dfs(node, restante):
        if not node:
            return
        camino.append(node.val)                       # elijo
        if not node.left and not node.right and restante == node.val:
            res.append(camino[:])                     # ¡COPIA!
        else:
            dfs(node.left,  restante - node.val)
            dfs(node.right, restante - node.val)
        camino.pop()                                  # DESHAGO

    dfs(root, target)
    return res
```

Fíjate: `append` … recursión … `pop`. Eso es *literalmente* el nivel 5. Backtracking no es un
tema nuevo, es DFS de árbol con una lista que limpias al salir.

---

## 18 — good_nodes

### Con nonlocal (flujo B + C)

```python
def good_nodes(root):
    total = 0

    def dfs(node, max_camino):
        """max_camino = el mayor valor visto desde la raíz hasta mi padre."""
        nonlocal total
        if not node:
            return
        if node.val >= max_camino:
            total += 1
        nuevo_max = max(max_camino, node.val)
        dfs(node.left,  nuevo_max)
        dfs(node.right, nuevo_max)

    dfs(root, float("-inf"))
    return total
```

### Con el conteo subiendo (flujo B + A) — sin nonlocal

```python
def good_nodes(root):
    def dfs(node, max_camino):
        if not node:
            return 0
        bueno = 1 if node.val >= max_camino else 0
        nuevo_max = max(max_camino, node.val)
        return bueno + dfs(node.left, nuevo_max) + dfs(node.right, nuevo_max)
    return dfs(root, float("-inf"))
```

**Haz las dos.** Es el mejor ejercicio de toda la carpeta para *sentir* la diferencia:
el contexto (`max_camino`) tiene que bajar en ambas, pero la respuesta puede juntarse arriba
(global) o subir por el `return`. Cuando la respuesta es una suma/conteo simple, la versión
que sube suele salir más limpia — y sin `nonlocal`.

**El `float("-inf")` inicial:** con `0`, el árbol `[-1,-2,-3]` te daría 0 nodos buenos, cuando la
respuesta es 3. Nunca inicialices un máximo en 0 si los valores pueden ser negativos. Es un bug
de una sola línea que cuesta entrevistas.

---

## 19 — valid_bst

```python
def valid_bst(root):
    def dfs(node, lo, hi):
        """CONTRATO: ¿todos los valores de este subárbol caen estrictamente
           entre lo y hi (y respetan la propiedad BST hacia abajo)?"""
        if not node:
            return True                       # el vacío siempre es válido
        if not (lo < node.val < hi):
            return False
        return (dfs(node.left,  lo, node.val) and    # el techo se aprieta
                dfs(node.right, node.val, hi))       # el piso se aprieta

    return dfs(root, float("-inf"), float("inf"))
```

### Por qué los límites y no la comparación padre-hijo

```
         5
        / \
       1   4
          / \
         3   6
```

El 3 respeta a su padre (3 < 4). Pero está en el subárbol **derecho** del 5, así que debería ser
> 5. Comparar solo con el padre pierde esa restricción. Los límites `(lo, hi)` acumulan **todas**
las restricciones de todos los ancestros en dos números. Elegantísimo.

Sigue el rango del 3 con el código: raíz 5 → `(-inf, inf)`. Al bajar a la derecha (4) → `(5, inf)`.
Ahí mismo truena: `5 < 4` es falso. ✅

**Nota:** `lo < node.val < hi` es estricto, por eso `[1,1]` es inválido. Si el problema permitiera
duplicados a la izquierda, sería `<=` de un lado. Lee siempre el enunciado.

### Alternativa: inorder

Un BST recorrido **inorder** (izq → nodo → der) da los valores **ordenados**. Entonces basta
recorrer inorder y verificar que cada valor sea mayor que el anterior:

```python
def valid_bst(root):
    anterior = float("-inf")

    def inorder(node):
        nonlocal anterior
        if not node:
            return True
        if not inorder(node.left):
            return False
        if node.val <= anterior:
            return False
        anterior = node.val
        return inorder(node.right)

    return inorder(root)
```

Menciona esta propiedad en una entrevista de BST y ganas puntos. Resuelve un montón de problemas
(k-ésimo menor, validar, convertir a lista ordenada).

---

## 20 — LCA

```python
def lca(root, p, q):
    """CONTRATO: devuelve None si ni p ni q están aquí abajo;
       devuelve p o q si encontró uno; devuelve el LCA si ya lo encontró."""
    if not root:
        return None
    if root is p or root is q:      # me encontré a uno: me reporto y no bajo más
        return root

    izq = lca(root.left, p, q)
    der = lca(root.right, p, q)

    if izq and der:                 # uno de cada lado -> YO soy el ancestro común
        return root
    return izq or der               # solo un lado tenía algo: lo paso hacia arriba
```

**Seis líneas para un problema que se siente imposible.** Todo el mérito está en el contrato: en
vez de "devuelve el LCA" (que no sabes calcular localmente), lo defines como *"devuelve lo que
encontré aquí abajo"*, y resulta que esa versión sí se combina fácil.

Esa es la técnica más transferible del nivel: **cuando un problema no se deja recursar,
generaliza el contrato.** Casi siempre es que estás pidiendo demasiado poco a la función.

**Por qué funciona `if root is p` sin seguir bajando:** si `q` estuviera debajo de `p`, entonces
`p` *es* el ancestro común más bajo. Devolverse a sí mismo es correcto.

### Bonus: LCA en un BST (LeetCode 235)

```python
def lca_bst(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)        # ambos a la izquierda
    if p.val > root.val and q.val > root.val:
        return lca_bst(root.right, p, q)       # ambos a la derecha
    return root                                # se separan aquí (o uno soy yo): es el LCA
```

Aquí **una sola** llamada recursiva: la propiedad del BST te dice hacia dónde ir sin explorar.
O(altura) en vez de O(n). Cuando el enunciado diga "BST", pregúntate siempre qué te ahorra.
