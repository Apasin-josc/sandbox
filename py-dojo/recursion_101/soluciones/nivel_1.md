# Soluciones — Nivel 1 (secuencias y memoización)

---

## 05 — suma_lista

```python
def suma_lista(nums):
    if not nums:              # lista vacía
        return 0
    return nums[0] + suma_lista(nums[1:])
```

### Versión con índice (la que sí usarías en producción)

```python
def suma_lista(nums):
    def helper(i):
        if i == len(nums):    # ya me pasé del final
            return 0
        return nums[i] + helper(i + 1)
    return helper(0)
```

`nums[1:]` **copia** la lista en cada llamada → O(n²) en tiempo y memoria. Con índice es O(n).

Fíjate en el patrón: **función pública + helper recursivo interno**. Lo vas a usar constantemente,
porque el helper suele necesitar parámetros extra (índices, acumuladores, límites) que no quieres
en la firma pública. Es exactamente lo que harás en el 14, 17, 19 y todo el nivel 5.

---

## 06 — reversa

```python
def reversa(s):
    if s == "":
        return ""
    return reversa(s[1:]) + s[0]      # el primero se va AL FINAL
```

**La trampa:** escribir `s[0] + reversa(s[1:])` — eso te devuelve el string igual. Piénsalo con
el contrato: si `reversa("ola")` me da `"alo"`, entonces `reversa("hola")` debe ser `"alo"` **más
la h al final**. La `h` era la primera, así que en la reversa va hasta atrás.

---

## 07 — es_palindromo

```python
def es_palindromo(s):
    if len(s) <= 1:                  # vacío o una sola letra: siempre palíndromo
        return True
    if s[0] != s[-1]:                # los extremos no coinciden: ya perdimos
        return False
    return es_palindromo(s[1:-1])    # quito ambos extremos y sigo
```

O en una línea, con cortocircuito:

```python
def es_palindromo(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and es_palindromo(s[1:-1])
```

**Por qué `<= 1` y no `== 0`:** con `"aba"` quitas los extremos y te queda `"b"`, longitud 1.
Si tu único caso base fuera `""`, `"b"` intentaría comparar `s[0] != s[-1]` (compara `"b"` consigo
mismo, ok) y recursaría a `""`... funcionaría de casualidad. Pero pensar en los dos casos desde el
principio es el hábito correcto: **si tu recursión reduce de 2 en 2, necesitas 2 casos base.**

Ese `and` con cortocircuito es la misma forma de tu `isSameTree` en el repo. Ya lo sabías.

---

## 08 — fibonacci

### Ingenuo — O(2ⁿ)

```python
def fib(n):
    if n <= 1:              # cubre fib(0)=0 y fib(1)=1 de un jalón
        return n
    return fib(n - 1) + fib(n - 2)
```

### Con memo — O(n)

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:           # ya lo calculé antes: lo reuso
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

**Tres cosas que valen oro aquí:**

1. **`memo=None` y no `memo={}`.** Un dict como valor por defecto se comparte entre *todas* las
   llamadas a la función para siempre (bug clásico de Python). Con `None` creas uno nuevo por
   invocación externa.
2. **Dónde va el `if n in memo`:** justo después del caso base y *antes* de recursar. Si lo pones
   después, ya hiciste el trabajo que querías evitar.
3. **Alternativa de una línea:** `from functools import cache` y decoras con `@cache`. Sábelo,
   pero en la entrevista escribe el dict a mano: quieren ver que entiendes el mecanismo.

**Por qué era exponencial:** `fib(5)` llama a `fib(3)` dos veces por caminos distintos, `fib(2)`
tres veces, etc. El árbol de llamadas se duplica en cada nivel. El memo lo aplasta a n nodos
únicos. Esto se llama **DP top-down**, y sí, ya la estás haciendo.

---

## 09 — subir_escalera

```python
def subir(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return 1                    # n=0: una forma (quedarse quieto). n=1: un paso.
    if n in memo:
        return memo[n]
    memo[n] = subir(n - 1, memo) + subir(n - 2, memo)
    return memo[n]
```

Es fibonacci corrido un lugar. Lo valioso no es el código, es **cómo se llegó** a él:

> *"Estoy en el escalón n. ¿De dónde pude venir? Solo de n-1 o de n-2. Entonces las formas de
> llegar a n son la suma de las formas de llegar a esos dos."*

Esa pregunta —**"¿cuáles son las últimas decisiones posibles?"**— es la que desbloquea casi
todos los problemas de conteo y de DP. Guárdala.

**Por qué `subir(0) = 1` y no 0:** hay exactamente una forma de "subir cero escalones": no hacer
nada. Si pones 0, todo el conteo se colapsa. Es el mismo tema del neutro del ejercicio 03.
