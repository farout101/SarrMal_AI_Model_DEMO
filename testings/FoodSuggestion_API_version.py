from Apps import env
import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

# Configure the API key
genai.configure(api_key=env.GEMINI_AI_API_KEY)

# Create the model configuration
generation_config = {
    "temperature": 0.1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_schema": content.Schema(
        type=content.Type.OBJECT,
        properties={
            "response": content.Schema(
                type=content.Type.OBJECT,
                properties={
                    "breakfast": content.Schema(
                        type=content.Type.OBJECT,
                        required=["name", "calories", "category", "ingredients"],
                        properties={
                            "main_dish": content.Schema(
                                type=content.Type.OBJECT,
                                properties={
                                    "name": content.Schema(type=content.Type.STRING),
                                    "calories": content.Schema(type=content.Type.NUMBER),
                                    "category": content.Schema(type=content.Type.STRING),
                                    "ingredients": content.Schema(
                                        type=content.Type.ARRAY,
                                        items=content.Schema(type=content.Type.STRING),
                                    ),
                                    "how_to_cook": content.Schema(type=content.Type.STRING),
                                    "meal_time": content.Schema(type=content.Type.STRING),
                                },
                            ),
                            "side_dish": content.Schema(
                                type=content.Type.OBJECT,
                                properties={
                                    "name": content.Schema(type=content.Type.STRING),
                                    "calories": content.Schema(type=content.Type.NUMBER),
                                    "category": content.Schema(type=content.Type.STRING),
                                    "ingredients": content.Schema(
                                        type=content.Type.ARRAY,
                                        items=content.Schema(type=content.Type.STRING),
                                    ),
                                    "how_to_cook": content.Schema(type=content.Type.STRING),
                                    "meal_time": content.Schema(type=content.Type.STRING),
                                },
                            ),
                        },
                    ),
                    "lunch": content.Schema(
                        type=content.Type.OBJECT,
                        required=["name", "calories", "category", "ingredients"],
                        properties={
                            "main_dish": content.Schema(
                                type=content.Type.OBJECT,
                                properties={
                                    "name": content.Schema(type=content.Type.STRING),
                                    "calories": content.Schema(type=content.Type.NUMBER),
                                    "category": content.Schema(type=content.Type.STRING),
                                    "ingredients": content.Schema(
                                        type=content.Type.ARRAY,
                                        items=content.Schema(type=content.Type.STRING),
                                    ),
                                    "how_to_cook": content.Schema(type=content.Type.STRING),
                                    "meal_time": content.Schema(type=content.Type.STRING),
                                },
                            ),
                            "side_dish": content.Schema(
                                type=content.Type.OBJECT,
                                properties={
                                    "name": content.Schema(type=content.Type.STRING),
                                    "calories": content.Schema(type=content.Type.NUMBER),
                                    "category": content.Schema(type=content.Type.STRING),
                                    "ingredients": content.Schema(
                                        type=content.Type.ARRAY,
                                        items=content.Schema(type=content.Type.STRING),
                                    ),
                                    "how_to_cook": content.Schema(type=content.Type.STRING),
                                    "meal_time": content.Schema(type=content.Type.STRING),
                                },
                            ),
                        },
                    ),
                    "dinner": content.Schema(
                        type=content.Type.OBJECT,
                        required=["name", "calories", "category", "ingredients"],
                        properties={
                            "main_dish": content.Schema(
                                type=content.Type.OBJECT,
                                properties={
                                    "name": content.Schema(type=content.Type.STRING),
                                    "calories": content.Schema(type=content.Type.NUMBER),
                                    "category": content.Schema(type=content.Type.STRING),
                                    "ingredients": content.Schema(
                                        type=content.Type.ARRAY,
                                        items=content.Schema(type=content.Type.STRING),
                                    ),
                                    "how_to_cook": content.Schema(type=content.Type.STRING),
                                    "meal_time": content.Schema(type=content.Type.STRING),
                                },
                            ),
                            "side_dish": content.Schema(
                                type=content.Type.OBJECT,
                                properties={
                                    "name": content.Schema(type=content.Type.STRING),
                                    "calories": content.Schema(type=content.Type.NUMBER),
                                    "category": content.Schema(type=content.Type.STRING),
                                    "ingredients": content.Schema(
                                        type=content.Type.ARRAY,
                                        items=content.Schema(type=content.Type.STRING),
                                    ),
                                    "how_to_cook": content.Schema(type=content.Type.STRING),
                                    "meal_time": content.Schema(type=content.Type.STRING),
                                },
                            ),
                        },
                    ),
                },
            ),
        },
    ),
    "response_mime_type": "application/json",
}

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    # safety_settings can be adjusted here if needed
)

history = []

print("Bot: Hello! How can I assist you today?")

while True:
  
  user_input = input("You: ")
  
  # Start a chat session
  chat_session = model.start_chat(history=history)

  # Send a message and get a response
  response = chat_session.send_message(user_input)

  model_response = response.text
  
  print(f'Bot: {model_response}')
  print()
  
  history.append({"role": "user", "parts": [user_input]})
  history.append({"role": "model", "parts": [model_response]})
  