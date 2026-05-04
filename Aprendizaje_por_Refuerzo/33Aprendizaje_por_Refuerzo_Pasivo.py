# Estados del sistema
estados = ['A', 'B']

# Política fija (qué acción tomar en cada estado): El agente NO decide, solo sigue esto
politica = {
    'A': 'ir_B',
    'B': 'ir_A'
}

# Transiciones del sistema (determinísticas en este ejemplo)
transiciones = {
    ('A', 'ir_B'): 'B',
    ('B', 'ir_A'): 'A'
}

# Recompensas al llegar a un estado
recompensas = {
    'A': 2,
    'B': 5
}

# Inicializamos valores estimados en 0
V = {s: 0 for s in estados}

# Factor de descuento (importancia del futuro)
gamma = 0.9

# Tasa de aprendizaje (qué tanto ajustamos cada vez)
alpha = 0.1


# Función que ejecuta el aprendizaje
def aprendizaje_pasivo(episodios=20):
    estado = 'A'  # estado inicial

    # Repetimos varios episodios
    for i in range(episodios):

        # Acción según la política (NO se elige, ya está definida)
        accion = politica[estado]

        # Obtenemos el siguiente estado
        siguiente_estado = transiciones[(estado, accion)]

        # Obtenemos recompensa del nuevo estado
        recompensa = recompensas[siguiente_estado]

        # ACTUALIZACIÓN (Temporal Difference): Ajustamos el valor del estado actual
        V[estado] = V[estado] + alpha * (
            recompensa + gamma * V[siguiente_estado] - V[estado]
        )

        # Nos movemos al siguiente estado
        estado = siguiente_estado

        # Mostrar progreso
        print(f"Iteración {i+1}: Estado {estado}, Valores { {k: round(v,2) for k,v in V.items()} }")

    return V


print("Estados:", estados)
print("Política fija:", politica)

valores = aprendizaje_pasivo()

print("\nValores finales aprendidos:")
for estado, valor in valores.items():
    print(estado, "->", round(valor, 2))