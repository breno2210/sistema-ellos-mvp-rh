import streamlit as st
import pandas as pd

# ===========================
# CONFIGURAÇÃO DA PÁGINA
# ===========================
st.set_page_config(page_title="Sistema Ellos - RH", layout="wide")

# ===========================
# CARREGAR DADOS
# ===========================
@st.cache_data
def load_data():
    funcionarios = pd.read_csv("data/funcionarios.csv")
    eventos = pd.read_csv("data/eventos.csv")
    financeiro = pd.read_csv("data/financeiro.csv")
    return funcionarios, eventos, financeiro

funcionarios, eventos, financeiro = load_data()

# ===========================
# MENU LATERAL (FUNCIONAL)
# ===========================
menu = st.sidebar.radio(
    "Menu",
    [
        "📊 Dashboard",
        "👥 Funcionários",
        "💰 Financeiro",
        "📄 Relatórios"
    ]
)
st.write("MENU ATUAL:", menu)

st.sidebar.markdown("---")
st.sidebar.markdown("Sistema MVP • Ellos")

# ===========================
# DASHBOARD
# ===========================
if menu == "📊 Dashboard":
    st.success("Você está no DASHBOARD")
    st.title("📊 Dashboard Geral")

    total_func = funcionarios.shape[0]
    total_ativos = funcionarios[funcionarios["Status"] == "Ativo"].shape[0]
    total_faltas = eventos[eventos["Tipo_evento"] == "Falta"].shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Funcionários", total_func)
    col2.metric("Ativos", total_ativos)
    col3.metric("Faltas", total_faltas)

    st.subheader("Funcionários por Unidade")
    por_unidade = funcionarios.groupby("Unidade")["Id_funcionario"].count()
    st.bar_chart(por_unidade)

# ===========================
# FUNCIONÁRIOS
# ===========================
elif menu == "👥 Funcionários":
    st.warning("Você está na TELA DE FUNCIONÁRIOS")
    st.title("👥 Funcionários")

    unidade = st.selectbox(
        "Filtrar por unidade",
        ["Todas"] + list(funcionarios["Unidade"].unique())
    )

    if unidade != "Todas":
        df = funcionarios[funcionarios["Unidade"] == unidade]
    else:
        df = funcionarios

    st.dataframe(df, use_container_width=True)

# ===========================
# FINANCEIRO
# ===========================
elif menu == "💰 Financeiro":
    st.info("Você está no MÓDULO FINANCEIRO")
    st.title("💰 Financeiro")

    st.subheader("Custos por Unidade")
    st.dataframe(financeiro, use_container_width=True)

    st.subheader("Custo Total")
    st.metric("Total Geral", f"R$ {financeiro['Custo_total'].sum():,.2f}")

# ===========================
# RELATÓRIOS
# ===========================
elif menu == "📄 Relatórios":
    st.error("Você está em RELATÓRIOS")
    st.title("📄 Relatórios")


    st.info("Módulo em desenvolvimento")
    st.write("Aqui entrarão relatórios consolidados de RH e Financeiro.")

