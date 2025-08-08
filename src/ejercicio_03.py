def combianr_listas_con_zip(lista1, lista2):
    lista_combinada = []

    for elemento1, elemento2 in zip(lista1, lista2):
        lista_combinada.append(elemento1)
        lista_combinada.append(elemento2)
    return lista_combinada

numeros = [1,2,3]
letras = ['a', 'b', 'c']
lista_final = combianr_listas_con_zip(numeros, letras)

print(lista_final)