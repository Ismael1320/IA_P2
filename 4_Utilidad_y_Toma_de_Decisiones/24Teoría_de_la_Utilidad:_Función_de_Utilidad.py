# Opciones disponibles con sus valores
opciones = {
    'Opcion_A': 100,
    'Opcion_B': 80,
    'Opcion_C': 50
}

# Función de utilidad
def utilidad(valor):

    # Calcular utilidad usando raíz cuadrada
    return valor ** 0.5


# Evaluar todas las opciones
def evaluar_opciones():

    # Variables para guardar la mejor opción
    mejor = None
    mejor_utilidad = float('-inf')

    # Recorrer opciones disponibles
    for opcion, valor in opciones.items():

        # Calcular utilidad
        u = utilidad(valor)

        # Mostrar resultados
        print(
            f"{opcion} -> Valor: {valor}, "
            f"Utilidad: {u:.2f}"
        )

        # Verificar si es la mejor utilidad
        if u > mejor_utilidad:

            mejor_utilidad = u
            mejor = opcion

    return mejor, mejor_utilidad


# Ejecutar evaluación
mejor, u = evaluar_opciones()

# Mostrar mejor resultado
print("Mejor opción:", mejor)
print("Mayor utilidad:", round(u, 2))