nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 9.0:
    conceito = "A"
    situacao = "Aprovado com Excelência"
    mensagem = "Desempenho excepcional!"
elif nota >= 7.0:
    conceito = "B"
    situacao = "Aprovado"
    mensagem = "Muito bom! Continue assim."
elif nota >= 5.0:
    conceito = "C"
    situacao = "Aprovado"
    mensagem = "Passou! Mas pode melhorar."
elif nota >= 3.0:
    conceito = "D"
    situacao = "Recuperação"
    mensagem = "Atenção! Você precisa de recuperação."
else:
    conceito = "F"
    situacao = "Reprovado"
    mensagem = "Não desista, tente novamente!"

print(f"\nAluno: {nome}")
print(f"Nota: {nota}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")
print(f"Mensagem: {mensagem}")