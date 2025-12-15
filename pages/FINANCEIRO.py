import streamlit as st
import pandas as pd

st.title("💰 Financeiro")

financeiro = pd.read_csv("data/financeiro.csv")

st.subheader("Custos por Unidade")
st.dataframe(financeiro, use_container_width=True)

st.metric(
    "Custo Total Geral",
    f"R$ {financeiro['Custo_total'].sum():,.2f}"
)
