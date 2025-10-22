"""Tipos Mutáveis e Imutáveis como Parâmetro"""
"""
# Programa Completo
# Subprograma


def trocar(valores, pos1, pos2):        # se possível, modifica o conteúdo de duas células
    if 0 <= pos1 < len(valores) and 0 <= pos2 < len(valores):
        temp = valores[pos1]
        valores[pos1] = valores[pos2]
        valores[pos2] = temp
    return None

# Programa Principal


amigas = ["Maria", "Regina", "Eliana", "Angelica"]   # vetor com 4 ‘strings’ — próximas aulas
trocar(amigas, 3, 1)
print(amigas)
"""
"""Funções como Parâmetro"""
"""
# Programa Completo

# Subprograma


def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def fib(num):
    if 1 <= num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def soma(f, n):         # Esta função soma os 'n' primeiros valores de uma dada função 'f'
    parcial = 0
    for ind in range(1, n+1):
        parcial = parcial + f(ind)
    return parcial


# Programa Principal
total = soma(fatorial, 10) + soma(fib, 10)
print(total)
"""
# Programa Completo Recursividade Mútua

#Subprograma
def flip(n):
    print("Flip")
    if n > 0:
        flop(n-1)


def flop(n):
    print("Flop")
    if n > 0:
        flip(n-1)


# Programa Principal
flip(5)