# AO* básico (simplificado)

# Grafo con relaciones AND / OR
grafo = {
    'A': [['B', 'C'], ['D']],  # A puede ir por B y C, o solo D
    'B': [['E']],
    'C': [['F']],
    'D': [],
    'E': [],
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

# Función AO*
def ao_star(nodo):

    # Verificar si el nodo es final
    if nodo not in grafo or not grafo[nodo]:
        return heuristica[nodo], [nodo]

    # Inicializar mejor costo y camino
    mejor_costo = float('inf')
    mejor_camino = []

    # Recorrer opciones AND / OR
    for opcion in grafo[nodo]:

        costo_total = 0
        camino_total = [nodo]

        # Evaluar cada hijo de la opción
        for hijo in opcion:

            # Llamada recursiva
            costo_hijo, camino_hijo = ao_star(hijo)

            # Sumar costos y caminos
            costo_total += costo_hijo
            camino_total += camino_hijo

        # Guardar la mejor opción
        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_camino = camino_total

    # Retornar mejor costo y camino
    return mejor_costo, mejor_camino


# Pedir nodo inicial
inicio = input("Nodo inicial: ").upper()

# Ejecutar AO*
costo, camino = ao_star(inicio)

# Mostrar resultados
print("Mejor camino:", " -> ".join(camino))
print("Costo estimado:", costo)