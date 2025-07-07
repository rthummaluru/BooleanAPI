from fastapi import APIRouter, HTTPException
from app.models import JobDescriptionRequest, BooleanQueryResponse
from app.services.classifier import classify_job_description
from app.services.query_generator import generate_query

router = APIRouter()

@router.post("/generate-query", response_model=BooleanQueryResponse)
async def generate_boolean_query_endpoint(request: JobDescriptionRequest):
    """
    Classify and generate a Boolean query for a job description.
    """
    try:
        # Classify the job description
        category = classify_job_description(request.job_description)
        print(f"Category: {category}")
        
        # Generate the Boolean query
        boolean_query = generate_query(request.job_description, category)
        return BooleanQueryResponse(boolean_query=boolean_query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))