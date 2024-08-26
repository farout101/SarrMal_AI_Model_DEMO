# Function to fetch an image from Unsplash
import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")

def fetch_unsplash(food_name):
    url = f"https://api.unsplash.com/search/photos?page=1&query={food_name} food&client_id={UNSPLASH_ACCESS_KEY}&per_page=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['small']
        else:
            return None
    else:
        st.error(f"Error fetching image: {response.status_code}")
        return None
    
def fetch_google(search_query):
    """
    Searches for an image using Google Custom Search API and returns the link to the first image result.

    Parameters:
    search_query (str): The search query string.

    Returns:
    str: The link to the first image result or a message if no results are found.
    """
    API_KEY = os.environ.get("OAUTH_API")
    SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'searchType': 'image'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        result = response.json()
        if 'items' in result:
            return result['items'][0]['link']
        else:
            return {"error": "didnt find image"}
    else:
        return {"error": "something wrong with image searching server"}