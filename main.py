import streamlit as st
import pandas as pd

# Configuração de página
st.set_page_config(page_title="IZEN - Inteligência em Isenção", page_icon="🛡️")

# Estilo customizado para o botão e textos
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ IZEN")
st.write("### O Escudo Digital do seu Lucro MEI")

# Input de dados
with st.container():
    st.write("---")
    faturamento = st.number_input("Quanto você faturou no total (Anual)?", min_value=0.0, value=50000.0, step=1000.0)
    tipo = st.selectbox("Qual a sua atividade principal?", ["Serviços (32%)", "Comércio / Indústria (8%)", "Transporte de Passageiros (16%)"])

# Cálculo de Isenção
if "32%" in tipo: perc = 0.32
elif "16%" in tipo: perc = 0.16
else: perc = 0.08

isento = faturamento * perc
tributavel = faturamento - isento

# Dashboard de Resultados
col1, col2 = st.columns(2)
with col1:
    st.metric("Lucro Isento (Livre de IR)", f"R$ {isento:,.2f}")
    st.caption("Este valor não paga imposto.")
with col2:
    st.metric("Base Tributável", f"R$ {tributavel:,.2f}")
    st.caption("Valor sujeito ao ajuste anual.")

# Gráfico de composição
st.write("#### 📊 Composição do seu Faturamento")
df = pd.DataFrame({'Status': ['Livre de Imposto', 'Sujeito a Imposto'], 'Valor': [isento, tributavel]})
st.bar_chart(df.set_index('Status'))

# Tabela Explicativa (O Toque de Autoridade)
with st.expander("🔍 Ver Regras da Receita Federal"):
    st.write("""
    | Atividade | Percentual de Isenção |
    | :--- | :--- |
    | **Serviços em geral** | 32% do faturamento bruto |
    | **Transporte de Passageiros** | 16% do faturamento bruto |
    | **Comércio e Indústria** | 8% do faturamento bruto |
    """)

# Seção de Venda (Call to Action)
st.divider()
st.write("### 🚀 Quer o relatório pronto para o IRPF?")
if st.button("GERAR DECLARAÇÃO COMPLETA (PDF)"):
    st.balloons()
    st.info("O IZEN Pro gera o passo a passo da sua Declaração de IR por apenas **R$ 29,90**.")
    st.write("**PIX de Pagamento:** `seu-email-ou-chave-aqui` ")
