import heapq

def greedy(grafo, inicio, objetivo, heuristica):
    cola = []
    heapq.heappush(cola, (heuristica(inicio), inicio))

    visitados = set()
    camino = {inicio: None}

    while cola: 
        _, actual = heapq.heappop(cola)

        if actual == objetivo:
            ruta = []
            while actual:
                ruta.append(actual)
                actual = camino[actual]
            return ruta[::-1]
        
        visitados.add(actual)

        for vecino, _ in grafo[actual]:
            if vecino not in visitados:
                heapq.heappush(cola, (heuristica(vecino), vecino))
                if vecino not in camino:
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

resultado = greedy(grafo, inicio, objetivo, heuristica)

if resultado:
    print("Camino encontrado: ", resultado)
else:
    print("No hay camino")