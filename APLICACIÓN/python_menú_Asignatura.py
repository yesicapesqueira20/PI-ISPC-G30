# Definir función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar información de la asignatura")
    print("2. Mostrar información de la asignatura")
    print("3. Salir")

# Definir función para ingresar información de la asignatura
def ingresar_informacion():
    id_asignatura = input("Ingrese el ID de la asignatura: ")
    nombre_asignatura = input("Ingrese el nombre completo de la asignatura: ")
    carga_horaria = input("Ingrese la carga horaria de la asignatura: ")
    id_profesor = input("Ingrese el ID del profesor de la asignatura: ")
    id_profesor_persona = input("Ingrese el ID del profesor persona de la asignatura: ")
    return id_asignatura, nombre_asignatura, carga_horaria, id_profesor, id_profesor_persona

# Definir función para mostrar información de la asignatura
def mostrar_informacion(id_asignatura, nombre_asignatura, carga_horaria, id_profesor, id_profesor_persona):
    print("ID de la asignatura:", id_asignatura)
    print("Nombre completo de la asignatura:", nombre_asignatura)
    print("Carga horaria de la asignatura:", carga_horaria)
    print("ID del profesor de la asignatura:", id_profesor)
    print("ID del profesor persona de la asignatura:", id_profesor_persona)

# Programa principal
opcion = 0
while opcion != 3:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        id_asignatura, nombre_asignatura, carga_horaria, id_profesor, id_profesor_persona = ingresar_informacion()
    elif opcion == 2:
        try:
            mostrar_informacion(id_asignatura, nombre_asignatura, carga_horaria, id_profesor, id_profesor_persona)
        except NameError:
            print("Primero ingrese la información de la asignatura.")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
