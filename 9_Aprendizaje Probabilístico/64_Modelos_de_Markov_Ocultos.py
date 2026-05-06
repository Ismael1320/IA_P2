estados = ['Soleado', 'Lluvioso']

# Observaciones (lo que sí vemos)
observaciones = ['Seco', 'Mojado']

# Probabilidades iniciales
inicio = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de observación según el estado
P_obs = {
    'Soleado': {'Seco': 0.8, 'Mojado': 0.2},
    'Lluvioso': {'Seco': 0.1, 'Mojado': 0.9}
}

# Observación que recibimos
dato = 'Mojado'


def inferir_estado():

    resultados = {}

    # Calculamos qué tan probable es cada estado
    for estado in estados:

        # combinamos lo que creíamos con lo que observamos
        resultados[estado] = inicio[estado] * P_obs[estado][dato]

    # Normalizamos
    total = sum(resultados.values())
    for e in resultados:
        resultados[e] /= total

    # Elegimos el estado más probable
    mejor = max(resultados, key=resultados.get)

    return mejor, resultados


estado, valores = inferir_estado()

print("Observación:", dato)

print("\nProbabilidades:")
for e, v in valores.items():
    print(e, "->", round(v, 2))

print("\nEstado más probable:", estado)