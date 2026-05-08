import random


# Gramática con palabras específicas
gramatica = {

    # La oración completa
    'S': [
        ('Juan corre', 0.5),
        ('Maria come', 0.5)
    ]
}


def generar(simbolo):

    # Si el símbolo no tiene más reglas, regresamos directamente la palabra
    if simbolo not in gramatica:
        return simbolo

    reglas = gramatica[simbolo]

    # Número aleatorio para escoger una regla
    r = random.random()

    acumulado = 0

    # Revisamos las reglas y probabilidades
    for produccion, prob in reglas:

        acumulado += prob

        # Elegimos la producción correspondiente
        if r <= acumulado:

            return produccion


print("Oraciones generadas:\n")

    # Generamos varias oraciones
for _ in range(5):

    print(generar('S'))