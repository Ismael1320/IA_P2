def  dfs_recursive (grafo, nodo, visitado = None):   
    if visitado is None:
        visitado = set()
    
    if nodo not in visitado:
        print(nodo, end=" ")
        visitado.add(nodo)

        for vecino in grafo[nodo]:
            dfs_recursive (grafo, vecino, visitado)
grafo = {
        'A': ['B' 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
dfs_recursive (grafo, 'A')