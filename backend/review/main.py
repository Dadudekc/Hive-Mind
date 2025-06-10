# backend/review/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from service import analyze_code

app = FastAPI()

class ReviewRequest(BaseModel):
    codebase: dict

@app.post("/review/analyze")
def review_endpoint(request: ReviewRequest):
    reviewed_code = analyze_code(request.codebase)
    return {"reviewed_code": reviewed_code}
