from app.services.adapters.base_adapter import BaseAdapter
from app.services.prompts import INDUSTRY_PROMPTS
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types


load_dotenv()
class GeminiAdapter(BaseAdapter):
    """
    Adapter for Gemini API.
    """
    def __init__(self, model: str = "gemini-2.5-flash"):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = model
        
    def generate_boolean_query(self, job_description: str, industry: str) -> str:
        """
        Generate a recruiter-grade Boolean search string
        from a job description and industry.
        """
        industry_prompt = INDUSTRY_PROMPTS.get(industry, INDUSTRY_PROMPTS["IT"])
        user_prompt = f"Job description: {job_description}"
        response = self.client.models.generate_content(
            model=self.model,
            contents=[user_prompt],
            config=types.GenerateContentConfig(
                system_instruction=industry_prompt,
                temperature=0.0,
            ),
        )
        boolean_query = response.text.strip()
        return boolean_query