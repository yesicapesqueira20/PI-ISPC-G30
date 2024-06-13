# Definir función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar información Alumno-Asignatura")
    print("2. Mostrar información Alumno-Asignatura")
    print("3. Salir")

# Definir función para ingresar información del Alumno-Asignatura
def ingresar_informacion():
    legajo = input("Ingrese el número de legajo del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")
    horario_asignatura = input("Ingrese el horario de la asignatura: ")
    nota = float(input("Ingrese la nota del alumno en la asignatura (decimal): "))
    return legajo, dni, id_asignatura, horario_asignatura, nota

# Definir función para mostrar información del Alumno-Asignatura
def mostrar_informacion(legajo, dni, id_asignatura, horario_asignatura, nota):
    print("Número de legajo del alumno:", legajo)
    print("DNI del alumno:", dni)
    print("ID de la asignatura:", id_asignatura)
    print("Horario de la asignatura:", horario_asignatura)
    print("Nota del alumno en la asignatura:", nota)

# Programa principal
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        legajo, dni, id_asignatura, horario_asignatura, nota = ingresar_informacion()
    elif opcion == 2:
        try:
            mostrar_informacion(legajo, dni, id_asignatura, horario_asignatura, nota)
        except NameError:
            print("Primero ingrese la información Alumno-Asignatura.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
