import os
from pathlib import Path

def crear_repositorio(nombre):
    """
    Creador de repositorios Github (Estructura basica)
    """    
    while True:
        print("'Q' para regresar al menu principal")
        print(f"Ingrese nombre del proyecto: ")
        nombre = input(f"\n\n :>>  ")
        if nombre.upper() == "Q":
            print("Volviendo al menu principal...")
            break
        if not nombre:
            print("El nombre no pude estar vacio")
            continue
        ruta = nombre
        if os.path.exists(ruta):
            print("El repositorio ya existe")
            continue
        os.mkdir(ruta)
        carpetas = ["src","tests","docs"]
        for carpeta in carpetas:
            os.mkdir(os.path.join(ruta, carpeta))
        archivos = {
            "README.md": f"# {nombre}\n\nDescripcion del proyecto.",
            ".gitignore": "__pycache__/\n.env\nvenv/",
            "LICENSE": "MIT License",
            "src/main.py": "# Codigo principal\n",
            "tests/tests_main.py": "# Pruebas del proyecto\n"
            }
        for archivo, contenido in archivos.items():
            ruta_archivo = os.path.join(ruta, archivo) 
            with open(ruta_archivo, "w", encoding = "utf-8") as f:
                f.write(contenido)
        print("\n!!! Repositorio creado correctamente !!!")
        break
