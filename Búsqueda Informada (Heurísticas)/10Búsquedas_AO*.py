# AO* básico (simplificado)

grafo = {
    'A': [['B', 'C'], ['D']],  # A puede ir por (B AND C) o solo D
    'B': [['E']],
    'C': [['F']],
    'D': [],
    'E': [],
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

def ao_star(nodo):
    # Si es nodo final
    if nodo not in grafo or not grafo[nodo]:
        return heuristica[nodo], [nodo]

    mejor_costo = float('inf')
    mejor_camino = []

    for opcion in grafo[nodo]:  # AND / OR
        costo_total = 0
        camino_total = [nodo]

        for hijo in opcion:
            costo_hijo, camino_hijo = ao_star(hijo)
            costo_total += costo_hijo
            camino_total += camino_hijo

        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_camino = camino_total

    return mejor_costo, mejor_camino


if __name__ == "__main__":
    inicio = input("Nodo inicial: ").upper()

    costo, camino = ao_star(inicio)

    print("Mejor camino:", " -> ".join(camino))
    print("Costo estimado:", costo)