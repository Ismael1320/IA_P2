import random

# Estados posibles
estados = ['A', 'B', 'C']

# Probabilidades de transición, solo dependen del estado actual
transiciones = {
    'A': {'A': 0.2, 'B': 0.5, 'C': 0.3},
    'B': {'A': 0.3, 'B': 0.4, 'C': 0.3},
    'C': {'A': 0.4, 'B': 0.2, 'C': 0.4}
}


def siguiente_estado(estado_actual):

    # Generamos un número para decidir el siguiente estado
    r = random.random()
    acumulado = 0

    for estado, prob in transiciones[estado_actual].items():
        acumulado += prob

        # Elegimos cuando se cumple el rango
        if r < acumulado:
            return estado


def simular(pasos=10):

    estado = 'A'  # punto de inicio

    for i in range(pasos):

        print("Paso", i + 1, "-> Estado:", estado)

        # Solo usamos el estado actual para avanzar
        estado = siguiente_estado(estado)


if __name__ == "__main__":

    simular(10)