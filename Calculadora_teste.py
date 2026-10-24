# Calculadora Básica em Python
print("=== CALCULADORA BÁSICA ===")

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("\nDigite o número da operação: ")

# Processamento e resultado
if opcao == "1":
    resultado = num1 + num2
    operacao = "+"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "-"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "*"
elif opcao == "4":
    if num2 == 0:
        print("Erro: não é possível dividir por zero!")
        exit()
    resultado = num1 / num2
    operacao = "/"
else:
    print("Opção inválida!")
    exit()

# Exibir resultado
print(f"\n✅ Resultado: {num1} {operacao} {num2} = {resultado}")