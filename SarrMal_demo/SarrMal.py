import streamlit as st
import google.generativeai as genai
import openai
import os
from components import chat_bots, image_searchings, food_suggestions, image_detection
from dotenv import load_dotenv
import json
import requests
from PIL import Image, ImageOps
from io import BytesIO

load_dotenv()

# Set your API keys
openai.api_key = os.environ.get("OPEN_AI_API_KEY")

# Function to generate a food suggestion using Gemini model
def generate_food_suggestion_gemini(prompt):
    return food_suggestions.generate_gemini_v3(prompt)

# Function to generate a food suggestion using OpenAI model
def generate_food_suggestion_openai(prompt):
    return food_suggestions.generate_openai(prompt)

# Function to web scrape images from Google or Unsplash
def fetch_food_image(food_name):
    if image_engine == "Google":
        return image_searchings.fetch_google(food_name)
    else:
        return image_searchings.fetch_unsplash(food_name)

# Old Function to load image from URL(this function has the issue of not being able to load some images, User Agent issue)
# def load_image(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#         content_type = response.headers['Content-Type']
        
#         # Check if the content is an image
#         if 'image' not in content_type:
#             st.warning("⚠️ The URL does not point to a valid image.")
#             return None
        
#         img = Image.open(BytesIO(response.content))
#         return img
#     except requests.exceptions.RequestException as e:
#         st.warning(f"😔 Oops! Failed to retrieve the web image.")
#         return None
#     except IOError as e:
#         st.warning(f"❌ Sorry, we couldn't open the image.")
#         return None

# Improved Function to load image from URL
def load_image(url):
    try:
        # Set the User-Agent to Chrome
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        content_type = response.headers['Content-Type']
        
        # Check if the content is an image
        if 'image' not in content_type:
            st.warning("⚠️ The URL does not point to a valid image.")
            return None
        
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        st.warning(f"😔 Oops! Failed to retrieve the web image. {e}")
        return None
    except IOError as e:
        st.warning(f"❌ Sorry, we couldn't open the image. {e}")
        return None

# Function to resize the image to a square shape
def resize_to_square(image, size=(512, 400)):
    return ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# Function to display the meal plan
def display_meal_plan(response):
    if response:
        st.subheader("Meal Plan")
        for meal_time, meal_info in response['response'].items():
            st.write(f"### {meal_time.capitalize()}")
            
            # Create two columns for main dish and side dish
            col1, col2 = st.columns(2)

            # Display main dish in the first column
            with col1:
                main_dish = meal_info.get("main_dish", {})
                if main_dish:
                    st.write(f"**Main Dish:** {main_dish.get('name')}")
                    image_url = fetch_food_image(main_dish.get('name'))
                    
                    if image_url:
                        # st.image(image_url, caption=main_dish.get('name'), use_column_width=True)
                        image = load_image(image_url)
                        if image:
                            square_img = resize_to_square(image)
                            st.image(square_img, caption=main_dish.get('name'), use_column_width=True)
                        # else:
                        #     st.write("🚫 Oops! No image found for this food.")
                        
                         
                    st.write(f"- Calories: {main_dish.get('calories')} kcal")
                    st.write(f"- Category: {main_dish.get('category')}")
                    
                    ingredients = ', '.join(main_dish.get('ingredients', []))
                    st.write(f"- Ingredients: {ingredients}")
                    
                    st.write(f"- How to Cook: {main_dish.get('how_to_cook')}")
                    st.write(f"- Meal Time: {main_dish.get('meal_time')}")
            
            # Display side dish in the second column
            with col2:
                side_dish = meal_info.get("side_dish", {})
                if side_dish:
                    st.write(f"**Side Dish:** {side_dish.get('name')}")
                    image_url = fetch_food_image(side_dish.get('name'))
                                        
                    if image_url:
                        # st.image(image_url, caption=side_dish.get('name'), use_column_width=True)
                        image = load_image(image_url)
                        if image:
                            square_img = resize_to_square(image)
                            st.image(square_img, caption=side_dish.get('name'), use_column_width=True)
                        # else:
                        #     st.write("🚫 Oops! No image found for this food.")
                            
                    st.write(f"- Calories: {side_dish.get('calories')} kcal")
                    st.write(f"- Category: {side_dish.get('category')}")
                    
                    ingredients = ', '.join(side_dish.get('ingredients', []))
                    st.write(f"- Ingredients: {ingredients}")
                    
                    st.write(f"- How to Cook: {side_dish.get('how_to_cook')}")
                    st.write(f"- Meal Time: {side_dish.get('meal_time')}")
            
            st.write("\n")


# Streamlit app layout
st.title("AI-Powered Food Suggestion System Demo")

# Sidebar for selecting functionality
functionality_choice = st.sidebar.selectbox(
    "Choose Functionality",
    ["Generate Meal Plan", "Chat about Food and Nutrition", "Search your own Food"]
)

