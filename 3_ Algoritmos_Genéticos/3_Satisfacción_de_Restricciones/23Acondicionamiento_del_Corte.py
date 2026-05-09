# Verificar si un color es válido para un nodo
def es_valido(nodo, color, asignacion, grafo):

    # Revisar vecinos del nodo
    for vecino in grafo[nodo]:

        # Verificar si algún vecino tiene el mismo color
        if vecino in asignacion and asignacion[vecino] == color:
            return False

    return True


# Resolver el problema usando backtracking
def resolver_arbol(asignacion, grafo, colores):

    # Verificar si todos los nodos fueron asignados
    if len(asignacion) == len(grafo):
        return asignacion

    # Seleccionar nodo sin asignar
    nodo = next(n for n in grafo if n not in asignacion)

    # Probar colores disponibles
    for color in colores:

        # Verificar si el color es válido
        if es_valido(nodo, color, asignacion, grafo):

            # Asignar color al nodo
            asignacion[nodo] = color

            # Llamada recursiva
            resultado = resolver_arbol(
                asignacion,
                grafo,
                colores
            )

            # Retornar solución encontrada
            if resultado:
                return resultado

            # Retroceder si no funciona
            del asignacion[nodo]

    return None


# Algoritmo Cutset Conditioning
def cutset_conditioning(grafo, colores, cutset):

    from itertools import product

    # Generar combinaciones posibles del cutset
    for combinacion in product(
        colores,
        repeat=len(cutset)
    ):

        asignacion = {}

        valido = True

        # Asignar colores al cutset
        for nodo, color in zip(cutset, combinacion):

            if es_valido(nodo, color, asignacion, grafo):
                asignacion[nodo] = color

            else:
                valido = False
                break

        # Continuar si la combinación no es válida
        if not valido:
            continue

        # Resolver el resto del grafo
        resultado = resolver_arbol(
            asignacion,
            grafo,
            colores
        )

        # Retornar solución encontrada
        if resultado:
            return resultado

    return None


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Nodos del cutset
cutset = ['C']

# Mostrar información
print("Nodos:", list(grafo.keys()))
print("Cutset:", cutset)

# Ejecutar Cutset Conditioning
resultado = cutset_conditioning(
    grafo,
    colores,
    cutset
)

# Mostrar resultado
if resultado:

    print("Solución encontrada:")

    for nodo, color in resultado.items():
        print(nodo, "->", color)

else:
    print("No hay solución")