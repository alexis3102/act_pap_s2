def generar_y_operar_conjuntos():
    pares = set()
    multiplos_de_tres = set()
    
    for numero in range(2, 21):
        if numero % 2 == 0:
            pares.add(numero)
            
    for numero in range(3, 31):
        if numero % 3 == 0:
            multiplos_de_tres.add(numero)

    print("Conjunto de números pares (2-20):", pares)
    print("Conjunto de múltiplos de 3 (3-30):", multiplos_de_tres)
    print("---------------------------------------")
    
    union = pares.union(multiplos_de_tres)
    interseccion = pares.intersection(multiplos_de_tres)
    diferencia = pares.difference(multiplos_de_tres)
    diferencia_simetrica = pares.symmetric_difference(multiplos_de_tres)
    
    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia (Pares - Multiplos):", diferencia)
    print("Diferencia Simétrica:", diferencia_simetrica)

generar_y_operar_conjuntos()