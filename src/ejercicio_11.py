def operaciones_de_conjuntos(lista1, lista2):
    conjunto1 = set()
    conjunto2 = set()
    
    for elemento in lista1:
        conjunto1.add(elemento)
        
    for elemento in lista2:
        conjunto2.add(elemento)
        
    union = conjunto1.union(conjunto2)
    interseccion = conjunto1.intersection(conjunto2)
    diferencia = conjunto1.difference(conjunto2)
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
    
    print(f"Conjunto 1: {conjunto1}")
    print(f"Conjunto 2: {conjunto2}")
    print("---------------------------------")
    print(f"Unión: {union}")
    print(f"Intersección: {interseccion}")
    print(f"Diferencia (Conjunto1 - Conjunto2): {diferencia}")
    print(f"Diferencia Simétrica: {diferencia_simetrica}")

# Ejemplo de uso
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

operaciones_de_conjuntos(lista_a, lista_b)