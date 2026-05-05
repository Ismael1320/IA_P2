import random

# Estados posibles
estados = ['A', 'B']

# Probabilidades de cambio, desde cada estado, a dónde puede ir
transiciones = {
    'A': ['A', 'B'],  # desde A puede quedarse o ir a B
    'B': ['A', 'B']   # desde B puede ir a A o quedarse
}


def monte_carlo(pasos=10):

    estado = 'A'  # empezamos en A
    conteo = {'A': 0, 'B': 0}

    for _ in range(pasos):

        # Contamos en qué estado estamos
        conteo[estado] += 1

        # Elegimos el siguiente estado al azar
        estado = random.choice(transiciones[estado])

    # Convertimos a proporciones
    total = sum(conteo.values())
    for e in conteo:
        conteo[e] = conteo[e] / total

    return conteo


resultado = monte_carlo(20)

print("Distribución aproximada:")
for estado, valor in resultado.items():
    print(estado, "->", round(valor, 2))