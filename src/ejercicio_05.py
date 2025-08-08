def buscar_palabras(lista_de_palabras):
    """
    Busca y devuelve las palabras que contienen una letra específica
    usando ciclos anidados.
    """
    
    palabras_encontradas = []

    
    letra_buscada = input("Ingrese la letra que desea buscar: ").lower()

    
    for palabra in lista_de_palabras:
        
        for letra in palabra.lower():
            if letra == letra_buscada:
                
                palabras_encontradas.append(palabra)
                
                break 

    return palabras_encontradas


mis_palabras = ["Python", "programacion", "ciclos", "lista", "clase", "variables"]

resultado = buscar_palabras(mis_palabras)

print(f"\nLas palabras que contienen la letra buscada son: {resultado}")