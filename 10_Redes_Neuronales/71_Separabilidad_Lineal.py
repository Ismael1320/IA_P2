# Datos simples con dos clases
datos = [
    (1, 'A'),
    (2, 'A'),
    (8, 'B'),
    (9, 'B')
]

# Línea de separación
limite = 5


def clasificar(valor):

    # Si el valor es menor al límite pertenece a A
    if valor < limite:
        return 'A'

    # Si es mayor o igual pertenece a B
    else:
        return 'B'


print("Clasificaciones:\n")

for valor, real in datos:

    prediccion = clasificar(valor)

    print(
        "Dato:", valor,
        "| Clase real:", real,
        "| Predicción:", prediccion
    )