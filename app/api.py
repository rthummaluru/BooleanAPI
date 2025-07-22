from fastapi import APIRouter, HTTPException
from app.models import JobDescriptionRequest, BooleanQueryResponse
from app.services.classifier import Classifier
from app.services.model_manager import ModelManager
import logging

router = APIRouter()
classifier = Classifier()
logging.basicConfig(level=logging.INFO)

@router.post("/generate-query", response_model=BooleanQueryResponse)
async def generate_boolean_query_endpoint(request: JobDescriptionRequest):
    """
    Classify and generate a Boolean query for a job description.
    """
    logging.info(f"Received API request")
    try:
        logging.info(f"Classifying job description")
        # Classify the job description
        industry = classifier.classify_job_description(request.job_description)
        print(f"Industry: {industry}")

        logging.info(f"Initializing model manager")
        # Initialize the model manager
        model_manager = ModelManager(request.model_type)
        adapter = model_manager.get_adapter()

        logging.info(f"Generating Boolean query")
        # Generate the Boolean query
        boolean_query = adapter.generate_boolean_query(request.job_description, industry)
        return BooleanQueryResponse(boolean_query=boolean_query)
        logging.info(f"Boolean query generated successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))