import heapq

def costo_uniforme(grafo, inicio, objetivo):
    visitados = set()
    cola = [(0, [inicio])]

    while cola:
        costo, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo == objetivo:
            return costo, camino
        
        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, peso in grafo[nodo]:
                nuevo_costo = costo +peso
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola, (nuevo_costo, nuevo_camino))

    return None

if __name__ == "__main__" :
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
        print("Costo minímo: ", costo)
        print("Camino:", " ".join(camino))
    else:
        print("No se encontro camino")