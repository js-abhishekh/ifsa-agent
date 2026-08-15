from fastapi import APIRouter, UploadFile, File
import uuid
import shutil
from pathlib import Path
from backend.models import UploadResponse
from backend.services.pdf_extractor import extract_portfolio_from_pdf, use_sample_portfolio
from backend.services.run_store import run_store

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload-pdf", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    run_id = "RUN-" + uuid.uuid4().hex[:6].upper()
    file_path = UPLOAD_DIR / f"{run_id}.pdf"
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        positions, status, message = await extract_portfolio_from_pdf(str(file_path))
        
        if not positions:
            fallback_positions = use_sample_portfolio()
            if fallback_positions:
                positions = fallback_positions
                status = "fallback"
                message = message + " Falling back to predefined sample portfolio."
        
        run_store.create_run(run_id)
        run_store.set_state(run_id, {"pdf_path": str(file_path), "positions": positions})
        
        return UploadResponse(
            run_id=run_id,
            file_path=str(file_path),
            extracted_positions=positions,
            extraction_status=status,
            extraction_message=message
        )
    except Exception as e:
        return UploadResponse(
            run_id=run_id,
            file_path=str(file_path),
            extracted_positions=[],
            extraction_status="failed",
            extraction_message=str(e)
        )

@router.get("/sample-portfolio", response_model=UploadResponse)
async def get_sample_portfolio():
    run_id = "RUN-" + uuid.uuid4().hex[:6].upper()
    file_path = "data/raw_pdfs/PUNJAB NATIONAL BANK.pdf"
    
    try:
        positions, status, message = await extract_portfolio_from_pdf(file_path)
        
        if not positions:
            fallback_positions = use_sample_portfolio()
            if fallback_positions:
                positions = fallback_positions
                status = "fallback"
                message = message + " Falling back to predefined sample portfolio."
        
        run_store.create_run(run_id)
        run_store.set_state(run_id, {"pdf_path": file_path, "positions": positions})
        
        return UploadResponse(
            run_id=run_id,
            file_path=file_path,
            extracted_positions=positions,
            extraction_status=status,
            extraction_message=message,
            is_demo=True
        )
    except Exception as e:
        return UploadResponse(
            run_id=run_id,
            file_path=file_path,
            extracted_positions=[],
            extraction_status="failed",
            extraction_message=str(e),
            is_demo=True
        )
