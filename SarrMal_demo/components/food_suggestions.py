import openai
import json
import streamlit as st
import openai
import google.generativeai as genai
import os
        
# This is the unused function to generate responses using openAI api
def generate_openai(prompt):
    """
    Generates a food suggestion using the OpenAI GPT model.

    Parameters:
    - prompt (str): The JSON string containing user details like weight, height, age, etc.

    Returns:
    - dict: A dictionary containing the meal plan.
    - None: If there is an error in processing the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a meal planner AI, and you'll strictly need to respond with the JSON format that I provided earlier. THE OUTPUT IS JSON FORMAT"},
                {"role": "user", "content": """{
                    "weight": 70,
                    "height": 180,
                    "age": 30,
                    "diseases": ["None"],
                    "allergies": ["None"],
                    "gender": "Male",
                    "exercise": "High"
                    "preferred": ["None"],
                    "food type": ["Healthy"]
                }"""},
                {"role": "assistant", "content": """{
                "response": {
                    "breakfast": {
                    "main_dish": {
                        "name": "Oatmeal with Fresh Berries",
                        "calories": 350,
                        "category": "Healthy",
                        "ingredients": ["Oats", "Milk", "Strawberries", "Blueberries", "Honey"],
                        "how_to_cook": "Combine oats with milk and cook over medium heat until thickened. Top with fresh berries and a drizzle of honey.",
                        "meal_time": "07:00 AM"
                    },
                    "side_dish": {
                        "name": "Greek Yogurt with Almonds",
                        "calories": 150,
                        "category": "Protein",
                        "ingredients": ["Greek Yogurt", "Almonds", "Honey"],
                        "how_to_cook": "Top Greek yogurt with chopped almonds and a drizzle of honey.",
                        "meal_time": "07:00 AM"
                    }
                    },
                    "lunch": {
                    "main_dish": {
                        "name": "Grilled Chicken Salad",
                        "calories": 450,
                        "category": "Protein",
                        "ingredients": ["Chicken Breast", "Mixed Greens", "Cherry Tomatoes", "Cucumber", "Olive Oil", "Lemon Juice"],
                        "how_to_cook": "Grill chicken breast until fully cooked, then slice. Toss with mixed greens, cherry tomatoes, cucumber, and a dressing of olive oil and lemon juice.",
                        "meal_time": "12:00 PM"
                    },
                    "side_dish": {
                        "name": "Quinoa Salad",
                        "calories": 200,
                        "category": "Grain",
                        "ingredients": ["Quinoa", "Black Beans", "Corn", "Red Bell Pepper", "Lime Juice", "Cilantro"],
                        "how_to_cook": "Cook quinoa according to package instructions. Mix with black beans, corn, diced red bell pepper, lime juice, and cilantro.",
                        "meal_time": "12:00 PM"
                    }
                    },
                    "dinner": {
                    "main_dish": {
                        "name": "Baked Salmon",
                        "calories": 500,
                        "category": "Protein",
                        "ingredients": ["Salmon Fillets", "Lemon", "Dill", "Olive Oil"],
                        "how_to_cook": "Place salmon fillets on a baking sheet, brush with olive oil, and season with lemon and dill. Bake at 375°F (190°C) for 15-20 minutes.",
                        "meal_time": "07:00 PM"
                    },
                    "side_dish": {
                        "name": "Steamed Broccoli",
                        "calories": 55,
                        "category": "Vegetable",
                        "ingredients": ["Broccoli Florets"],
                        "how_to_cook": "Steam broccoli florets until tender, about 5 minutes. Season with a pinch of salt if desired.",
                        "meal_time": "07:00 PM"
                    }
                    }
                }
                }"""},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": "..."}
            ]
        )
        completion_content = response['choices'][0]['message']['content']
        response_json = json.loads(completion_content)
        return response_json
    except json.JSONDecodeError as json_err:
        st.error("😥 There was an error processing the response. Please try again later.")
        # st.write(json_err)
        return None
    except Exception as e:
        st.error("😥 An unexpected error occurred. Please try again.")
        # st.write(e)
        return None    
    

# Food Suggestion AI model for SarrMal API (Version 1)
def generate_gemini(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-suggestion-ai-v1-uss801z982xp')
        result = model.generate_content(prompt)
        response = json.loads(result.text)
        return response
    except json.JSONDecodeError as json_err:
        st.error("😥 There was an error processing the response. Please try again later.")
        # print("There was an error processing the response. Please try again later.")
        # print(json_err)
        return None
    except Exception as e:
        st.error("😥 An unexpected error occurred. Please try again.")
        # st.write(e)
        return None
    
# The main difference between between Version 1 and 3 is the input format and the training data
# Food Suggestion AI model for SarrMal API (Version 3, also the final version)
def generate_gemini_v3(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-suggestion-ai-v3-t2z0eh7qpaq8')
        result = model.generate_content(prompt)
        cleaned_result = result.text.strip("```json").strip("```")
        data = json.loads(cleaned_result)
        return data
    except json.JSONDecodeError as json_err:
        st.error("😥 There was an error processing the response. Please try again later.")
        # print("There was an error processing the response. Please try again later.")
        # print(json_err)
        return None
    except Exception as e:
        st.error("😥 An unexpected error occurred. Please try again.")
        # st.write(e)
        return None
    
def suggestion_from_image(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/final-food-analysis-v1-kva230h5vrbk')
        result = model.generate_content(prompt)
        response = result.text
        return response
    except json.JSONDecodeError as json_err:
        st.error("😥 There was an error processing the response. Please try again later.")
        # print("There was an error processing the response. Please try again later.")
        # print(json_err)
        return None
    except Exception as e:
        st.error("😥 An unexpected error occurred. Please try again.")
        # st.write(e)
        return None

#For testing the models    
  
# print(suggestion_from_image("Egg fried Rice")) 
    
# print(generate_gemini("""{
#                 "weight": 80,
#                 "height": 140,
#                 "age": 30,
#                 "diseases": "Diabetes, hyptertension",
#                 "allergies": "peanut, milk",
#                 "gender": "male",
#                 "exercise": "moderate",
#             }"""))

# print(generate_gemini_v3("""{
#         "weight": 80,
#         "height": 140,
#         "age": 40,
#         "diseases": ["Diabetes","hyptertension"],   
#         "allergies": ["Shell Fish"],
#         "gender": "male",
#         "exercise": "moderate",
#         "preferred": "Burmese",
#         "food-type": "Vegetarian",
#     }"""))

# print(suggestion_from_image("Egg fried Rice"))