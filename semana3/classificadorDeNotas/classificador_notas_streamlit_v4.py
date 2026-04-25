import streamlit as st

st.title("🎓 Classificador de Notas")

nome = st.text_input("Nome do aluno:")
nota = st.slider("Nota do aluno:", 0.0, 10.0, 5.0)

st.divider()

if nota >= 9.0:
    conceito = "A"
    situacao = "Aprovado com Excelência"
    mensagem = "Desempenho excepcional!"
    tipo = "success"
elif nota >= 7.0:
    conceito = "B"
    situacao = "Aprovado"
    mensagem = "Muito bom! Continue assim."
    tipo = "success"
elif nota >= 5.0:
    conceito = "C"
    situacao = "Aprovado"
    mensagem = "Passou! Mas pode melhorar."
    tipo = "info"
elif nota >= 3.0:
    conceito = "D"
    situacao = "Recuperação"
    mensagem = "Atenção! Você precisa de recuperação."
    tipo = "warning"
else:
    conceito = "F"
    situacao = "Reprovado"
    mensagem = "Não desista, tente novamente!"
    tipo = "error"

col1, col2 = st.columns(2)
col1.metric("Nota", f"{nota:.1f}")
col2.metric("Conceito", conceito)
st.metric("Situação", situacao)  # situação ocupa a linha inteira

if tipo == "success":
    st.success(mensagem)
elif tipo == "info":
    st.info(mensagem)
elif tipo == "warning":
    st.warning(mensagem)
else:
    st.error(mensagem)