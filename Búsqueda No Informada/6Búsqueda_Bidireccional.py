from collections import deque

def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]
    
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:

        camino_inicio = cola_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

    for vecino in grafo.get (nodo_inicio, []):
        if vecino not in visitados_inicio:
            nuevo_camino=camino_inicio + [vecino]
            visitados_inicio[vecino] = nuevo_camino
            cola_inicio.append(nuevo_camino)


            if vecino in visitados_objetivo:
                return nuevo_camino + visitados_objetivo[vecino][::-1][1:]
            
            camino_obj = cola_objetivo.popleft()
            nodo_obj = camino_obj[-1]

            for vecino in grafo.get(nodo_obj, []):
                if vecino not in visitados_objetivo:
                    nuevo_camino = camino_obj + [vecino]
                    visitados_objetivo[vecino] = nuevo_camino
                    cola_objetivo.append(nuevo_camino)

                    if vecino in visitados_inicio:
                        return visitados_inicio[vecino] + nuevo_camino[::-1][1:]
                    
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

resultado = bidireccional(grafo, inicio, objetivo)

if resultado:
    print("Camino encontrado: ", resultado)
else:
    print("No se encontró el objetivo")