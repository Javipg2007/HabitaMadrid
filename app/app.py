import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="HabitaMadrid",
    page_icon="🏠",
    layout="wide"
)

# Título
st.title("🏠 HabitaMadrid")

st.write(
    "Sistema de recomendación de municipios de la Comunidad de Madrid."
)

# Leer dataset
df = pd.read_csv("../data/habitamadrid_dataset_final.csv")

# Mostrar datos
st.subheader("Dataset")

st.dataframe(df)

# Ranking
st.subheader("Ranking actual")

ranking = df.sort_values(
    by="score_final",
    ascending=False
)

st.dataframe(
    ranking[["municipio", "score_final"]]
)
