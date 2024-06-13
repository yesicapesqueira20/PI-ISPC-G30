# Definir función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar información del profesor")
    print("2. Mostrar información del profesor")
    print("3. Salir")

# Definir función para ingresar información del profesor
def ingresar_informacion():
    id_profesor = input("Ingrese el ID del profesor: ")
    domicilio = input("Ingrese el domicilio del profesor: ")
    dni = input("Ingrese el DNI del profesor: ")
    return id_profesor, domicilio, dni

# Definir función para mostrar información del profesor
def mostrar_informacion(id_profesor, domicilio, dni):
    print("ID del profesor:", id_profesor)
    print("Domicilio del profesor:", domicilio)
    print("DNI del profesor:", dni)

# Programa principal
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        id_profesor, domicilio, dni = ingresar_informacion()
    elif opcion == 2:
        try:
            mostrar_informacion(id_profesor, domicilio, dni)
        except NameError:
            print("Primero ingrese la información del profesor.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
