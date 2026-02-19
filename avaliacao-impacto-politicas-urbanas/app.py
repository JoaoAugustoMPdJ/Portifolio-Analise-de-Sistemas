import streamlit as st
import pandas as pd
from src.pipeline import Pipeline

st.set_page_config(
    page_title="Avaliação de Impacto Urbano",
    layout="wide"
)

st.title("📊 Avaliação de Impacto de Políticas Urbanas")

pipeline = Pipeline()

# =======================
# SIDEBAR / INPUTS
# =======================
st.subheader("Dados")

dominio = st.selectbox(
    "Domínio",
    ["Segurança", "Mobilidade", "Clima"]
)

analise = st.selectbox(
    "Análise",
    ["Exploração", "Impacto"]
)

file = st.file_uploader(
    "Envie o CSV",
    type=["csv"]
)

crime_tipo = None
bairro = None

if dominio == "Segurança":
    crime_tipo = st.text_input("Tipo de crime (opcional)")
    bairro = st.text_input("Bairro (opcional)")

# =======================
# PROCESSAMENTO
# =======================
if file is not None:
    df = pd.read_csv(file, sep=None, engine="python")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Configuração")
        st.write("📌 Domínio selecionado:", dominio)
        st.write("📌 Análise:", analise)
        st.write("📌 Linhas do CSV:", len(df))

    with col2:
        st.markdown("### Resultado")

        result = pipeline.run(
            df=df,
            domain=dominio,
            analysis=analise,
            crime_tipo=crime_tipo,
            bairro=bairro
        )

        if result is None:
            st.error("❌ Dados insuficientes para análise.")

        elif isinstance(result, dict) and "error" in result:
            st.error(result["error"])

        else:
            st.line_chart(result.set_index("data"))
