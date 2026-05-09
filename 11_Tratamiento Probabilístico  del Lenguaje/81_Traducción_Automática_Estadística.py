# Diccionario con posibles traducciones, cada palabra tiene una probabilidad
traducciones = {

    'house': {
        'casa': 0.8,
        'hogar': 0.2
    },

    'car': {
        'auto': 0.7,
        'coche': 0.3
    },

    'book': {
        'libro': 0.9,
        'cuaderno': 0.1
    }
}


def traducir(palabra):

    # Revisamos si la palabra existe
    if palabra not in traducciones:
        return "No encontrada"

    opciones = traducciones[palabra]

    mejor_traduccion = ""
    mayor_probabilidad = 0

    # Buscamos la traducción con mayor probabilidad
    for traduccion, probabilidad in opciones.items():

        if probabilidad > mayor_probabilidad:

            mayor_probabilidad = probabilidad
            mejor_traduccion = traduccion

    return mejor_traduccion, mayor_probabilidad


palabra = "house"

resultado, prob = traducir(palabra)

print("Palabra original:", palabra)

print("Traducción elegida:", resultado)

print("Probabilidad:", prob)