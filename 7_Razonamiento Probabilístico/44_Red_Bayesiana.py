# Probabilidades del clima (qué tan seguido ocurre cada uno)
P_clima = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Dependiendo del clima, el riego se usa más o menos
P_riego_dado_clima = {
    'Soleado': 0.5,
    'Lluvioso': 0.1
}

# Aquí ya mezclamos dos cosas: clima y riego y vemos qué tan probable es que el suelo termine mojado
P_mojado = {
    ('Soleado', True): 0.8,
    ('Soleado', False): 0.1,
    ('Lluvioso', True): 0.9,
    ('Lluvioso', False): 0.7
}


def probabilidad_mojado():

    total = 0

    # Vamos clima por clima
    for clima in P_clima:

        # Probabilidad de ese clima
        p_c = P_clima[clima]

        # Aquí separamos: con riego y sin riego
        p_r = P_riego_dado_clima[clima]
        p_no_r = 1 - p_r

        # Sumamos el caso donde sí hay riego
        total += p_c * p_r * P_mojado[(clima, True)]

        # Y también el caso donde no hay riego
        total += p_c * p_no_r * P_mojado[(clima, False)]

    return total


# Solo mostramos el resultado final
resultado = probabilidad_mojado()
print("Probabilidad de suelo mojado:", round(resultado, 2))