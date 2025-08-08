def sistema_de_temperaturas():
    registro_temperaturas = {}
    
    while True:
        print("\n--- Sistema de Temperaturas ---")
        print("a) Agregar/Actualizar temperatura")
        print("p) Calcular promedio por ciudad")
        print("d) Calcular promedio por día")
        print("s) Salir")
        
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == 'a':
            ciudad = input("Ciudad: ").title()
            dia = input("Día (ej. Lunes): ").title()
            temp = float(input("Temperatura: "))
            
            if ciudad not in registro_temperaturas:
                registro_temperaturas[ciudad] = {}
            registro_temperaturas[ciudad][dia] = temp
            print("Temperatura registrada.")
        
        elif opcion == 'p':
            ciudad = input("Ciudad para calcular promedio: ").title()
            if ciudad in registro_temperaturas and registro_temperaturas[ciudad]:
                total_temp = 0
                contador = 0
                for temp in registro_temperaturas[ciudad].values():
                    total_temp += temp
                    contador += 1
                promedio = total_temp / contador
                print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}ºC")
            else:
                print("Error: No hay datos para esa ciudad.")
        
        elif opcion == 'd':
            dia = input("Día para calcular promedio: ").title()
            total_temp = 0
            contador = 0
            for ciudad in registro_temperaturas:
                if dia in registro_temperaturas[ciudad]:
                    total_temp += registro_temperaturas[ciudad][dia]
                    contador += 1
            if contador > 0:
                promedio = total_temp / contador
                print(f"El promedio de temperatura del día {dia} es: {promedio:.2f}ºC")
            else:
                print("Error: No hay datos para ese día.")
                
        elif opcion == 's':
            print("Saliendo del sistema.")
            break
            
        else:
            print("Opción no válida.")
            
sistema_de_temperaturas()