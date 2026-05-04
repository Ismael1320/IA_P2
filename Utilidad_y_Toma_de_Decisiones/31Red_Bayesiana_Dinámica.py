
# Lista de estados posibles (lo que NO vemos directamente)
estados = ['Soleado', 'Lluvia']

# Probabilidades de transición: Indica qué tan probable es pasar de un estado a otro
transiciones = {
    'Soleado': {'Soleado': 0.8, 'Lluvia': 0.2},
    'Lluvia': {'Soleado': 0.4, 'Lluvia': 0.6}
}

# Probabilidades de observación: Indica qué tan probable es observar algo dado un estado
observaciones_prob = {
    'Soleado': {'Seco': 0.9, 'Mojado': 0.1},
    'Lluvia': {'Seco': 0.2, 'Mojado': 0.8}
}

# Creencia inicial: Probabilidad inicial de cada estado (antes de observar nada)
creencia = {
    'Soleado': 0.5,
    'Lluvia': 0.5
}

# Función que actualiza la creencia según una nueva observación
def actualizar_creencia(creencia, observacion):
    nueva_creencia = {}

    # Recorremos cada posible estado actual
    for estado in estados:
        prob_total = 0

        # Sumamos la probabilidad de llegar a este estado desde todos los estados anteriores
        for estado_prev in estados:
            # Probabilidad de transición de estado_prev a estado actual
            prob_transicion = transiciones[estado_prev][estado]

            # Multiplicamos:(probabilidad anterior) * (probabilidad de transición)
            prob_total += creencia[estado_prev] * prob_transicion

        # Ahora incorporamos la evidencia (observación), es decir, qué tan probable es ver eso en este estado
        prob_observacion = observaciones_prob[estado][observacion]

        # Multiplicamos ambas probabilidades
        nueva_creencia[estado] = prob_total * prob_observacion

    # Normalizamos para que las probabilidades sumen 1
    total = sum(nueva_creencia.values())

    for estado in nueva_creencia:
        nueva_creencia[estado] /= total

    return nueva_creencia


print("Estados posibles:", estados)
print("Observaciones posibles: Seco / Mojado\n")

# Pedimos una secuencia de observaciones al usuario
secuencia = input("Ingresa observaciones separadas por coma (ej: Seco,Mojado): ")

# Convertimos la cadena en lista
secuencia = secuencia.split(",")

# Mostramos la creencia inicial antes de procesar datos
print("\nCreencia inicial:", creencia)

# Procesamos cada observación una por una
for obs in secuencia:
    obs = obs.strip()  # eliminamos espacios extra

# Actualizamos la creencia con la nueva observación
    creencia = actualizar_creencia(creencia, obs)

# Mostramos el resultado actual
    print(f"\nDespués de observar '{obs}':")
    print({k: round(v, 3) for k, v in creencia.items()})