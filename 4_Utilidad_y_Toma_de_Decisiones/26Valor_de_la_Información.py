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


def utilidad_esperada():
    mejor = float('-inf')

    for decision in decisiones:
        total = 0
        for clima in prob_clima:
            total += prob_clima[clima] * utilidad[(decision, clima)]

        print(f"{decision} -> EU: {total}")

        if total > mejor:
            mejor = total

    return mejor


def utilidad_con_informacion():
    total = 0

    for clima in prob_clima:
        mejor = float('-inf')

        for decision in decisiones:
            u = utilidad[(decision, clima)]
            if u > mejor:
                mejor = u

        total += prob_clima[clima] * mejor

    return total


print("Sin información:")
eu_sin = utilidad_esperada()

print("\nCon información perfecta:")
eu_con = utilidad_con_informacion()

voi = eu_con - eu_sin

print("\nEU sin información:", eu_sin)
print("EU con información:", eu_con)
print("Valor de la información:", round(voi, 2))