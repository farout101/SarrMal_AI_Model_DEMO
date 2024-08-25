from pydantic import BaseModel, ValidationError
import openai
import json
from typing import List
import env

# Set your OpenAI API key
openai.api_key = env.OPENAI_API_KEY

class Dish(BaseModel):
    name: str
    calories: float
    category: str
    ingredients: List[str]
    how_to_cook: str
    meal_time: str

class Meal(BaseModel):
    main_dish: Dish
    side_dish: Dish

class ResponseModel(BaseModel):
    breakfast: Meal
    lunch: Meal
    dinner: Meal

class FullResponse(BaseModel):
    response: ResponseModel

def generate_meal_plan(input_message: dict) -> None:
    response = openai.ChatCompletion.create(
        model="gpt-4o-2024-08-06",
        messages=[
        {"role": "system", "content": "You are a meal planner AI, and you'll strictly need to respond with the JSON format that I provided earlier. THE OUTPUT IS JSON FORMAT"},
        {"role": "user", "content": """{
            "weight": 70,
            "height": 180,
            "age": 30,
            "diseases": ["None"],
            "allergies": ["None"],
            "gender": "Male",
            "exercise": "High"
        }"""},
        {"role": "assistant", "content": """{
        "response": {
            "breakfast": {
            "main_dish": {
                "name": "Oatmeal with Fresh Berries",
                "calories": 350,
                "category": "Healthy",
                "ingredients": ["Oats", "Milk", "Strawberries", "Blueberries", "Honey"],
                "how_to_cook": "Combine oats with milk and cook over medium heat until thickened. Top with fresh berries and a drizzle of honey.",
                "meal_time": "07:00 AM"
            },
            "side_dish": {
                "name": "Greek Yogurt with Almonds",
                "calories": 150,
                "category": "Protein",
                "ingredients": ["Greek Yogurt", "Almonds", "Honey"],
                "how_to_cook": "Top Greek yogurt with chopped almonds and a drizzle of honey.",
                "meal_time": "07:00 AM"
            }
            },
            "lunch": {
            "main_dish": {
                "name": "Grilled Chicken Salad",
                "calories": 450,
                "category": "Protein",
                "ingredients": ["Chicken Breast", "Mixed Greens", "Cherry Tomatoes", "Cucumber", "Olive Oil", "Lemon Juice"],
                "how_to_cook": "Grill chicken breast until fully cooked, then slice. Toss with mixed greens, cherry tomatoes, cucumber, and a dressing of olive oil and lemon juice.",
                "meal_time": "12:00 PM"
            },
            "side_dish": {
                "name": "Quinoa Salad",
                "calories": 200,
                "category": "Grain",
                "ingredients": ["Quinoa", "Black Beans", "Corn", "Red Bell Pepper", "Lime Juice", "Cilantro"],
                "how_to_cook": "Cook quinoa according to package instructions. Mix with black beans, corn, diced red bell pepper, lime juice, and cilantro.",
                "meal_time": "12:00 PM"
            }
            },
            "dinner": {
            "main_dish": {
                "name": "Baked Salmon",
                "calories": 500,
                "category": "Protein",
                "ingredients": ["Salmon Fillets", "Lemon", "Dill", "Olive Oil"],
                "how_to_cook": "Place salmon fillets on a baking sheet, brush with olive oil, and season with lemon and dill. Bake at 375°F (190°C) for 15-20 minutes.",
                "meal_time": "07:00 PM"
            },
            "side_dish": {
                "name": "Steamed Broccoli",
                "calories": 55,
                "category": "Vegetable",
                "ingredients": ["Broccoli Florets"],
                "how_to_cook": "Steam broccoli florets until tender, about 5 minutes. Season with a pinch of salt if desired.",
                "meal_time": "07:00 PM"
            }
            }
        }
        }"""},
        {"role": "user", "content": json.dumps(input_message)},
        {"role": "assistant", "content": "..."}
    ]
    )

    # Assuming the completion is in the response's 'choices' field
    completion_content = response['choices'][0]['message']['content']

    # Try to load the response as JSON first
    try:
        # Ensure that completion_content is valid JSON
        json_content = json.loads(completion_content)

        # Ensure that completion_content is valid JSON
        json_content = json.loads(completion_content)
        formatted_json = json.dumps(json_content, indent=4)
        print(formatted_json)

    except json.JSONDecodeError:
        print("The response is not valid JSON.")
        print("Received content:", completion_content)
    except ValidationError as e:
        print(f"Validation error: {e}")

# Example input message
input_message = {
    "weight": 50,
    "height": 120,
    "age": 10,
    "diseases": ["None"],
    "allergies": ["None"],
    "gender": "Male",
    "exercise": "High"
}

generate_meal_plan(input_message)