import os
import re  # For regular expression matching
import json  # For handling JSON data
from io import BytesIO  # For handling byte streams (e.g., file uploads)
import streamlit as st  # For creating Streamlit apps

from PIL import Image  # For image processing
import google.generativeai as genai  # For using the Gemini AI model



import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('X:\CURRENT PROJECTS\ChatBot_with_Streamlit\saves\\token.json'):
        creds = Credentials.from_authorized_user_file('X:\CURRENT PROJECTS\ChatBot_with_Streamlit\saves\\token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'X:\CURRENT PROJECTS\ChatBot_with_Streamlit\saves\client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('X:\CURRENT PROJECTS\ChatBot_with_Streamlit\saves\\token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


# Load environment variables from .env file
creds = load_creds()

# Configure the API key
genai.configure(credentials=creds)

# Import your model (replace this with your actual model instance)
GEMINI_PRO_1O5 = genai.GenerativeModel('gemini-1.5-pro')

# Regular expression pattern to extract JSON content from the response
PATTERN = r"```json(.*?)```"

def get_food_name(image: Image.Image):
    # Generate the response using the AI model
    response = GEMINI_PRO_1O5.generate_content([
        """give me result by following format
        
        ```json{
            "food_name": str
        }
        
        if the image is not food then return the following format
        json{
            "message": "short message"
        }
        """,
        image])

    # Get the content text from the response
    content_text = response.text
    print(content_text)

    # Clean the response by removing the JSON-like structure
    match = re.search(PATTERN, content_text, re.DOTALL)
    if match:
        # Extract the JSON string
        json_string = match.group(1)
        # Convert the string to a Python dictionary
        try:
            json_dict = json.loads(json_string)
            return json_dict
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON: {str(e)}")
    else:
        raise ValueError("No JSON-like content found in the response.")

def main():
    # Streamlit app setup
    st.title("Food Image Prediction")

    # File uploader for the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the uploaded image file
        image = Image.open(BytesIO(uploaded_file.read()))

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Use the model to predict the food ID and calories from the image
        try:
            result = get_food_name(image)
            st.write(result)  # Display the result in the Streamlit app
        except ValueError as e:
            st.error(f"Error: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
