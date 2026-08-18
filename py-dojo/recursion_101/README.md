# Recursion 101

Guía para dejar de "adivinar" recursión y empezar a **derivarla**.

---

## 0. Primero: el diagnóstico

Si te sientes perdido, casi seguro es por **esto**:

> Estás intentando seguir la recursión con la cabeza — llamada por llamada, stack frame por
> stack frame — y tu memoria de trabajo se satura a la tercera llamada.

Eso no se arregla con más neuronas. **Nadie** simula recursión mentalmente. Los que se ven
"cracks" no la simulan: **confían en ella**. Este documento es cómo se hace esa transición.

Y una cosa más, porque sé que te estresa: tú ya escribiste `isSubtree` y `diameterOfBinaryTree`
bien. No es que no sepas. Es que no tienes todavía un **procedimiento repetible** para llegar
ahí sin depender de la inspiración. Eso es exactamente lo que vamos a construir.

---

## 1. La regla de oro: el salto de fe

Cuando escribes una función recursiva, **asume que la función ya funciona** para entradas más
chicas. No la sigas. No la traces. Solo úsala.

```python
def max_depth(root):
    if not root:
        return 0
    # SALTO DE FE: asumo que max_depth() YA me da bien la profundidad
    # del subárbol izquierdo y del derecho. No me pregunto CÓMO.
    izq = max_depth(root.left)
    der = max_depth(root.right)
    return 1 + max(izq, der)
```

La pregunta correcta **nunca** es *"¿y luego qué llamada se ejecuta?"*.
La pregunta correcta es:

> **"Si un genio me regalara la respuesta para los subproblemas, ¿qué haría yo con ella?"**

Todo lo demás son detalles que la computadora se encarga de ejecutar.

### ¿Por qué funciona el salto de fe? (para que no se sienta a magia)

Es inducción matemática disfrazada:

1. Demuestras el caso más chico a mano (**caso base**).
2. Demuestras que *si* funciona para `n-1`, entonces funciona para `n` (**paso recursivo**).
3. Por lo tanto funciona para todo `n`.

Si esas dos piezas están bien, la función **está correcta**, aunque nunca la hayas trazado.
Trazar es para depurar, no para diseñar.

---

## 2. La plantilla de las 3 preguntas

Antes de escribir **una sola línea**, responde estas tres, por escrito, en un comentario.
En serio: escríbelas. Vas a hacerlo con los 23 ejercicios de esta carpeta.

### Pregunta 1 — ¿Cuál es el CONTRATO?

Una frase: *"esta función recibe X y devuelve Y"*. Sin ambigüedad.

- ❌ "recorre el árbol"
- ✅ "recibe un nodo y devuelve **la altura del subárbol que cuelga de ese nodo**"

**El 80% de la recursión rota es un contrato mal definido.** Si tu función a veces devuelve
la altura y a veces el diámetro, nunca va a servir. Un contrato, una función.

### Pregunta 2 — ¿Cuál es el CASO BASE?

La entrada más pequeña posible donde la respuesta es **obvia sin recursión**.

| Estructura | Caso base típico |
|---|---|
| número `n` | `n == 0` o `n == 1` |
| lista / string | vacío `[]` / `""` |
| árbol | `not root` (nodo nulo) |
| grafo | ya visitado |

Truco para árboles: usa `if not root` (nodo nulo), **no** `if not root.left and not root.right`
(hoja). El nodo nulo es más simple y te evita bugs con nodos de un solo hijo.

### Pregunta 3 — ¿Cómo COMBINO los subproblemas?

Aplicas el salto de fe: ya tienes `f(izq)` y `f(der)` (o `f(n-1)`). ¿Qué operación los junta
en la respuesta de este nivel? Sumar, `max`, `and`/`or`, concatenar, `1 + ...`.

### Pregunta 4 (bonus, la que evita el `RecursionError`)

¿Cada llamada recursiva se acerca **estrictamente** al caso base? Si llamas `f(n)` dentro de
`f(n)`, o pasas `root` en vez de `root.left`, hiciste un ciclo infinito.

---

## 3. Los 3 flujos de información (esto es LO que desbloquea trees)

Aquí está el 90% de por qué los árboles se sienten confusos. En un árbol la información puede
viajar en **tres direcciones distintas**, y cada una se implementa diferente. Casi todos los
problemas de trees son "¿cuál de las tres necesito?".

### Flujo A — La info SUBE (return value)

De las hojas hacia la raíz. Cada nodo pregunta a sus hijos, combina, y devuelve.

```python
def dfs(node):
    if not node:
        return 0
    return 1 + max(dfs(node.left), dfs(node.right))   # subiendo
```

**Cuándo:** altura, contar nodos, sumar, "¿son iguales?", invertir.

### Flujo B — La info BAJA (parámetros)

De la raíz hacia las hojas. El padre le *pasa contexto* al hijo.

