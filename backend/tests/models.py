# backend/tests/models.py
from pydantic import BaseModel
from typing import List, Dict

class CodeSnippet(BaseModel):
    module: str
    code: str

class CodeGenerationResult(BaseModel):
    """
    Represents the full code generation result as a list of code snippets.
    """
    codebase: Dict[str, str]

class TestCase(BaseModel):
    module: str
    test_script: str
    description: str = "Placeholder test case for module"

class TestSuite(BaseModel):
    """
    Represents a collection of test cases.
    """
    tests: List[TestCase]
