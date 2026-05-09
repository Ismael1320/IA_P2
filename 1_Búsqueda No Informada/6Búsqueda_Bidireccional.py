from collections import deque

# Búsqueda bidireccional
def bidireccional(grafo, inicio, objetivo):

    # Verificar si inicio y objetivo son iguales
    if inicio == objetivo:
        return [inicio]

    # Colas para buscar desde ambos extremos
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    # Diccionarios para guardar nodos visitados y caminos
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    # Continuar mientras existan nodos por recorrer
    while cola_inicio and cola_objetivo:

        # Expandir desde el inicio
        camino_inicio = cola_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

        # Recorrer vecinos del nodo actual
        for vecino in grafo.get(nodo_inicio, []):

            # Evitar repetir nodos
            if vecino not in visitados_inicio:

                # Crear nuevo camino
                nuevo_camino = camino_inicio + [vecino]

                # Guardar vecino visitado
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                # Verificar si ambos recorridos se encontraron
                if vecino in visitados_objetivo:
                    return nuevo_camino + visitados_objetivo[vecino][::-1][1:]

        # Expandir desde el objetivo
        camino_obj = cola_objetivo.popleft()
        nodo_obj = camino_obj[-1]

        # Recorrer vecinos del nodo actual
        for vecino in grafo.get(nodo_obj, []):

            # Evitar repetir nodos
            if vecino not in visitados_objetivo:

                # Crear nuevo camino
                nuevo_camino = camino_obj + [vecino]

                # Guardar vecino visitado
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)

                # Verificar si ambos recorridos se encontraron
                if vecino in visitados_inicio:
                    return visitados_inicio[vecino] + nuevo_camino[::-1][1:]

    # Retornar None si no existe camino
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

# Ejecutar búsqueda bidireccional
resultado = bidireccional(grafo, inicio, objetivo)

# Mostrar resultado final
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No se encontró el objetivo")