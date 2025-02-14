def fibonacci_ineficiente (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_ineficiente(n - 1) + fibonacci_ineficiente(n - 2)
    

def fibonacci_eficiente (n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci_eficiente(n - 1, memo) + fibonacci_eficiente(n - 2, memo)
    return memo[n]

print(fibonacci_eficiente(10))

def generar_fibonacci_hasta(k):
    fib = [0, 1]  # Iniciar con los dos primeros números
    while fib[-1] + fib[-2] <= k:
        fib.append(fib[-1] + fib[-2])
    return fib

# Ejemplo de uso
# print(generar_fibonacci_hasta(10))


def fibonacci(n, memory={}):
    if n in memory:
     return memory[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memory[n] = fibonacci(n-1, memory) + fibonacci(n-2, memory)
    return memory[n]