import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client for Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def get_recipe(ingredients):
    prompt = (
        f"You are a helpful and creative chef. Suggest a unique and delicious recipe using only these ingredients: {ingredients}. "
        f"Include a recipe name, list of ingredients, and clear step-by-step instructions."
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

# Streamlit app layout
st.set_page_config(page_title="🍳 RecipeBot", page_icon="🥘")
st.title("🍽️ Groq-Powered Cooking Recipe Chatbot")
st.write("Enter your available ingredients below and get a delicious recipe suggestion!")

ingredients_input = st.text_input("🛒 Ingredients (comma-separated):", placeholder="e.g., milk, bread, egg")

if st.button("Get Recipe"):
    if ingredients_input.strip():
        with st.spinner("Cooking up something tasty..."):
            try:
                recipe = get_recipe(ingredients_input)
                st.markdown("## 👨‍🍳 Here's a recipe for you:")
                st.markdown(recipe)
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter some ingredients.")
