def actualizar_creencia(creencia, accion, observacion, transiciones, observaciones):
    nueva_creencia = {}

    for s in creencia:
        prob = 0
        for s_prev in creencia:
            prob += creencia[s_prev] * dict(transiciones[(s_prev, accion)]).get(s, 0)

        prob *= dict(observaciones[(accion, s)]).get(observacion, 0)
        nueva_creencia[s] = prob

    total = sum(nueva_creencia.values())
    if total > 0:
        for s in nueva_creencia:
            nueva_creencia[s] /= total

    return nueva_creencia



estados = ['A', 'B']
acciones = ['ir']
observaciones_posibles = ['ver_A', 'ver_B']

transiciones = {
    ('A', 'ir'): [('A', 0.7), ('B', 0.3)],
    ('B', 'ir'): [('A', 0.4), ('B', 0.6)]
}

observaciones = {
    ('ir', 'A'): [('ver_A', 0.8), ('ver_B', 0.2)],
    ('ir', 'B'): [('ver_A', 0.3), ('ver_B', 0.7)]
}

creencia = {'A': 0.5, 'B': 0.5}

print("Creencia inicial:", creencia)

accion = 'ir'
observacion = input("Observación recibida (ver_A / ver_B): ")

nueva = actualizar_creencia(creencia, accion, observacion, transiciones, observaciones)

print("Nueva creencia:", {k: round(v, 2) for k, v in nueva.items()})