# Un corpus es un conjunto de textos o palabras

texto = [
    "hola",
    "mundo",
    "hola",
    "python",
    "hola"
]


def contar_palabras(texto):

    frecuencias = {}

    # Contamos cuántas veces aparece cada palabra
    for palabra in texto:

        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def calcular_probabilidades(frecuencias):

    probabilidades = {}

    total = sum(frecuencias.values())

    # Calculamos probabilidad de cada palabra
    for palabra, cantidad in frecuencias.items():

        probabilidades[palabra] = cantidad / total

    return probabilidades


frecuencias = contar_palabras(texto)

probabilidades = calcular_probabilidades(frecuencias)

print("Frecuencias:")
print(frecuencias)

print("\nProbabilidades:")
for palabra, prob in probabilidades.items():
    print(palabra, "->", round(prob, 2))