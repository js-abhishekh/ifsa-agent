from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class UploadResponse(BaseModel):
    run_id: str
    file_path: str
    extracted_positions: List[Dict[str, Any]]
    extraction_status: str
    extraction_message: str
    is_demo: Optional[bool] = False

class RunRequest(BaseModel):
    run_id: str
    positions: List[Dict[str, Any]]
    max_retries: int = 2

class RunResponse(BaseModel):
    run_id: str
    status: str
