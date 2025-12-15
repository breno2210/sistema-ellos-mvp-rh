import streamlit as st

# =====================================
# CONFIGURAÇÃO GLOBAL
# =====================================
st.set_page_config(
    page_title="Sistema RH Ellos",
    layout="wide"
)

# =====================================
# ESTILO EXTRA (ajuste fino)
# =====================================
st.markdown("""
<style>
.hero {
    padding: 60px 20px 40px 20px;
}
.hero-title {
    font-size: 56px;
    font-weight: 700;
    color: #1B1B1B;
    margin-bottom: 10px;
}
.hero-subtitle {
    font-size: 24px;
    color: #2E7D32;
    margin-bottom: 30px;
}
.hero-text {
    font-size: 18px;
    color: #4F4F4F;
    line-height: 1.6;
}
.card {
    background-color: #F5F7F6;
    padding: 24px;
    border-radius: 12px;
    border-left: 6px solid #2E7D32;
}
.card h4 {
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# HERO / APRESENTAÇÃO
# =====================================
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class="hero">
        <div class="hero-title">🏢 Sistema Ellos</div>
        <div class="hero-subtitle">MVP de RH com integração Financeira</div>

        <p class="hero-text">
            Plataforma desenvolvida para apoiar a gestão de pessoas,
            oferecendo indicadores operacionais, controle financeiro
            e base para tomada de decisão estratégica.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>📌 Módulos disponíveis</h4>
        <ul>
            <li><strong>Dashboard</strong> – visão geral e indicadores</li>
            <li><strong>Funcionários</strong> – dados cadastrais e filtros</li>
            <li><strong>Financeiro</strong> – custos e consolidação</li>
            <li><strong>Relatórios</strong> – análises gerenciais</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =====================================
# BLOCO INFERIOR (VALOR DO SISTEMA)
# =====================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h4>📊 Dados centralizados</h4>
        <p>Integra informações de RH e Financeiro em um único ambiente.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h4>⚙️ Estrutura escalável</h4>
        <p>Projeto preparado para evoluir com novos módulos e banco de dados.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h4>🚀 Foco em decisão</h4>
        <p>Dashboards claros para apoio à gestão e tomada de decisão.</p>
    </div>
    """, unsafe_allow_html=True)
