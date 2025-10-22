# Programa Caixa Eletrônico
# Programa Principal        
valor = int(input("Digite o valor a ser sacado: "))
nota200 = (valor // 200)
nota100 = (valor % 200) // 100
nota50 = (valor % 100) // 50
nota20 = (valor % 50) // 20
nota10 = ((valor % 50) % 20) // 10
nota5 = (valor % 10) // 5
nota2 = (valor %5) // 2
moeda1 = ((valor % 5) % 2) // 1
print("Notas de 200: ", nota200)
print("Notas de 100: ", nota100)
print("Notas de 50", nota50)
print("Notas de 20", nota20)
print("Notas de 10", nota10)
print("Notas de 5", nota5)
print("Notas de 2", nota2)
print("Moeda de 1", moeda1)
