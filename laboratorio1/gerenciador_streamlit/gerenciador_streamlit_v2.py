import streamlit as st

st.title("Gerenciador de Tarefas")

st.write("Este é o menu inicial do projeto.")

opcao = st.selectbox(
    "Escolha uma opção:",
    [
        "Adicionar tarefa",
        "Listar tarefas",
        "Marcar tarefa como concluída",
        "Excluir tarefa",
        "Sair"
    ]
)

if opcao is not None:
    st.write("Você escolheu:", opcao)