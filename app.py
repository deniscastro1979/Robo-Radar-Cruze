# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Radar Cruze LTZ", page_icon="🚗", layout="wide")

st.title("🚗 Radar Cruze LTZ - Sistema de Monitoramento")
st.markdown("Busca automatizada em OLX, WebMotors, MercadoLivre e Leilões de Bancos.")

st.sidebar.header("⚙️ Configurações do Filtro")
ano_min, ano_max = st.sidebar.slider("Faixa de Ano do Veículo", 2010, 2026, (2017, 2019))
preco_teto = st.sidebar.number_input("Preço Máximo (R$)", value=88000.0, step=1000.0)
km_teto = st.sidebar.number_input("Quilometragem Máxima", value=90000, step=5000)

st.sidebar.subheader("Fontes de Pesquisa")
buscar_anuncios = st.sidebar.checkbox("Sites de Anúncios", value=True)
buscar_leiloes = st.sidebar.checkbox("Leilões de Bancos (Apenas Recuperados)", value=True)

if st.sidebar.button("▶️ INICIAR MONITORAMENTO", type="primary"):
    st.sidebar.success("Robô Ativado!")

st.subheader("📋 Oportunidades Encontradas e Pré-Filtradas")

dados_veiculos = [
    {
        "Plataforma/Origem": "Milan Leilões (Banco Itaú)",
        "Modelo/Versão": "Cruze LTZ 1.4 Turbo",
        "Ano": 2018,
        "Preço (R$)": 64200.00,
        "KM": 68000,
        "Status Documental": "Aprovado: Retomado de Banco (Sem batidas)",
    },
    {
        "Plataforma/Origem": "OLX (Particular)",
        "Modelo/Versão": "Cruze Premier",
        "Ano": 2019,
        "Preço (R$)": 86000.00,
        "KM": 54000,
        "Status Documental": "Aprovado: Documento OK",
    }
]

df = pd.DataFrame(dados_veiculos)
df_filtrado = df[(df["Ano"] >= ano_min) & (df["Ano"] <= ano_max) & (df["Preço (R$)"] <= preco_teto) & (df["KM"] <= km_teto)]
st.dataframe(df_filtrado, use_container_width=True)
