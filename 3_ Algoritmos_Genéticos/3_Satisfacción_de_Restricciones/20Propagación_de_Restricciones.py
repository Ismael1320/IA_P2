# Verificar si un valor es válido
def es_valido(variable, valor, asignacion, grafo):

    # Revisar vecinos de la variable
    for vecino in grafo[variable]:

        # Verificar si algún vecino tiene el mismo valor
        if vecino in asignacion and asignacion[vecino] == valor:
            return False

    return True


# Propagación de restricciones
def propagacion(asignacion, dominios, grafo):

    # Recorrer variables asignadas
    for var in asignacion:

        valor = asignacion[var]

        # Revisar vecinos de la variable
        for vecino in grafo[var]:

            if vecino not in asignacion:

                # Eliminar valor del dominio del vecino
                if valor in dominios[vecino]:
                    dominios[vecino].remove(valor)

                    # Verificar si el dominio queda vacío
                    if len(dominios[vecino]) == 0:
                        return False

    return True


# Backtracking con propagación
def backtracking(asignacion, dominios, grafo):

    # Verificar si todas las variables fueron asignadas
    if len(asignacion) == len(grafo):
        return asignacion

    # Seleccionar variable sin asignar
    for var in grafo:
        if var not in asignacion:
            break

    # Probar valores disponibles
    for valor in dominios[var]:

        # Verificar si el valor es válido
        if es_valido(var, valor, asignacion, grafo):

            # Crear nueva asignación
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[var] = valor

            # Copiar dominios
            nuevos_dominios = {
                v: dominios[v][:]
                for v in dominios
            }

            # Aplicar propagación
            if propagacion(
                nueva_asignacion,
                nuevos_dominios,
                grafo
            ):

                # Llamada recursiva
                resultado = backtracking(
                    nueva_asignacion,
                    nuevos_dominios,
                    grafo
                )

                if resultado:
                    return resultado

    return None


# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

# Crear dominios iniciales
dominios = {
    var: colores[:]
    for var in grafo
}

# Ejecutar backtracking con propagación
resultado = backtracking({}, dominios, grafo)

# Mostrar resultado
print("Resultado:", resultado)