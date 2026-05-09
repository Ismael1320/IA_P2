# Texto de ejemplo
texto = """
Jesus estudia inteligencia artificial.
Ismael trabaja con redes neuronales.
Gonzalo aprende Python.
"""


def extraer_nombres(texto):

    nombres = []

    # Dividimos el texto en palabras
    palabras = texto.split()

    # Revisamos cada palabra
    for palabra in palabras:

        # Si empieza con mayúscula, la tomamos como posible nombre
        if palabra[0].isupper():

            # Quitamos puntos o saltos de línea
            limpio = palabra.replace(".", "")

            nombres.append(limpio)

    return nombres


resultado = extraer_nombres(texto)

print("Nombres encontrados:\n")

for nombre in resultado:
    print("-", nombre)