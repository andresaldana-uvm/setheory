# Instalación

setheory requiere Python 3.11 o posterior.

## Instalación desde GitHub

setheory no se distribuye actualmente a través de PyPI. Para instalar la versión más reciente directamente desde GitHub:

```bash
python -m pip install git+https://github.com/andresaldana-uvm/setheory.git
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

A continuación, instala el paquete en modo editable junto con sus dependencias de desarrollo:

```bash
python -m pip install -e ".[dev]"
```

La instalación editable permite que los cambios realizados en el código fuente local estén disponibles sin reinstalar el paquete.

Las dependencias de desarrollo incluyen las herramientas necesarias para ejecutar la suite de tests y otras tareas de mantenimiento del proyecto.

## Verificar la instalación

Después de instalar el paquete, puedes comprobar que setheory se puede importar correctamente:

```bash
python -c "import setheory; print(setheory.__file__)"
```