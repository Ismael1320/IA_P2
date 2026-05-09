# Backjumping dirigido por conflictos
def cbj(grafo, colores):

    # Guardar asignaciones de colores
    asignacion = {}

    # Guardar conflictos de cada nodo
    conflictos = {
        nodo: set()
        for nodo in grafo
    }

    # Verificar si un color es válido
    def es_valido(nodo, color):

        for vecino in grafo[nodo]:

            # Verificar conflicto de color
            if vecino in asignacion and asignacion[vecino] == color:
                return False, vecino

        return True, None

    # Función recursiva de búsqueda
    def resolver(nodos, i=0):

        # Verificar si todos los nodos fueron asignados
        if i == len(nodos):
            return True

        # Obtener nodo actual
        nodo = nodos[i]

        # Probar colores disponibles
        for color in colores:

            valido, conflicto = es_valido(nodo, color)

            # Asignar color si es válido
            if valido:

                asignacion[nodo] = color

                # Llamada recursiva
                if resolver(nodos, i + 1):
                    return True

                # Retroceder si no funciona
                del asignacion[nodo]

            else:
                # Guardar conflicto encontrado
                conflictos[nodo].add(conflicto)

        return False

    # Lista de nodos
    nodos = list(grafo.keys())

    # Ejecutar algoritmo CBJ
    resolver(nodos)

    return asignacion


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

# Colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Mostrar información
print("Nodos:", list(grafo.keys()))
print("Colores:", colores)

# Ejecutar CBJ
resultado = cbj(grafo, colores)

# Mostrar resultado
if resultado:

    print("Asignación válida:")

    for nodo, color in resultado.items():
        print(nodo, "->", color)

else:
    print("No hay solución")