import streamlit as st

from transformers import pipeline

generation = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

st.title("Asistente")

preguntas = st.text_input("realiza tu pregunta:")


if st.button("send"):
    promp = f"Contexto: eres un asistente que responde preguntas sencillas:\nPregunta: {preguntas}\nRespuesta:"
    result = generation(promp, max_length=150, num_return_sequences=1)
    st.write(result[0]['generated_text'].split("Respuesta:")[1].strip())