def adicao(num1, num2):
	return num1 + num2

def subtracao(num1, num2):
	return num1 - num2

def multiplicacao(num1, num2):
	return num1 * num2

def divisao(num1, num2):
	return num1 / num2

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("\nDigite sua opção (1/2/3/4): "))
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if opcao == 1:
	print("\n", num1, "+", num2, "=", adicao(num1, num2))
elif opcao == 2:
	print("\n", num1, "-", num2, "=", subtracao(num1, num2))
elif opcao == 3:
	print("\n", num1, "*", num2, "=", multiplicacao(num1, num2))
elif opcao == 4:
	print("\n", num1, "/", num2, "=", divisao(num1, num2))
else:
	print("\nOpção Inválida!")
