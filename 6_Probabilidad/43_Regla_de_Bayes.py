# Probabilidades conocidas
P_A = 0.3        # probabilidad de que haya falla
P_B_dado_A = 0.9 # probabilidad de que suene la alarma si hay falla
P_B = 0.5        # probabilidad total de que suene la alarma


def bayes(P_A, P_B_dado_A, P_B):

    # Aplicamos la fórmula de Bayes:
    # P(A | B) = (P(B | A) * P(A)) / P(B)
    resultado = (P_B_dado_A * P_A) / P_B

    return resultado


print("P(A):", P_A)
print("P(B | A):", P_B_dado_A)
print("P(B):", P_B)

# Calculamos la probabilidad de falla dado que sonó la alarma
resultado = bayes(P_A, P_B_dado_A, P_B)
print("\nP(A | B):", round(resultado, 2))