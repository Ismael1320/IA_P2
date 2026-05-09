import heapq

# Búsqueda Greedy Best First Search
def greedy(grafo, inicio, objetivo, heuristica):

    # Cola de prioridad
    cola = []

    # Agregar nodo inicial usando su heurística
    heapq.heappush(cola, (heuristica(inicio), inicio))

    # Conjunto de nodos visitados
    visitados = set()

    # Diccionario para guardar el camino
    camino = {inicio: None}

    # Continuar mientras haya nodos en la cola
    while cola:

        # Obtener el nodo con menor heurística
        _, actual = heapq.heappop(cola)

        # Verificar si se llegó al objetivo
        if actual == objetivo:

            # Reconstruir la ruta
            ruta = []

            while actual:
                ruta.append(actual)
                actual = camino[actual]

            return ruta[::-1]

        # Marcar nodo como visitado
        visitados.add(actual)

        # Recorrer vecinos del nodo actual
        for vecino, _ in grafo[actual]:

            # Evitar repetir nodos
            if vecino not in visitados:

                # Agregar vecino a la cola según su heurística
                heapq.heappush(cola, (heuristica(vecino), vecino))

                # Guardar el nodo anterior
                if vecino not in camino:
                    camino[vecino] = actual

    # Retornar None si no existe camino
    return None


# Función heurística
def heuristica(nodo):

    valores = {
        'A': 5,
        'B': 3,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 0
    }

    return valores[nodo]


# Grafo con pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Mostrar nodos disponibles
print("Nodos disponibles:", list(grafo.keys()))

# Pedir datos al usuario
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

# Ejecutar búsqueda Greedy
resultado = greedy(grafo, inicio, objetivo, heuristica)

# Mostrar resultado final
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No hay camino")