# Soluciones — Nivel 5 (backtracking)

Backtracking = **DFS sobre un árbol de decisiones que no existe en memoria.**
Tú lo vas construyendo con `append`, y lo destruyes con `pop` al salir.

---

## 21 — subsets

### Versión "incluyo / no incluyo"

```python
def subsets(nums):
    res, camino = [], []

    def backtrack(i):
        if i == len(nums):          # ya decidí sobre todos
            res.append(camino[:])   # ¡COPIA!
            return
        camino.append(nums[i])      # decisión A: lo incluyo
        backtrack(i + 1)
        camino.pop()                # DESHAGO
        backtrack(i + 1)            # decisión B: no lo incluyo

    backtrack(0)
    return res
```

### Versión "for + start" (la que se generaliza a los otros dos)

```python
def subsets(nums):
    res = []

    def backtrack(start, camino):
        res.append(camino[:])              # TODO nodo del árbol es una respuesta
        for i in range(start, len(nums)):
            camino.append(nums[i])
            backtrack(i + 1, camino)
            camino.pop()

    backtrack(0, [])
    return res
```

Aprende la segunda: es el mismo molde de los ejercicios 22 y 23, y de toda la familia de
combinaciones. Nota que aquí guardas en **cada** nodo (todo prefijo es un subconjunto válido),
mientras que en el 23 solo guardas cuando `restante == 0`.

### El `camino[:]` — el bug que TODOS cometen

Sin la copia, `res` guarda **referencias a la misma lista**. Como sigues mutándola con
`append`/`pop`, al final todas las entradas de `res` apuntan a la misma lista vacía:

```python
res.append(camino)     # ✗ guardas una referencia viva
res.append(camino[:])  # ✓ guardas una foto del estado actual
```

`list(camino)` y `camino.copy()` hacen lo mismo. **Corre el código sin la copia una vez** para
ver el desastre — se te queda grabado mucho mejor que leerlo.

---

## 22 — permutaciones

### Con un set de usados

```python
def permutaciones(nums):
    res, camino, usados = [], [], set()

    def backtrack():
        if len(camino) == len(nums):
            res.append(camino[:])
            return
        for x in nums:
            if x in usados:
                continue
            usados.add(x)          # elijo
            camino.append(x)
            backtrack()            # exploro
            camino.pop()           # DESHAGO
            usados.remove(x)       # DESHAGO (¡las dos cosas!)

    backtrack()
    return res
```

### Sin set, pasando la lista restante

```python
def permutaciones(nums):
    if len(nums) <= 1:
        return [nums[:]]
    res = []
    for i in range(len(nums)):
        resto = nums[:i] + nums[i + 1:]        # todos menos el elegido
        for p in permutaciones(resto):         # SALTO DE FE
            res.append([nums[i]] + p)
    return res
```

La segunda es más "recursión pura" (sin estado mutable) y para mí es más fácil de razonar: *"una
permutación es: elegir un primer elemento, seguido de cualquier permutación del resto."* La
primera es más eficiente. Ambas son respuestas válidas en una entrevista; di en voz alta el
trade-off y ya ganaste.

**La regla de oro del deshacer:** si modificaste **dos** estructuras antes de bajar (`usados` y
`camino`), deshaces **las dos** al subir. Cada `append` tiene su `pop`, cada `add` su `remove`.
Olvidar uno es el bug #1 de backtracking.

**Complejidad:** O(n! · n). Es inevitable — solo la salida ya tiene n! listas de n elementos.
Que un algoritmo sea exponencial no lo hace incorrecto; el punto es no explorar de más.

---

## 23 — combination_sum

```python
def combination_sum(candidatos, target):
    res = []

    def backtrack(start, restante, camino):
        if restante == 0:
            res.append(camino[:])       # éxito
            return
        if restante < 0:
            return                      # me pasé: PODA
        for i in range(start, len(candidatos)):
            camino.append(candidatos[i])
            backtrack(i, restante - candidatos[i], camino)   # i, NO i+1
            camino.pop()

    backtrack(0, target, [])
    return res
```

### Las dos decisiones de una sola letra

**`backtrack(i, ...)` en vez de `i + 1`:** puedes reusar el mismo candidato. Si el problema no lo
permitiera (LeetCode 40), sería `i + 1`.

**`range(start, ...)` en vez de `range(0, ...)`:** esto es lo que evita duplicados. Al no volver
nunca a índices anteriores, solo generas combinaciones en orden no-decreciente, así que `[2,2,3]`
se genera una vez y `[2,3,2]` o `[3,2,2]` nunca aparecen. Si empezaras en 0, tendrías
permutaciones en vez de combinaciones — que es justo el ejercicio 22.

> Toda la familia de problemas de combinaciones sale de mover esas dos perillas:
>
> | Problema | empieza en | recursa con |
> |---|---|---|
> | Permutaciones (46) | 0 (todos los no usados) | — |
> | Subsets (78) | `start` | `i + 1` |
> | Combination Sum (39) | `start` | `i` |
> | Combination Sum II (40) | `start` | `i + 1` + saltar duplicados |
>
> No son cuatro problemas. Es uno con cuatro configuraciones.

### La poda

`if restante < 0: return` corta la rama en cuanto te pasas. Si además ordenas los candidatos,
puedes cortar aún antes con un `break`:

```python
candidatos.sort()
for i in range(start, len(candidatos)):
    if candidatos[i] > restante:
        break        # los siguientes son aún más grandes: ni los intento
```

**Podar es la habilidad central del backtracking.** El esqueleto lo tiene cualquiera; lo que
distingue una buena solución es qué tan pronto detectas que una rama no lleva a nada. En N-Queens,
sudoku o word search, la poda es literalmente el problema.

---

## Ya que terminaste esto

El esqueleto que acabas de aprender es el mismo de:

- **Word Search / islas** (LeetCode 79, 200) — backtracking sobre una matriz; la matriz es el
  grafo y los "visitados" son tu `usados`.
- **N-Queens** (51) — backtracking puro con poda fuerte.
- **DFS en grafos** — la Receta 2 del README + un `set` de visitados como caso base.

O sea: ya puedes con la sección de Trees y de Backtracking de NeetCode. Sigue con graphs. 🚀
