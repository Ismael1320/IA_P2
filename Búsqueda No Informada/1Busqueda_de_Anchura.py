from collections import deque

def bfs_camino(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino
        
        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None

if __name__ == "__main__" :
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Camino más corto de A a F: ")
    print(bfs_camino(grafo, 'A', 'F'))