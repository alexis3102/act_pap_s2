def gestionar_calificaciones():
    estudiantes = {}

    def agregar_estudiante(nombre):
        if nombre not in estudiantes:
            estudiantes[nombre] = []
            print(f"Estudiante '{nombre}' agregado.")
        else:
            print("El estudiante ya existe.")

    def agregar_calificacion(nombre, calificacion):
        if nombre in estudiantes:
            estudiantes[nombre].append(calificacion)
            print(f"Calificación agregada a '{nombre}'.")
        else:
            print("Error: El estudiante no existe.")

    def calcular_promedio(nombre):
        if nombre in estudiantes:
            if estudiantes[nombre]:
                return sum(estudiantes[nombre]) / len(estudiantes[nombre])
            else:
                return "No tiene calificaciones."
        else:
            return "El estudiante no existe."

    while True:
        print("\n--- Gestión de Calificaciones ---")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Calcular promedio")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ").title()
            agregar_estudiante(nombre)
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del estudiante: ").title()
            calificacion = float(input("Ingrese la calificación: "))
            agregar_calificacion(nombre, calificacion)
        
        elif opcion == '3':
            nombre = input("Ingrese el nombre del estudiante: ").title()
            promedio = calcular_promedio(nombre)
            print(f"El promedio de '{nombre}' es: {promedio}")

        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

gestionar_calificaciones()