from fastapi import FastAPI, Request
import openai
import os

# Initialize FastAPI app
app = FastAPI()

# Set your OpenAI API Key from Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Basic test route to confirm the backend is working
@app.get("/")
def read_root():
    return {"message": "🚀 Coding Bot Backend is running!"}

# Route to generate code based on prompt
@app.post("/generate")
async def generate_code(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt", "")

    # Call OpenAI API to generate code
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use gpt-4 if preferred
        messages=[
            {"role": "system", "content": "You are a coding assistant. Generate code only."},
            {"role": "user", "content": user_prompt}
        ]
    )

    # Extract the generated code from the response
    code = response['choices'][0]['message']['content']
    return {"generated_code": code}
