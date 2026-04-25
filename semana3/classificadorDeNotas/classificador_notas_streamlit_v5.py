import streamlit as st

st.set_page_config(page_title="Classificador de Notas", page_icon="🎓")
st.title("🎓 Classificador de Notas")

nome = st.text_input("Nome do aluno:", placeholder="Ex: Maria Silva")
nota = st.number_input("Nota do aluno:")

st.divider()

if nota < 0 or nota > 10:
    st.error("Nota inválida! Digite um valor entre 0 e 10.")
else:
    if nota >= 9.0:
        conceito, situacao = "A", "Aprovado com Excelência"
        mensagem, tipo = "Desempenho excepcional!", "success"
    elif nota >= 7.0:
        conceito, situacao = "B", "Aprovado"
        mensagem, tipo = "Muito bom! Continue assim.", "success"
    elif nota >= 5.0:
        conceito, situacao = "C", "Aprovado"
        mensagem, tipo = "Passou! Mas pode melhorar.", "info"
    elif nota >= 3.0:
        conceito, situacao = "D", "Recuperação"
        mensagem, tipo = "Atenção! Você precisa de recuperação.", "warning"
    else:
        conceito, situacao = "F", "Reprovado"
        mensagem, tipo = "Não desista, tente novamente!", "error"

    if nome:
        st.markdown(f"### Resultado de **{nome}**")

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
