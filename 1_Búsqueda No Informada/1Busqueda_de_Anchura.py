from collections import deque

# Esta función busca el camino más corto entre dos nodos usando BFS
def bfs_camino(grafo, inicio, objetivo):
    visitados = set()              # aquí vamos guardando los nodos que ya vimos
    cola = deque([[inicio]])       # empezamos con un camino que solo tiene el inicio

    while cola:
        camino = cola.popleft()    # tomamos el primer camino que se agregó
        nodo = camino[-1]          # nos fijamos en el último nodo de ese camino

        # si ya llegamos al objetivo, regresamos el camino completo
        if nodo == objetivo:
            return camino

        # si todavía no hemos visitado este nodo, lo exploramos
        if nodo not in visitados:
            visitados.add(nodo)

            # recorremos sus vecinos para crear nuevos caminos
            for vecino in grafo[nodo]:
                nuevo_camino = camino + [vecino]  # extendemos el camino actual
                cola.append(nuevo_camino)         # lo metemos a la cola para revisarlo después

    # si se acaba todo y no encontramos nada, regresamos None
    return None


# aquí definimos el grafo (quién está conectado con quién)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Camino más corto de A a F:")
print(bfs_camino(grafo, 'A', 'F'))