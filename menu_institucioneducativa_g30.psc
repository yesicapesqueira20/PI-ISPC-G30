Algoritmo menu_institucioneducativa_g30
	Inicio
    // Declarar la agenda como un diccionario vac�o
    agenda <- {}
	
    Mientras Verdadero Hacer
        Imprimir "**" * 50
        Imprimir "Bienvenido al registro de Gesti�n Educativa SA. Elija una de las siguientes opciones:"
        Imprimir "**" * 50
        Imprimir "1. Registro Alumnos"
        Imprimir "2. Registro Profesores"
        Imprimir "3. Registro Asignaturas"
        Imprimir "4. Salir"
        Imprimir "**" * 10
		
        opcion <- Leer("Ingrese una opci�n: ")
		
        Si opcion = "1" Entonces
            Mientras Verdadero Hacer
                Imprimir "**" * 50
                Imprimir "Bienvenido al registro de Alumnos. Elija una de las siguientes opciones:"
                Imprimir "**" * 50
                Imprimir "1. Agregar una persona"
                Imprimir "2. Modificar una persona"
                Imprimir "3. Eliminar una persona"
                Imprimir "4. Mostrar toda la agenda persona a persona"
                Imprimir "5. Mostrar agenda completa"
                Imprimir "6. Salir"
                Imprimir "**" * 10
				
                opcion <- Leer("Ingrese una opci�n: ")
				
                Si opcion = "1" Entonces
                    id_alumno <- Leer("Ingrese el A&DNI: ")
                    apellido <- Leer("Ingrese el apellido: ")
                    nombre <- Leer("Ingrese el nombre: ")
                    dni <- Leer("Ingrese el DNI: ")
                    email <- Leer("Ingrese el email: ")
                    telefono <- Leer("Ingrese el n�mero de tel�fono: ")
					
                    persona <- {
				"apellido": apellido,
				"nombre": nombre,
				"dni": dni,
				"email": email,
				"telefono": telefono
                    }
					
                    agenda[dni] <- persona
                    Imprimir "Persona agregada exitosamente."
					
                Sino Si opcion = "2" Entonces
						dni <- Leer("Ingrese el DNI de la persona que desea modificar: ")
						
						Si dni en agenda Entonces
							persona <- agenda[dni]
							Imprimir "Datos actuales de la persona:"
							Imprimir persona
							
							opcion_modificar <- Leer("�Desea cambiar los dem�s campos de la persona? (s/n): ")
							
							Si opcion_modificar = "s" Entonces
								apellido <- Leer("Ingrese el nuevo apellido: ")
								nombre <- Leer("Ingrese el nuevo nombre: ")
								email <- Leer("Ingrese el nuevo email: ")
								telefono <- Leer("Ingrese el nuevo n�mero de tel�fono: ")
								
								persona["apellido"] <- apellido
								persona["nombre"] <- nombre
								persona["email"] <- email
								persona["telefono"] <- telefono
								
								Imprimir "Persona modificada exitosamente."
							Sino
								Imprimir "No se realizaron cambios."
							FinSi
						Sino
							Imprimir "No se encontr� ninguna persona con ese DNI."
						FinSi
						
					Sino Si opcion = "3" Entonces
							dni <- Leer("Ingrese el DNI de la persona que desea eliminar: ")
							
							Si dni en agenda Entonces
								Eliminar agenda[dni]
								Imprimir "Persona eliminada exitosamente."
							Sino
								Imprimir "No se encontr� ninguna persona con ese DNI."
							FinSi
							
						Sino Si opcion = "4" Entonces
								Si agenda No est� vac�a Entonces
									Imprimir "Agenda:"
									Para cada dni, persona en agenda Hacer
										Imprimir "DNI:", dni
										Imprimir "Apellido:", persona["apellido"]
										Imprimir "Nombre:", persona["nombre"]
										Imprimir "Email:", persona["email"]
										Imprimir "Tel�fono:", persona["telefono"]
										Imprimir "--------------------"
									FinPara
								Sino
									Imprimir "La agenda est� vac�a."
								FinSi
								
							Sino Si opcion = "5" Entonces
									Imprimir "La agenda completa:"
									Imprimir agenda
									
								Sino Si opcion = "6" Entonces
										Imprimir "�Hasta luego!"
										Romper
										
									Sino
										Imprimir "Opci�n inv�lida. Por favor, ingrese una opci�n v�lida."
									FinSi
								FinMientras
								
		Sino Si opcion = "2" Entonces
			Mientras Verdadero Hacer
				Imprimir "**" * 50
				Imprimir "Bienvenido al registro de Profesores. Elija una de las siguientes opciones:"
				Imprimir "**" * 50
				Imprimir "1. Agregar una persona"
				Imprimir "2. Modificar una persona"
				Imprimir "3. Eliminar una persona"
				Imprimir "4. Mostrar toda la agenda persona a persona"
				Imprimir "5. Mostrar agenda completa"
				Imprimir "6. Salir"
				Imprimir "**" * 10												
										
					opcion <- Leer("Ingrese una opci�n: ")
										
								Si opcion = "1" Entonces
											id_profesor <- Leer("Ingrese el A&DNI: ")
											apellido <- Leer("Ingrese el apellido: ")
											nombre <- Leer("Ingrese el nombre: ")
											dni <- Leer("Ingrese el DNI: ")
											email <- Leer("Ingrese el email: ")
											telefono <- Leer("Ingrese el n�mero de tel�fono: ")
											
											persona <- {
										"apellido": apellido,
										"nombre": nombre,
										"dni": dni,
										"email": email,
										"telefono": telefono
											}
											
											agenda[dni] <- persona
											Imprimir "Persona agregada exitosamente."
											
								Sino Si opcion = "2" Entonces
												dni <- Leer("Ingrese el DNI de la persona que desea modificar: ")
												
												Si dni en agenda Entonces
													persona <- agenda[dni]
													Imprimir "Datos actuales de la persona:"
													Imprimir persona
													
													opcion_modificar <- Leer("�Desea cambiar los dem�s campos de la persona? (s/n): ")
													
													Si opcion_modificar = "s" Entonces
														apellido <- Leer("Ingrese el nuevo apellido: ")
														nombre <- Leer("Ingrese el nuevo nombre: ")
														email <- Leer("Ingrese el nuevo email: ")
														telefono <- Leer("Ingrese el nuevo n�mero de tel�fono: ")
														
														persona["apellido"] <- apellido
														persona["nombre"] <- nombre
														persona["email"] <- email
														persona["telefono"] <- telefono
														
														Imprimir "Persona modificada exitosamente."
													Sino
														Imprimir "No se realizaron cambios."
													FinSi
												Sino
													Imprimir "No se encontr� ninguna persona con ese DNI."
												FinSi
												
								Sino Si opcion = "3" Entonces
													dni <- Leer("Ingrese el DNI de la persona que desea eliminar: ")
													
													Si dni en agenda Entonces
														Eliminar agenda[dni]
														Imprimir "Persona eliminada exitosamente."
													Sino
														Imprimir "No se encontr� ninguna persona con ese DNI."
													FinSi
													
									Sino Si opcion = "4" Entonces
														Si agenda No est� vac�a Entonces
															Imprimir "Agenda:"
															Para cada dni, persona en agenda Hacer
																Imprimir "DNI:", dni
																Imprimir "Apellido:", persona["apellido"]
																Imprimir "Nombre:", persona["nombre"]
																Imprimir "Email:", persona["email"]
																Imprimir "Tel�fono:", persona["telefono"]
																Imprimir "--------------------"
															FinPara
														Sino
															Imprimir "La agenda est� vac�a."
														FinSi
														
									Sino Si opcion = "5" Entonces
															Imprimir "La agenda completa:"
															Imprimir agenda
															
									Sino Si opcion = "6" Entonces
																Imprimir "�Hasta luego!"
																Romper
																
															Sino
																Imprimir "Opci�n inv�lida. Por favor, ingrese una opci�n v�lida."
															FinSi
														FinMientras													
														
		Sino Si opcion = "3" Entonces
			Mientras Verdadero Hacer
				Imprimir "**" * 50
				Imprimir "Bienvenido al registro de Asignaturas. Elija una de las siguientes opciones:"
				Imprimir "**" * 50
				Imprimir "1. Agregar una asignatura"
				Imprimir "2. Modificar una asignatura"
				Imprimir "3. Eliminar una asignatura"
				Imprimir "4. Mostrar toda la agenda persona a persona"
				Imprimir "5. Mostrar agenda completa"
				Imprimir "6. Salir"
				Imprimir "**" * 10
																																								
					opcion <- Leer("Ingrese una opci�n: ")
																
							Si opcion = "1" Entonces
																	id_asignatura <- Leer("Ingrese el c�digo de la asignatura: ")
																	id_profesor <- Leer("Ingrese el A&DNI del profesor: ")
																	nombre <- Leer("Ingrese el nombre de la asignatura: ")
																	codigo_asignatura <- Leer("Ingrese el c�digo de la asignatura: ")
																	
																	asignatura <- {
																"nombre": nombre,
																"codigo_asignatura": codigo_asignatura,
																"id_asignatura": id_asignatura,
																"id_profesor": id_profesor
																	}
																	
																	agenda[codigo_asignatura] <- asignatura
																	Imprimir "Asignatura agregada exitosamente."
																	
								Sino Si opcion = "2" Entonces
																		codigo_asignatura <- Leer("Ingrese el c�digo de la asignatura que desea modificar: ")
																		
																		Si codigo_asignatura en agenda Entonces
																			asignatura <- agenda[codigo_asignatura]
																			Imprimir "Datos actuales de la asignatura:"
																			Imprimir asignatura
																			
																			opcion_modificar <- Leer("�Desea cambiar los dem�s campos de la asignatura? (s/n): ")
								Sino Si opcion = "3" Entonces
													id_asignatura <- Leer("Ingrese el id_asignatura de la asignatura que desea eliminar: ")
													
													Si id_asignatura en agenda Entonces
														Eliminar agenda[id_asignatura]
														Imprimir "asignatura eliminada exitosamente."
													Sino
														Imprimir "No se encontr� ninguna persona con ese DNI."
													FinSi
													
								Sino Si opcion = "4" Entonces
														Si agenda No est� vac�a Entonces
															Imprimir "Agenda:"
															Para cada dni, persona en agenda Hacer
																Imprimir "codigo_asignatura:", codigo_asignatura
											
																Imprimir "Nombre:", asignatura["nombre"]
														
																Imprimir "--------------------"
															FinPara
														Sino
															Imprimir "La agenda est� vac�a."
														FinSi
														
								Sino Si opcion = "5" Entonces
															Imprimir "La agenda completa:"
															Imprimir agenda
															
								Sino Si opcion = "6" Entonces
																Imprimir "�Hasta luego!"
																Romper
																
															Sino
																Imprimir "Opci�n inv�lida. Por favor, ingrese una opci�n v�lida."
															FinSi
														FinMientras	
   		Sino Si opcion = "4" Entonces
																Imprimir "�Hasta luego!"
																Romper
																
															Sino
																Imprimir "Opci�n inv�lida. Por favor, ingrese una opci�n v�lida."
															FinSi                  

FinAlgoritmo
