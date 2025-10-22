# SubPrograma

def ordenar(valores):
    # Função Interna: ondeMenor

    def ondeMenor(vals, inicio):
        posMenor = inicio
        for p in range(inicio+1, len(vals)):
            if vals[p] < vals[posMenor]:
                posMenor = p
        return posMenor

    for ind in range(len(valores)-1):
        posicao = ondeMenor(valores, ind)
        temp = valores[ind]
        valores[ind] = valores[posicao]
        valores[posicao] = temp
    return None


# Programa Principal

quant = int(input())
if quant == 0:
    print("Nenhum número foi lido, portanto, sem mínimo e máximo!!")
else:
    lista = []
    for ind in range(quant):
        num = input().split()
        lista.append(num)

    valores = []
    for j in range(len(lista)):
        valores += lista[j]
    ordenar(valores)
    print(valores)
    print("Menor Número: ", valores[0], " e Maior Número: ", valores[-1])
"""
num = input().split()
print(num)
"""