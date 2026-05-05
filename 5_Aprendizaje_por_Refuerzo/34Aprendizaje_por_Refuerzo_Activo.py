import random

# Estados del sistema
estados = ['A', 'B']


# Acciones posibles en cada estado
acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

# Transiciones del sistema
transiciones = {
    ('A', 'ir_B'): 'B',
    ('B', 'ir_A'): 'A'
}

# Recompensas por llegar a un estado
recompensas = {
    'A': 2,
    'B': 5
}

# Inicializamos la tabla Q
# Q(estado, acción)
Q = {}
for s in estados:
    for a in acciones[s]:
        Q[(s, a)] = 0  # empezamos sin conocimiento

# Parámetros del aprendizaje
alpha = 0.1   # qué tanto aprende cada vez
gamma = 0.9   # importancia del futuro
epsilon = 0.2 # probabilidad de explorar

# Función para elegir acción
def elegir_accion(estado):
    # Con probabilidad epsilon → explorar (acción aleatoria)
    if random.random() < epsilon:
        return random.choice(acciones[estado])
    else:
        # Elegir la mejor acción conocida (explotar)
        return max(acciones[estado], key=lambda a: Q[(estado, a)])

# Algoritmo Q-Learning
def q_learning(episodios=20):
    estado = 'A'  # estado inicial

    for i in range(episodios):

        # Elegir acción (exploración o explotación)
        accion = elegir_accion(estado)

        # Obtener siguiente estado
        siguiente_estado = transiciones[(estado, accion)]

        # Obtener recompensa
        recompensa = recompensas[siguiente_estado]


        # ACTUALIZACIÓN Q-LEARNING: Buscar el mejor valor futuro posible
        mejor_futuro = max(Q[(siguiente_estado, a)] for a in acciones[siguiente_estado])

        # Actualizar valor Q
        Q[(estado, accion)] = Q[(estado, accion)] + alpha * (
            recompensa + gamma * mejor_futuro - Q[(estado, accion)]
        )

        # Pasar al siguiente estado
        estado = siguiente_estado

        # Mostrar progreso
        print(f"Iteración {i+1}: Estado {estado}, Q = { {k: round(v,2) for k,v in Q.items()} }")

    return Q


print("Estados:", estados)
print("Acciones:", acciones)

tabla_q = q_learning()

print("\nValores Q finales:")
for clave, valor in tabla_q.items():
    print(clave, "->", round(valor, 2))