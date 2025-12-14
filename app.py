import streamlit as st
import pandas as pd

# ===========================
# CONFIGURAÇÕES DO LAYOUT
# ===========================
st.set_page_config(page_title="Sistema de RH", layout="wide")

# CSS para estilizar como na imagem
st.markdown("""
    <style>
        .main { background-color: #F5F5F5; }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #E0E0E0;
            text-align: center;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        .card h2 {
            font-size: 42px;
            margin: 0;
            font-weight: 600;
            color: #333;
        }
        .card-title {
            font-size: 16px;
            color: #555;
            margin-bottom: 8px;
            font-weight: 500;
        }
        .alert-box {
            background-color: #FFF3F3;
            border-left: 5px solid #E53935;
            padding: 15px;
            border-radius: 8px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)


# ===========================
# CARREGAMENTO DE DADOS
# ===========================
@st.cache_data
def load_data():
    funcionarios = pd.read_csv("data/funcionarios.csv")
    eventos = pd.read_csv("data/eventos.csv")
    return funcionarios, eventos


funcionarios, eventos = load_data()

faltas_dia = eventos[eventos["Tipo_evento"] == "Falta"].shape[0]
func_por_unidade = funcionarios.groupby("Unidade")["Id_funcionario"].count()
custo_mes = 10000  # Exemplo fixo, você pode integrar depois

# ===========================
# MENU LATERAL
# ===========================
st.sidebar.title("Menu")
st.sidebar.markdown("✔ Registro de presença")
st.sidebar.markdown("👤 Cadastro de funcionário")
st.sidebar.markdown("💲 Financeiro")
st.sidebar.markdown("📊 Relatórios")
st.sidebar.markdown("---")
st.sidebar.markdown("🚪 Sair")


# ===========================
# TÍTULO
# ===========================
st.markdown("<h1 style='text-align:center;'>Sistema de RH</h1>", unsafe_allow_html=True)


# ===========================
# CARDS SUPERIORES
# ===========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'><div class='card-title'>Faltas do dia</div><h2>{}</h2></div>".format(faltas_dia), unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><div class='card-title'>Funcionários por unidade</div>".format(), unsafe_allow_html=True)
    for unidade, qtd in func_por_unidade.items():
        st.markdown(f"<p><b>{unidade}:</b> {qtd}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'><div class='card-title'>Custos do mês</div><h2>R${:,.0f}</h2></div>".format(custo_mes), unsafe_allow_html=True)

with col4:
    st.markdown("<div class='card'><div class='card-title'>Alertas</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='alert-box'>⚠️ Faltas acima da média</div>", unsafe_allow_html=True)


# ===========================
# PAINEL GERAL
# ===========================
st.subheader("Painel Geral")
st.dataframe(funcionarios)
