'''
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

'''

def matchingStrings(strings, queries):
    # Paso 1: Contar las frecuencias de las cadenas en `strings`
    frequency = {}
    for s in strings:
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1
    
    # Paso 2: Obtener las frecuencias para cada consulta
    result = []
    for q in queries:
        if q in frequency:
            result.append(frequency[q])
        else:
            result.append(0)
    
    return result

# Ejemplo de uso
strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
print(matchingStrings(strings, queries))  # Salida: [2, 1, 0]