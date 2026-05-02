def value_iteration(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=10):

    V = {s: 0 for s in estados}

    for _ in range(iteraciones):
        nuevo_V = V.copy()

        for s in estados:
            valores_acciones = []

            for a in acciones[s]:
                total = 0
                for (s2, prob) in transiciones[(s, a)]:
                    r = recompensas.get((s, a, s2), 0)
                    total += prob * (r + gamma * V[s2])

                valores_acciones.append(total)

            if valores_acciones:
                nuevo_V[s] = max(valores_acciones)

        V = nuevo_V

    return V



estados = ['A', 'B']

acciones = {
    'A': ['ir_B'],
    'B': ['ir_A']
}

transiciones = {
    ('A', 'ir_B'): [('B', 1.0)],
    ('B', 'ir_A'): [('A', 1.0)]
}

recompensas = {
    ('A', 'ir_B', 'B'): 5,
    ('B', 'ir_A', 'A'): 2
}

V = value_iteration(estados, acciones, transiciones, recompensas)

print("Valores óptimos:")
for estado, valor in V.items():
    print(estado, "->", round(valor, 2))