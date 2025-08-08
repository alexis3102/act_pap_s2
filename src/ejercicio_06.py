import random

def coordenadas_aleatorias():
    # No podemos usar una tupla directamente porque es inmutable.
    puntos_temporales = []
    for _ in range(10):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        puntos_temporales.append((x, y))

    
    coordenadas = tuple(puntos_temporales)
    
    
    puntos_en_circulo = []

    
    for x, y in coordenadas:
        
        if (x**2 + y**2) < 25:
            puntos_en_circulo.append((x, y))

    print(f"Tupla de puntos generados: {coordenadas}")
    print(f"Puntos dentro del círculo de radio 5: {puntos_en_circulo}")


coordenadas_aleatorias()