```python
def dfs(node, acumulado):          # <- el contexto baja como parámetro
    if not node:
        return
    dfs(node.left,  acumulado + node.val)
    dfs(node.right, acumulado + node.val)
```

**Cuándo:** "suma del camino desde la raíz", validar BST (rango min/max), profundidad actual,
"¿este nodo es el máximo del camino?".

### Flujo C — Estado GLOBAL (`nonlocal` / atributo / lista mutable)

Una respuesta que vive fuera de la recursión y se va actualizando.

```python
def diameter(root):
    res = 0
    def dfs(node):
        nonlocal res                  # <- estado global
        if not node: return 0
        izq, der = dfs(node.left), dfs(node.right)
        res = max(res, izq + der)     # respuesta que NO es lo que retorno
        return 1 + max(izq, der)      # contrato del return: ALTURA
    dfs(root)
    return res
```

**Cuándo:** "el mejor de todos los nodos" — diámetro, max path sum, el nodo más profundo.

> 🔑 **La señal para usar el Flujo C:** cuando lo que quieres responder (`diámetro`) **no es**
> lo que necesitas devolverle a tu padre (`altura`). Son dos cosas distintas → una va en el
> `return`, la otra en el `nonlocal`.
>
> Tú ya escribiste esto en `diameter_binary_tree.py`. Si te sintió "truco", es porque nadie te
> dijo que es un patrón con nombre. Ya lo sabes usar.

**Muchos problemas combinan B y C.** (Ej.: `good_nodes` — el máximo del camino *baja*, el
contador *es global*.)

---

## 4. Cómo trazar cuando SÍ te trabas (sin volverte loco)

Diseñar = salto de fe. Depurar = trazar. Pero traza **bien**:

**a) Usa el árbol más chico que rompa.** No tracees `[3,9,20,null,null,15,7]`. Tracea `[1,2]`.
Si funciona con 1 y 2 nodos, casi siempre funciona con 500.

**b) Imprime con indentación** — es la forma más rápida de *ver* la pila:

```python
def dfs(node, depth=0):
    sangria = "  " * depth
    print(f"{sangria}-> entro a {node.val if node else None}")
    if not node:
        print(f"{sangria}<- devuelvo 0")
        return 0
    r = 1 + max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
    print(f"{sangria}<- devuelvo {r} desde {node.val}")
    return r
```

Corre esto una vez con un árbol de 3 nodos y **de verdad míralo**. Vale más que 10 videos.

**c) Dibuja el árbol de llamadas en papel, no en la cabeza.** Un nodo por llamada, una flecha
por valor devuelto. La recursión es un árbol; tu memoria de trabajo es una pila de 3 slots.

---

## 5. Recetas (los esqueletos que vas a reusar toda la vida)

### Receta 1 — Recursión lineal (números / listas)
```python
def f(n):
    if n == 0:                 # caso base
        return VALOR_BASE
    return COMBINA(n, f(n - 1))   # salto de fe
```

### Receta 2 — DFS de árbol que devuelve un valor
```python
def dfs(node):
    if not node:
        return NEUTRO          # 0 para sumas, True para "and", etc.
    izq = dfs(node.left)
    der = dfs(node.right)
    return COMBINA(node.val, izq, der)
```

### Receta 3 — DFS con estado global
```python
def solve(root):
    res = INICIAL
    def dfs(node):
        nonlocal res
        if not node: return NEUTRO
        izq, der = dfs(node.left), dfs(node.right)
        res = max(res, ALGO(izq, der, node.val))   # actualizo la respuesta
        return LO_QUE_MI_PADRE_NECESITA            # otro contrato distinto
    dfs(root)
    return res
```

### Receta 4 — DFS con contexto que baja
```python
def dfs(node, contexto):
    if not node:
        return CASO_BASE
    return dfs(node.left,  actualiza(contexto, node)) or \
           dfs(node.right, actualiza(contexto, node))
```

### Receta 5 — Backtracking (elige / explora / deshaz)
```python
def backtrack(i, camino):
    if CONDICION_DE_PARO:
        res.append(camino[:])      # ¡COPIA! camino[:] no camino
        return
    for opcion in opciones(i):
        camino.append(opcion)      # elijo
        backtrack(i + 1, camino)   # exploro
        camino.pop()               # DESHAGO  <- esto es el backtracking
```

Backtracking es *"recursión + deshacer"*. Es la base de N-Queens, sudoku, word search,
generar combinaciones... y aparece muchísimo en entrevistas.

---

## 6. Errores clásicos (checa esta lista cuando algo falle)

