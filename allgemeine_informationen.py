import streamlit as st

def app():
    st.title("Allgemeine Informationen")
    
    st.write("""
        Der Chatbot der Streamlit App unterstützt dich bei der Erstellung von visuellen Inhalten (Werbebanner), die für die bestimmten Zielgruppen von Zalando optimiert sind. 
        Diese Inhalte sind auf Kundenpräferenzen und aktuellen Trends zugeschnitten. Es ermöglicht, Werbebanner für Zalando zu erstellen, die nicht nur visuell ansprechend sind, 
        sondern auch für SEO und SEA optimiert werden können.
    """)

    st.subheader("So funktioniert die App")
    st.write("""
        Die App nutzt künstliche Intelligenz, um visuelle Inhalte zu generieren, die speziell auf die Vorlieben und Trends deiner Zielgruppe zugeschnitten sind. 
        Sie besteht aus mehreren Seiten, die du über die Navigation auf der linken Seite erreichen kannst.
        Durch die Eingabe aller nötigen Informationen, wie Zielgruppendefinition und Unternehmensinformationen, kann die App personalisierte Werbebanner erstellen. Speichere alle Daten über den Button in der App, um die bestmöglichen Ergebnisse zu erzielen. Navigiere dann zur nächsten Seite. 
        
        Für die Erstellung der Werbebanner wird ein OpenAI-Modell verwendet, das auf den eingegebenen Informationen basiert. Du musst dafür keinen Prompt schreiben, es reicht, die benötigten Informationen in der App einzugeben.
        Über den Chatbot am Ende der App, werden die Werbebanner generiert udn du kannst du mit dem OpenAI-Modell interagieren, sowie die generierten Werbebanner anpassen.
    
        Um optimale Ergebnisse zu erzielen, benötigt die App folgende Daten:
        - Zielgruppendefinition (Alter, Geschlecht, Interessen) in Form einer User Persona
        - Aktuelle Trends und Präferenzen der Zielgruppe
        - Unternehmensspezifische Informationen und Anforderungen
    
    """)
    
