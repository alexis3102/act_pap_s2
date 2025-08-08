def fibonacci_secuencia():
    fib_list = []
    a, b = 0, 1
    contador = 0
    while contador < 20:
        fib_list.append(a)
        a, b = b, a + b
        contador += 1
    
    return tuple(fib_list)

fib_tupla = fibonacci_secuencia()

print("Números impares de la secuencia de Fibonacci:")

for numero in fib_tupla:
    if numero % 2 != 0:
        print(numero)