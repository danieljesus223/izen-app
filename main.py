import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DO LINK ---
link_app = "https://danieljesus223-izen-app-main-9nbdh.streamlit.app" 

# --- CONFIGURAÇÃO DA PÁGINA (Deve vir antes de quase tudo) ---
st.set_page_config(page_title="IZEN - Assessoria Fiscal", page_icon="🛡️", layout="centered")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ IZEN</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Assessoria Fiscal Premium</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📲 Instalar no Celular")
    with st.expander("Ver instruções", expanded=True):
        st.markdown("""
**No iPhone:**
1. Abra no Safari
2. Toque em **Compartilhar** ⬆️
3. **Adicionar à Tela de Início**

**No Android:**
1. Toque nos **3 pontos** ⋮
2. **Instalar aplicativo**
        """)
    
    st.markdown("---")
    st.markdown("### 💬 Suporte")
    link_wa_lateral = "https://wa.me/5543991533162?text=Preciso%20de%20suporte%20técnico"
    st.markdown(f'<a href="{link_wa_lateral}" style="text-decoration:none;"><div style="background-color:#111;color:#00ffa3;padding:10px;text-align:center;border-radius:8px;border:1px solid #00ffa3;font-weight:bold;">Falar com Especialista</div></a>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("v2.1.0 | 2026 © IZEN")

# CSS Avançado - Design de Escritório de Luxo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    .main { background-color: #050505; }
    
    /* Card de Resultado */
    .result-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid #1a1a1a;
        text-align: center;
        margin-bottom: 25px;
    }

    /* Botão WhatsApp Premium */
    .btn-wa {
        background: #25D366;
        color: white !important;
        padding: 20px;
        text-align: center;
        border-radius: 16px;
        font-weight: 800;
        font-size: 18px;
        text-decoration: none;
        display: block;
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(37, 211, 102, 0.2);
    }
    .btn-wa:hover { transform: translateY(-3px); box-shadow: 0 15px 30px rgba(37, 211, 102, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: white;'>🛡️ IZEN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Diagnóstico de Isenção e Assessoria IRPF</p>", unsafe_allow_html=True)

# --- CALCULADORA ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        faturamento = st.number_input("Faturamento Anual MEI", min_value=0.0, value=60000.0)
    with col2:
        tipo = st.selectbox("Sua Atividade", ["Serviços", "Comércio", "Transportes"])

# Lógica
perc = 0.32 if tipo == "Serviços" else 0.16 if tipo == "Transportes" else 0.08
isento = faturamento * perc
tributavel = faturamento - isento

# --- RESULTADO ---
st.markdown(f"""
    <div class="result-card">
        <p style="color: #888; text-transform: uppercase; letter-spacing: 2px; font-size: 12px;">Resultado Preliminar</p>
        <h2 style="color: #00ffa3; font-size: 42px; margin: 0;">R$ {isento:,.2f} Isentos</h2>
        <p style="color: #666; font-size: 14px; margin-top: 10px;">Base Tributável Estimada: R$ {tributavel:,.2f}</p>
    </div>
    """, unsafe_allow_html=True)

# --- ASSESSORIA HUMANA ---
st.markdown("### 🤝 Assessoria Especializada")
st.write("Não preencha sua declaração sozinho. Nossa assessoria garante a transmissão correta e o aproveitamento máximo da sua isenção.")

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("✅ **Transmissão Oficial**")
    st.markdown("✅ **Análise de Documentos**")
with col_b:
    st.markdown("✅ **Proteção Anti-Malha Fina**")
    st.markdown("✅ **Recibo de Entrega**")

st.write("---")
st.markdown("#### 📑 O que vamos precisar para sua Assessoria:")
col_list1, col_list2 = st.columns(2)

with col_list1:
    st.markdown("- [ ] CNPJ do MEI")
    st.markdown("- [ ] Relatório de Faturamento")
    st.markdown("- [ ] Comprovantes de Despesas")

with col_list2:
    st.markdown("- [ ] Informe Bancário")
    st.markdown("- [ ] CPF e Título de Eleitor")
    st.markdown("- [ ] Conta Gov.br (Ouro ou Prata)")

st.info("💡 Não tem tudo em mãos? Fique tranquilo, nosso especialista ajudará você a organizar cada documento.")

st.write("---")
st.markdown("### 💎 Planos de Assessoria")

# --- SEÇÃO DE PAGAMENTO ---
c1, c2, c3 = st.columns(3)

# Links de Pagamento (Substitua pelos seus links reais do PagBank/Mercado Pago)
link_pago_essencial = "https://pag.ae/81sCwqFwa"
link_pago_popular = "https://pag.ae/81sCBaYTR"
link_pago_full = "https://pag.ae/81sCCiZMa"

with c1:
    st.markdown("""
    <div style="border: 1px solid #333; padding: 15px; border-radius: 10px; text-align: center; min-height: 150px;">
        <p style="font-size: 12px; color: #888;">ESSENCIAL</p>
        <h4 style="margin: 0;">R$ 147</h4>
        <p style="font-size: 11px;">Apenas IRPF</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pagar Essencial", link_pago_essencial, use_container_width=True)

with c2:
    st.markdown("""
    <div style="border: 2px solid #00ffa3; padding: 15px; border-radius: 10px; text-align: center; background: rgba(0,255,163,0.05); min-height: 150px;">
        <p style="font-size: 12px; color: #00ffa3;">POPULAR</p>
        <h4 style="margin: 0;">R$ 247</h4>
        <p style="font-size: 11px;">IRPF + DASN-SIMEI</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pagar Popular", link_pago_popular, use_container_width=True, type="primary")

with c3:
    st.markdown("""
    <div style="border: 1px solid #333; padding: 15px; border-radius: 10px; text-align: center; min-height: 150px;">
        <p style="font-size: 12px; color: #888;">FULL</p>
        <h4 style="margin: 0;">R$ 397</h4>
        <p style="font-size: 11px;">Completo + VIP</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pagar Full", link_pago_full, use_container_width=True)

st.write("")
link_wa = "https://wa.me/5543991533162?text=Olá!%20Fiz%20meu%20diagnóstico%20no%20IZEN%20e%20preciso%20de%20ajuda%20com%20minha%20declaração."
st.markdown(f'<a href="{link_wa}" class="btn-wa">FALAR COM ESPECIALISTA AGORA</a>', unsafe_allow_html=True)

st.write("")
st.caption("A análise acima é uma estimativa. A assessoria humana valida todos os dados antes do envio.")
