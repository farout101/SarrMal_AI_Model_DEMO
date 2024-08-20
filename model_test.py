"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import env
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=env.GEMINI_AI_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
  type = content.Type.OBJECT,
  properties = {
    "Breakfast": content.Schema(
      type = content.Type.OBJECT,
      properties = {
        "": content.Schema(
          type = content.Type.STRING,
        ),
      },
    ),
    "Lunch": content.Schema(
      type = content.Type.OBJECT,
      properties = {
        "": content.Schema(
          type = content.Type.STRING,
        ),
      },
    ),
    "Dinner": content.Schema(
      type = content.Type.OBJECT,
      properties = {
        "": content.Schema(
          type = content.Type.STRING,
        ),
      },
    ),
  },
),
"response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="tunedModels/food-suggestion-7n5tbcihkpat",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("""{
    "weight": 70,
    "height": 175,
    "age": 25,
    "diseases": ["None"],
    "allergies": ["Peanuts"],
    "gender": "Male",
    "exercise": "Moderate"
  }""")

print(response.text)