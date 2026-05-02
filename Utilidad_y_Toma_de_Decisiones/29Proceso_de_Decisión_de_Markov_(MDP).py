def evaluar_politica(estados, politica, transiciones, recompensas, gamma=0.9, iteraciones=10):
    V={s: 0 for s in estados}

    for _ in range(iteraciones):
        nuevo_V = V.copy()

        for s in estados:
            a = politica[s]
            total=0
            
            for (s2, prob) in transiciones.get((s, a), []):
                r = recompensas.get((s, a, s2), 0)
                total += prob*(r + gamma *V[s2])

            nuevo_V[s] = total

        V = nuevo_V

       
    return V

estados = ['A', 'B']

acciones = {
    'A' : ['ir_B'],
    'B' : ['ir_A']
}

transiciones = {
    ('A', 'ir_B'): [('B', 1.0)],
    ('B', 'ir_A'): [('A', 1.0)]
}

recompensas = {
    ('A', 'ir_B', 'B'): 5,
    ('B', 'ir_A', 'A'): 2
}

politica = {
    'A' : 'ir_B',
    'B' : 'ir_A'
} 

valores = evaluar_politica(estados,politica, transiciones, recompensas, iteraciones=50)

print ("Valores de la política: ")
for estado, valor in valores.items():
    print(estado, "->", round(valor, 2))