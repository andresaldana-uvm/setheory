# Testing

setheory utiliza `pytest` para verificar el comportamiento de la biblioteca.

La suite de tests se encuentra en:

```text
_developer-tools/tests/
```

## Ejecutar la suite

Con el entorno virtual activado y las dependencias de desarrollo instaladas, ejecuta:

```bash
python -m pytest _developer-tools/tests
```

Este comando ejecuta todos los tests de la biblioteca.

## Ejecutar archivo específico

Para ejecutar únicamente los tests de una funcionalidad concreta:

```bash
python -m pytest _developer-tools/tests/test_construction.py
```

## Ejecución antes de un commit

Antes de integrar cambios en la rama de desarrollo, la suite completa debe ejecutarse correctamente:

```bash
python -m pytest _developer-tools/tests
```

Todos los tests deben finalizar correctamente antes de realizar el commit.

Un resultado esperado tiene una forma similar a:

```text
18 passed in 0.01s
```

El número exacto de tests puede cambiar a medida que se amplía la biblioteca.