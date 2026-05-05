# Estados del sistema
estados = ['A', 'B']

# Acciones posibles
acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

# Valores Q (simulan lo aprendido)
# (estado, acción) -> valor
Q = {
    ('A', 'ir_B'): 31.0,
    ('B', 'ir_A'): 34.0
}

# Función para obtener política
def obtener_politica(estados, acciones, Q):
    politica = {}

    # Recorremos cada estado
    for estado in estados:

        # Elegimos la acción con mayor valor Q
        mejor_accion = max(
            acciones[estado], 
            key=lambda a: Q[(estado, a)]
        )

        # Guardamos la mejor acción para ese estado
        politica[estado] = mejor_accion

    return politica




print("Valores Q:", Q)

politica = obtener_politica(estados, acciones, Q)

print("\nPolítica encontrada:\n")

for estado, accion in politica.items():
    print(estado, "->", accion)