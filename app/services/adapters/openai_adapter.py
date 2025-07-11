from app.services.adapters.base_adapter import BaseAdapter
from app.services.prompts import INDUSTRY_PROMPTS
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

class OpenAIAdapter(BaseAdapter):
    """
    Adapter for OpenAI API.
    """
    def __init__(self, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
    
    def generate_boolean_query(self, job_description: str, industry: str) -> str:
        """
        Generate a recruiter-grade Boolean search string
        from a job description and industry.
        """
        industry_prompt = INDUSTRY_PROMPTS.get(industry, INDUSTRY_PROMPTS["IT"])
        user_prompt = f"Job description: {job_description}"
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": industry_prompt}, {"role": "user", "content": user_prompt}],
                max_tokens=500,
                temperature=0.0,
            )
        except Exception as e:
            raise RuntimeError(f"OpenAI API call failed: {e}")
        boolean_query = response.choices[0].message.content.strip()
        return boolean_query