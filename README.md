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

The AI models integrated into this demo are hosted and managed via Google Cloud. Due to this, direct access to the models is restricted, and only authorized users can utilize them. The models are secured with Google OAuth, ensuring that only those with the necessary credentials can execute and interact with the AI.

This approach is essential for maintaining the security and privacy of the data processed by the AI models. It also allows us to control and monitor who can access the models, preventing unauthorized usage.

Since the models are deployed on Google Cloud, users who wish to interact with them must have the appropriate OAuth credentials. Without these credentials, it won't be possible to access the full capabilities of the models.

## Displaying Images

For image searching, we initially used the Unsplash API; however, it didn't meet our accuracy requirements. As a result, we transitioned to the Google Custom Search API. This API provided more reliable results, but it came with a limitation: a restricted number of daily requests.

To work around this, we implemented a system that loops the API requests through multiple Google accounts. This approach allows us to handle a larger volume of requests while staying within the API's usage limits.

## About the Chat Bot

The final models integrated into the SarrMal app are:

- **Food_Suggestion_model_v3**: Responsible for generating food suggestions tailored to the user's input.
- **FINAL_FOOD_ANALYSIS_V1**: This model handles the transition from image to text. We utilized OpenAI's vision model through the OpenAI API to detect and analyze images, as the Gemini model does not support tuning for image-related tasks.

In scenarios where image detection fails or is unavailable, we've implemented a "fail-safe plan" that accepts direct text input, such as the food name, ensuring the system remains operational.

We chose not to train our AI models from scratch due to several constraints. Firstly, there is a lack of comprehensive datasets specifically tailored to our focus area. Secondly, even with a suitable dataset, the time available for AI model development was insufficient to achieve the desired level of accuracy. As a result, we opted to tune existing multi-modal models instead of building our own from the ground up.

## The Main Functionality of the Food Models

The primary goal of our AI models is to analyze the user's health information and provide personalized meal plans, particularly for individuals with diabetes and hypertension. These meal plans are designed to be reliable and tailored to the user's specific health needs.

This repository contains only the stripped-down version of our SarrMal AI models. You can check the full API version [OneBitMyanmar/SarrMal_API](https://github.com/One-Bit-Myanmar/api-for-sarrmal-app).

---

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
