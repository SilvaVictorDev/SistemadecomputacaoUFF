# Programa Testador de Intervalos.

# Programa Principal.

qtdTestes = int(input("Digite a quantidade de testes: "))
qtdValores = int(input("Digite a quantidade de valores: "))
intMin = float(input("Digite o intervalo mínimo: "))
intMax = float(input("Digite o intervalo máximo: "))

# Testes

for i in range(0, qtdTestes):
    abaixoInt = 0
    acimaInt = 0
    noInt = 0
    soma = 0
    for ind in range(0, qtdValores):
        valor = float(input("Digite qualquer valor: "))
        if valor < intMin:
            abaixoInt = abaixoInt + 1
        elif valor > intMax:
            acimaInt = acimaInt + 1
        else:
            noInt = noInt + 1
            soma = soma + valor

# Impressão
    print()
    print("Teste", i + 1, ":")
    print("    Intervalo: [" + str(intMin) + ",",  str(intMax) + "]")
    print("    Abaixo do Intervalo: ", str(abaixoInt) + "," " No intervalo: ", str(noInt) + ",", "\n",
          "Acima do Intervalo: ", str(acimaInt) + ".")
    if i == 0:
        print("    Soma dos Valores Dentro do Intervalo: ", soma)
    else:
        print("    Soma de Valores no Intervalo: ", soma)
    print()
