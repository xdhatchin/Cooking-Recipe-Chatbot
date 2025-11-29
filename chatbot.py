import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file to get the API key
load_dotenv()

# Initialize OpenAI-compatible client for Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def get_recipe_suggestion(ingredients):
    prompt = (
        f"You are a helpful and creative chef. Suggest a unique and delicious recipe using only these ingredients: {ingredients}. "
        f"Include a recipe name, a list of ingredients needed, and clear step-by-step instructions."
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a friendly and helpful recipe assistant."},
            {"role": "user", "content": prompt}
        ],

        temperature=0.7
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🍳 Welcome to RecipeBot!")
    ingredients = input("🛒 Enter the ingredients you have (comma separated): ")
    print("\n🔍 Finding a recipe...\n")
    recipe = get_recipe_suggestion(ingredients)
    print("👨‍🍳 Here's a recipe you can try:\n")
    print(recipe)
