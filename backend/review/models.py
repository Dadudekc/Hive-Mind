# backend/review/models.py
from pydantic import BaseModel
from typing import List

class CodeSnippet(BaseModel):
    module: str
    code: str

class CodeGenerationResult(BaseModel):
    """
    Represents the full code generation result as a list of code snippets.
    """
    codebase: List[CodeSnippet]
