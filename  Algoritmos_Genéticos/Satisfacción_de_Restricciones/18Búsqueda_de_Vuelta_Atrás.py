def backtracking(grafo, actual, objetivo, visitados, camino):
    visitados.add(actual)
    camino.append(actual)

    print("Visitados: ", camino)

    if actual == objetivo:
        print("Camino encontrado: ", camino)
        return True
    
    for vecino in grafo[actual]:
        if vecino not in visitados:
            if backtracking(grafo, vecino, objetivo, visitados, camino):
                return True
            
    camino.pop()
    return False

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio = input("Nodo inicial: ")
objetivo = input("Nodo objetivo: ")

visitados = set()
camino = []

if not backtracking (grafo, inicio, objetivo, visitados, camino):
    print("No se encontró camino.")