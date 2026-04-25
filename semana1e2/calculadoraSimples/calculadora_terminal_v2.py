#python -m streamlit run calculadora_streamlit.py

print("Calculadora simples em Python")
print("Escolha uma operação: +, -, * ou /")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

print("O primeiro número é maior que o segundo?", numero1 > numero2)
print("O primeiro número é menor que o segundo?", numero1 < numero2)
print("Os dois números são iguais?", numero1 == numero2)