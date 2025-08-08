def inventario_de_productos():
    inventario = {}
    
    while True:
        print("\n--- Inventario de Productos ---")
        print("a) Agregar producto")
        print("u) Actualizar cantidad")
        print("e) Eliminar producto")
        print("m) Mostrar inventario")
        print("s) Salir")
        
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == 'a':
            producto = input("Ingrese el nombre del producto: ").title()
            cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
            inventario[producto] = cantidad
            print(f"{producto} agregado al inventario.")
            
        elif opcion == 'u':
            producto = input("Ingrese el nombre del producto a actualizar: ").title()
            if producto in inventario:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {producto}: "))
                inventario[producto] = nueva_cantidad
                print(f"Cantidad de {producto} actualizada.")
            else:
                print("Error: El producto no existe en el inventario.")
                
        elif opcion == 'e':
            producto = input("Ingrese el nombre del producto a eliminar: ").title()
            if producto in inventario:
                del inventario[producto]
                print(f"{producto} eliminado del inventario.")
            else:
                print("Error: El producto no existe en el inventario.")
                
        elif opcion == 'm':
            print("\nInventario Actual:")
            if inventario:
                for producto, cantidad in inventario.items():
                    print(f"- {producto}: {cantidad}")
            else:
                print("El inventario está vacío.")
        
        elif opcion == 's':
            print("Saliendo del sistema.")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")

inventario_de_productos()