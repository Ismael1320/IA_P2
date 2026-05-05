def iteracion_de_politicas(estados, acciones, transiciones, recompensas, gamma=0.9, iteraciones=10):
    politica={s: acciones[s][0] for s in estados}
    V={s: 0 for s in estados}

    for _ in range(10):
        nuevo_V = V.copy()
        for s in estados:
            a=politica[s]
            total=0
            for (s2, prob) in  transiciones[(s, a)]:
                r= recompensas.get((s, a, s2), 0)
                total += prob*(r + gamma *V[s2])
                nuevo_V[s] = total
            V = nuevo_V

        estable = True
        for s in estados:
            mejor_accion = None
            mejor_valor = float('-inf')

            for a in acciones[s]:
                total = 0
                for (s2, prob) in transiciones[(s, a)]:
                    r= recompensas.get((s, a, s2), 0)
                    total += prob*(r + gamma *V[s2])

                    if total > mejor_valor:
                        mejor_valor =total
                        mejor_accion = a

                if mejor_accion != politica[s]:
                    politica[s] = mejor_accion
                    estable = False

            if estable:
                break

    return politica, V

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

politica, valores = iteracion_de_politicas(estados, acciones, transiciones, recompensas)

print ("Política óptima: ")
for estado, accion in politica.items():
    print(estado, "->", accion)

print ("\nValores: ")
for estado, valor in valores.items():
    print(estado, "->", round(valor, 2))