# Definir función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar información de la localidad")
    print("2. Mostrar información de la localidad")
    print("3. Salir")

# Definir función para ingresar información de la localidad
def ingresar_informacion():
    codigo_postal = input("Ingrese el código postal de la localidad: ")
    nombre_localidad = input("Ingrese el nombre de la localidad: ")
    return codigo_postal, nombre_localidad

# Definir función para mostrar información de la localidad
def mostrar_informacion(codigo_postal, nombre_localidad):
    print("Código postal:", codigo_postal)
    print("Nombre de la localidad:", nombre_localidad)

# Programa principal
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        codigo_postal, nombre_localidad = ingresar_informacion()
    elif opcion == 2:
        try:
            mostrar_informacion(codigo_postal, nombre_localidad)
        except NameError:
            print("Primero ingrese la información de la localidad.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
