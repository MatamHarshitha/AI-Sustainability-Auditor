


import streamlit as st
import pandas as pd

st.title("Sustainability Dashboard")

df = pd.read_csv("data/processed/final_output.csv")

st.metric("Total CO2", df["co2_kg"].sum().round(2))
st.bar_chart(df.groupby("predicted_scope")["co2_kg"].sum())
st.title("Vendor Dashboard")
if "vendor" in df.columns:
    st.bar_chart(df.groupby("vendor")["co2_kg"].sum())

st.dataframe(df)



