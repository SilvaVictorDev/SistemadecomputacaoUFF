
""" Este é um exemplo de comentário """

"""
valor = float(input("Entre com um valor: "))
if valor > 0:
    print(valor, "è maior do que zero.")
"""
"""
salario = float(input("Diga seu salário atual: "))
if salario > 10000:
    inps = salario * 0.10
    impostoRenda = salario * 0.15
    print("Valor do INPS:", inps, "e do Imposto de Renda:", impostoRenda)
"""
"""
valor = float(input("Entre com um valor:"))
if valor > 0:
    print(valor, "é maior do que zero.")
else:
    print(valor, "é menor ou igual a zero.")
"""

"""
Programa Abono Salarial

salario = float(input("Diga seu salário atual: "))
tempo = int(input("Diga quantos anos completos tem de serviço: "))
if tempo < 1:
    print("Seu salário se mantém o mesmo:", salario)
else:
    if tempo < 10:
        salario = salario * 1.10
    else:
        salario = salario * 1.25
    print("Seu novo salário, com abono:", salario)
"""
"""
Programa Calculadora

valores = input("Entre com dois inteiros positivos: ").split()
x = int(valores[0])     # primeira substring da lista
y = int(valores[1])     # segunda substring da lista
op = input("Informe o operador (+, -, *, / ou **): ")
if op == "+":
    resultado = x + y
elif op == "-":
    resultado = x - y
elif op == "*":
    resultado = x * y
elif op == "/":
    resultado = x / y
elif op == "**":
    resultado = x ** y
else:
    resultado = None
if resultado == None:
    print(op, ": Operador inexistente!!")
else:
    print(x, op, y, "=", resultado)
"""
"""
Laço While
indice = 1
while indice <= 10:
    print(indice, end=" ")
    indice = indice + 1
print()
"""
"""
Cálculo Fatorial usando While
num = int(input("Digite um valor inteiro e positivo: "))
i = 1
fat = 1
while i <= num:
    fat = fat * i
    i = i + 1
print ("O fatorial de", num, "=", fat)
"""
"""
Cálculo Fatorial usando For
num = int(input("Digite valor inteiro e positivo: "))
fat = 1
for i in range(1, num + 1):
    fat = fat * i
print("O fatorial de", num, "=", fat)
"""

