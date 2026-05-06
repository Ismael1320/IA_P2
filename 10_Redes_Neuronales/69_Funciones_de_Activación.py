def relu(x):
    # Si es positivo, lo deja igual; si no, lo vuelve 0
    return max(0, x)


def sigmoide(x):
    # Convierte cualquier valor a un rango entre 0 y 1
    return 1 / (1 + (2.71828 ** -x))


def escalon(x):
    # Devuelve 1 si es positivo, si no 0
    if x >= 0:
        return 1
    else:
        return 0


# Probamos con un valor
x = -2

print("ReLU:", relu(x))
print("Sigmoide:", round(sigmoide(x), 3))
print("Escalón:", escalon(x))