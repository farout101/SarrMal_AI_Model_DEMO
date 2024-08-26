import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
genai.configure(api_key=os.environ.get("GEMINI_AI_API_KEY"))
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
    except genai.exceptions.APIError as api_err:
        # Specific handling for API errors
        st.error("Oops! There was a problem connecting to the AI service. Please try again later.")
        # Log the error if needed for debugging (not shown to the user)
        st.write(api_err)
        return None
    except ValueError as val_err:
        # Handle issues related to invalid values, etc.
        st.error("It seems there was an issue with the input provided. Please check and try again.")
        st.write(val_err)
        return None
    except Exception as e:
        # Generic error handling
        st.error("Something went wrong. Please try again.")
        st.write(e)
        return None