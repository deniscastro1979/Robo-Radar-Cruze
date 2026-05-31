import streamlit as st
import urllib.parse

# Configuração da página do aplicativo
st.set_page_config(page_title="Radar Sedans SP Real", page_icon="🚗", layout="wide")

# Título Principal
st.title("🚗 Radar Multimarcas - Busca Real de Sedans (Estado de SP)")
st.markdown("---")
st.write("Configure os filtros na lateral para gerar os links diretos de busca com anúncios 100% ativos e reais no mercado de SP.")

# --- DICIONÁRIO DE MARCAS E MODELOS (SEDANS) ---
marcas_modelos = {
    "Chevrolet": ["Cruze"],
    "Volkswagen": ["Jetta", "Virtus"],
    "Fiat": ["Cronos", "Linea"],
    "Ford": ["Fusion", "Focus"],
    "Hyundai": ["Elantra", "HB20S"],
    "Honda": ["Civic", "City"],
    "Toyota": ["Corolla", "Yaris"]
}

# --- BARRA LATERAL DE FILTROS ---
st.sidebar.header("🔍 Configurar Sua Busca")

# Seleção de Marca e Modelo
marca_selecionada = st.sidebar.selectbox("Selecione a Marca:", list(marcas_modelos.keys()))
modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", marcas_modelos[marca_selecionada])

# Filtros de Ano e Preço Max
ano_min = st.sidebar.number_input("Ano Mínimo:", min_value=2010, max_value=2027, value=2017)
ano_max = st.sidebar.number_input("Ano Máximo:", min_value=2010, max_value=2027, value=2022)
preco_maximo = st.sidebar.number_input("Preço Máximo (R$):", min_value=20000, max_value=300000, value=90000, step=1000)

st.sidebar.markdown("---")
st.sidebar.info("📌 Os links gerados mostram apenas anúncios ativos de particulares, lojas e concessionárias do Estado de SP.")

# --- CONSTRUÇÃO DOS LINKS REAIS DE BUSCA (ESTADO DE SP) ---

# Termo de busca tratado para URLs
termo_busca = f"{marca_selecionada} {modelo_selecionado}"
termo_url = urllib.parse.quote(termo_busca)

# 1. Link Real WebMotors (Já inclui Particulares + Lojas/Concessionárias de SP)
url_webmotors = f"https://www.webmotors.com.br/carros/estoque/comboio/sp?tipoveiculo=carros&anoinicial={ano_min}&anofinal={ano_max}&precofinal={preco_maximo}&q={termo_url}"

# 2. Link Real OLX (Filtrado para o Estado de SP - Inclui Lojas profissionais e Particulares ativos)
url_olx = f"https://www.olx.com.br/autos-e-autos/carros-vans-e-utilitarios/estado-sp?an={ano_min}&ax={ano_max}&pe={preco_maximo}&q={termo_url}"

# 3. Link Real Mercado Livre (Filtrado para São Paulo, Sedans, ativos)
url_mercadolivre = f"https://lista.mercadolivre.com.br/veiculos/carros-vans/{marca_selecionada.lower()}/{modelo_selecionado.lower()}/sao-paulo/_PriceRange_0-{preco_maximo}_YearRange_{ano_min}-{ano_max}"

# 4. Link focado em Grandes Portais de Lojas/Concessionárias (iCarros - SP)
url_icarros = f"https://www.icarros.com.br/achar/modelos.jsp?anoinicial={ano_min}&anofinal={ano_max}&precofinal={preco_maximo}&marca={marca_selecionada}&modelo={modelo_selecionado}&estado=SP"


# --- EXIBIÇÃO DOS PAINÉIS DE BUSCA ---

st.subheader(f"📋 Motores de Busca Prontos para: {marca_selecionada} {modelo_selecionado} ({ano_min} - {ano_max})")
st.write(f"Preço Limite: **R$ {preco_maximo:,.2f}** | Região: **Estado de São Paulo (Foco em Lojas e Particulares)**")

st.markdown("### 🚀 Clique nos botões para abrir os anúncios ativos:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🌐 Grandes Portais (Lojas & Particulares)")
    st.link_button("🔥 Abrir na WebMotors (SP)", url_webmotors, use_container_width=True, help="Abre o estoque real de lojistas e particulares de SP")
    st.link_button("📦 Abrir no Mercado Livre (SP)", url_mercadolivre, use_container_width=True, help="Abre listagem direta de sedans em SP")

with col2:
    st.markdown("#### 🏪 Classificados & Redes de Lojas")
    st.link_button("💬 Abrir na OLX (SP)", url_olx, use_container_width=True, help="Busca anúncios ativos diretos no estado")
    st.link_button("🏬 Abrir no iCarros (Concessionárias SP)", url_icarros, use_container_width=True, help="Foco total em estoque de lojas e concessionárias de SP")

st.markdown("---")
st.markdown("### 🏛️ Verificação em Leilões de Bancos ativos (SP)")
st.write("Os leilões mudam os lotes toda semana. Use os links diretos dos principais leiloeiros de bancos de SP para ver o pátio de hoje:")

col3, col4 = st.columns(2)
with col3:
    st.link_button("🔨 Milan Leilões (Pátio Barueri/Itaú)", "https://www.milanleiloes.com.br", use_container_width=True)
with col4:
    st.link_button("🔨 Freitas Leiloeiro (Pátio Guarulhos/Bradesco)", "https://www.freitasleiloeiro.com.br", use_container_width=True)
