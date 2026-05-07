x = 2

# Primera capa
peso1 = 0.5
sesgo1 = 1

# Segunda capa
peso2 = 0.8
sesgo2 = 0.5


# Función de activación simple
def relu(valor):

    if valor > 0:
        return valor
    else:
        return 0


# Primera neurona
def capa1(x):

    salida = x * peso1 + sesgo1

    return relu(salida)


# Segunda neurona
def capa2(entrada):

    salida = entrada * peso2 + sesgo2

    return relu(salida)


# La salida de una capa entra a la siguiente
salida1 = capa1(x)
salida_final = capa2(salida1)
print("Salida capa 1:", round(salida1, 2))
print("Salida final:", round(salida_final, 2))