| Síntoma | Causa casi siempre |
|---|---|
| `RecursionError` | No hay caso base, o no te acercas a él (pasaste `root` en vez de `root.left`) |
| Devuelve `None` | Se te olvidó el `return` en la llamada recursiva (`f(n-1)` en vez de `return f(n-1)`) |
| Resultado siempre 0 / vacío | Estás mutando una variable local pensando que es global → te falta `nonlocal` |
| Todas las respuestas iguales en backtracking | Guardaste `camino` en vez de `camino[:]` (misma lista compartida) |
| `AttributeError: 'NoneType' has no attribute 'val'` | Tocas `node.val` antes de checar `if not node` |
| Funciona con árbol lleno, falla con uno chueco | Usaste "hoja" como caso base en vez de "nodo nulo" |

---

## 7. El roadmap de esta carpeta

23 ejercicios, de trivial a nivel entrevista. **Hazlos en orden.** Los primeros se ven tontos
a propósito: son para automatizar la plantilla de 3 preguntas sin que la estructura te distraiga.

| Nivel | Qué entrena | Ejercicios |
|---|---|---|
| **0 — Calentamiento** | La plantilla pura, sin estructuras | `01`–`04` |
| **1 — Secuencias** | Recursión sobre listas y strings + memoización | `05`–`09` |
| **2 — Árboles: la info SUBE** | Flujo A. El pan de cada día | `10`–`13` |
| **3 — Árboles: estado global** | Flujo C. Aquí vive el 70% de los "medium" | `14`–`16` |
| **4 — Árboles: la info BAJA** | Flujo B (+C). Aquí vive el otro 30% | `17`–`20` |
| **5 — Backtracking** | Recursión + deshacer. Puerta a graphs | `21`–`23` |

```
00_..04  →  Nivel 0    01 cuenta_regresiva   02 suma_hasta   03 factorial   04 potencia
            Nivel 1    05 suma_lista   06 reversa_string   07 es_palindromo
                       08 fibonacci_memo   09 subir_escalera
            Nivel 2    10 max_depth   11 contar_nodos   12 invertir_arbol   13 same_tree
            Nivel 3    14 diametro   15 esta_balanceado   16 max_path_sum
            Nivel 4    17 path_sum   18 good_nodes   19 valid_bst   20 lca
            Nivel 5    21 subsets   22 permutaciones   23 combination_sum
```

---

## 8. Cómo usar la carpeta

Cada archivo trae el enunciado, las 3 preguntas **en blanco para que las llenes**, un stub, y
casos de prueba listos.

```powershell
cd py-dojo\recursion_101
python 01_cuenta_regresiva.py
```

Vas a ver algo así:

```
== cuenta_regresiva ==
  [ ] caso 1: todavia no lo implementas
  --> 0/3 correctos (3 sin implementar)
```

Implementas, vuelves a correr, y persigues el `3/3`.

**Las soluciones están en [`soluciones/`](soluciones/), una por nivel, con explicación línea
por línea.** Regla honesta contigo mismo:

> Intenta **20 minutos reales** antes de abrir la solución. Si la abres, no la copies:
> ciérrala y reescribe el archivo desde cero. Al día siguiente, rehaz ese ejercicio en blanco.
> Un problema que copiaste no lo sabes; uno que reescribiste de memoria sí.

---

## 9. Plan de 4 semanas (realista, ~45 min/día)

| Semana | Qué haces | Meta |
|---|---|---|
| **1** | Niveles 0 y 1 (`01`–`09`) + relee §2 y §3 cada día | Escribir las 3 preguntas sin pensarlo |
| **2** | Nivel 2 y 3 (`10`–`16`) | Reconocer "¿es Flujo A o C?" en <1 min |
| **3** | Nivel 4 y 5 (`17`–`23`) | Backtracking con la receta de memoria |
| **4** | Rehaz `14`, `16`, `19`, `20`, `23` en blanco + los de `neetcode/trees` | Explicarlos en voz alta mientras codeas |

Esa última parte —**hablar en voz alta mientras resuelves**— es literalmente lo que te van a
pedir en la entrevista de FAANG. Practícalo desde ahora, se siente ridículo y funciona.

---

## 10. Qué sigue (por qué esto sí te lleva a graphs / heaps / Dijkstra)

No es casualidad que quieras esto antes de graphs. Los árboles son grafos sin ciclos:

- **DFS en grafos** = exactamente la Receta 2, más un `set` de visitados (que es el caso base:
  "si ya lo visité, regreso"). Si dominas trees, DFS de grafos es *un `if` más*.
- **Backtracking** (nivel 5) = DFS en un grafo implícito de estados. Word search, islas,
  N-Queens: mismo esqueleto.
- **Memoización** (ej. `08`) = la puerta a programación dinámica. Top-down DP *es* recursión
  con caché, nada más.
- **Dijkstra / BFS** son iterativos con cola o heap, **no** recursivos — pero el modelo mental
  de "explorar vecinos y combinar" es el mismo que estás construyendo aquí.
- **Heaps** son árboles binarios completos guardados en un array; `sift_up`/`sift_down` se
  escriben recursivos de forma natural.

O sea: esta carpeta no es un desvío, es el prerrequisito real. Vas bien. 🌳
