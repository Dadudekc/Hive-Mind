# backend/debugger/models.py
from pydantic import BaseModel
from typing import List, Dict
import time

class CodeSnippet(BaseModel):
    module: str
    code: str

class CodeGenerationResult(BaseModel):
    """
    Represents the full code generation result as a list of code snippets.
    """
    codebase: Dict[str, str]

class DebugLog(BaseModel):
    module: str
    message: str
    timestamp: float = time.time()

class DebugReport(BaseModel):
    """
    Represents a debug report for a module including before/after code and logs.
    """
    module: str
    original_code: str
    debugged_code: str
    logs: List[DebugLog]
