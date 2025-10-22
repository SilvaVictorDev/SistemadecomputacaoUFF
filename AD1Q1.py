# Programa Soma e Média

i = 0
num = []
soma = 0
media = 0
while i != 30:
    entrada = input()
    if entrada == "":
        i = 30
    else:
        num.append(float(entrada))
        i = i + 1
if entrada == "" and len(num) < 1:
    print("Nenhuma linha lida com conteúdo, portanto não há soma nem média!")
elif entrada == "" and len(num) >= 1:
    for j in range(len(num)):
        soma = soma + num[j]
    media = soma / len(num)
    print("Soma dos Números: " "%4.2f" % soma)
    print("Média dos Números: " "%4.2f" % media)
