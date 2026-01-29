import streamlit as st
import pandas as pd

# Configuração de Alta Qualidade
st.set_page_config(page_title="IZEN - Inteligência Financeira", page_icon="🛡️", layout="centered")

# CSS Personalizado para interface Premium
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #00ffa3; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #0066FF; color: white; border: none; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #0052cc; border: none; color: white; }
    .report-card { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Topo do App
st.image("https://img.icons8.com/fluency/96/shield-with-check.png", width=60)
st.title("IZEN")
st.markdown("##### *Inteligência em Isenção para MEI*")
st.write("---")

# Área de Cálculo (Interface Limpa)
with st.container():
    st.markdown("### 📝 Dados da sua Empresa")
    col_a, col_b = st.columns(2)
    with col_a:
        faturamento = st.number_input("Faturamento Bruto Anual", min_value=0.0, value=50000.0, help="Soma de todas as suas vendas/serviços no ano.")
    with col_b:
        tipo = st.selectbox("Atividade Principal", ["Prestação de Serviços", "Comércio / Indústria", "Transporte de Passageiros"])

# Lógica de Cálculo
percentuais = {"Prestação de Serviços": 0.32, "Comércio / Indústria": 0.08, "Transporte de Passageiros": 0.16}
perc = percentuais[tipo]
isento = faturamento * perc
tributavel = faturamento - isento

# Dashboard Visual
st.markdown("### 📊 Resultado da Análise")
col1, col2 = st.columns(2)
with col1:
    st.metric("Lucro Isento", f"R$ {isento:,.2f}")
    st.caption("✅ Livre de impostos")
with col2:
    st.metric("Lucro Tributável", f"R$ {tributavel:,.2f}")
    st.caption("⚠️ Base de cálculo do IR")

# Gráfico de Alta Qualidade
st.write("")
df_viz = pd.DataFrame({"Status": ["Livre de IR", "Sujeito a IR"], "Valor": [isento, tributavel]})
st.bar_chart(df_viz.set_index("Status"), color=["#00ffa3", "#ff4b4b"])

# Seção de Valor Agregado
with st.expander("💡 Como essa regra funciona?"):
    st.write(f"De acordo com a Receita Federal, para a sua atividade de **{tipo}**, presume-se que **{perc*100:.0f}%** do seu faturamento seja lucro isento. O restante é considerado rendimento tributável, a menos que você tenha contabilidade completa.")

# Chamada para o Relatório PRO
st.write("---")
st.markdown("""
    <div class='report-card'>
        <h3 style='color: #0066FF; margin-top: 0;'>🚀 Obtenha seu Relatório IZEN Pro</h3>
        <p>Não corra riscos com a malha fina. Receba o guia detalhado de preenchimento para sua declaração.</p>
    </div>
    """, unsafe_allow_html=True)

# Seção de Venda Profissional
st.write("---")
st.markdown("""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 12px; border-left: 5px solid #28a745;">
        <h3 style="color: #1d1d1d; margin-top: 0;">🚀 Relatório IZEN Pro</h3>
        <p style="color: #444;">Receba agora o passo a passo detalhado para preencher sua declaração sem erros e evitar a malha fina.</p>
    </div>
    """, unsafe_allow_html=True)

# O seu link do PagBank aqui
link_pagbank = "https://pag.ae/81sAJrK-p" 

st.write("")

# Botão Estilizado com as cores de confiança
st.markdown(f'''
    <a href="{link_pagbank}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #28a745; color: white; padding: 18px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 1.2em; box-shadow: 0px 4px 10px rgba(40, 167, 69, 0.3);">
            ✅ ADQUIRIR RELATÓRIO POR R$ 29,90
        </div>
    </a>
''', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.8em; color: gray; margin-top: 10px;'>Pagamento seguro via PagBank</p>", unsafe_allow_html=True)

