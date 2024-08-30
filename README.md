# SarrMal Demo (Stripped Down Version)

This repository contains a stripped-down version of the main functions from the SarrMal Demo API. It is designed for the demonstration of our tuned AI models.

## How to Use

To run the demo app, follow these instructions:

1. Clone the repository:
    ```bash
    git clone https://github.com/One-Bit-Myanmar/api-for-sarrmal-app
    ```
2. Navigate to the project directory:
    ```bash
    cd CHATBOT_WITH_STREAMLIT
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main app using Streamlit:
    ```bash
    streamlit run SarrMal_demo/components/SarrMal.py
    ```

This will start the application, and you can interact with the AI models through the Streamlit interface.

## The AI Models

The AI models integrated into this demo app are difficult to access directly because they are secured with Google OAuth. This was done to ensure that only authorized users can interact with the models, maintaining data security and integrity.

## Displaying Images

Initially, we used the Unsplash API for image searching, but due to its inaccuracy, we switched to the Google Custom Search API. However, the Google API has a limited number of daily requests, so we loop the API through multiple Google accounts to bypass this limitation.

## About the Chat Bot

The final models used in this SarrMal app include:

- **Food_Suggestion_model_v3**: This model is responsible for generating food suggestions based on user input.
- **FINAL_FOOD_ANALYSIS_V1**: Used in the transition between image and text. We leveraged OpenAI's vision model via the OpenAI API for image detection, as the Gemini model does not allow tuning for image models.

In case the image detection fails, we implemented a "fail-safe plan" that takes text input (food name) directly.

We decided not to train our AI models from scratch due to the lack of comprehensive datasets related to our focus area. Even if suitable datasets were available, the limited time frame for AI model development made it impractical. Instead, we opted to tune pre-existing multi-modal models.

## The Main Functionality of the Food Models

The primary goal of our models is to detect users' health information and provide reliable meal plans, specifically targeting individuals with diabetes and hypertension.

This repository contains only the stripped-down version of our SarrMal AI models. You can check the full API version [OneBitMyanmar/SarrMal_API](https://github.com/One-Bit-Myanmar/api-for-sarrmal-app).

---

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
