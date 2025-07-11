from pydantic import BaseModel

class JobDescriptionRequest(BaseModel):
    model_type: str
    job_description: str

class BooleanQueryResponse(BaseModel):
    boolean_query: str