import streamlit as st
import pandas as pd

st.title("HabitaMadrid")

df = pd.read_csv("../data/habitamadrid_dataset_final.csv")

st.dataframe(df)
