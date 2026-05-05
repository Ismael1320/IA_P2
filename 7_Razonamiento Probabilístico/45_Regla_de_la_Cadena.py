# Probabilidades simples para tres eventos
P_A = 0.7                 # probabilidad de que el sistema esté activo
P_B_dado_A = 0.6         # probabilidad de detección si el sistema está activo
P_C_dado_AyB = 0.8       # probabilidad de alerta si ya ocurrió lo anterior


def regla_cadena(P_A, P_B_A, P_C_AB):

    # Aplicamos la regla de la cadena:
    resultado = P_A * P_B_A * P_C_AB

    return resultado


# Calculamos la probabilidad conjunta de todo el proceso
resultado = regla_cadena(P_A, P_B_dado_A, P_C_dado_AyB)

print("Probabilidad conjunta:", round(resultado, 3))