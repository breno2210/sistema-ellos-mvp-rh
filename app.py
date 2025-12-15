import streamlit as st

st.set_page_config(
    page_title="Sistema Ellos - RH",
    layout="wide"
)

# MENU LATERAL
st.sidebar.title("Sistema Ellos")
st.sidebar.caption("RH • Financeiro • Relatórios")

# CONTEÚDO PRINCIPAL (HTML PURO)
st.markdown(
    """
    <div style="max-width:900px; margin-top:40px;">

        <h1 style="color:#1E8E5A; font-size:48px; margin-bottom:10px;">
            🏢 Sistema Ellos
        </h1>

        <h3 style="color:#1E8E5A; font-weight:500;">
            MVP de RH com integração Financeira
        </h3>

        <p style="font-size:18px; color:#374151; margin-top:30px;">
            Plataforma desenvolvida para apoiar a gestão de pessoas,
            oferecendo indicadores operacionais, controle financeiro
            e base para tomada de decisão estratégica.
        </p>

        <p style="font-size:17px; color:#374151; margin-top:30px;">
            Use o menu lateral para navegar entre os módulos:
        </p>

        <ul style="font-size:17px; color:#1E8E5A;">
            <li><strong>Painel</strong> – visão geral e indicadores</li>
            <li><strong>Funcionários</strong> – gestão e filtros</li>
            <li><strong>Financeiro</strong> – custos e consolidação</li>
            <li><strong>Relatórios</strong> – análises gerenciais</li>
        </ul>

    </div>
    """,
    unsafe_allow_html=True
)
