import heapq

# Algoritmo A* para encontrar el mejor camino
def a_star(grafo, inicio, objetivo, heuristica):

    # Cola de prioridad
    cola = []

    # Agregar nodo inicial
    heapq.heappush(cola, (0, inicio))

    # Guardar el costo acumulado
    costo = {inicio: 0}

    # Guardar el camino recorrido
    camino = {inicio: None}

    # Continuar mientras haya nodos en la cola
    while cola:

        # Obtener nodo con menor prioridad
        _, actual = heapq.heappop(cola)

        # Verificar si se llegó al objetivo
        if actual == objetivo:

            # Reconstruir la ruta
            ruta = []

            while actual:
                ruta.append(actual)
                actual = camino[actual]

            return ruta[::-1]

        # Recorrer vecinos del nodo actual
        for vecino, peso in grafo[actual]:

            # Calcular nuevo costo
            nuevo_costo = costo[actual] + peso

            # Actualizar si el costo es menor
            if vecino not in costo or nuevo_costo < costo[vecino]:

                costo[vecino] = nuevo_costo

                # Calcular prioridad usando heurística
                prioridad = nuevo_costo + heuristica(vecino)

                # Agregar vecino a la cola
                heapq.heappush(cola, (prioridad, vecino))

                # Guardar nodo anterior
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

# Ejecutar algoritmo A*
resultado = a_star(grafo, inicio, objetivo, heuristica)

# Mostrar resultado final
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No hay camino")