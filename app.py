import streamlit as st
import pandas as pd

# Configuração da página do aplicativo
st.set_page_config(page_title="Radar Multimarcas - Sedans", page_icon="🚗", layout="wide")

# Título Principal
st.title("🚗 Radar Multimarcas - Sistema de Monitoramento de Sedans")
st.markdown("---")

# Banco de dados simulado com oportunidades reais de mercado e leilões
dados_veiculos = [
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ", "Ano": 2018, "Preço (R$)": 82500, "KM": 68000, "Origem": "OLX (Particular)", "Link": "#"},
    {"Marca": "Chevrolet", "Modelo": "Cruze Premier", "Ano": 2020, "Preço (R$)": 94000, "KM": 45000, "Origem": "WebMotors", "Link": "#"},
    {"Marca": "Volkswagen", "Modelo": "Jetta R-Line", "Ano": 2019, "Preço (R$)": 99800, "KM": 72000, "Origem": "Mercado Livre", "Link": "#"},
    {"Marca": "Volkswagen", "Modelo": "Virtus Comfortline", "Ano": 2021, "Preço (R$)": 76500, "KM": 51000, "Origem": "Leilão Banco Itaú", "Link": "#"},
    {"Marca": "Fiat", "Modelo": "Cronos Precision", "Ano": 2020, "Preço (R$)": 68900, "KM": 59000, "Origem": "OLX", "Link": "#"},
    {"Marca": "Ford", "Modelo": "Fusion EcoBoost", "Ano": 2017, "Preço (R$)": 84000, "KM": 88000, "Origem": "WebMotors", "Link": "#"},
    {"Marca": "Hyundai", "Modelo": "Elantra GLS", "Ano": 2018, "Preço (R$)": 79900, "KM": 80000, "Origem": "Particular", "Link": "#"},
    {"Marca": "Hyundai", "Modelo": "HB20S Evolution", "Ano": 2021, "Preço (R$)": 69000, "KM": 38000, "Origem": "Leilão Bradesco", "Link": "#"},
    {"Marca": "Honda", "Modelo": "Civic EXL", "Ano": 2018, "Preço (R$)": 92000, "KM": 75000, "Origem": "WebMotors", "Link": "#"},
    {"Marca": "Honda", "Modelo": "City EXL", "Ano": 2019, "Preço (R$)": 78000, "KM": 61000, "Origem": "OLX", "Link": "#"},
    {"Marca": "Toyota", "Modelo": "Corolla XEI", "Ano": 2019, "Preço (R$)": 93500, "KM": 69000, "Origem": "Particular", "Link": "#"},
    {"Marca": "Toyota", "Modelo": "Yaris Sedan XLS", "Ano": 2020, "Preço (R$)": 79000, "KM": 47000, "Origem": "Leilão Santander", "Link": "#"}
]

df_original = pd.DataFrame(dados_veiculos)

# Dicionário mapeando as marcas aos seus respectivos modelos sedans selecionados por você
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

# --- BARRA LATERAL DE FILTROS ---
st.sidebar.header("🔍 Painel de Controle e Filtros")

# Filtro 1: Escolha da Marca
lista_marcas = list(marcas_modelos.keys())
marca_selecionada = st.sidebar.selectbox("Selecione a Marca:", lista_marcas)

# Filtro 2: Escolha Dinâmica do Modelo baseado na marca escolhida
if marca_selecionada == "Todos":
    modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", ["Todos"])
else:
    opcoes_modelos = ["Todos"] + marcas_modelos[marca_selecionada]
    modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", opcoes_modelos)

# Filtro 3: Faixa de Ano
ano_min, ano_max = int(df_original["Ano"].min()), int(df_original["Ano"].max())
filtro_ano = st.sidebar.slider("Faixa de Ano do Veículo:", 2010, 2026, (2017, 2022))

# Filtro 4: Preço Teto
preco_maximo = st.sidebar.slider("Preço Máximo (R$):", 40000, 150000, 95000, step=1000)

# Filtro 5: Quilometragem Máxima
km_maxima = st.sidebar.slider("Quilometragem Máxima (KM):", 10000, 150000, 90000, step=5000)

# Botão de Comando do Robô
st.sidebar.markdown("---")
if st.sidebar.button("▶️ INICIAR MONITORAMENTO", use_container_width=True):
    st.sidebar.success(f"Robô Ativado para {marca_selecionada}!")

# --- LÓGICA DE FILTRAGEM DO BANCO DE DADOS ---
df_filtrado = df_original.copy()

# Filtrando por Marca
if marca_selecionada != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Marca"] == marca_selecionada]
    
    # Filtrando por Modelo (verifica se o texto digitado está contido no nome do modelo do banco)
    if modelo_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Modelo"].str.contains(modelo_selecionado, case=False)]

# Filtrando por Ano, Preço e KM
df_filtrado = df_filtrado[
    (df_filtrado["Ano"] >= filtro_ano[0]) & 
    (df_filtrado["Ano"] <= filtro_ano[1]) &
    (df_filtrado["Preço (R$)"] <= preco_maximo) &
    (df_filtrado["KM"] <= km_maxima)
]

# --- EXIBIÇÃO DOS RESULTADOS ---
st.subheader(f"📋 Oportunidades Encontradas ({len(df_filtrado)})")

if not df_filtrado.empty:
    # Formatação visual para exibição da tabela de moedas
    df_exibicao = df_filtrado.copy()
    df_exibicao["Preço (R$)"] = df_exibicao["Preço (R$)"].map("R$ {:,.2f}".format)
    df_exibicao["KM"] = df_exibicao["KM"].map("{:,} KM".format)
    
    st.dataframe(df_exibicao, use_container_width=True)
else:
    st.warning("Nenhum sedan encontrado com os filtros atuais. Tente aumentar o preço máximo ou expandir a faixa de anos na lateral.")
