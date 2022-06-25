# pip install streamlit

import streamlit as st

with st.form(key="Include_cliente"):
    input_name = st.text_input(label="Insira seu nome: ")
    input_age = st.number_input(label="Insira seu nome: ")
    input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor", "Desiner", "Engenheiro"],  )
    input_button_submit = st.form_submit_button("Enviar")