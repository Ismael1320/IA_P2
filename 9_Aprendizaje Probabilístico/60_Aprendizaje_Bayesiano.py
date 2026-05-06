# Probabilidad inicial
P_hipotesis = {
    'Falla': 0.4,
    'No_Falla': 0.6
}

# Qué tan probable es observar el dato si cada hipótesis es cierta
P_dato = {
    'Falla': 0.9,
    'No_Falla': 0.2
}


def aprender():

    posterior = {}

    # Aplicamos idea de Bayes
    for h in P_hipotesis:
        posterior[h] = P_hipotesis[h] * P_dato[h]

    # Normalizamos para que sumen 1
    total = sum(posterior.values())
    for h in posterior:
        posterior[h] /= total

    return posterior


print("Antes:", P_hipotesis)

resultado = aprender()

print("\nDespués de observar el dato:")
for h, v in resultado.items():
    print(h, "->", round(v, 2))