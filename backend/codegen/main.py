from fastapi import FastAPI
from models import Blueprint
from service import generate_code

app = FastAPI()

@app.post("/codegen/generate")
def codegen_endpoint(blueprint: Blueprint):
    codebase = generate_code(blueprint.dict())
    return {"codebase": codebase}
