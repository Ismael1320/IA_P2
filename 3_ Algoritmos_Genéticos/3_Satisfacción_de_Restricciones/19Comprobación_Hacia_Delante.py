# Forward Checking para coloreo de grafos
def comparacion_hacia_delante(grafo, colores):

    # Crear dominios iniciales para cada nodo
    dominios = {nodo: colores[:] for nodo in grafo}

    # Guardar asignaciones realizadas
    asignacion = {}

    # Verificar si un color es válido
    def es_valido(nodo, color):

        for vecino in grafo[nodo]:

            # Evitar colores repetidos en vecinos
            if vecino in asignacion and asignacion[vecino] == color:
                return False

        return True

    # Función principal de Forward Checking
    def fc(asignacion, dominios):

        # Verificar si todos los nodos fueron asignados
        if len(asignacion) == len(grafo):
            return asignacion

        # Seleccionar nodo sin asignar
        nodo = next(n for n in grafo if n not in asignacion)

        # Probar colores disponibles
        for color in dominios[nodo]:

            # Verificar si el color es válido
            if es_valido(nodo, color):

                # Copiar dominios actuales
                nuevos_dominios = {
                    n: dominios[n][:]
                    for n in dominios
                }

                # Asignar color al nodo
                asignacion[nodo] = color

                # Actualizar dominios de vecinos
                for vecino in grafo[nodo]:

                    if vecino not in asignacion:

                        if color in nuevos_dominios[vecino]:
                            nuevos_dominios[vecino].remove(color)

                        # Verificar dominio vacío
                        if not nuevos_dominios[vecino]:
                            break

                else:

                    # Llamada recursiva
                    resultado = fc(
                        asignacion,
                        nuevos_dominios
                    )

                    if resultado:
                        return resultado

                # Retroceder si no funciona
                del asignacion[nodo]

        return None

    return fc(asignacion, dominios)


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Mostrar información
print("Nodos:", list(grafo.keys()))
print("Colores:", colores)

# Ejecutar Forward Checking
resultado = comparacion_hacia_delante(grafo, colores)

# Mostrar resultado
if resultado:

    print("Solución encontrada:")

    for nodo, color in resultado.items():
        print(nodo, "->", color)

else:
    print("No hay solución")