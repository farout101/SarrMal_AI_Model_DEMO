# Creating the README.md file with the provided content

readme_content = """
# Streamlit Chatbot

This project is a simple chatbot built using Streamlit, integrated with OpenAI's API and Google's Gemini AI. The chatbot allows users to interact with AI models to get responses based on user input.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/farout101/Streamlit_ChatBot.git
    cd Streamlit_ChatBot
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```sh
    python -m venv chatbot-env
    source chatbot-env/bin/activate  # On Windows, use `chatbot-env\\Scripts\\activate`
    ```

3. **Install the Required Packages**:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Before running the chatbot, you need to configure your API keys. The chatbot can use either OpenAI's API or Google's Gemini AI, depending on your preference.

### Code Structure

Chatbot_With_Streamlit/
│
├── .gitignore
├── botv1.py
├── botv2.py
├── env.py
├── FoodSuggestion.py
├── model_test.py
├── notes.ipynb
├── README.md
├── requirements.txt
│
├── saves/
│ ├── client_secret_1.json
│ ├── client_secret_2.json
│ ├── client_secret_web.json
│ └── GoogleAuthentication.txt
│
└── pycache/

### Option 1: OpenAI API Key

1. **Set Up Environment Variables**:

    Create an `env.py` file in the project directory and add your OpenAI API key to it:

    ```python
    import os

    os.environ['OPENAI_API_KEY'] = 'your-openai-api-key'
    ```

    Alternatively, you can set the environment variable directly in your shell:

    ```sh
    export OPENAI_API_KEY='your-openai-api-key'
    ```

### Option 2: Google Gemini AI API Key

1. **Set Up Environment Variables**:

    Similarly, create an `env.py` file in the project directory and add your Gemini AI API key:

    ```python
    import os

    os.environ['GEMINI_AI_API_KEY'] = 'your-gemini-api-key'
    ```

    Or set the environment variable directly in your shell:

    ```sh
    export GEMINI_AI_API_KEY='your-gemini-api-key'
    ```

### Choosing Between OpenAI and Gemini AI

In the `bot.py` file, you can configure which API to use by setting the corresponding API key and adjusting the code to call the appropriate AI service. Ensure that you only set up the API key for the service you intend to use.

## Running the Chatbot

1. **Start the Streamlit Application**:

    ```sh
    streamlit run bot.py
    ```

    This will start a local server and open the Streamlit app in your default web browser.

2. **Using the Chatbot**:

    - Once the app is running, you can enter your queries in the text box provided, and the chatbot will respond based on the selected AI model.
    - If you've set up predefined prompts or custom instructions, you can select or modify these before sending your query.

## Additional Features

- **Predefined Prompts**: You can add predefined prompts that users can select from a dropdown menu. This is useful for common questions or specific instructions.
  
- **Custom Instructions**: Add custom instructions that the AI model will consider while generating responses. This can help guide the model's tone or response style.

- **Error Handling**: The application includes user-friendly error messages to guide you in case of issues such as API connection failures or invalid inputs.

## Troubleshooting

- If you encounter any issues with API keys, ensure they are correctly set in the environment variables and that they are valid.
- If the application fails to start, make sure that all dependencies are properly installed by running `pip install -r requirements.txt` again.

## Contributing

Feel free to submit issues or pull requests if you have improvements or bug fixes.
"""

# Save the content to a README.md file
with open("/mnt/data/README.md", "w") as file:
    file.write(readme_content)

# Credentials
The credentials for the OpenAI API and Google Gemini AI API are stored in the `env.py` file. You need to set up these credentials before running the chatbot.