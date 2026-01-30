import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA (Deve ser o primeiro comando)
st.set_page_config(page_title="IZEN - Assessoria Fiscal", page_icon="🛡️", layout="centered")

# 2. CONFIGURAÇÃO DE LINKS (Edite aqui depois)
# Cole seus links do PagSeguro entre as aspas quando estiverem prontos
link_pag_147 = "https://pag.ae/81sCwqFwa "# Plano Essencial
link_pag_247 = "https://pag.ae/81sCBaYTR" # Plano Popular
link_pag_397 = "https://pag.ae/81sCCiZMa"# Plano Full

# 3. ESTILO CSS (Design Luxo Dark)
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
    .btn-wa {
        background: #25D366;
        color: white !important;
        padding: 18px;
        text-align: center;
        border-radius: 12px;
        font-weight: 800;
        text-decoration: none;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ IZEN</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📲 Instalar App")
    st.caption("v2.1.0 | 2026 © IZEN")

# 5. HEADER (LOGO OU EMOJI)
col_l1, col_l2, col_l3 = st.columns([1, 1.5, 1])
with col_l2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center; color: white;'>🛡️ IZEN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-weight: 600;'>Assessoria IRPF para MEI</p>", unsafe_allow_html=True)

# 6. CALCULADORA
faturamento = st.number_input("Faturamento Anual MEI", min_value=0.0, value=60000.0)
tipo = st.selectbox("Sua Atividade", ["Serviços", "Comércio", "Transportes"])

perc = 0.32 if tipo == "Serviços" else 0.16 if tipo == "Transportes" else 0.08
isento = faturamento * perc
tributavel = faturamento - isento

# 7. RESULTADO
st.markdown(f"""
    <div class="result-card">
        <p style="color: #888; text-transform: uppercase; letter-spacing: 2px; font-size: 11px;">Isenção Estimada</p>
        <h2 style="color: #00ffa3; font-size: 40px; margin: 0;">R$ {isento:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

# 8. PLANOS DE PAGAMENTO
st.markdown("### 💎 Planos de Assessoria")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div style="border: 1px solid #333; padding: 10px; border-radius: 10px; text-align: center; min-height: 100px;"><b>ESSENCIAL</b><br>R$ 147</div>', unsafe_allow_html=True)
    st.link_button("Contratar", link_pag_147, use_container_width=True)

with c2:
    st.markdown('<div style="border: 2px solid #00ffa3; padding: 10px; border-radius: 10px; text-align: center; background: rgba(0,255,163,0.05); min-height: 100px;"><b>POPULAR</b><br>R$ 247</div>', unsafe_allow_html=True)
    st.link_button("Contratar", link_pag_247, use_container_width=True, type="primary")

with c3:
    st.markdown('<div style="border: 1px solid #333; padding: 10px; border-radius: 10px; text-align: center; min-height: 100px;"><b>FULL</b><br>R$ 397</div>', unsafe_allow_html=True)
    st.link_button("Contratar", link_pag_397, use_container_width=True)

st.write("---")
# BOTÃO WHATSAPP FINAL
link_wa = "https://wa.me/5543991533162?text=Fiz%20meu%20diagnóstico%20e%20quero%20começar"
st.markdown(f'<a href="{link_wa}" class="btn-wa">FALAR COM ESPECIALISTA AGORA</a>', unsafe_allow_html=True)

st.write("---")
st.markdown("### 🛠️ Outras Soluções Especializadas IZEN")

with st.expander("📝 Gestão e Obrigações"):
    st.write("""
    * **DASN-SIMEI:** Declaração anual de faturamento.
    * **Parcelamento:** Regularização de impostos em atraso.
    * **Baixa/Alteração:** Mudanças no seu contrato ou encerramento.
    * **Notas Fiscais:** Gestão e emissão profissional de notas.
    """)

with st.expander("📊 Financeiro e Renda"):
    st.write("""
    * **Comprovação de Renda:** Pró-labore oficial para bancos.
    * **Relatório Mensal:** Organização de receitas para fiscalização.
    * **Restituição:** Recuperação de impostos pagos a mais (Monofásicos).
    """)

with st.expander("🚀 Crescimento e Suporte"):
    st.write("""
    * **Desenquadramento:** Migração segura de MEI para ME.
    * **Conta Gov.br:** Suporte para níveis Ouro/Prata.
    * **Alvarás:** Consultoria para licenças e dispensas.
    """)

st.write("---")
st.markdown("### 🛠️ Outros Serviços Especializados")

# Criando 3 colunas para os cards de serviços extras
ca, cb = st.columns(2)

with ca:
    st.markdown("""
        <div style="background: rgba(255,255,255,0.03); padding: 15px; border-radius: 15px; border: 1px solid #333; margin-bottom: 10px;">
            <p style="color: #00ffa3; font-weight: bold; margin-bottom: 5px;">📦 GESTÃO MEI</p>
            <ul style="font-size: 13px; color: #ccc; padding-left: 20px;">
                <li>Declaração Anual (DASN)</li>
                <li>Parcelamento de Dívidas</li>
                <li>Emissão de Notas Fiscais</li>
                <li>Baixa e Alteração</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Consultar Gestão", "https://wa.me/5543991533162?text=Quero%20saber%20mais%20sobre%20Gestão%20MEI", use_container_width=True)

with cb:
    st.markdown("""
        <div style="background: rgba(255,255,255,0.03); padding: 15px; border-radius: 15px; border: 1px solid #333; margin-bottom: 10px;">
            <p style="color: #00ffa3; font-weight: bold; margin-bottom: 5px;">🚀 ESTRATÉGICO</p>
            <ul style="font-size: 13px; color: #ccc; padding-left: 20px;">
                <li>Migração para ME</li>
                <li>Recuperação de Impostos</li>
                <li>Pró-Labore (Renda)</li>
                <li>Suporte Gov.br Ouro</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Consultar Estratégico", "https://wa.me/5543991533162?text=Quero%20saber%20mais%20sobre%20Serviços%20Estratégicos", use_container_width=True)

# Card de Assinatura Mensal (Recorrência)
st.markdown("""
    <div style="background: linear-gradient(145deg, #0a0a0a, #111); padding: 20px; border-radius: 20px; border: 1px solid #00ffa3; text-align: center; margin-top: 20px;">
        <h4 style="color: #fff; margin: 0;">💎 IZEN Prime (Mensal)</h4>
        <p style="color: #888; font-size: 14px;">Assessoria completa todo mês para o seu negócio não parar.</p>
        <p style="color: #00ffa3; font-size: 18px; font-weight: bold;">A partir de R$ 97,00/mês</p>
    </div>
""", unsafe_allow_html=True)
st.link_button("Seja IZEN Prime", "https://wa.me/5543991533162?text=Tenho%20interesse%20no%20IZEN%20Prime%20Mensal", use_container_width=True)

