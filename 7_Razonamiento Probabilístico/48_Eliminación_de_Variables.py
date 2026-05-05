# Probabilidad del clima
P_clima = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidad de riego según el clima
P_riego_dado_clima = {
    'Soleado': 0.5,
    'Lluvioso': 0.1
}

# Probabilidad de suelo mojado según clima y riego
P_mojado = {
    ('Soleado', True): 0.8,
    ('Soleado', False): 0.1,
    ('Lluvioso', True): 0.9,
    ('Lluvioso', False): 0.7
}


def eliminacion_variables():

    resultado = {}

    # Queremos P(Mojado), así que eliminamos "Riego" eso significa sumar todos los casos donde riego puede ser True o False
    for clima in P_clima:

        p_c = P_clima[clima]
        p_r = P_riego_dado_clima[clima]
        p_no_r = 1 - p_r

        # Sumamos los dos casos (con y sin riego)
        p_m = (
            p_r * P_mojado[(clima, True)] +
            p_no_r * P_mojado[(clima, False)]
        )

        # Guardamos el resultado parcial por clima
        resultado[clima] = p_c * p_m

    # Ahora sumamos todo para obtener la probabilidad total
    total = sum(resultado.values())

    return total


valor = eliminacion_variables()
print("Probabilidad de suelo mojado:", round(valor, 2))