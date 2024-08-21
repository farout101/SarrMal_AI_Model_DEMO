import streamlit as st
import google.generativeai as genai
import os
import env

# Configuration
genai.configure(api_key=env.GEMINI_AI_API_KEY, transport='grpc')

# Function to generate a food suggestion based on user input
def generate_food_suggestion(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-suggestion-ai-v1-uss801z982xp')
        result = model.generate_content(prompt)
        
        # Accessing the generated content
        return result.text
    except genai.exceptions.APIError as api_err:
        st.error("Oops! There was a problem connecting to the AI service. Please try again later.")
        st.write(api_err)
        return None
    except ValueError as val_err:
        st.error("It seems there was an issue with the input provided. Please check and try again.")
        st.write(val_err)
        return None
    except Exception as e:
        st.error("Something went wrong. Please try again.")
        st.write(e)
        return None

# Streamlit app layout
st.title("AI-Powered Food Suggestion Chatbot")
st.write("Get personalized food suggestions based on your profile!")

# User input fields for generating the food suggestion prompt
st.subheader("Your Details")
weight = st.number_input("Weight (kg)", min_value=1, max_value=300, value=70)
height = st.number_input("Height (cm)", min_value=30, max_value=250, value=175)
age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
exercise = st.selectbox("Exercise Level", ["None", "Light", "Moderate", "Intense"])

diseases = st.text_area("List any diseases (comma-separated)", "None")
allergies = st.text_area("List any allergies (comma-separated)", "Peanuts")

# Generate the prompt based on user input
prompt = f"""{{
    "weight": {weight},
    "height": {height},
    "age": {age},
    "diseases": [{', '.join([f'"{disease.strip()}"' for disease in diseases.split(',')])}],
    "allergies": [{', '.join([f'"{allergy.strip()}"' for allergy in allergies.split(',')])}],
    "gender": "{gender}",
    "exercise": "{exercise}"
}}"""

st.write("### Generated Prompt")
st.code(prompt)

# Container for displaying the chat messages
chat_container = st.container()

# Button to generate and display the food suggestion
if st.button("Get Food Suggestion"):
    with st.spinner("Generating food suggestion..."):
        response = generate_food_suggestion(prompt)
        with chat_container:
            if response:
                st.subheader("Suggested Food Plan")
                st.write(response)
            else:
                st.warning("No response generated. Please check your input or try again later.")

# Button to clear the chat
if st.button("Clear"):
    st.session_state.clear()

