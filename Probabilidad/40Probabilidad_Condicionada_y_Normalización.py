# Probabilidades a priori
priori = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de evidencia
prob_evidencia = {
    'Soleado': 0.2,   # si está soleado, es poco probable que esté mojado
    'Lluvioso': 0.9   # si llueve, es muy probable que esté mojado
}

# Calcular probabilidad condicionada
def calcular_posterior(priori, prob_evidencia):

    posterior = {}

    # Paso 1: calcular valores sin normalizar
    for estado in priori:

        # P(estado) * P(evidencia | estado)
        posterior[estado] = priori[estado] * prob_evidencia[estado]

    # Paso 2: normalización
    total = sum(posterior.values())

    for estado in posterior:
        posterior[estado] /= total  # dividir entre el total

    return posterior


print("Probabilidades a priori:", priori)
print("Probabilidad de evidencia:", prob_evidencia)

resultado = calcular_posterior(priori, prob_evidencia)

print("\nProbabilidades condicionadas (normalizadas):\n")

for estado, prob in resultado.items():
    print(estado, "->", round(prob, 2))