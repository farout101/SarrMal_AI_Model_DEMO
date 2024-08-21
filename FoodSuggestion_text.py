import streamlit as st
import google.generativeai as genai
import os
import json
import env

UNSPLASH_ACCESS_KEY = env.UNSPLASH_ACCESS_KEY
#This is a Tuned Gemini Modela and No Gemini API key is required for this model!!

# Function to generate a food suggestion based on user input
def generate_food_suggestion(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-suggestion-ai-v1-uss801z982xp')
        result = model.generate_content(prompt)
        
        # Parse the JSON response
        response = json.loads(result.text)
        return response
    except json.JSONDecodeError as json_err:
        st.error("There was an error processing the response. Please try again later.")
        st.write(json_err)
        return None
    except Exception as e:
        st.error("An unexpected error occurred. Please try again.")
        st.write(e)
        return None

# Function to display the meal plan
def display_meal_plan(response):
    if response:
        st.subheader("Meal Plan")
        
        for meal_time, meal_info in response['response'].items():
            st.write(f"### {meal_time.capitalize()}")
            main_dish = meal_info.get("main_dish", {})
            side_dish = meal_info.get("side_dish", {})

            if main_dish:
                st.write(f"**Main Dish:** {main_dish.get('name')}")
                st.write(f"- Calories: {main_dish.get('calories')} kcal")
                st.write(f"- Category: {main_dish.get('category')}")
                st.write(f"- Ingredients: {main_dish.get('ingredients')}")
                st.write(f"- How to Cook: {main_dish.get('how_to_cook')}")
                st.write(f"- Meal Time: {main_dish.get('meal_time')}")
            
            if side_dish:
                st.write(f"**Side Dish:** {side_dish.get('name')}")
                st.write(f"- Calories: {side_dish.get('calories')} kcal")
                st.write(f"- Category: {side_dish.get('category')}")
                st.write(f"- Ingredients: {side_dish.get('ingredients')}")
                st.write(f"- How to Cook: {side_dish.get('how_to_cook')}")
                st.write(f"- Meal Time: {side_dish.get('meal_time')}")
            st.write("\n")

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
                display_meal_plan(response)
            else:
                st.warning("No response generated. Please check your input or try again later.")

# Button to clear the chat
if st.button("Clear"):
    st.session_state.clear()
