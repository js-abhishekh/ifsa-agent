from fastapi import APIRouter, Request
import json
import asyncio
from sse_starlette.sse import EventSourceResponse
from backend.services.run_store import run_store

router = APIRouter()

@router.get("/stream/{run_id}")
async def stream_events(request: Request, run_id: str):
    queue = run_store.get_event_queue(run_id)

    if not queue:
        return EventSourceResponse(iter([]))

    async def event_generator():
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    # Wait up to 10s for a real event; send a ping if nothing arrives
                    event = await asyncio.wait_for(queue.get(), timeout=10.0)
                except asyncio.TimeoutError:
                    # Send a keepalive ping so the frontend knows we're still alive
                    yield {"event": "ping", "data": "{}"}
                    continue

                if event is None:
                    break
                yield {
                    "event": event.get("event", "message"),
                    "data": json.dumps(event)
                }
        except asyncio.CancelledError:
            pass

    return EventSourceResponse(event_generator())

