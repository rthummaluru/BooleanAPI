from pydantic import BaseModel

class JobDescription(BaseModel):
    job_description: str

class BooleanQueryResponse(BaseModel):
    boolean_query: str