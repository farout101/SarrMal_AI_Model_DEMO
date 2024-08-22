# Importing the generativeai module from the google package.
import google.generativeai as genai
import streamlit as st

# Configuring the generativeai module to use gRPC (Google Remote Procedure Call) as the transport protocol.
genai.configure(transport='grpc')

# Loading the fine-tuned model using the specified model name.
model = genai.GenerativeModel(model_name=f'tunedModels/food-suggestion-ai-v1-uss801z982xp')

# Providing a prompt for the model to generate content based on.
prompt = """{
    "weight": 89,
    "height": 170,
    "age": 19,
    "diseases": ["Diabetes"],
    "allergies": ["None"],
    "gender": "Male",
    "exercise": "Moderate"
  }"""

prompt = '{"weight": 89, "height": 170, "age": 19, "diseases": ["Diabetes"], "allergies": ["None"], "gender": "Male", "exercise": "Moderate"}'

# Generating content using the loaded model and the provided prompt.
for x in range(10):
  result = model.generate_content(prompt)
  # Printing the generated content.
  print(result.text)
