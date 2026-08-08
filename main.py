from organizador import crear_repositorio as repo

def ingresar_valor():
    while True:
        opcion = input(f"\n:>> ")
        try:
            op = int(opcion)
            if op == 1:
                repo(opcion)
            elif op == 2:
                print(f"Hasta luego, vuelve pronto.\nSaliendo del programa...")
                break
            else:
                print("ERROR: Opcion no valida. Elige una opcion")
        except ValueError:
            print("No acepto letras. Elige una opcion")
            


def pantalla():
    print(f"=" * 33)
    print(f" " * 33)
    print("   ORGANIZADOR DE REPOSITORIOS   ")
    print("           PARA GITHUB           ")
    print(f" " * 33)
    print(f"=" * 33)
    print("Selecciona una opcion.")
    print("1. Crear repositorio")
    print("2. Salir del organizador")
    ingresar_valor()
            

pantalla()
