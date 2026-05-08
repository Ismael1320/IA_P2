x = 2

# Peso inicial
peso = 0.5

# Resultado esperado
esperado = 4

# Tasa de aprendizaje
aprendizaje = 0.1


def calcular_salida(x, peso):

    # Salida de la neurona
    return x * peso



# Calculamos salida actual
salida = calcular_salida(x, peso)

print("Salida inicial:", salida)

# Calculamos error
error = esperado - salida

print("Error:", error)

# Ajustamos el peso para reducir el error
peso = peso + aprendizaje * error

# Nueva salida después del ajuste
nueva_salida = calcular_salida(x, peso)

print("Nuevo peso:", round(peso, 2))

print("Nueva salida:", round(nueva_salida, 2))