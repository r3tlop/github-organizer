\# Organizador de Repositorios para GitHub



Herramienta desarrollada en \*\*Python\*\* que permite crear automáticamente una estructura básica y organizada para nuevos proyectos destinados a ser utilizados como repositorios de GitHub.



El programa genera la carpeta principal del proyecto junto con diferentes directorios y archivos esenciales, evitando tener que crearlos manualmente cada vez que se inicia un nuevo proyecto.



\## Características



Actualmente el programa permite:



\* Crear un nuevo proyecto.

\* Solicitar el nombre del proyecto.

\* Validar que el nombre no esté vacío.

\* Comprobar si el repositorio ya existe.

\* Crear automáticamente la estructura de carpetas.

\* Generar un archivo `README.md`.

\* Generar un archivo `.gitignore`.

\* Generar un archivo `LICENSE`.

\* Crear una carpeta `src` para el código principal.

\* Crear una carpeta `tests` para las pruebas.

\* Crear una carpeta `docs` para documentación.

\* Crear archivos iniciales dentro de las carpetas correspondientes.

\* Regresar al menú principal mediante la opción `Q`.



\## Estructura generada



Al crear un proyecto, el programa genera una estructura similar a la siguiente:



```text

nombre-del-proyecto/

│

├── README.md

├── .gitignore

├── LICENSE

│

├── src/

│   └── main.py

│

├── tests/

│   └── tests\_main.py

│

└── docs/

```



Esta estructura busca proporcionar una organización inicial para comenzar a desarrollar un proyecto y posteriormente convertirlo en un repositorio de GitHub.



\## Tecnologías utilizadas



\* \*\*Python 3\*\*

\* Módulo `os`

\* Módulo `pathlib`

\* Manejo de archivos y directorios

\* Funciones

\* Condicionales

\* Ciclos `while` y `for`

\* Manejo de excepciones con `try/except`

\* Diccionarios y listas



No requiere la instalación de librerías externas.



\## Instalación



\### 1. Clonar el repositorio



```bash

git clone https://github.com/TU-USUARIO/organizador-repositorios.git

```



\### 2. Entrar al proyecto



```bash

cd organizador-repositorios

```



\### 3. Ejecutar el programa



```bash

python main.py

```



En algunos sistemas puede ser necesario utilizar:



```bash

python3 main.py

```



\## Uso



Al ejecutar el programa se muestra un menú principal:



```text

=================================

&#x20;                                

&#x20;  ORGANIZADOR DE REPOSITORIOS   

&#x20;          PARA GITHUB           

&#x20;                                

=================================

Selecciona una opcion.

1\. Crear repositorio

2\. Salir del organizador

```



\### Crear un repositorio



Selecciona la opción:



```text

1\. Crear repositorio

```



Después introduce el nombre del proyecto.



Por ejemplo:



```text

Ingrese nombre del proyecto:



:>> Calculadora-Python

```



El programa creará automáticamente:



```text

Calculadora-Python/

├── README.md

├── .gitignore

├── LICENSE

├── src/

├── tests/

└── docs/

```



\### Salir



Selecciona:



```text

2\. Salir del organizador

```



Para cerrar el programa.



También puedes utilizar `Q` dentro del creador de repositorios para regresar al menú principal.



\## Funcionamiento



El programa está dividido actualmente en dos archivos principales.



\### `main.py`



Se encarga del menú principal y de recibir la opción seleccionada por el usuario.



```python

from organizador import crear\_repositorio as repo

```



La función `ingresar\_valor()` valida que la opción introducida sea un número y determina qué acción ejecutar.



\### `organizador.py`



Contiene la función:



```python

crear\_repositorio()

```



Esta función se encarga de:



1\. Solicitar el nombre del proyecto.

2\. Validar la entrada.

3\. Comprobar si el proyecto ya existe.

4\. Crear la carpeta principal.

5\. Crear las carpetas `src`, `tests` y `docs`.

6\. Crear los archivos iniciales.

7\. Escribir el contenido correspondiente en cada archivo.



\## Objetivo del proyecto



El objetivo principal es practicar y aplicar conocimientos de \*\*Python, automatización, manejo de archivos y organización de proyectos\*\*, creando una herramienta que facilite la preparación inicial de nuevos repositorios.



Este proyecto también sirve como práctica para comprender cómo funcionan las estructuras de proyectos antes de utilizar herramientas de control de versiones como Git y plataformas como GitHub.



\## Próximas mejoras



Este proyecto se encuentra en una primera versión y está pensado para seguir evolucionando.



Algunas mejoras planeadas son:



\* \[ ] Permitir seleccionar la ruta donde se creará el proyecto.

\* \[ ] Crear diferentes plantillas según el lenguaje de programación.

\* \[ ] Agregar plantillas específicas para Python.

\* \[ ] Agregar plantillas para HTML, CSS y JavaScript.

\* \[ ] Crear automáticamente `requirements.txt` para proyectos Python.

\* \[ ] Permitir elegir diferentes tipos de `.gitignore`.

\* \[ ] Inicializar automáticamente un repositorio mediante `git init`.

\* \[ ] Crear automáticamente el primer commit.

\* \[ ] Integrar GitHub para crear repositorios remotos.

\* \[ ] Realizar automáticamente el `push` del proyecto a GitHub.

\* \[ ] Mejorar la interfaz del menú.

\* \[ ] Agregar mensajes de error más descriptivos.



\## Autor: \[@r3tlop](https://github.com/r3tlop)
