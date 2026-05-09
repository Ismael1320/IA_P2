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


# Calcular utilidad esperada sin información
def utilidad_esperada():

    mejor = float('-inf')

    # Evaluar cada decisión
    for decision in decisiones:

        total = 0

        # Calcular utilidad esperada
        for clima in prob_clima:

            total += (
                prob_clima[clima]
                * utilidad[(decision, clima)]
            )

        print(f"{decision} -> EU: {total}")

        # Guardar mejor utilidad
        if total > mejor:
            mejor = total

    return mejor


# Calcular utilidad con información perfecta
def utilidad_con_informacion():

    total = 0

    # Revisar cada posible clima
    for clima in prob_clima:

        mejor = float('-inf')

        # Buscar mejor decisión para ese clima
        for decision in decisiones:

            u = utilidad[(decision, clima)]

            if u > mejor:
                mejor = u

        # Sumar utilidad ponderada
        total += prob_clima[clima] * mejor

    return total


# Calcular utilidad sin información
print("Sin información:")
eu_sin = utilidad_esperada()

# Calcular utilidad con información perfecta
print("\nCon información perfecta:")
eu_con = utilidad_con_informacion()

# Calcular valor de la información
voi = eu_con - eu_sin

# Mostrar resultados
print("\nEU sin información:", eu_sin)
print("EU con información:", eu_con)
print("Valor de la información:", round(voi, 2))