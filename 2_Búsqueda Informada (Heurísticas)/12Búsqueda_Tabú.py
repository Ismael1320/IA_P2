import random

def tabu(grafo, inicio, objetivo, heuristica, max_iter = 10, tabu_tam = 3):
    actual = inicio
    mejor = actual
    camino = [actual]

    lista_tabu = []

    for _ in range(max_iter):
        vecinos = grafo[actual]

        if not vecinos:
            break

        candidatos = [v[0] for v in vecinos if v[0] not in lista_tabu]

        if not candidatos:
            candidatos = [v[0] for v in vecinos]


        siguiente = min(candidatos, key = lambda x: heuristica[x])

        lista_tabu.append(siguiente)
        if len(lista_tabu) > tabu_tam:
            lista_tabu.pop(0)

            actual = siguiente
            camino.append(actual)

            if heuristica[actual] < heuristica[mejor]:
                mejor = actual

            if actual == objetivo:
                break

    return camino, mejor

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('A', 1)],
    'E': [('F', 1)],
    'F': []
}

heuristica = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

print("Nodos disponibles: ", list(grafo.keys()))
inicio = input("Nodo inicial: ").upper()
objetivo = input("Nodo objetivo: ").upper()

camino, mejor = tabu(grafo, inicio, objetivo, heuristica)


print("Camino recorrido: ", camino)
print("Mejor nodo encontrado: ", mejor)