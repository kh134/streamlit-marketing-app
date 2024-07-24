 # Importing required packages
import streamlit as st
import user_persona
import company_info
import openai_model
import data
import allgemeine_informationen

# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Allgemeine Informationen": allgemeine_informationen,
    "Zielgruppe": user_persona,
    "Unternehmensinformationen": company_info,
    "Data": data,
    "OpenAI Model": openai_model,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()