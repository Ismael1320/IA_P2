prob_clima = {
    'soleado': 0.7,
    'lluvia': 0.3
}


utilidad = {
    ('llevar_paraguas', 'soleado'): 5,
    ('llevar_paraguas', 'lluvia'): 8,
    ('no_paraguas', 'soleado'): 10,
    ('no_paraguas', 'lluvia'): 0
}

decisiones = ['llevar_paraguas', 'no_paraguas']

def utilidad_esperada(decision):
    total = 0
    for clima in prob_clima:
        total += prob_clima[clima] * utilidad[(decision, clima)]
    return total


def mejor_decision():
    mejor = None
    mejor_valor = float('-inf')

    for decision in decisiones:
        valor = utilidad_esperada(decision)
        print(f"Decisión: {decision} -> Utilidad esperada: {valor}")

        if valor > mejor_valor:
            mejor_valor = valor
            mejor = decision

    return mejor, mejor_valor



mejor, valor = mejor_decision()

print("\nMejor decisión:", mejor)
print("Utilidad esperada:", valor)