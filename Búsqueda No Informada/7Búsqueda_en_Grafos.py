from collections import deque

def busqueda_en_grafos(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino
        
        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo.get(nodo, []):
                nuevo_camino = camino + [vecino]
                cola.append(nuevo_camino)

    return None

grafo = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A','F'],
    'D': ['B','G'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E'],
}

inicio = input("Nodo inicial: ")
objetivo = input("Nodo objetivo: ")

resultado = busqueda_en_grafos(grafo, inicio, objetivo)

if resultado:
    print("Camino encontrado: ", resultado)
else:
    print("No se encontró el objetivo")