import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Vendas")
st.caption("Análise geral de desempenho")

try:
    df = pd.read_csv("vendas.csv")
except FileNotFoundError:
    st.error("Arquivo vendas.csv não encontrado.")
    st.stop()

st.sidebar.header("Filtros")
opcoes = ["Todos"] + list(df["Produto"].unique())
produto_selecionado = st.sidebar.selectbox("Produto", opcoes)

if produto_selecionado == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["Produto"] == produto_selecionado]

total_vendas = df_filtrado["Valor Total"].sum()
total_itens = df_filtrado["Quantidade"].sum()
ticket_medio = total_vendas / total_itens

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento Total", f"R$ {total_vendas:,.2f}")
col2.metric("Itens Vendidos", total_itens)
col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

st.subheader("Análises")
fig_bar = px.bar(df_filtrado, x="Produto", y="Valor Total", title="Faturamento")
fig_qtd = px.bar(df_filtrado, x="Produto", y="Quantidade", title="Quantidade Vendida")

col_g1, col_g2 = st.columns(2)
with col_g1:
    st.plotly_chart(fig_bar, width="stretch")
with col_g2:
    st.plotly_chart(fig_qtd, width="stretch")

st.subheader("Detalhamento dos Dados")
st.dataframe(df_filtrado)
