def agenda_telefonica():
    agenda = {}
    
    while True:
        print("\n--- Agenda Telefónica ---")
        print("a) Agregar contacto")
        print("b) Buscar por nombre")
        print("m) Mostrar todos los contactos")
        print("e) Eliminar contacto")
        print("s) Salir")
        
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == 'a':
            nombre = input("Ingrese el nombre del contacto: ").title()
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado.")
            
        elif opcion == 'b':
            nombre = input("Ingrese el nombre a buscar: ").title()
            if nombre in agenda:
                print(f"Teléfono de {nombre}: {agenda[nombre]}")
            else:
                print(f"El contacto '{nombre}' no se encuentra en la agenda.")
                
        elif opcion == 'm':
            print("\n--- Todos los Contactos ---")
            if agenda:
                for nombre, telefono in agenda.items():
                    print(f"- {nombre}: {telefono}")
            else:
                print("La agenda está vacía.")
                
        elif opcion == 'e':
            nombre = input("Ingrese el nombre del contacto a eliminar: ").title()
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print(f"El contacto '{nombre}' no existe en la agenda.")
                
        elif opcion == 's':
            print("Saliendo de la agenda.")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")

agenda_telefonica()