# Convenciones de versionado

setheory utiliza versionado dinámico mediante `setuptools-scm`. La versión del paquete se obtiene a partir de las etiquetas (`tags`) de Git en lugar de mantenerse manualmente en `pyproject.toml`.

## Versionado semántico

Las versiones siguen, en general, el formato de versionado semántido:

```text
MAJO.MINOR.PATCH
```

Por ejmplo:

```text
0.1.0
0.2.0
0.2.1
1.0.0
```

Los componentes de la versión representan:

|Componente|Propósito|
|-|-|
|MAJOR|Cambios incompatibles con la API existente.|
|MINOR|Nuevas funcionalidades compatibles con la API existente.|
|PATCH|Correcciones de errores y cambios comptaibles que no añaden funcionalidades principales.|

Mientras el proyecto se encuentre en desarrollo inicial, las versiones `0.x` pueden utilizarse para indicar que la API puede cambiar antes de una versión estable `1.0.0`.

## Etiquetas de Git

Las versiones publicadas deben corresponder a etiquetas de Git con el prefijo `v`:

```text
v0.1.0
v0.2.0
v0.2.1
v1.0.0
```

Por ejemplo, para crear una nueva versión:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Versión durante el desarrollo

Cuando el repositorio contiene commits posteriores a la última etiqueta, `setuptools-scm` puede generar una versión de desarrollo a partir de la etiqueta más reciente y del estado del repositorio.

Por ejemplo, después de:

```text
v0.1.0
   │
   ├── commit
   ├── commit
   └── commit
```

la versión instalada puede incluir información adicional que indique que el código se encuentra por delante de `0.1.0`.

Esto permite distinguir una versión etiquetada de una versión construida directamente desde el estado de desarrollo.

## Flujo de versiones

Las versiones deben crearse a partir de código establce integrado en `main`.

El fluho general es:

```text
develop
   │
   │  estabilización
   ↓
 main
   │
   │  crear tag
   ↓
 v0.1.0
```

Después de crear una etiqueta, el desarrollo continúa normalmente en `develop` hasta preparar la siguiente versión.

## Configuración

El versionado dinámico está configurado en `pyproject.toml`:

```text
[project]
dynamic = ["version"]

[tool.setuptools_scm]
```

No se debe añadir manualmente una línea como:

```text
version = "0.1.0"
```

mientras el proyecto utilice `setuptools-scm` para gestionar la versión.