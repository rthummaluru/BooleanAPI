from fastapi import APIRouter, HTTPException
from app.models import JobDescriptionRequest, BooleanQueryResponse
from app.services import generate_boolean_query

router = APIRouter()

@router.post("/generate-query", response_model=BooleanQueryResponse)
async def generate_boolean_query_endpoint(request: JobDescriptionRequest):
    """
    Accepts a job description and returns a Boolean query for SQL full-text search.
    """
    try:
        boolean_query = await generate_boolean_query(request.job_description)
        return BooleanQueryResponse(boolean_query=boolean_query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))