import streamlit as st
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

st.title("Que tal estas hoy??")
input = st.text_area("Escribe para analizar:")

if st.button("Send"):
    Responce = sentiment_analysis(input)
    st.write(Responce) 