def sistema_de_votacion():
    candidatos_votados = set()
    
    print("Sistema de Votación")
    print("Ingrese el nombre de su candidato. Escriba 'fin' para terminar.")
    
    while True:
        voto = input("Ingrese su voto: ").title()
        
        if voto == 'Fin':
            break
        
        candidatos_votados.add(voto)
        
    print("\n--- Resultado de la Votación ---")
    if candidatos_votados:
        print("Los siguientes candidatos recibieron votos:")
        for candidato in candidatos_votados:
            print(f"- {candidato}")
    else:
        print("No se registraron votos.")

sistema_de_votacion()