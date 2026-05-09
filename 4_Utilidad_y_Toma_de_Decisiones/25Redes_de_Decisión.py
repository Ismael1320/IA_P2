# Probabilidades del clima
prob_clima = {
    'soleado': 0.7,
    'lluvia': 0.3
}

# Tabla de utilidades
utilidad = {
    ('llevar_paraguas', 'soleado'): 5,
    ('llevar_paraguas', 'lluvia'): 8,
    ('no_paraguas', 'soleado'): 10,
    ('no_paraguas', 'lluvia'): 0
}

# Decisiones disponibles
decisiones = [
    'llevar_paraguas',
    'no_paraguas'
]


# Calcular utilidad esperada
def utilidad_esperada(decision):

    total = 0

    # Recorrer posibles climas
    for clima in prob_clima:

        # Calcular utilidad esperada
        total += (
            prob_clima[clima]
            * utilidad[(decision, clima)]
        )

    return total


# Buscar la mejor decisión
def mejor_decision():

    mejor = None
    mejor_valor = float('-inf')

    # Evaluar cada decisión
    for decision in decisiones:

        valor = utilidad_esperada(decision)

        # Mostrar utilidad esperada
        print(
            f"Decisión: {decision} "
            f"-> Utilidad esperada: {valor}"
        )

        # Guardar mejor resultado
        if valor > mejor_valor:

            mejor_valor = valor
            mejor = decision

    return mejor, mejor_valor


# Ejecutar evaluación
mejor, valor = mejor_decision()

# Mostrar resultado final
print("\nMejor decisión:", mejor)
print("Utilidad esperada:", valor)