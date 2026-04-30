def es_valido(nodo, color, asignacion, grafo):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True


def resolver_arbol(asignacion, grafo, colores):

    if len(asignacion) == len(grafo):
        return asignacion

    nodo = next(n for n in grafo if n not in asignacion)

    for color in colores:
        if es_valido(nodo, color, asignacion, grafo):
            asignacion[nodo] = color
            resultado = resolver_arbol(asignacion, grafo, colores)
            if resultado:
                return resultado
            del asignacion[nodo]

    return None


def cutset_conditioning(grafo, colores, cutset):
    from itertools import product


    for combinacion in product(colores, repeat=len(cutset)):
        asignacion = {}

        valido = True
        for nodo, color in zip(cutset, combinacion):
            if es_valido(nodo, color, asignacion, grafo):
                asignacion[nodo] = color
            else:
                valido = False
                break

        if not valido:
            continue

        resultado = resolver_arbol(asignacion, grafo, colores)
        if resultado:
            return resultado

    return None


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colores = ['Rojo', 'Verde', 'Azul']


cutset = ['C']

print("Nodos:", list(grafo.keys()))
print("Cutset:", cutset)

resultado = cutset_conditioning(grafo, colores, cutset)

if resultado:
    print("Solución encontrada:")
    for nodo, color in resultado.items():
        print(nodo, "->", color)
else:
    print("No hay solución")