def contar_palabras_unicas():
    palabras_unicas = set()
    palabras_repetidas = set()
    
    print("Ingrese palabras una por una. Escriba 'salir' para terminar.")
    
    while True:
        entrada = input("Palabra: ").lower()
        
        if entrada == 'salir':
            break
        
        if entrada in palabras_unicas:
            palabras_repetidas.add(entrada)
        
        palabras_unicas.add(entrada)
        
    print("\n--- Resultados ---")
    print(f"Número de palabras únicas: {len(palabras_unicas)}")
    print(f"Palabras únicas: {palabras_unicas}")
    print(f"Palabras que se repitieron: {palabras_repetidas}")

contar_palabras_unicas()