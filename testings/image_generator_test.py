import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Unsplash API details
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")

# Function to fetch an image from Unsplash based on food name
def fetch_food_image(food_name):
    url = f"https://api.unsplash.com/search/photos?page=1&query={food_name}&client_id={UNSPLASH_ACCESS_KEY}&per_page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['small']  # Return the URL of the first image
        else:
            return None
    else:
        st.error(f"Error fetching image: {response.status_code}")
        return None

# Streamlit app layout
st.title("AI-Powered Food Suggestion Chatbot")

# User input field for food name
food_name = st.text_input("Enter Food Name")

if food_name:
    # Fetch and display the food image
    image_url = fetch_food_image(food_name)
    if image_url:
        st.image(image_url, caption=food_name, use_column_width=True)
    else:
        st.warning("No image found for the given food name.")
