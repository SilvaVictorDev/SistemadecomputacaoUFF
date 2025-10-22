# Subprogramas
def escrever(valores):
    for item in valores:
        print(item, end=" ")
    print()
    return None


def ler(valores):
    for ind in range(len(valores)):
        valores[ind] = float(input("vs["+str(ind+1)+"] = "))
    return None


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

# Programa Principal - exemplo
TAM = 10
numeros = [0.0]*TAM
ler(numeros)
escrever(numeros)
ordenar(numeros)
escrever(numeros)