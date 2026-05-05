def comparación_hacia_delante(grafo, color):
    dominios = {nodo: color[:] for nodo in grafo}
    asignacion = {}

    def es_valido(nodo, color):
        for vecino in grafo[nodo]:
            if vecino in asignacion and asignacion[vecino] == color:
                return False
        return True
    
    def fc(asignacion, dominios):
        if len(asignacion) == len(grafo):
            return asignacion
        
        nodo = next(n for n in grafo if n not in asignacion)

        for color in dominios[nodo]:
            if es_valido(nodo, color):
                nuevos_dominios = {n: dominios[n][:] for n in dominios}

                asignacion[nodo] = color

                for vecino in grafo[nodo]:
                    if vecino not in asignacion:
                        if color in nuevos_dominios[vecino]:
                            nuevos_dominios[vecino].remove(color)

                        if not nuevos_dominios[vecino]:
                            break

                else: 
                    resultado = fc(asignacion, nuevos_dominios)
                    if resultado:
                        return resultado
                    
                del asignacion[nodo]

        return None
    return fc(asignacion, dominios)

grafo = {
    'A': ['B','C'],
    'B': ['A','C','D'],
    'C': ['A', 'B', 'D'],
    'D': ['B','C']
}

colores = ['Rojo', 'Verde', 'Azul']

print("Nodos: ", list(grafo.keys()))
print("Colores: ", list(colores))

resultado = comparación_hacia_delante(grafo, colores)

if resultado:
        print("Solución encontrada: ")
        for nodo, color in resultado.items():
            print(nodo, " -> ", color)
else:
        print("No hay solución")