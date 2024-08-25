"""
Install the Google AI Python SDK

$ pip install google-generativeai
$ pip install google.ai.generativelanguage
"""

import os
import env as env
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=env.GEMINI_AI_API_KEY)
# Create the model
generation_config = {
  "temperature": 0.1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    properties = {
      "response": content.Schema(
        type = content.Type.OBJECT,
        properties = {
          "breakfast": content.Schema(
            type = content.Type.OBJECT,
            properties = {
              "main_dish": content.Schema(
                type = content.Type.OBJECT,
                required = """["name", "calories", "category", "ingredients"]""",
                properties = {
                  "name": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "calories": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "category": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "how_to_cook": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "meal_time": content.Schema(
                    type = content.Type.STRING,
                  ),
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

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="I'll give you the JSON format of the user data.\nYou'll have to calculate the user's body condition and give us back the food suggestion with the provided format.\n{ weight: 70,    height: 175,    age: 25,    diseases: [None],    allergies: [Peanuts],    gender: Male,    exercise: Moderate}\nAll of the foods can be contain any food\nCalculate the health data accurately too.\nThe foods might be better if they have the health benefits.\nThe side dish can be bevarage too, but it doesn't mean it always has to be bevarage.\nAlways follow the format. I don't want any null value.",
)

print("the model is running")
chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)