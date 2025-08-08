def eliminar_duplicados(lista_con_duplicados):
    numeros_unicos = set()
    
    for numero in lista_con_duplicados:
        numeros_unicos.add(numero)
        
    cantidad_original = len(lista_con_duplicados)
    cantidad_unicos = len(numeros_unicos)
    
    duplicados = cantidad_original - cantidad_unicos
    
    print(f"Lista original: {lista_con_duplicados}")
    print(f"Conjunto con números únicos: {numeros_unicos}")
    print(f"Número de elementos duplicados encontrados: {duplicados}")
    
# Ejemplo de uso
mi_lista = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
eliminar_duplicados(mi_lista)