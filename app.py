import streamlit as st
import pandas as pd

# Configuração da página do aplicativo
st.set_page_config(page_title="Radar Sedans SP Total", page_icon="🚗", layout="wide")

# Título Principal
st.title("🚗 Radar Multimarcas - Monitoramento Total de Sedans (Estado de SP)")
st.markdown("---")

# Banco de dados simulado com oportunidades focadas no Estado de São Paulo (Particulares, Lojas e Leilões)
dados_veiculos = [
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ", "Ano": 2018, "Preço (R$)": 82500, "KM": 68000, "Tipo": "Sites (Particulares)", "Local": "São Paulo - SP (OLX)", "Link": "https://www.olx.com.br"},
    {"Marca": "Chevrolet", "Modelo": "Cruze Premier", "Ano": 2020, "Preço (R$)": 94000, "KM": 45000, "Tipo": "Sites (Particulares)", "Local": "Campinas - SP (WebMotors)", "Link": "https://www.webmotors.com.br"},
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ", "Ano": 2017, "Preço (R$)": 64200, "KM": 79000, "Tipo": "Leilões de Bancos (Recuperados)", "Local": "Pátio Barueri - SP (Leilão Itaú)", "Link": "https://www.milanleiloes.com.br"},
    {"Marca": "Volkswagen", "Modelo": "Jetta R-Line", "Ano": 2019, "Preço (R$)": 99800, "KM": 72000, "Tipo": "Lojas e Concessionárias", "Local": "Loja Multimarcas - Av. Europa (SP)", "Link": "https://www.webmotors.com.br"},
    {"Marca": "Volkswagen", "Modelo": "Virtus Comfortline", "Ano": 2021, "Preço (R$)": 74100, "KM": 51000, "Tipo": "Leilões de Bancos (Recuperados)", "Local": "Pátio Guarulhos - SP (Leilão Bradesco)", "Link": "https://www.freitasleiloeiro.com.br"},
    {"Marca": "Volkswagen", "Modelo": "Virtus Highline", "Ano": 2020, "Preço (R$)": 78900, "KM": 55000, "Tipo": "Lojas e Concessionárias", "Local": "Concessionária Seminovos - São Bernardo - SP", "Link": "https://www.icarros.com.br"},
    {"Marca": "Fiat", "Modelo": "Cronos Precision", "Ano": 2020, "Preço (R$)": 68900, "KM": 59000, "Tipo": "Sites (Particulares)", "Local": "Santo André - SP (Mercado Livre)", "Link": "https://www.mercadolivre.com.br"},
    {"Marca": "Ford", "Modelo": "Fusion EcoBoost", "Ano": 2017, "Preço (R$)": 84000, "KM": 88000, "Tipo": "Lojas e Concessionárias", "Local": "Portal dos Autos - Shopping de Carros (SP)", "Link": "https://www.autoline.com.br"},
    {"Marca": "Hyundai", "Modelo": "HB20S Evolution", "Ano": 2021, "Preço (R$)": 61200, "KM": 38000, "Tipo": "Leilões de Bancos (Recuperados)", "Local": "Pátio Caieiras - SP (Leilão Santander)", "Link": "https://www.therezaleiloes.com.br"},
    {"Marca": "Honda", "Modelo": "Civic EXL", "Ano": 2018, "Preço (R$)": 92000, "KM": 75000, "Tipo": "Sites (Particulares)", "Local": "Sorocaba - SP", "Link": "https://www.olx.com.br"},
    {"Marca": "Toyota", "Modelo": "Corolla XEI", "Ano": 2019, "Preço (R$)": 93500, "KM": 69000, "Tipo": "Lojas e Concessionárias", "Local": "Toyota Seminovos Certificados - SP", "Link": "https://www.webmotors.com.br"},
    {"Marca": "Toyota", "Modelo": "Yaris Sedan XLS", "Ano": 2020, "Preço (R$)": 71000, "KM": 47000, "Tipo": "Leilões de Bancos (Recuperados)", "Local": "Pátio Jacareí - SP (Leilão Safra)", "Link": "https://www.vizeu.com.br"}
]

