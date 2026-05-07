import streamlit as st
import pandas as pd
from ag import AG
# import os

#os.system('cls')   <-- Pesquisei e nao funciona no deploy

st.set_page_config(page_title="Algoritmo Genético", layout="centered")
st.title("🧬 Algoritmo Genético")
st.subheader("Cálculo de roteamento de cidades")

# Substituindo os input do main com terminal com o streamlit:
tamanho_populacao = st.number_input("Tamanho da população", min_value=2, value=20)
taxa_selecao = st.slider("Taxa de seleção (%)", 20, 40, 30)
taxa_mutacao = st.slider("Taxa de mutação (%)", 5, 10, 7)
qtd_geracoes = st.number_input("Quantidade de gerações", min_value=1, value=10)

# Dentro desse if garante que só vai rodar se clicarem no botão Iniciar:
if st.button("▶️ Iniciar"):
    estado_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    taxa_reproducao = 100 - taxa_selecao
    populacao = []
    nova_populacao = []

    AG.gerar_populacao(populacao, tamanho_populacao, estado_final)
    populacao.sort()

    # Barra de progresso:
    progress = st.progress(0)
    container = st.container()  # Como se fosse a <div> do html, pra não aparecer o a barra de progresso a cada geração

    def exibir_geracao(num, pop):
        """
        Exibe uma geração como tabela no Streamlit.
        Converte a lista de cromossomos em um DataFrame do pandas
        para aproveitar a exibição interativa do st.dataframe().
        """

        container.subheader(f"Geração {num}")
        dados = []

        for indv in pop:
            dados.append({"Rota": str(indv.valor), "Aptidão": indv.aptidao})

        df = pd.DataFrame(dados)
        df.index = range(1, len(df) + 1)    # pra começar direto do 1, sem o 0 padrão do pandas

        container.dataframe(df, use_container_width=True)

    exibir_geracao(1, populacao)
    progress.progress(1 / qtd_geracoes)

    # Mesma lógica do main.py -----> seleção, reprodução, mutação e substituição
    for i in range(1, qtd_geracoes):
        AG.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
        AG.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)

        if i % (len(populacao) / taxa_mutacao) == 0:
            AG.mutar(nova_populacao, estado_final)

        populacao = nova_populacao.copy()
        nova_populacao.clear()
        populacao.sort()

        progress.progress((i + 1) / qtd_geracoes)
        exibir_geracao(i + 1, populacao)

    st.success("Evolução concluída!")