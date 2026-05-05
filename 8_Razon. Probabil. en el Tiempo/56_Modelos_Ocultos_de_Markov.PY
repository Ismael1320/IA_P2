import random

# Estados ocultos (no los vemos directamente)
estados = ['Soleado', 'Lluvioso']

# Probabilidades iniciales
inicio = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de observación
observacion = {
    'Soleado': 0.2,
    'Lluvioso': 0.9
}


def generar_muestra():

    # Elegimos un estado oculto según la probabilidad inicial
    if random.random() < inicio['Soleado']:
        estado = 'Soleado'
    else:
        estado = 'Lluvioso'

    # Generamos lo observable basado en ese estado
    if random.random() < observacion[estado]:
        obs = "Mojado"
    else:
        obs = "Seco"

    return estado, obs


print("Generando ejemplos\n")

for _ in range(5):

    estado, obs = generar_muestra()

    # Mostramos lo oculto y lo observado
    print("Estado real:", estado, "| Observación:", obs)