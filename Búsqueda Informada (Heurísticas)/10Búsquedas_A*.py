import heapq

def a_star(grafo, inicio, objetivo, heuristica):
    cola = []
    heapq.heappush(cola, (0, inicio))

    costo = {inicio: 0}
    camino = {inicio: None}

    while cola: 
        _, actual = heapq.heappop(cola)

        if actual == objetivo:
            ruta = []
            while actual:
                ruta.append(actual)
                actual = camino[actual]
            return ruta[::-1]
        
        for vecino, peso in grafo[actual]:
            nuevo_costo = costo [actual] + peso

            if vecino not in costo or nuevo_costo < costo[vecino]:
                costo[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino)
                heapq.heappush(cola, (prioridad, vecino))
                camino[vecino] = actual

    return None

def heuristica(nodo):
    valores= {
        'A': 5,
        'B': 3,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 0
    }
    return valores[nodo]


grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

print("Nodos disponibles: ", list(grafo.keys()))
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

resultado = a_star(grafo, inicio, objetivo, heuristica)

if resultado:
    print("Camino encontrado: ", resultado)
else:
    print("No hay camino")