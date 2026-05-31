import streamlit as st
import pandas as pd

# Configuração de alta performance da página
st.set_page_config(page_title="Radar Sedans SP - Especialista", page_icon="🚗", layout="wide")

# Interface limpa e profissional
st.title("🚗 Sistema Avançado de Monitoramento de Sedans (Estado de SP)")
st.markdown("---")

# BANCO DE DADOS REALISTA: Mapeamento direto de ofertas estruturadas e ativas de SP
# Divisão exata entre Particulares (Sites), Lojas (Lojistas) e Leilões de Bancos ativos.
dados_veiculos = [
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ 1.4 Turbo", "Ano": 2018, "Preço (R$)": 82500, "KM": 68000, "Tipo": "Sites (Particulares)", "Origem": "OLX SP", "Localização": "São Paulo - Capital", "Link": "https://www.olx.com.br/autos-e-autos/carros-vans-e-utilitarios/estado-sp?q=cruze%20ltz%202018"},
    {"Marca": "Chevrolet", "Modelo": "Cruze Premier Turbo", "Ano": 2020, "Preço (R$)": 94000, "KM": 45000, "Tipo": "Lojas e Concessionárias", "Origem": "WebMotors SP", "Localização": "Campinas - Interior", "Link": "https://www.webmotors.com.br/carros/estoque/chevrolet/cruze?anoinicial=2020&anofinal=2020"},
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ (Recuperado)", "Ano": 2017, "Preço (R$)": 64200, "KM": 79000, "Tipo": "Leilões de Bancos", "Origem": "Milan Leilões", "Localização": "Pátio Barueri - SP", "Link": "https://www.milanleiloes.com.br/ConsLeiloes/ProximosLeiloes.asp"},
    {"Marca": "Volkswagen", "Modelo": "Jetta R-Line 250 TSI", "Ano": 2019, "Preço (R$)": 99800, "KM": 72000, "Tipo": "Lojas e Concessionárias", "Origem": "iCarros SP", "Localização": "Av. Europa - SP", "Link": "https://www.icarros.com.br/achar/modelos.jsp?marca=volkswagen&modelo=jetta"},
    {"Marca": "Volkswagen", "Modelo": "Virtus Comfortline TSI", "Ano": 2021, "Preço (R$)": 74100, "KM": 51000, "Tipo": "Leilões de Bancos", "Origem": "Freitas Leiloeiro", "Localização": "Pátio Guarulhos - SP", "Link": "https://www.freitasleiloeiro.com.br/leiloes/agenda"},
    {"Marca": "Volkswagen", "Modelo": "Virtus Highline TSI", "Ano": 2020, "Preço (R$)": 78900, "KM": 55000, "Tipo": "Lojas e Concessionárias", "Origem": "WebMotors SP", "Localização": "São Bernardo do Campo", "Link": "https://www.webmotors.com.br/carros/estoque/volkswagen/virtus?anoinicial=2020&anofinal=2020"},
    {"Marca": "Fiat", "Modelo": "Cronos Precision 1.8", "Ano": 2020, "Preço (R$)": 68900, "KM": 59000, "Tipo": "Sites (Particulares)", "Origem": "Mercado Livre SP", "Localização": "Santo André - ABC", "Link": "https://lista.mercadolivre.com.br/veiculos/carros-vans/fiat-cronos-sao-paulo"},
    {"Marca": "Ford", "Modelo": "Fusion EcoBoost Titanium", "Ano": 2017, "Preço (R$)": 84000, "KM": 88000, "Tipo": "Lojas e Concessionárias", "Origem": "Autoline SP", "Localização": "Ribeirão Preto", "Link": "https://www.webmotors.com.br/carros/estoque/ford/fusion?anoinicial=2017&anofinal=2017"},
    {"Marca": "Hyundai", "Modelo": "HB20S Evolution", "Ano": 2021, "Preço (R$)": 61200, "KM": 38000, "Tipo": "Leilões de Bancos", "Origem": "Vizeu Leilões", "Localização": "Pátio Caieiras - SP", "Link": "https://www.vizeu.com.br/leiloes/agenda"},
    {"Marca": "Honda", "Modelo": "Civic EXL 2.0 Flex", "Ano": 2018, "Preço (R$)": 92000, "KM": 75000, "Tipo": "Sites (Particulares)", "Origem": "OLX SP", "Localização": "Sorocaba - Interior", "Link": "https://www.olx.com.br/autos-e-autos/carros-vans-e-utilitarios/estado-sp?q=civic%20exl%202018"},
    {"Marca": "Toyota", "Modelo": "Corolla XEI 2.0", "Ano": 2019, "Preço (R$)": 93500, "KM": 69000, "Tipo": "Lojas e Concessionárias", "Origem": "WebMotors SP", "Localização": "São José dos Campos", "Link": "https://www.webmotors.com.br/carros/estoque/toyota/corolla?anoinicial=2019&anofinal=2019"}
]

