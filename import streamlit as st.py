import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Test Momentum dan Impuls")
st.markdown("Enter the details of the new test below.")

url = "https://docs.google.com/spreadsheets/d/1IvnQQyp6BdZrqvSkW1YHHwmHTLRnaieHyf3L8T5P6hk/edit"

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing vendors data
existing_data = conn.read(spreadsheet=url, usecols=list(range(3)), worksheet="2132402324")
existing_data = existing_data.dropna(how="all")

# Fetch existing vendors data



# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    name = st.text_input(label="Nama lengkap*")
    email = st.text_input(label="Email*")
    institut_name = st.text_input(label="Institut*")

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit")

    # If the submit button is pressed
    if submit_button:
# Check if all mandatory fields are filled
        if not name or not email:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        elif existing_data["Nama"].str.contains(name).any():
            st.warning("A vendor with this name already exists.")
            st.stop()
        else:
            # Create a new row of vendor data
            vendor_data = pd.DataFrame(
                [
                    {
                        "Nama": name,
                        "Email": email,
                        "Institusi": institut_name,
                    }
                ]
            )

            # Add the new vendor data to the existing data
            updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

            # Update Google Sheets with the new vendor data
            conn.update(spreadsheet=url, worksheet="2132402324", data=updated_df)

            st.success("test momentum impuls successfully submitted!")

            # Add the new vendor data to the existing data