# Búsqueda con backtracking
def backtracking(grafo, actual, objetivo, visitados, camino):

    # Marcar nodo como visitado
    visitados.add(actual)

    # Agregar nodo al camino
    camino.append(actual)

    # Mostrar nodos visitados
    print("Visitados:", camino)

    # Verificar si se llegó al objetivo
    if actual == objetivo:
        print("Camino encontrado:", camino)
        return True

    # Recorrer vecinos del nodo actual
    for vecino in grafo[actual]:

        # Evitar repetir nodos
        if vecino not in visitados:

            # Llamada recursiva
            if backtracking(
                grafo,
                vecino,
                objetivo,
                visitados,
                camino
            ):
                return True

    # Retroceder si no se encuentra solución
    camino.pop()

    return False


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Pedir datos al usuario
inicio = input("Nodo inicial: ")
objetivo = input("Nodo objetivo: ")

# Estructuras auxiliares
visitados = set()
camino = []

# Ejecutar backtracking
if not backtracking(
    grafo,
    inicio,
    objetivo,
    visitados,
    camino
):
    print("No se encontró camino.")