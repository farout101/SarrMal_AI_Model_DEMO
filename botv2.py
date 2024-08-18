import streamlit as st
import google.generativeai as genai
import os
import env

# Configuration
genai.configure(api_key=env.GEMINI_AI_API_KEY)
generation_config = {"temperature": 0.25, "max_output_tokens": 1024, "top_k": 40, "top_p": 0.95}

# Function to generate a response using Google Generative AI
def generate_response(prompt):
    model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
    chat_session = genai.ChatSession(model=model)  # Initialize chat session
    gemini_response = chat_session.send_message(prompt)

   # Access text using the correct attribute (replace 'content.parts[0].text' if needed)
    generated_text = gemini_response.candidates[0].content.parts[0].text  

    return generated_text

# Streamlit app layout
st.title("Mini Chatbot with Gemini AI")
st.write("Ask me anything!")

# Predefined prompts
predefined_prompts = [
    "How to be a Sigma?",
    "What is gay?",
    "Why people gay?",
    "Give me tips for the development of the gay detetion AI model.",
    "Why men are always superior to women?",
    "Why do gay people weak?"
]

# Dropdown for predefined prompts
selected_prompt = st.selectbox("Choose a predefined prompt:", predefined_prompts)

# Predefined custom instructions
custom_instructions = "This is the Chat session about the power ranger."

if st.button("Ask"):
    with st.spinner("Generating response..."):
        response = generate_response(selected_prompt)
        with st.chat_message("user"):
            st.write(selected_prompt)
        with st.chat_message("assistant"):
            st.write(response)

# User input
user_input = st.text_input("You:", "")

col1, col2 = st.columns([9,1])

with col1:
    if st.button("Send"):
        with st.spinner("Generating response..."):
            response = generate_response(user_input)
            with st.chat_message("user"):
                st.write(user_input)
            with st.chat_message("assistant"):
                st.write(response)
                
with col2:
    if st.button("Clear"):
        st.empty()