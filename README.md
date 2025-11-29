# Cooking-Recipe-Chatbot
Cooking Recipe Chatbot — an interactive web app that generates recipe suggestions from user-provided ingredients. Built with Python, Streamlit, and the Groq API (OpenAI-compatible client). Includes prompt-engineered logic to turn ingredient lists into full recipe ideas and cooking instructions.

✅ Features

Accepts a list of ingredients from the user.

Returns recipe suggestions (dish ideas, ingredients mapping, step-by-step method).

Lightweight Streamlit UI for quick interaction.

Prompt-engineered templates for consistent, usable recipe outputs.

Secure handling of API keys using .env.

🧰 Tech Stack

Language: Python 3.8+

UI: Streamlit

API: Groq API (OpenAI-compatible client)

Env: python-dotenv

Libraries: requests / openai-compatible client or groq-client (adapt as used in project), pandas (optional), streamlit

📁 Files

(Adjust names to match your repo)

.
├─ app.py                 # Streamlit app entrypoint
├─ recipe_engine.py       # Prompt composition + API call logic
├─ requirements.txt       # Python dependencies
├─ .env.example           # Example environment variables
└─ README.md

🧩 Requirements

Python 3.8 or newer

An API key for the Groq API (or whichever OpenAI-compatible endpoint you're using)

(Optional) An OpenAI key if testing with OpenAI

Install dependencies:

pip install -r requirements.txt


requirements.txt example:

streamlit
python-dotenv
requests
# add groq-client or openai if used:
# groq-client
# openai

🔐 Environment Variables

Create a .env file in the repo root using .env.example as reference.

.env.example

GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here   # optional if using OpenAI or compatible fallback
MODEL_NAME=gpt-4o-mini                     # or the model name you use


Important: Never commit your .env or API keys to version control.

▶️ Run Locally

Clone repository:

git clone https://github.com/<your-username>/cooking-recipe-chatbot.git
cd cooking-recipe-chatbot


Install dependencies:

pip install -r requirements.txt


Create .env and add your keys:

cp .env.example .env
# then edit .env to add your keys


Start Streamlit:

streamlit run app.py


Open http://localhost:8501 in your browser.

🧪 Usage

Enter ingredients (comma-separated or one-per-line) in the input box.

Click Generate Recipe (or the app’s button).

The chatbot returns:

Recipe title(s)

Required ingredients & substitutions

Estimated prep/cook time

Step-by-step instructions

Optional serving and dietary notes

Example input:

chicken, garlic, onions, tomatoes, spinach

✍️ Prompt Engineering Notes

To keep results consistent and useful, the app uses a structured prompt template. Example pattern used in recipe_engine.py:

You are a helpful cooking assistant. Given the user's list of ingredients, produce:
1) A short recipe title.
2) A list of required ingredients and any recommended substitutes.
3) Estimated prep time and cook time.
4) Step-by-step instructions (numbered).
5) Serving size and any dietary notes.

User ingredients: {ingredients}
Constraints: use only the provided ingredients unless substitutions are requested. Keep steps concise and beginner-friendly.


Tips to improve outputs

Add temperature, cuisine, or dietary preference fields to the prompt for more specific recipes.

Use few-shot examples in the prompt (1–2 high-quality examples) to guide style.

Limit token length if you want shorter answers.

☁️ Deployment

You can deploy easily to Streamlit Community Cloud or any Python-capable host.

Streamlit Community Cloud

Push your repo to GitHub.

Create a new app on Streamlit Cloud and connect the GitHub repo.

Add your secrets (API keys) in the Streamlit dashboard (don’t add .env to the repo).

Other platforms

Heroku, Render, or any Dockerized service — ensure env vars set and streamlit run app.py is the start command.

🤝 Contributing

Contributions welcome! Ideas:

Add recipe ranking based on pantry items count.

Add image generation for final dish.

Support multi-step user clarifications (follow-up Q&A).

Add caching for repeated prompts to reduce API calls.

Please open issues or PRs with a clear description of changes.

📜 License

Add your chosen license here (e.g., MIT). Example:

MIT License
