import openai
import os
from app.services.prompts import CLASSIFIER_PROMPT
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_job_description(job_description: str) -> str:
    """
    Classify a job description into one of the following categories:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": CLASSIFIER_PROMPT}, 
                  {"role": "user", "content": job_description}],
        temperature=0.0,
        max_tokens=10
    )
    category = response["choices"][0]["message"]["content"].strip()
    return category
