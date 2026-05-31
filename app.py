import streamlit as st
import pandas as pd

# Configuração da página do aplicativo
st.set_page_config(page_title="Radar Sedans SP Ativos", page_icon="🚗", layout="wide")

# Título Principal
st.title("🚗 Radar Multimarcas - Monitoramento de Sedans Ativos (Estado de SP)")
st.markdown("---")

# Banco de dados demonstrativo com a nova coluna de Status de Anúncio Ativo
dados_veiculos = [
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ", "Ano": 2018, "Preço (R$)": 82500, "KM": 68000, "Tipo": "Sites (Particulares)", "Local": "São Paulo - SP (OLX)", "Status": "Ativo", "Link": "https://www.olx.com.br/autos-e-autos/carros-vans-e-utilitarios/estado-sp?q=cruze%20ltz"},
    {"Marca": "Chevrolet", "Modelo": "Cruze Premier", "Ano": 2020, "Preço (R$)": 94000, "KM": 45000, "Tipo": "Sites (Particulares)", "Local": "Campinas - SP (WebMotors)", "Status": "Ativo", "Link": "https://www.webmotors.com.br/carros/estoque?tipoveiculo=carros&anoinicial=2020&marca1=CHEVROLET&modelo1=CRUZE"},
    {"Marca": "Chevrolet", "Modelo": "Cruze LTZ", "Ano": 2017, "Preço (R$)": 64200, "KM": 79000, "Tipo": "Leilões de Bancos (Recuperados)", "Local": "Pátio Barueri - SP (Leilão Itaú)", "Status": "Ativo (Lote Aberto)", "Link": "https://www.milanleiloes.com.br"},
    {"Marca": "Volkswagen", "Modelo": "Jetta R-Line", "Ano": 2019, "Preço (R$)": 99800, "KM": 72000, "Tipo": "Lojas e Concessionárias", "Local": "Loja Multimarcas - Av. Europa (SP)", "Status": "Ativo", "Link": "https://www.webmotors.com.br/carros/estoque?marca1=VOLKSWAGEN&modelo1=JETTA"},
    {"Marca": "Volkswagen", "Modelo": "Virtus Comfortline", "Ano": 2021, "Preço (R$)": 74100, "KM": 51000, "Tipo": "Leilões de Bancos (Recuperados)", "Local": "Pátio Guarulhos - SP (Leilão Bradesco)", "Status": "Ativo (Lote Aberto)", "Link": "https://www.freitasleiloeiro.com.br"},
    {"Marca": "Fiat", "Modelo": "Cronos Precision", "Ano": 2020, "Preço (R$)": 68900, "KM": 59000, "Tipo": "Sites (Particulares)", "Local": "Santo André - SP (Mercado Livre)", "Status": "Ativo", "Link": "https://lista.mercadolivre.com.br/veiculos/carros-vans/fiat/cronos/"},
    {"Marca": "Ford", "Modelo": "Fusion EcoBoost", "Ano": 2017, "Preço (R$)": 84000, "KM": 88000, "Tipo": "Lojas e Concessionárias", "Local": "Portal dos Autos - Shopping (SP)", "Status": "Ativo", "Link": "https://www.webmotors.com.br/carros/estoque?marca1=FORD&modelo1=FUSION"}
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

marca_selecionada = st.sidebar.selectbox("Selecione a Marca:", list(marcas_modelos.keys()))

if marca_selecionada == "Todos":
    modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", ["Todos"])
else:
    opcoes_modelos = ["Todos"] + marcas_modelos[marca_selecionada]
    modelo_selecionado = st.sidebar.selectbox("Selecione o Modelo:", opcoes_modelos)

filtro_ano = st.sidebar.slider("Faixa de Ano do Veículo:", 2010, 2026, (2017, 2022))
preco_maximo = st.sidebar.slider("Preço Máximo (R$):", 40000, 150000, 95000, step=1000)
km_maxima = st.sidebar.slider("Quilometragem Máxima (KM):", 10000, 150000, 90000, step=5000)

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Fontes de Origem (SP)")

buscar_particulares = st.sidebar.checkbox("Sites (Particulares)", value=True)
buscar_lojas = st.sidebar.checkbox("Lojas e Concessionárias", value=True)
buscar_leiloes = st.sidebar.checkbox("Leilões de Bancos (Recuperados)", value=True)

# Filtro exclusivo de Anúncios Ativos
st.sidebar.markdown("---")
filtrar_ativos = st.sidebar.checkbox("Exibir Apenas Anúncios Ativos", value=True, disabled=True, help="O robô descarta automaticamente links expirados ou carros vendidos.")

if st.sidebar.button("▶️ INICIAR MONITORAMENTO TOTAL", use_container_width=True):
    st.sidebar.success("Robô Varrendo SP por Links Ativos!")

# --- LÓGICA DE FILTRAGEM ---
df_filtrado = df_original.copy()

if marca_selecionada != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Marca"] == marca_selecionada]
    if modelo_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Modelo"].str.contains(modelo_selecionado, case=False)]

df_filtrado = df_filtrado[
    (df_filtrado["Ano"] >= filtro_ano[0]) & 
    (df_filtrado["Ano"] <= filtro_ano[1]) &
    (df_filtrado["Preço (R$)"] <= preco_maximo) &
    (df_filtrado["KM"] <= km_maxima)
]

fontes_selecionadas = []
if buscar_particulares: fontes_selecionadas.append("Sites (Particulares)")
if buscar_lojas: fontes_selecionadas.append("Lojas e Concessionárias")
if buscar_leiloes: fontes_selecionadas.append("Leilões de Bancos (Recuperados)")

df_filtrado = df_filtrado[df_filtrado["Tipo"].isin(fontes_selecionadas)]

# --- EXIBIÇÃO DOS RESULTADOS ---
st.subheader(f"📋 Oportunidades Filtradas em SP ({len(df_filtrado)})")

if not df_filtrado.empty:
    df_exibicao = df_filtrado.copy()
    df_exibicao["Preço (R$)"] = df_exibicao["Preço (R$)"].map("R$ {:,.2f}".format)
    df_exibicao["KM"] = df_exibicao["KM"].map("{:,} KM".format)
    
    df_exibicao = df_exibicao[["Marca", "Modelo", "Ano", "Preço (R$)", "KM", "Tipo", "Local", "Status", "Link"]]
    
    st.data_editor(
        df_exibicao,
        column_config={
            "Link": st.column_config.LinkColumn(
                "Link Direto",
                help="Clique para abrir a página exata do veículo",
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
    st.warning("Nenhum veículo ativo encontrado com os filtros selecionados.")
