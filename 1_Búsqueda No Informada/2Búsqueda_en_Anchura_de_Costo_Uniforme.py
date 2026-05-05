import heapq

# Esta función busca el camino de menor costo entre dos nodos usando búsqueda de costo uniforme
def costo_uniforme(grafo, inicio, objetivo):
    visitados = set()
    cola = [(0, [inicio])]  # (costo acumulado, camino)

    while cola:
        # sacamos el camino con menor costo hasta ahora
        costo, camino = heapq.heappop(cola)
        nodo = camino[-1]

        # si ya llegamos al objetivo, regresamos el resultado
        if nodo == objetivo:
            return costo, camino
        
        # si no lo hemos visitado, lo expandimos
        if nodo not in visitados:
            visitados.add(nodo)

            # revisamos sus vecinos y sumamos los costos
            for vecino, peso in grafo[nodo]:
                nuevo_costo = costo + peso
                nuevo_camino = camino + [vecino]  # extendemos el camino
                heapq.heappush(cola, (nuevo_costo, nuevo_camino))

    # si no se encontró ningún camino
    return None


# grafo con pesos (cada arista tiene un costo)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': []
}

resultado = costo_uniforme(grafo, 'A', 'F')

if resultado:
    costo, camino = resultado
    print("Costo mínimo:", costo)
    print("Camino:", " -> ".join(camino))
else:
    print("No se encontró camino")