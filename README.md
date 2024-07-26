# Streamlit Chatbot

This project is a simple chatbot built using Streamlit and OpenAI's API. The chatbot allows users to interact with an AI model to get responses based on user input.

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
    source chatbot-env/bin/activate  # On Windows, use `chatbot-env\Scripts\activate`
    ```

3. **Install the Required Packages**:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Before running the chatbot, you need to configure your OpenAI API key.

1. **Set Up Environment Variables**:

    Create an `env.py` file in the project directory and add your OpenAI API key to it.

    ```python
    import os

    os.environ['OPENAI_API_KEY'] = 'your-openai-api-key'
    ```

    Alternatively, you can set the environment variable directly in your shell:

    ```sh
    export OPENAI_API_KEY='your-openai-api-key'
    ```

## Running the Chatbot

1. **Start the Streamlit Application**:

    ```sh
    streamlit run bot.py
    ```

    This will start a local server and open the Streamlit app in your default web browser.