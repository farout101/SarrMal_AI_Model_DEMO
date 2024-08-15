import streamlit as st
import requests
import os
import env

# Set your Gemini AI API key from environment variable
gemini_api_key = env.GEMINI_AI_API_KEY
gemini_endpoint = "https://api.gemini-ai.com/v1/chat/completions"  # Hypothetical endpoint

# Function to generate a response from Gemini AI
def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {gemini_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemini-turbo",  # Replace with the actual model name
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(gemini_endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        message = response_data["choices"][0]["message"]["content"].strip()
        return message
    else:
        return "Failed to get a response from Gemini AI."

# Streamlit app layout
st.title("Mini Chatbot with Gemini AI")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        with st.spinner("Generating response..."):
            response = generate_response(user_input)
            st.write(f"Bot: {response}")
    else:
        st.write("Please enter a message.")
