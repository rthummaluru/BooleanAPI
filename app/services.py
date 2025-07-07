import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_boolean_query(job_description: str) -> str:
    """
    Generate a boolean query for a job description.
    """
    system_prompt = """
    You are a senior technical recruiter and Boolean search expert. Your task is to analyze any IT-related job description and generate a concise, precision-focused Boolean search string.

    OBJECTIVE:
        Create a Boolean search string that retrieves resumes containing only the most unique tools, platforms, or processes from the job description — the elements that directly signal candidate relevance.

    Do NOT include:
        - Job titles, experience levels, degrees, or certifications
        - Generic or implied skills (e.g., support, configuration, implementation)
        - Exclusion logic (e.g., NOT clauses)

    BOOLEAN RULES:
	    1.	Use AND to combine mandatory unique concepts.
	    2.	Use OR for synonyms, acronyms, or alternate spellings within each concept group.
	    3.	Use quotation marks "" for exact multi-word phrases.
        4.	Use wildcards * only when necessary to capture variants.
        5.	Limit the final query to 3–5 unique concept groups for maximum precision.

    OUTPUT FORMAT:
        Return a single-line Boolean string only. Do not include explanations or summaries. Example format:

        ("UniqueTool1" OR "Alias1") AND ("UniqueProcess1" OR "Alias2") AND ("UniquePlatform1" OR "Alias3")
    """

    user_prompt = f"Job description: {job_description}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    boolean_query = response["choices"][0]["message"]["content"].strip()
    return boolean_query