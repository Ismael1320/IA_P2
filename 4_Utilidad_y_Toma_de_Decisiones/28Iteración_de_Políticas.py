# Función que aplica iteración de políticas
def iteracion_de_politicas(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=10):
    
    # Se elige una acción inicial para cada estado
    politica = {s: acciones[s][0] for s in estados}
    
    # Valores iniciales de los estados
    V = {s: 0 for s in estados}

    # Ciclo principal de iteraciones
    for _ in range(10):
        nuevo_V = V.copy()

        # Evaluación de la política actual
        for s in estados:
            a = politica[s]
            total = 0

            # Se calcula el valor esperado del estado
            for (s2, prob) in transiciones[(s, a)]:
                r = recompensas.get((s, a, s2), 0)
                total += prob * (r + gamma * V[s2])

            nuevo_V[s] = total

        V = nuevo_V

        # Verifica si la política cambia
        estable = True

        # Mejora de la política
        for s in estados:
            mejor_accion = None
            mejor_valor = float('-inf')

            # Se prueban todas las acciones posibles
            for a in acciones[s]:
                total = 0

                for (s2, prob) in transiciones[(s, a)]:
                    r = recompensas.get((s, a, s2), 0)
                    total += prob * (r + gamma * V[s2])

                # Guarda la acción con mayor valor
                if total > mejor_valor:
                    mejor_valor = total
                    mejor_accion = a

            # Actualiza la política si encuentra una mejor acción
            if mejor_accion != politica[s]:
                politica[s] = mejor_accion
                estable = False

        # Si ya no cambia, termina el proceso
        if estable:
            break

    return politica, V


# Lista de estados
estados = ['A', 'B']

# Acciones disponibles en cada estado
acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

# Probabilidades de transición
transiciones = {
    ('A', 'ir_B'): [('B', 1.0)],
    ('B', 'ir_A'): [('A', 1.0)]
}

# Recompensas por cada transición
recompensas = {
    ('A', 'ir_B', 'B'): 5,
    ('B', 'ir_A', 'A'): 2
}

# Ejecuta el algoritmo
politica, valores = iteracion_de_politicas(
    estados,
    acciones,
    transiciones,
    recompensas
)

# Muestra la política óptima
print("Política óptima:")
for estado, accion in politica.items():
    print(estado, "->", accion)

# Muestra el valor de cada estado
print("\nValores:")
for estado, valor in valores.items():
    print(estado, "->", round(valor, 2))