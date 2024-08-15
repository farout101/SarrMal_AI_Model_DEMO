import google.generativeai as genai
import os
import env

# Configuration
genai.configure(api_key=env.GEMINI_AI_API_KEY)
generation_config = {"temperature": 0.25, "max_output_tokens": 1024, "top_k": 40, "top_p": 0.95}

# Initialization
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

# Generate Content
response = model.generate_content("Write a short story about a brave knight who saves a princess from a dragon.")
print(response)