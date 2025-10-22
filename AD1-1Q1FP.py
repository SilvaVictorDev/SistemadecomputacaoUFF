# Programa Trocador de Dinheiro

# Programa Principal

valor = 0
while valor != "":
    valor = (input("Digite o valor a ser Trocado em R$: ")).replace(" ", "")

# Define a quantidade de cada nota e moeda.

    if valor != "":
        nota100 = int(valor) // 100
        nota50 = (int(valor) % 100) // 50
        nota20 = (int(valor) % 50) // 20
        nota10 = ((int(valor) % 50) % 20) // 10
        nota5 = (int(valor) % 10) // 5
        nota2 = (int(valor) % 5) // 2
        moeda1 = ((int(valor) % 5) % 2) // 1
        print()
        print("Trocando", valor, "em: ")

# Imprimi a quantidade de cada nota e moeda

        if nota100 > 0:
            if nota100 == 1:
                print("  ", nota100, "nota de 100 reais")
            else:
                print("  ", nota100, "notas de 100 reais")
        if nota50 > 0:
            if nota50 == 1:
                print("  ", nota50, "nota de 50 reais")
            else:
                print("  ", nota50, "notas de 50 reais")
        if nota20 > 0:
            if nota20 == 1:
                print("  ", nota20, "nota de 20 reais")
            else:
                print("  ", nota20, "notas de 20 reais")
        if nota10 > 0:
            if nota10 == 1:
                print("  ", nota10, "nota de 10 reais")
            else:
                print("  ", nota10, "notas de 10 reais")
        if nota5 > 0:
            if nota5 == 1:
                print("  ", nota5, "nota de 5 reais")
            else:
                print("  ", nota5, "notas de 5 reais")
        if nota2 > 0:
            if nota2 == 1:
                print("  ", nota2, "nota de 2 reais")
            else:
                print("  ", nota2, "notas de 2 reais")
        if moeda1 > 0:
            if moeda1 == 1:
                print("  ", moeda1, "moeda de 1 real")
            else:
                print("  ", moeda1, "moedas de 1 real")
        print()
