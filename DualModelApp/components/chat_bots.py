import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()

# Function to generate a response using Google Generative AI
def gemini_chat_api(prompt):
    # Configuration
    genai.configure(api_key=os.environ.get("GEMINI_AI_API_KEY"))
    generation_config = {"temperature": 0.25, "max_output_tokens": 1024, "top_k": 40, "top_p": 0.95}
        
    try:
        model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
        chat_session = genai.ChatSession(model=model)  # Initialize chat session
        gemini_response = chat_session.send_message(prompt)

        # Access text using the correct attribute
        generated_text = gemini_response.candidates[0].content.parts[0].text  
        return generated_text
    except genai.exceptions.APIError as api_err:
        # Specific handling for API errors
        st.error("😔 Oops! There was a problem connecting to the AI service. Please try again later.")
        # Log the error if needed for debugging (not shown to the user)
        st.write(api_err)
        return None
    except ValueError as val_err:
        # Handle issues related to invalid values, etc.
        st.error("😥 It seems there was an issue with the input provided. Please check and try again.")
        st.write(val_err)
        return None
    except Exception as e:
        # Generic error handling
        st.error("😥 Something went wrong. Please try again.")
        st.write(e)
        return None

def gemini_chat_oauth(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-chatbot-v2-471btbzagxuv')
        result = model.generate_content(prompt)
        return result.text
    except json.JSONDecodeError as json_err:
        st.error("😥 There was an error processing the response. Please try again later.")
        st.write(json_err)
        return None
    except Exception as e:
        st.error("😥 An unexpected error occurred. Please try again.")
        st.write(e)
        return None

# Set your OpenAI API key from environment variable
openai.api_key = os.environ.get("OPEN_AI_API_KEY") 

# Function to generate a response from OpenAI
def openai_chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    message = response.choices[0].message["content"].strip()
    return message