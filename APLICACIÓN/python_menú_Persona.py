# Definir función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar información de la persona")
    print("2. Mostrar información de la persona")
    print("3. Salir")

# Definir función para ingresar información de la persona
def ingresar_informacion():
    dni = input("Ingrese el DNI de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    telefono = input("Ingrese el teléfono de la persona: ")
    localidad = input("Ingrese la localidad de la persona: ")
    codigo_postal = input("Ingrese el código postal de la persona: ")
    return dni, nombre, apellido, telefono, localidad, codigo_postal

# Definir función para mostrar información de la persona
def mostrar_informacion(dni, nombre, apellido, telefono, localidad, codigo_postal):
    print("DNI de la persona:", dni)
    print("Nombre de la persona:", nombre)
    print("Apellido de la persona:", apellido)
    print("Teléfono de la persona:", telefono)
    print("Localidad de la persona:", localidad)
    print("Código postal de la persona:", codigo_postal)

# Programa principal
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        dni, nombre, apellido, telefono, localidad, codigo_postal = ingresar_informacion()
    elif opcion == 2:
        try:
            mostrar_informacion(dni, nombre, apellido, telefono, localidad, codigo_postal)
        except NameError:
            print("Primero ingrese la información de la persona.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
