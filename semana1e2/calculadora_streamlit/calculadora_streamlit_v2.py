import streamlit as st

st.title("Calculadora com Streamlit")
st.write("Meu primeiro app em Python")

numero1 = st.number_input("Digite o primeiro número:", value=0.0)
numero2 = st.number_input("Digite o segundo número:", value=0.0)