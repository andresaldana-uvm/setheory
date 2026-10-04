# Convención de ramas

Utiliza `main` y `develop` como ramas principales. Las demás ramas son ramas temporales de trabajo creadas a partir de `develop` según su propósito.

## Propósito de cada rama

Rama|Propósito
|-|-|
main|Código estable y listo para una versión.
develop|Rama de integración para el desarrollo en curso.
feature/*|Desarrollo de nuevas funcionalidades u operaciones.
research/*|Investigación matemática, trabajo teórico y experimentos relacionados con la teoría de conjuntos.
bugfix/*|Corrección de errores o comportamientos incorrectos.
docs/*|Cambios en la documentación.
refactor/*|Reestructuración del código sin cambiar su comportamiento.

## Flujo de trabajo con ramas

El trabajo nuevo debe partir normalmente de `develop`:

```text
develop
   │
   ├── feature/...
   ├── research/...
   ├── bugfix/...
   ├── docs/...
   └── refactor/...
```

Una vez que el trabajo esté terminado, revisado y probado, puede integrarse en `develop`.

Cuando `develop` alcance un estado estable y adecuado para una versión, puede integrarse en `main`.

```text
feature/* ──┐
research/* ─┤
bugfix/* ───┤
docs/* ─────┤
refactor/* ─┘
             ↓
          develop
             ↓
            main
```