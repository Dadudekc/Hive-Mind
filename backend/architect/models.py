from pydantic import BaseModel
from typing import List

class Blueprint(BaseModel):
    project: str
    modules: List[str]
    design: str
    tech_stack: List[str]
    scalability: str
