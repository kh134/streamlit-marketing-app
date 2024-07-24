# user_persona.py
import streamlit as st

def app():
    st.title('User Persona')

    # Eingabefelder für grundlegende Informationen der User Persona
    with st.form(key='user_persona_form'):
        altersgruppen = st.selectbox("Alter", ["14-18", "18-25", "26-30", "31-40", "41-50", "51-60", "61-70", "Älter als 70"])
        geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich", "Andere"])
        standort = st.text_input("Standort")
        bildungsniveau = st.selectbox("Bildungsniveau", ["Schüler", "Student", "Berufseinsteiger", "Berufstätig", "Rentner"])
        einkommensniveau = st.selectbox("Einkommensniveau", ["Niedrig", "Mittel", "Hoch"])

        # Psychografische Daten
        interessen = st.text_area("Interessen und Hobbys")
        werte = st.text_area("Werte und Einstellungen")
        lebensstil = st.text_area("Lebensstil")
        persönlichkeitsmerkmale = st.text_area("Persönlichkeitsmerkmale")

        # Verhaltensdaten
        häufigkeit_der_käufe = st.selectbox("Häufigkeit der Käufe", ["Täglich", "Wöchentlich", "Monatlich", "Jährlich"])
        bevorzugte_produktkategorien = st.text_area("Bevorzugte Produktkategorien")
        bevorzugte_plattform = st.text_area("Bevorzugte Plattformen")
        budget = st.slider("Budget", 0, 1000, 100)  # Min, Max, Default
        motivation_ziele = st.text_area("Motivation und Ziele")
        
        # Produktspezifische Informationen 
        markenpraferenzen = st.text_area("Markenpräferenzen")
        stile = st.text_area("Stile")
        produktmerkmale = st.text_area("Produktmerkmale")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("User Persona erstellen")

        if submit_button:
            # Speichern der Persona-Daten im session_state
            st.session_state['persona_data'] = {
                "altersgruppen": altersgruppen,
                "geschlecht": geschlecht,
                "standort": standort,
                "bildungsniveau": bildungsniveau,
                "einkommensniveau": einkommensniveau,
                "interessen": interessen,
                "werte": werte,
                "lebensstil": lebensstil,
                "persönlichkeitsmerkmale": persönlichkeitsmerkmale,
                "häufigkeit_der_käufe": häufigkeit_der_käufe,
                "bevorzugte_produktkategorien": bevorzugte_produktkategorien,
                "bevorzugte_plattform": bevorzugte_plattform,
                "budget": budget,
                "motivation_ziele": motivation_ziele,
                "markenpraferenzen": markenpraferenzen,
                "stile": stile,
                "produktmerkmale": produktmerkmale
            }


            st.success("User Persona erfolgreich erstellt!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
