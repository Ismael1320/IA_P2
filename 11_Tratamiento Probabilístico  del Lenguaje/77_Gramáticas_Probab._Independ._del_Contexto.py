import random

# S  = oración completa
# NP = sujeto
# VP = verbo

gramatica = {

    # La oración completa siempre será: sujeto + verbo
    'S': [
        ('NP VP', 1.0)
    ],

    # El sujeto puede ser Juan o María, cada uno tiene 50% de probabilidad
    'NP': [
        ('Juan', 0.5),
        ('Maria', 0.5)
    ],

    # El verbo puede ser "corre" o "come"
    # "corre" tiene más probabilidad
    'VP': [
        ('corre', 0.6),
        ('come', 0.4)
    ]
}


def generar(simbolo):

    # Si el símbolo ya no tiene reglas, significa que ya es una palabra final
    if simbolo not in gramatica:
        return simbolo

    # Obtenemos las reglas disponibles
    reglas = gramatica[simbolo]

    # Número aleatorio para escoger una regla
    r = random.random()

    acumulado = 0

    # Recorremos las reglas y sus probabilidades
    for produccion, prob in reglas:

        acumulado += prob

        # Cuando el número entra en el rango,seleccionamos esa producción
        if r <= acumulado:

            palabras = []

            # Dividimos la producción
            for s in produccion.split():

                # Expandimos cada símbolo recursivamente
                palabras.append(generar(s))

            # Unimos las palabras para formar la oración
            return " ".join(palabras)


print("Oraciones generadas:\n")

# Generamos varias oraciones de ejemplo
for _ in range(5):

    oracion = generar('S')

    print(oracion)