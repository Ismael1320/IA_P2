import random

# Estados del sistema
estados = ['A', 'B']

# Acciones posibles
acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

# Transiciones (a dónde se mueve)
transiciones = {
    ('A', 'ir_B'): 'B',
    ('B', 'ir_A'): 'A'
}

# Recompensas por llegar a un estado
recompensas = {
    'A': 2,
    'B': 5
}

# Tabla Q (estado, acción): Inicialmente todo en 0 (no sabe nada)
Q = {}
for s in estados:
    for a in acciones[s]:
        Q[(s, a)] = 0

# Parámetros
alpha = 0.1   # qué tanto aprende cada vez
gamma = 0.9   # importancia del futuro
epsilon = 0.2 # probabilidad de explorar

# Función para elegir acción
def elegir_accion(estado):
    # A veces explora (elige aleatorio)
    if random.random() < epsilon:
        return random.choice(acciones[estado])
    
    # Si no, usa lo que ha aprendido (mejor acción)
    return max(acciones[estado], key=lambda a: Q[(estado, a)])


# Entrenamiento
estado = 'A'  # estado inicial

for i in range(20):  # repetir varias veces

    # Elegir acción
    accion = elegir_accion(estado)

    # Obtener siguiente estado
    siguiente_estado = transiciones[(estado, accion)]

    # Obtener recompensa
    recompensa = recompensas[siguiente_estado]

    # ACTUALIZAR Q: Buscar el mejor valor futuro desde el nuevo estado
    mejor_futuro = max(Q[(siguiente_estado, a)] for a in acciones[siguiente_estado])

    # Fórmula de Q-Learning
    Q[(estado, accion)] = Q[(estado, accion)] + alpha * (
        recompensa + gamma * mejor_futuro - Q[(estado, accion)]
    )

    # Cambiar de estado
    estado = siguiente_estado

    # Mostrar progreso
    print(f"Iteración {i+1}: {Q}")


# RESULTADO FINAL
print("\nValores Q finales:")
for k, v in Q.items():
    print(k, "->", round(v, 2))