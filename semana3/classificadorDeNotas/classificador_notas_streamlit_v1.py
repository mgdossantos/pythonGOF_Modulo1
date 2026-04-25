import streamlit as st

st.title("Classificador de Notas")

nota = st.number_input("Digite a nota:", min_value=0.0, max_value=10.0)

if nota >= 5.0:
    st.write("Aprovado")
else:
    st.write("Reprovado")