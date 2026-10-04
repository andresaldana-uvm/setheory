# API pública

Importa la API pública soportada desde `setheory.api`:

```python
from setheory.api import Set
```

## Conjuntos

### `Set`

```python
Set(U, P)
```

Representa el conjunto 

$$
A = \set{x \in U \vert P(x)}
$$

donde $U$ es el universo y $P$ es un predicado que determina si un elemento pertenece al conjunto.

El universo debe ser compartido entre los conjuntos que participan en operaciones o relaciones de conjuntos.

## Pertenencia

```python
x in A
```

Comprueba si $x$ pertenece al conjunto $A$. El elemento pertenece al conjunto si pertenece al universo y el predicado $P$ se valúa como verdadero.

## Elementos

```python
A.elements
```

Devuelve los elementos $A$ como un `set` de Python.

## Operaciones entre conjuntos

Las operaciones entre conjuntos requieren que ambos conjuntos tengan el mismo universo.

### Intersección

```python
A & B
```

Devuelve

$$
A \cap B = \set{x \in U \vert P(x) \land Q(x)}.
$$

### Unión

```python
A | B
```

Devuelve

$$
A \cup B = \set{x \in U \vert P(x) \lor Q(x)}.
$$

### Diferencia

```python
A - B
````

Devuelve

$$
A - B = \set{x \in U \vert P(x) \land \neg{Q(x)}}.
$$

### Diferencia simétrica

```python
A ^ B
```

Devuelve

$$
A \Delta B = \set{x \in U \vert P(x) \neq Q(x)}.
$$

### Complemento

```python
~A
```

Devuelve el complemento de $A$ respecto a su universo:

$$
A^c = \set{x \in U \vert \neg{P(x)}}.
$$

## Relaciones entre conjuntos

### Subconjunto

```python
A <= B
```

Comprueba si $A$ es un subconjunto de $B$.

### Subconjunto propio

```python
A < B
```

Comprueba si $A$ es un subconjunto propio de $B$.

### Igualdad

```python
A == B
```

Comprueba si $A$ y $B$ contienen los mismos elementos.

## Representación

```python
repr(A)
str(A)
```

`reprs(A)` y `str(A)` representan el conjunto mediante sus elementos materializados como un `set` de Python.
