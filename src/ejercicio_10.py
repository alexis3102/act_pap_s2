def sumar_tuplas(tupla1, tupla2):
    lista_suma = []
    
    for i in range(len(tupla1)):
        suma_elemento = tupla1[i] + tupla2[i]
        lista_suma.append(suma_elemento)
        
    return tuple(lista_suma)

numeros1 = (1, 2, 3)
numeros2 = (4, 5, 6)

tupla_resultante = sumar_tuplas(numeros1, numeros2)

print(f"El resultado de la suma es: {tupla_resultante}")