# Algoritmo Hill Climbing
def hill_climbing(grafo, inicio, objetivo, heuristica):

    # Nodo actual
    actual = inicio

    # Guardar el camino recorrido
    camino = [actual]

    # Continuar hasta llegar al objetivo
    while actual != objetivo:

        # Obtener vecinos del nodo actual
        vecinos = grafo[actual]

        # Verificar si el nodo no tiene vecinos
        if not vecinos:
            return camino

        # Elegir el vecino con mejor heurística
        mejor = min(vecinos, key=lambda x: heuristica[x[0]])
        mejor_nodo = mejor[0]

        # Detener si no hay mejora
        if heuristica[mejor_nodo] >= heuristica[actual]:
            return camino

        # Avanzar al mejor nodo
        actual = mejor_nodo
        camino.append(actual)

    # Retornar camino encontrado
    return camino


# Grafo con pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Valores heurísticos
heuristica = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Mostrar nodos disponibles
print("Nodos disponibles:", list(grafo.keys()))

# Pedir datos al usuario
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

# Ejecutar Hill Climbing
resultado = hill_climbing(grafo, inicio, objetivo, heuristica)

# Mostrar resultado
print("Camino recorrido:", resultado)