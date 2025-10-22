# SubPrograma

def ler():
    linha = input("Digite os Valores do Vetor, separados por espaços:\n")
    partes = linha.split()
    for ind in range(len(partes)):
        dinheiro[partes[ind]] = float(partes[ind])
    return dinheiro


# ProgramaPrincipal
dinheiro = ler()
print(dinheiro)
