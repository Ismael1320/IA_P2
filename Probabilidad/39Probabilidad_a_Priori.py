# Datos iniciales (frecuencias)
# Número de días observados en el pasado
datos = {
    'Soleado': 6,
    'Nublado': 3,
    'Lluvioso': 1
}

# Función para calcular probabilidades a priori
def calcular_priori(datos):

    # Calculamos el total de observaciones
    total = sum(datos.values())

    # Diccionario donde guardaremos probabilidades
    probabilidades = {}

    # Recorremos cada tipo de clima
    for estado in datos:

        # Probabilidad a priori = frecuencia / total
        probabilidades[estado] = datos[estado] / total

    return probabilidades


print("Datos observados:", datos)

priori = calcular_priori(datos)

print("\nProbabilidades a priori:\n")

# Mostrar resultados
for estado, prob in priori.items():
    print(estado, "->", round(prob, 2))