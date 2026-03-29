import streamlit as st

st.title("Calculadora com Streamlit")
st.write("Meu primeiro app em Python")

numero1 = st.number_input("Digite o primeiro número:", value=0.0)
numero2 = st.number_input("Digite o segundo número:", value=0.0)

operacao = st.selectbox(
    "Escolha a operação:",
    ["+", "-", "*", "/"]
)


st.subheader("Comparação entre os números")
st.write("O primeiro número é maior que o segundo?", numero1 > numero2)
st.write("O primeiro número é menor que o segundo?", numero1 < numero2)
st.write("Os dois números são iguais?", numero1 == numero2)
