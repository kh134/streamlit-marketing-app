# company_info.py
import streamlit as st

def app():
    st.title('Unternehmensinformationen')

    # Eingabefelder für Unternehmensdaten
    with st.form(key='company_info_form'):
        unternehmensname = st.text_input("Unternehmensname", "Zalando")
        branche = st.text_input("Branche", "Online Mode und Lifestyle Einzelhandel")
        groesse = st.selectbox("Unternehmensgröße", ["Kleinunternehmen", "Mittelständisch", "Großunternehmen"], index=2)

        # Informationen zu USPs und Zielen
        usps = st.text_area("USPs (Unique Selling Points)", "Breites Sortiment an Modeartikeln, kostenfreie Lieferung und Rücksendung, personalisierte Einkaufserlebnisse, Nachhaltigkeitsinitiativen")
        unternehmensziel = st.text_area("Unternehmensziele", "Steigerung des Umsatzes, Erhöhung der Markenbekanntheit, Verbesserung der Kundenzufriedenheit")
        ziele = st.text_area("Zielsetzungen der Kampagne", "Verschiedene Werbebanner für verschiedene Zielgruppen (Männer, Frauen, Sport, etc.). Die Nutzung von GenAI ermöglicht es, Werbebanner für Zalando zu erstellen, die nicht nur visuell ansprechend sind, sondern auch für SEO und SEA optimiert werden können. Durch die Anpassung an Zielgruppen und Trends sowie die Integration von SEO-optimierten Texten und Designs können die Werbebanner effektivere Ergebnisse erzielen und die Marketingziele unterstützen.")

        # Informationen zur Markenpersönlichkeit
        vision = st.text_area("Unternehmensvision", "Die führende Online-Plattform für Mode und Lifestyle in Europa zu sein.")
        mission = st.text_area("Unternehmensmission", "Kunden ein einzigartiges Einkaufserlebnis zu bieten, das durch eine breite Auswahl an Modeartikeln, personalisierte Empfehlungen und nachhaltige Initiativen geprägt ist.")
        markenpersoenlichkeit = st.text_area("Markenpersönlichkeit und -werte", "Modern, Trendbewusst, Kundenorientiert, Nachhaltig")
        
        # Informationen zu Hauptzielgruppen
        hauptzielgruppen = st.text_area("Hauptzielgruppen des Unternehmens", "Modebewusste Konsumenten, junge Erwachsene, Familien, Sportbegeisterte")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Unternehmensdaten speichern")

        if submit_button:
            # Speichern der Unternehmensdaten im session_state
            st.session_state['company_data'] = {
                "unternehmensname": unternehmensname,
                "branche": branche,
                "groesse": groesse,
                "usps": usps,
                "unternehmensziel": unternehmensziel,
                "ziele": ziele,
                "vision": vision,
                "mission": mission,
                "markenpersoenlichkeit": markenpersoenlichkeit,
                "hauptzielgruppen": hauptzielgruppen
            }

            st.success("Unternehmensdaten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()

