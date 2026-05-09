# Función para evaluar una política dada
def evaluar_politica(estados, politica, transiciones, recompensas, gamma=0.9, iteraciones=10):
    
    # Inicializa los valores de los estados en 0
    V = {s: 0 for s in estados}

    # Repite el cálculo varias veces
    for _ in range(iteraciones):
        nuevo_V = V.copy()

        # Recorre cada estado
        for s in estados:
            a = politica[s]
            total = 0

            # Calcula el valor esperado según la política
            for (s2, prob) in transiciones.get((s, a), []):
                r = recompensas.get((s, a, s2), 0)
                total += prob * (r + gamma * V[s2])

            nuevo_V[s] = total

        # Actualiza los valores
        V = nuevo_V

    return V


# Estados del sistema
estados = ['A', 'B']

# Acciones disponibles
acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

# Transiciones entre estados
transiciones = {
    ('A', 'ir_B'): [('B', 1.0)],
    ('B', 'ir_A'): [('A', 1.0)]
}

# Recompensas obtenidas
recompensas = {
    ('A', 'ir_B', 'B'): 5,
    ('B', 'ir_A', 'A'): 2
}

# Política a evaluar
politica = {
    'A': 'ir_B',
    'B': 'ir_A'
}

# Ejecuta la evaluación de la política
valores = evaluar_politica(
    estados,
    politica,
    transiciones,
    recompensas,
    iteraciones=50
)

# Muestra los valores obtenidos
print("Valores de la política:")
for estado, valor in valores.items():
    print(estado, "->", round(valor, 2))