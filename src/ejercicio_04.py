def carrito_compras():
    print("Bienvenido al Carrito de Compras")
    
    productos_menu = {
        "1": {"nombre": "pastel", "precio": 3000},
        "2": {"nombre": "arroz", "precio": 1000},
        "3": {"nombre": "leche", "precio": 4000}
    }
    
    carrito = []

    while True:
        print("\n--------MENU----------")
        print("(a) Agregar un producto")
        print("(b) Eliminar un producto")
        print("(c) Mostrar productos en el carrito")
        print("(d) Calcular el total")
        print("(e) Salir")
        print("----------------------")
        
        opcion = input("Escriba su opción: ").lower()
        
        if opcion == "a":
            print("\nProductos disponibles:")
            
            
            indice_menu = 1
            while indice_menu <= len(productos_menu):
                producto_actual = productos_menu[str(indice_menu)]
                print(f"({indice_menu}) {producto_actual['nombre']} - ${producto_actual['precio']}")
                indice_menu += 1
            
            peticion = input("Escriba el número del producto deseado: ")
            
            if peticion in productos_menu:
                carrito.append(productos_menu[peticion])
                print(f"'{productos_menu[peticion]['nombre']}' ha sido agregado.")
            else:
                print("Error: Producto no válido.")
        
        elif opcion == "b":
            if not carrito:
                print("El carrito está vacío.")
                continue

            print("\nProductos en el carrito:")
            
            
            indice = 0
            while indice < len(carrito):
                producto_actual = carrito[indice]
                print(f"({indice}) {producto_actual['nombre']} - ${producto_actual['precio']}")
                indice += 1
            
            try:
                indice_eliminar = int(input("Escriba el número del producto a eliminar: "))
                if 0 <= indice_eliminar < len(carrito):
                    producto_eliminado = carrito.pop(indice_eliminar)
                    print(f"'{producto_eliminado['nombre']}' ha sido eliminado.")
                else:
                    print("Error: Número no válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                
        elif opcion == "c":
            if not carrito:
                print("El carrito está vacío.")
            else:
                print("\nProductos en el carrito:")
                
               
                indice = 0
                while indice < len(carrito):
                    producto_actual = carrito[indice]
                    print(f"- {producto_actual['nombre']} - ${producto_actual['precio']}")
                    indice += 1
        
        elif opcion == "d":
            if not carrito:
                print("El carrito está vacío. Total: $0")
                continue
                
            suma_total = 0
            indice = 0
            while indice < len(carrito):
                suma_total += carrito[indice]['precio']
                indice += 1
            print(f"\nEl total a pagar es: ${suma_total}")

        elif opcion == "e":
            print("Saliendo del programa. ¡Gracias por su compra!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

carrito_compras()