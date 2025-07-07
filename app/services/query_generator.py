import openai
import os
from dotenv import load_dotenv
from app.services.prompts import INDUSTRY_PROMPTS

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_query(job_description: str, category: str) -> str:
    """
    Generate a Boolean query for a job description based on the category.
    """
    industry_prompt = INDUSTRY_PROMPTS.get(category, INDUSTRY_PROMPTS["IT"])
    user_prompt = f"Job description: {job_description}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": industry_prompt}, {"role": "user", "content": user_prompt}],
        temperature=0.0,
        max_tokens=1000
    )
    boolean_query = response["choices"][0]["message"]["content"].strip()
    return boolean_query