import streamlit as st
import pandas as pd
import os

# Configuración de la página
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

# Ruta al CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "habitamadrid_dataset_final.csv"
)

# Leer CSV
df = pd.read_csv(csv_path)

# Mostrar dataset
st.subheader("Dataset completo")
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
