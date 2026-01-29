import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="IZEN - Inteligência em Isenção", layout="centered")

st.title("💰 IZEN")
st.subheader("O Escudo do seu Lucro MEI")

# Entrada de dados
faturamento = st.number_input("Quanto você faturou no ano? (R$)", min_value=0.0, value=10000.0, step=1000.0)
servico = st.checkbox("Meu negócio é Prestação de Serviços")

# Lógica de cálculo (Regras da Receita Federal)
percentual = 0.32 if servico else 0.08
lucro_isento = faturamento * percentual
lucro_tributavel = faturamento - lucro_isento

# Exibição dos resultados em cards
col1, col2 = st.columns(2)
col1.metric("Lucro Isento (Protegido)", f"R$ {lucro_isento:,.2f}")
col2.metric("Lucro Tributável", f"R$ {lucro_tributavel:,.2f}")

# Gráfico Nativo (Super leve)
st.write("### 📊 Visão Geral do seu Capital")
dados_grafico = pd.DataFrame({
    'Tipo': ['Isento', 'Tributável'],
    'Valores': [lucro_isento, lucro_tributavel]
}).set_index('Tipo')

st.bar_chart(dados_grafico)

# Seção de Venda
st.divider()
st.info("💡 Você sabia? Com a escrituração correta, você pode transformar quase todo seu lucro em isento.")
if st.button("🚀 Liberar Relatório Completo para o IRPF"):
    st.warning("PIX Copia e Cola Gerado: 00020126580014br.gov.bcb.pix...")
    st.write("Envie o comprovante de R$ 29,90 para liberar seu PDF oficial.")
  
