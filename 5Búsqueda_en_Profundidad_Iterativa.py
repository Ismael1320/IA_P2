def dls(grafo, nodo, objetivo, limite, profundidad=0, camino=None):
    if camino is None:
        camino =[]

    camino.append(nodo)

    if nodo == objetivo:
        return camino

    if profundidad == limite:
        return None
    
    for vecino in grafo.get(nodo, []):
        if vecino not in camino:
            resultado = dls(grafo, vecino, objetivo, limite, profundidad + 1, camino.copy())
            if resultado is not None:
                return resultado
    
    return None

def iddfs(grafo, inicio, objetivo, max_limite):
    for limite in range(max_limite + 1):
        print(f"Buscando con límite = {limite}")
        resultado = dls(grafo, inicio, objetivo, limite)

        if resultado is not None:
            return resultado
    
    return None

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': [],
}

inicio = input("Nodo inicial: ")
objetivo = input("Nodo objetivo: ")
max_limite = int(input("Límite máximo de profundidad: "))

resultado = iddfs(grafo, inicio, objetivo, max_limite)

if resultado:
    print("Camino encontrado: ", resultado)
else:
    print("No se encontró el objetivo")