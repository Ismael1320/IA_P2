prob_cara = 0.5  # empezamos con una suposición


def EM(iteraciones=5):

    global prob_cara

    # Datos observados
    datos = [1, 0, 1, 1, 0]

    for i in range(iteraciones):

        # Paso E: calculamos cuántas caras esperamos
        esperadas = sum(datos)

        # Paso M: ajustamos la probabilidad con lo observado
        prob_cara = esperadas / len(datos)

        print(f"Iteración {i+1} -> Probabilidad de cara: {round(prob_cara, 2)}")


EM(5)