# Importing the generativeai module from the google package.
import google.generativeai as genai

# Configuring the generativeai module to use gRPC (Google Remote Procedure Call) as the transport protocol.
genai.configure(transport='grpc')

# Loading the fine-tuned model using the specified model name.
model = genai.GenerativeModel(model_name=f'tunedModels/food-suggestion-ai-v1-uss801z982xp')

# Providing a prompt for the model to generate content based on.
prompt = """{
    "weight": 70,
    "height": 175,
    "age": 25,
    "diseases": ["None"],
    "allergies": ["Peanuts"],
    "gender": "Male",
    "exercise": "Moderate"
  }"""

# Generating content using the loaded model and the provided prompt.
result = model.generate_content(prompt)

# Printing the generated content.
print(result.text)