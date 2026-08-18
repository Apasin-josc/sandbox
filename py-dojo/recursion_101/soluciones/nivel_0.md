# Soluciones — Nivel 0 (calentamiento)

> Antes de leer: ¿ya intentaste 20 minutos? Si sí, adelante. Y recuerda: **no copies**.
> Lee, cierra, reescribe de memoria.

---

## 01 — cuenta_regresiva

```python
def cuenta_regresiva(n):
    if n == 0:                          # caso base: no queda nada que contar
        return []
    return [n] + cuenta_regresiva(n - 1)  # yo + lo que ya me da el resto
```

**Contrato:** recibe `n` y devuelve la lista de `n` hasta 1.

Lo importante: en la línea del `return` **no estás recorriendo nada**. Estás diciendo
*"la lista de n es: n, seguido de la lista de n-1"*. Eso es una **definición**, no un
algoritmo. Toda la recursión se escribe así.

Prueba mental: `cuenta_regresiva(1)` → `[1] + cuenta_regresiva(0)` → `[1] + []` → `[1]`. ✅

---

## 02 — suma_hasta

```python
def suma_hasta(n):
    if n == 0:
        return 0                     # 0 es el neutro de la suma
    return n + suma_hasta(n - 1)
```

Idéntico al 01 cambiando `[n] +` por `n +` y `[]` por `0`. **Ese es el punto**: es la misma
recursión con otro neutro y otra operación. Es la Receta 1:

```
if caso_base: return NEUTRO
return COMBINA(actual, f(mas_chico))
```

---

## 03 — factorial

```python
def factorial(n):
    if n == 0:
        return 1                     # neutro de la MULTIPLICACIÓN
    return n * factorial(n - 1)
```

**Por qué 1 y no 0:** si el caso base devolviera 0, todo el producto colapsa a 0
(`5*4*3*2*1*0 = 0`). El caso base tiene que devolver el valor que **no altera** la operación:
0 para sumar, 1 para multiplicar, `True` para `and`, `False` para `or`, `""`/`[]` para concatenar.

Esta pregunta —*"¿cuál es el neutro de mi operación?"*— resuelve la mitad de los casos base
que vas a escribir en tu vida.

---

## 04 — potencia

```python
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)
```

### Bonus: potencia_rápida, O(log n)

```python
def potencia_rapida(base, exp):
    if exp == 0:
        return 1
    mitad = potencia_rapida(base, exp // 2)   # UNA sola llamada, no dos
    if exp % 2 == 0:
        return mitad * mitad                  # base^10 = (base^5)^2
    return mitad * mitad * base               # base^11 = (base^5)^2 * base
```

**Ojo con el detalle que casi todos arruinan:** guardar `mitad` en una variable. Si escribes
`return potencia_rapida(base, exp//2) * potencia_rapida(base, exp//2)` haces **dos** llamadas
y vuelves a O(n) — el mismo pecado que el fibonacci ingenuo del ejercicio 08.

**Por qué importa esto para árboles:** partir el problema *a la mitad* en vez de *restarle 1*
convierte una cadena de n llamadas en un árbol de altura log n. Es exactamente la razón por la
que un BST balanceado busca en O(log n) y una lista ligada en O(n). Mismo principio.
