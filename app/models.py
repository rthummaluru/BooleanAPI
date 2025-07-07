from pydantic import BaseModel

class JobDescriptionRequest(BaseModel):
    job_description: str

class BooleanQueryResponse(BaseModel):
    boolean_query: str