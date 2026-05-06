# Probabilidades iniciales
P_clase = {
    'Spam': 0.5,
    'No_Spam': 0.5
}

# Probabilidad de palabras dado cada clase
P_palabras = {
    'Spam': {
        'oferta': 0.8,
        'gratis': 0.7
    },
    'No_Spam': {
        'oferta': 0.2,
        'gratis': 0.1
    }
}

# Correo a analizar
correo = ['oferta', 'gratis']


def naive_bayes():

    resultados = {}

    for clase in P_clase:

        # empezamos con la probabilidad base
        prob = P_clase[clase]

        # multiplicamos por cada palabra
        for palabra in correo:
            prob *= P_palabras[clase][palabra]

        resultados[clase] = prob

    # elegimos la clase más probable
    mejor = max(resultados, key=resultados.get)

    return mejor, resultados


clase, valores = naive_bayes()

print("Probabilidades:")
for c, v in valores.items():
    print(c, "->", round(v, 4))

print("\nClasificación:", clase)