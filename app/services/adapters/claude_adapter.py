from app.services.adapters.base_adapter import BaseAdapter
from app.services.prompts import INDUSTRY_PROMPTS
from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
class ClaudeAdapter(BaseAdapter):
    """
    Adapter for Claude API.
    """
    def __init__(self, model: str = "claude-3-5-sonnet-20240620"):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        
    def generate_boolean_query(self, job_description: str, industry: str) -> str:
        """
        Generate a recruiter-grade Boolean search string
        from a job description and industry.
        """
        industry_prompt = INDUSTRY_PROMPTS.get(industry, INDUSTRY_PROMPTS["IT"])
        user_prompt = f"Job description: {job_description}"

        response = self.client.messages.create(
            model=self.model,
            system=industry_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=500,
            temperature=0.0,
        )
        boolean_query = "claude: " + response.content[0].text
        return boolean_query