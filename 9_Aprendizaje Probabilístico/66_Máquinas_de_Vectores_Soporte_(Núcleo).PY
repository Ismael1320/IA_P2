datos = [
    (1, 'A'),
    (2, 'A'),
    (8, 'B'),
    (9, 'B')
]

# Punto a clasificar
nuevo = 5


def kernel(x, y):
    # Núcleo simple
    return x * y  # producto simple


def clasificar():

    puntaje_A = 0
    puntaje_B = 0

    # Comparamos con todos los puntos conocidos
    for valor, clase in datos:

        # Aplicamos el "núcleo"
        resultado = kernel(nuevo, valor)

        if clase == 'A':
            puntaje_A += resultado
        else:
            puntaje_B += resultado

    # Elegimos el mayor puntaje
    if puntaje_A > puntaje_B:
        return 'A'
    else:
        return 'B'


print("Clasificación:", clasificar())