import streamlit as st

st.title("Classificador de Notas")

nome = st.text_input("Nome do aluno:")
nota = st.slider("Nota do aluno:", 0.0, 10.0, 5.0)

if nota >= 9.0:
    conceito = "A"
    situacao = "Aprovado com Excelência"
elif nota >= 7.0:
    conceito = "B"
    situacao = "Aprovado"
elif nota >= 5.0:
    conceito = "C"
    situacao = "Aprovado"
elif nota >= 3.0:
    conceito = "D"
    situacao = "Recuperação"
else:
    conceito = "F"
    situacao = "Reprovado"

st.write(f"Aluno: {nome}")
st.write(f"Nota: {nota}")
st.write(f"Conceito: {conceito}")
st.write(f"Situação: {situacao}")