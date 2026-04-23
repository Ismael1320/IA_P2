def dfs_recursive(grafo, nodo, visitado=None, resultado=None):
    if visitado is None:
        visitado= set()

    if resultado is None:
        resultado = []

    if nodo not in visitado:
        print(nodo, end= " ")
        visitado.add(nodo)
        resultado.append(nodo)

        for vecino in grafo.get(nodo, []):
            dfs_recursive(grafo, vecino, visitado, resultado)

    return resultado

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

print(dfs_recursive(grafo, 'B'))