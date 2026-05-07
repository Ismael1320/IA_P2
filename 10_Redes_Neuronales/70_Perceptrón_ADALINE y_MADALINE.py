entradas = [1, 2]

pesos = [0.5, 0.3]

sesgo = 1


# ---------Perceptrón-------------
# Solo decide entre 0 y 1
def perceptron(entradas, pesos, sesgo):

    suma = 0

    for i in range(len(entradas)):
        suma += entradas[i] * pesos[i]

    suma += sesgo

    if suma >= 0:
        return 1
    else:
        return 0


# -------------ADALINE--------
# Devuelve el valor directo de la suma
def adaline(entradas, pesos, sesgo):

    suma = 0

    for i in range(len(entradas)):
        suma += entradas[i] * pesos[i]

    suma += sesgo

    return suma


#-------------MADALINE----------------
# Usa varias salidas tipo ADALINE
def madaline():

    salida1 = adaline(entradas, pesos, sesgo)
    salida2 = adaline(entradas, [0.2, 0.4], 0.5)

    # Promediamos ambas salidas
    return (salida1 + salida2) / 2


print("Perceptrón:", perceptron(entradas, pesos, sesgo))
print("ADALINE:", round(adaline(entradas, pesos, sesgo), 2))
print("MADALINE:", round(madaline(), 2))