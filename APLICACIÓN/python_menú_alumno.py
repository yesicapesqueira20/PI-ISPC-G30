# Definir función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar información del alumno")
    print("2. Mostrar información del alumno")
    print("3. Salir")

# Definir función para ingresar información del alumno
def ingresar_informacion():
    legajo = input("Ingrese el número de legajo del alumno: ")
    email = input("Ingrese la casilla electrónica del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    return legajo, email, edad

# Definir función para mostrar información del alumno
def mostrar_informacion(legajo, email, edad):
    print("Número de legajo:", legajo)
    print("Casilla electrónica:", email)
    print("Edad:", edad)

# Programa principal
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        legajo, email, edad = ingresar_informacion()
    elif opcion == 2:
        try:
            mostrar_informacion(legajo, email, edad)
        except NameError:
            print("Primero ingrese la información del alumno.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
