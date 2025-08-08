def contar_frecuencia_palabras(frase):
    palabras = frase.lower().split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    frecuencia_ordenada = sorted(frecuencia.items(), key=lambda item: item[1], reverse=True)
    
    for palabra, cantidad in frecuencia_ordenada:
        print(f"'{palabra}': {cantidad}")

mi_frase = "Python es un lenguaje de programación. Python es genial"
contar_frecuencia_palabras(mi_frase)