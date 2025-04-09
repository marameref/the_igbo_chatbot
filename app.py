import streamlit as st
import requests

st.set_page_config(page_title="Igbo Chatbot", page_icon="🤖", layout="centered")

st.title("🧑🏾‍💼 Igbo Chatbot for Office Stationery 🛒")
st.markdown("Talk to the chatbot in Igbo to ask about pens, books, papers, etc.")

# Text input
user_input = st.text_input("You:", placeholder="Ndewo, gịnị ka m nwere ike ịzụta?")

# Display chatbot response
if st.button("Send") and user_input:
    # Call the local FastAPI/Flask backend (Step 4)
    try:
        response = requests.post(
            "http://localhost:8000/chat",  # replace with your actual endpoint
            json={"user_input": user_input}
        )
        if response.status_code == 200:
            reply = response.json()["response"]
            st.markdown(f"**🤖 Chatbot:** {reply}")
        else:
            st.error("Chatbot service returned an error.")
    except Exception as e:
        st.error(f"Connection error: {e}")