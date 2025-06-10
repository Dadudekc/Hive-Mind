from fastapi import FastAPI
from pydantic import BaseModel
from service import generate_blueprint

app = FastAPI()

class BlueprintRequest(BaseModel):
    project_description: str

@app.post("/architect/generate")
def architect_endpoint(request: BlueprintRequest):
    blueprint = generate_blueprint(request.project_description)
    return blueprint
