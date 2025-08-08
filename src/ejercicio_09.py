import math

def calcular_distancia_total(puntos):
    distancia_total = 0
    
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distancia_total += distancia
        
    return distancia_total

mis_puntos = ((1, 2), (4, 6), (8, 3), (1, 1))

distancia_recorrida = calcular_distancia_total(mis_puntos)

print(f"La distancia total recorrida es: {distancia_recorrida:.2f}")