import asyncio
from fastapi import APIRouter
from backend.models import RunRequest, RunResponse
from backend.services.run_store import run_store
from backend.services.pipeline_runner import run_pipeline

router = APIRouter()

# Guard against duplicate pipeline runs for the same run_id
_running_runs: set = set()


async def _guarded_run(run_id: str, positions, pdf_path, max_retries):
    """Run the pipeline and clean up the guard set when done."""
    try:
        await run_pipeline(
            run_id=run_id,
            positions=positions,
            pdf_path=pdf_path,
            max_retries=max_retries,
        )
    finally:
        _running_runs.discard(run_id)


@router.post("/run", response_model=RunResponse)
async def run_pipeline_endpoint(request: RunRequest):
    if request.run_id in _running_runs:
        return RunResponse(run_id=request.run_id, status="already_running")
    _running_runs.add(request.run_id)

    state = run_store.get_state(request.run_id) or {}
    pdf_path = state.get("pdf_path")

    asyncio.create_task(_guarded_run(
        run_id=request.run_id,
        positions=request.positions,
        pdf_path=pdf_path,
        max_retries=request.max_retries,
    ))
    return RunResponse(run_id=request.run_id, status="started")


@router.get("/result/{run_id}")
async def get_result(run_id: str):
    state = run_store.get_state(run_id) or {}
    return {
        "compliance_summary": state.get("final_compliance_summary", "Pipeline completed successfully."),
        "calculated_metrics": state.get("calculated_metrics", []),
        "audit_flags": state.get("audit_flags", []),
        "validation_errors": state.get("validation_errors", []),
        "portfolio_inputs": state.get("portfolio_inputs", []),
    }
