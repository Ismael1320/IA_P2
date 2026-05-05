# Probabilidades del clima
P_clima = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de que el suelo esté mojado dependiendo del clima
P_mojado_dado_clima = {
    'Soleado': 0.1,
    'Lluvioso': 0.8
}


def inferencia():

    total = 0

    # Recorremos todos los valores posibles del clima aunque no sepamos cuál ocurrió realmente
    for clima in P_clima:

        # Probabilidad de ese clima
        p_c = P_clima[clima]

        # Probabilidad de suelo mojado en ese clima
        p_m = P_mojado_dado_clima[clima]

        # Sumamos el caso: clima + suelo mojado
        total += p_c * p_m

    return total


# Calculamos la probabilidad total de que el suelo esté mojado
resultado = inferencia()
print("Probabilidad de suelo mojado:", round(resultado, 2))