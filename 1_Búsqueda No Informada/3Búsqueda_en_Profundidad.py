# Búsqueda en profundidad usando recursividad
def dfs_recursive(grafo, nodo, visitado=None, resultado=None):

    # Crear estructuras vacías en la primera ejecución
    if visitado is None:
        visitado = set()

    if resultado is None:
        resultado = []

    # Verificar si el nodo ya fue visitado
    if nodo not in visitado:

        # Mostrar y guardar el nodo actual
        print(nodo, end=" ")
        visitado.add(nodo)
        resultado.append(nodo)

        # Recorrer los vecinos del nodo
        for vecino in grafo.get(nodo, []):
            dfs_recursive(grafo, vecino, visitado, resultado)

    # Regresar el recorrido completo
    return resultado


# Grafo representado con un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

# Iniciar DFS desde el nodo B
print(dfs_recursive(grafo, 'B'))