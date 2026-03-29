import streamlit as st

st.title("Gerenciador de Tarefas")

st.write("Olá. Bem-vinda ao Gerenciador de Tarefas!")
st.write("Escolha uma opção:")

st.write("1 - Adicionar tarefa")
st.write("2 - Listar tarefas")
st.write("3 - Marcar tarefa como concluída")
st.write("4 - Excluir tarefa")
st.write("5 - Sair")

opcao = st.text_input("Digite o número da opção:")

st.write("Você escolheu:", opcao)