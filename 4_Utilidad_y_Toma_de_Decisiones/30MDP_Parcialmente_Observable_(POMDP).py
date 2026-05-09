# Función para actualizar la creencia del agente
def actualizar_creencia(creencia, accion, observacion, transiciones, observaciones):
    
    # Diccionario donde se guardará la nueva creencia
    nueva_creencia = {}

    # Recorre cada estado posible
    for s in creencia:
        prob = 0

        # Calcula la probabilidad de llegar al estado actual
        for s_prev in creencia:
            prob += creencia[s_prev] * dict(
                transiciones[(s_prev, accion)]
            ).get(s, 0)

        # Ajusta la probabilidad según la observación recibida
        prob *= dict(
            observaciones[(accion, s)]
        ).get(observacion, 0)

        nueva_creencia[s] = prob

    # Normaliza las probabilidades
    total = sum(nueva_creencia.values())

    if total > 0:
        for s in nueva_creencia:
            nueva_creencia[s] /= total

    return nueva_creencia


# Estados posibles
estados = ['A', 'B']

# Acciones disponibles
acciones = ['ir']

# Observaciones posibles
observaciones_posibles = ['ver_A', 'ver_B']

# Probabilidades de transición
transiciones = {
    ('A', 'ir'): [('A', 0.7), ('B', 0.3)],
    ('B', 'ir'): [('A', 0.4), ('B', 0.6)]
}

# Probabilidades de observación
observaciones = {
    ('ir', 'A'): [('ver_A', 0.8), ('ver_B', 0.2)],
    ('ir', 'B'): [('ver_A', 0.3), ('ver_B', 0.7)]
}

# Creencia inicial del agente
creencia = {'A': 0.5, 'B': 0.5}

print("Creencia inicial:", creencia)

# Acción realizada
accion = 'ir'

# Observación ingresada por el usuario
observacion = input("Observación recibida (ver_A / ver_B): ")

# Actualiza la creencia
nueva = actualizar_creencia(
    creencia,
    accion,
    observacion,
    transiciones,
    observaciones
)

# Muestra la nueva creencia
print("Nueva creencia:", {
    k: round(v, 2) for k, v in nueva.items()
})