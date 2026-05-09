import random

# Algoritmo de búsqueda Tabú
def tabu(grafo, inicio, objetivo, heuristica, max_iter=10, tabu_tam=3):

    # Nodo actual y mejor nodo encontrado
    actual = inicio
    mejor = actual

    # Guardar el camino recorrido
    camino = [actual]

    # Lista tabú para evitar repetir nodos recientes
    lista_tabu = []

    # Ejecutar iteraciones
    for _ in range(max_iter):

        # Obtener vecinos del nodo actual
        vecinos = grafo[actual]

        # Verificar si no hay vecinos
        if not vecinos:
            break

        # Filtrar vecinos que no estén en la lista tabú
        candidatos = [v[0] for v in vecinos if v[0] not in lista_tabu]

        # Si todos están prohibidos, usar todos los vecinos
        if not candidatos:
            candidatos = [v[0] for v in vecinos]

        # Elegir el mejor vecino según la heurística
        siguiente = min(candidatos, key=lambda x: heuristica[x])

        # Agregar nodo a la lista tabú
        lista_tabu.append(siguiente)

        # Mantener tamaño máximo de la lista tabú
        if len(lista_tabu) > tabu_tam:
            lista_tabu.pop(0)

        # Avanzar al siguiente nodo
        actual = siguiente
        camino.append(actual)

        # Actualizar mejor nodo encontrado
        if heuristica[actual] < heuristica[mejor]:
            mejor = actual

        # Detener si se llegó al objetivo
        if actual == objetivo:
            break

    # Retornar camino y mejor nodo encontrado
    return camino, mejor


# Grafo con pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('A', 1)],
    'E': [('F', 1)],
    'F': []
}

# Valores heurísticos
heuristica = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Mostrar nodos disponibles
print("Nodos disponibles:", list(grafo.keys()))

# Pedir datos al usuario
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

# Ejecutar búsqueda tabú
camino, mejor = tabu(grafo, inicio, objetivo, heuristica)

# Mostrar resultados
print("Camino recorrido:", camino)
print("Mejor nodo encontrado:", mejor)