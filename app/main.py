from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Boolean Query Generator",
    description="Generate a Boolean query for a job description",
    version="0.1.0",
)

app.include_router(router)
