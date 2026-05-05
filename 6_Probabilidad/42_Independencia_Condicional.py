# Probabilidades dadas
P_A_dado_C = 0.6   # probabilidad de A dado C
P_B_dado_C = 0.5   # probabilidad de B dado C
P_AyB_dado_C = 0.3 # probabilidad de A y B al mismo tiempo dado C


def verificar_independencia(P_A_C, P_B_C, P_AyB_C):

    # Si son independientes dado C, esto debe cumplirse:
    # P(A y B | C) = P(A | C) * P(B | C)
    producto = P_A_C * P_B_C

    print("P(A y B | C):", P_AyB_C)
    print("P(A | C) * P(B | C):", producto)

    # Comparamos usando un margen pequeño por decimales
    if abs(P_AyB_C - producto) < 0.0001:
        return True
    else:
        return False




resultado = verificar_independencia(
    P_A_dado_C,
    P_B_dado_C,
    P_AyB_dado_C
)

# Mostramos el resultado final
if resultado:
    print("\nSí son independientes dado C")
else:
    print("\nNo son independientes dado C")