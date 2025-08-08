def filtrar_pares(lista_numeros):
    numero_pares = []

    for numero in lista_numeros:
        #si el resuido de una divicion es sero es par por eso el %
        if numero% 2 == 0:
            numero_pares.append(numero)
        #devolvemos la lista con los numeros pares
    return numero_pares
    
mi_lista = [1,2,3,4,5,6,7,8,9,10]
#lo convertimos en variable para imprimir
lista_resultante = filtrar_pares(mi_lista)

print(f"la lista de numeros pares es: {lista_resultante}")
#la f es para decirle a python "que este pendiente de lo que esta entre {} y python esta atento para convertir lo que este en esas {} en texto"
