def generate_gemini_v3(prompt):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-suggestion-ai-v3-t2z0eh7qpaq8')
        result = model.generate_content(prompt)
        # response = json.loads(result.text)
        return result.text
    except json.JSONDecodeError as json_err:
        st.error("There was an error processing the response. Please try again later.")
        st.write(json_err)
        return None
    except Exception as e:
        st.error("An unexpected error occurred. Please try again.")
        st.write(e)
        return None