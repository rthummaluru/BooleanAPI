from openai import OpenAI
import os
from app.services.prompts import CLASSIFIER_PROMPT
from dotenv import load_dotenv

load_dotenv()
class Classifier:
    def __init__(self, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def classify_job_description(self, job_description: str) -> str:
        """
        Classify a job description into one of the following categories:
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": CLASSIFIER_PROMPT}, 
                    {"role": "user", "content": job_description}],
            temperature=0.0,
            max_tokens=10
        )
        category = response.choices[0].message.content.strip()
        return category
