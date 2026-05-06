entradas = [2, 3]

#Importancia de cada entrada
pesos = [0.5, 0.8]

sesgo = 1


def neurona(entradas, pesos, sesgo):

    suma = 0

    # Multiplicamos cada entrada por su peso
    for i in range(len(entradas)):
        suma += entradas[i] * pesos[i]

    # Sumamos el sesgo
    suma += sesgo

    # Activación simple
    if suma > 0:
        return suma
    else:
        return 0


resultado = neurona(entradas, pesos, sesgo)
print("Salida de la neurona:", resultado)