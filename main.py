import streamlit as st
import pandas as pd

# Configuração de Página Premium
st.set_page_config(page_title="IZEN - Shield Your Profit", page_icon="🛡️", layout="centered")

# CSS Avançado - Design de Elite
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .main { background-color: #050505; }
    
    /* Card Principal de Resultado */
    .premium-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid #333;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Estilização das Métricas */
    div[data-testid="stMetricValue"] {
        color: #00ffa3 !important;
        font-weight: 800 !important;
        font-size: 36px !important;
    }
    
    /* Botão de Pagamento Estilo Apple */
    .btn-buy {
        background: linear-gradient(90deg, #0066FF 0%, #00CCFF 100%);
        color: white !important;
        padding: 20px;
        text-align: center;
        border-radius: 16px;
        font-weight: 800;
        font-size: 20px;
        text-decoration: none;
        display: block;
        transition: all 0.4s ease;
        box-shadow: 0 4px 15px rgba(0, 102, 255, 0.4);
    }
    .btn-buy:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 102, 255, 0.6);
    }

    /* Input Styling */
    .stNumberInput, .stSelectbox {
        background-color: #111 !important;
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: white; font-size: 50px;'>🛡️ IZEN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 18px;'>Inteligência em Isenção Fiscal para MEI</p>", unsafe_allow_html=True)
st.write("")

# --- INPUTS ---
with st.container():
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        faturamento = st.number_input("Faturamento Anual 2025", min_value=0.0, value=60000.0, step=1000.0)
    with col_in2:
        tipo = st.selectbox("Atividade", ["Serviços (32%)", "Comércio (8%)", "Transporte (16%)"])

# Lógica
perc = 0.32 if "32" in tipo else 0.16 if "16" in tipo else 0.08
isento = faturamento * perc
tributavel = faturamento - isento

# --- DASHBOARD PREMIUM ---
st.markdown(f"""
    <div class="premium-card">
        <p style="color: #888; margin-bottom: 5px; font-size: 14px; text-transform: uppercase; letter-spacing: 2px;">Lucro Isento Detectado</p>
        <h2 style="color: #00ffa3; font-size: 52px; margin: 0;">R$ {isento:,.2f}</h2>
        <p style="color: #555; font-size: 14px; margin-top: 10px;">Este valor está protegido e não sofrerá tributação de IRPF.</p>
    </div>
    """, unsafe_allow_html=True)

# --- GRÁFICO ---
st.write("#### ⚖️ Composição de Rendimentos")
df_viz = pd.DataFrame({"Categoria": ["Livre de IR", "Tributável"], "Valor": [isento, tributavel]})
st.bar_chart(df_viz, x="Categoria", y="Valor", color="#0066FF")

# --- ÁREA DE VENDAS PRO ---
st.write("")
with st.container():
    st.markdown("""
        <div style="background: rgba(255,255,255,0.03); padding: 25px; border-radius: 20px; border: 1px dashed #444;">
            <h4 style="color: #fff; margin-top:0;">💎 Upgrade para IZEN Pro</h4>
            <p style="color: #aaa; font-size: 15px;">A Receita Federal exige o preenchimento correto de 3 fichas diferentes. Errar um campo pode custar <b>R$ 165,74</b> em multa mínima.</p>
            <ul style="color: #888; font-size: 14px;">
                <li>Guia passo a passo em PDF</li>
                <li>Códigos oficiais das fichas</li>
                <li>Suporte prioritário via WhatsApp</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # LINKS (Substitua pelos seus)
    link_pagbank = "SEU_LINK_PAGBANK"
    link_wa = "https://wa.me/5543991533162?text=Preciso%20de%20ajuda%20com%20o%20IZEN"

    st.markdown(f'<a href="{link_pagbank}" class="btn-buy">LIBERAR RELATÓRIO COMPLETO →</a>', unsafe_allow_html=True)
    
    st.write("")
    st.markdown(f"""
        <div style="text-align: center;">
            <a href="{link_wa}" style="color: #25D366; text-decoration: none; font-size: 14px; font-weight: 600;">
                Dúvidas? Fale com um especialista no WhatsApp
            </a>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.caption("© 2026 IZEN Intelligence - Tecnologia de Proteção Fiscal")
