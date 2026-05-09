# Algoritmo Value Iteration
def value_iteration(
    estados,
    acciones,
    transiciones,
    recompensas,
    gamma=0.9,
    iteraciones=10
):

    # Inicializar valores de los estados
    V = {s: 0 for s in estados}

    # Ejecutar iteraciones
    for _ in range(iteraciones):

        # Copiar valores actuales
        nuevo_V = V.copy()

        # Recorrer estados
        for s in estados:

            valores_acciones = []

            # Revisar acciones disponibles
            for a in acciones[s]:

                total = 0

                # Revisar transiciones posibles
                for (s2, prob) in transiciones[(s, a)]:

                    # Obtener recompensa
                    r = recompensas.get((s, a, s2), 0)

                    # Calcular valor esperado
                    total += prob * (
                        r + gamma * V[s2]
                    )

                valores_acciones.append(total)

            # Guardar mejor valor del estado
            if valores_acciones:
                nuevo_V[s] = max(valores_acciones)

        # Actualizar valores
        V = nuevo_V

    return V


# Lista de estados
estados = ['A', 'B']

# Acciones disponibles
acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

# Modelo de transiciones
transiciones = {
    ('A', 'ir_B'): [('B', 1.0)],
    ('B', 'ir_A'): [('A', 1.0)]
}

# Recompensas
recompensas = {
    ('A', 'ir_B', 'B'): 5,
    ('B', 'ir_A', 'A'): 2
}

# Ejecutar Value Iteration
V = value_iteration(
    estados,
    acciones,
    transiciones,
    recompensas
)

# Mostrar resultados
print("Valores óptimos:")

for estado, valor in V.items():
    print(estado, "->", round(valor, 2))