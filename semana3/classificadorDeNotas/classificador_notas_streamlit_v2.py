import streamlit as st

st.title("Classificador de Notas")

nota = st.slider("Nota do aluno:", 0.0, 10.0, 5.0)

if nota >= 9.0:
    st.write("Conceito A - Aprovado com Excelência")
elif nota >= 7.0:
    st.write("Conceito B - Aprovado")
elif nota >= 5.0:
    st.write("Conceito C - Aprovado")
elif nota >= 3.0:
    st.write("Conceito D - Recuperação")
else:
    st.write("Conceito F - Reprovado")