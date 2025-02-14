'''
Tres 1's => 1000 puntos

Tres 6's => 600 puntos

Tres 5's => 500 puntos

Tres 4's => 400 puntos

Tres 3's => 300 puntos

Tres 2's => 200 puntos

Un 1 => 100 puntos

Un 5 => 50 puntos
'''



def calcular_puntuacion(dados):
    frecuencia = {}
    for dado in dados:
        if dado in frecuencia:
            frecuencia[dado] += 1
        else:
            frecuencia[dado] = 1
    
    puntuacion = 0

    for numero, count in frecuencia.items():
        if count >= 3:
            if numero == 1:
                puntuacion += 1000
            else:
                puntuacion += (numero * 100)
        
        if numero == 1:
            puntuacion += 100
        elif numero == 5:
            puntuacion += 50
        
    return puntuacion