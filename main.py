import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA (Deve ser o primeiro comando)
st.set_page_config(page_title="IZEN - Assessoria Fiscal", page_icon="🛡️", layout="centered")

# 2. CONFIGURAÇÃO DE LINKS OFICIAIS
link_pag_147 = "https://pag.ae/81sCwqFwa" # Plano Essencial
link_pag_247 = "https://pag.ae/81sCBaYTR" # Plano Popular
link_pag_397 = "https://pag.ae/81sCCiZMa" # Plano Full
whatsapp_link = "https://wa.me/5543991533162"

# 3. ESTILO CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    .main { background-color: #050505; }
    .result-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid #1a1a1a;
        text-align: center;
        margin-bottom: 25px;
    }
    .premium-card {
        background: rgba(0, 255, 163, 0.03);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(0, 255, 163, 0.2);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ IZEN</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.info("Especialista em Proteção Fiscal para MEI")
    st.caption("v3.1.0 | 2026 © IZEN")

# 5. HEADER (LOGO OU EMOJI)
col_l1, col_l2, col_l3 = st.columns([1, 1.5, 1])
with col_l2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center; color: white;'>🛡️ IZEN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-weight: 600;'>Diagnóstico de Isenção e Assessoria</p>", unsafe_allow_html=True)

# 6. CALCULADORA
with st.expander("📊 Simular minha Isenção Agora", expanded=True):
    faturamento = st.number_input("Faturamento Anual MEI (R$)", min_value=0.0, value=60000.0)
    tipo = st.selectbox("Sua Atividade Principal", ["Serviços", "Comércio", "Transportes"])

    perc = 0.32 if tipo == "Serviços" else 0.16 if tipo == "Transportes" else 0.08
    isento = faturamento * perc
    
    st.markdown(f"""
        <div class="result-card">
            <p style="color: #888; text-transform: uppercase; letter-spacing: 2px; font-size: 11px;">Valor Isento Estimado</p>
            <h2 style="color: #00ffa3; font-size: 40px; margin: 0;">R$ {isento:,.2f}</h2>
            <p style="color: #555; font-size: 12px;">Isso é o que você não paga imposto no seu CPF.</p>
        </div>
        """, unsafe_allow_html=True)

# 7. PLANOS IRPF (O CARRO-CHEFE)
st.markdown("### 💎 Planos de Assessoria IRPF")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div style="border: 1px solid #333; padding: 10px; border-radius: 10px; text-align: center; min-height: 100px;"><b>ESSENCIAL</b><br><small>R$ 147</small></div>', unsafe_allow_html=True)
    st.link_button("Contratar", link_pag_147, use_container_width=True)
with c2:
    st.markdown('<div style="border: 2px solid #00ffa3; padding: 10px; border-radius: 10px; text-align: center; background: rgba(0,255,163,0.05); min-height: 100px;"><b>POPULAR</b><br><small>R$ 247</small></div>', unsafe_allow_html=True)
    st.link_button("Contratar", link_pag_247, use_container_width=True, type="primary")
with c3:
    st.markdown('<div style="border: 1px solid #333; padding: 10px; border-radius: 10px; text-align: center; min-height: 100px;"><b>FULL</b><br><small>R$ 397</small></div>', unsafe_allow_html=True)
    st.link_button("Contratar", link_pag_397, use_container_width=True)

# 8. ÁREA DE SERVIÇOS (GRÁTIS VS PREMIUM)
st.write("---")
st.markdown("### 🚀 Ecossistema de Soluções IZEN")

tab1, tab2 = st.tabs(["🎁 Serviços Gratuitos", "🏆 Soluções Premium"])

with tab1:
    st.write("Use nossas ferramentas gratuitas para organizar seu negócio:")
    cg1, cg2 = st.columns(2)
    with cg1:
        st.markdown("""<div style="height: 110px;"><b>📋 Checklist IRPF</b><br><small>Lista de docs para não cair na malha fina.</small></div>""", unsafe_allow_html=True)
        st.link_button("Baixar Grátis", f"{whatsapp_link}?text=Quero%20o%20Checklist%20Gratuito", use_container_width=True)
    with cg2:
        st.markdown("""<div style="height: 110px;"><b>🔍 Consulta CNPJ</b><br><small>Verificamos pendências no seu MEI agora.</small></div>""", unsafe_allow_html=True)
        st.link_button("Consultar Agora", f"{whatsapp_link}?text=Quero%20consultar%20meu%20CNPJ", use_container_width=True)

with tab2:
    st.markdown('<div class="premium-card"><b>🛠️ Regularização Total</b><br><small>Parcelamento de dívidas e limpeza de CNPJ.</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><b>📈 IZEN Prime (Mensal)</b><br><small>Sua contabilidade MEI completa por mês.</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><b>🚀 Migração para ME</b><br><small>Planejamento para quem estourou o teto.</small></div>', unsafe_allow_html=True)
    st.link_button("Solicitar Orçamento Premium", f"{whatsapp_link}?text=Quero%20um%20orçamento%20Premium", use_container_width=True)

st.write("---")
st.link_button("💬 Dúvidas? Fale com o Especialista", whatsapp_link, use_container_width=True)
