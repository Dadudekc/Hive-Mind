# backend/codegen/models.py
from pydantic import BaseModel
from typing import List

class Blueprint(BaseModel):
    project: str
    modules: List[str]
    design: str
    tech_stack: List[str]
    scalability: str

class CodeSnippet(BaseModel):
    module: str
    code: str

class CodeGenerationResult(BaseModel):
    """
    Represents the full code generation result as a list of code snippets.
    """
    codebase: List[CodeSnippet]