df_original = pd.DataFrame(dados_veiculos)

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
st.sidebar.header("🔍 Painel de Controle")

# Filtro de Marca
marca_selecionada = st.sidebar.selectbox("Selecione a Marca:", list(marcas_modelos.keys()))

# Filtro de Modelo
if marca_selecionada == "Todos":
    modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", ["Todos"])
else:
    opcoes_modelos = ["Todos"] + marcas_modelos[marca_selecionada]
    modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", opcoes_modelos)

# Faixa de Ano, Preço e KM
filtro_ano = st.sidebar.slider("Faixa de Ano do Veículo:", 2010, 2026, (2017, 2022))
preco_maximo = st.sidebar.slider("Preço Máximo (R$):", 40000, 150000, 95000, step=1000)
km_maxima = st.sidebar.slider("Quilometragem Máxima (KM):", 10000, 150000, 90000, step=5000)

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Fontes de Origem (SP)")

# Caixas de Seleção para Ativar/Desativar as Origens de Venda
buscar_particulares = st.sidebar.checkbox("Sites (Particulares - OLX, M.Livre)", value=True)
buscar_lojas = st.sidebar.checkbox("Lojas e Concessionárias (Seminovos)", value=True)
buscar_leiloes = st.sidebar.checkbox("Leilões de Bancos (Recuperados)", value=True)

# Botão de Comando do Robô
st.sidebar.markdown("---")
if st.sidebar.button("▶️ INICIAR MONITORAMENTO TOTAL", use_container_width=True):
    st.sidebar.success("Robô Varrendo SP: Particulares, Lojas e Leilões!")

# --- LÓGICA DE FILTRAGEM ---
df_filtrado = df_original.copy()

# Filtro de Marca e Modelo
if marca_selecionada != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Marca"] == marca_selecionada]
    if modelo_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Modelo"].str.contains(modelo_selecionado, case=False)]

# Filtro de Ano, Preço e KM
df_filtrado = df_filtrado[
    (df_filtrado["Ano"] >= filtro_ano[0]) & 
    (df_filtrado["Ano"] <= filtro_ano[1]) &
    (df_filtrado["Preço (R$)"] <= preco_maximo) &
    (df_filtrado["KM"] <= km_maxima)
]

# Filtro de Origem
fontes_selecionadas = []
if buscar_particulares:
    fontes_selecionadas.append("Sites (Particulares)")
if buscar_lojas:
    fontes_selecionadas.append("Lojas e Concessionárias")
if buscar_leiloes:
    fontes_selecionadas.append("Leilões de Bancos (Recuperados)")

df_filtrado = df_filtrado[df_filtrado["Tipo"].isin(fontes_selecionadas)]

# --- EXIBIÇÃO DOS RESULTADOS ---
st.subheader(f"📋 Oportunidades Filtradas em SP ({len(df_filtrado)})")

if not df_filtrado.empty:
    df_exibicao = df_filtrado.copy()
    df_exibicao["Preço (R$)"] = df_exibicao["Preço (R$)"].map("R$ {:,.2f}".format)
    df_exibicao["KM"] = df_exibicao["KM"].map("{:,} KM".format)
    
    df_exibicao = df_exibicao[["Marca", "Modelo", "Ano", "Preço (R$)", "KM", "Tipo", "Local", "Link"]]
    
    st.data_editor(
        df_exibicao,
        column_config={
            "Link": st.column_config.LinkColumn(
                "Link do Anúncio",
                help="Clique para abrir a oferta original",
                validate=r"^https?://",
                max_chars=100,
                display_text="Ver Anúncio/Lote"
            )
        },
        disabled=True,
        use_container_width=True,
        hide_index=True
    )
else:
    st.warning("Nenhum veículo encontrado com os filtros selecionados em SP.")
