'''
You will be given a list of 32 bit unsigned integers. Flip all the bits (0 ->1) and (1 -> 0) and return the result as an unsigned integer.

Example
n = 9(10)
9(10) = 1001(2) We're working with 32 bits, so:
00000000000000000000000000001001(2)= 9(10) 
11111111111111111111111111110110(2) = 4294967286(10)

Return 4294967286

Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns

int: the unsigned decimal integer result

'''
def flippingBits(n):
    # Máscara de 32 bits con todos los bits en 1
    mask = 0xFFFFFFFF  # Esto es igual a 4294967295 en decimal
    # Invertir los bits de n y aplicar la máscara para asegurar 32 bits
    flipped = ~n & mask
    '''
    El operador ~ (bitwise NOT) invierte todos los bits de n. Sin embargo, en Python, los enteros tienen
    una representación de bits arbitraria (no están limitados a 32 bits), por lo que ~n podría producir 
    un número negativo o un número con más de 32 bits.
    Al hacer ~n & mask, nos aseguramos de que solo se consideren los 32 bits menos significativos 
    (es decir, truncamos el resultado a 32 bits).
    '''
    return flipped

# Ejemplo de uso
n = 9
print(flippingBits(n))  # Salida: 4294967286