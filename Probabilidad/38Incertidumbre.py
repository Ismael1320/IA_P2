# Probabilidades iniciales
# Probabilidad de que el día sea soleado o nublado
prob_clima = {
    'Soleado': 0.6,
    'Nublado': 0.4
}


# Probabilidad de lluvia dado el clima
prob_lluvia_dado_clima = {
    'Soleado': 0.1,   # poca probabilidad de lluvia
    'Nublado': 0.7    # alta probabilidad de lluvia
}

# Cálculo de probabilidad total
def calcular_prob_lluvia():

    total = 0

    # Aplicamos la fórmula de probabilidad total
    for clima in prob_clima:
        
        # P(clima) * P(lluvia | clima)
        total += prob_clima[clima] * prob_lluvia_dado_clima[clima]

    return total


print("Probabilidades del clima:", prob_clima)
print("Probabilidad de lluvia dado el clima:", prob_lluvia_dado_clima)

resultado = calcular_prob_lluvia()

print("\nProbabilidad total de lluvia:", round(resultado, 2))