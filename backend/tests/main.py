# backend/tests/main.py
from fastapi import FastAPI
from models import CodeGenerationResult
from service import generate_tests

app = FastAPI()

@app.post("/tests/generate")
def generate_endpoint(code: CodeGenerationResult):
    test_cases = generate_tests(code.dict())
    return {"test_cases": test_cases}
