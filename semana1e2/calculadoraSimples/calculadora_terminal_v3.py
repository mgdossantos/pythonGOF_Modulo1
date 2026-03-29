print("Calculadora simples em Python")
print("Escolha uma operação: +, -, * ou /")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada: ")

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    resultado = numero1 / numero2

else:
    resultado = "Operação inválida"

print("Resultado:", resultado)

print("O primeiro número é maior que o segundo?", numero1 > numero2)
print("O primeiro número é menor que o segundo?", numero1 < numero2)
print("Os dois números são iguais?", numero1 == numero2)