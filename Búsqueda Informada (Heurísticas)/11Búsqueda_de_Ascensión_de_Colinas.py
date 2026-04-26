def hill_climbing(grafo, inicio, objetivo, heuristica):
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = grafo[actual]

        if not vecinos:
            return camino
        
        mejor = min(vecinos, key=lambda x: heuristica[x[0]])
        mejor_nodo = mejor[0]

        if heuristica[mejor_nodo] >= heuristica[actual]:
            return camino
        
        actual = mejor_nodo
        camino.append(actual)

    return camino

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristica = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

print("Nodos disponibles: ", list(grafo.keys()))
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

resultado = hill_climbing(grafo, inicio, objetivo, heuristica)


print("Camino recorrido: ", resultado)
