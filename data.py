# page_four.py

import streamlit as st

def app():
    st.title('Data')

    # Check if persona_data and company_data are available in session state
    if 'persona_data' in st.session_state and 'company_data' in st.session_state:
        persona_data = st.session_state['persona_data']
        company_data = st.session_state['company_data']

        # Format persona data as a plain text string
        persona_data_txt = "\n".join([f"{key}: {value}" for key, value in persona_data.items()])
        company_data_txt = "\n".join([f"{key}: {value}" for key, value in company_data.items()])

        # Display persona and company data using markdown for better readability
        st.text("Persona")
        st.markdown(f"```\n{persona_data_txt}\n```")

        st.text("Company")
        st.markdown(f"```\n{company_data_txt}\n```")

        # Create a single text file content with both persona and company data
        combined_data_txt = f"Persona Data:\n{persona_data_txt}\n\nCompany Data:\n{company_data_txt}"

        # Create a button to download the combined data as a .txt file
        st.download_button(
            label="Download Data",
            data=combined_data_txt,
            file_name='persona_and_company_data.txt',
            mime='text/plain'
        )
    else:
        st.warning("No data found. Please create a user persona first and fill out company information.")

# For testing purposes, you can run this app as a standalone Streamlit app
if __name__ == "__main__":
    app()
