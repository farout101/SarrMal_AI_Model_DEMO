# Function to fetch an image from Unsplash
import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
UNSPLASH_ACCESS_KEY_2 = os.environ.get("UNSPLASH_ACCESS_KEY_2")

# Function to fetch an image from Unsplash
# Unsplash API not as stable as Google Custom Search API, Used only as a fail safe
def fetch_unsplash(food_name):
    def get_image(api_key):
        url = f"https://api.unsplash.com/search/photos?page=1&query={food_name}%20food&client_id={api_key}&per_page=1"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                return data['results'][0]['urls']['small']
            else:
                return None
        else:
            return None

    # Try the first API key
    image_url = get_image(UNSPLASH_ACCESS_KEY)
    if image_url:
        return image_url
    
    # If the first key fails, try the second API key
    image_url = get_image(UNSPLASH_ACCESS_KEY_2)
    if image_url:
        return image_url
    else:
        st.warning("😥 Unable to fetch image with both API keys. Please try again later.")
        return None

# The main image searching function used in our API
def fetch_google(search_query):
    """
    Searches for an image using Google Custom Search API and returns the link to the first image result.

    Parameters:
    search_query (str): The search query string.

    Returns:
    str: The link to the first image result or a message if no results are found.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    search_engine_id = os.environ.get("SEARCH_ENGINE_ID")

    # We looped through multiple API keys to increase the chances of getting a result, as the API has a daily limit of 100 requests, now we have 600 requests per day xD
    api_keys = [
        os.environ.get("OAUTH_API_1"),
        os.environ.get("OAUTH_API_2"),
        os.environ.get("OAUTH_API_3"),
        os.environ.get("OAUTH_API_4"),
        os.environ.get("OAUTH_API_5"),
        os.environ.get("OAUTH_API_6")
    ]

    for api_key in api_keys:
        params = {
            'q': search_query,
            'key': api_key,
            'cx': search_engine_id,
            'searchType': 'image'
        }
        response = requests.get(url, params=params)
        # print(response)
        # print(response.text)
        if response.status_code == 200:
            result = response.json()
            if 'items' in result:
                return result['items'][0]['link']
            else:
                return {"error": "didn't find image"}
    return {"error": "something wrong with image searching server"}
