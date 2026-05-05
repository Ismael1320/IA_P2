# Palabras posibles
palabras = ['hola', 'adios']

# Probabilidad de reconocer la señal dada una palabra
P_senal = {
    'hola': 0.8,
    'adios': 0.3
}

# Probabilidad inicial de cada palabra
P_palabra = {
    'hola': 0.6,
    'adios': 0.4
}


def reconocer():

    resultados = {}

    # Calculamos qué tan probable es cada palabra
    for p in palabras:

        # combinamos lo que ya creíamos con lo que observamos
        resultados[p] = P_palabra[p] * P_senal[p]

    # elegimos la palabra más probable
    mejor = max(resultados, key=resultados.get)

    return mejor, resultados


palabra, valores = reconocer()

print("Probabilidades:")
for p, v in valores.items():
    print(p, "->", round(v, 2))

print("\nPalabra reconocida:", palabra)