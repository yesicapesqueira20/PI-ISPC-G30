agenda = {}
while True:
    print("**" * 50)  
    print("Bienvenido al registro de Gestion educatica SA. Elija una de las siguientes opciones: ")#Diccionario (sin funciones ni POO)
    print("**" * 50)    
    print("1. Registro Alumnos")
    print("2. Registro profesores")
    print("3. Registro asignaturas")
    print("4. Salir")
    print("**" * 10)

    opcion = input("Ingrese una opción: ")
     if opcion == "1":
        while True:
            print("**" * 50)  
            print("Bienvenido al registro de Alumnos. Elija una de las siguientes opciones: ")#Diccionario (sin funciones ni POO)
            print("**" * 50)    
            print("1. Agregar una persona")
            print("2. Modificar una persona")
            print("3. Eliminar una persona")
            print("4. Mostrar toda la agenda persona a persona")
            print("5. Mostrar agenda completa")
            print("6. Salir")
            print("**" * 10)

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                id_alumno = input("Ingrese el A&DNI")
                apellido = input("Ingrese el apellido: ")
                nombre = input("Ingrese el nombre: ")
                dni = input("Ingrese el DNI: ")
                email = input("Ingrese el email: ")
                telefono = input("Ingrese el número de teléfono: ")

                persona = {
                    "apellido": apellido,
                    "nombre": nombre,
                    "dni": dni,
                    "email": email,
                    "telefono": telefono
                }

                agenda[dni] = persona
                print("Persona agregada exitosamente.")

            elif opcion == "2":
                dni = input("Ingrese el DNI de la persona que desea modificar: ")

                if dni in agenda:
                    persona = agenda[dni]
                    print("Datos actuales de la persona:")
                    print(persona)

                    opcion_modificar = input("¿Desea cambiar los demás campos de la persona? (s/n): ")

                    if opcion_modificar.lower() == "s":
                        apellido = input("Ingrese el nuevo apellido: ")
                        nombre = input("Ingrese el nuevo nombre: ")
                        email = input("Ingrese el nuevo email: ")
                        telefono = input("Ingrese el nuevo número de teléfono: ")

                        persona["apellido"] = apellido
                        persona["nombre"] = nombre
                        persona["email"] = email
                        persona["telefono"] = telefono

                        print("Persona modificada exitosamente.")
                    else:
                        print("No se realizaron cambios.")
                else:
                    print("No se encontró ninguna persona con ese DNI.")

    opcion = input("Ingrese una opción: ")
     if opcion == "2":
        while True:
            print("**" * 50)  
            print("Bienvenido al registro de Profesores. Elija una de las siguientes opciones: ")#Diccionario (sin funciones ni POO)
            print("**" * 50)    
            print("1. Agregar una persona")
            print("2. Modificar una persona")
            print("3. Eliminar una persona")
            print("4. Mostrar toda la agenda persona a persona")
            print("5. Mostrar agenda completa")
            print("6. Salir")
            print("**" * 10)

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                id_profesor = input("Ingrese el A&DNI")
                apellido = input("Ingrese el apellido: ")
                nombre = input("Ingrese el nombre: ")
                dni = input("Ingrese el DNI: ")
                email = input("Ingrese el email: ")
                telefono = input("Ingrese el número de teléfono: ")

                persona = {
                    "apellido": apellido,
                    "nombre": nombre,
                    "dni": dni,
                    "email": email,
                    "telefono": telefono
                }

                agenda[dni] = persona
                print("Persona agregada exitosamente.")

            elif opcion == "2":
                dni = input("Ingrese el DNI de la persona que desea modificar: ")

                if dni in agenda:
                    persona = agenda[dni]
                    print("Datos actuales de la persona:")
                    print(persona)

                    opcion_modificar = input("¿Desea cambiar los demás campos de la persona? (s/n): ")

                    if opcion_modificar.lower() == "s":
                        apellido = input("Ingrese el nuevo apellido: ")
                        nombre = input("Ingrese el nuevo nombre: ")
                        email = input("Ingrese el nuevo email: ")
                        telefono = input("Ingrese el nuevo número de teléfono: ")

                        persona["apellido"] = apellido
                        persona["nombre"] = nombre
                        persona["email"] = email
                        persona["telefono"] = telefono

                        print("Persona modificada exitosamente.")
                    else:
                        print("No se realizaron cambios.")
                else:
                    print("No se encontró ninguna persona con ese DNI.")

     opcion = input("Ingrese una opción: ")
     if opcion == "3":
        while True:
            print("**" * 50)  
            print("Bienvenido al registro de asignaturas. Elija una de las siguientes opciones: ")#Diccionario (sin funciones ni POO)
            print("**" * 50)    
            print("1. Agregar una asignaturas")
            print("2. Modificar una asignaturas")
            print("3. Eliminar una asignaturas")
            print("4. Mostrar toda la agenda persona a persona")
            print("5. Mostrar agenda completa")
            print("6. Salir")
            print("**" * 10)

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                id_asignatura = input("Ingrese el codigo_asignatura")
                id_profesor = input("Ingrese el A&DNI")
    
                nombre = input("Ingrese el nombre_asignatura")
                codigo_asignatura = input("Ingrese el codigo_asignatura: ")
               

                persona = {
                
                    "nombre": nombre_asignatura,
                    "codigo_asignatura": codigo_asignatura,
                    "id_asignatura": codigo_asignatura",
                    "id_profesor": id_profesor,
                }

                agenda[codigo_asignatura] = persona
                print("Persona agregada exitosamente.")

            elif opcion == "2":
                dni = input("Ingrese el codigo_asignatura que desea modificar: ")

                if dni in agenda:
                    persona = agenda[dni]
                    print("Datos actuales de la persona:")
                    print(persona)

                    opcion_modificar = input("¿Desea cambiar los demás campos de la persona? (s/n): ")

                    if opcion_modificar.lower() == "s":
                        
                        nombre = input("Ingrese el nuevo nombre: ")
                       
                        persona["nombre"] = nombre

                        print("PersonaAsignatura modificada exitosamente.")
                    else:
                        print("No se realizaron cambios.")
                else:
                    print("No se encontró ninguna asignaturas con ese codigo.")

            elif opcion == "3":
                codigo_asignatura = input("Ingrese el codigo de la asignatura que desea eliminar: ")

                if codigo_asignatura in agenda:
                    del agenda[codigo_asignatura]
                    print("Persona eliminada exitosamente.")
                else:
                    print("No se encontró ninguna asignatura con ese codigo.")

            elif opcion == "4":
                if agenda:
                    print("Agenda:")
                    for id_asignatura, persona in agenda.items():
                        print(f"id_asignatura: {codigo_asignatura}")
                       
                        print(f"Nombre: {persona['nombre_asignatura']}")
                      
                        print("--------------------")
                else:
                    print("La agenda está vacía.")

            elif opcion == "5":
                print("La agenda completa:")
                print(agenda)

            elif opcion == "6":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
       
     elif opcion == "4":
                print("¡Hasta luego!")
                break