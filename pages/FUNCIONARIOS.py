import streamlit as st
import pandas as pd

st.title("👥 Funcionários")

funcionarios = pd.read_csv("data/funcionarios.csv")

unidade = st.selectbox(
    "Filtrar por unidade",
    ["Todas"] + list(funcionarios["Unidade"].unique())
)

if unidade != "Todas":
    df = funcionarios[funcionarios["Unidade"] == unidade]
else:
    df = funcionarios

st.dataframe(df, use_container_width=True)
