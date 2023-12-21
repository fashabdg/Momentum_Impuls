import streamlit as st
import pandas as pd

# Display Title and Description
st.title("Test Momentum dan Impuls")
st.markdown("Enter the details of the new test below.")

url = "https://docs.google.com/spreadsheets/d/1ULklRn3sur4FGOYbI4uJ_-IJS7LjRkxUSVtXJxA5YGE/edit?usp=sharing"

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing vendors data
existing_data = conn.read(usecols=list(range(3)), worksheet="test")
existing_data = existing_data.dropna(how="all")

# Fetch existing vendors data
st.dataframe(existing_data)

# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    name = st.text_input(label="Nama lengkap*")
    email = st.text_input(label="Email*")
    institusi = st.text_input(label="Institusi*")

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
                        "Institusi": institusi,
                    }
                ]
            )

            # Add the new vendor data to the existing data
            updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

            st.dataframe(updated_df)

            url = "https://docs.google.com/spreadsheets/d/1ULklRn3sur4FGOYbI4uJ_-IJS7LjRkxUSVtXJxA5YGE/edit?usp=sharing"

            # Update Google Sheets with the new vendor data
            conn.update(worksheet="test", data=updated_df)

            st.success("test momentum impuls successfully submitted!")
            
def display_quiz():
    questions = [
        "Sebuah benda yang mempunyai massa 100 gram bergerak lurus dengan kecepatan 10 m/s dan percepatan 2 m/s? Perubahan momentum benda setelah bergerak 5 sekon adalah... ",
        "Sebuah truk bermassa 2000 kg dan melaju dengan kecepatan 36 km/jam menabrak sebuah pohon dan berhenti dalam waktu 0,1 detik. Gaya rata-rata pada truk selama berlangsungnya tabrakan adalah....N",
        "Seorang nelayan naik perahu yang bergerak dengan kecepatan 4 m/s. Massa perahu dan orang masing-masing 200 kg dan 50 kg. Pada suatu saat, orang tadi meloncat dari perahu dengan kecepatan 8 m/s searah gerak perahu maka kecepatan perahu sesaat setelah orang tadi meloncat adalah...",
        "Sebuah perluru bermassa 100gram ditembakkan dengan kecepatan v pada sebuah balok yang bermassa 0,9 kg yang dilkatkan pada seutas tali, kemudian peluru menancap pada balok dan naik setinggi 0,8 m. Tentukan nilai dari v!",
        "Sebuah benda jatuh bebas dari ketinggian 80 m di atas tanah. Jika tumbukan yang terjadi dengan tanah adalah elastis sebagian (e = 0,2), kecepatan pantul benda setelah tumbukan adalah..."
    ]

    options = [
        ["3 kg*m/s", "2 kg*m/s", "1 kg*m/s", "4 kg*m/s"],
        ["200,000 N", "320,000 N", "360,000 N", "240,000 N"],
        ["1.5 m/s", "2.0 m/s", "2.5 m/s", "3.0 m/s"],
        ["4.0 m/s", "6.0 m/s", "8.0 m/s", "10.0 m/s"],
        ["6 m/s", "8 m/s", "10 m/s", "12 m/s"]
    ]

    answers = ("C", "A", "D", "A", "B")
    guesses = []
    score = 0

    st.header("Quiz Time!")
    for i, question in enumerate(questions):
        st.write(f"**Question {i + 1}:** {question}")
        for option in options[i]:
            st.write(option)

        guess = st.radio(f"Enter your answer for Question {i + 1} (A, B, C, D):", ('A', 'B', 'C', 'D'))
        guesses.append(guess.upper())
        if guess.upper() == answers[i]:
            score += 1

    if st.button("Submit"):
        st.header("Results")
        st.write("Answers: ", " ".join(answers))
        st.write("Your guesses: ", " ".join(guesses))

        final_score = int(score / len(questions) * 100)
        st.write(f"Your score is: {final_score}%")

def main():
    st.title("Simple Quiz App")
    display_quiz()

if __name__ == "__main__":
    main()
