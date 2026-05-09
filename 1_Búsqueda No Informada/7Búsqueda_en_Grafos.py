from collections import deque

# Búsqueda en grafos usando una cola
def busqueda_en_grafos(grafo, inicio, objetivo):

    # Conjunto para guardar nodos visitados
    visitados = set()

    # Cola con el nodo inicial
    cola = deque([[inicio]])

    # Continuar mientras haya caminos en la cola
    while cola:

        # Obtener el primer camino de la cola
        camino = cola.popleft()

        # Obtener el último nodo del camino
        nodo = camino[-1]

        # Verificar si se encontró el objetivo
        if nodo == objetivo:
            return camino

        # Revisar si el nodo ya fue visitado
        if nodo not in visitados:

            # Marcar nodo como visitado
            visitados.add(nodo)

            # Recorrer vecinos del nodo actual
            for vecino in grafo.get(nodo, []):

                # Crear un nuevo camino
                nuevo_camino = camino + [vecino]

                # Agregar el nuevo camino a la cola
                cola.append(nuevo_camino)

    # Retornar None si no se encontró el objetivo
    return None


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E'],
}

# Pedir datos al usuario
inicio = input("Nodo inicial: ")
objetivo = input("Nodo objetivo: ")

# Ejecutar la búsqueda
resultado = busqueda_en_grafos(grafo, inicio, objetivo)

# Mostrar resultado final
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No se encontró el objetivo")