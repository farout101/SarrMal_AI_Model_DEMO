import streamlit as st
import google.generativeai as genai
import os
import env

# Configuration
genai.configure(api_key=env.GEMINI_AI_API_KEY)
generation_config = {"temperature": 0.25, "max_output_tokens": 1024, "top_k": 40, "top_p": 0.95}

# Function to generate a response using Google Generative AI
def generate_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
        chat_session = genai.ChatSession(model=model)  # Initialize chat session
        gemini_response = chat_session.send_message(prompt)

        # Access text using the correct attribute
        generated_text = gemini_response.candidates[0].content.parts[0].text  
        return generated_text
    except Exception as e:
        return f"An error occurred: {e}"

# Function to display chat messages
def display_chat_message(role, message):
    with st.chat_message(role):
        st.write(message)

# Streamlit app layout
st.title("Mini Chatbot with Gemini AI")
st.write("Ask me anything!")

# Predefined prompts
predefined_prompts = [
    "How to be a Sigma?",
    "What is gay?",
    "Why people gay?",
    "Give me tips for the development of the gay detection AI model.",
    "Why men are always superior to women?",
    "Why do gay people weak?"
]

# Dropdown for predefined prompts
selected_prompt = st.selectbox("Choose a predefined prompt:", predefined_prompts)

# Predefined custom instructions
custom_instructions = "This is a chat session about Power Rangers."

# Container for chat messages
chat_container = st.container()

# Handle predefined prompt
if st.button("Ask"):
    with st.spinner("Generating response..."):
        full_prompt = f"{custom_instructions} {selected_prompt}"
        response = generate_response(full_prompt)
        with chat_container:
            display_chat_message("user", selected_prompt)
            display_chat_message("assistant", response)

# User input
user_input = st.text_input("You:", "")

col1, col2 = st.columns([9, 1])

# Handle user input
with col1:
    if st.button("Send"):
        if user_input:
            with st.spinner("Generating response..."):
                response = generate_response(f"{custom_instructions} {user_input}")
                with chat_container:
                    display_chat_message("user", user_input)
                    display_chat_message("assistant", response)
        else:
            st.warning("Please enter a message before sending.")

# Handle clear action
with col2:
    if st.button("Clear"):
        st.session_state.clear()