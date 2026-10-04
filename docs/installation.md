# Instalación

setheory requiere Python 3.11 o posterior.

## Instalación desde GitHub

setheory no se distribuye actualmente a través de PyPI. Para instalar la versión más reciente directamente desde GitHub:

```bash
python -m pip install git+https://github.com/<usuario>/setheory.git
```

## Instalación desde una copia local

Si ya tienes una copia del repositorio, instala el paquete desde la raíz del proyecto:

```bash
python -m pip install .
```

## Instalación para el desarrollo

Desde la raíz del proyecto, creo y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Después, instala el paquete en modo editable:

```bash
python -m pip install -e .
```

La instalación editable permite que los cambios realizados en el código fuente local estén disponibles sin tener que reinstalar el paquete.

## Verificar la instalación

Después de instalar el paquete, verifica que pueda importarse correctamente:

```bash
python -c "from setheory.api import Set; print(Set)"
```