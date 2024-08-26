import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPEN_AI_API_KEY")

# Function to generate a response from OpenAI
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    message = response.choices[0].message["content"].strip()
    return message

# Streamlit app layout
st.title("Mini Chatbot with OpenAI")
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