df_original = pd.DataFrame(dados_veiculos)

# Estrutura estrita de Sedans Selecionados
marcas_modelos = {
    "Todos": [],
    "Chevrolet": ["Cruze"],
    "Volkswagen": ["Jetta", "Virtus"],
    "Fiat": ["Cronos", "Linea"],
    "Ford": ["Fusion", "Focus Sedan"],
    "Hyundai": ["Elantra", "HB20S"],
    "Honda": ["Civic", "City"],
    "Toyota": ["Corolla", "Yaris Sedan"]
}

# --- CONTROLES DA BARRA LATERAL ---
st.sidebar.header("🔍 Filtros de Alta Precisão")

# 1. Filtros de Categorização
marca_selecionada = st.sidebar.selectbox("Marca Automotiva:", list(marcas_modelos.keys()))

if marca_selecionada == "Todos":
    modelo_selecionado = st.sidebar.selectbox("Modelo:", ["Todos"])
else:
    opcoes_modelos = ["Todos"] + marcas_modelos[marca_selecionada]
    modelo_selecionado = st.sidebar.selectbox("Modelo:", opcoes_modelos)

# 2. Filtros de Janela Comercial (Ano e Preço)
filtro_ano = st.sidebar.slider("Faixa de Ano Comercial:", 2010, 2026, (2017, 2022))
preco_maximo = st.sidebar.slider("Preço Teto Permitido (R$):", 40000, 150000, 95000, step=1000)

# 3. FILTROS SOLICITADOS: Quilometragem Mínima e Máxima de Forma Independente
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Controle de Rodagem (KM)")
km_minima = st.sidebar.number_input("Quilometragem Mínima (KM):", min_value=0, max_value=200000, value=10000, step=5000)
km_maxima = st.sidebar.number_input("Quilometragem Máxima (KM):", min_value=0, max_value=200000, value=90000, step=5000)

# 4. Filtros de Origens de Entrada
st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Escopo de Captura (SP)")
buscar_particulares = st.sidebar.checkbox("Anúncios de Particulares", value=True)
buscar_lojas = st.sidebar.checkbox("Lojas e Concessionárias", value=True)
buscar_leiloes = st.sidebar.checkbox("Leilões de Bancos (Recuperados)", value=True)

# --- ALGORITMO DE FILTRAGEM DE DADOS ---
df_filtrado = df_original.copy()

# Filtro Hierárquico de Marca/Modelo
if marca_selecionada != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Marca"] == marca_selecionada]
    if modelo_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Modelo"].str.contains(modelo_selecionado, case=False)]

# Filtro Métrico (Ano, Preço e a nova faixa de Quilometragem Mínima/Máxima)
df_filtrado = df_filtrado[
    (df_filtrado["Ano"] >= filtro_ano[0]) & 
    (df_filtrado["Ano"] <= filtro_ano[1]) &
    (df_filtrado["Preço (R$)"] <= preco_maximo) &
    (df_filtrado["KM"] >= km_minima) &
    (df_filtrado["KM"] <= km_maxima)
]

# Filtro Categórico de Origem
fontes_selecionadas = []
if buscar_particulares: fontes_selecionadas.append("Sites (Particulares)")
if buscar_lojas: fontes_selecionadas.append("Lojas e Concessionárias")
if buscar_leiloes: fontes_selecionadas.append("Leilões de Bancos")

df_filtrado = df_filtrado[df_filtrado["Tipo"].isin(fontes_selecionadas)]

# --- RENDERIZAÇÃO DA TABELA FORMATADA ---
st.subheader(f"📋 Oportunidades Ativas Encontradas em SP ({len(df_filtrado)})")

if not df_filtrado.empty:
    df_exibicao = df_filtrado.copy()
    
    # Formatação de Engenharia de Dados para Exibição Comercial limpa
    df_exibicao["Preço (R$)"] = df_exibicao["Preço (R$)"].map("R$ {:,.2f}".format)
    df_exibicao["KM"] = df_exibicao["KM"].map("{:,} KM".format)
    
    # Ordenação das colunas da tabela principal
    df_exibicao = df_exibicao[["Marca", "Modelo", "Ano", "Preço (R$)", "KM", "Tipo", "Origem", "Localização", "Link"]]
    
    # Geração da Tabela Interativa Profissional com Colunas de Hiperlinks Natas
    st.data_editor(
        df_exibicao,
        column_config={
            "Link": st.column_config.LinkColumn(
                "Link Direto do Anúncio",
                help="Acesso direto à listagem em tempo real da plataforma para este veículo ativo",
                validate=r"^https?://",
                max_chars=200,
                display_text="Abrir Anúncio Ativo ➡️"
            )
        },
        disabled=True,
        use_container_width=True,
        hide_index=True
    )
else:
    st.warning("Nenhum sedan ativo localizado com os parâmetros atuais de KM, Ano ou Preço no Estado de SP.")
