# backend/debugger/main.py
from fastapi import FastAPI
from models import CodeGenerationResult
from service import debug_code

app = FastAPI()

@app.post("/debugger/analyze")
def analyze_endpoint(code: CodeGenerationResult):
    debugged_code = debug_code(code.dict())
    return {"debugged_code": debugged_code}