# Toggle for selecting the AI model
model_choice = st.sidebar.radio("Choose the AI model", options=["SarrMal (Tuning)", "OpenAI (GPT-4)"])
st.sidebar.write("🌟 Please note that the OpenAI model is currently in beta and may occasionally produce results that are not entirely accurate.")
st.sidebar.write("🌟 Additionally, the format for ingredients may vary slightly between models.")
if st.sidebar.radio("Choose Image Generator", options=["Unsplash", "Google"]) == "Google":
    image_engine  = "Google"
    # st.write("Google Image Searching is Active.")
else:
    image_engine = "Unsplash"
    # st.write("Unsplash Image Searching is Active.")
st.sidebar.write("📓 Please note that the Google Image Generator is currently in beta and may occasionally produce results that are not entirely accurate.")


if functionality_choice == "Generate Meal Plan":
    st.write("Get personalized food suggestions!")
    if model_choice == "SarrMal (Tuning)":
        st.write("SarrMal (Tuning) model is Active.")
    else:
        st.write("OpenAI (GPT-4) model is Active.")
    # User input fields for generating the food suggestion prompt
    if image_engine == "Google":
        st.write("Google Image Searching is Active.")
    else:
        st.write("Unsplash Image Searching is Active.")
        
    st.subheader("Your Details")
    weight = st.number_input("Weight (kg)", min_value=1, max_value=300, value=70)
    height = st.number_input("Height (cm)", min_value=30, max_value=250, value=175)
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    exercise = st.selectbox("Exercise Level", ["None", "Light", "Moderate", "Intense"])
    diseases = st.multiselect("List any diseases", ["None", "Diabetes", "Hypertension"], default=["None"])
    allergies = st.multiselect("List any allergies", ["None", "Peanuts", "Shellfish", "Milk"], default=["None"])
    preferred_food = st.selectbox("Preferred Food", ["Burmese", "Chinese", "Western", "Japanese", "Korean", "Indian", "Other"])
    food_type = st.selectbox(
        "Food Type",
        [
            "Vegetarian",
            "Non-Vegetarian",
            "Balanced",
            "Other"
        ]
    )
    sugar_level = st.number_input("Sugar Level (mg/dL)", min_value=1, max_value=500, value=100)
    # Generate the prompt based on user input
    
    if sugar_level < 70:
        sugar_status = f"{food_type} (Increase sugar intake)"
    elif 70 <= sugar_level <= 99:
        sugar_status = f"{food_type} (Maintain normal sugar intake)"
    elif 100 <= sugar_level <= 125:
        sugar_status = f"{food_type} (Moderate sugar intake)"
    else:
        sugar_status = f"{food_type} (Low sugar option)"
        
    
    prompt = f"""{{
        "weight": {weight},
        "height": {height},
        "age": {age},
        "diseases": {diseases},
        "allergies": {allergies},
        "gender": "{gender}",
        "exercise": "{exercise}",
        "preferred": "{preferred_food}",
        "food-type": "{sugar_status}"
    }}"""


    #For Model1 and Model2    
    # prompt = f"""{{
    #     "weight": {weight},
    #     "height": {height},
    #     "age": {age},
    #     "diseases": [{', '.join([f'"{disease.strip()}"' for disease in diseases.split(',')])}],
    #     "allergies": [{', '.join([f'"{allergy.strip()}"' for allergy in allergies.split(',')])}],
    #     "gender": "{gender}",
    #     "exercise": "{exercise}",
    # }}"""

    st.write("### Your Preferences and Details")
    st.code(prompt)

    # Button to generate and display the food suggestion
    if st.button("Get Food Suggestion"):
        with st.spinner("Generating food suggestion..."):
            if model_choice == "SarrMal (Tuning)":
                response = generate_food_suggestion_gemini(prompt)
            else:
                response = generate_food_suggestion_openai(prompt)
            
            if response:
                display_meal_plan(response)
            else:
                st.warning("No response generated. Please check your input or try again later.")

