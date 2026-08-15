from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from backend.routers import upload, run, stream

app = FastAPI(title="FRTB-SA Agent Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(run.router, prefix="/api", tags=["run"])
app.include_router(stream.router, prefix="/api", tags=["stream"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/data/uploads", StaticFiles(directory="data/uploads"), name="uploads")

@app.get("/")
def read_root():
    return {
        "message": "FRTB-SA Agent Backend is running.",
        "frontend_url": "http://localhost:3000",
        "api_docs": "/docs",
        "health_check": "/health"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
