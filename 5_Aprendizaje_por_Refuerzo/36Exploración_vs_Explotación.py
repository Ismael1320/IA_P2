import random

# Opciones disponibles
opciones = ['A', 'B', 'C']

# Recompensas reales (desconocidas para el agente): Simulan qué tan buena es cada opción
recompensas_reales = {
    'A': 2,
    'B': 5,
    'C': 3
}

# Estimación inicial (lo que el agente cree)
Q = {op: 0 for op in opciones}

# Parámetros
epsilon = 0.3  # probabilidad de explorar
alpha = 0.1    # aprendizaje

# Función para elegir opción
def elegir_opcion():
    # EXPLORACIÓN: elegir al azar
    if random.random() < epsilon:
        return random.choice(opciones)
    
    # EXPLOTACIÓN: elegir la mejor conocida
    return max(opciones, key=lambda op: Q[op])


# Simulación
for i in range(20):

    # Elegir opción
    opcion = elegir_opcion()

    # Obtener recompensa real
    recompensa = recompensas_reales[opcion]

    # Actualizar estimación
    Q[opcion] = Q[opcion] + alpha * (recompensa - Q[opcion])

    # Mostrar progreso
    print(f"Iteración {i+1}: Elegido {opcion}, Q = { {k: round(v,2) for k,v in Q.items()} }")

# Resultado final
print("\nMejor opción aprendida:")
mejor = max(opciones, key=lambda op: Q[op])
print(mejor, "con valor", round(Q[mejor], 2))