elif functionality_choice == "Chat about Food and Nutrition":
    st.write("Food oriented chat session!")
    if model_choice == "SarrMal (Tuning)":
        st.write("SarrMal (Tuning) is Active.")
    else:
        st.write("OpenAI (GPT-4) is Active.")

    # Function to display chat messages
    def display_chat_message(role, message):
        with st.chat_message(role):
            st.write(message)

    # Initialize session state for chat history if not already initialized
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Container for chat messages
    chat_container = st.container()

    # User input
    user_input = st.text_input("You:", "")

    # Handle user input
    if st.button("Send"):
        if user_input:
            # Append user message to chat history
            st.session_state.chat_history.append({"role": "user", "message": user_input})

            # Generate response
            with st.spinner("Generating response..."):
                if model_choice == "SarrMal (Tuning)":
                    response = chat_bots.gemini_chat_oauth(user_input)
                else:
                    response = chat_bots.openai_chat(user_input)

            # Append AI response to chat history
            st.session_state.chat_history.append({"role": "assistant", "message": response})

            # Clear input field after sending
            # st.text_input("You:", "", key="user_input")

        else:
            st.warning("Please enter a message before sending.")

    # Display the entire chat history
    with chat_container:
        for message in st.session_state.chat_history:
            display_chat_message(message["role"], message["message"])

    # Button to clear the chat history
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        
# Old Placeholder Function
# elif functionality_choice == "Search your own Food":
#     st.write("Search for any food item!")
#     st.write("Image detection : OpenAI (GPT-4) is Active.(Fixed for this functionality)!")
#     st.write("Food suggestion : SarrMal (Tuning) is Active.(Fixed for this functionality)!")
    
#     # Option for user to upload an image or use the camera
#     upload_option = st.radio("Choose image source:", ("Upload from device", "Use camera", "Use Text(If the image is not available)"))
    
#     if upload_option == "Upload from device":
#         uploaded_image = st.file_uploader("Upload an image of the food item", type=["jpg", "jpeg", "png"])
#     elif upload_option == "Use camera":
#         uploaded_image = st.camera_input("Take a picture of the food item")
#     else:
#         uploaded_image = None
#         food_name = st.text_input("Enter the name of the food item", "")
    
#     if uploaded_image is not None:
#         # Display the uploaded image
#         st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        
#         # Encode and send the image to OpenAI API
#         base64_image = image_detection.encode_image(uploaded_image)
#         food_name = image_detection.get_food_name(base64_image)
        
#         # Display the result
#         if food_name:
#             st.write(f"The name of the food is: **{food_name}**")
#         else:
#             st.write("This is not recognized as a food item.")
            
elif functionality_choice == "Search your own Food":
    st.write("🍽️ **Search for any food item!**")
    st.write("🚀 Only SarrMal (Tuning) model is available for this functionality.")
    
    # Option for user to upload an image or use the camera
    upload_option = st.radio("📸 Choose image source:", ("Upload from device", "Use camera"))
    
    if upload_option == "Upload from device":
        uploaded_image = st.file_uploader("🖼️ Upload an image of the food item", type=["jpg", "jpeg", "png"])
    elif upload_option == "Use camera":
        uploaded_image = st.camera_input("📷 Take a picture of the food item")
    else:
        uploaded_image = None
        food_name = st.text_input("Enter the name of the food item", "")
    
    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption='📷 **Uploaded Image**', use_column_width=True)
        
        # Encode and send the image to the AI model
        base64_image = image_detection.encode_image(uploaded_image)
        food_name = image_detection.get_food_name(base64_image)
        
        # Get the response from the SarrMal Food Suggestion Model
        response = food_suggestions.suggestion_from_image(food_name)
        
        if response:
            st.markdown(f"**🍲 Food Name**: <span style='color:green'>{response.get('food_name')}</span>", unsafe_allow_html=True)
            st.markdown(f"**📏 Portion Size**: <span style='color:blue'>{response.get('portion_size')}</span>", unsafe_allow_html=True)
            st.markdown(f"**🔥 Calories Estimate**: <span style='color:red'>{response.get('calories_estimate')}</span>", unsafe_allow_html=True)
            st.markdown(f"**🏷️ Categories**: <span style='color:purple'>{', '.join(response.get('categories', []))}</span>", unsafe_allow_html=True)
            st.markdown(f"**🕒 Meal Time**: <span style='color:orange'>{', '.join(response.get('meal_time', []))}</span>", unsafe_allow_html=True)
            st.markdown(f"**🌍 Cuisine**: <span style='color:brown'>{response.get('cuisine')}</span>", unsafe_allow_html=True)
            st.markdown(f"**🛒 Ingredients**: <span style='color:darkblue'>{', '.join(response.get('ingredients', []))}</span>", unsafe_allow_html=True)
            
            st.write("**👨‍🍳 How to Cook:**")
            for step in response.get('how_to_cook', []):
                st.markdown(f"- {step} 🍴", unsafe_allow_html=True)
                
            st.write("**🍽️ Recommended Sides:**")
            for side in response.get('recommended_sides', []):
                st.markdown(f"- **{side['side_name']}**: _{side['description']}_", unsafe_allow_html=True)
                
            st.write("**🥤 Recommended Drinks:**")
            for drink in response.get('recommended_drinks', []):
                st.markdown(f"- **{drink['drink_name']}**: _{drink['description']}_", unsafe_allow_html=True)
                
            st.markdown(f"**📝 Notes**: <span style='color:gray'>{response.get('notes')}</span>", unsafe_allow_html=True)
        else:
            st.write("❌ This is not recognized as a food item.")