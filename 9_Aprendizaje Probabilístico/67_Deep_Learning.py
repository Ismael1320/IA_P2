entrada = 5

#Qué tan importante es la entrada
peso = 0.8


sesgo = 1


def neurona(x):

    # Paso 1: combinación lineal
    z = x * peso + sesgo

    # Paso 2: función de activación
    if z > 0:
        return z
    else:
        return 0


salida = neurona(entrada)

print("Salida de la neurona:", salida)