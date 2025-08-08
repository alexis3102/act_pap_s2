contador = []
while True:
    usuario = (input("escriba su calificacion: "))
    if (usuario == "fin"):
         break
    
    try:
        calificacion = int(usuario)
        if calificacion >= 0:
             contador.append(calificacion)
        else:
             print("Por favor, ingrese una calificación válida (un número positivo)")
    except ValueError:
         print("error: por favor, ingrese un numero o 'fin'")


def organisado(lista):
     lista.sort()
     print(lista)

organisado(contador)