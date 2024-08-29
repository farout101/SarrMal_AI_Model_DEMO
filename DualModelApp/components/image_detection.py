import streamlit as st
import openai
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI with your API key
openai.api_key = os.environ.get("OPEN_AI_API_KEY")

def encode_image(image):
    return base64.b64encode(image.read()).decode("utf-8")

def get_food_name(base64_image):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "When I give you a food image, you'll have to return the name of the food. If it's not food, return nothing."},
            {"role": "user", "content": [
                {"type": "text", "text": "What is the name of this food? return ONLY THE NAME of the food, nothing more, nothing less. If it's not food, return error."},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"}
                }],
            }]
        )
    return response.choices[0].message['content']